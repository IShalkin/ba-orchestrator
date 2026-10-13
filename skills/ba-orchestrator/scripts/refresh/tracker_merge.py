#!/usr/bin/env python3
"""Merge one tracker pull into the refresh state, and list the items that need mapping (workflow R1, light mode).

Usage:
  python tracker_merge.py STATE PULL.json

PULL.json records the whole query result: {"query": "<the query run>", "total": <the tracker's own count of matching
items>, "items": [...]}. A pull whose items do not number exactly its total is refused (exit 1, nothing written):
a pull that kept one page of a newest-first result would move the watermark past every item it dropped, and their
changes would never be merged. Query "updated >= <tracker_last_updated minus a margin> ORDER BY updated ASC" and page
to the end.

The statuses that count as cancelled are the one set init_state.py recorded in STATE/state.json
(cancelled_statuses); build_baseline.py reads the same set.

Each item is {key, summary, status, labels, issuetype, parent_key, assignee, created, updated,
description, ac}. A pull that lacks description, ac or updated on any item is refused (exit 1, nothing written):
some tracker APIs' compact views drop those fields without saying so, and a pull without them would mark every
item re-worded. So is an empty summary, description or ac on an item that had text there in the export or an earlier pull
(the field was not fetched), unless --allow-empty-summary / --allow-empty-description / --allow-empty-ac KEY says it
was deleted. Write the pull from the raw tool response with a script, never retyped: the hash depends on it.

Text hash = md5 of the letters and digits (any script, case-folded) of summary + description + ac, after stripping HTML tags and unescaping
entities, because one API can return a body as markdown for one item and HTML for the next. The symbols that change
a number's meaning are kept as word tokens first (SYMBOLS: a comparator or "=" before a number, a sign before a digit,
a decimal point or comma between digits, "%" after and "±" before a number), so "< 2 s" -> "> 2 s", "1.5" -> "15",
"-20" -> "20" and "2-5" -> "25" are changes; markup never writes these between digits. The first live
sighting of a baseline-export item is flagged when its numbers or negation words differ from the export, or its
letters+digits text falls below a 0.9 similarity (see SIMILARITY). Every state file is written atomically.
Writes STATE/tracker/now.json (current state per key), STATE/tracker/texts.json (the last text of every item that
can be mapped, so apply_mappings.py can check an amended mapping's quote), STATE/tomap.json (CUMULATIVE: every live item outside the
baseline export, or re-opened since the export (now.json "reopened"), whose text is not yet mapped at its current
hash, including items pulled earlier and still unmapped), STATE/flags.json (cancelled_keys: items cancelled since they were last seen live; reopened_keys: items
live again since they were last seen cancelled; text_changed_keys: baseline-export items whose text changed) and the STATE/state.json watermark tracker_last_updated (the newest
`updated` seen; query the next pull from it). Exit 0 = merged, 1 = refused pull or missing state.
"""
import argparse, collections, csv, datetime, difflib, hashlib, html, json, os, re, sys, tempfile
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

REQUIRED = ("key", "summary", "status", "issuetype", "updated", "description", "ac")
TEXT_FIELDS = ("summary", "description", "ac")
FLAG_LISTS = (("cancelled_keys", "cancelled", False), ("reopened_keys", "re-opened", True),
              ("text_changed_keys", "text changed", True))


def as_text(v):
    """A text field as a string: a list is joined line by line, an object is written as JSON (some tracker APIs return
    the description as a document object or the acceptance criteria as a list)."""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return "\n".join(as_text(x) for x in v)
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


def has_text(d):
    """{has_summary, has_description, has_ac}: which text fields the item carries, for the empty-field guard."""
    return {f"has_{f}": bool(as_text(d.get(f)).strip()) for f in TEXT_FIELDS}

SIMILARITY = 0.9
NEGATION = {"not", "no", "never", "cannot", "without", "nor", "none", "neither", "nothing", "nobody", "nowhere",
            "dont", "doesnt", "didnt", "isnt", "arent", "wasnt", "werent", "cant", "couldnt", "wont", "wouldnt",
            "shouldnt", "mustnt", "hasnt", "havent", "hadnt", "neednt", "shant", "aint"}
DEFAULT_CANCELLED = "Cancelled,Canceled"
WIKI_HEADING = re.compile(r"(?m)^\s*h[1-6]\.\s")
MARKUP_NUMBERS = re.compile(r"(?m)^\s*\d+[.)]\s|!\[[^\]]*\]\([^)]*\)|![^!\s|]+\.(?:png|jpe?g|gif|svg|webp|bmp)(?:\|[^!]*)?!", re.I)


NUM = r"(?=[ \t*_]*[-−–]?\d)"
SYMBOLS = ((rf"(?:<=|≤|&le;){NUM}", " zzle "), (rf"(?:>=|≥|&ge;){NUM}", " zzge "), (rf"<{NUM}", " zzlt "),
           (rf">{NUM}", " zzgt "), (rf"={NUM}", " zzeq "), (rf"±{NUM}", " zzpm "), (r"(?<=\d)\s*%", " zzpct "),
           (r"[-−–—](?=\d)", " zzminus "), (r"(?<=\d)[.,](?=\d)", " zzsep "))
TAG_RX = re.compile(r"</?[a-z!][^>]*>", re.I)
SYMBOL_MARKUP = ((re.compile(r"(?<![\w-])-(?=[^\s-])([^\n-]*[^\s-])-(?![\w-])"), r"\1"),
                 (re.compile(r"(?m)^[ \t]*>+[ \t]?"), ""))


def plain_text(t):
    """Markup-free, case-folded text: tags stripped, entities unescaped, typographic apostrophes straightened, and
    the meaning-bearing symbols around numbers kept as word tokens (SYMBOLS)."""
    t = html.unescape(TAG_RX.sub(" ", t or ""))
    for rx, rep in SYMBOL_MARKUP:
        t = rx.sub(rep, t)
    for rx, tok in SYMBOLS:
        t = re.sub(rx, tok, t)
    return t.casefold().replace("’", "'")


def norm_text(t):
    r"""Letters and digits of ANY script (\w, Unicode), case-folded: what is hashed and compared. An [a-z0-9] class
    would erase non-Latin text and hash only its digits."""
    return re.sub(r"[\W_]+", "", plain_text(t))


def words(t):
    """Lower-case words of a body, markup-free: tags stripped, entities unescaped, wiki heading markers, ordered-list
    markers and embedded image names dropped."""
    return " ".join(re.findall(r"[^\W_]+(?:'[^\W_]+)?", plain_text(MARKUP_NUMBERS.sub(" ", WIKI_HEADING.sub(" ", t or "")))))


def is_negation(w):
    return w in NEGATION or w.endswith("n't")


def cancelled_set(state):
    """The one cancelled-status set of a refresh state (recorded by init_state.py), lower-cased."""
    st = load(Path(state) / "state.json", {})
    return {x.strip().lower() for x in st.get("cancelled_statuses", DEFAULT_CANCELLED.split(",")) if x.strip()}


def item_text(d):
    """The text of an item that is hashed, compared and quoted: summary, description and acceptance criteria (a
    ticket whose only text is its summary is re-worded by re-titling it)."""
    return f"{d.get('summary') or ''}\n{d.get('description') or ''}\n{d.get('ac') or ''}"


def body(d):
    return norm_text(item_text(d))


def diverged(old_words, new_words):
    """First-sighting rule: numbers or negations changed, or the letters+digits text diverged past the floor."""
    a, b = old_words.split(), new_words.split()
    nums = [collections.Counter(re.findall(r"\d+|zz[a-z]+", " ".join(x))) for x in (a, b)]
    negs = [collections.Counter(w for w in x if is_negation(w)) for x in (a, b)]
    if nums[0] != nums[1] or negs[0] != negs[1]:
        return True
    x, y = re.sub(r"[\W_]+", "", old_words), re.sub(r"[\W_]+", "", new_words)
    return x != y and difflib.SequenceMatcher(None, x, y, autojunk=False).ratio() < SIMILARITY


def snapshot(rec, mapping=None):
    """The state of an item a review covered: its status and text hash, plus, for a mapping problem, the mapping row's
    hash, effect and requirement ids. accept.py clears a flag only while this is unchanged."""
    out = {"status": (rec or {}).get("status", ""), "text_hash": (rec or {}).get("text_hash", "")}
    if mapping is not None:
        out["mapping"] = [mapping.get("text_hash", ""), (mapping.get("effect") or "").strip(), mapping.get("req_ids", "")]
    return out


def text_hash(d):
    return hashlib.md5(body(d).encode()).hexdigest()


def key_sort(k):
    p, _, n = k.rpartition("-")
    return (p, int(n) if n.isdigit() else 0, k)


def load(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def atomic_write(path, text):
    """Write a temp file beside the target, then rename it over: a crash or an error never leaves it truncated."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def dump(path, obj):
    atomic_write(path, json.dumps(obj, ensure_ascii=False, indent=1) + "\n")


def read_mappings(state):
    p = state / "mappings.csv"
    if not p.exists():
        return {}
    with open(p, newline="", encoding="utf-8") as f:
        return {r["key"]: r for r in csv.DictReader(f)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", type=Path)
    ap.add_argument("pull", type=Path)
    for f in TEXT_FIELDS:
        ap.add_argument(f"--allow-empty-{f}", action="append", default=[], metavar="KEY",
                        help=f"accept an empty {f} for KEY although it had one before (it was really deleted)")
    a = ap.parse_args()
    cancelled = cancelled_set(a.state)
    try:
        doc = json.loads(a.pull.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        sys.exit(f"ERROR: cannot read {a.pull}: {e}")
    if not isinstance(doc, dict) or not isinstance(doc.get("items"), list) or not isinstance(doc.get("total"), int):
        sys.exit('ERROR: the pull must be {"query": ..., "total": <the tracker\'s count of matches>, "items": [...]}: '
                 "without the total a truncated pull cannot be told from a complete one")
    pull = doc["items"]
    if not all(isinstance(d, dict) for d in pull):
        sys.exit("ERROR: every item of the pull must be an object")
    keys = [d.get("key") for d in pull]
    if len(pull) != doc["total"] or len(set(keys)) != len(keys):
        sys.exit(f"ERROR: the pull holds {len(pull)} items ({len(set(keys))} distinct) for a total of {doc['total']}: "
                 "page to the end (ORDER BY updated ASC) before merging; nothing written, the watermark did not move")
    lacking = [d.get("key", "?") for d in pull if not all(f in d for f in REQUIRED)]
    if lacking:
        sys.exit(f"ERROR: {len(lacking)} item(s) lack one of {', '.join(REQUIRED)} (a compact view drops them; "
                 f"pull with the full field list): {lacking[:5]}")
    for d in pull:
        for f in TEXT_FIELDS:
            d[f] = as_text(d[f])
    empty = [d["key"] for d in pull if not d["updated"]]
    if empty:
        sys.exit(f"ERROR: empty `updated` in the pull: {empty[:5]}")
    nowp = a.state / "tracker" / "now.json"
    if not nowp.exists():
        sys.exit(f"ERROR: {nowp} missing; run init_state.py first")
    now = load(nowp, {})
    for f in TEXT_FIELDS:
        lost = [d["key"] for d in pull if not d[f].strip() and now.get(d["key"], {}).get(f"has_{f}")
                and d["key"] not in getattr(a, f"allow_empty_{f}")]
        if lost:
            sys.exit(f"ERROR: empty {f} for {len(lost)} item(s) that had one: {lost[:5]}; fetch the field "
                     f"(or pass --allow-empty-{f} KEY for text really deleted)")
    export_text = load(a.state / "tracker" / "export-text.json", {})
    maps = read_mappings(a.state)
    pending = {d["key"]: d for d in load(a.state / "tomap.json", [])}
    tp = a.state / "traced-keys.json"
    if not tp.exists():
        print("WARN  no traced-keys.json: build the page once before the first merge, or a re-opened item the trace "
              "places is listed to map")
    traced = set(load(tp, []))
    newly_cancelled, reopened, text_changed = [], [], []
    for d in pull:
        k, old, h = d["key"], now.get(d["key"]), text_hash(d)
        labels = d.get("labels") or ""
        rec = dict(key=k, type=d["issuetype"], status=d["status"], summary=d["summary"],
                   labels=" ".join(labels) if isinstance(labels, list) else str(labels), created=d.get("created", ""),
                   updated=d["updated"], text_hash=h, in_export=bool(old and old.get("in_export")),
                   **has_text(d))
        is_cancelled = rec["status"].lower() in cancelled
        if old and ((old.get("status") or "").lower() in cancelled) != is_cancelled:
            (newly_cancelled if is_cancelled else reopened).append(k)
        rec["reopened"] = not is_cancelled and bool(rec["in_export"] and (k in reopened or (old or {}).get("reopened")))
        if rec["in_export"] and old.get("text_hash") and old["text_hash"] != h:
            text_changed.append(k)
        elif rec["in_export"] and not old.get("text_hash") and k in export_text and \
                diverged(export_text[k], words(item_text(d))):
            text_changed.append(k)
        if (not rec["in_export"] or rec["reopened"]) and not is_cancelled and maps.get(k, {}).get("text_hash") != h:
            pending[k] = dict(d, text_hash=h)
        else:
            pending.pop(k, None)
        now[k] = rec
    pending = {k: v for k, v in pending.items() if maps.get(k, {}).get("text_hash") != v["text_hash"]
               and not (k in traced and now.get(k, {}).get("in_export"))
               and (now.get(k, {}).get("status") or "").lower() not in cancelled}
    dump(nowp, now)
    dump(a.state / "tomap.json", [pending[k] for k in sorted(pending, key=key_sort)])
    texts = load(a.state / "tracker" / "texts.json", {})
    texts.update({d["key"]: dict({f: d[f] for f in TEXT_FIELDS}, text_hash=now[d["key"]]["text_hash"]) for d in pull
                  if not now[d["key"]]["in_export"] or now[d["key"]]["reopened"]})
    dump(a.state / "tracker" / "texts.json", texts)
    fp = a.state / "flags.json"
    fl = load(fp, {})
    found = {"cancelled_keys": newly_cancelled, "reopened_keys": reopened, "text_changed_keys": text_changed}
    for name, _, _ in FLAG_LISTS:
        fl[name] = sorted(set(fl.get(name, [])) | set(found[name]), key=key_sort)
    dump(fp, fl)
    sp = a.state / "state.json"
    st = load(sp, {})
    st["tracker_last_updated"] = max([st.get("tracker_last_updated", "")] + [d["updated"] for d in pull])
    st["last_pull"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "file": a.pull.name, "items": len(pull)}
    dump(sp, st)
    print(f"items {len(now)} · pulled {len(pull)} · to map {len(pending)} · newly cancelled {len(newly_cancelled)} "
          f"· re-opened {len(reopened)} · text changed (baseline items) {len(text_changed)} · watermark {st['tracker_last_updated']}")


if __name__ == "__main__":
    main()
