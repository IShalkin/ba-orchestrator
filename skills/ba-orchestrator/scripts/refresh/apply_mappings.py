#!/usr/bin/env python3
"""Merge mapped rows into the cumulative STATE/mappings.csv, one row per item key, newest wins (workflow R1).

Usage:
  python apply_mappings.py STATE MAPPED.csv [--key-pattern RE] [--req-pattern RE]

MAPPED.csv columns: key, text_hash, req_ids, effect, quote, note. req_ids lists requirement ids separated by any of
; , / | or whitespace (written back ';'-separated); it may be empty for an item that states no requirement.
effect is one of EFFECTS exactly (a trailing "(note)" allowed). A row may also amend the mapping of an item
already mapped at its current text (STATE/tracker/texts.json holds that text). Refused, with nothing written (exit 1):
  - a key that is neither in STATE/tomap.json nor such an amendment, or a text_hash that differs from the item's
    hash there (the mapping was made against other text);
  - a key or requirement id that does not match its pattern, a requirement id in no catalogue (STATE/
    requirement-ids.json, written by every build_baseline.py run; build once before the first mapping), or an
    effect outside EFFECTS;
  - a key given twice in MAPPED.csv (one row per item; put every requirement id in its req_ids);
  - a mapping with requirement ids but no quote, a quote shorter than QUOTE_MIN_WORDS words and QUOTE_MIN_CHARS
    letters, or a quote whose words are not a contiguous run of whole words of the item's text (case-folded, tags
    stripped, any script), so a quote cannot be invented, paraphrased or reduced to a fragment such as "e";
  - an "upgrades"/"adds"/"conflicts"/"descopes" effect with no requirement id, a "no requirement" effect with one,
    or a "conflicts with <ids>" / "descopes <ids>" effect naming an id that is not in req_ids.
mappings.csv is replaced atomically (temp file and rename) after the rows are validated and sorted, so a failure
never truncates it. After writing, exit 1 when any item in tomap.json is still unmapped at its current hash.
Only "adds to existing coverage" and "upgrades ..." raise coverage on the baseline page; every other effect is
routed to review (build_baseline.py).
"""
import argparse, csv, datetime, io, json, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tracker_merge import atomic_write, item_text, key_sort, load, norm_text, words

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

COLS = ["key", "text_hash", "req_ids", "effect", "quote", "note", "mapped_on"]
FIXED = ("adds to existing coverage", "upgrades none->partial", "upgrades partial->full", "no requirement",
         "new requirement candidate")
NAMES_IDS = ("conflicts with", "descopes")
EFFECTS = FIXED + tuple(f"{x} <ids>" for x in NAMES_IDS)
LIFTS = ("adds to existing coverage", "upgrades none->partial", "upgrades partial->full")
NEEDS_IDS = LIFTS + NAMES_IDS
QUOTE_MIN_WORDS, QUOTE_MIN_CHARS = 4, 20


def quote_problem(quote, item):
    """None when the quote is a contiguous run of whole words of the item's text and long enough to mean something."""
    q, text = words(quote).split(), words(item_text(item)).split()
    if len(q) < QUOTE_MIN_WORDS and sum(c.isalpha() for c in norm_text(quote)) < QUOTE_MIN_CHARS:
        return f"the quote is too short to justify a mapping (needs {QUOTE_MIN_WORDS} words or {QUOTE_MIN_CHARS} letters)"
    if not any(text[i:i + len(q)] == q for i in range(len(text) - len(q) + 1)):
        return "the quote is not in the item's text as whole words (quote it exactly)"
    return None


def split_ids(s):
    return [x for x in re.split(r"[\s,;/|]+", s or "") if x]


def effect_kind(effect):
    """The effect a mapping row states, or None: one of FIXED exactly (a trailing "(note)" allowed), or
    "conflicts with" / "descopes" followed by the ids. Every reader of an effect goes through this."""
    low = re.sub(r"\s*\([^)]*\)$", "", " ".join((effect or "").lower().split()))
    if low in FIXED:
        return low
    return next((x for x in NAMES_IDS if low == x or low.startswith(x + " ")), None)


def lifts(effect):
    return effect_kind(effect) in LIFTS


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", type=Path)
    ap.add_argument("mapped", type=Path)
    ap.add_argument("--key-pattern", default=r"[A-Z][A-Z0-9_]*-\d+")
    ap.add_argument("--req-pattern", default=r"[A-Z][A-Z0-9]*-\d+[a-z]?")
    a = ap.parse_args()
    p = a.state / "mappings.csv"
    try:
        with open(a.mapped, newline="", encoding="utf-8-sig") as f:
            new = list(csv.DictReader(f))
        rows = {}
        if p.exists():
            with open(p, newline="", encoding="utf-8") as f:
                rows = {r["key"]: r for r in csv.DictReader(f)}
        tomap = {d["key"]: d for d in json.loads((a.state / "tomap.json").read_text(encoding="utf-8"))}
        texts = load(a.state / "tracker" / "texts.json", {})
        rp = a.state / "requirement-ids.json"
        if not rp.exists():
            sys.exit(f"ERROR: {rp} missing: build the page once (build_baseline.py writes the catalogue's ids)")
        known = set(json.loads(rp.read_text(encoding="utf-8")))
    except (OSError, ValueError, KeyError) as e:
        sys.exit(f"ERROR: {e}")
    errors, clean, seen = [], [], {}
    for k, t in texts.items():
        if k not in tomap and rows.get(k, {}).get("text_hash") == t.get("text_hash"):
            tomap[k] = dict(t, key=k)
    for n, r in enumerate(new, 2):
        k, ids = (r.get("key") or "").strip(), split_ids(r.get("req_ids"))
        effect, quote = (r.get("effect") or "").strip(), (r.get("quote") or "").strip()
        where = f"line {n} {k}"
        if k in seen:
            errors.append(f"{where}: key given twice (also line {seen[k]}); put every requirement id in one row")
        seen.setdefault(k, n)
        if not re.fullmatch(a.key_pattern, k):
            errors.append(f"{where}: key {k!r} does not match {a.key_pattern}")
        if k not in tomap:
            errors.append(f"{where}: not in tomap.json (map only what tracker_merge.py listed; re-merge first)")
        elif (r.get("text_hash") or "").strip() != tomap[k]["text_hash"]:
            errors.append(f"{where}: text_hash differs from tomap.json (mapped against other text)")
        bad = [x for x in ids if not re.fullmatch(a.req_pattern, x)]
        if bad:
            errors.append(f"{where}: requirement id(s) {bad} do not match {a.req_pattern}")
        elif set(ids) - known:
            errors.append(f"{where}: requirement id(s) {sorted(set(ids) - known)} are in no catalogue")
        kind = effect_kind(effect)
        if kind is None:
            errors.append(f"{where}: effect {effect!r} is not one of {list(EFFECTS)}")
        elif kind in NEEDS_IDS and not ids:
            errors.append(f"{where}: effect {effect!r} needs requirement id(s)")
        elif kind == "no requirement" and ids:
            errors.append(f"{where}: effect 'no requirement' with requirement id(s) {ids}")
        if ids and not quote:
            errors.append(f"{where}: a mapping needs the quote that justifies it")
        if quote and k in tomap and (why := quote_problem(quote, tomap[k])):
            errors.append(f"{where}: {why}")
        if kind in NAMES_IDS:
            named = [x for x in split_ids(effect) if re.fullmatch(a.req_pattern, x)]
            if not named or set(named) - set(ids):
                errors.append(f"{where}: effect {effect!r} must name its requirement id(s), each in req_ids {ids}")
        clean.append(dict({c: (r.get(c) or "").strip() for c in COLS}, key=k, req_ids=";".join(ids)))
    if errors:
        print("\n".join("ERROR " + e for e in errors))
        sys.exit(f"ERROR: {len(errors)} problem(s); nothing written")
    today = datetime.date.today().isoformat()
    for r in clean:
        rows[r["key"]] = dict(r, mapped_on=today)
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    w.writerows(sorted(rows.values(), key=lambda r: key_sort(r["key"])))
    atomic_write(p, out.getvalue())
    missing = sorted((k for k, d in tomap.items() if rows.get(k, {}).get("text_hash") != d["text_hash"]), key=key_sort)
    print(f"mappings {len(rows)} · applied {len(new)} · NOT mapped from tomap: {missing or 'none'}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
