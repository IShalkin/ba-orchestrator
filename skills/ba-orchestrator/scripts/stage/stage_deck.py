#!/usr/bin/env python3
"""Stage a .pptx deck for researchers: a text layer and a rendered PNG per slide, hidden slides included.

Usage:
  python stage_deck.py DECK.pptx OUT_DIR [--render auto|libreoffice|powerpoint|none] [--pdf FILE] [--dpi N]

Writes OUT_DIR/<deck-stem>/:
  slide-NNN.md    slide number, HIDDEN flag, text of the slide's own shapes (paragraphs in shape order; SmartArt,
                  chart and embedded-object text is only in the render) and speaker notes
  deck.pdf        the export, every slide unhidden first (unless --render none)
  slide-NNN.png   one per page, when a rasteriser is available (pdftoppm, or pypdfium2 + Pillow)

Renderers, detected at runtime: LibreOffice (`soffice`, hidden slides exported by filter option), or on
macOS Microsoft PowerPoint through osascript (it is brought to the foreground, every slide is unhidden on
a temporary copy, the copy is closed without saving; the source is never opened). --pdf uses an existing
export instead. The slide count is ALWAYS compared with the page count and a mismatch fails: an export can
drop hidden slides silently. No rasteriser: the PDF is written and the script says so (exit 0).
OUT_DIR/<deck-stem>/ must be absent or empty, so a re-staged deck never mixes with an older version.

Exit 0 = staged, 1 = failure (renderer missing when requested, export failed, count mismatch).
Stdlib only; the renderer and rasteriser are optional external tools.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile, zipfile, zlib
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "rel": "http://schemas.openxmlformats.org/package/2006/relationships"}
RID = "{%s}id" % NS["r"]
T, BR = "{%s}t" % NS["a"], "{%s}br" % NS["a"]


class StageError(Exception):
    pass


def rels(z, part):
    """Relationship id -> (type suffix, target part name) for a part."""
    p = PurePosixPath(part)
    rp = str(p.parent / "_rels" / (p.name + ".rels"))
    if rp not in z.namelist():
        return {}
    out = {}
    for r in ET.fromstring(z.read(rp)).findall("rel:Relationship", NS):
        t = r.get("Target")
        target = t.lstrip("/") if t.startswith("/") else os.path.normpath(str(p.parent / t)).replace(os.sep, "/")
        out[r.get("Id")] = (r.get("Type").rsplit("/", 1)[-1], target)
    return out


FLD = "{%s}fld" % NS["a"]
AUTO_FIELDS = ("slidenum", "datetime")


def paragraphs(elem):
    out = []
    for para in elem.iter("{%s}p" % NS["a"]):
        auto = {id(t) for f in para.iter(FLD) if (f.get("type") or "").lower().startswith(AUTO_FIELDS) for t in f.iter(T)}
        t = "".join("\n" if x.tag == BR else x.text or "" for x in para.iter()
                    if x.tag in (T, BR) and id(x) not in auto).strip()
        if t:
            out.append(t)
    return out


def notes_text(z, part):
    """Speaker notes: the body placeholders of the notes slide (skips slide image and number fields)."""
    root = ET.fromstring(z.read(part))
    out = []
    for sp in root.iter("{%s}sp" % NS["p"]):
        ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if ph is not None and ph.get("type") == "body":
            out += paragraphs(sp)
    return out


def read_deck(path):
    """[{n, part, hidden, text: [..], notes: [..]}] in presentation order."""
    with zipfile.ZipFile(path) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        prels = rels(z, "ppt/presentation.xml")
        slides = []
        for i, sid in enumerate(pres.findall("p:sldIdLst/p:sldId", NS), 1):
            part = prels[sid.get(RID)][1]
            root = ET.fromstring(z.read(part))
            notes = [t for kind, t in rels(z, part).values() if kind == "notesSlide"]
            slides.append({"n": i, "part": part, "hidden": root.get("show") in ("0", "false"),
                           "text": paragraphs(root), "notes": notes_text(z, notes[0]) if notes else []})
    if not slides:
        raise StageError("no slides in presentation.xml")
    return slides


def slide_md(s, deck):
    head = f"# {deck} - slide {s['n']}" + (" (HIDDEN)" if s["hidden"] else "")
    meta = f"- slide: {s['n']}\n- hidden: {'yes' if s['hidden'] else 'no'}\n- part: {s['part']}"
    return "\n\n".join([head, meta, "## Text (slide shapes only; SmartArt and charts are in the render)", *(s["text"] or ["(no text)"]),
                         "## Speaker notes", *(s["notes"] or ["(none)"])]) + "\n"


def pdf_page_count(data):
    """Count /Type /Page objects outside streams, plus those inside object streams (/ObjStm, Flate or uncompressed).
    Other stream payloads (page content, fonts, images) are never scanned: their bytes can hold the literal."""
    pat = re.compile(rb"/Type\s*/Page(?![a-zA-Z])")
    stream = re.compile(rb"stream\r?\n(.*?)\r?\nendstream", re.S)
    n = len(pat.findall(stream.sub(b"", data)))
    for m in stream.finditer(data):
        if b"/ObjStm" not in data[data.rfind(b"obj", 0, m.start()):m.start()]:
            continue
        try:
            body = zlib.decompress(m.group(1))
        except zlib.error:
            body = m.group(1)
        n += len(pat.findall(body))
    return n


def check_counts(slides, pages, what="page"):
    if slides != pages:
        raise StageError(f"COUNT MISMATCH: deck has {slides} slides, export has {pages} {what}s. "
                         "An export can drop hidden slides; do not stage this render.")


def renderer_available(name):
    if name == "libreoffice":
        return bool(shutil.which("soffice") or shutil.which("libreoffice"))
    return sys.platform == "darwin" and bool(shutil.which("osascript")) and (
        Path("/Applications/Microsoft PowerPoint.app").exists())


def render_libreoffice(deck, out_pdf):
    if not renderer_available("libreoffice"):
        return False
    exe = shutil.which("soffice") or shutil.which("libreoffice")
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / ("deck" + deck.suffix)
        shutil.copyfile(deck, src)
        fmt = 'pdf:impress_pdf_Export:{"ExportHiddenSlides":{"type":"boolean","value":"true"}}'
        r = subprocess.run([exe, f"-env:UserInstallation={Path(tmp, 'profile').as_uri()}", "--headless",
                            "--convert-to", fmt, "--outdir", tmp, str(src)], capture_output=True, text=True,
                           timeout=600)
        pdf = Path(tmp) / "deck.pdf"
        if r.returncode or not pdf.exists():
            raise StageError(f"LibreOffice export failed: {r.stderr.strip() or r.stdout.strip()}")
        shutil.move(str(pdf), out_pdf)
    return True


PPT_SCRIPT = '''on run argv
  set src to item 1 of argv
  set dst to item 2 of argv
  tell application "Microsoft PowerPoint"
    activate
    open (POSIX file src)
    set pres to active presentation
    repeat with s in slides of pres
      set hidden of slide show transition of s to false
    end repeat
    save pres in (POSIX file dst as string) as save as PDF
    close pres saving no
  end tell
end run'''


def render_powerpoint(deck, out_pdf):
    if not renderer_available("powerpoint"):
        return False
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / ("deck" + deck.suffix)
        shutil.copyfile(deck, src)
        r = subprocess.run(["osascript", "-e", PPT_SCRIPT, str(src), str(out_pdf.resolve())],
                           capture_output=True, text=True, timeout=600)
        if r.returncode or not out_pdf.exists():
            raise StageError(f"PowerPoint export failed (a stale PowerPoint process often causes -9074): "
                             f"{r.stderr.strip()}")
    return True


def rasterise(pdf, out_dir, dpi):
    """Write slide-NNN.png per page; return the list, or None when no rasteriser is available."""
    if shutil.which("pdftoppm"):
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(Path(tmp, "p"))],
                               capture_output=True, text=True)
            if r.returncode:
                raise StageError(f"pdftoppm failed: {r.stderr.strip()}")
            pages = sorted(Path(tmp).glob("p-*.png"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
            out = []
            for i, p in enumerate(pages, 1):
                out.append(Path(shutil.move(str(p), out_dir / f"slide-{i:03d}.png")))
            return out
    try:
        import pypdfium2, PIL
    except ImportError:
        return None
    doc, out = pypdfium2.PdfDocument(str(pdf)), []
    for i, page in enumerate(doc, 1):
        p = out_dir / f"slide-{i:03d}.png"
        page.render(scale=dpi / 72).to_pil().save(p)
        out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--render", choices=["auto", "libreoffice", "powerpoint", "none"], default="auto")
    ap.add_argument("--pdf", type=Path, help="use this existing export instead of rendering")
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    try:
        slides = read_deck(a.deck)
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError, StageError) as e:
        sys.exit(f"ERROR: cannot read {a.deck}: {e}")
    out = a.out_dir / a.deck.stem
    if out.exists() and any(out.iterdir()):
        sys.exit(f"ERROR: {out} is not empty; staging into it would mix versions. Remove it or choose another OUT_DIR")
    order = [] if a.pdf or a.render == "none" else ["libreoffice", "powerpoint"] if a.render == "auto" else [a.render]
    if order and not any(map(renderer_available, order)):
        sys.exit(f"ERROR: no renderer available ({' or '.join(order)}); install LibreOffice, or pass "
                 "--pdf with an export that includes hidden slides, or --render none")
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for s in slides:
        p = out / f"slide-{s['n']:03d}.md"
        p.write_text(slide_md(s, a.deck.name), encoding="utf-8")
        written.append(p)
    hidden = [s["n"] for s in slides if s["hidden"]]
    print(f"{len(slides)} slides, hidden: {hidden or 'none'}")
    status = 0
    try:
        pdf = out / "deck.pdf"
        if a.pdf:
            shutil.copyfile(a.pdf, pdf)
        elif a.render == "none":
            pdf = None
        else:
            fn = {"libreoffice": render_libreoffice, "powerpoint": render_powerpoint}
            if not any(fn[r](a.deck, pdf) for r in order):
                raise StageError(f"no renderer available ({' or '.join(order)}); install LibreOffice, or pass "
                                 "--pdf with an export that includes hidden slides, or --render none")
        if pdf:
            written.append(pdf)
            pngs = rasterise(pdf, out, a.dpi)
            if pngs is None:
                print("NOTE: no rasteriser (pdftoppm, or pypdfium2 + Pillow); wrote the PDF only")
                check_counts(len(slides), pdf_page_count(pdf.read_bytes()))
            else:
                written += pngs
                check_counts(len(slides), len(pngs), "rendered page")
    except (StageError, OSError, subprocess.TimeoutExpired) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        status = 1
    for p in written:
        print(f"{p.stat().st_size:>10}  {p}")
    sys.exit(status)


if __name__ == "__main__":
    main()
