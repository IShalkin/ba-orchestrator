#!/usr/bin/env python3
"""Stage an .xlsx workbook as markdown, one file per sheet (stdlib zipfile + xml, no openpyxl).

Usage:
  python stage_sheet.py BOOK.xlsx OUT_DIR

Writes OUT_DIR/<book-stem>/NN-<sheet>.md per sheet, in workbook order: sheet name, state (visible, hidden,
veryHidden), the used range, then a table whose first column is the spreadsheet row number and whose header
is the column letters (row 1 of the sheet is a data row, so a header row is never guessed or dropped).
Cells: shared strings, inline strings, formula string results, booleans, errors and numbers as stored
(dates are serial numbers; cached formula values are used, formulas are not evaluated; a formula with no
cached value is written as "=<formula>"). OUT_DIR/<book-stem>/ must be absent or empty.
Exit 0 = staged, 1 = unreadable workbook.
"""
import argparse, os, re, sys, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def col_index(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n


def col_letters(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def shared_strings(z):
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    out = []
    for si in root.findall(M + "si"):
        skip = {t for ph in si.findall(M + "rPh") for t in ph.iter(M + "t")}
        out.append("".join(t.text or "" for t in si.iter(M + "t") if t not in skip))
    return out


def cell_value(c, sst):
    t, v = c.get("t", "n"), c.find(M + "v")
    if t == "inlineStr":
        is_ = c.find(M + "is")
        return "".join(x.text or "" for x in is_.iter(M + "t")) if is_ is not None else ""
    if v is None or v.text is None:
        f = c.find(M + "f")  # a workbook not last saved by a spreadsheet app may carry no cached value
        return f"={f.text}" if f is not None and f.text else ""
    if t == "s":
        return sst[int(v.text)]
    if t == "b":
        return "TRUE" if v.text == "1" else "FALSE"
    return v.text  # n, str (formula string), e (error), d (ISO date)


def sheets(z):
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = {r.get("Id"): r.get("Target") for r in
            ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).iter(PR + "Relationship")}
    for s in wb.iter(M + "sheet"):
        t = rels[s.get(RID)]
        part = t.lstrip("/") if t.startswith("/") else os.path.normpath("xl/" + t).replace(os.sep, "/")
        yield s.get("name"), s.get("state", "visible"), part


def cell(v):
    return v.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")


def sheet_md(z, name, state, part, sst):
    root = ET.fromstring(z.read(part))
    rows, maxc = [], 0
    rn = 0
    for r in root.iter(M + "row"):
        vals, ci = {}, 0
        rn = int(r.get("r") or rn + 1)  # r is optional in the format: fall back to position
        for c in r.findall(M + "c"):
            ci = col_index(c.get("r")) if c.get("r") else ci + 1
            v = cell_value(c, sst)
            if v != "":
                vals[ci] = v
        if vals:
            rows.append((rn, vals))
            maxc = max(maxc, max(vals))
    dim = root.find(M + "dimension")
    lines = [f"# Sheet: {name}", "", f"- state: {state}", f"- used range: {dim.get('ref') if dim is not None else '?'}",
             f"- non-empty rows: {len(rows)}", ""]
    if rows:
        lines += ["| row | " + " | ".join(col_letters(i) for i in range(1, maxc + 1)) + " |",
                  "|---|" + "---|" * maxc]
        lines += [f"| {n} | " + " | ".join(cell(vals.get(i, "")) for i in range(1, maxc + 1)) + " |"
                  for n, vals in rows]
    else:
        lines.append("(empty sheet)")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", type=Path)
    ap.add_argument("out_dir", type=Path)
    a = ap.parse_args()
    out = a.out_dir / a.book.stem
    if out.exists() and any(out.iterdir()):
        sys.exit(f"ERROR: {out} is not empty; staging into it would mix versions. Remove it or choose another OUT_DIR")
    written = []
    try:
        with zipfile.ZipFile(a.book) as z:
            sst = shared_strings(z)
            out.mkdir(parents=True, exist_ok=True)
            for n, (name, state, part) in enumerate(sheets(z), 1):
                p = out / f"{n:02d}-{re.sub(r'[^A-Za-z0-9._-]+', '_', name).strip('_') or 'sheet'}.md"
                p.write_text(sheet_md(z, name, state, part, sst), encoding="utf-8")
                written.append(p)
                print(f"sheet {n}: {name} ({state})")
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError, IndexError, ValueError) as e:
        sys.exit(f"ERROR: cannot read {a.book}: {e}")
    for p in written:
        print(f"{p.stat().st_size:>10}  {p}")


if __name__ == "__main__":
    main()
