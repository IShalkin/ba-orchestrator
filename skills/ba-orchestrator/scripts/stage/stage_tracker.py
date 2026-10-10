#!/usr/bin/env python3
"""Export issues from a tracker with a Jira-compatible REST API v2 into staged, readable files.

Usage:
  python stage_tracker.py OUT_DIR --base-url URL --jql JQL --token-env VAR --ac-field FIELD
         [--fields LIST] [--epic-field FIELD] [--sprint-field FIELD] [--auth bearer|basic --user NAME]
         [--page-size N] [--part-kb N]

Pages GET <base>/rest/api/2/search with startAt/maxResults until every issue is read. The token is read
from the environment variable named by --token-env, never from the command line. The acceptance-criteria
field must be NAMED (--ac-field customfield_NNNNN, or "none"): on some servers "*all" does not return every
custom field, which reads as "no acceptance criteria". HTTPS is verified against the default trust store
plus SSL_CERT_FILE / REQUESTS_CA_BUNDLE when set. The base URL must be https:// (--allow-http to override),
and a redirect to another scheme, host or port is refused, so the token never leaves the named server.
OUT_DIR must be absent or empty, so a re-export never mixes with older parts.

Writes OUT_DIR/issues.json (raw issues, sorted by key), OUT_DIR/index.md (status and type counts, then one
row per issue: key, type, status, epic, labels, sprint, assignee, summary) and OUT_DIR/bodies-NNN.md
(description, acceptance criteria and links per issue, parts of at most --part-kb KB).
Exit 0 = exported, 1 = HTTP, TLS or response failure, 2 = usage.
"""
import argparse, base64, json, os, re, ssl, sys, urllib.error, urllib.parse, urllib.request
from collections import Counter
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

DEFAULT_FIELDS = "summary,issuetype,status,labels,assignee,parent,description,issuelinks,created,updated"


def tls_context():
    ctx = ssl.create_default_context()  # default store kept; an extra bundle is added, never a replacement
    for var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE"):
        if os.environ.get(var):
            ctx.load_verify_locations(os.environ[var])
    return ctx


class SameOrigin(urllib.request.HTTPRedirectHandler):
    """urllib copies the Authorization header onto every redirect: refuse any that changes the origin."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        o, n = urllib.parse.urlsplit(req.full_url), urllib.parse.urlsplit(newurl)
        if (o.scheme, o.hostname, o.port) != (n.scheme, n.hostname, n.port):
            raise urllib.error.HTTPError(newurl, code, f"redirect to another origin refused ({n.scheme}://{n.netloc}); "
                                         "the token was not sent there", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_all(a, headers, ctx):
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx), SameOrigin())
    issues, start = [], 0
    while True:
        q = urllib.parse.urlencode({"jql": a.jql, "startAt": start, "maxResults": a.page_size, "fields": a.fields})
        url = a.base_url.rstrip("/") + a.api_path + "?" + q
        req = urllib.request.Request(url, headers=headers)
        with opener.open(req, timeout=120) as r:
            ctype, body = r.headers.get("Content-Type", ""), r.read()
        if "json" not in ctype:
            raise ValueError(f"non-JSON response ({ctype or 'no content type'}) at startAt={start}; "
                             f"a login or error page? First bytes: {body[:200]!r}")
        page = json.loads(body)
        got = page.get("issues", [])
        issues += got
        start += len(got)
        print(f"page startAt={page.get('startAt', start - len(got))}: {len(got)} issues, total {page.get('total')}")
        total = page.get("total")
        if not got or (total is not None and start >= total):
            return issues


def text(v):
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, dict) and "value" in v:
        return str(v["value"])
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


def name(v):
    if isinstance(v, dict):
        return v.get("displayName") or v.get("name") or v.get("key") or v.get("value") or ""
    return "" if v is None else str(v)


def sprints(v):
    out = []
    for s in v if isinstance(v, list) else [v] if v else []:
        if isinstance(s, dict):
            out.append(s.get("name", ""))
        else:
            m = re.search(r"name=([^,\]]*)", str(s))
            out.append(m.group(1) if m else str(s))
    return ", ".join(out)


def key_order(k):
    m = re.match(r"(.*?)-(\d+)$", k)
    return (m.group(1), int(m.group(2))) if m else (k, 0)


def row(i, a):
    f = i.get("fields", {})
    epic = text(f.get(a.epic_field)) if a.epic_field else ""
    if not epic and isinstance(f.get("parent"), dict):
        epic = f["parent"].get("key", "")
    return [i["key"], name(f.get("issuetype")), name(f.get("status")), epic, ", ".join(f.get("labels") or []),
            sprints(f.get(a.sprint_field)) if a.sprint_field else "", name(f.get("assignee")), f.get("summary") or ""]


def links(f):
    out = []
    for l in f.get("issuelinks") or []:
        t = l.get("type", {})
        if "outwardIssue" in l:
            out.append(f"{t.get('outward', 'links to')} {l['outwardIssue'].get('key')}")
        if "inwardIssue" in l:
            out.append(f"{t.get('inward', 'linked from')} {l['inwardIssue'].get('key')}")
    return out


def body(i, a):
    f = i.get("fields", {})
    ac = "(acceptance-criteria field not requested: --ac-field none)" if a.ac_field == "none" else (
        text(f.get(a.ac_field)) or "(empty)")
    lk = links(f)
    return (f"## {i['key']}: {f.get('summary') or ''}\n\n"
            f"- type: {name(f.get('issuetype'))}\n- status: {name(f.get('status'))}\n"
            f"- created: {f.get('created', '')}\n- updated: {f.get('updated', '')}\n\n"
            f"### Description\n\n{text(f.get('description')) or '(empty)'}\n\n"
            f"### Acceptance criteria ({a.ac_field})\n\n{ac}\n\n"
            f"### Links\n\n" + ("\n".join(f"- {x}" for x in lk) if lk else "(none)") + "\n\n")


def cell(v):
    return str(v).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--jql", required=True)
    ap.add_argument("--token-env", required=True, help="NAME of the environment variable holding the token")
    ap.add_argument("--ac-field", required=True, help='acceptance-criteria field id, or "none"')
    ap.add_argument("--fields", default=DEFAULT_FIELDS, help=f"comma list (default {DEFAULT_FIELDS})")
    ap.add_argument("--epic-field", help="custom field holding the epic key (default: parent key)")
    ap.add_argument("--sprint-field")
    ap.add_argument("--auth", choices=["bearer", "basic"], default="bearer")
    ap.add_argument("--user", help="user name for --auth basic")
    ap.add_argument("--api-path", default="/rest/api/2/search")
    ap.add_argument("--page-size", type=int, default=100)
    ap.add_argument("--part-kb", type=int, default=400)
    ap.add_argument("--allow-http", action="store_true", help="permit an http:// base URL (the token travels in clear)")
    a = ap.parse_args()
    if urllib.parse.urlsplit(a.base_url).scheme != "https" and not a.allow_http:
        ap.error("--base-url must be https:// (or pass --allow-http)")
    if a.out_dir.exists() and any(a.out_dir.iterdir()):
        ap.error(f"{a.out_dir} is not empty; a re-export into it would mix with older parts")
    token = os.environ.get(a.token_env)
    if not token:
        ap.error(f"environment variable {a.token_env} is empty or unset")
    if a.auth == "basic" and not a.user:
        ap.error("--auth basic needs --user")
    fields = [x.strip() for x in a.fields.split(",") if x.strip()]
    for extra in (a.ac_field, a.epic_field, a.sprint_field):
        if extra and extra != "none" and extra not in fields:
            fields.append(extra)
    a.fields = ",".join(fields)
    auth = ("Basic " + base64.b64encode(f"{a.user}:{token}".encode()).decode()) if a.auth == "basic" \
        else f"Bearer {token}"
    try:
        issues = fetch_all(a, {"Authorization": auth, "Accept": "application/json"}, tls_context())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR: HTTP {e.code} {e.reason}: {e.read()[:300]!r}")
    except (urllib.error.URLError, ssl.SSLError, OSError, ValueError) as e:
        sys.exit(f"ERROR: {e}")
    issues.sort(key=lambda i: key_order(i["key"]))
    if a.ac_field != "none" and issues and not any(a.ac_field in i.get("fields", {}) for i in issues):
        print(f"WARNING: no issue returned field {a.ac_field}; check the field id before reading AC as empty")
    a.out_dir.mkdir(parents=True, exist_ok=True)
    written = [a.out_dir / "issues.json", a.out_dir / "index.md"]
    written[0].write_text(json.dumps(issues, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    rows = [row(i, a) for i in issues]
    counts = lambda col: ", ".join(f"{k or '?'} {n}" for k, n in sorted(Counter(r[col] for r in rows).items()))
    idx = ["# Issue export", "", f"- JQL: `{a.jql}`", f"- issues: {len(rows)}", f"- by status: {counts(2)}",
           f"- by type: {counts(1)}", f"- acceptance-criteria field: {a.ac_field}", "",
           "| key | type | status | epic | labels | sprint | assignee | summary |", "|---|---|---|---|---|---|---|---|"]
    idx += ["| " + " | ".join(cell(v) for v in r) + " |" for r in rows]
    written[1].write_text("\n".join(idx) + "\n", encoding="utf-8")
    parts, cur, limit = [], "", a.part_kb * 1024
    for i in issues:
        b = body(i, a)
        if cur and len((cur + b).encode("utf-8")) > limit:
            parts.append(cur)
            cur = ""
        cur += b  # ponytail: one issue larger than the limit stays whole in its own part
    if cur:
        parts.append(cur)
    for n, p in enumerate(parts, 1):
        path = a.out_dir / f"bodies-{n:03d}.md"
        path.write_text(f"# Issue bodies, part {n} of {len(parts)}\n\n" + p, encoding="utf-8")
        written.append(path)
    print(f"{len(issues)} issues")
    for p in written:
        print(f"{p.stat().st_size:>10}  {p}")


if __name__ == "__main__":
    main()
