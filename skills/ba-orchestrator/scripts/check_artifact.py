#!/usr/bin/env python3
"""Deterministic conformance check for ba-orchestrator outputs (run by the orchestrator, not the model).

Usage:
  python check_artifact.py artifact RUN_DIR/03-artifacts/<id>/artifact.md --run-dir RUN_DIR
  python check_artifact.py research RUN_DIR/02-research/<id>.md
  python check_artifact.py review   RUN_DIR/05-review/<id>.md

Checks the formats in references/artifact-conventions.md. For artifacts it also checks that every
[E:id] exists in the run's research logs, that linked companion files exist, and that the Summary
stays within budget. Exit 0 = conforms (warnings may print), 1 = errors.
It checks form and evidence references only, NOT whether the content is right; that is the critic's job.
"""
import argparse, re, sys
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


def headings(text):
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]


def section(text, name):
    m = re.search(rf"^##\s+{re.escape(name)}[^\n]*\n(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def evidence_ids(research_text):
    ev = section(research_text, "Evidence")
    ids = []
    for line in ev.splitlines():
        m = re.match(r"^\|\s*([A-Za-z0-9._-]+)\s*\|", line)
        if m and m.group(1).lower() != "id" and not set(m.group(1)) <= set("-:"):
            ids.append(m.group(1))
    return ids


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
        if not any(h.startswith(s) for h in hs):
            err.append(f"section missing: ## {s}")
    if hs and not hs[0].startswith("Summary"):
        warn.append("## Summary should be the first section")
    words = len(section(text, "Summary").split())
    if words > SUMMARY_MAX_WORDS:
        err.append(f"Summary has {words} words (max {SUMMARY_MAX_WORDS})")
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


def check_research(path):
    err, warn = [], []
    text = path.read_text(encoding="utf-8")
    hs = headings(text)
    for s in ("Findings by research question", "Evidence"):
        if s not in hs:
            err.append(f"section missing: ## {s}")
    if not re.search(r"^Sources searched:", text, re.M):
        err.append("line missing: Sources searched:")
    ids = evidence_ids(text)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        err.append(f"duplicate evidence ids: {dup}")
    for line in section(text, "Evidence").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and cells and cells[0] not in ("id",) and not set(cells[0]) <= set("-:"):
            if len(cells) < 5 or not cells[4]:
                err.append(f"evidence row needs 5 columns incl. quote: {line[:80]}")
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
    if not p.exists():
        print(f"ERROR file not found: {p}")
        sys.exit(1)
    if a.kind == "artifact":
        run = Path(a.run_dir) if a.run_dir else p.parent.parent.parent
        err, warn, info = check_artifact(p, run)
    elif a.kind == "research":
        err, warn, info = check_research(p)
    else:
        err, warn, info = check_review(p)
    for w in warn:
        print("WARN ", w)
    for e in err:
        print("ERROR", e)
    print(f"{'FAIL' if err else 'OK'} {a.kind} {p.name} {info}")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
