"""Behaviour tests for scripts/refresh/ (light refresh, workflow R1) with seeded controls: each detector here is shown
to fire on a planted change, and the deck and whiteboard checks to stay silent on their no-change twins. Tiny synthetic decks, whiteboard dumps and
tracker pulls in a temp dir. Stdlib only."""
import csv, json, shutil, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path

REFRESH = Path(__file__).resolve().parent.parent / "skills" / "ba-orchestrator" / "scripts" / "refresh"
P = ('xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
     'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
     'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
REL = 'xmlns="http://schemas.openxmlformats.org/package/2006/relationships"'
SLIDES = ["Scope: users export orders as CSV", "Weekly report to managers every Monday", "Audit trail kept for a year"]


def make_pptx(path, texts, hidden=(), notes=None, sldnum=False, date=None):
    """Slides in presentation order; the parts are numbered in reverse, so order never comes from part names.
    hidden: 1-based slide numbers to hide; notes: {slide number: speaker notes}; sldnum: a slide-number field whose
    cached text is the position (as PowerPoint saves it); date: a date field with that cached text."""
    notes = notes or {}
    with zipfile.ZipFile(path, "w") as z:
        n = len(texts)
        z.writestr("ppt/presentation.xml", f'<p:presentation {P}><p:sldIdLst>' + "".join(
            f'<p:sldId id="{256 + i}" r:id="rId{i}"/>' for i in range(1, n + 1)) + "</p:sldIdLst></p:presentation>")
        z.writestr("ppt/_rels/presentation.xml.rels", f"<Relationships {REL}>" + "".join(
            f'<Relationship Id="rId{i}" Type="http://x/slide" Target="slides/slide{n + 1 - i}.xml"/>'
            for i in range(1, n + 1)) + "</Relationships>")
        for i, t in enumerate(texts, 1):
            show = ' show="0"' if i in hidden else ""
            foot = (f'<a:p><a:fld id="{{B{i}}}" type="slidenum"><a:t>{i}</a:t></a:fld></a:p>' if sldnum else "") + \
                   (f'<a:p><a:r><a:t>Updated </a:t></a:r><a:fld id="{{C{i}}}" type="datetime1"><a:t>{date}</a:t></a:fld></a:p>' if date else "")
            z.writestr(f"ppt/slides/slide{n + 1 - i}.xml", f'<p:sld {P}{show}><p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>'
                       f"{t}</a:t></a:r></a:p>{foot}</p:txBody></p:sp></p:spTree></p:cSld></p:sld>")
            if i in notes:
                z.writestr(f"ppt/slides/_rels/slide{n + 1 - i}.xml.rels", f"<Relationships {REL}><Relationship Id=\"rId1\" "
                           f'Type="http://x/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/></Relationships>')
                z.writestr(f"ppt/notesSlides/notesSlide{i}.xml", f'<p:notes {P}><p:cSld><p:spTree><p:sp><p:nvSpPr>'
                           '<p:cNvPr id="1" name="n"/><p:cNvSpPr/><p:nvPr><p:ph type="body"/></p:nvPr></p:nvSpPr>'
                           f"<p:txBody><a:p><a:r><a:t>{notes[i]}</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld></p:notes>")


IDS = [f"{t}-{n}" for t in ("BR", "FR", "NFR") for n in range(1, 10)]


def run(script, *args, ids=True):
    if script == "apply_mappings.py" and ids and not (Path(args[0]) / "requirement-ids.json").exists():
        (Path(args[0]) / "requirement-ids.json").write_text(json.dumps(IDS), encoding="utf-8")
    return subprocess.run([sys.executable, "-I", str(REFRESH / script), *map(str, args)], capture_output=True, text=True)


def pulled(items, total=None):
    """A pull as tracker_merge.py takes it: the query's items with the tracker's own count of matches."""
    return json.dumps({"query": "project = PROJ ORDER BY updated ASC", "total": len(items) if total is None else total,
                       "items": items})


def item(key, status="To Do", description="", ac="", updated="2026-10-10T10:00:00.000+0000", **kw):
    summary = kw.pop("summary", {"PROJ-1": "Export", "PROJ-2": "Old", "PROJ-3": "Audit"}.get(key, f"Item {key}"))
    return dict(key=key, summary=summary, status=status, labels=[], issuetype="Story", parent_key="",
                assignee="", created="2026-10-01T10:00:00.000+0000", updated=updated, description=description, ac=ac, **kw)


class RefreshTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.d = Path(self.tmp.name)
        self.st = d / "state"
        make_pptx(d / "deck.pptx", SLIDES)
        self.widgets = [{"id": "w1", "type": "sticky", "text": "Export orders", "x": 10, "y": 20},
                        {"id": "w2", "type": "sticky", "text": "Audit log", "x": 200, "y": 20}]
        (d / "board.json").write_text(json.dumps(self.widgets), encoding="utf-8")
        export = [{"key": "PROJ-1", "fields": {"summary": "Export", "status": {"name": "To Do"}, "issuetype": {"name": "Story"},
                                               "labels": [], "created": "2026-10-01", "updated": "2026-10-01T10:00:00.000+0000",
                                               "description": "h1. Export\nUsers export orders as *CSV* within 30 days.",
                                               "customfield_100": "Given an order list, when I export, then a CSV downloads."}},
                  {"key": "PROJ-2", "fields": {"summary": "Old", "status": {"name": "Cancelled"}, "issuetype": {"name": "Story"},
                                               "updated": "2026-10-01T10:00:00.000+0000", "description": "x", "customfield_100": ""}},
                  {"key": "PROJ-3", "fields": {"summary": "Audit", "status": {"name": "In Progress"}, "issuetype": {"name": "Story"},
                                               "updated": "2026-10-02T10:00:00.000+0000", "description": "Keep an audit trail.",
                                               "customfield_100": None}}]
        (d / "issues.json").write_text(json.dumps(export), encoding="utf-8")
        r = run("init_state.py", self.st, "--tracker-export", d / "issues.json", "--ac-field", "customfield_100",
                "--deck", f"deck={d / 'deck.pptx'}", "--whiteboard", f"board={d / 'board.json'}")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def tearDown(self):
        self.tmp.cleanup()

    def flags(self):
        return json.loads((self.st / "flags.json").read_text(encoding="utf-8"))

    def deck_check(self, texts, name="deck2.pptx", **kw):
        make_pptx(self.d / name, texts, **kw)
        r = run("source_check.py", self.st, "deck", self.d / name)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return self.flags()["decks"]["deck"]

    def test_init_refuses_twice(self):
        r = run("init_state.py", self.st, "--tracker-export", self.d / "issues.json", "--ac-field", "none")
        self.assertEqual(r.returncode, 1)
        self.assertIn("already initialised", r.stderr)

    def test_deck_no_change(self):
        f = self.deck_check(SLIDES)
        self.assertEqual((f["changed_slides"], f["new_slides"], f["moved_slides"]), ([], [], []))

    def test_deck_one_word_swap_flags_exactly_that_slide(self):
        f = self.deck_check([SLIDES[0], SLIDES[1].replace("Monday", "Friday"), SLIDES[2]])
        self.assertEqual(f["changed_slides"], [2])
        self.assertEqual(f["new_slides"], [2])
        self.assertEqual(f["moved_slides"], [])
        self.assertIn("Monday", f["old_text"]["2"])

    def test_deck_reorder_is_moved_not_changed(self):
        f = self.deck_check([SLIDES[2], SLIDES[0], SLIDES[1]])
        self.assertEqual((f["changed_slides"], f["new_slides"]), ([], []))
        self.assertEqual(f["moved_slides"], [{"from": 3, "to": 1}, {"from": 1, "to": 2}, {"from": 2, "to": 3}])

    def test_deck_accept_moves_the_baseline(self):
        self.deck_check([SLIDES[0], "New slide", SLIDES[2]])
        r = self.accept("deck", self.d / "deck2.pptx")
        self.assertEqual(r.returncode, 0, r.stderr)
        kept = self.flags()["decks"]["deck"]
        self.assertTrue(kept["accepted"])
        self.assertEqual([kept[k] for k in ("changed_slides", "new_slides", "moved_slides")], [[], [], []])
        f = self.deck_check([SLIDES[0], "New slide", SLIDES[2]])
        self.assertEqual(f["changed_slides"], [])

    def test_accept_only_the_checked_file(self):
        self.deck_check([SLIDES[0], "Edited two", SLIDES[2]])
        make_pptx(self.d / "deck3.pptx", [SLIDES[0], "Edited two", "Edited three, never checked"])
        r = self.accept("deck", self.d / "deck3.pptx")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("is not the reviewed check", r.stderr)
        self.assertIn("deck", self.flags()["decks"])
        for kind, f in (("whiteboard", self.d / "board.json"), ("deck", self.d / "deck.pptx")):
            with self.subTest(kind):
                if kind == "deck":
                    self.accept("deck", self.d / "deck2.pptx")
                r = self.accept(kind, f)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("is not the reviewed check", r.stderr)

    def test_cited_slide_numbers_survive_an_accepted_insert(self):
        f = self.deck_check([SLIDES[0], "Inserted slide", SLIDES[1], SLIDES[2]])
        self.assertEqual(f["moved_slides"], [{"from": 2, "to": 3}, {"from": 3, "to": 4}])
        self.assertEqual(self.accept("deck", self.d / "deck2.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], "Inserted slide", SLIDES[1].replace("Monday", "Friday"), SLIDES[2]], "deck3.pptx")
        self.assertEqual(f["changed_slides"], [2])
        self.assertIn("Monday", f["old_text"]["2"])
        self.assertEqual(f["moved_slides"], [])
        self.assertEqual(self.accept("deck", self.d / "deck3.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], "Inserted slide, edited", SLIDES[1].replace("Monday", "Friday"),
                             SLIDES[2].replace("year", "decade")], "deck4.pptx")
        self.assertEqual(f["changed_slides"], [3])
        self.assertEqual(f["new_slides"], [2, 4])

    def test_deck_hidden_flag_and_notes_are_compared(self):
        f = self.deck_check(SLIDES, hidden=(2,))
        self.assertEqual(f["changed_slides"], [2])
        self.assertIn("[hidden]", f["new_text"]["2"])
        f = self.deck_check(SLIDES, notes={3: "Say: retention is legal's call"})
        self.assertEqual(f["changed_slides"], [3])

    def test_whiteboard_changed_and_added(self):
        r = run("source_check.py", self.st, "whiteboard", self.d / "board.json")
        self.assertEqual(r.returncode, 0, r.stderr)
        f = self.flags()["whiteboards"]["board"]
        self.assertEqual((f["changed"], f["added"], f["deleted"]), ([], [], []))
        w = [dict(self.widgets[0], text="Export orders and invoices"), self.widgets[1],
             {"id": "w3", "type": "sticky", "text": "Archive after a year", "x": 400, "y": 20, "parentId": "w2"}]
        (self.d / "board2.json").write_text(json.dumps({"value": w}), encoding="utf-8")
        r = run("source_check.py", self.st, "whiteboard", self.d / "board2.json", "--id", "board")
        self.assertEqual(r.returncode, 0, r.stderr)
        f = self.flags()["whiteboards"]["board"]
        self.assertEqual((f["changed"], f["added"], f["deleted"]), (["w1"], ["w3"], []))
        self.assertEqual(f["added_text"], {"w3": "Archive after a year"})
        self.assertEqual(f["parents"], {"w3": ["w2"]})
        (self.d / "board4.json").write_text(json.dumps([dict(self.widgets[0], x=999), self.widgets[1]]), encoding="utf-8")
        run("source_check.py", self.st, "whiteboard", self.d / "board4.json")
        self.assertEqual(self.flags()["whiteboards"]["board"]["changed"], ["w1"])
        (self.d / "board3.json").write_text(json.dumps([self.widgets[0], {"type": "sticky", "text": "no id"}]), encoding="utf-8")
        r = run("source_check.py", self.st, "whiteboard", self.d / "board3.json")
        self.assertEqual(r.returncode, 1)
        r = run("source_check.py", self.st, "whiteboard", self.d / "board.json", "--id", "Other")
        self.assertEqual(r.returncode, 1)
        self.assertIn("no whiteboard with id", r.stderr)

    def merge(self, pull, *args):
        (self.d / "pull.json").write_text(pulled(pull), encoding="utf-8")
        return run("tracker_merge.py", self.st, self.d / "pull.json", *args)

    def test_compact_pull_refused(self):
        before = (self.st / "tracker/now.json").read_bytes()
        pull = [item("PROJ-1")]
        del pull[0]["description"]
        r = self.merge(pull)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("lack one of", r.stderr)
        self.assertEqual((self.st / "tracker/now.json").read_bytes(), before)
        r = self.merge([item("PROJ-1", updated="")])
        self.assertEqual(r.returncode, 1)

    def test_cancellation_of_a_live_item_flagged(self):
        r = self.merge([item("PROJ-3", status="Cancelled", description="Keep an audit trail."),
                        item("PROJ-2", status="Cancelled", description="x")])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.flags()["cancelled_keys"], ["PROJ-3"])

    def test_first_sighting_similarity_and_later_change(self):
        same = item("PROJ-1", description="<h1>Export</h1><p>Users export orders as <b>CSV</b> within 30 days.</p>",
                    ac="Given an order list, when I export, then a CSV downloads.")
        r = self.merge([same])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.flags()["text_changed_keys"], [])
        r = self.merge([dict(same, ac="Given a list, the export is a signed PDF archive emailed to finance.")])
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])
        self.tmp.cleanup()
        self.setUp()
        r = self.merge([item("PROJ-1", description="Totally different scope: billing export to an ERP.", ac="")],
                       "--allow-empty-ac", "PROJ-1")
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])

    def test_first_sighting_flags_any_number_or_negation_change(self):
        ac = "Given an order list, when I export, then a CSV downloads."
        for name, desc, a in (("number", "<p>Users export orders as CSV within 90 days.</p>", ac),
                              ("negation", "<p>Users do not export orders as <b>CSV</b> within 30 days.</p>", ac),
                              ("negation in the criteria", "Users export orders as CSV within 30 days.",
                               ac.replace("then a", "then no"))):
            with self.subTest(name):
                self.tmp.cleanup()
                self.setUp()
                self.merge([item("PROJ-1", description=desc, ac=a)])
                self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])

    def review(self, **tracker):
        """What build_baseline.py writes: the reviewed state, here the current checks and the given tracker keys."""
        fl = self.flags()
        rv = {sec: {i: {"md5": f["md5"]} for i, f in (fl.get(sec) or {}).items()} for sec in ("decks", "whiteboards")}
        now = json.loads((self.st / "tracker/now.json").read_text(encoding="utf-8"))
        tracker = tracker or {k: fl.get(k, []) for k in ("cancelled_keys", "reopened_keys", "text_changed_keys")}
        tracker = {k: {x: {"status": now[x]["status"], "text_hash": now[x]["text_hash"]} for x in v} for k, v in tracker.items()}
        (self.st / "review.json").write_text(json.dumps({"requirements": [], "reviewed": dict(rv, tracker=tracker)}),
                                             encoding="utf-8")

    def accept(self, kind, f=None):
        self.review()
        return run("accept.py", self.st, kind, *([f] if f else []))

    def test_accept_tracker_clears_only_what_was_reviewed(self):
        self.merge([item("PROJ-3", status="Cancelled", description="Keep an audit trail.")])
        r = run("accept.py", self.st, "tracker")
        self.assertEqual(r.returncode, 1)
        self.assertIn("review it first", r.stderr)
        self.review(cancelled_keys=["PROJ-3"], text_changed_keys=[])
        self.merge([item("PROJ-1", status="Cancelled", description="x")], "--allow-empty-ac", "PROJ-1")
        self.assertEqual(self.flags()["cancelled_keys"], ["PROJ-1", "PROJ-3"])
        r = run("accept.py", self.st, "tracker")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.flags()["cancelled_keys"], ["PROJ-1"])
        st = json.loads((self.st / "state.json").read_text(encoding="utf-8"))
        self.assertEqual(st["accepted"][-1]["cancelled_keys"], ["PROJ-3"])

    def test_tomap_is_cumulative_and_apply_mappings_guards(self):
        r = self.merge([item("PROJ-5", description="Users export orders as PDF."), item("PROJ-6", description="Fix CI")])
        self.assertIn("to map 2", r.stdout)
        r = self.merge([item("PROJ-1", description="Users export orders as CSV.")], "--allow-empty-ac", "PROJ-1")
        tomap = {d["key"]: d for d in json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))}
        self.assertEqual(sorted(tomap), ["PROJ-5", "PROJ-6"])
        mapped = self.d / "mapped.csv"

        def write(rows):
            with open(mapped, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["key", "text_hash", "req_ids", "effect", "quote", "note"])
                w.writerows(rows)
        h5, h6 = tomap["PROJ-5"]["text_hash"], tomap["PROJ-6"]["text_hash"]
        write([["PROJ-5", h5, "FR-2", "upgrades none->partial", "", ""]])
        r = run("apply_mappings.py", self.st, mapped)
        self.assertEqual(r.returncode, 1)
        self.assertIn("needs the quote", r.stdout)
        self.assertFalse((self.st / "mappings.csv").exists())
        write([["PROJ-5", "0" * 32, "FR-2", "upgrades none->partial", "Users export orders as PDF.", ""]])
        r = run("apply_mappings.py", self.st, mapped)
        self.assertEqual(r.returncode, 1)
        self.assertIn("text_hash differs", r.stdout)
        write([["PROJ-5", h5, "FR-2", "upgrades none->partial", "Users export orders as PDF.", ""]])
        r = run("apply_mappings.py", self.st, mapped)
        self.assertEqual(r.returncode, 1)
        self.assertIn("NOT mapped from tomap: ['PROJ-6']", r.stdout)
        before = (self.st / "mappings.csv").read_bytes()
        good5 = ["PROJ-5", h5, "FR-2", "upgrades none->partial", "Users export orders as PDF.", ""]
        for name, row, msg in (
                ("key not in tomap", ["PROJ-8", h5, "FR-2", "upgrades none->partial", "x", ""], "not in tomap.json"),
                ("quote not in the text", dict(enumerate(good5)) | {4: "Users export invoices as PDF."}, "quote is not in"),
                ("unknown effect", dict(enumerate(good5)) | {3: "relates to"}, "is not one of"),
                ("no requirement with ids", dict(enumerate(good5)) | {3: "no requirement"}, "'no requirement' with"),
                ("upgrade without ids", dict(enumerate(good5)) | {2: ""}, "needs requirement id(s)"),
                ("bad requirement id", dict(enumerate(good5)) | {2: "FR-2, fr_9"}, "do not match"),
                ("bad key", ["proj-5", h5, "FR-2", "upgrades none->partial", "x", ""], "does not match")):
            with self.subTest(name):
                write([[row[i] for i in range(6)] if isinstance(row, dict) else row])
                r = run("apply_mappings.py", self.st, mapped)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn(msg, r.stdout)
                self.assertEqual((self.st / "mappings.csv").read_bytes(), before)
        write([["PROJ-6", h6, "", "no requirement (engineering/env/bug)", "", ""],
               ["PROJ-5", h5, "FR-2, BR-2 / FR-3", "upgrades none->partial", "users export ORDERS as pdf", ""]])
        r = run("apply_mappings.py", self.st, mapped)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("NOT mapped from tomap: none", r.stdout)
        rows = {x["key"]: x for x in csv.DictReader((self.st / "mappings.csv").read_text(encoding="utf-8").splitlines())}
        self.assertEqual(rows["PROJ-5"]["req_ids"], "FR-2;BR-2;FR-3")
        r = self.merge([item("PROJ-1", description="Users export orders as CSV.")], "--allow-empty-ac", "PROJ-1")
        self.assertIn("to map 0", r.stdout)
        r = self.merge([item("PROJ-5", description="Users export orders as PDF and XLSX.")])
        self.assertIn("to map 1", r.stdout)
        st = json.loads((self.st / "state.json").read_text(encoding="utf-8"))
        self.assertEqual(st["tracker_last_updated"], "2026-10-10T10:00:00.000+0000")

    def test_custom_key_pattern_sorts_without_losing_rows(self):
        self.merge([item("ACME#5", description="Export orders."), item("PROJ-5", description="Export orders as PDF.")])
        tomap = {d["key"]: d for d in json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))}
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["key", "text_hash", "req_ids", "effect", "quote", "note"])
            w.writerow(["PROJ-5", tomap["PROJ-5"]["text_hash"], "", "no requirement", "", ""])
        self.assertEqual(run("apply_mappings.py", self.st, self.d / "m.csv").returncode, 1)
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["key", "text_hash", "req_ids", "effect", "quote", "note"])
            w.writerow(["ACME#5", tomap["ACME#5"]["text_hash"], "", "no requirement", "", ""])
        r = run("apply_mappings.py", self.st, self.d / "m.csv", "--key-pattern", r"[A-Z]+[#-]\d+")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        keys = [x["key"] for x in csv.DictReader((self.st / "mappings.csv").read_text(encoding="utf-8").splitlines())]
        self.assertEqual(sorted(keys), ["ACME#5", "PROJ-5"])


    def test_init_needs_explicit_source_ids(self):
        for spec in (str(self.d / "deck.pptx"), f"Slide deck={self.d / 'deck.pptx'}", "deck="):
            with self.subTest(spec):
                r = run("init_state.py", self.d / "s2", "--tracker-export", self.d / "issues.json", "--ac-field", "none",
                        "--deck", spec)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("ID=PATH", r.stderr)
        r = run("init_state.py", self.d / "s3", "--tracker-export", self.d / "issues.json", "--ac-field", "none",
                "--deck", f"x={self.d / 'deck.pptx'}", "--whiteboard", f"x={self.d / 'board.json'}")
        self.assertEqual(r.returncode, 1)
        self.assertIn("unique", r.stderr)

    def test_slide_identity_by_content_across_insert_and_edit(self):
        B = SLIDES[1]
        f = self.deck_check([SLIDES[0], "Inserted slide", B.replace("Monday", "Friday"), SLIDES[2]])
        self.assertEqual(f["changed_slides"], [2])
        self.assertEqual(f["inserted_slides"], [2])
        self.assertEqual(f["edited"], [{"cited": 2, "now": 3}])
        self.assertEqual(self.accept("deck", self.d / "deck2.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], "Inserted slide", B.replace("Monday", "Sunday"), SLIDES[2]], "deck3.pptx")
        self.assertEqual(f["changed_slides"], [2])
        self.tmp.cleanup()
        self.setUp()
        f = self.deck_check([SLIDES[0], SLIDES[2].replace("year", "decade")])
        self.assertEqual(f["changed_slides"], [2, 3])
        self.assertEqual(self.accept("deck", self.d / "deck2.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], SLIDES[2].replace("year", "century")], "deck3.pptx")
        self.assertEqual(f["changed_slides"], [3])

    def test_moves_after_an_accepted_insert_report_cited_numbers(self):
        self.deck_check([SLIDES[0], "Inserted slide", SLIDES[1], SLIDES[2]])
        self.assertEqual(self.accept("deck", self.d / "deck2.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], "Inserted slide", SLIDES[2], SLIDES[1]], "deck3.pptx")
        self.assertIn({"from": 2, "to": 4}, f["moved_slides"])
        self.assertEqual(f["changed_slides"], [])

    def test_accept_binds_to_the_reviewed_check(self):
        self.deck_check([SLIDES[0], "Edited two", SLIDES[2]])
        self.review()
        self.deck_check([SLIDES[0], "Edited two", "Edited three"], "deck3.pptx")
        for f in ("deck3.pptx", "deck2.pptx"):
            with self.subTest(f):
                r = run("accept.py", self.st, "deck", self.d / f)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("is not the reviewed check", r.stderr)

    def test_whiteboard_signature_fields(self):
        base = dict(self.widgets[0], label="L", width=10, height=10, style={"backgroundColor": "#fff"})
        (self.d / "b0.json").write_text(json.dumps([base, self.widgets[1]]), encoding="utf-8")
        run("source_check.py", self.st, "whiteboard", self.d / "b0.json")
        self.assertEqual(self.accept("whiteboard", self.d / "b0.json").returncode, 0)
        for name, change in (("label", {"label": "M"}), ("width", {"width": 20}), ("height", {"height": 20}),
                             ("colour", {"style": {"backgroundColor": "#f00"}}), ("parent", {"parentId": "w2"}),
                             ("connector end", {"startRefId": "w2"}), ("type", {"type": "shape"}), ("y", {"y": 99})):
            with self.subTest(name):
                (self.d / "b1.json").write_text(json.dumps([dict(base, **change), self.widgets[1]]), encoding="utf-8")
                run("source_check.py", self.st, "whiteboard", self.d / "b1.json")
                self.assertEqual(self.flags()["whiteboards"]["board"]["changed"], ["w1"])

    def test_similarity_floor_alone_and_contractions(self):
        ac = "Given an order list, when I export, then a CSV downloads."
        for name, desc, a in (
                ("rewrite, same numbers", "Billing team reconciles invoices against the ledger within 30 days.", ""),
                ("isn't", "Users export orders as CSV within 30 days.", ac.replace("then a CSV downloads", "then a CSV isn't downloaded")),
                ("never", "Users never export orders as CSV within 30 days.", ac),
                ("neither", "Neither user exports orders as CSV within 30 days.", ac)):
            with self.subTest(name):
                self.tmp.cleanup()
                self.setUp()
                self.merge([item("PROJ-1", description=desc, ac=a)], "--allow-empty-ac", "PROJ-1")
                self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])

    def test_non_latin_text_is_compared(self):
        ru = "Пользователи экспортируют заказы в течение 30 дней."
        export = [{"key": "PROJ-1", "fields": {"summary": "x", "status": {"name": "To Do"}, "issuetype": {"name": "Story"},
                                               "updated": "2026-10-01", "description": ru, "customfield_100": ""}}]
        (self.d / "ru.json").write_text(json.dumps(export), encoding="utf-8")
        st = self.d / "ru"
        self.assertEqual(run("init_state.py", st, "--tracker-export", self.d / "ru.json", "--ac-field", "customfield_100").returncode, 0)
        (self.d / "p.json").write_text(pulled([item("PROJ-1", description=ru.replace("экспортируют", "запрещено экспортировать"))]), encoding="utf-8")
        run("tracker_merge.py", st, self.d / "p.json")
        self.assertEqual(json.loads((st / "flags.json").read_text(encoding="utf-8"))["text_changed_keys"], ["PROJ-1"])
        self.merge([item("PROJ-5", description=ru)])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-5", h, "FR-2", "upgrades none->partial", "Пользователи изобрели эту цитату целиком", ""]])
        r = run("apply_mappings.py", self.st, self.d / "m.csv")
        self.assertEqual(r.returncode, 1)
        self.assertIn("not in the item's text", r.stdout)
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-5", h, "FR-2", "upgrades none->partial", "экспортируют заказы в течение 30 дней", ""]])
        self.assertEqual(run("apply_mappings.py", self.st, self.d / "m.csv").returncode, 0)
        r = self.merge([item("PROJ-5", description=ru.replace("экспортируют", "удаляют"))])
        self.assertIn("to map 1", r.stdout)

    def test_cancelled_statuses_come_from_the_state(self):
        st = self.d / "s4"
        r = run("init_state.py", st, "--tracker-export", self.d / "issues.json", "--ac-field", "none",
                "--cancelled-status", "Cancelled,Won't Do")
        self.assertEqual(r.returncode, 0, r.stderr)
        (self.d / "p.json").write_text(pulled([item("PROJ-3", status="Won't Do", description="Keep an audit trail.")]),
                                       encoding="utf-8")
        run("tracker_merge.py", st, self.d / "p.json")
        self.assertEqual(json.loads((st / "flags.json").read_text(encoding="utf-8"))["cancelled_keys"], ["PROJ-3"])
        self.assertIn("Won't Do", json.loads((st / "state.json").read_text(encoding="utf-8"))["cancelled_statuses"])

    def test_mapping_quotes_duplicates_and_named_ids(self):
        self.merge([item("PROJ-5", description="Users export orders as PDF every night.")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        cases = (("one letter", [["PROJ-5", h, "FR-2", "upgrades none->partial", "e", ""]], "too short"),
                 ("word fragment", [["PROJ-5", h, "FR-2", "upgrades none->partial", "port orders as PDF every", ""]], "as whole words"),
                 ("letters across a word break", [["PROJ-5", h, "FR-2", "upgrades none->partial", "users export order SAS PDF", ""]],
                  "as whole words"),
                 ("duplicate key", [["PROJ-5", h, "BR-2", "upgrades none->partial", "Users export orders as PDF", ""],
                                    ["PROJ-5", h, "BR-3", "upgrades none->partial", "Users export orders as PDF", ""]], "given twice"),
                 ("conflict id not in req_ids", [["PROJ-5", h, "FR-3", "conflicts with BR-3", "Users export orders as PDF", ""]],
                  "must name its requirement id"),
                 ("conflict naming no id", [["PROJ-5", h, "FR-3", "conflicts with", "Users export orders as PDF", ""]],
                  "must name its requirement id"))
        for name, rows, msg in cases:
            with self.subTest(name):
                with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
                    csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"]] + rows)
                r = run("apply_mappings.py", self.st, self.d / "m.csv")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn(msg, r.stdout)
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-5", h, "FR-3; BR-3", "conflicts with BR-3", "export orders as pdf every night", ""]])
        self.assertEqual(run("apply_mappings.py", self.st, self.d / "m.csv").returncode, 0)

    def test_slide_rewritten_in_place_keeps_its_cited_number(self):
        rewrite = "Managers now receive a PDF digest by email with regional charts"
        f = self.deck_check([SLIDES[0], rewrite, SLIDES[2]])
        self.assertEqual(f["changed_slides"], [2])
        self.assertEqual(f["edited"], [{"cited": 2, "now": 2}])
        self.assertEqual(f["inserted_slides"], [])
        self.assertEqual(self.accept("deck", self.d / "deck2.pptx").returncode, 0)
        f = self.deck_check([SLIDES[0], rewrite.replace("PDF", "XLSX"), SLIDES[2]], "deck3.pptx")
        self.assertEqual(f["changed_slides"], [2])

    def test_unrelated_insert_does_not_inherit_a_deleted_slides_number(self):
        f = self.deck_check([SLIDES[0], SLIDES[2], "Pricing tiers for enterprise customers"])
        self.assertEqual(f["changed_slides"], [2])
        self.assertEqual(f["edited"], [])
        self.assertEqual(f["inserted_slides"], [3])
        self.assertIsNone(f["origin_next"]["3"])

    def test_auto_fields_are_not_content(self):
        for name, kw0, kw1, texts, want in (
                ("slide numbers, insert", {"sldnum": True}, {"sldnum": True}, [SLIDES[0], "Pricing tiers"] + SLIDES[1:],
                 ([], [{"from": 2, "to": 3}, {"from": 3, "to": 4}])),
                ("date re-saved", {"date": "10/1/2026"}, {"date": "10/12/2026"}, SLIDES, ([], []))):
            with self.subTest(name):
                self.tmp.cleanup()
                self.setUp()
                make_pptx(self.d / "deck0.pptx", SLIDES, **kw0)
                shutil.rmtree(self.st)
                r = run("init_state.py", self.st, "--tracker-export", self.d / "issues.json", "--ac-field", "none",
                        "--deck", f"deck={self.d / 'deck0.pptx'}")
                self.assertEqual(r.returncode, 0, r.stderr)
                f = self.deck_check(texts, **kw1)
                self.assertEqual((f["changed_slides"], f["moved_slides"]), want)

    def test_summary_is_item_text(self):
        r = self.merge([item("PROJ-3", description="Keep an audit trail.")])
        self.assertEqual(self.flags()["text_changed_keys"], [])
        self.merge([item("PROJ-3", summary="Drop the audit trail", description="Keep an audit trail.")])
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-3"])
        self.merge([item("PROJ-7", summary="Export orders to CSV nightly", description="")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        with open(self.d / "m.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-7", h, "FR-1", "adds to existing coverage", "Export orders to CSV nightly", ""]])
        r = run("apply_mappings.py", self.st, self.d / "m.csv")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_markup_numbers_are_not_content(self):
        for name, desc in (("markdown list", "Export\n\n1. Users export orders as CSV within 30 days."),
                           ("wiki image", "Export !image-20261001-101500.png! Users export orders as CSV within 30 days."),
                           ("markdown image", "Export ![shot](https://x.example.com/a-2026.png) Users export orders as CSV within 30 days.")):
            with self.subTest(name):
                self.tmp.cleanup()
                self.setUp()
                self.merge([item("PROJ-1", description=desc, ac="Given an order list, when I export, then a CSV downloads.")])
                self.assertEqual(self.flags()["text_changed_keys"], [])
        self.merge([item("PROJ-1", description="Export\n\n1. Users export orders as CSV within 90 days.",
                         ac="Given an order list, when I export, then a CSV downloads.")], "--allow-empty-ac", "PROJ-1")
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])

    def test_empty_ac_refused_when_the_item_had_criteria(self):
        before = (self.st / "tracker/now.json").read_bytes()
        r = self.merge([item("PROJ-1", description="Users export orders as CSV within 30 days.", ac="")])
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("empty ac", r.stderr)
        self.assertEqual((self.st / "tracker/now.json").read_bytes(), before)
        self.assertEqual(self.merge([item("PROJ-3", description="Keep an audit trail.")]).returncode, 0)
        self.assertEqual(self.merge([item("PROJ-9", description="New", ac="Given x, then y.")]).returncode, 0)
        r = self.merge([item("PROJ-9", description="New", ac="")])
        self.assertEqual(r.returncode, 1, r.stdout)
        r = self.merge([item("PROJ-9", description="New", ac="")], "--allow-empty-ac", "PROJ-9")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_position_pairing_only_when_unambiguous(self):
        rewrite = "Managers now receive a PDF digest by email with regional charts"
        f = self.deck_check([SLIDES[0], "Pricing tiers for enterprise customers", rewrite, SLIDES[2]])
        self.assertEqual(f["changed_slides"], [2])
        self.assertEqual(f["edited"], [])
        self.assertEqual(f["inserted_slides"], [2, 3])
        f = self.deck_check([SLIDES[0], "Audit records are deleted after ninety days by policy"], "deck3.pptx")
        self.assertEqual((f["changed_slides"], f["edited"]), ([2, 3], []))
        f = self.deck_check([SLIDES[0], rewrite, "Audit records are deleted after ninety days by policy"], "deck4.pptx")
        self.assertEqual(f["edited"], [{"cited": 2, "now": 2}, {"cited": 3, "now": 3}])

    def test_empty_text_fields_refused_when_the_item_had_text(self):
        before = (self.st / "tracker/now.json").read_bytes()
        ac = "Given an order list, when I export, then a CSV downloads."
        for field, kw in (("description", dict(description="", ac=ac)),
                          ("summary", dict(description="Users export orders as CSV within 30 days.", ac=ac, summary=""))):
            with self.subTest(field):
                r = self.merge([item("PROJ-1", **kw)])
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn(f"empty {field}", r.stderr)
                self.assertEqual((self.st / "tracker/now.json").read_bytes(), before)
        r = self.merge([item("PROJ-1", description="", ac=ac)], "--allow-empty-description", "PROJ-1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.merge([item("PROJ-3", description="Keep an audit trail.", summary="")]).returncode, 1)

    def test_empty_field_guard_holds_on_later_pulls_and_allow_is_per_field(self):
        full = dict(summary="SSO", description="Users sign in with SSO.", ac="Given a user, then SSO works.")
        r = self.merge([item("PROJ-60", **full)])
        self.assertEqual(r.returncode, 0, r.stderr)
        for field in ("summary", "description", "ac"):
            with self.subTest(field):
                r = self.merge([item("PROJ-60", **dict(full, **{field: ""}))])
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn(f"empty {field}", r.stderr)
        r = self.merge([item("PROJ-60", **dict(full, description="", ac=""))], "--allow-empty-ac", "PROJ-60")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("empty description", r.stderr)
        r = self.merge([item("PROJ-60", **dict(full, description="", ac=""))], "--allow-empty-ac", "PROJ-60",
                       "--allow-empty-description", "PROJ-60")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_each_pull_is_recorded(self):
        self.assertNotIn("last_pull", json.loads((self.st / "state.json").read_text(encoding="utf-8")))
        self.assertEqual(self.merge([item("PROJ-3", description="Keep an audit trail.")]).returncode, 0)
        lp = json.loads((self.st / "state.json").read_text(encoding="utf-8"))["last_pull"]
        self.assertEqual((lp["file"], lp["items"]), ("pull.json", 1))

    def test_item_moved_out_of_an_area_records_its_old_area(self):
        w = self.widgets + [{"id": "w3", "type": "sticky", "text": "Archive", "x": 400, "y": 20, "parentId": "w2"}]
        (self.d / "b1.json").write_text(json.dumps(w), encoding="utf-8")
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "b1.json").returncode, 0)
        r = self.accept("whiteboard", self.d / "b1.json")
        self.assertEqual(r.returncode, 0, r.stderr)
        (self.d / "b2.json").write_text(json.dumps(self.widgets + [dict(w[2], parentId=None)]), encoding="utf-8")
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "b2.json").returncode, 0)
        f = self.flags()["whiteboards"]["board"]
        self.assertEqual((f["changed"], f["old_parents"]), (["w3"], {"w3": ["w2"]}))
        (self.d / "b3.json").write_text(json.dumps(self.widgets), encoding="utf-8")
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "b3.json").returncode, 0)
        f = self.flags()["whiteboards"]["board"]
        self.assertEqual((f["deleted"], f["parents"]), (["w3"], {"w3": ["w2"]}))

    def test_a_coverage_category_change_is_flagged_in_either_direction(self):
        ac = "Given an order list, when I export, then a CSV downloads."
        r = self.merge([item("PROJ-2", description="x"),
                        item("PROJ-3", status="Cancelled", description="Keep an audit trail."),
                        item("PROJ-1", status="In Progress", description="h1. Export\nUsers export orders as *CSV* within 30 days.",
                             ac=ac)])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        f = self.flags()
        self.assertEqual((f["reopened_keys"], f["cancelled_keys"], f["text_changed_keys"]), (["PROJ-2"], ["PROJ-3"], []))
        self.assertIn("re-opened 1", r.stdout)
        r = self.merge([item("PROJ-3", description="Keep an audit trail.")])
        self.assertIn("PROJ-3", self.flags()["reopened_keys"])
        self.assertEqual(self.accept("tracker").returncode, 0)
        self.assertEqual(self.flags()["reopened_keys"], [])

    def test_nested_areas_record_every_ancestor(self):
        w = self.widgets + [{"id": "a1", "type": "area", "text": "Audit", "x": 0, "y": 0},
                            {"id": "a2", "type": "area", "text": "Logs", "x": 5, "y": 5, "parentId": "a1"},
                            {"id": "w6", "type": "sticky", "text": "Keep logs a year", "x": 1, "y": 1, "parentId": "a2"},
                            {"id": "c1", "type": "area", "text": "Loop", "x": 0, "y": 0, "parentId": "c2"},
                            {"id": "c2", "type": "area", "text": "Loop", "x": 0, "y": 0, "parentId": "c1"},
                            {"id": "w7", "type": "sticky", "text": "In a cycle", "x": 1, "y": 1, "parentId": "c1"}]
        (self.d / "n1.json").write_text(json.dumps(w), encoding="utf-8")
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "n1.json").returncode, 0)
        f = self.flags()["whiteboards"]["board"]
        self.assertEqual(f["parents"]["w6"], ["a2", "a1"])
        self.assertEqual(f["parents"]["w7"], ["c1", "c2"])
        self.assertEqual(self.accept("whiteboard", self.d / "n1.json").returncode, 0)
        (self.d / "n2.json").write_text(json.dumps([x for x in w if x["id"] != "w6"]), encoding="utf-8")
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "n2.json").returncode, 0)
        self.assertEqual(self.flags()["whiteboards"]["board"]["parents"]["w6"], ["a2", "a1"])

    def test_unknown_requirement_id_is_refused(self):
        r = self.merge([item("PROJ-5", description="Users export orders as PDF.")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        m = self.d / "u.csv"
        with open(m, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-5", h, "FR-2", "upgrades none->partial", "Users export orders as PDF", ""]])
        r = run("apply_mappings.py", self.st, m, ids=False)
        self.assertEqual(r.returncode, 1)
        self.assertIn("build the page once", r.stderr)
        for effect in ("upgrades none->partial", "adds to existing coverage", "conflicts with BR-99"):
            with self.subTest(effect):
                with open(m, "w", newline="", encoding="utf-8") as f:
                    csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                             ["PROJ-5", h, "BR-99", effect, "Users export orders as PDF", ""]])
                r = run("apply_mappings.py", self.st, m)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("in no catalogue", r.stdout)
        with open(m, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["key", "text_hash", "req_ids", "effect", "quote", "note"],
                                     ["PROJ-5", h, "FR-2", "upgrades none->partial", "Users export orders as PDF", ""]])
        self.assertEqual(run("apply_mappings.py", self.st, m).returncode, 0)

    def test_a_pull_must_prove_it_is_complete(self):
        before = [(self.st / f).read_bytes() for f in ("tracker/now.json", "state.json")]
        newest_first = [item("PROJ-1", description="Users export orders as CSV within 90 days.", ac="A CSV downloads.",
                             updated="2026-10-12T10:00:00.000+0000")]
        no_total = json.dumps({"query": "q", "items": newest_first})
        for case, text in (("truncated", pulled(newest_first, total=2)), ("bare list, no total", json.dumps(newest_first)),
                           ("object without a total", no_total),
                           ("duplicate key", pulled(newest_first * 2))):
            with self.subTest(case):
                (self.d / "pull.json").write_text(text, encoding="utf-8")
                r = run("tracker_merge.py", self.st, self.d / "pull.json")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertEqual([(self.st / f).read_bytes() for f in ("tracker/now.json", "state.json")], before)
        r = self.merge([item("PROJ-3", description="Keep an audit trail.", updated="2026-10-11T10:00:00.000+0000")]
                       + newest_first)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("watermark 2026-10-12T10:00:00.000+0000", r.stdout)

    def test_symbols_between_digits_are_content(self):
        text = ("Search responds in < 2 s and > 1 s. Keep orders 1.5 years. Store at -20 °C. Ship in 2-5 days. "
                "Load 95% of pages. Retry ≤ 3 times.")
        html_form = ("<p>Search responds in &lt; 2 s and &gt; 1 s.</p><ul><li>Keep orders 1.5 years.</li><li>Store at -20 °C.</li>"
                     "<li>Ship in 2-5 days.</li><li>Load 95% of pages.</li><li>Retry &le; 3 times.</li></ul>")
        text += " Tolerance ± 2 mm. Set x = 50. Dose 1,5 mg."
        html_form = html_form.replace("</ul>", "<li>Tolerance &plusmn; 2 mm.</li><li>Set x = 50.</li><li>Dose 1,5 mg.</li></ul>")
        edits = [("< 2 s", "> 2 s"), ("< 2 s", "<= 2 s"), ("< 2 s", "2 s"), ("≤ 3", "3"), ("1.5 years", "15 years"),
                 ("-20 °C", "20 °C"), ("2-5 days", "25 days"), ("95%", "95"), ("± 2 mm", "2 mm"), ("= 50", "50"),
                 ("1,5 mg", "15 mg"), ("< 2 s and", "< 3 s and")]
        export = lambda d: [{"key": "PROJ-1", "fields": {"summary": "Search", "status": {"name": "To Do"},
                             "issuetype": {"name": "Story"}, "updated": "2026-10-01", "description": d, "customfield_100": ""}}]
        for n, (a, b) in enumerate(edits):
            with self.subTest(f"{a} -> {b}"):
                st = self.d / f"sym{n}"
                (self.d / "sx.json").write_text(json.dumps(export(text)), encoding="utf-8")
                self.assertEqual(run("init_state.py", st, "--tracker-export", self.d / "sx.json", "--ac-field",
                                     "customfield_100").returncode, 0)
                for arm, first in (("first sighting", text.replace(a, b)), ("later pull", None)):
                    if first is None:
                        (self.d / "p.json").write_text(pulled([item("PROJ-1", summary="Search", description=html_form)]), encoding="utf-8")
                        r = run("tracker_merge.py", st, self.d / "p.json")
                        self.assertIn("text changed (baseline items) 0", r.stdout)
                        first = text.replace(a, b)
                    else:
                        st2 = self.d / f"sym{n}b"
                        shutil.copytree(st, st2)
                    (self.d / "p.json").write_text(pulled([item("PROJ-1", summary="Search", description=first)]), encoding="utf-8")
                    r = run("tracker_merge.py", st if arm == "later pull" else st2, self.d / "p.json")
                    self.assertIn("text changed (baseline items) 1", r.stdout, arm)

    def test_markup_before_a_number_is_not_a_symbol(self):
        import importlib.util
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("tm", REFRESH / "tracker_merge.py")
        tm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tm)
        for wiki, other in (("Retention: -30 days- 90 days", "Retention: ~~30 days~~ 90 days"),
                            ("Retention: -30 days- 90 days", "<p>Retention: <del>30 days</del> 90 days</p>"),
                            ("bq. 20 users at once", "> 20 users at once"), ("Limits\n20 users", "Limits\n======\n20 users"),
                            ("Search in < *2 s*", "Search in &lt; <strong>2 s</strong>")):
            with self.subTest(other):
                self.assertEqual(tm.norm_text(wiki.replace("bq. ", "")), tm.norm_text(other))
        for a, b in (("x < 2 s", "x > 2 s"), ("Store at -20 °C", "Store at 20 °C"), ("2-5 days", "25 days")):
            with self.subTest(a):
                self.assertNotEqual(tm.norm_text(a), tm.norm_text(b))

    def test_a_reopened_export_item_the_trace_places_is_not_to_map(self):
        (self.st / "traced-keys.json").write_text(json.dumps(["PROJ-2"]), encoding="utf-8")
        self.merge([item("PROJ-2", description="x"), item("PROJ-3", description="Keep an audit trail.")])
        self.assertEqual(json.loads((self.st / "tomap.json").read_text(encoding="utf-8")), [])
        self.assertTrue(json.loads((self.st / "tracker/now.json").read_text(encoding="utf-8"))["PROJ-2"]["reopened"])
        self.assertIn("PROJ-2", self.flags()["reopened_keys"])

    def test_a_reopened_export_item_is_mapped_like_a_new_one(self):
        r = self.merge([item("PROJ-2", description="x"), item("PROJ-3", description="Keep an audit trail.")])
        tomap = [d["key"] for d in json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))]
        self.assertEqual(tomap, ["PROJ-2"])
        now = json.loads((self.st / "tracker/now.json").read_text(encoding="utf-8"))
        self.assertTrue(now["PROJ-2"]["reopened"])
        self.merge([item("PROJ-2", description="x", summary="Old again")])
        self.assertEqual([d["key"] for d in json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))], ["PROJ-2"])
        self.merge([item("PROJ-2", status="Cancelled", description="x", summary="Old again")])
        self.assertEqual(json.loads((self.st / "tomap.json").read_text(encoding="utf-8")), [])
        self.assertFalse(json.loads((self.st / "tracker/now.json").read_text(encoding="utf-8"))["PROJ-2"]["reopened"])

    def test_typographic_apostrophe_negation(self):
        ac = "Given an order list, when I export, then a CSV downloads."
        self.merge([item("PROJ-1", description="Users export orders as CSV within 30 days.",
                         ac=ac.replace("then a CSV downloads", "then a CSV isn\u2019t downloaded"))])
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])

    def test_accept_tracker_keeps_a_key_reworded_after_the_review(self):
        same = item("PROJ-1", description="Users export orders as CSV within 30 days.",
                    ac="Given an order list, when I export, then a CSV downloads.")
        self.merge([same])
        self.merge([dict(same, ac="Given a list, the export is a signed PDF archive.")])
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])
        self.review()
        self.merge([dict(same, ac="Users never export orders.")])
        self.assertEqual(run("accept.py", self.st, "tracker").returncode, 0)
        self.assertEqual(self.flags()["text_changed_keys"], ["PROJ-1"])
        self.review()
        self.assertEqual(run("accept.py", self.st, "tracker").returncode, 0)
        self.assertEqual(self.flags()["text_changed_keys"], [])

    def test_atomic_write_leaves_the_target_whole_on_a_crash(self):
        import importlib.util, os
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("tm", REFRESH / "tracker_merge.py")
        tm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tm)
        target = self.d / "mappings.csv"
        target.write_text("key\nPROJ-1\n", encoding="utf-8")
        real = os.replace

        def boom(*a):
            raise OSError("disk full")
        tm.os.replace = boom
        try:
            with self.assertRaises(OSError):
                tm.atomic_write(target, "key\n")
        finally:
            tm.os.replace = real
        self.assertEqual(target.read_text(encoding="utf-8"), "key\nPROJ-1\n")
        self.assertEqual([p.name for p in self.d.iterdir() if p.name.startswith(".mappings")], [])

    def write_mapped(self, rows):
        p = self.d / "mapped.csv"
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["key", "text_hash", "req_ids", "effect", "quote", "note"])
            w.writerows(rows)
        return run("apply_mappings.py", self.st, p)

    def test_effects_are_exact(self):
        self.merge([item("PROJ-5", description="Users export orders as PDF every day.")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        quote = "Users export orders as PDF"
        for effect, ids, ok in (("upgrades none->partial typo", "FR-2", False), ("no requirement but it exports", "", False),
                                ("adds to existing coverage!", "FR-2", False), ("no requirement (engineering)", "", True),
                                ("Upgrades  None->Partial", "FR-2", True), ("conflicts with FR-2", "FR-2", True)):
            with self.subTest(effect):
                r = self.write_mapped([["PROJ-5", h, ids, effect, quote if ids else "", ""]])
                self.assertEqual(r.returncode == 0, ok, r.stdout)

    def test_a_quote_needs_letters(self):
        self.merge([item("PROJ-6", description="Fix the build 12345678901234567890")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        r = self.write_mapped([["PROJ-6", h, "FR-3", "adds to existing coverage", "12345678901234567890", ""]])
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("too short", r.stdout)

    def test_a_mapping_is_amended_at_the_same_text(self):
        self.merge([item("PROJ-5", description="Users export orders as PDF every day.")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        quote = "Users export orders as PDF"
        self.assertEqual(self.write_mapped([["PROJ-5", h, "FR-2", "adds to existing coverage", quote, ""]]).returncode, 0)
        self.merge([item("PROJ-5", description="Users export orders as PDF every day.")])
        self.assertEqual(json.loads((self.st / "tomap.json").read_text(encoding="utf-8")), [])
        r = self.write_mapped([["PROJ-5", h, "FR-2;FR-3", "adds to existing coverage", quote, ""]])
        self.assertEqual(r.returncode, 0, r.stdout)
        rows = {x["key"]: x for x in csv.DictReader((self.st / "mappings.csv").read_text(encoding="utf-8").splitlines())}
        self.assertEqual(rows["PROJ-5"]["req_ids"], "FR-2;FR-3")
        r = self.write_mapped([["PROJ-5", h, "FR-2", "adds to existing coverage", "Users export invoices as PDF", ""]])
        self.assertIn("quote is not in", r.stdout)
        self.assertEqual(self.write_mapped([["PROJ-7", h, "FR-2", "adds to existing coverage", quote, ""]]).returncode, 1)

    def test_an_empty_complete_pull_is_recorded(self):
        (self.d / "p0.json").write_text(pulled([]), encoding="utf-8")
        r = run("tracker_merge.py", self.st, self.d / "p0.json")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads((self.st / "state.json").read_text(encoding="utf-8"))["last_pull"]["items"], 0)
        (self.d / "p1.json").write_text(pulled([], total=1), encoding="utf-8")
        self.assertEqual(run("tracker_merge.py", self.st, self.d / "p1.json").returncode, 1)

    def test_structured_text_fields_are_read_as_text(self):
        r = self.merge([item("PROJ-9", description={"type": "doc", "text": "Export"}, ac=["Given a list", "then a CSV"])])
        self.assertEqual(r.returncode, 0, r.stderr)
        tomap = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))
        self.assertEqual(tomap[0]["ac"], "Given a list\nthen a CSV")
        export = [{"key": "PROJ-1", "fields": {"summary": "s", "status": {"name": "To Do"}, "issuetype": {"name": "Story"},
                                               "updated": "2026-10-01", "description": {"type": "doc"}, "x": ["a", "b"]}}]
        (self.d / "i2.json").write_text(json.dumps(export), encoding="utf-8")
        r = run("init_state.py", self.d / "st2", "--tracker-export", self.d / "i2.json", "--ac-field", "x")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(json.loads((self.d / "st2/tracker/now.json").read_text(encoding="utf-8"))["PROJ-1"]["has_ac"])

    def test_the_trace_suppresses_only_export_items(self):
        self.merge([item("PROJ-5", description="Users export orders as PDF every day.")])
        h = json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))[0]["text_hash"]
        self.write_mapped([["PROJ-5", h, "FR-2", "adds to existing coverage", "Users export orders as PDF", ""]])
        (self.st / "traced-keys.json").write_text(json.dumps(["PROJ-5"]), encoding="utf-8")
        self.merge([item("PROJ-5", description="Users export orders as PDF and XLSX every day.")])
        self.assertEqual([d["key"] for d in json.loads((self.st / "tomap.json").read_text(encoding="utf-8"))], ["PROJ-5"])

    def test_init_writes_its_marker_last(self):
        st = self.d / "st3"
        (st / "baseline.json").mkdir(parents=True)
        r = run("init_state.py", st, "--tracker-export", self.d / "issues.json", "--ac-field", "none")
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse((st / "tracker/now.json").exists())

    def test_whiteboard_paths_are_fixed_at_init(self):
        w = [dict(x, label="L") for x in self.widgets]
        (self.d / "b2.json").write_text(json.dumps(w), encoding="utf-8")
        r = run("source_check.py", self.st, "whiteboard", self.d / "b2.json", "--map", "text=label")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("differs from the paths", r.stderr)
        self.assertEqual(run("source_check.py", self.st, "whiteboard", self.d / "b2.json").returncode, 0)
        self.review()
        r = run("accept.py", self.st, "whiteboard", self.d / "b2.json", "--map", "text=label")
        self.assertEqual(r.returncode, 1, r.stdout)
        widgets = json.loads((self.st / "baseline.json").read_text(encoding="utf-8"))["whiteboards"]["board"]["widgets"]
        self.assertEqual(widgets["w1"]["text"], "Export orders")

    def test_accept_reports_unreadable_state(self):
        (self.st / "flags.json").write_text("{bad", encoding="utf-8")
        r = run("accept.py", self.st, "tracker")
        self.assertEqual(r.returncode, 1)
        self.assertIn("ERROR:", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_repeated_slide_text_is_matched_per_occurrence(self):
        a, b = "Same text on two slides", "Other slide"
        make_pptx(self.d / "d0.pptx", [a, a, b])
        st = self.d / "st4"
        run("init_state.py", st, "--tracker-export", self.d / "issues.json", "--ac-field", "none", "--deck", f"deck={self.d / 'd0.pptx'}")
        for texts, changed in (([a, b, b], [2]), ([a, b], [2]), ([b, a, a], [])):
            with self.subTest(texts):
                make_pptx(self.d / "d1.pptx", texts)
                run("source_check.py", st, "deck", self.d / "d1.pptx")
                self.assertEqual(json.loads((st / "flags.json").read_text(encoding="utf-8"))["decks"]["deck"]["changed_slides"], changed)


if __name__ == "__main__":
    unittest.main()
