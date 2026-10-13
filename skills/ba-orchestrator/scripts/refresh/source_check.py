#!/usr/bin/env python3
"""Detect changes in a slide deck or a whiteboard against the baseline the requirements were derived from
(workflow R1, light mode).

Usage:
  python source_check.py STATE deck DECK.pptx [--id ID]
  python source_check.py STATE whiteboard WIDGETS.json [--id ID] [--map FIELD=PATH ...]

ID is the source id given to init_state.py (the manifest source's "id"); it may be omitted when the baseline holds
one source of that kind. Results go to STATE/flags.json under decks.ID or whiteboards.ID; build_baseline.py turns
them into the list of requirements to review.

Decks are compared by slide TEXT, matched by content (one occurrence to one occurrence), never by index: a moved slide keeps its text and is not
flagged, any edited word is. Reported: changed_slides (CITED numbers, the numbering of the deck the researchers
read, whose text is gone; kept stable across accepted inserts and moves by the baseline's origin map), new_slides
(current numbers whose text was not in the baseline), moved_slides (cited number -> current number: a "slide N"
locator now points elsewhere), edited (cited -> current, a gone slide paired with its most similar new slide by
content first, then a leftover pair at the same position) and inserted_slides (new text paired with no baseline slide: new content to review).
Each check records the file's md5; accept.py accepts only a file whose check was reviewed. The signature is the slide-shape text, the hidden flag and
the speaker notes, in presentation order (the numbering stage_deck.py gives the researchers).
Whiteboards are compared by widget id; the signature is type, text, label, position, size, colour, parent and
connector ends. Reported: changed, added (with their text), deleted.
Exit 0 = checked, 1 = unreadable input, unknown name or an incomplete widget listing.
"""
import argparse, datetime, difflib, hashlib, json, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent / "stage")]
from stage_deck import ET, StageError, read_deck, zipfile

READ_ERRORS = (OSError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError, StageError)
from stage_whiteboard import FIELDS, normalise
from tracker_merge import dump, load

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

SIG_FIELDS = ("type", "text", "label", "x", "y", "width", "height", "colour", "parent", "start", "end")


def flat(parts):
    return " ".join(" ".join(parts).split())


def deck_slides(path):
    """{slide number: signature text}. ponytail: the text layer only, so a change visible only in the render
    (colour, strike-through, a picture) is not seen; render the deck when its md5 changed."""
    return {str(s["n"]): ("[hidden] " if s["hidden"] else "") + flat(s["text"]) + (" [notes] " + flat(s["notes"]) if s["notes"] else "")
            for s in read_deck(path)}


def whiteboard_widgets(path, maps=()):
    fields = {k: list(v) for k, v in FIELDS.items()}
    for m in maps:
        k, _, p = m.partition("=")
        if k not in fields or not p:
            raise ValueError(f"--map {m}: FIELD must be one of {', '.join(fields)}")
        fields[k].insert(0, p)
    ws, skipped = normalise(json.loads(Path(path).read_text(encoding="utf-8")), fields)
    if skipped:
        raise ValueError(f"{skipped} item(s) without an id under the paths tried (add --map id=PATH)")
    return {i: {"sig": hashlib.md5(json.dumps([w[f] for f in SIG_FIELDS]).encode()).hexdigest(), "text": w["text"][:300],
                "parent": w["parent"]} for i, w in ws.items()}


def board_map(board, given):
    """The field paths a whiteboard is read with: the ones recorded at init. A different --map would compare the
    board under another reading, so it is refused; a state from before the paths were recorded uses --map."""
    want = board.get("map", given)
    if given and list(given) != list(want):
        raise ValueError(f"--map {given} differs from the paths the baseline was read with {want}: drop --map")
    return want


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def pick_id(section, sid, kind):
    if sid:
        if sid not in section:
            raise ValueError(f"no {kind} with id {sid!r} in the baseline (have: {sorted(section)})")
        return sid
    if len(section) != 1:
        raise ValueError(f"the baseline holds {len(section)} {kind}s {sorted(section)}: pass --id")
    return next(iter(section))


PAIR_FLOOR = 0.5


def pair_edits(old, new, gone, fresh):
    """Pair each gone baseline slide with a new-text slide. First by CONTENT: greedy on the highest similarity, each
    slide used once, pairs below PAIR_FLOOR left unpaired. Then by POSITION, only when it is unambiguous: a gone slide
    still unpaired is paired with an unpaired new slide at the same number when the nearest unchanged neighbour on
    each side holds the same slide in both decks (a slide rewritten in place keeps its cited number, so its next edit
    is flagged). An insert or a delete next to the rewrite shifts a neighbour, so nothing is paired there: the gone
    slide is reported changed and the new slide is listed for review as text no citation covers.
    Returns {new number: old number}."""
    cands = sorted(((difflib.SequenceMatcher(None, old[g], new[f], autojunk=False).ratio(), g, f)
                    for g in gone for f in fresh), key=lambda x: (-x[0], int(x[1]), int(x[2])))
    out, used = {}, set()
    for r, g, f in cands:
        if r >= PAIR_FLOOR and g not in used and f not in out:
            out[f] = g
            used.add(g)
    left = {g for g in gone if g not in used}
    free = {f for f in fresh if f not in out}

    def held(i):
        i = str(i)
        return (i not in old and i not in new) or (i in old and i in new and old[i] == new[i])

    def aligned(g):
        for step in (-1, 1):
            i = int(g) + step
            while str(i) in left and str(i) in free:
                i += step
            if not held(i):
                return False
        return True
    for g in sorted(left, key=int):
        if g in free and aligned(g):
            out[g] = g
            used.add(g)
    return out


def match_occurrences(old, new):
    """{new number: old number} for slides with the same text, one occurrence to one occurrence (a repeated slide
    text is matched as many times as it occurs): the same number first, then in order."""
    by_text = {}
    for n in sorted(old, key=int):
        by_text.setdefault(old[n], [[], []])[0].append(n)
    for n in sorted(new, key=int):
        if new[n] in by_text:
            by_text[new[n]][1].append(n)
    out = {}
    for olds, news in by_text.values():
        for n in [x for x in news if x in olds]:
            out[n] = n
        for o, n in zip([x for x in olds if x not in out.values()], [x for x in news if x not in out]):
            out[n] = o
    return out


def check_deck(base, path):
    """Compare a deck with the accepted baseline. Slide numbers in the report are the CITED numbers (the deck the
    researchers read), carried through every accepted insert, move or edit by the baseline's origin map, so a
    "slide N" locator keeps pointing at the slide it quoted."""
    old, new = base["slides"], deck_slides(path)
    origin = base.get("origin") or {n: int(n) for n in old}
    same = match_occurrences(old, new)
    gone = [n for n in old if n not in same.values()]
    fresh = [n for n in new if n not in same]
    changed = sorted(origin[n] for n in gone if origin.get(n) is not None)
    added = sorted(int(n) for n in fresh)
    moved = [{"from": origin[same[n]], "to": int(n)} for n in sorted(same, key=int)
             if same[n] != n and origin.get(same[n]) is not None]
    edits = pair_edits(old, new, gone, fresh)
    nxt = {n: origin.get(same[n]) if n in same else origin.get(edits[n]) if n in edits else None for n in new}
    return {"md5": md5(path), "md5_changed": md5(path) != base.get("md5"), "changed_slides": changed,
            "new_slides": added, "inserted_slides": sorted(int(n) for n in fresh if n not in edits), "moved_slides": moved, "slides_base": len(old), "slides_now": len(new),
            "old_text": {str(origin[n]): old[n] for n in gone if origin.get(n) is not None},
            "new_text": {str(n): new[str(n)] for n in added}, "origin_next": nxt,
            "edited": [{"cited": origin[g], "now": int(f)} for f, g in sorted(edits.items(), key=lambda x: int(x[0]))
                       if origin.get(g) is not None]}


def check_whiteboard(base, path, maps=()):
    old, now = base["widgets"], whiteboard_widgets(path, maps)
    added = sorted(k for k in now if k not in old)
    changed = sorted(k for k in now if k in old and now[k]["sig"] != old[k]["sig"])
    return {"md5": md5(path), "changed": changed, "added": added, "deleted": sorted(k for k in old if k not in now),
            "widgets_base": len(old), "widgets_now": len(now), "added_text": {k: now[k]["text"] for k in added},
            "changed_text": {k: {"old": old[k]["text"], "new": now[k]["text"]} for k in changed},
            "parents": {k: c for k in changed + added for c in [ancestors(now, k)] if c} |
                       {k: c for k in old if k not in now for c in [ancestors(old, k)] if c},
            "old_parents": {k: c for k in changed for c in [[x for x in ancestors(old, k) if x not in ancestors(now, k)]] if c}}


def ancestors(ws, k):
    """The parent chain of item k in widgets ws, nearest first; stops at a missing parent or a cycle."""
    out, p = [], (ws.get(k) or {}).get("parent")
    while p and p not in out and p != k:
        out.append(p)
        p = (ws.get(p) or {}).get("parent")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", type=Path)
    ap.add_argument("kind", choices=["deck", "whiteboard"])
    ap.add_argument("file", type=Path)
    ap.add_argument("--id", dest="sid")
    ap.add_argument("--map", action="append", default=[], metavar="FIELD=PATH")
    a = ap.parse_args()
    try:
        base = load(a.state / "baseline.json", None)
        if base is None:
            raise ValueError(f"{a.state / 'baseline.json'} missing; run init_state.py first")
        sec = "decks" if a.kind == "deck" else "whiteboards"
        name = pick_id(base.get(sec) or {}, a.sid, a.kind)
        r = check_deck(base[sec][name], a.file) if a.kind == "deck" else \
            check_whiteboard(base[sec][name], a.file, board_map(base[sec][name], a.map))
    except READ_ERRORS as e:
        sys.exit(f"ERROR: {e}")
    fp = a.state / "flags.json"
    fl = load(fp, {})
    r["checked_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    fl.setdefault(sec, {})[name] = r
    dump(fp, fl)
    if a.kind == "deck":
        print(f"deck {name}: md5 {'CHANGED' if r['md5_changed'] else 'same'} · slides {r['slides_base']}->{r['slides_now']} "
              f"· changed (baseline numbers) {r['changed_slides']} · new {r['new_slides']} · moved {len(r['moved_slides'])}")
    else:
        print(f"whiteboard {name}: widgets {r['widgets_base']}->{r['widgets_now']} · changed {len(r['changed'])} "
              f"· added {len(r['added'])} · deleted {len(r['deleted'])}")


if __name__ == "__main__":
    main()
