#!/usr/bin/env python3
"""Build the baseline page: the requirement lists, each requirement compared with every named source, every fact
linked to its source. Run by the orchestrator (SKILL.md step 4c); the manifest is described in run-protocol §12.

Usage:
  python build_baseline.py RUN_DIR [--manifest PATH] [--out PATH]

Default manifest RUN_DIR/06-final/baseline-manifest.json; default output RUN_DIR/06-final/baseline.html (a light
refresh passes --out, so the read-only baseline run is not written to). The page is self-contained (inline
CSS and JS, no external assets). Paths inside the manifest are relative to RUN_DIR unless absolute.

Evidence rows come from every RUN_DIR/02-research/*.md Evidence table, read by header. A requirement's evidence
ids are found by pattern (<prefix>-<n>, prefixes from the manifest's sources) in its catalogue row's evidence and
sources columns and in its trace row's evidence column. A source column shows a check mark and one link per cited
evidence row (its url; a deck row whose locator says "slide N" is labelled "slide N"); the hover text is the
locator and the quote. A row whose url is a path, "n/a: ...", or absent (a v0.3 log) is shown without a link.

Integrity, before anything is written:
  - coverage counts per req_type are recomputed from the trace (a duplicated req_id counts once, with its lowest
    coverage, as merge_trace.py does) and must equal coverage_summary's per_req_type, so the page can only be
    built from the trace that was summarised; the check runs on the BASELINE, before any refresh overlay;
  - coverage per requirement id must equal the summary's coverage_by_req (a count-preserving swap fails), catalogue
    ids must be unique and their type must match the trace's req_type;
  - the page must contain none of the banned patterns (defaults: home paths in any case or slash, AWS key ids,
    12-digit numbers bare or grouped, leftover [E: tags; plus the manifest's banned_patterns, case-insensitive),
    checked in the markup, the unescaped markup and the visible text. Exit 1 on any, and no file is written.
With refresh_state (workflow R1, light mode) the current tracker state is overlaid after the check: mapped live
items add their keys only at their current text hash and only for an "adds" or "upgrades" effect; a requirement with
coverage none or not traced that gains one becomes partial (never full); stale, cancelled, conflicting or descoping
mappings go to review instead; curated coverage_overrides and conflicts are applied. A requirement whose cited deck slide, whiteboard item or
tracker item changed is listed in REFRESH_STATE/review.json (never on the page) and counted on stdout.
Exit 0 = written, 1 = input, integrity or banned-pattern failure, 2 = usage.
"""
import argparse, collections, csv, datetime, html, json, re, sys, urllib.parse
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE / "stage"), str(HERE / "refresh")]
from apply_mappings import effect_kind, lifts, split_ids
from check_artifact import LEGACY_COLS, cells_of, evidence_table, is_url
from merge_trace import COVERAGE, expand, norm
from tracker_merge import FLAG_LISTS, atomic_write, cancelled_set, key_sort, load, snapshot

E = html.escape
TAG = re.compile(r"\s*\[E:[^\]]*\]")
TOKEN = re.compile(r"[^\s\"'<>()\[\]{}|,;`]+")
WEB = re.compile(r"(?:(?:https?|ftps?)://|(?=[\w-]+(?:\.[\w-]+)*\.[a-z]{2,24}(?::\d+)?/))", re.I)
SEG = r"[/\\](?:{})[/\\]+[^/\\]"
SHARE = r"(?:^|^[a-z][\w+.-]*:)(?:\\\\|//)[^/\\]+[/\\]+[\w-]*(?:users|home)[\w-]*\$?[/\\]+[^/\\]"
HOME_WIN = re.compile(SEG.format(r"users\$?|homes?\$?") + "|" + SHARE + r"|(?:^|[/\\])~[a-z_][\w.-]*[/\\]", re.I)
HOME_POSIX = re.compile(SEG.format(r"Users|homes?\$?") + r"|^/(?i:users)/+[^/]|(?:^|/)~[a-z_][\w.-]*/")


def home_path(text):
    """True when the text names a home folder (see the rule above). One function for the ban and home_locator."""
    for tok in TOKEN.findall(text or ""):
        if WEB.match(tok):
            parts = re.split(r"[?#]", tok, maxsplit=1)
            local = re.match(r"(?:https?|ftps?)://(?:localhost|127\.\d+\.\d+\.\d+|\[::1\])(?::\d+)?(/[^?#]*)", tok, re.I)
            pieces = re.split(r"[&=]", parts[1]) if len(parts) > 1 else []
            pieces += [local[1]] if local else []
            if not pieces:
                continue
        else:
            pieces = [tok]
        for t in pieces:
            win = "\\" in t or re.match(r"[a-z]:|//|[a-z][\w+.-]*:", t, re.I)
            if (HOME_WIN if win else HOME_POSIX).search(t):
                return True
    return False


def bounded(core, alphabet, prefixed=False):
    """An id pattern that no character of the id's own alphabet may extend on either side: glue from another
    alphabet ("deploy_123456789012", "key_AKIA...") is still the id, a longer run of its own alphabet is not. An id
    with a fixed prefix (AKIA) is bounded on the right only: the prefix marks its start ("9ASIA..." is a key id)."""
    return ("" if prefixed else rf"(?<!{alphabet})") + rf"{core}(?!{alphabet})"


DIGIT_BANS = {bounded(r"\d{12}", "[0-9]"), bounded(r"\d{4}[- ]\d{4}[- ]\d{4}", "[0-9]")}
DEFAULT_BANNED = [(home_path, "a home path")] + [(bounded(r"(?:AKIA|ASIA)[0-9A-Z]{16}", "[0-9A-Z]", True), 0)] + \
                 [(p, 0) for p in sorted(DIGIT_BANS)] + [(r"\[E:", re.I)]
GUID = re.compile(r"(?:\{|%7B|(?<![0-9a-f-]))[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?:\}|%7D|(?![0-9a-f-]))", re.I)
HEXRUN = re.compile(r"(?<![0-9a-f])[0-9a-f]{32,}(?![0-9a-f])", re.I)
INLINE_TAG = re.compile(r"</?(?:a|span|b|i|em|strong|code)\b[^>]*>", re.I)
RANGE_SEP = r"(?:-|–|—|to|through|thru)"
SLIDES = re.compile(r"\b(?:slides?|pages?|pp?\.|pgs?\.?)\s*(?:[#:=(]|no\.?|nr\.?|number)?\s*"
                    rf"(\d+(?:\s*(?:{RANGE_SEP}|,|&|and)\s*\d+)*)", re.I)
KINDS = ("deck", "whiteboard", "tracker", "wiki", "file")
CHECKED_IN = {"deck": "decks", "whiteboard": "whiteboards"}
COV_LABEL = {"full": "Full", "partial": "Partial", "none": "None", "": "Not traced"}


class BuildError(Exception):
    pass


def clean(s):
    return TAG.sub("", s or "").strip()


def cited_locator(loc):
    """The locator without its staging pointer (the part after an arrow, a "(staged ...)" note): by convention a local
    file for critics, never shown. Everything else is the citation and is banned-scanned BEFORE any path is cut."""
    loc = re.split(r"\s*(?:→|->)\s*", loc or "", maxsplit=1)[0]
    return re.sub(r"\(\s*staged\b[^)]*\)", "", loc, flags=re.I)


def home_locator(loc):
    """True when the cited locator names a home folder. Such a locator is never shown (cutting the path can leave a
    name behind: "/Users/Jo Smith Jr/deck.pptx" cuts to "Smith Jr/deck.pptx"); the row keeps its link and quote."""
    return home_path(cited_locator(loc))


def locator_text(loc):
    """The locator as shown: staging pointer dropped, then any local path (/..., ~/..., C:\\..., \\\\server) cut,
    including path segments after a space ("C:\\Users\\Jo Smith\\x.pptx"). A path inside a URL is kept."""
    if home_locator(loc):
        return ""
    loc = cited_locator(loc)
    loc = re.sub(r"(?<![\w.:/\\])(?:[A-Za-z]:[\\/]|~/|/|\\\\)[^\s)\]]*(?:\s+[^\s)\]]*[\\/][^\s)\]]*)*", "", loc)
    return re.sub(r"\s{2,}", " ", clean(loc)).strip(" ,;")


def slide_numbers(loc):
    out = []
    for m in SLIDES.finditer(loc or ""):
        for a, b in re.findall(rf"(\d+)(?:\s*{RANGE_SEP}\s*(\d+))?", m[1]):
            lo, hi = int(a), int(b or a)
            out += range(lo, hi + 1) if lo <= hi else [lo, hi]
    return out


def path_in(run, p):
    p = Path(p)
    return p if p.is_absolute() else run / p


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), [dict(x) for x in r]


def load_manifest(path):
    try:
        m = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise BuildError(f"cannot read manifest {path}: {e}")
    missing = [k for k in ("title", "request_verbatim", "catalogues", "trace", "coverage_summary", "sources") if not m.get(k)]
    for i, c in enumerate(m.get("catalogues") or []):
        missing += [f"catalogues[{i}].{k}" for k in ("type", "path", "id_col", "statement_col") if not c.get(k)]
    for i, s in enumerate(m.get("sources") or []):
        missing += [f"sources[{i}].{k}" for k in ("name", "evidence_prefixes", "kind") if not s.get(k)]
        if s.get("kind") and s["kind"] not in KINDS:
            missing.append(f"sources[{i}].kind {s['kind']!r} is not one of {list(KINDS)}")
    ids = [s["id"] for s in m.get("sources") or [] if s.get("id")]
    if len(set(ids)) != len(ids):
        missing.append(f"source ids must be unique: {ids}")
    prefixes = [p for s in m.get("sources") or [] for p in s.get("evidence_prefixes") or []]
    if len(set(prefixes)) != len(prefixes):
        missing.append(f"evidence prefixes must be unique across sources (each cites one source): {prefixes}")
    if missing:
        raise BuildError(f"manifest {path} lacks: {', '.join(missing)}")
    return m


def load_evidence(run, warn):
    ev = {}
    for log in sorted((run / "02-research").glob("*.md")):
        header, rows = evidence_table(log.read_text(encoding="utf-8"))
        if rows and (header is None or "url" not in header):
            warn.append(f"{log.name}: {len(rows)} evidence rows without a url column (a v0.3 log): shown without links")
        for _, r in rows:
            if header is None:
                r = {c: r.get(i, "") for i, c in enumerate(LEGACY_COLS)}
            if r.get("id"):
                ev[r["id"]] = {k: r.get(k, "") for k in ("source", "locator", "url", "date", "quote")}
    return ev


def read_trace(path):
    """req_id -> {type, coverage, keys, gap_note, evidence}: lowest coverage of a duplicated id, keys and evidence
    of every occurrence (merge_trace.py counts the same way)."""
    head, rows = read_rows(path)
    rows = [{norm(k): (v or "").strip() for k, v in r.items() if k} for r in rows]
    need = [c for c in ("req_id", "req_type", "coverage", "jira_keys", "gap_note", "evidence") if c not in map(norm, head)]
    if need:
        raise BuildError(f"{path}: missing trace column(s) {need}")
    by_id = collections.defaultdict(list)
    for r in rows:
        if r["req_id"]:
            if r["coverage"].lower() not in COVERAGE:
                raise BuildError(f"{path}: {r['req_id']}: coverage {r['coverage']!r} is not one of {COVERAGE}")
            by_id[r["req_id"]].append(r)
    out = {}
    for k, occ in by_id.items():
        low = min(occ, key=lambda r: COVERAGE.index(r["coverage"].lower()))
        keys = []
        for r in occ:
            keys += r["jira_keys_expanded"].split() if r.get("jira_keys_expanded") else expand(r["jira_keys"], [], k)
        out[k] = {"type": low["req_type"], "coverage": low["coverage"].lower(), "keys": list(dict.fromkeys(keys)),
                  "gap_note": low["gap_note"], "evidence": " ".join(r["evidence"] for r in occ)}
    return out


def check_counts(trace, summary):
    """The trace must be the one summarised: coverage per requirement id equals coverage_by_req, and the counts
    per req_type equal per_req_type. A count-preserving swap between two ids fails the first check."""
    by_req = summary.get("coverage_by_req")
    if not isinstance(by_req, dict):
        raise BuildError("coverage_summary has no coverage_by_req (written by merge_trace.py?)")
    want_ids = {k: str(v).lower() for k, v in by_req.items()}
    got_ids = {k: t["coverage"] for k, t in trace.items()}
    if got_ids != want_ids:
        diff = sorted(k for k in set(got_ids) | set(want_ids) if got_ids.get(k) != want_ids.get(k))
        raise BuildError(f"trace and coverage_summary disagree for {len(diff)} requirement(s), e.g. "
                         + ", ".join(f"{k}: trace {got_ids.get(k)} vs summary {want_ids.get(k)}" for k in diff[:5])
                         + "; re-run merge_trace.py on this trace, or point the manifest at the trace it summarised")
    got = collections.defaultdict(collections.Counter)
    for t in trace.values():
        got[t["type"]][t["coverage"]] += 1
    want = summary.get("per_req_type")
    if not isinstance(want, dict):
        raise BuildError("coverage_summary has no per_req_type (written by merge_trace.py?)")
    got = {t: {c: n for c, n in v.items() if n} for t, v in got.items()}
    want = {t: {c: n for c, n in (v or {}).items() if n} for t, v in want.items()}
    want = {t: v for t, v in want.items() if v}
    if got != want:
        raise BuildError(f"trace and coverage_summary disagree on coverage per req_type: trace {got} vs summary {want}; "
                         "re-run merge_trace.py on this trace, or point the manifest at the trace it summarised")


def first_existing(run, *paths):
    for p in paths:
        if p and path_in(run, p).exists():
            return path_in(run, p)
    return None


def build(run, manifest_path):
    man = load_manifest(manifest_path)
    warn = []
    try:
        summary = json.loads(path_in(run, man["coverage_summary"]).read_text(encoding="utf-8"))
        trace = read_trace(path_in(run, man["trace"]))
        check_counts(trace, summary)
        ev = load_evidence(run, warn)
        sources = man["sources"]
        src_of = {p: s for s in sources for p in s["evidence_prefixes"]}
        prefixes = sorted(src_of, key=len, reverse=True)
        eid_rx = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(map(re.escape, prefixes)) + r")-\d+[a-z]?(?![A-Za-z0-9])")
        reqs, order = {}, []
        for cat in man["catalogues"]:
            head, rows = read_rows(path_in(run, cat["path"]))
            for col in [cat["id_col"], cat["statement_col"]] + ([cat["group_col"]] if cat.get("group_col") else []):
                if col not in head:
                    raise BuildError(f"{cat['path']}: no column {col!r} (columns: {head})")
            ev_cols = [c for c in head if norm(c) in cat.get("evidence_cols", ["evidence", "sources"])]
            for r in rows:
                rid = (r.get(cat["id_col"]) or "").strip()
                if not rid:
                    continue
                if rid in reqs:
                    raise BuildError(f"{cat['path']}: requirement id {rid} is listed twice (also in "
                                     f"{reqs[rid]['type']}); every id must be unique across the catalogues")
                t = trace.get(rid, {})
                if t and t["type"] != cat["type"]:
                    raise BuildError(f"{rid}: the catalogue says {cat['type']}, the trace's req_type says {t['type']}")
                text = " ".join([r.get(c) or "" for c in ev_cols] + [t.get("evidence", "")])
                reqs[rid] = {"id": rid, "type": cat["type"], "stmt": clean(r[cat["statement_col"]]),
                             "group": (r.get(cat.get("group_col") or "") or "").strip(),
                             "eids": list(dict.fromkeys(eid_rx.findall(text))), "cov": t.get("coverage", ""),
                             "keys": list(t.get("keys", [])), "note": clean(t.get("gap_note", ""))}
                order.append(rid)
    except (OSError, ValueError, csv.Error) as e:
        raise BuildError(str(e))
    stray = sorted(set(trace) - set(reqs))
    if stray:
        warn.append(f"{len(stray)} trace req_id(s) are in no catalogue: {stray[:10]}")
    unknown = sorted({e for r in reqs.values() for e in r["eids"] if e not in ev})
    if unknown:
        warn.append(f"{len(unknown)} cited evidence id(s) are in no research log: {unknown[:10]}")

    unref = list((summary.get("unreferenced_issues") or {}).get("keys") or [])
    issues_file = first_existing(run, (summary.get("inputs") or {}).get("issues"))
    info = {}
    if issues_file:
        raw = json.loads(issues_file.read_text(encoding="utf-8"))
        for i in (raw.get("issues", []) if isinstance(raw, dict) else raw):
            f = i.get("fields") or i
            st = f.get("status")
            info[i["key"]] = {"summary": f.get("summary", ""), "status": st.get("name", "") if isinstance(st, dict) else st or ""}
    ex = (summary.get("unreferenced_issues") or {}).get("excluded_statuses")
    conflicts_extra, review = overlay(run, man, reqs, unref, info, ev, src_of, warn,
                                      {x.lower() for x in ex} if isinstance(ex, list) else None)

    tracker = man.get("tracker") or {}
    tracker_src = [s for s in sources if s["kind"] == "tracker"]
    cols = [s for s in sources if s["kind"] != "tracker"]
    key_prefixes = tracker.get("key_prefixes") or sorted({k.rsplit("-", 1)[0] for r in reqs.values() for k in r["keys"]}
                                                         | {k.rsplit("-", 1)[0] for k in unref})
    key_rx = re.compile(r"\b(?:" + "|".join(map(re.escape, key_prefixes)) + r")-\d+\b") if key_prefixes else None
    page = render(run, man, reqs, order, cols, tracker_src, ev, src_of, unref, info, conflicts_extra, stray)
    if key_rx and tracker.get("browse_url"):
        page = link_keys(page, key_rx, tracker["browse_url"])
    views = {"markup": page,
             "unescaped and URL-decoded markup": urllib.parse.unquote(html.unescape(page)),
             "visible text": html.unescape(re.sub(r"<[^>]+>", " ", INLINE_TAG.sub("", page))),
             "cited locators": "\n".join(cited_locator(ev[e]["locator"]) for r in reqs.values() for e in r["eids"]
                                          if e in ev and not home_locator(ev[e]["locator"]))}
    homes = sorted({e for r in reqs.values() for e in r["eids"] if e in ev and home_locator(ev[e]["locator"])})
    if homes:
        warn.append(f"{len(homes)} cited locator(s) name a local home folder and are shown without the locator: {homes[:10]}")
    bad = []
    for pat, flags in DEFAULT_BANNED + [(p, re.I) for p in man.get("banned_patterns") or []]:
        strip = (lambda t: HEXRUN.sub(" ", GUID.sub(" ", t))) if pat in DIGIT_BANS else (lambda t: t)
        found = pat if callable(pat) else (lambda t, p=pat, f=flags: bool(re.search(p, t, f)))
        hit = next((v for v, text in views.items() if found(strip(text))), None)
        if hit:
            where = [e for e, row in ev.items() if found(strip(urllib.parse.unquote(html.unescape(
                " ".join(row.values())))))] + [q for q, r in reqs.items() if found(strip(r["stmt"] + " " + r["group"] + " " + r["note"]))] \
                + [k for k, v in info.items() if found(strip(" ".join(map(str, v.values()))))] \
                + [row[0] or f"conflict row {n}" for n, row in enumerate(conflict_rows(run, man, conflicts_extra)[1], 1)
                   if found(strip(" ".join(row)))]
            if not where:
                where = ["no single carrier: search the page source"]
            bad.append(f"{flags if callable(pat) else repr(pat)} in the {hit} (in {', '.join(map(str, where[:5]))})")
    if bad:
        raise BuildError("banned pattern(s) in the page, not written: " + "; ".join(bad))
    return page, warn, review, reqs


def overlay(run, man, reqs, unref, info, ev, src_of, warn, summary_excl=None):
    """Refresh overlay (workflow R1 light mode), after the integrity check. Returns (extra conflicts, review).
    A mapping counts only at the item's CURRENT text hash and only while the item is live; only an "adds" or
    "upgrades" effect raises coverage (to partial at most). A stale, cancelled, conflicting or descoping mapping
    raises nothing and goes to review instead."""
    st = path_in(run, man["refresh_state"]) if man.get("refresh_state") else None
    review = None
    if st:
        now = json.loads((st / "tracker" / "now.json").read_text(encoding="utf-8"))
        maps = read_rows(st / "mappings.csv")[1] if (st / "mappings.csv").exists() else []
        cancelled = cancelled_set(st)
        excl = (summary_excl or set())
        if summary_excl is not None and cancelled != excl:
            raise BuildError(f"the refresh state's cancelled statuses {sorted(cancelled)} differ from the baseline summary's "
                             f"excluded statuses {sorted(excl)}: one set must govern both (init_state.py --cancelled-status)")
        live = {k: v for k, v in now.items() if (v.get("status") or "").lower() not in cancelled}
        traced = {k for r in reqs.values() for k in r["keys"]}
        for r in reqs.values():
            gone = [k for k in r["keys"] if k in now and k not in live]
            if gone:
                r["keys"], r["dropped"] = [k for k in r["keys"] if k not in gone], gone
                if not r["keys"]:
                    r["cov"] = "none"
                elif r["cov"] == "full":
                    r["cov"] = "partial"
        atomic_write(st / "requirement-ids.json", json.dumps(sorted(reqs), ensure_ascii=False) + "\n")
        ack = load(st / "state.json", {}).get("acknowledged_mappings") or {}
        mapped, extra, problems, unlinked = set(), collections.defaultdict(list), {}, {}
        for m in maps:
            k, effect = m.get("key", ""), (m.get("effect") or "").strip()
            ids = split_ids(m.get("req_ids"))
            unknown = [q for q in ids if q not in reqs]
            ids = [q for q in ids if q in reqs]
            if k not in now:
                continue
            if unknown:
                why = f"{k} (mapped: {effect}) names requirement id(s) {unknown} that are in no catalogue"
            elif k not in live:
                why = f"{k} (mapped: {effect}) is cancelled"
            elif m.get("text_hash") != now[k].get("text_hash"):
                why = f"{k} text changed since it was mapped ({effect}); re-map it"
            elif not lifts(effect):
                why = f"{k}: {effect}"
            else:
                why = None
            if k in live and m.get("text_hash") == now[k].get("text_hash") and ids and not unknown:
                mapped.add(k)
            if why:
                snap = snapshot(now[k], m)
                stale = m.get("text_hash") != now[k].get("text_hash")
                if (ids or stale or unknown or effect_kind(effect) != "no requirement") and ack.get(k) != snap:
                    problems[k] = snap
                    for q in ids:
                        extra[q].append(why)
                    if not ids:
                        unlinked[k] = why
                continue
            for q in ids:
                reqs[q]["keys"] = list(dict.fromkeys(reqs[q]["keys"] + [k]))
                if reqs[q]["cov"] in ("", "none"):
                    reqs[q]["cov"] = "partial"
        by_key = {m.get("key", ""): m for m in maps}
        atomic_write(st / "traced-keys.json", json.dumps(sorted(traced, key=key_sort)) + "\n")
        unmapped = {d["key"]: f"{d['key']} is not mapped at its current text; map it"
                    for d in load(st / "tomap.json", []) if isinstance(d, dict) and d.get("key") in live
                    and by_key.get(d["key"], {}).get("text_hash") != now[d["key"]].get("text_hash")
                    and d["key"] not in problems and d["key"] not in traced}
        info.update({k: {"summary": v.get("summary", ""), "status": v.get("status", "")} for k, v in now.items()})
        keep = [k for k in unref if k not in now or (k in live and k not in mapped)]
        new = sorted((k for k, v in live.items() if (not v.get("in_export") or v.get("reopened")) and k not in mapped
                      and k not in traced), key=key_sort)
        unref[:] = keep + [k for k in new if k not in keep]
        flags_p = st / "flags.json"
        flags = json.loads(flags_p.read_text(encoding="utf-8")) if flags_p.exists() else {}
        by_id = {(s["kind"], s.get("id")): s for s in man["sources"]}
        for kind, sec in (("deck", "decks"), ("whiteboard", "whiteboards")):
            stray = [i for i in (flags.get(sec) or {}) if (kind, i) not in by_id]
            if stray:
                raise BuildError(f"flags.json has {kind} check(s) {stray} that match no manifest source of kind "
                                 f"{kind!r} by id (sources: {[(s['kind'], s.get('id')) for s in man['sources']]}); "
                                 "give the source \"id\": the id passed to init_state.py")
        base = load(st / "baseline.json", {})
        board_ids = {i: set((b or {}).get("widgets") or {}) for i, b in (base.get("whiteboards") or {}).items()}
        unchecked = [f"{s['name']} ({s['kind']} {s.get('id')})" for s in man["sources"]
                     for sec in [CHECKED_IN.get(s["kind"])]
                     if sec and s.get("id") not in (flags.get(sec) or {})]
        for u in unchecked:
            warn.append(f"{u} was never checked against the baseline: run source_check.py on the current file")
        pulled = load(st / "state.json", {}).get("last_pull")
        by_hand, hand_due = flags.get("by_hand") or {}, []
        for s in man["sources"]:
            sid = s.get("id") or s["name"]
            done = (by_hand.get(sid) or {}).get("checked_at", "")
            if s["kind"] not in CHECKED_IN and s["kind"] != "tracker" and (not done or (pulled and done <= pulled.get("at", ""))):
                hand_due.append(sid)
                unchecked.append(f"{s['name']} ({s['kind']} {sid}, no checker: re-read it by hand)")
                warn.append(f"{s['name']} ({s['kind']}) is not checked by a light refresh: re-read it, then "
                            f"accept.py STATE source --id {sid}")
        if not pulled:
            unchecked.append("tracker (never pulled)")
            warn.append("the tracker was never pulled into this state: pull and run tracker_merge.py")
        review = (st / "review.json", review_list(reqs, flags, ev, src_of, extra, now, problems, board_ids,
                                                  unlinked, unchecked, unmapped, pulled, hand_due))
    cur_p = first_existing(run, man.get("curated"), str(st / "curated.json") if st else None)
    cur = json.loads(cur_p.read_text(encoding="utf-8")) if cur_p else {}
    for q, v in (cur.get("coverage_overrides") or {}).items():
        if q not in reqs:
            warn.append(f"coverage override for unknown requirement {q}")
            continue
        if v.get("coverage") not in ("full", "partial", "none") or not (v.get("reason") or "").strip():
            raise BuildError(f"coverage override {q}: needs coverage full|partial|none and a reason")
        reqs[q]["cov"], reqs[q]["note"] = v["coverage"], clean(v["reason"])
    return list(cur.get("conflicts") or []), review


def review_list(reqs, flags, ev, src_of, extra=None, now=None, problems=None, board_ids=None, unlinked=None,
                unchecked=None, unmapped=None, pulled=None, hand_due=None):
    now, board_ids = now or {}, board_ids or {}
    out, referenced = [], {k for r in reqs.values() for k in r["keys"] + r.get("dropped", [])}
    cited_slides, named_items = collections.defaultdict(set), collections.defaultdict(set)
    for r in reqs.values():
        why = list((extra or {}).get(r["id"], []))
        keys = r["keys"] + r.get("dropped", [])
        for e in r["eids"]:
            s, row = src_of.get(e.rsplit("-", 1)[0]), ev.get(e)
            if not s or not row:
                continue
            if s["kind"] == "deck":
                f = (flags.get("decks") or {}).get(s.get("id")) or {}
                nums = slide_numbers(row["locator"])
                cited_slides[s.get("id")].update(nums)
                if not nums and (f.get("changed_slides") or f.get("new_slides") or f.get("moved_slides")):
                    why.append(f"{s['name']}: the deck changed and the citation names no slide number")
                for n in nums:
                    if n in f.get("changed_slides", []):
                        why.append(f"{s['name']}: slide {n} changed")
                    why += [f"{s['name']}: slide {n} moved to {mv.get('to')}" for mv in f.get("moved_slides", [])
                            if mv.get("from") == n]
            if s["kind"] == "whiteboard":
                f = (flags.get("whiteboards") or {}).get(s.get("id")) or {}
                cited = row["locator"] + " " + row["url"]
                parents, old_parents = f.get("parents") or {}, f.get("old_parents") or {}
                for w in f.get("changed", []) + f.get("deleted", []) + f.get("added", []):
                    p = next((x for x in area_chain(parents.get(w)) + area_chain(old_parents.get(w)) if names(cited, x)), None)
                    if not w or not (names(cited, w) or p):
                        continue
                    named_items[s.get("id")].add(w)
                    added = w in f.get("added", [])
                    if names(cited, w):
                        why.append(f"{s['name']}: item {w} changed or deleted")
                    else:
                        why.append(f"{s['name']}: item {w} {'added to' if added else 'in'} cited area {p}"
                                   f"{'' if added else ' changed or deleted'}")
                known = board_ids.get(s.get("id"), set()) | set(f.get("changed", []) + f.get("deleted", []) + f.get("added", []))
                tokens = set(re.findall(r"[\w-]+", cited))
                if (f.get("changed") or f.get("deleted") or f.get("added")) and not any(
                        w in tokens if re.fullmatch(r"[\w-]+", w) else names(cited, w) for w in known):
                    why.append(f"{s['name']}: the whiteboard changed and the citation names no item id")
        why += [f"{k} {said}" for name, said, _ in FLAG_LISTS for k in flags.get(name, []) if k in keys]
        if why:
            out.append({"req": r["id"], "why": sorted(set(why))})
    added = {n: f.get("added_text", {}) for n, f in (flags.get("whiteboards") or {}).items() if f.get("added_text")}
    new_slides = {}
    for n, f in (flags.get("decks") or {}).items():
        edit_of = {x.get("now"): x.get("cited") for x in f.get("edited", [])}
        left = [x for x in f.get("new_slides", f.get("inserted_slides", [])) if edit_of.get(x) not in cited_slides[n]]
        if left:
            new_slides[n] = left
    uncited_items = {}
    for n, f in (flags.get("whiteboards") or {}).items():
        left = {w: (f.get("changed_text") or {}).get(w, {}) for w in f.get("changed", []) if w not in named_items[n]}
        if left:
            uncited_items[n] = left
    return {"requirements": out, "whiteboard_added": added, "deck_new_slides": new_slides,
            "whiteboard_changed_uncited": uncited_items,
            "mapping_problems_unlinked": dict(sorted((unlinked or {}).items(), key=lambda x: key_sort(x[0]))),
            "sources_unchecked": list(unchecked or []),
            "tracker_unmapped": dict(sorted((unmapped or {}).items(), key=lambda x: key_sort(x[0]))),
            "checked": {f"{sec[:-1]} {i}": f"{f.get('checked_at', 'unknown time')}{' (accepted)' if f.get('accepted') else ''}"
                        for sec in ("decks", "whiteboards") for i, f in sorted((flags.get(sec) or {}).items())}
                       | {f"source {i}": f"{f.get('checked_at', 'unknown time')} (re-read by hand)"
                          for i, f in sorted((flags.get("by_hand") or {}).items())}
                       | ({"tracker": f"{pulled.get('at', 'unknown time')} ({pulled.get('items', '?')} items)"} if pulled else {}),
            "unreferenced_text_changed": sorted({k for name, _, may in FLAG_LISTS if may for k in flags.get(name, [])
                                                 if k not in referenced}, key=key_sort),
            "reviewed": {"decks": {i: {"md5": f.get("md5")} for i, f in (flags.get("decks") or {}).items()},
                         "whiteboards": {i: {"md5": f.get("md5")} for i, f in (flags.get("whiteboards") or {}).items()},
                         "tracker": dict({k: {x: snapshot(now.get(x)) for x in flags.get(k, [])}
                                          for k, _, _ in FLAG_LISTS}, mappings=dict(problems or {})),
                         "by_hand": list(hand_due or []), "pull": (pulled or {}).get("at")}}


def area_chain(v):
    """The areas an item is in, nearest first (flags written before areas nested hold one parent id)."""
    return [v] if isinstance(v, str) else list(v or [])


def names(text, wid):
    """True when the citation text names the whiteboard item id as a whole token."""
    return bool(re.search(rf"(?<![\w-]){re.escape(wid)}(?![\w-])", text))


def link_keys(page, rx, base):
    """Link every tracker key in visible text: never inside a tag (attributes), an existing link, script or style."""
    parts = re.split(r"(<a\b.*?</a>|<script\b.*?</script>|<style\b.*?</style>|<[^>]*>)", page, flags=re.S | re.I)
    for i in range(0, len(parts), 2):
        parts[i] = rx.sub(lambda m: f'<a href="{E(base + m[0])}" target="_blank" rel="noopener">{m[0]}</a>', parts[i])
    return "".join(parts)


def src_cell(r, s, ev, src_of, stats=None):
    mine = [e for e in r["eids"] if src_of.get(e.rsplit("-", 1)[0]) is s and e in ev]
    if not mine:
        return ""
    links, tips = {}, []
    for n, e in enumerate(mine, 1):
        row = ev[e]
        loc = locator_text(row["locator"])
        tip = (f"{loc}: {row['quote']}" if loc else row["quote"])[:600]
        tips.append(tip)
        nums = slide_numbers(loc or cited_locator(row["locator"])) if s["kind"] == "deck" else []
        label = (f"slide {nums[0]}" if len(nums) == 1 else "slides " + ", ".join(map(str, nums))) if nums else str(n)
        url = row["url"] if is_url(row.get("url")) else ""
        links.setdefault((label, url), tip)
        if stats is not None:
            stats["linked" if url else "unlinked"] += 1
    parts = [f'<a href="{E(u)}" target="_blank" rel="noopener" title="{E(t)}">{E(l)}</a>' if u
             else f'<span class="nolink" title="{E(t)}">{E(l)}</span>' for (l, u), t in links.items()]
    return f'<span class="ok" title="{E(chr(10).join(tips)[:1500])}">✓</span> ' + " ".join(parts)


def link_note(stats, keys_linked):
    """What the page links, stated only as far as it is true."""
    n, linked = stats["linked"] + stats["unlinked"], stats["linked"]
    if not n:
        ev = "No requirement cites a source item other than the tracker."
    elif linked == n:
        ev = f"Every cited source item ({n}) links to its source; hover for the locator and the exact quote."
    else:
        ev = (f"{linked} of {n} cited source items link to their source; the other {n - linked} have no addressable "
              "URL (dotted underline): hover for the locator and the exact quote.")
    return ev + (" Tracker keys link to the tracker." if keys_linked else " Tracker keys are not linked (no browse URL).")


def n_of(n, word):
    return f"{n} {word}" + ("" if n == 1 else "s")


def md_cell(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(clean(s)))


def render(run, man, reqs, order, cols, tracker_src, ev, src_of, unref, info, conflicts_extra, stray):
    types = list(dict.fromkeys(c["type"] for c in man["catalogues"]))
    by_type = {t: [reqs[i] for i in order if reqs[i]["type"] == t] for t in types}
    tid = {t: "t-" + re.sub(r"\W+", "-", t.lower()) for t in types}
    head = ("<tr><th>ID</th><th>Requirement</th>" + "".join(f"<th>{E(s['name'])}</th>" for s in cols)
            + f"<th>{E(tracker_src[0]['name'] if tracker_src else 'Tracker')} coverage</th><th>Tracker issues</th></tr>")

    stats = collections.Counter()

    def tr(r):
        note = f'<div class="note">{E(r["note"][:300])}</div>' if r["note"] and r["cov"] != "full" else ""
        c = r["cov"] or "nt"
        return (f'<tr><td class="id">{E(r["id"])}</td><td>{E(r["stmt"])}{note}</td>'
                + "".join(f"<td>{src_cell(r, s, ev, src_of, stats)}</td>" for s in cols)
                + f'<td class="cov c-{c}">{COV_LABEL[r["cov"]]}</td><td class="keys">{E(" ".join(r["keys"]))}</td></tr>')

    def table(rows, name):
        body, n = [], 2 + len(cols) + 2
        for g in dict.fromkeys(r["group"] for r in rows):
            if g:
                body.append(f'<tr class="grp"><td colspan="{n}">{E(g)}</td></tr>')
            body += [tr(r) for r in rows if r["group"] == g]
        return (f'<input class="filter" data-t="{name}" placeholder="Filter rows">'
                f'<div class="tw"><table id="{name}"><thead>{head}</thead><tbody>{"".join(body)}</tbody></table></div>')

    tables = {t: table(by_type[t], tid[t] + "-tbl") for t in types}
    cnt = {t: collections.Counter(r["cov"] for r in rows) for t, rows in by_type.items()}
    backed = {t: {s["name"]: sum(bool(src_cell(r, s, ev, src_of)) for r in rows) for s in cols} for t, rows in by_type.items()}
    no_issue = [r for i in order for r in [reqs[i]] if not r["keys"]]
    cf_head, cf_rows = conflict_rows(run, man, conflicts_extra)
    tracker_name = tracker_src[0]["name"] if tracker_src else "the tracker"

    def cov_txt(t):
        c = cnt[t]
        return (f"{t}: {c['full']} full, {c['partial']} partial, {c['none']} none"
                + (f", {c['']} not traced" if c[""] else ""))
    bullets = [
        "<b>Documented:</b> " + ", ".join(f'<a href="#{tid[t]}">{len(by_type[t])} {E(t)}</a>' for t in types) + ".",
        f"<b>{E(tracker_name)}:</b> " + "; ".join(E(cov_txt(t)) for t in types) + ".",
        "<b>Sources:</b> " + "; ".join(E(f"{s['name']} backs {sum(backed[t][s['name']] for t in types)} of {len(order)} requirements")
                                         for s in cols) + "." if cols else "<b>Sources:</b> no source other than the tracker.",
        f'<b>Gaps:</b> <a href="#no-issue">{n_of(len(no_issue), "requirement")} with no tracker issue</a>'
        + (f'; <a href="#unref">{n_of(len(unref), "tracker issue")} referenced by no requirement</a>' if unref else "") + ".",
    ]
    if cf_rows:
        bullets.append(f'<b>Conflicts:</b> <a href="#conflicts">{n_of(len(cf_rows), "conflict")} between the sources</a>.')
    counts = ("<table class='k'><thead><tr><th>Type</th><th>Documented</th>" + "".join(f"<th>{E(s['name'])}</th>" for s in cols)
              + "<th>Full</th><th>Partial</th><th>None</th><th>Not traced</th></tr></thead><tbody>"
              + "".join(f"<tr><td>{E(t)}</td><td>{len(by_type[t])}</td>" + "".join(f"<td>{backed[t][s['name']]}</td>" for s in cols)
                        + f"<td>{cnt[t]['full']}</td><td>{cnt[t]['partial']}</td><td>{cnt[t]['none']}</td><td>{cnt[t]['']}</td></tr>"
                        for t in types) + "</tbody></table>")
    sections = [("short", "In short",
                 f'<p class="lead">The request, verbatim:</p><blockquote>{E(man["request_verbatim"])}</blockquote>'
                 f'<ul class="tight">{"".join(f"<li>{b}</li>" for b in bullets[:5])}</ul>{counts}'
                 f'<p class="note">Coverage means a {E(tracker_name)} item states the requirement; it does not mean the work '
                 f"is built. {E(link_note(stats, bool((man.get('tracker') or {}).get('browse_url'))))}</p>")]
    for t in types:
        sections.append((tid[t], f"{t} requirements ({len(by_type[t])})", tables[t]))
    sections.append(("no-issue", f"Requirements with no tracker issue ({len(no_issue)})",
                     "<div class='tw'><table><thead><tr><th>ID</th><th>Type</th><th>Requirement</th><th>Coverage</th></tr></thead><tbody>"
                     + "".join(f'<tr><td class="id">{E(r["id"])}</td><td>{E(r["type"])}</td><td>{E(r["stmt"])}</td>'
                               f'<td class="cov c-{r["cov"] or "nt"}">{COV_LABEL[r["cov"]]}</td></tr>' for r in no_issue)
                     + "</tbody></table></div>"))
    if unref:
        by_st = collections.Counter(info.get(k, {}).get("status", "") or "unknown" for k in unref)
        sections.append(("unref", f"Tracker issues no requirement references ({len(unref)})",
                         "<p>" + E(", ".join(f"{n} {s}" for s, n in sorted(by_st.items()))) + ".</p>"
                         "<div class='tw'><table><thead><tr><th>Issue</th><th>Summary</th><th>Status</th></tr></thead><tbody>"
                         + "".join(f'<tr><td class="id">{E(k)}</td><td>{E(info.get(k, {}).get("summary", ""))}</td>'
                                   f'<td>{E(info.get(k, {}).get("status", ""))}</td></tr>' for k in unref)
                         + "</tbody></table></div>"))
    if cf_rows:
        sections.append(("conflicts", f"Conflicts between sources ({len(cf_rows)})",
                         "<div class='tw'><table><thead><tr>" + "".join(f"<th>{E(h)}</th>" for h in cf_head)
                         + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{md_cell(c)}</td>" for c in row) + "</tr>"
                                                            for row in cf_rows) + "</tbody></table></div>"))
    src_lines = []
    for s in man["sources"]:
        mine = [v for e, v in ev.items() if src_of.get(e.rsplit("-", 1)[0]) is s]
        dates = sorted(d for v in mine for d in re.findall(r"\b\d{4}-\d{2}-\d{2}\b", v["date"]))
        span = f", dated {dates[0]}" + (f" to {dates[-1]}" if dates[-1] != dates[0] else "") if dates else ""
        src_lines.append(f"<li><b>{E(s['name'])}</b> ({E(s['kind'])}): {len(mine)} evidence rows{E(span)}.</li>")
    how = (f'<ul class="tight">{"".join(src_lines)}'
           f"<li>Tracker coverage per requirement is measured by script over the merged trace; the counts are checked "
           "against the trace's coverage summary before this page is written.</li>"
           + (f"<li>{len(stray)} traced ids are in no requirement list and are not shown.</li>" if stray else "")
           + f"<li>Generated {datetime.date.today().isoformat()} from run {E(run.resolve().name)}. Draft until signed off.</li></ul>")
    sections.append(("how", "How this was made", how))
    nav = "".join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t, _ in sections)
    body = "".join(f'<section id="{i}"><h2>{E(t)}</h2>{c}</section>' for i, t, c in sections)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
            f'<title>{E(man["title"])}</title><style>{CSS}</style></head><body><nav><div class="tt">Contents</div><ul>{nav}</ul></nav>'
            f'<main><h1>{E(man["title"])}</h1>{body}</main><script>{JS}</script></body></html>\n')


def conflict_rows(run, man, extra):
    head, rows = [], []
    if man.get("conflicts"):
        lines = path_in(run, man["conflicts"]).read_text(encoding="utf-8").splitlines()
        for line in lines:
            s = line.strip()
            if s.startswith("| CF-"):
                rows.append(cells_of(s))
            elif s.startswith("|") and not rows and not set(s) <= set("|-: "):
                head = cells_of(s)
    if extra:
        keys = head or list(extra[0])
        pos = {re.sub(r"\W+", "_", h.lower()).strip("_"): i for i, h in enumerate(keys)}
        for c in extra:
            row = [""] * len(keys)
            for k, v in c.items():
                i = pos.get(re.sub(r"\W+", "_", k.lower()).strip("_"))
                if i is not None:
                    row[i] = str(v)
            row[0] = row[0] or str(c.get("id", ""))
            rows.append(row)
        head = keys
    width = max([len(head)] + [len(r) for r in rows]) if rows else 0
    return (head + [""] * (width - len(head)), [r + [""] * (width - len(r)) for r in rows])


CSS = """body{margin:0;font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;color:#1d2433;background:#f6f7f9;display:flex}
nav{position:sticky;top:0;align-self:flex-start;width:230px;height:100vh;overflow:auto;padding:20px 14px;background:#fff;
border-right:1px solid #e3e6eb;box-sizing:border-box;font-size:13px}nav ul{list-style:none;margin:0;padding:0}
nav li a{display:block;padding:4px 6px;color:#33415c;text-decoration:none;border-radius:4px}nav li a:hover{background:#eef2f8}
.tt{font-weight:700;margin-bottom:8px}main{flex:1;max-width:1300px;padding:24px 32px}h1{font-size:24px;margin:0 0 16px}
section{background:#fff;border:1px solid #e3e6eb;border-radius:8px;padding:16px 20px;margin:0 0 18px}h2{font-size:19px;margin:0 0 10px}
blockquote{margin:6px 0 12px;padding:8px 14px;border-left:4px solid #5b7bd5;background:#f2f5fc}ul.tight li{margin:3px 0}
.lead{margin:0;color:#555}.note{font-size:12.5px;color:#666;margin-top:3px}.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{border-bottom:1px solid #e8eaee;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#f3f5f8;position:sticky;top:0}td.id{white-space:nowrap;font-weight:600}td.keys{font-size:12.5px;max-width:200px}
td.cov{white-space:nowrap}.c-full{background:#e6f5ea}.c-partial{background:#fff4d1}.c-none{background:#fde6e3}.c-nt{background:#efefef}
tr.grp td{background:#eef2f8;font-weight:700}table.k{width:auto;margin:10px 0}span[title]{cursor:help}.ok{color:#1b7f3b;font-weight:700}
.nolink{border-bottom:1px dotted #999}input.filter{margin:4px 0 8px;padding:6px 8px;width:320px;border:1px solid #ccd;border-radius:4px}
a{color:#2f5bb7}"""
JS = """document.querySelectorAll('input.filter').forEach(i=>i.addEventListener('input',()=>{const q=i.value.toLowerCase();
document.querySelectorAll('#'+i.dataset.t+' tbody tr').forEach(r=>{r.style.display=r.classList.contains('grp')||
r.textContent.toLowerCase().includes(q)?'':'none'})}));"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--manifest", type=Path, help="default RUN_DIR/06-final/baseline-manifest.json")
    ap.add_argument("--out", type=Path, help="default RUN_DIR/06-final/baseline.html")
    a = ap.parse_args()
    run = a.run_dir
    manifest = a.manifest or run / "06-final" / "baseline-manifest.json"
    try:
        page, warn, review, reqs = build(run, manifest)
    except (BuildError, OSError, ValueError, csv.Error) as e:
        sys.exit(f"ERROR: {e}")
    for w in warn:
        print("WARN ", w)
    out = a.out or run / "06-final" / "baseline.html"
    atomic_write(out, page)
    if review is not None:
        path, data = review
        atomic_write(path, json.dumps(data, ensure_ascii=False, indent=1) + "\n")
        slides = sum(len(v) for v in data["deck_new_slides"].values())
        items = sum(len(v) for v in data["whiteboard_added"].values())
        changed = sum(len(v) for v in data["whiteboard_changed_uncited"].values())
        unlinked, unchecked = len(data["mapping_problems_unlinked"]), len(data["sources_unchecked"])
        unmapped = len(data["tracker_unmapped"])
        n = (len(data["requirements"]) + len(data["unreferenced_text_changed"]) + slides + items + changed + unlinked
             + unchecked + unmapped)
        print(f"NEEDS REVIEW: {n} ({len(data['requirements'])} requirements whose source changed, "
              f"{len(data['unreferenced_text_changed'])} re-worded or re-opened items no requirement references, {slides} new slides "
              f"no citation covers, {items} new whiteboard items, {changed} changed whiteboard items no citation names, "
              f"{unlinked} item mappings to review, {unchecked} sources never checked, {unmapped} items not mapped) "
              f"-> {path}")
        for i, when in data["checked"].items():
            print(f"checked {i}: {when}")
    cov = collections.Counter(r["cov"] or "not traced" for r in reqs.values())
    print(f"{len(reqs)} requirements, coverage {dict(sorted(cov.items()))}")
    print(f"{out.stat().st_size:>10}  {out}")


if __name__ == "__main__":
    main()
