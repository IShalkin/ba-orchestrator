"""Verify the generated ba-orchestrator references against the source data. Exit 1 on any failure."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# source data lives in ../data in the published repo, or in ../ (the extraction workspace)
EXTRACTED = next(p for p in (HERE.parent / "data", HERE.parent) if (p / "taxonomy.py").exists())
SKILL = Path(sys.argv[1]).resolve()
REF = SKILL / "references"
exec((EXTRACTED / "taxonomy.py").read_text(encoding="utf-8"))
exec((HERE / "mm8_en.py").read_text(encoding="utf-8"))
exec((HERE / "scrub.py").read_text(encoding="utf-8"))
ROWS = json.loads((EXTRACTED / "framework-table1.repaired.json").read_text(encoding="utf-8"))
slugify = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower().replace("&", " and ").replace("'", "")).strip("-")
norm = lambda s: re.sub(r"[\s•]", "", s)
fails = []

# 1. every source field value appears verbatim (modulo whitespace) in the right card
checked = 0
for tid, _, sl in TAXONOMY:
    for sid, _, ml in sl:
        for name, refs in ml:
            card = (REF / "methods" / f"{slugify(name)}.md").read_text(encoding="utf-8")
            nc = norm(card)
            for r in refs:
                rec = MM8[r] if isinstance(r, str) else ROWS[r]
                for k, v in rec.items():
                    if k == "Source" or not v.strip():
                        continue
                    checked += 1
                    if norm(scrub(v)) not in nc:
                        fails.append(f"lost text: {name} <- row {r} field {k!r}")
            for f in ("id:", "task:", "subtask:", "source_count:", "## Problem Solved", "## Step-by-Step Procedure"):
                if f not in card:
                    fails.append(f"card {name} missing {f}")
rows_total = sum(1 for _ in ROWS) + len(MM8)
print(f"1) source field values checked: {checked} (from {rows_total} source records)")

# 2. links in taxonomy and task guides resolve; every card is linked
linked = set()
for md in [REF / "taxonomy.md", *sorted((REF / "tasks").glob("*.md"))]:
    for target in re.findall(r"\]\(([^)#]+)\)", md.read_text(encoding="utf-8")):
        p = (md.parent / target).resolve()
        if not p.exists():
            fails.append(f"broken link in {md.name}: {target}")
        if p.parent.name == "methods":
            linked.add(p.name)
cards = {p.name for p in (REF / "methods").glob("*.md")}
print(f"2) cards on disk: {len(cards)}, linked from indexes: {len(linked & cards)}, orphan cards: {sorted(cards - linked)}")
fails += [f"orphan card {c}" for c in cards - linked]

# 3. search index consistent with cards
idx = json.loads((REF / "methods-index.json").read_text(encoding="utf-8"))
ids = {e["id"] + ".md" for e in idx}
print(f"3) index entries: {len(idx)}, match cards: {ids == cards}")
if ids != cards:
    fails.append("index/cards mismatch")

# 4. no author / book attribution left in any generated file
AUTH = re.compile(r"\b(Adzic|Cadle|Robertson|Lamsweerde|Clements|Kazman|Cockburn|IIBA|BABOK|Lauesen|Beus-Dukic|Armour|Blais|Nicieja|Frisendal|Wiegers|Hokanson|Beatty|Pohl|Rupp|Patton|Meyer|Gilb|NotebookLM|MindMap8)\b")
gen = [*(REF / "methods").glob("*.md"), *(REF / "tasks").glob("*.md"), REF / "taxonomy.md", REF / "methods-index.json"]
hits = [(g.name, m.group(0)) for g in gen for m in AUTH.finditer(g.read_text(encoding="utf-8"))]
print(f"4) author/book attributions in generated files: {len(hits)}")
fails += [f"attribution left: {h}" for h in hits[:20]]

print("RESULT:", "PASS" if not fails else f"FAIL ({len(fails)})")
for f in fails[:40]:
    print("  ", f)
sys.exit(1 if fails else 0)
