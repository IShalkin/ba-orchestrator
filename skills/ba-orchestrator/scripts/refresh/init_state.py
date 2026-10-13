#!/usr/bin/env python3
"""One-time: build the refresh state from the inputs the baseline run was derived from (workflow R1, light mode).

Usage:
  python init_state.py STATE --tracker-export ISSUES.json --ac-field FIELD
         [--deck ID=DECK.pptx ...] [--whiteboard ID=WIDGETS.json ...] [--map FIELD=PATH ...]
         [--cancelled-status Cancelled,Canceled]

ISSUES.json is the tracker export the baseline trace was built on: stage_tracker.py's issues.json (items with a
"fields" object; the acceptance criteria are read from fields.<FIELD>, or pass "none"), or a list in the pull
format of tracker_merge.py. ID is the stable source id ([A-Za-z0-9_-], required, unique) that the baseline
manifest's source carries as "id": flags bind to a source by this id only, never by its display name or kind, and
build_baseline.py refuses a flag whose id is no manifest source of that kind. --cancelled-status is the ONE set of
statuses that count as cancelled for this state (tracker_merge.py and build_baseline.py read it from state.json);
give it the value the baseline's merge_trace.py --exclude-status used.
Pass the SAME deck and whiteboard files the researchers read, not a newer copy, or the first check compares
against the wrong baseline. Refuses to run on an initialised state (STATE/tracker/now.json exists).
Writes baseline.json, tracker/now.json, tracker/export-text.json (the words of each item), flags.json and
state.json (watermark, and the md5 of every input). Exit 0 = initialised, 1 = refused or unreadable input.
"""
import argparse, datetime, json, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent / "stage")]
from source_check import READ_ERRORS, deck_slides, md5, whiteboard_widgets
from tracker_merge import DEFAULT_CANCELLED, dump, has_text, item_text, words

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def flat_issue(i, ac_field):
    """An export item in the pull format: a raw tracker item (with "fields") or one already flat."""
    if "fields" not in i:
        return i
    f = i["fields"]

    def name(v):
        return (v or {}).get("name", "") if isinstance(v, dict) else v or ""
    ac = f.get(ac_field) if ac_field != "none" else ""
    return {"key": i["key"], "summary": f.get("summary", ""), "status": name(f.get("status")),
            "issuetype": name(f.get("issuetype")), "labels": " ".join(f.get("labels") or []),
            "created": f.get("created", ""), "updated": f.get("updated", ""),
            "description": f.get("description") or "", "ac": ac if isinstance(ac, str) else json.dumps(ac) if ac else ""}


def named(spec):
    sid, sep, path = spec.partition("=")
    if not sep or not re.fullmatch(r"[A-Za-z0-9_-]+", sid) or not path:
        raise ValueError(f"{spec!r}: give the source as ID=PATH, ID of letters, digits, _ or - (the manifest source's id)")
    return sid, Path(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", type=Path)
    ap.add_argument("--tracker-export", type=Path, required=True)
    ap.add_argument("--ac-field", required=True, help='field holding the acceptance criteria, or "none"')
    ap.add_argument("--deck", action="append", default=[], metavar="NAME=PATH")
    ap.add_argument("--whiteboard", action="append", default=[], metavar="NAME=PATH")
    ap.add_argument("--map", action="append", default=[], metavar="FIELD=PATH", help="whiteboard field path")
    ap.add_argument("--cancelled-status", default=DEFAULT_CANCELLED)
    a = ap.parse_args()
    if (a.state / "tracker" / "now.json").exists():
        sys.exit(f"ERROR: {a.state} is already initialised; a refresh state is built once")
    try:
        raw = json.loads(a.tracker_export.read_text(encoding="utf-8"))
        items = [flat_issue(i, a.ac_field) for i in (raw.get("issues", []) if isinstance(raw, dict) else raw)]
        if not items:
            raise ValueError(f"{a.tracker_export}: no items")
        ids = [named(x)[0] for x in a.deck + a.whiteboard]
        if len(set(ids)) != len(ids):
            raise ValueError(f"source ids must be unique across decks and whiteboards: {ids}")
        decks = {n: {"md5": md5(p), "slides": (sl := deck_slides(p)), "origin": {k: int(k) for k in sl}}
                 for n, p in map(named, a.deck)}
        boards = {n: {"md5": md5(p), "widgets": whiteboard_widgets(p, a.map), "map": a.map} for n, p in map(named, a.whiteboard)}
    except READ_ERRORS as e:
        sys.exit(f"ERROR: {e}")
    if a.ac_field != "none" and not any(i.get("ac") for i in items):
        print(f"WARN  no exported item carries {a.ac_field}: check the field name (the text hash covers description + ac)")
    now = {i["key"]: dict(key=i["key"], type=i.get("issuetype", ""), status=i.get("status", ""), summary=i.get("summary", ""),
                          labels=i.get("labels", ""), created=i.get("created", ""), updated=i.get("updated", ""),
                          text_hash="", in_export=True, **has_text(i)) for i in items}
    dump(a.state / "tracker" / "export-text.json", {i["key"]: words(item_text(i)) for i in items})
    dump(a.state / "baseline.json", {"decks": decks, "whiteboards": boards})
    dump(a.state / "flags.json", {})
    inputs = {"tracker_export": {"path": str(a.tracker_export), "md5": md5(a.tracker_export)}}
    inputs.update({f"deck:{n}": {"path": str(p), "md5": md5(p)} for n, p in map(named, a.deck)})
    inputs.update({f"whiteboard:{n}": {"path": str(p), "md5": md5(p)} for n, p in map(named, a.whiteboard)})
    dump(a.state / "state.json", {"tracker_last_updated": max(i.get("updated", "") for i in items), "inputs": inputs,
                                  "cancelled_statuses": [x.strip() for x in a.cancelled_status.split(",") if x.strip()],
                                  "initialised": datetime.datetime.now().isoformat(timespec="seconds")})
    dump(a.state / "tracker" / "now.json", now)
    print(f"items {len(now)} · decks {({n: len(d['slides']) for n, d in decks.items()})} · "
          f"whiteboards {({n: len(b['widgets']) for n, b in boards.items()})}")


if __name__ == "__main__":
    main()
