#!/usr/bin/env python3
"""Merge the trace.csv files of split executors and measure coverage, deterministically (run-protocol §8).

Usage:
  python merge_trace.py OUT_DIR --trace A.csv [B.csv ...] [--catalogue CAT.csv ...] [--issues issues.json]
         [--exclude-status Cancelled,Canceled] [--baseline OLD/coverage-summary.json]

Trace schema (fixed): req_id, req_type, capability, jira_keys, coverage, jira_statuses, mvp_class_source,
mvp_class_jira, conflict_flags, gap_note, evidence. Header variants are accepted: case, surrounding spaces
and a bracketed suffix are ignored ("coverage(full|partial|none)" -> coverage).
Keys in jira_keys are expanded: "ABC-10..ABC-20", "ABC-10..20", "ABC-10–ABC-20" (en dash) and
"ABC-10 to ABC-20"; a span over 200, a reversed range or a range across prefixes is not expanded and is
listed under range_errors. Other keys are found by pattern; between two keys only a list separator (comma,
semicolon, slash, "&", "and", whitespace) is accepted, and anything else ("...", a dash, "through") or a
stray number after a key ("ABC-10-12") is listed under range_errors, not guessed.
coverage is case-insensitive and must be full, partial or none; any other value fails the merge (exit 1).
A catalogue is a CSV with a req_id (or id) column, else its first column is used.
issues.json is a list of issues (or {"issues": [...]}) as written by stage_tracker.py.

Writes OUT_DIR/trace-merged.csv (every row, sorted by req_id then input order, with source_file, line and
the expanded keys) and OUT_DIR/coverage-summary.json:
  counts per req_type and per capability (coverage value -> count over DISTINCT req_ids; a duplicated
  req_id counts once, with its LOWEST coverage, whatever the input order), conflict-flag rows, duplicate req_ids (each occurrence), catalogue ids missing from the
  trace, trace ids not in the catalogue, catalogue duplicates, range errors, referenced keys absent from
  issues.json, issues not referenced by any requirement (excluded statuses dropped), by status, and the
  counted coverage per req_id. With --baseline (an earlier coverage-summary.json), also "drift": req_ids
  whose coverage changed (from, to), req_ids added and req_ids removed (refresh runs, workflow R1).
Exit 0 = merged, 1 = unreadable input, missing column or a coverage value outside the schema.
"""
import argparse, csv, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

SCHEMA = ["req_id", "req_type", "capability", "jira_keys", "coverage", "jira_statuses", "mvp_class_source",
          "mvp_class_jira", "conflict_flags", "gap_note", "evidence"]
MAX_SPAN = 200
KEY = r"([A-Za-z][A-Za-z0-9_]*)-(\d+)"
RANGE = re.compile(KEY + r"\s*(?:\.\.|–|\bto\b)\s*(?:([A-Za-z][A-Za-z0-9_]*)-)?(\d+)")
NO_FLAG = {"", "none", "-", "n/a", "no"}
COVERAGE = ["none", "partial", "full"]  # lowest first: a duplicated req_id counts with its lowest coverage
LIST_SEP = re.compile(r"^(?:[\s,;/&]|\band\b)*$", re.I)


def norm(h):
    return re.sub(r"\s+", "_", re.sub(r"\(.*?\)|\[.*?\]", "", h or "").strip().lower())


def expand(cell, errors, where):
    keys = []

    def sub(m):
        p, lo, p2, hi = m.group(1).upper(), int(m.group(2)), (m.group(3) or m.group(1)).upper(), int(m.group(4))
        if p2 != p or hi < lo or hi - lo > MAX_SPAN:
            errors.append({"where": where, "range": m.group(0), "reason":
                           "prefix differs" if p2 != p else "reversed" if hi < lo else f"span over {MAX_SPAN}"})
            return " "
        keys.extend(f"{p}-{n}" for n in range(lo, hi + 1))
        return " "

    rest = RANGE.sub(sub, cell or "")
    found = list(re.finditer(KEY, rest))
    gaps = [rest[x.end():y.start()] for x, y in zip(found, found[1:])]
    tail = rest[found[-1].end():] if found else ""
    if any(not LIST_SEP.match(g) for g in gaps) or re.search(r"\d", tail):
        errors.append({"where": where, "range": cell, "reason": "separator is not a list or a range form"})
    keys += [f"{m.group(1).upper()}-{m.group(2)}" for m in found]
    return list(dict.fromkeys(keys))


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise ValueError(f"{path}: empty")
    return [norm(h) for h in rows[0]], rows[1:]


def read_trace(path):
    head, body = read_csv(path)
    missing = [c for c in SCHEMA if c not in head]
    if missing:
        raise ValueError(f"{path}: missing column(s) {', '.join(missing)} (header: {head})")
    out = []
    for line, r in enumerate(body, 2):
        if not any(x.strip() for x in r):
            continue
        d = {c: (r[head.index(c)] if head.index(c) < len(r) else "").strip() for c in SCHEMA}
        d["coverage"] = d["coverage"].lower()
        if d["coverage"] not in COVERAGE:
            raise ValueError(f"{path}:{line}: coverage {d['coverage']!r} is not one of {', '.join(COVERAGE)}")
        d["source_file"], d["line"] = str(path), line
        out.append(d)
    return out


def read_catalogue(path):
    head, body = read_csv(path)
    col = head.index("req_id") if "req_id" in head else head.index("id") if "id" in head else 0
    return [(r[col].strip(), str(path), line) for line, r in enumerate(body, 2) if len(r) > col and r[col].strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--trace", nargs="+", required=True, type=Path)
    ap.add_argument("--catalogue", nargs="+", default=[], type=Path)
    ap.add_argument("--issues", type=Path)
    ap.add_argument("--exclude-status", default="Cancelled,Canceled")
    ap.add_argument("--baseline", type=Path, help="an earlier coverage-summary.json to diff against")
    a = ap.parse_args()
    try:
        rows = [r for t in a.trace for r in read_trace(t)]
        cat = [c for p in a.catalogue for c in read_catalogue(p)]
        issues = None
        if a.issues:
            raw = json.loads(a.issues.read_text(encoding="utf-8"))
            issues = raw.get("issues", []) if isinstance(raw, dict) else raw
        old = json.loads(a.baseline.read_text(encoding="utf-8")).get("coverage_by_req") if a.baseline else None
        if a.baseline and not isinstance(old, dict):
            raise ValueError(f"{a.baseline}: no coverage_by_req (written by an older merge_trace.py? re-merge the baseline)")
    except (OSError, ValueError, csv.Error) as e:
        sys.exit(f"ERROR: {e}")

    range_errors, referenced = [], set()
    for r in rows:
        r["keys"] = expand(r["jira_keys"], range_errors, f"{r['source_file']}:{r['line']}")
        referenced.update(r["keys"])

    by_id = defaultdict(list)
    for r in rows:
        by_id[r["req_id"]].append(r)
    first = [min(occ, key=lambda r: (COVERAGE.index(r["coverage"]), r["source_file"], r["line"]))
             for _, occ in sorted(by_id.items())]
    per = {"req_type": defaultdict(Counter), "capability": defaultdict(Counter)}
    for r in first:
        for dim in per:
            per[dim][r[dim]][r["coverage"]] += 1

    cat_ids = Counter(c[0] for c in cat)
    summary = {
        "inputs": {"trace": [{"file": str(t), "rows": sum(r["source_file"] == str(t) for r in rows)} for t in a.trace],
                   "catalogue": [str(p) for p in a.catalogue], "issues": str(a.issues) if a.issues else None},
        "rows": len(rows),
        "distinct_req_ids": len(by_id),
        "per_req_type": {k: dict(sorted(v.items())) for k, v in sorted(per["req_type"].items())},
        "per_capability": {k: dict(sorted(v.items())) for k, v in sorted(per["capability"].items())},
        "coverage_totals": dict(sorted(Counter(r["coverage"] for r in first).items())),
        "conflict_rows": [{"req_id": r["req_id"], "conflict_flags": r["conflict_flags"], "file": r["source_file"],
                           "line": r["line"]} for r in sorted(rows, key=lambda r: (r["req_id"], r["source_file"], r["line"]))
                          if r["conflict_flags"].strip().lower() not in NO_FLAG],
        "duplicates": [{"req_id": k, "occurrences": [{"file": r["source_file"], "line": r["line"],
                                                      "coverage": r["coverage"]}
                                                     for r in sorted(occ, key=lambda r: (r["source_file"], r["line"]))]}
                       for k, occ in sorted(by_id.items()) if len(occ) > 1],
        "range_errors": sorted(range_errors, key=lambda e: (e["where"], e["range"])),
        "coverage_by_req": {r["req_id"]: r["coverage"] for r in first},
    }
    if a.baseline:
        new = summary["coverage_by_req"]
        summary["drift"] = {"baseline": str(a.baseline),
                            "changed": [{"req_id": k, "from": old[k], "to": new[k]} for k in sorted(set(old) & set(new))
                                        if old[k] != new[k]],
                            "added": sorted(set(new) - set(old)), "removed": sorted(set(old) - set(new))}
    if a.catalogue:
        summary["missing_from_trace"] = sorted(set(cat_ids) - set(by_id))
        summary["not_in_catalogue"] = sorted(set(by_id) - set(cat_ids))
        summary["catalogue_duplicates"] = sorted(k for k, n in cat_ids.items() if n > 1)
    if issues is not None:
        excluded = {s.strip().lower() for s in a.exclude_status.split(",") if s.strip()}
        status = {i["key"].upper(): ((i.get("fields") or {}).get("status") or {}).get("name", "") for i in issues}
        unref = sorted((k for k, s in status.items() if k not in referenced and s.lower() not in excluded),
                       key=lambda k: (k.rsplit("-", 1)[0], int(k.rsplit("-", 1)[1])))
        summary["unknown_referenced_keys"] = sorted(referenced - set(status))
        summary["unreferenced_issues"] = {"excluded_statuses": sorted(excluded), "count": len(unref),
                                          "by_status": dict(sorted(Counter(status[k] for k in unref).items())),
                                          "keys": unref}

    a.out_dir.mkdir(parents=True, exist_ok=True)
    merged, js = a.out_dir / "trace-merged.csv", a.out_dir / "coverage-summary.json"
    order = {str(t): n for n, t in enumerate(a.trace)}
    with open(merged, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(SCHEMA + ["jira_keys_expanded", "source_file", "line"])
        for r in sorted(rows, key=lambda r: (r["req_id"], order[r["source_file"]], r["line"])):
            w.writerow([r[c] for c in SCHEMA] + [" ".join(r["keys"]), r["source_file"], r["line"]])
    js.write_text(json.dumps(summary, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{len(rows)} rows, {len(by_id)} distinct req_ids, {len(summary['duplicates'])} duplicated, "
          f"{len(range_errors)} range errors")
    for p in (merged, js):
        print(f"{p.stat().st_size:>10}  {p}")


if __name__ == "__main__":
    main()
