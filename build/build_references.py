"""Build ba-orchestrator reference files (method cards, task indexes, taxonomy, search index).

Method text is copied from the repaired method table and the English translation of mind map 8.
Only two things change: line breaks are added (before numbered steps and bullets), and the
attribution scrub list in scrub.py is applied. When several source descriptions are merged into one
card, they appear as neutral variants (Variant A, B, ...). verify_references.py checks that nothing
else was lost.
"""
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

TASK_EN = {
    "T1": "Strategy Analysis and Justification",
    "T2": "Situation Investigation and Elicitation",
    "T3": "Stakeholders",
    "T4": "Modelling and Analysis",
    "T5": "Requirements Specification",
    "T6": "Prioritisation and Requirements Management",
    "T7": "Validation and Acceptance",
    "T8": "Change Deployment and Solution Evaluation",
}
SUB_EN = {
    "1.1": "External Environment and Market Analysis", "1.2": "Strategy, Goals and Measures",
    "1.3": "Current State, Capabilities and Gaps", "1.4": "Solution Options and Feasibility", "1.5": "Business Case",
    "2.1": "Problem and Scope Framing", "2.2": "Root Cause Analysis", "2.3": "Boundaries and Context",
    "2.4": "Domain, Document and Data Research", "2.5": "Interviews, Questionnaires and Individual Techniques",
    "2.6": "Group and Creative Sessions", "2.7": "Observation and Immersion",
    "2.8": "Prototypes and Scenarios for Elicitation",
    "3.1": "Stakeholder Identification", "3.2": "Stakeholder Analysis and Mapping",
    "3.3": "Engagement, Conflict and Negotiation",
    "4.1": "Business Processes and User Work", "4.2": "Data and Concepts", "4.3": "Behaviour and Interactions",
    "4.4": "Goals, Obstacles and Rationale", "4.5": "Decomposition and Systems Analysis", "4.6": "Architecture Analysis",
    "5.1": "User Stories and Story Mapping", "5.2": "Use Cases and Scenarios", "5.3": "User Interface",
    "5.4": "Business Rules and Decision Logic", "5.5": "Non-Functional Requirements",
    "5.6": "Requirements Documents and Phrasing", "5.7": "Specification by Example and Acceptance Criteria",
    "5.8": "Formal Specification",
    "6.1": "Prioritisation", "6.2": "Backlog, Estimation and Release Planning",
    "6.3": "Organisation, Baselines and Reuse", "6.4": "Traceability and Status",
    "6.5": "Requirements Change Management", "6.6": "Requirements Risk and Process Improvement",
    "7.1": "Reviews and Inspections", "7.2": "Prototypes, Animation and Usability",
    "7.3": "Formal Model Verification", "7.4": "Testing and Acceptance",
    "8.1": "Organisational Change", "8.2": "People and Learning", "8.3": "Benefits and Outcome Evaluation",
}
FIELDS = ["Problem Solved", "Uncertainty Reduced", "BA Lifecycle Phase", "Input Artifacts", "Output Artifacts",
          "Participants & Roles", "Prerequisites", "Step-by-Step Procedure", "Analyst Questions & Prompts",
          "Minimal Realistic Example", "Quality Criteria & Verification", "Errors & Anti-Patterns",
          "When NOT to Use", "Alternatives & Complementary Methods", "Supported Decisions", "AI & Agentic Adaptation"]


def slugify(s):
    s = s.lower().replace("&", " and ").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def record(ref):
    return MM8[ref] if isinstance(ref, str) else ROWS[ref]


def fmt(text):
    t = scrub(text.strip())
    t = re.sub(r"\s*•\s*", "\n• ", t).lstrip("\n")
    t = re.sub(r"(?<=[.;:)\]'\"])\s+(?=\d{1,2}\.\s)", "\n", t)
    return t


def first_sentence(text, limit):
    t = " ".join(scrub(text).split())
    m = re.match(r"(.+?[.;])(\s|$)", t)
    s = m.group(1) if m and len(m.group(1)) <= limit else t
    return s if len(s) <= limit else s[: limit - 1].rsplit(" ", 1)[0] + "…"


def main():
    (REF / "methods").mkdir(parents=True, exist_ok=True)
    (REF / "tasks").mkdir(parents=True, exist_ok=True)
    for old in list((REF / "methods").glob("*.md")) + list((REF / "tasks").glob("*.md")):
        old.unlink()  # regenerate from scratch so renamed methods leave no stale cards
    index, slugs = [], set()
    tree = ["# BA Task Taxonomy", "",
            "Task → subtask → methods. Each method links to its card in `methods/`. "
            "Use the task files in `tasks/` for one-line selection guidance (problem solved / when not to use).", ""]
    for tid, _, sublist in TAXONOMY:
        tname = TASK_EN[tid]
        tfile = f"{tid}-{slugify(tname)}.md"
        tlines = [f"# {tid}. {tname}", "",
                  "Selection guide: each line shows what the method solves and when NOT to use it "
                  "(first variant; open the card for every variant's full text).", ""]
        tree.append(f"## {tid}. {tname} — [task guide](tasks/{tfile})")
        for sid, _, mlist in sublist:
            sname = SUB_EN[sid]
            tlines += [f"## {sid} {sname}", ""]
            tree.append(f"- **{sid} {sname}**: " + ", ".join(
                f"[{name}](methods/{slugify(name)}.md)" for name, _ in mlist))
            for name, refs in mlist:
                slug = slugify(name)
                assert slug not in slugs, slug
                slugs.add(slug)
                recs = [record(r) for r in refs]
                aliases = sorted({scrub(r["Method Name"].strip()) for r in recs} - {name})
                card = ["---", f"id: {slug}", f"name: \"{name}\"", f"task: {tid}", f"task_name: \"{tname}\"",
                        f"subtask: \"{sid}\"", f"subtask_name: \"{sname}\"",
                        f"source_count: {len(recs)}", "---", "",
                        f"# {name}", "", f"`{tid} {tname} › {sid} {sname}`", ""]
                if aliases:
                    card += ["**Also described as:** " + "; ".join(aliases), ""]
                multi = len(recs) > 1
                if multi:
                    card += [f"This card merges {len(recs)} descriptions of the method, labelled Variant A–"
                             f"{chr(64 + len(recs))} in every field.", ""]
                for f in FIELDS:
                    vals = [(f"Variant {chr(65 + i)}", rec[f]) for i, rec in enumerate(recs) if rec.get(f, "").strip()]
                    if not vals:
                        continue
                    card += [f"## {f}", ""]
                    for tag, v in vals:
                        if multi:
                            card += [f"**[{tag}]**", ""]
                        card += [fmt(v), ""]
                (REF / "methods" / f"{slug}.md").write_text("\n".join(card).rstrip() + "\n", encoding="utf-8")
                prob = first_sentence(recs[0]["Problem Solved"], 220)
                notfor = first_sentence(recs[0]["When NOT to Use"], 170)
                tlines.append(f"- [{name}](../methods/{slug}.md) — {prob} *Not for:* {notfor}")
                j = lambda k: scrub(" ".join(r.get(k, "") for r in recs).strip())
                index.append({
                    "id": slug, "name": name, "task": tid, "task_name": tname, "subtask": sid, "subtask_name": sname,
                    "aliases": aliases, "variants": len(recs), "path": f"references/methods/{slug}.md",
                    "phases": sorted({p.strip().lower() for r in recs for p in re.split(r"[/,;]", r["BA Lifecycle Phase"]) if p.strip()}),
                    "problem": j("Problem Solved"), "uncertainty": j("Uncertainty Reduced"),
                    "when_not": j("When NOT to Use"), "outputs": j("Output Artifacts"), "decisions": j("Supported Decisions"),
                })
            tlines.append("")
        (REF / "tasks" / tfile).write_text("\n".join(tlines).rstrip() + "\n", encoding="utf-8")
        tree.append("")
    (REF / "taxonomy.md").write_text("\n".join(tree).rstrip() + "\n", encoding="utf-8")
    (REF / "methods-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"methods: {len(index)}, task files: {len(TAXONOMY)}")


main()
