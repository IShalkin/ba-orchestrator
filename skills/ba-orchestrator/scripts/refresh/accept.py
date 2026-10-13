#!/usr/bin/env python3
"""After the flagged requirements were reviewed: make the reviewed source state the new baseline and clear its flags
(workflow R1, light mode). Accepting moves the baseline and silences the flag, so run it only after the review.

Usage:
  python accept.py STATE deck DECK.pptx [--id ID]
  python accept.py STATE whiteboard WIDGETS.json [--id ID] [--map FIELD=PATH ...]
  python accept.py STATE tracker
  python accept.py STATE source --id ID    (a wiki or file source a person re-read: no script checks those; only an
                                           id the built review listed, and it is due again after the next pull)

One model for every source: build_baseline.py writes STATE/review.json with "reviewed", the exact state the review
covered: per deck and whiteboard the md5 of the checked file, and the tracker's cancelled and text-changed keys.
accept.py accepts only that:
  - a deck or whiteboard whose file md5 equals the reviewed md5 AND the md5 of its current check in flags.json
    (a check run after the page was built is not reviewed: rebuild and review first); a deck keeps the cited slide
    numbers through the accept (the origin map that check computed);
  - for the tracker, a reviewed key only while it is in the state the review saw (status and text hash in
    STATE/tracker/now.json): a key flagged by a later pull, or re-worded or re-opened after the page was built,
    stays flagged. The mapping problems the review listed (a cancelled, stale, conflicting or descoping mapping) are
    acknowledged at the state the review saw in STATE/state.json "acknowledged_mappings"; the page build stops
    listing each while the item and its mapping row are in that state.
The accepted deck or whiteboard stays in flags.json as a clean check of the accepted file (nothing changed), so
the page build can tell it from a source never checked.
Every acceptance is logged in STATE/state.json under "accepted" (kind, id, md5 or keys, time).
Exit 0 = accepted, 1 = not reviewed, unreadable input or unknown id.
"""
import argparse, datetime, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent / "stage")]
from source_check import READ_ERRORS, board_map, check_deck, check_whiteboard, deck_slides, md5, pick_id, whiteboard_widgets
from tracker_merge import FLAG_LISTS, dump, load, snapshot


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", type=Path)
    ap.add_argument("kind", choices=["deck", "whiteboard", "tracker", "source"])
    ap.add_argument("file", type=Path, nargs="?")
    ap.add_argument("--id", dest="sid")
    ap.add_argument("--map", action="append", default=[], metavar="FIELD=PATH")
    a = ap.parse_args()
    bp, fp, sp = a.state / "baseline.json", a.state / "flags.json", a.state / "state.json"
    entry = {"kind": a.kind, "at": datetime.datetime.now().isoformat(timespec="seconds")}
    try:
        base, fl, st = load(bp, {}), load(fp, {}), load(sp, {})
        reviewed = (load(a.state / "review.json", None) or {}).get("reviewed")
        if not isinstance(reviewed, dict) or not reviewed:
            raise ValueError("no STATE/review.json with 'reviewed': build the page (it writes review.json) and review it first")
        if a.kind == "tracker":
            now = load(a.state / "tracker" / "now.json", {})
            tracker = reviewed.get("tracker")
            if not isinstance(tracker, dict):
                raise ValueError("review.json has no tracker review: rebuild the page and review it first")
            for k, _, _ in FLAG_LISTS:
                seen = tracker.get(k) or {}
                if not isinstance(seen, dict):
                    raise ValueError("review.json predates per-key review states: rebuild the page and review it first")
                done = {x for x in fl.get(k, []) if x in seen and seen[x] == snapshot(now.get(x))}
                entry[k] = sorted(done)
                fl[k] = [x for x in fl.get(k, []) if x not in done]
            seen = tracker.get("mappings") or {}
            st.setdefault("acknowledged_mappings", {}).update(seen)
            entry["mappings"] = sorted(seen)
        elif a.kind == "source":
            if not a.sid:
                raise ValueError("accept source needs --id (the source id, or its name when it has none)")
            if a.sid not in (reviewed.get("by_hand") or []):
                raise ValueError(f"{a.sid!r} is no source this review asked to re-read by hand "
                                 f"(review.json lists {reviewed.get('by_hand') or []}): check the id, rebuild the page first")
            if reviewed.get("pull") != (st.get("last_pull") or {}).get("at"):
                raise ValueError("the tracker was pulled after this review was built: rebuild the page, re-read the "
                                 "source, then accept")
            fl.setdefault("by_hand", {})[a.sid] = {"checked_at": entry["at"], "accepted": True}
            entry["id"] = a.sid
        else:
            if not a.file:
                raise ValueError(f"accept {a.kind} needs the current file")
            sec = "decks" if a.kind == "deck" else "whiteboards"
            sid = pick_id(base.get(sec) or {}, a.sid, a.kind)
            have = md5(a.file)
            checked = (fl.get(sec) or {}).get(sid) or {}
            rv = (reviewed.get(sec) or {}).get(sid) or {}
            if rv.get("md5") != have or checked.get("md5") != have:
                raise ValueError(f"{a.file} (md5 {have}) is not the reviewed check of {sid!r}: reviewed md5 "
                                 f"{rv.get('md5')}, last check md5 {checked.get('md5')}; run source_check.py on it, "
                                 "rebuild the page, review, then accept")
            base[sec][sid] = ({"md5": have, "slides": deck_slides(a.file), "origin": checked["origin_next"]}
                              if a.kind == "deck" else
                              {"md5": have, "widgets": whiteboard_widgets(a.file, m := board_map(base[sec][sid], a.map)),
                               "map": m})
            fl[sec][sid] = dict(check_deck(base[sec][sid], a.file) if a.kind == "deck"
                                else check_whiteboard(base[sec][sid], a.file, m), checked_at=entry["at"], accepted=True)
            entry.update(id=sid, md5=have)
    except READ_ERRORS as e:
        sys.exit(f"ERROR: {e}")
    dump(bp, base)
    dump(fp, fl)
    st.setdefault("accepted", []).append(entry)
    dump(sp, st)
    print("accepted", a.kind, entry.get("id", ""))


if __name__ == "__main__":
    main()
