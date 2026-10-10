"""Behaviour tests for scripts/stage/ (deck text layer and count check, whiteboard coordinates, tracker paging,
sheets, trace merge). Tiny synthetic fixtures in a temp dir; rendering is tested only for the count check. Stdlib only."""
import csv, importlib.util, json, os, subprocess, sys, tempfile, threading, unittest, zipfile
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.dont_write_bytecode = True  # load() must not leave __pycache__ inside the skill
STAGE = Path(__file__).resolve().parent.parent / "skills" / "ba-orchestrator" / "scripts" / "stage"
P = 'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" ' \
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" ' \
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
REL = 'xmlns="http://schemas.openxmlformats.org/package/2006/relationships"'
S = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" ' \
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'


def run(script, *args, env=None):
    return subprocess.run([sys.executable, "-I", str(STAGE / script), *map(str, args)], capture_output=True,
                          text=True, env=env)


def load(script):
    spec = importlib.util.spec_from_file_location(script[:-3], STAGE / script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rels(*items):
    return f"<Relationships {REL}>" + "".join(
        f'<Relationship Id="{i}" Type="http://x/{t}" Target="{g}"/>' for i, t, g in items) + "</Relationships>"


def sp(text, ph=None):
    tag = f'<p:ph type="{ph}"/>' if ph else ""
    nv = f'<p:nvSpPr><p:cNvPr id="1" name="s"/><p:cNvSpPr/><p:nvPr>{tag}</p:nvPr></p:nvSpPr>'
    return f'<p:sp>{nv}<p:txBody><a:p><a:r><a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp>'


def make_pptx(path):
    with zipfile.ZipFile(path, "w") as z:
        # presentation order differs from part numbering on purpose: slide3 part is shown second
        z.writestr("ppt/presentation.xml", f'<p:presentation {P}><p:sldIdLst><p:sldId id="256" r:id="rId1"/>'
                   '<p:sldId id="257" r:id="rId3"/><p:sldId id="258" r:id="rId2"/></p:sldIdLst></p:presentation>')
        z.writestr("ppt/_rels/presentation.xml.rels", rels(("rId1", "slide", "slides/slide1.xml"),
                   ("rId2", "slide", "slides/slide2.xml"), ("rId3", "slide", "slides/slide3.xml")))
        z.writestr("ppt/slides/slide1.xml", f'<p:sld {P}><p:cSld><p:spTree>{sp("Title one")}{sp("Body one")}'
                   '</p:spTree></p:cSld></p:sld>')
        z.writestr("ppt/slides/slide3.xml", f'<p:sld {P} show="0"><p:cSld><p:spTree>{sp("Secret plan")}'
                   '</p:spTree></p:cSld></p:sld>')
        z.writestr("ppt/slides/slide2.xml", f'<p:sld {P}><p:cSld><p:spTree>{sp("Last slide")}'
                   f'{sp("Line one</a:t></a:r><a:br/><a:r><a:t>Line two")}</p:spTree></p:cSld></p:sld>')
        z.writestr("ppt/slides/_rels/slide1.xml.rels", rels(("rId9", "notesSlide", "../notesSlides/notesSlide1.xml")))
        z.writestr("ppt/notesSlides/notesSlide1.xml", f'<p:notes {P}><p:cSld><p:spTree>{sp("1", "sldNum")}'
                   f'{sp("Say this aloud", "body")}</p:spTree></p:cSld></p:notes>')


class DeckTest(unittest.TestCase):
    def test_text_layer_order_hidden_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            deck = Path(tmp) / "d.pptx"
            make_pptx(deck)
            r = run("stage_deck.py", deck, Path(tmp) / "out", "--render", "none")
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp) / "out" / "d"
            s1, s2, s3 = ((out / f"slide-00{n}.md").read_text(encoding="utf-8") for n in (1, 2, 3))
            self.assertIn("Title one\n\nBody one", s1)
            self.assertIn("Say this aloud", s1)
            self.assertNotIn("## Speaker notes\n\n1", s1)  # the slide-number field is not a note
            self.assertIn("(HIDDEN)", s2)
            self.assertIn("Secret plan", s2)
            self.assertIn("- hidden: no", s3)
            self.assertIn("Last slide", s3)
            self.assertIn("Line one\nLine two", s3)  # <a:br> separates the runs
            self.assertIn("hidden: [2]", r.stdout)
            self.assertIn("slide-003.md", r.stdout)
            self.assertIn("slide shapes only", s1)
            r = run("stage_deck.py", deck, Path(tmp) / "out", "--render", "none")  # re-staging into the same folder
            self.assertEqual(r.returncode, 1)
            self.assertIn("not empty", r.stderr)

    def test_count_mismatch_fails(self):
        mod = load("stage_deck.py")
        mod.check_counts(3, 3)
        with self.assertRaisesRegex(mod.StageError, "COUNT MISMATCH"):
            mod.check_counts(3, 2)
        pdf = b"%PDF-1.4\n1 0 obj<</Type /Pages /Count 2>>endobj\n2 0 obj<</Type /Page>>endobj\n" \
              b"3 0 obj<</Type/Page>>endobj\n%%EOF\n"
        self.assertEqual(mod.pdf_page_count(pdf), 2)
        import zlib
        content = zlib.compress(b"BT (/Type /Page) Tj ET")  # page text holding the literal is not a page
        objstm = zlib.compress(b"1 0 2 20 <</Type /Page>> <</Type /Page>>")
        pdf2 = (b"%PDF-1.5\n4 0 obj<</Length 9>>stream\n" + content + b"\nendstream\nendobj\n"
                b"5 0 obj<</Type /ObjStm /N 2>>stream\n" + objstm + b"\nendstream\nendobj\n"
                b"6 0 obj<</Length 9>>stream\n/Type /Page\nendstream\nendobj\n%%EOF\n")
        self.assertEqual(mod.pdf_page_count(pdf2), 2)
        raw = b"%PDF-1.5\n5 0 obj<</Type /ObjStm /N 2>>stream\n1 0 2 20 <</Type /Page>> <</Type /Page>>\nendstream\nendobj\n"
        self.assertEqual(mod.pdf_page_count(raw), 2)  # an uncompressed object stream is scanned as it is
        with tempfile.TemporaryDirectory() as tmp:
            deck, fake = Path(tmp) / "d.pptx", Path(tmp) / "x.pdf"
            make_pptx(deck)
            fake.write_bytes(pdf)
            r = run("stage_deck.py", deck, Path(tmp) / "out", "--pdf", fake)
            self.assertEqual(r.returncode, 1, r.stdout)  # 3 slides, 2 pages (or an unrenderable fake PDF)
            env = dict(os.environ, PATH=tmp)  # no soffice/libreoffice on PATH
            r = run("stage_deck.py", deck, Path(tmp) / "out2", "--render", "libreoffice", env=env)
            self.assertEqual(r.returncode, 1)
            self.assertIn("no renderer available", r.stderr)
            self.assertFalse((Path(tmp) / "out2").exists())  # nothing written, so the advised retry can reuse it
            r = run("stage_deck.py", deck, Path(tmp) / "out2", "--render", "none")
            self.assertEqual(r.returncode, 0, r.stderr)


class WhiteboardTest(unittest.TestCase):
    def test_absolute_coordinates_and_connections(self):
        widgets = {"value": [
            {"id": "area", "type": "area", "x": 100, "y": 200, "width": 500, "height": 400, "text": "Lane A"},
            {"id": "grp", "type": "shape", "x": 50, "y": 60, "width": 200, "height": 200, "parentId": "area"},
            {"id": "n1", "type": "sticky note", "x": 10, "y": 20, "width": 50, "height": 50, "parentId": "grp",
             "text": "", "htmlText": "<p>Order &amp; pay</p>", "createdBy": {"name": "Ann"}, "createdOn": 1700000000000,
             "style": {"backgroundColor": "#ffcc00"}},
            {"id": "n2", "type": "sticky note", "x": 400, "y": 300, "width": 50, "height": 50, "text": "Ship",
             "style": {"backgroundColor": "red;background-image:url(http://x/y)"}},
            {"id": "c1", "type": "arrow", "startRefId": "n1", "endRefId": "n2", "label": {"labels": [{"text": "then"}]}},
        ]}
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "board.json"
            src.write_text(json.dumps(widgets), encoding="utf-8")
            r = run("stage_whiteboard.py", src, Path(tmp) / "out")
            self.assertEqual(r.returncode, 0, r.stderr)
            md = (Path(tmp) / "out" / "board" / "widgets.md").read_text(encoding="utf-8")
            row = next(l for l in md.splitlines() if l.startswith("| n1 "))
            self.assertIn("| 160 | 280 |", row)  # 10+50+100, 20+60+200
            self.assertIn("Order & pay", row)
            self.assertIn("Ann", row)
            self.assertIn("2023-11-14T22:13:20Z", row)
            self.assertIn("#ffcc00", row)
            self.assertIn('CONNECTS n1 <-> n2 (connector c1, arrow) label "then"', md)
            html = (Path(tmp) / "out" / "board" / "board.html").read_text(encoding="utf-8")
            self.assertIn("<polyline", html)
            self.assertIn("background:#ffcc00", html)
            self.assertNotIn("url(", html)  # a colour outside the grammar never reaches the style
            self.assertIn("board.html", r.stdout)

    def test_items_without_id_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "b.json"
            src.write_text(json.dumps([{"widgetId": "a", "x": 1}, {"widgetId": "b", "x": 2}]), encoding="utf-8")
            r = run("stage_whiteboard.py", src, Path(tmp) / "out")
            self.assertEqual(r.returncode, 1)
            self.assertIn("2 item(s) not listed", r.stderr)
            self.assertFalse((Path(tmp) / "out").exists())  # nothing written, so a retry can reuse the folder
            r = run("stage_whiteboard.py", src, Path(tmp) / "out", "--map", "id=widgetId")
            self.assertEqual(r.returncode, 0, r.stderr)  # the advised retry, same folder, succeeds
            self.assertIn("| b ", (Path(tmp) / "out" / "b" / "widgets.md").read_text(encoding="utf-8"))
            src.write_text(json.dumps([{"id": "p", "children": [{"id": "c"}]}]), encoding="utf-8")
            r = run("stage_whiteboard.py", src, Path(tmp) / "out3")
            self.assertEqual(r.returncode, 1)
            self.assertIn("1 item(s) not listed", r.stderr)  # a nested child is counted, not walked


def make_xlsx(path):
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("xl/workbook.xml", f'<workbook {S}><sheets><sheet name="Reqs" sheetId="1" r:id="rId1"/>'
                   '<sheet name="Old data" sheetId="2" state="hidden" r:id="rId2"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", rels(("rId1", "worksheet", "worksheets/sheet1.xml"),
                   ("rId2", "worksheet", "/xl/worksheets/sheet2.xml")))
        z.writestr("xl/sharedStrings.xml", f'<sst {S}><si><t>id</t></si><si><r><t>tit</t></r><r><t>le</t></r></si>'
                   '<si><t>a|b</t></si><si><t>c\\|d</t></si></sst>')
        z.writestr("xl/worksheets/sheet1.xml", f'<worksheet {S}><dimension ref="A1:C2"/><sheetData>'
                   '<row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c></row>'
                   '<row r="2"><c r="A2"><v>42</v></c><c r="B2" t="s"><v>2</v></c><c r="C2" t="b"><v>1</v></c>'
                   '<c r="D2"><f>A2*2</f></c></row><row r="3"><c r="A3" t="s"><v>3</v></c></row>'
                   '</sheetData></worksheet>')
        z.writestr("xl/worksheets/sheet2.xml", f'<worksheet {S}><sheetData><row r="3"><c r="B3" t="inlineStr">'
                   '<is><t>inline</t><rPh sb="0" eb="1"><t>PHON</t></rPh></is></c></row></sheetData></worksheet>')


class SheetTest(unittest.TestCase):
    def test_two_sheets(self):
        with tempfile.TemporaryDirectory() as tmp:
            book = Path(tmp) / "b.xlsx"
            make_xlsx(book)
            r = run("stage_sheet.py", book, Path(tmp) / "out")
            self.assertEqual(r.returncode, 0, r.stderr)
            s1 = (Path(tmp) / "out" / "b" / "01-Reqs.md").read_text(encoding="utf-8")
            s2 = (Path(tmp) / "out" / "b" / "02-Old_data.md").read_text(encoding="utf-8")
            self.assertIn("- state: visible", s1)
            self.assertIn("| 1 | id | title |  |", s1)
            self.assertIn("| 2 | 42 | a\\|b | TRUE | =A2*2 |", s1)  # no cached value: the formula is kept
            self.assertIn("- state: hidden", s2)
            self.assertIn("| 3 |  | inline |", s2)  # the phonetic run is not cell text
            self.assertIn("| 3 | c\\\\\\|d |", s1)  # c\|d: the backslash is escaped, so the pipe stays escaped
        for script in ("stage_tracker.py", "stage_whiteboard.py"):  # the same table-cell escape, two more copies
            self.assertEqual(load(script).cell("c\\|d"), "c\\\\\\|d", script)


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


class MergeTraceTest(unittest.TestCase):
    def test_merge(self):
        head = ["req_id", "req_type", "capability", "jira_keys", "coverage", "jira_statuses", "mvp_class_source",
                "mvp_class_jira", "conflict_flags", "gap_note", "evidence"]
        head2 = [h.upper() if h != "coverage" else " Coverage(full|partial|none) " for h in head]
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            write_csv(t / "a.csv", [head, ["FR-1", "FR", "Order", "ABC-1..3", "full", "", "", "", "", "", "E1"],
                                    ["FR-2", "FR", "Order", "ABC-5 to ABC-6", "partial", "", "", "", "MVP_MISMATCH", "", ""]])
            write_csv(t / "b.csv", [head2, ["BR-1", "BR", "Pay", "ABC-9–10; abc-11", "none", "", "", "", "none", "", ""],
                                    ["FR-2", "FR", "Order", "ABC-1..999", "full", "", "", "", "", "", ""]])
            write_csv(t / "cat.csv", [["req_id", "title"], ["FR-1", "x"], ["FR-2", "y"], ["FR-3", "z"], ["FR-3", "z"]])
            st = lambda s: {"status": {"name": s}}
            issues = [{"key": f"ABC-{n}", "fields": st("Open")} for n in range(1, 12)]
            issues[3]["fields"] = st("Done")         # ABC-4: unreferenced, Done
            issues[7]["fields"] = st("Cancelled")    # ABC-8: unreferenced, excluded
            (t / "issues.json").write_text(json.dumps(issues), encoding="utf-8")
            args = ["--trace", t / "a.csv", t / "b.csv", "--catalogue", t / "cat.csv", "--issues", t / "issues.json"]
            r = run("merge_trace.py", t / "out", *args)
            self.assertEqual(r.returncode, 0, r.stderr)
            s = json.loads((t / "out" / "coverage-summary.json").read_text(encoding="utf-8"))
            self.assertEqual((s["rows"], s["distinct_req_ids"]), (4, 3))
            self.assertEqual(s["per_req_type"], {"BR": {"none": 1}, "FR": {"full": 1, "partial": 1}})
            self.assertEqual(s["per_capability"]["Order"], {"full": 1, "partial": 1})
            self.assertEqual([d["req_id"] for d in s["duplicates"]], ["FR-2"])
            self.assertEqual([c["req_id"] for c in s["conflict_rows"]], ["FR-2"])
            self.assertEqual(s["missing_from_trace"], ["FR-3"])
            self.assertEqual(s["not_in_catalogue"], ["BR-1"])
            self.assertEqual(s["catalogue_duplicates"], ["FR-3"])
            self.assertEqual(len(s["range_errors"]), 1)
            self.assertIn("span over 200", s["range_errors"][0]["reason"])
            u = s["unreferenced_issues"]
            self.assertEqual((u["keys"], u["by_status"]), (["ABC-4", "ABC-7"], {"Done": 1, "Open": 1}))
            self.assertEqual(s["unknown_referenced_keys"], [])
            merged = (t / "out" / "trace-merged.csv").read_text(encoding="utf-8")
            self.assertIn("ABC-9 ABC-10 ABC-11", merged)
            self.assertIn("ABC-1 ABC-2 ABC-3", merged)
            first = (t / "out" / "coverage-summary.json").read_bytes(), merged
            r = run("merge_trace.py", t / "out", *args)
            self.assertEqual(first, ((t / "out" / "coverage-summary.json").read_bytes(),
                                     (t / "out" / "trace-merged.csv").read_text(encoding="utf-8")))  # deterministic

    def test_order_ranges_coverage_and_drift(self):
        head = ["req_id", "req_type", "capability", "jira_keys", "coverage", "jira_statuses", "mvp_class_source",
                "mvp_class_jira", "conflict_flags", "gap_note", "evidence"]
        row = lambda rid, keys, cov: [rid, "FR", "Order", keys, cov, "", "", "", "", "", ""]
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            write_csv(t / "a.csv", [head, row("FR-1", "ABC-1", "Full"), row("FR-2", "ABC-10...ABC-12", "FULL")])
            write_csv(t / "b.csv", [head, row("FR-1", "ABC-2", "none"), row("FR-3", "ABC-20-22", "partial"),
                                    row("FR-4", "ABC-30 through ABC-31", "none"), row("FR-5", "ABC-40, ABC-41 and ABC-42", "full"),
                                    row("FR-6", "ABC-50..52 through XYZ-1", "none")])
            sums = []
            for order in ((t / "a.csv", t / "b.csv"), (t / "b.csv", t / "a.csv")):
                r = run("merge_trace.py", t / "out", "--trace", *order)
                self.assertEqual(r.returncode, 0, r.stderr)
                sums.append(json.loads((t / "out" / "coverage-summary.json").read_text(encoding="utf-8")))
            for s in sums:
                s.pop("inputs")
            self.assertEqual(sums[0], sums[1])  # the input order changes nothing
            s = sums[0]
            self.assertEqual(s["coverage_totals"], {"full": 2, "none": 3, "partial": 1})  # FR-1 counts as none
            self.assertEqual(sorted(e["range"] for e in s["range_errors"]),
                             ["ABC-10...ABC-12", "ABC-20-22", "ABC-30 through ABC-31", "ABC-50..52 through XYZ-1"])
            write_csv(t / "c.csv", [head, row("FR-1", "ABC-1", "full"), row("FR-9", "ABC-9", "none")])
            r = run("merge_trace.py", t / "out2", "--trace", t / "c.csv", "--baseline", t / "out" / "coverage-summary.json")
            self.assertEqual(r.returncode, 0, r.stderr)
            d = json.loads((t / "out2" / "coverage-summary.json").read_text(encoding="utf-8"))["drift"]
            self.assertEqual(d["changed"], [{"req_id": "FR-1", "from": "none", "to": "full"}])
            self.assertEqual((d["added"], d["removed"]), (["FR-9"], ["FR-2", "FR-3", "FR-4", "FR-5", "FR-6"]))
            write_csv(t / "d.csv", [head, row("FR-1", "ABC-1", "covered")])
            r = run("merge_trace.py", t / "out3", "--trace", t / "d.csv")
            self.assertEqual(r.returncode, 1)
            self.assertIn("covered", r.stderr)
            write_csv(t / "e.csv", [head, row("FR-1", "ABC-1", "full")[:-1] + ["two\nlines"], row("", "ABC-2", "none")])
            r = run("merge_trace.py", t / "out4", "--trace", t / "e.csv")
            self.assertEqual(r.returncode, 1)
            self.assertIn("e.csv:4: empty req_id", r.stderr)  # physical line 4: the record above spans two

    def test_missing_column_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_csv(Path(tmp) / "a.csv", [["req_id", "coverage"], ["FR-1", "full"]])
            r = run("merge_trace.py", Path(tmp) / "out", "--trace", Path(tmp) / "a.csv")
            self.assertEqual(r.returncode, 1)
            self.assertIn("missing column", r.stderr)


class Stub(BaseHTTPRequestHandler):
    ISSUES = [{"key": f"XY-{n}", "fields": {"summary": f"Story {n}", "status": {"name": "Open" if n < 3 else "Done"},
               "issuetype": {"name": "Story"}, "labels": ["ui"], "assignee": {"displayName": "Bo"},
               "parent": {"key": "XY-100"}, "description": "desc", "customfield_1": f"AC {n}",
               "issuelinks": [{"type": {"outward": "blocks"}, "outwardIssue": {"key": "XY-9"}}]}} for n in (3, 1, 2)]
    seen = []
    redirect_to = None

    def do_GET(self):
        Stub.seen.append((self.path, self.headers.get("Authorization")))
        u = urlparse(self.path)
        if u.path.endswith("/moved"):
            self.send_response(302)
            self.send_header("Location", Stub.redirect_to)
            self.end_headers()
            return
        if u.path.endswith("/bad"):
            body, ctype = b"<html>login</html>", "text/html"
        elif u.path.endswith("/emptypage"):
            body, ctype = b'{"startAt": 0, "total": 3, "issues": []}', "application/json"
        elif u.path.endswith("/noissues"):
            body, ctype = b'{"errorMessages": ["gateway"]}', "application/json"
        else:
            q = parse_qs(u.query)
            start, size = int(q["startAt"][0]), int(q["maxResults"][0])
            body = json.dumps({"startAt": start, "total": 3, "issues": self.ISSUES[start:start + size]}).encode()
            ctype = "Application/JSON;charset=UTF-8" if u.path.endswith("/upper") else "application/json;charset=UTF-8"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


class TrackerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Stub)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def tracker(self, out, *extra, token="s3cret"):
        env = dict(os.environ, TRK_TOKEN=token)
        return run("stage_tracker.py", out, "--base-url", self.base, "--jql", "project = XY", "--token-env",
                   "TRK_TOKEN", "--ac-field", "customfield_1", "--page-size", 2, "--allow-http", *extra, env=env)

    def test_two_pages(self):
        Stub.seen.clear()
        with tempfile.TemporaryDirectory() as tmp:
            r = self.tracker(Path(tmp))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(len(Stub.seen), 2)
            self.assertTrue(all(a == "Bearer s3cret" for _, a in Stub.seen))
            self.assertIn("customfield_1", Stub.seen[0][0])
            self.assertNotIn("s3cret", r.stdout + r.stderr)
            keys = [i["key"] for i in json.loads((Path(tmp) / "issues.json").read_text(encoding="utf-8"))]
            self.assertEqual(keys, ["XY-1", "XY-2", "XY-3"])
            idx = (Path(tmp) / "index.md").read_text(encoding="utf-8")
            self.assertIn("- by status: Done 1, Open 2", idx)
            self.assertIn("| XY-1 | Story | Open | XY-100 | ui |  | Bo | Story 1 |", idx)
            body = (Path(tmp) / "bodies-001.md").read_text(encoding="utf-8")
            self.assertIn("AC 2", body)
            self.assertIn("- blocks XY-9", body)

    def test_parts_split(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = self.tracker(Path(tmp), "--part-kb", 0)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(len(list(Path(tmp).glob("bodies-*.md"))), 3)

    def test_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = self.tracker(Path(tmp), "--api-path", "/bad")
            self.assertEqual(r.returncode, 1)
            self.assertIn("non-JSON", r.stderr)
            r = self.tracker(Path(tmp), "--api-path", "/noissues")
            self.assertEqual(r.returncode, 1)  # a JSON error body is not an empty search
            self.assertIn("no 'issues' list", r.stderr)
            r = self.tracker(Path(tmp), "--api-path", "/emptypage")
            self.assertEqual(r.returncode, 1)  # an empty page short of total is an incomplete export
            self.assertIn("short of total", r.stderr)
            self.assertEqual(self.tracker(Path(tmp), token="").returncode, 2)
            env = dict(os.environ, TRK_TOKEN="t")
            r = run("stage_tracker.py", tmp, "--base-url", self.base, "--jql", "x", "--token-env", "TRK_TOKEN",
                    "--ac-field", "none", env=env)  # no --allow-http
            self.assertEqual(r.returncode, 2)
            self.assertIn("https", r.stderr)
        with tempfile.TemporaryDirectory() as tmp:
            r = self.tracker(Path(tmp), "--api-path", "/upper")
            self.assertEqual(r.returncode, 0, r.stderr)  # media types are case-insensitive

    def test_refuses_cross_origin_redirect_and_non_empty_out(self):
        other = HTTPServer(("127.0.0.1", 0), Stub)
        threading.Thread(target=other.serve_forever, daemon=True).start()
        try:
            Stub.redirect_to = f"http://127.0.0.1:{other.server_port}/rest/api/2/search?startAt=0&maxResults=2"
            Stub.seen.clear()
            with tempfile.TemporaryDirectory() as tmp:
                r = self.tracker(Path(tmp), "--api-path", "/moved")
                self.assertEqual(r.returncode, 1)
                self.assertIn("another origin refused", r.stderr)
                self.assertEqual(len(Stub.seen), 1)  # the other server was never called with the token
                (Path(tmp) / "bodies-009.md").write_text("old", encoding="utf-8")
                r = self.tracker(Path(tmp))
                self.assertEqual(r.returncode, 2)
                self.assertIn("not empty", r.stderr)
        finally:
            other.shutdown()
            other.server_close()

    def test_warns_when_ac_field_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run("stage_tracker.py", tmp, "--base-url", self.base, "--jql", "x", "--token-env", "TRK_TOKEN",
                    "--ac-field", "customfield_404", "--allow-http", env=dict(os.environ, TRK_TOKEN="t"))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("no issue returned field customfield_404", r.stdout)


if __name__ == "__main__":
    unittest.main()
