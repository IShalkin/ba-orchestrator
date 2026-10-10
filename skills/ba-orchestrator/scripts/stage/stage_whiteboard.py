#!/usr/bin/env python3
"""Stage a whiteboard widget export: a widget listing with absolute coordinates, and an HTML reconstruction.

Usage:
  python stage_whiteboard.py WIDGETS.json OUT_DIR [--map FIELD=PATH ...] [--name NAME]

Input: a JSON list of widgets, or an object holding that list under "value", "widgets", "data" or "items".
Writes OUT_DIR/<name>/:
  widgets.md   one row per widget: id, type, ABSOLUTE x/y (a child's x/y are relative to its parent, so parent
               offsets are added recursively), size, parent, author and dates, tag-stripped text; then every
               connector as "CONNECTS a <-> b" with its label. A connector records a link, not a direction.
  board.html   absolute-positioned boxes and connector lines, for screenshotting into tiles.

Field names: FIELDS below lists, per field, the dotted paths tried in order (list indices allowed, e.g.
"label.labels.0.text"). It covers the two common export shapes: flat (x, y, width, parentId, text, style.backgroundColor,
startRefId) and nested (position.x, geometry.width, parent.id, data.content, startItem.id). Override with
--map FIELD=PATH. Items with no id (under every path tried) and widgets nested in a "children" list are
not listed: they are counted, and any such item fails the run (fix with --map id=PATH). OUT_DIR/<name>/
must be absent or empty. Exit 0 = staged, 1 = unreadable input or skipped items.
"""
import argparse, datetime, html, json, re, sys
from collections import Counter
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

FIELDS = {
    "id": ["id"],
    "type": ["type"],
    "x": ["x", "position.x"],
    "y": ["y", "position.y"],
    "width": ["width", "geometry.width"],
    "height": ["height", "geometry.height"],
    "parent": ["parentId", "parent.id"],
    "text": ["text", "htmlText", "data.content", "data.title", "title"],
    "colour": ["style.backgroundColor", "style.fillColor", "style.color"],
    "created_by": ["createdBy.name", "createdBy.username", "createdBy.id", "createdBy"],
    "created_on": ["createdOn", "createdAt"],
    "updated_by": ["updatedBy.name", "updatedBy.username", "updatedBy.id", "modifiedBy.id", "updatedBy"],
    "updated_on": ["updatedOn", "modifiedAt", "updatedAt"],
    "start": ["startRefId", "startItem.id", "start.id"],
    "end": ["endRefId", "endItem.id", "end.id"],
    "label": ["label.labels.0.text", "label.text", "label", "captions.0.content", "title"],
}
LIST_KEYS = ("value", "widgets", "data", "items")


def get(w, path):
    cur = w
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return None
    return cur


def field(w, name, fields):
    for path in fields[name]:
        v = get(w, path)
        if v not in (None, "", []) and not isinstance(v, (dict, list)):
            return v
    return None


def plain(v):
    if v is None:
        return ""
    s = re.sub(r"<br\s*/?>|</(p|div|li|h\d)>", " ", str(v), flags=re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def when(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        secs = v / 1000 if v > 1e11 else v
        return datetime.datetime.fromtimestamp(secs, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return "" if v is None else str(v)


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def normalise(raw, fields):
    widgets = raw
    if isinstance(raw, dict):
        widgets = next((raw[k] for k in LIST_KEYS if isinstance(raw.get(k), list)), None)
    if not isinstance(widgets, list):
        raise ValueError("no widget list found (expected a list, or one under " + "/".join(LIST_KEYS) + ")")
    out, skipped = {}, 0
    for w in widgets:
        if isinstance(w, dict) and isinstance(w.get("children"), list):
            skipped += len(w["children"])  # ponytail: nested children are counted, not walked
        if not isinstance(w, dict) or field(w, "id", fields) is None:
            skipped += 1
            continue
        d = {k: field(w, k, fields) for k in fields}
        d["id"] = str(d["id"])
        for k in ("x", "y", "width", "height"):
            d[k] = num(d[k])
        for k in ("parent", "start", "end"):
            d[k] = None if d[k] is None else str(d[k])
        d["text"], d["label"] = plain(d["text"]), plain(d["label"])
        d["type"], d["colour"] = str(d["type"] or ""), plain(d["colour"])
        out[d["id"]] = d
    return out, skipped


def absolutise(ws):
    """Add parent offsets recursively; a missing parent or a cycle stops the walk and is noted."""
    for w in ws.values():
        x, y, seen, p, note = w["x"], w["y"], {w["id"]}, w["parent"], ""
        while p:
            if p in seen:
                note = "parent cycle"
                break
            if p not in ws:
                note = f"parent {p} not in export"
                break
            seen.add(p)
            x, y, p = x + ws[p]["x"], y + ws[p]["y"], ws[p]["parent"]
        w["ax"], w["ay"], w["note"] = x, y, note


def is_connector(w):
    return bool(w["start"] or w["end"]) or any(k in w["type"].lower() for k in ("arrow", "connector", "line"))


def cell(v):
    return str(v).replace("|", "\\|").replace("\n", " ")


def widgets_md(ws, name):
    boxes = sorted((w for w in ws.values() if not is_connector(w)), key=lambda w: (w["ay"], w["ax"], w["id"]))
    links = sorted((w for w in ws.values() if is_connector(w)), key=lambda w: w["id"])
    types = Counter(w["type"] for w in ws.values())
    lines = [f"# Whiteboard {name}", "", f"{len(ws)} widgets: " + ", ".join(f"{t or '?'} {n}" for t, n in
             sorted(types.items())), "", "Coordinates are absolute (parent offsets added).", "", "## Widgets", "",
             "| id | type | x | y | w | h | parent | colour | created by | created | updated by | updated | text |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for w in boxes:
        parent = (w["parent"] or "") + (f" ({w['note']})" if w["note"] else "")
        lines.append("| " + " | ".join(cell(v) for v in (
            w["id"], w["type"], f"{w['ax']:g}", f"{w['ay']:g}", f"{w['width']:g}", f"{w['height']:g}", parent, w["colour"],
            plain(w["created_by"]), when(w["created_on"]), plain(w["updated_by"]), when(w["updated_on"]),
            w["text"])) + " |")
    lines += ["", "## Connections", "", "A connection links two widgets; it is not a direction.", ""]
    for w in links:
        label = f' label "{w["label"] or w["text"]}"' if (w["label"] or w["text"]) else ""
        lines.append(f"- CONNECTS {w['start'] or '?'} <-> {w['end'] or '?'} (connector {w['id']}, {w['type']}){label}")
    if not links:
        lines.append("(none)")
    return "\n".join(lines) + "\n"


def board_html(ws, name):
    boxes = [w for w in ws.values() if not is_connector(w)]
    if not boxes:
        return "<!doctype html><title>empty</title>\n"
    x0, y0 = min(w["ax"] for w in boxes), min(w["ay"] for w in boxes)
    W = max(w["ax"] + w["width"] for w in boxes) - x0 + 20
    H = max(w["ay"] + w["height"] for w in boxes) - y0 + 20
    divs, polys = [], []
    for w in sorted(boxes, key=lambda w: (w["width"] * w["height"] < 1, -w["width"] * w["height"], w["id"])):
        divs.append(f'<div class="w" title="{html.escape(w["id"] + " " + w["type"])}" style="left:{w["ax"] - x0 + 10:g}px;'
                    f'top:{w["ay"] - y0 + 10:g}px;width:{w["width"]:g}px;height:{w["height"]:g}px'
                    + (f';background:{html.escape(w["colour"])}' if w["colour"] else "") + '">'
                    f'{html.escape(w["text"])}</div>')
    for w in sorted((w for w in ws.values() if is_connector(w)), key=lambda w: w["id"]):
        a, b = ws.get(w["start"]), ws.get(w["end"])
        if a and b:
            pts = [(a["ax"] + a["width"] / 2 - x0 + 10, a["ay"] + a["height"] / 2 - y0 + 10),
                   (b["ax"] + b["width"] / 2 - x0 + 10, b["ay"] + b["height"] / 2 - y0 + 10)]
            polys.append(f'<polyline points="{" ".join(f"{px:g},{py:g}" for px, py in pts)}"><title>'
                         f'{html.escape(w["id"] + " " + w["label"])}</title></polyline>')
    return (f'<!doctype html><meta charset="utf-8"><title>{html.escape(name)}</title><style>'
            f'body{{margin:0}}#b{{position:relative;width:{W:g}px;height:{H:g}px;font:12px sans-serif}}'
            '.w{position:absolute;box-sizing:border-box;border:1px solid #888;background:rgba(255,250,200,.85);'
            'overflow:hidden;padding:2px}svg{position:absolute;left:0;top:0;pointer-events:none}'
            'polyline{stroke:#c00;stroke-width:2;fill:none}</style><div id="b">' + "".join(divs) +
            f'<svg width="{W:g}" height="{H:g}">' + "".join(polys) + "</svg></div>\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("widgets", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--map", action="append", default=[], metavar="FIELD=PATH", help="try PATH first for FIELD")
    ap.add_argument("--name", help="output subdirectory (default: the input file stem)")
    a = ap.parse_args()
    fields = {k: list(v) for k, v in FIELDS.items()}
    for m in a.map:
        k, _, path = m.partition("=")
        if k not in fields or not path:
            sys.exit(f"ERROR: --map {m}: FIELD must be one of {', '.join(fields)}")
        fields[k].insert(0, path)
    try:
        ws, skipped = normalise(json.loads(a.widgets.read_text(encoding="utf-8")), fields)
    except (OSError, ValueError) as e:
        sys.exit(f"ERROR: cannot read {a.widgets}: {e}")
    absolutise(ws)
    name = a.name or a.widgets.stem
    out = a.out_dir / name
    if out.exists() and any(out.iterdir()):
        sys.exit(f"ERROR: {out} is not empty; staging into it would mix versions. Remove it or choose another OUT_DIR")
    out.mkdir(parents=True, exist_ok=True)
    written = [out / "widgets.md", out / "board.html"]
    written[0].write_text(widgets_md(ws, name), encoding="utf-8")
    written[1].write_text(board_html(ws, name), encoding="utf-8")
    print(f"{len(ws)} widgets, {sum(map(is_connector, ws.values()))} connectors")
    for p in written:
        print(f"{p.stat().st_size:>10}  {p}")
    if skipped:
        sys.exit(f"ERROR: {skipped} item(s) not listed (no id under the paths tried, or nested children); "
                 "the listing is incomplete. Add the export's id path with --map id=PATH")


if __name__ == "__main__":
    main()
