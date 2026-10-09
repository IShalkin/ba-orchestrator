#!/usr/bin/env python3
"""Rank BA method cards for a problem statement.

Usage:
  python find_methods.py "conflicting stakeholder priorities on scope" [--task T6] [--subtask 6.1]
                         [--phase elicitation] [--top 10] [--json]

Scores name/aliases highest, then problem + uncertainty text, then outputs and supported decisions.
Matching is keyword-based (no embeddings): rephrase with the vocabulary of the method cards
if results look off, and always read the shortlisted cards before choosing.
"""
import argparse, json, math, re, sys
from collections import Counter
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

INDEX = Path(__file__).resolve().parent.parent / "references" / "methods-index.json"
STOP = set("a an and are as at be by for from how in into is it its of on or that the this to under we what when "
           "where which who why with without our their".split())
WEIGHTS = {"name": 3.0, "problem": 2.0, "outputs": 1.0, "decisions": 1.0}


def stem(w):
    # Truncation stemmer: "priorities"/"prioritization" -> "priori", "qualities"/"quality" -> "qualit".
    w = w[:-1] if w.endswith("s") and len(w) > 4 else w
    return w[:6]


def tokens(text):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) >= 3]


def fields(e):
    return {
        "name": e["name"] + " " + " ".join(e["aliases"]),
        "problem": e["problem"] + " " + e.get("uncertainty", ""),
        "outputs": e["outputs"],
        "decisions": e["decisions"],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query")
    ap.add_argument("--task", help="T1..T8")
    ap.add_argument("--subtask", help="e.g. 2.5")
    ap.add_argument("--phase", help="substring of a lifecycle phase, e.g. elicitation")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    pool = [e for e in idx
            if (not a.task or e["task"] == a.task.upper())
            and (not a.subtask or e["subtask"] == a.subtask)
            and (not a.phase or any(a.phase.lower() in p for p in e["phases"]))]
    docs = [{k: Counter(tokens(v)) for k, v in fields(e).items()} for e in idx]
    df = Counter(t for d in docs for t in set().union(*d.values()))
    idf = {t: math.log(1 + len(idx) / c) for t, c in df.items()}
    q = set(tokens(a.query))
    by_id = {e["id"]: d for e, d in zip(idx, docs)}

    scored = []
    for e in pool:
        d = by_id[e["id"]]
        s = sum(WEIGHTS[k] * idf.get(t, 0) * math.log(1 + d[k][t]) for k in WEIGHTS for t in q if d[k][t])
        if s > 0:
            scored.append((s, e))
    scored.sort(key=lambda x: -x[0])
    top = scored[: a.top]

    if a.json:
        print(json.dumps([{"score": round(s, 2), **{k: e[k] for k in ("id", "name", "task", "subtask", "subtask_name", "path")}}
                          for s, e in top], ensure_ascii=False, indent=1))
        return
    if not top:
        print("No matches. Try other wording, or browse references/taxonomy.md.")
        return
    for s, e in top:
        prob = " ".join(e["problem"].split())[:160]
        notfor = " ".join(e["when_not"].split())[:120]
        print(f"{s:6.2f}  {e['task']} {e['subtask']} {e['name']}  [{e['path']}]")
        print(f"        solves: {prob}")
        print(f"        not for: {notfor}")


if __name__ == "__main__":
    main()
