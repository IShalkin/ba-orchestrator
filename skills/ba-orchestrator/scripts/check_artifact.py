#!/usr/bin/env python3
"""Deterministic conformance check for ba-orchestrator outputs (run by the orchestrator, not the model).

Usage:
  python check_artifact.py artifact RUN_DIR/03-artifacts/<id>/artifact.md --run-dir RUN_DIR
  python check_artifact.py research RUN_DIR/02-research/<id>.md
  python check_artifact.py review   RUN_DIR/05-review/<id>.md

Checks the formats in references/artifact-conventions.md. For artifacts it also checks that every
[E:id] exists in the run's research logs, that linked companion files exist, and that the Summary
stays within budget (WARN above 300 words, ERROR above 360). Exit 0 = conforms (warnings may print),
1 = errors. An error tagged FORM-ONLY (Summary over the limit, a missing artifact heading other than Summary
and Output) needs only that fix on relaunch; the result line says FAIL FORM-ONLY when every error is
form-only. A missing or empty Summary or Output is a content error: the executor did not finish.
For research logs, the Evidence table is read by its header (| id | source | locator | url | date | quote |):
every row needs a quote and a url that is an http(s) URL, a file path, or "n/a: <reason>". A v0.3 header
without url is a WARN, so an older run can be resumed.
It checks form and evidence references only, NOT whether the content is right; that is the critic's job.
"""
import argparse, ipaddress, json, re, sys
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

EID = re.compile(r"\[E:([A-Za-z0-9._-]+)\]")
LABELS = {"E": EID, "ASSUMPTION": re.compile(r"\[ASSUMPTION\]"), "GAP": re.compile(r"\[GAP\]"),
          "METHOD": re.compile(r"\[METHOD\]")}
ART_SECTIONS = ["Summary", "Purpose and decision supported", "Procedure log", "Output", "Assumptions",
                "Open questions", "Self-check"]
ART_KEYS = ["method", "scope", "source_variant", "inputs", "status"]
SUMMARY_MAX_WORDS = 300
SUMMARY_HARD_MAX_WORDS = 360
CONTENT_SECTIONS = ("Summary", "Output")
UNSEARCHED = re.compile(r"GAP\W*not\s+(?:yet\s+)?searched|needs\s+staging", re.I)
FORM = "FORM-ONLY "


def headings(text):
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]


def section(text, name):
    m = re.search(rf"^##\s+{re.escape(name)}[^\n]*\n(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


EVIDENCE_COLS = ["id", "source", "locator", "url", "date", "quote"]
LEGACY_COLS = ["id", "source", "locator", "date", "quote"]
URL_RELEASE = (0, 4, 0)
URL_LIKE = re.compile(r"ur[il]|link|href|web|address|permalink", re.I)
PLACEHOLDER = re.compile(r"\.\.\.|…|<|>|(?:^|[/\\=?&#:.])(?:tbd|tbc|todo|none|null|unknown|placeholder|xxx+|n/a)(?:$|[/\\.?&#])",
                         re.I)
NA_OK = re.compile(r"n/a:\s*(?!(?:<[^>]*>|\.\.\.|…|tbd|tbc|todo|none|null|unknown|placeholder|reason|why|n/a|-+|\?+)\s*$)\S.*",
                   re.I)


def is_url(cell):
    """An http(s) URL with a real host (a dotted name, an IPv4 address or localhost) that is not a template or a truncation: no <...>
    or {...} slot, no path segment that is only an ellipsis, no trailing ellipsis. Words such as TODO or none in a path
    or query are real ("/display/TODO/", "?status=none", "compare/v1.0...v2.0" all pass)."""
    m = re.fullmatch(r"https?://([^/\s?#:@]+)(?::\d+)?(?:[/?#]\S*)?", cell or "")
    if not m or re.search(r"[<>{}]", cell) or re.search(r"(?:\.\.\.|…)$|/(?:\.\.\.|…)(?:[/?#]|$)", cell):
        return False
    host = m.group(1).lower()
    if PLACEHOLDER.search("/" + host):
        return False
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        pass
    return host == "localhost" or bool(re.fullmatch(r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}", host))


def is_path(cell):
    r"""A local path: absolute (/, ~/, ./, ../, C:\ or C:/, \\server, file://) with at least one real segment, or
    relative with a file extension or a trailing slash. "n/a", "TBD/", "/none", "//" and "and/or" never pass."""
    c = cell or ""
    if "://" in c and not c.lower().startswith("file://"):
        return False
    rest = c[7:] if c.lower().startswith("file://") else c
    segs = [x for x in re.split(r"[/\\]", rest) if x not in ("", "~", ".", "..")]
    if not segs or PLACEHOLDER.search("/" + rest) or re.fullmatch(r"[A-Za-z]:", segs[0]) and len(segs) == 1:
        return False
    if re.match(r"(?:file://|~?[/\\]|\.{1,2}[/\\]|[A-Za-z]:[/\\])", c):
        return True
    if not re.search(r"[/\\]", c):
        return bool(re.fullmatch(r"[^\s|]+\.[A-Za-z]\w*", c))
    return c.endswith(("/", "\\")) or bool(re.search(r"\.\w+$", segs[-1]))


def url_ok(cell):
    return is_url(cell) or bool(NA_OK.fullmatch(cell or "")) or is_path(cell)


def head_name(cell):
    """A header cell as a column name: lower-case, a bracketed suffix dropped ("URL (web)" -> "url")."""
    return re.sub(r"\s+", " ", re.sub(r"\(.*?\)|\[.*?\]", "", cell)).strip().lower()


def run_release(run_dir):
    """The release recorded in RUN_DIR/status.json: a tuple, (0, 3, 0) for a run that predates the field, None
    when there is no status.json (a log checked outside a run is held to the current format)."""
    p = Path(run_dir) / "status.json" if run_dir else None
    if not p or not p.exists():
        return None
    try:
        rel = (json.loads(p.read_text(encoding="utf-8")).get("skill_version") or {}).get("release") or "0.3.0"
        return tuple(int(x) for x in re.findall(r"\d+", rel)[:3])
    except (ValueError, OSError):
        return None


def cells_of(line):
    """Cells of a markdown table row; an escaped \\| stays inside its cell."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def evidence_table(text):
    """(header, rows) of the ## Evidence table, read by HEADER position so a column added or moved never shifts
    another. header is the lower-cased cells of the first row with an "id" cell (None when there is no such
    row); rows are (line, {column: cell}) for every data row. Cells beyond the header width join the last
    column (an unescaped | inside a trailing quote). Without a header, cells are keyed by position (0, 1, ...)."""
    header, rows = None, []
    for line in section(text, "Evidence").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = cells_of(line)
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        low = [head_name(c) for c in cells]
        if header is None and "id" in low:
            header = low
            continue
        if low == header:
            continue
        if header:
            width = len(cells)
            if len(cells) > len(header):
                cells = cells[:len(header) - 1] + [" | ".join(cells[len(header) - 1:])]
            row = {h: (cells[i] if i < len(cells) else "") for i, h in enumerate(header)}
            row[WIDTH] = width
            rows.append((line, row))
        else:
            rows.append((line, dict(enumerate(cells))))
    return header, rows


WIDTH = 0


def row_id(row):
    return row["id"] if "id" in row else row.get(0, "")


def evidence_ids(research_text):
    return [i for _, r in evidence_table(research_text)[1] if re.fullmatch(r"[A-Za-z0-9._-]+", i := row_id(r))]


def check_artifact(path, run_dir):
    err, warn = [], []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        err.append("missing YAML frontmatter")
    else:
        fm = text.split("---", 2)[1]
        for k in ART_KEYS:
            if not re.search(rf"^{k}:", fm, re.M):
                err.append(f"frontmatter key missing: {k}")
    hs = headings(text)
    for s in ART_SECTIONS:
        if s in CONTENT_SECTIONS:
            if not section(text, s).strip():
                err.append(f"section missing or empty: ## {s} (the executor did not finish; relaunch for content)")
        elif not any(h.startswith(s) for h in hs):
            err.append(f"{FORM}section missing: ## {s}")
    if hs and not hs[0].startswith("Summary"):
        warn.append("## Summary should be the first section")
    words = len(section(text, "Summary").split())
    if words > SUMMARY_HARD_MAX_WORDS:
        err.append(f"{FORM}Summary has {words} words (max {SUMMARY_MAX_WORDS}, hard limit {SUMMARY_HARD_MAX_WORDS})")
    elif words > SUMMARY_MAX_WORDS:
        warn.append(f"Summary has {words} words (target {SUMMARY_MAX_WORDS}, hard limit {SUMMARY_HARD_MAX_WORDS})")
    counts = {k: len(p.findall(text)) for k, p in LABELS.items()}
    if sum(counts.values()) == 0:
        err.append("no evidence labels at all")
    used = set(EID.findall(text))
    research = sorted((run_dir / "02-research").glob("*.md")) if run_dir else []
    known = set()
    for r in research:
        known |= set(evidence_ids(r.read_text(encoding="utf-8")))
    missing = sorted(used - known)
    if missing:
        err.append(f"[E:] ids not found in any research log: {missing[:15]}{' ...' if len(missing) > 15 else ''}")
    for target in re.findall(r"\]\((?!https?:)([^)#\s]+)\)", text):
        if not (path.parent / target).exists():
            err.append(f"linked companion missing: {target}")
    return err, warn, counts


def check_research(path, run_dir=None):
    err, warn = [], []
    text = path.read_text(encoding="utf-8")
    hs = headings(text)
    for s in ("Findings by research question", "Evidence"):
        if s not in hs:
            err.append(f"section missing: ## {s}")
    if not re.search(r"^Sources searched:", text, re.M):
        err.append("line missing: Sources searched:")
    header, table = evidence_table(text)
    quote_at = header.index("quote") if header and "quote" in header else None
    width = len(header) if header else 0
    if (header is None or "url" not in header) and (rel := run_release(run_dir or path.parent.parent)) \
            and rel < URL_RELEASE:
        quote_at, width = -1, 0
    rows = {l for l, _ in table}

    def scanned(l):
        if l not in rows or quote_at is None:
            return l
        cells = cells_of(l)
        if quote_at == -1:
            at = 5 if len(cells) >= 6 and url_ok(cells[3]) and not re.match(r"\d{4}", cells[3]) else 4
            return "|".join(cells[:at] + cells[at + 1:])
        return "|".join(cells[:quote_at] + ([] if quote_at == width - 1 else cells[quote_at + 1:]))
    hits = UNSEARCHED.findall("\n".join(scanned(l) for l in text.splitlines()))
    unsearched = sorted(set(hits))
    if unsearched:
        err.append(f"{len(hits)} unanswered marker(s) {unsearched} left: the researcher "
                   "stopped early or a source needs staging; stage it if needed and relaunch with PREVIOUS LOG")
    ids = evidence_ids(text)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        err.append(f"duplicate evidence ids: {dup}")
    release = run_release(run_dir or path.parent.parent)
    old_run = release is not None and release < URL_RELEASE
    renamed = [h for h in header or [] if h not in EVIDENCE_COLS and URL_LIKE.search(h)]
    if old_run and (header is None or "url" not in header) and not renamed:
        if table:
            warn.append(f"legacy evidence table without a url column, accepted because this run started under "
                        f"{'.'.join(map(str, release))}; new logs use | {' | '.join(EVIDENCE_COLS)} |")
        for line, _ in table:
            cells = cells_of(line)
            if len(cells) < 5 or not cells[4]:
                err.append(f"evidence row needs 5 columns incl. quote: {line[:80]}")
            elif len(cells) >= 6 and url_ok(cells[3]) and not re.match(r"\d{4}", cells[3]):
                err.append(f"evidence row {cells[0]} looks like a v0.4 row (url in the 4th cell) under a v0.3 header: "
                           "use the current header for the whole table")
    elif table and header is None:
        err.append(f"evidence table has no header row (| {' | '.join(EVIDENCE_COLS)} |)")
    elif header:
        legacy = "url" not in header
        need = LEGACY_COLS if legacy else EVIDENCE_COLS
        absent = [c for c in need if c not in header]
        if absent:
            err.append(f"evidence table header lacks column(s) {absent} (expected | {' | '.join(EVIDENCE_COLS)} |)")
        if legacy and renamed:
            err.append(f"evidence table has a url column under another name {renamed}: name it url")
        elif legacy:
            err.append(f"evidence table has no url column (required from {'.'.join(map(str, URL_RELEASE))}; "
                       f"header: | {' | '.join(EVIDENCE_COLS)} |)")
        for line, r in table:
            if not r.get("quote"):
                err.append(f"evidence row needs {len(header)} columns incl. a non-empty quote: {line[:80]}")
            if not legacy and not url_ok(r.get("url", "")):
                err.append(f"evidence row {row_id(r)}: url {r.get('url', '')[:60]!r} is not an http(s) URL with a "
                           "real host, a file path, or 'n/a: <reason>' (placeholders such as https://... or TBD fail)")
    cited = set(EID.findall(section(text, "Findings by research question")))
    orphan = sorted(cited - set(ids))
    if orphan:
        err.append(f"findings cite ids not in the evidence table: {orphan}")
    return err, warn, {"evidence_rows": len(ids)}


def check_review(path):
    err, warn = [], []
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^Verdict:\s*(PASS|REVISE)\b", text, re.M)
    if not m:
        err.append("line missing: 'Verdict: PASS' or 'Verdict: REVISE'")
    if not any(h.startswith("Defects") for h in headings(text)):
        err.append("section missing: ## Defects")
    return err, warn, {"verdict": m.group(1) if m else None}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["artifact", "research", "review"])
    ap.add_argument("path")
    ap.add_argument("--run-dir")
    a = ap.parse_args()
    p = Path(a.path)
    if a.kind == "artifact" and p.is_dir():
        p = p / "artifact.md"
    if not p.exists():
        print(f"ERROR file not found: {p}")
        sys.exit(1)
    if a.kind == "artifact":
        run = Path(a.run_dir) if a.run_dir else p.parent.parent.parent
        err, warn, info = check_artifact(p, run)
    elif a.kind == "research":
        err, warn, info = check_research(p, a.run_dir)
    else:
        err, warn, info = check_review(p)
    for w in warn:
        print("WARN ", w)
    for e in err:
        print("ERROR", e)
    result = "OK" if not err else "FAIL FORM-ONLY" if all(e.startswith(FORM) for e in err) else "FAIL"
    print(f"{result} {a.kind} {p.name} {info} warnings={len(warn)}")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
