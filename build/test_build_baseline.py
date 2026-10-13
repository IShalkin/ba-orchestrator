"""Behaviour tests for scripts/build_baseline.py on a tiny run directory built in a temp dir. The trace and its
coverage summary are written by the real merge_trace.py, so the page is tested against what production feeds it.
Stdlib only."""
import csv, json, re, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "skills" / "ba-orchestrator" / "scripts"
BROWSE = "https://tracker.example.com/browse/"
DECK_URL = "https://files.example.com/sites/acme/deck.pptx"
BOARD_URL = "https://board.example.com/acme/b1?wid=w-1"
SCHEMA = ["req_id", "req_type", "capability", "jira_keys", "coverage", "jira_statuses", "mvp_class_source",
          "mvp_class_jira", "conflict_flags", "gap_note", "evidence"]
EV6 = "## Evidence\n| id | source | locator | url | date | quote |\n|---|---|---|---|---|---|\n"
EV5 = "## Evidence\n| id | source | locator | date | quote |\n|---|---|---|---|---|\n"


def research(rid, table, rows):
    return (f"# Research {rid}\nSources searched: x\n\n## Findings by research question\n### RQ1\nok\n\n" + table
            + "".join(rows))


def write_csv(path, head, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(rows)


class BuildBaselineTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        run = self.run = Path(self.tmp.name) / "20261012-1200-acme"
        for d in ("02-research", "03-artifacts/cat", "04-synthesis", "06-final", "merge"):
            (run / d).mkdir(parents=True)
        (run / "02-research/R1.md").write_text(research("R1", EV6, [
            f"| R1-1 | deck | ACME scope.pptx slide 3 → /tmp/x-staging/slide-003.md | {DECK_URL} | 2026-10-01 | \"Users export orders\" |\n",
            f"| R1-2 | deck | ACME scope.pptx slide 5 | {DECK_URL} | 2026-10-01 | \"Weekly | report\" |\n",
            f"| R1-3 | deck | ACME scope.pptx slides 7-9 (staged /tmp/acme-staging/s7.md) | {DECK_URL} | 2026-10-01 | \"Archive\" |\n"]),
            encoding="utf-8")
        (run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1, widget w-1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, widget w-2 | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        (run / "02-research/R4.md").write_text(research("R4", EV5, [
            "| R4-1 | wiki | Requirements page §2 | 2026-09-30 | \"Must keep an audit trail\" |\n"]), encoding="utf-8")
        write_csv(run / "03-artifacts/cat/br.csv", ["id", "statement", "sources"], [
            ["BR-1", "Users can export orders [E:R1-1]", "R1-1; R2-1"],
            ["BR-2", "Keep an audit trail", "R4-1, R2-2"],
            ["BR-3", "A weekly report goes to managers", "R1-2"],
            ["BR-4", "Archive orders after a year", "R1-3"]])
        write_csv(run / "03-artifacts/cat/fr.csv", ["id", "statement", "capability", "evidence"], [
            ["FR-1", "Export to CSV", "Export", "R1-1"],
            ["FR-2", "Export to PDF", "Export", ""],
            ["FR-3", "Log every change", "Audit", "R4-1"]])
        write_csv(run / "merge/trace.csv", SCHEMA, [
            ["BR-1", "BR", "Export", "PROJ-1", "full", "", "", "", "", "", "R1-1"],
            ["BR-2", "BR", "Audit", "", "none", "", "", "", "", "no issue states it [E:R4-1]", ""],
            ["FR-1", "FR", "Export", "PROJ-1, PROJ-7", "partial", "", "", "", "", "PDF variant missing", ""],
            ["FR-2", "FR", "Export", "PROJ-2..PROJ-3", "full", "", "", "", "", "", ""],
            ["FR-3", "FR", "Audit", "PROJ-4", "none", "", "", "", "", "", ""],
            ["FR-3", "FR", "Audit", "PROJ-4", "full", "", "", "", "", "", ""],
            ["BR-4", "BR", "Audit", "PROJ-11", "full", "", "", "", "", "", ""]])
        issues = [{"key": f"PROJ-{n}", "fields": {"summary": f"Item {n}", "status": {"name": s}}}
                  for n, s in ((1, "Done"), (2, "To Do"), (3, "To Do"), (4, "Done"), (7, "Done"), (8, "To Do"),
                               (9, "In Progress"), (10, "Cancelled"), (11, "Done"))]
        (run / "merge/issues.json").write_text(json.dumps(issues), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(SCRIPTS / "stage" / "merge_trace.py"), str(run / "merge"),
                            "--trace", str(run / "merge/trace.csv"), "--issues", str(run / "merge/issues.json")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        (run / "04-synthesis/conflicts.md").write_text(
            "| id | severity | topic | side A | side B |\n|---|---|---|---|---|\n"
            "| CF-01 | High | **Export** format | deck says CSV | board says PDF |\n", encoding="utf-8")
        self.manifest = {
            "title": "ACME orders: business and functional requirements compared with the sources",
            "request_verbatim": "Document the business and functional requirements and compare them with the tickets, "
                                "the whiteboard and the slide deck.",
            "catalogues": [{"type": "BR", "path": "03-artifacts/cat/br.csv", "id_col": "id", "statement_col": "statement"},
                           {"type": "FR", "path": "03-artifacts/cat/fr.csv", "id_col": "id", "statement_col": "statement",
                            "group_col": "capability"}],
            "trace": "merge/trace-merged.csv", "coverage_summary": "merge/coverage-summary.json",
            "sources": [{"name": "Slide deck", "evidence_prefixes": ["R1"], "kind": "deck", "id": "deck"},
                        {"name": "Whiteboard", "evidence_prefixes": ["R2"], "kind": "whiteboard", "id": "board"},
                        {"name": "Wiki", "evidence_prefixes": ["R4"], "kind": "wiki"},
                        {"name": "Tracker", "evidence_prefixes": ["R3"], "kind": "tracker"}],
            "tracker": {"browse_url": BROWSE}, "conflicts": "04-synthesis/conflicts.md"}

    def tearDown(self):
        self.tmp.cleanup()

    def build(self, **changes):
        m = dict(self.manifest, **changes)
        (self.run / "06-final/baseline-manifest.json").write_text(json.dumps(m), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(SCRIPTS / "build_baseline.py"), str(self.run)],
                           capture_output=True, text=True)
        out = self.run / "06-final/baseline.html"
        return r, out.read_text(encoding="utf-8") if out.exists() else None

    def row(self, page, rid):
        m = re.search(rf'<tr><td class="id">{rid}</td>.*?</tr>', page)
        self.assertIsNotNone(m, rid)
        return m[0]

    def test_links_present_and_correct(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        br1 = self.row(page, "BR-1")
        self.assertIn(f'href="{DECK_URL}"', br1)
        self.assertRegex(br1, r'<a href="[^"]+deck\.pptx"[^>]*title="ACME scope\.pptx slide 3: &quot;Users export orders&quot;">slide 3</a>')
        self.assertIn('href="https://board.example.com/acme/b1?wid=w-1"', br1)
        self.assertIn(f'<a href="{BROWSE}PROJ-1" target="_blank" rel="noopener">PROJ-1</a>', br1)
        self.assertNotIn("x-staging", page)
        self.assertIn("Users can export orders</td>", br1)
        fr2 = self.row(page, "FR-2")
        for k in ("PROJ-2", "PROJ-3"):
            self.assertIn(f'href="{BROWSE}{k}"', fr2)
        self.assertIn('<div class="note">PDF variant missing</div>', self.row(page, "FR-1"))
        self.assertIn('class="cov c-nt">Not traced', self.row(page, "BR-3"))
        self.assertIn('<tr class="grp"><td colspan="7">Export</td></tr>', page)
        self.assertIn("CF-01", page)
        self.assertIn("<b>Export</b> format", page)
        for n in (8, 9):
            self.assertIn(f'<td class="id"><a href="{BROWSE}PROJ-{n}"', page)
        self.assertNotIn("PROJ-10", page)
        self.assertNotIn("<script src", page)
        self.assertNotIn('<link ', page)

    def test_in_short_counts_match_the_trace(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        short = page.split('<section id="short">')[1].split("</section>")[0]
        self.assertIn(self.manifest["request_verbatim"], short)
        self.assertLessEqual(short.count("<li>"), 5)
        summ = json.loads((self.run / "merge/coverage-summary.json").read_text(encoding="utf-8"))["per_req_type"]
        for t, total, not_traced in (("BR", 4, 1), ("FR", 3, 0)):
            c = summ[t]
            want = f"{t}: {c.get('full', 0)} full, {c.get('partial', 0)} partial, {c.get('none', 0)} none"
            self.assertIn(want + (f", {not_traced} not traced" if not_traced else "") + "", short)
            self.assertIn(f">{total} {t}</a>", short)
        self.assertIn("Slide deck backs 4 of 7 requirements", short)
        self.assertIn("Whiteboard backs 2 of 7 requirements", short)
        self.assertIn("2 requirements with no tracker issue", short)
        self.assertIn("2 tracker issues referenced by no requirement", short)
        self.assertIn("1 conflict between the sources", short)

    def test_summary_mismatch_refuses_to_write(self):
        p = self.run / "merge/coverage-summary.json"
        s = json.loads(p.read_text(encoding="utf-8"))
        s["per_req_type"]["FR"]["full"] += 1
        p.write_text(json.dumps(s), encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("disagree", r.stderr)
        self.assertIsNone(page)

    def test_banned_pattern_refuses_to_write(self):
        for name, cat_text, extra in (("home path", "Export to /Users/someone/x.csv", None),
                                      ("aws key", "key AKIA" + "A" * 16, None),
                                      ("twelve digits", "account 123456789012", None),
                                      ("manifest pattern", "Export to CSV for ACME-INTERNAL", [r"ACME-INTERNAL"])):
            with self.subTest(name):
                write_csv(self.run / "03-artifacts/cat/fr.csv", ["id", "statement", "capability", "evidence"],
                          [["FR-1", cat_text, "Export", ""], ["FR-2", "x", "Export", ""], ["FR-3", "y", "Audit", ""]])
                (self.run / "06-final/baseline.html").unlink(missing_ok=True)
                r, page = self.build(**({"banned_patterns": extra} if extra else {}))
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("banned pattern", r.stderr)
                if not extra:
                    self.assertNotIn(cat_text.split()[-1], r.stderr)
                self.assertIsNone(page)

    def test_tracker_key_inside_an_attribute_is_not_linked(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('title="board b1, widget w-1: &quot;Export also covers PROJ-7 scope&quot;"', page)
        self.assertNotRegex(page, r'title="[^"]*<a')
        self.assertNotRegex(page, r"<a [^>]*>[^<]*<a ")
        visible = re.sub(r"<[^>]*>", "", page.split("<style>")[0] + page.split("</style>")[1]).count("PROJ-7")
        self.assertEqual(len(re.findall(rf'<a href="{BROWSE}PROJ-7"[^>]*>PROJ-7</a>', page)), visible)

    def test_legacy_evidence_without_url_renders_without_a_link(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fr3 = self.row(page, "FR-3")
        wiki = re.findall(r"<td>(.*?)</td>", fr3)[3]
        self.assertIn("✓", wiki)
        self.assertIn('<span class="nolink" title="Requirements page §2: &quot;Must keep an audit trail&quot;">1</span>', wiki)
        self.assertNotIn("href", wiki)
        br2 = self.row(page, "BR-2")
        self.assertIn('<span class="nolink" title="board b1, widget w-2', br2)

    def test_count_check_is_per_requirement(self):
        p = self.run / "merge/trace-merged.csv"
        t = p.read_text(encoding="utf-8")
        t = t.replace("FR-1,FR,Export,\"PROJ-1, PROJ-7\",partial", "FR-1,FR,Export,\"PROJ-1, PROJ-7\",full")
        t = t.replace("FR-2,FR,Export,PROJ-2..PROJ-3,full", "FR-2,FR,Export,PROJ-2..PROJ-3,partial")
        self.assertIn("PROJ-7\",full", t)
        p.write_text(t, encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("disagree for 2 requirement(s)", r.stderr)
        self.assertIsNone(page)

    def test_duplicate_trace_id_counts_its_lowest_coverage(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('class="cov c-none">None', self.row(page, "FR-3"))

    def test_duplicate_catalogue_id_or_type_mismatch_refused(self):
        br = self.run / "03-artifacts/cat/br.csv"
        orig = br.read_text(encoding="utf-8")
        br.write_text(orig + "BR-1,Same id twice,R1-1\n", encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("listed twice", r.stderr)
        br.write_text(orig, encoding="utf-8")
        m = dict(self.manifest)
        m["catalogues"] = [dict(c, type="Business") if c["type"] == "BR" else c for c in m["catalogues"]]
        r, page = self.build(catalogues=m["catalogues"])
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("the catalogue says Business, the trace's req_type says BR", r.stderr)

    def test_banned_patterns_in_every_view(self):
        def fr(text, group="Export"):
            write_csv(self.run / "03-artifacts/cat/fr.csv", ["id", "statement", "capability", "evidence"],
                      [["FR-1", text, group, "R1-1"], ["FR-2", "x", "Export", ""], ["FR-3", "y", "Audit", ""]])
        for name, text, group, extra in (
                ("home dir", "see /home/someone/notes.md", "Export", None),
                ("lower-case users dir", "see /users/someone/x.csv", "Export", None),
                ("windows any case", r"copy c:\users\someone\x.csv", "Export", None),
                ("windows upper", r"copy C:\Users\someone\x.csv", "Export", None),
                ("temporary key", "key ASIA" + "B" * 16, "Export", None),
                ("grouped digits", "account 1234-5678-9012", "Export", None),
                ("evidence tag in a group header", "Export to CSV", "Export [E:R1-1]", None),
                ("escaped ampersand", "Export for Procter & Gamble", "Export", [r"Procter & Gamble"]),
                ("escaped apostrophe", "Ask O'Neil", "Export", [r"O'Neil"]),
                ("key split by a link", "Owner PROJ-7 Smith", "Export", [r"PROJ-7 Smith"]),
                ("manifest pattern any case", "acme-internal note", "Export", [r"ACME-INTERNAL"])):
            with self.subTest(name):
                fr(text, group)
                (self.run / "06-final/baseline.html").unlink(missing_ok=True)
                r, page = self.build(**({"banned_patterns": extra} if extra else {}))
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("banned pattern", r.stderr)
                self.assertIsNone(page)
        fr("See https://board.example.com/users/42 for owners")
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_link_note_states_only_what_is_true(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("Every check mark", page)
        self.assertRegex(page, r"\d+ of \d+ cited source items link to their source; the other \d+ have no addressable URL")
        self.assertIn("R4.md: 1 evidence rows without a url column", r.stdout)
        write_csv(self.run / "03-artifacts/cat/br.csv", ["id", "statement", "sources"], [
            ["BR-1", "Users can export orders", "R1-1; R2-1"], ["BR-2", "Keep an audit trail", ""],
            ["BR-3", "A weekly report goes to managers", "R1-2"], ["BR-4", "Archive", "R1-3"]])
        write_csv(self.run / "03-artifacts/cat/fr.csv", ["id", "statement", "capability", "evidence"], [
            ["FR-1", "Export to CSV", "Export", ""], ["FR-2", "Export to PDF", "Export", ""], ["FR-3", "Log", "Audit", ""]])
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Every cited source item (", page)
        r, page = self.build(tracker={})
        self.assertIn("Tracker keys are not linked (no browse URL).", page)

    def test_locators_and_slide_ranges(self):
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("acme-staging", page)
        self.assertNotIn("(staged", page)
        self.assertIn(">slides 7, 8, 9</a>", self.row(page, "BR-4"))
        self.assertIn("&quot;Weekly | report&quot;", self.row(page, "BR-3"))
        (self.run / "02-research/R1.md").write_text(research("R1", EV6, [
            f"| R1-1 | deck | ACME scope.pptx slide 3, see C:\\stage\\s3.md and ~/stage/s3.md | {DECK_URL} | 2026 | \"q\" |\n",
            f"| R1-2 | deck | slide 5 | https://... | 2026 | \"q\" |\n",
            f"| R1-3 | deck | slides 7-9 | {DECK_URL} | 2026 | \"q\" |\n"]), encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("stage", page.split("<style>")[0] + page.split("</style>")[1])
        self.assertIn('<span class="nolink" title="slide 5: &quot;q&quot;">slide 5</span>', self.row(page, "BR-3"))

    def state(self):
        st = self.run.parent / "state"
        (st / "tracker").mkdir(parents=True)
        now = {k: {"key": k, "status": s, "summary": f"Item {k}", "in_export": e, "text_hash": f"h{k[5:]}"} for k, s, e in (
            ("PROJ-1", "Done", True), ("PROJ-4", "Done", True), ("PROJ-8", "To Do", True), ("PROJ-9", "In Progress", True),
            ("PROJ-20", "To Do", False), ("PROJ-21", "Cancelled", False), ("PROJ-22", "To Do", False),
            ("PROJ-23", "To Do", False), ("PROJ-24", "To Do", False))}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        write_csv(st / "mappings.csv", ["key", "text_hash", "req_ids", "effect", "quote", "note"], [
            ["PROJ-20", "h20", "BR-2, FR-2", "upgrades none->partial", "keep an audit trail", ""],
            ["PROJ-21", "h21", "BR-3", "upgrades none->partial", "weekly report", ""],
            ["PROJ-9", "h9", "BR-3", "upgrades none->partial", "weekly report", ""],
            ["PROJ-22", "h22", "", "no requirement", "", ""],
            ["PROJ-23", "h23", "FR-3", "conflicts with FR-3", "logging is optional", ""],
            ["PROJ-24", "h-old", "FR-3", "upgrades none->partial", "log every change", ""]])
        (st / "flags.json").write_text(json.dumps({
            "decks": {"deck": {"md5": "d1", "changed_slides": [5, 8], "moved_slides": [{"from": 3, "to": 4}],
                               "new_slides": [6], "inserted_slides": [6]}},
            "whiteboards": {"board": {"md5": "b1", "changed": ["w-2"], "deleted": [], "added": ["w-9"],
                                      "added_text": {"w-9": "Encrypt exports"}}},
            "cancelled_keys": ["PROJ-4"], "text_changed_keys": ["PROJ-1", "PROJ-8"],
            "by_hand": {"Wiki": {"checked_at": "2026-10-13T09:30:00", "accepted": True}}}), encoding="utf-8")
        (st / "baseline.json").write_text(json.dumps({"whiteboards": {"board": {"md5": "b0", "widgets": {
            "w-1": {"sig": "s1", "text": "Export"}, "w-2": {"sig": "s2", "text": "Audit log"}}}}}), encoding="utf-8")
        (st / "state.json").write_text(json.dumps({"last_pull": {"at": "2026-10-13T09:00:00", "file": "p.json",
                                                                 "items": 9}}), encoding="utf-8")
        return st

    def test_refresh_overlay(self):
        st = self.state()
        (st / "curated.json").write_text(json.dumps({"coverage_overrides": {"FR-1": {"coverage": "none",
                                                                                     "reason": "PROJ-7 dropped CSV"}},
                                                     "conflicts": [{"id": "CF-02", "severity": "Low", "topic": "Audit",
                                                                    "side_a": "BR-2", "side_b": "PROJ-20"}]}), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('class="cov c-partial">Partial', self.row(page, "BR-2"))
        self.assertIn(f'href="{BROWSE}PROJ-20"', self.row(page, "BR-2"))
        self.assertIn('class="cov c-full">Full', self.row(page, "FR-2"))
        self.assertIn(f'href="{BROWSE}PROJ-20"', self.row(page, "FR-2"))
        br3 = self.row(page, "BR-3")
        self.assertIn('class="cov c-partial">Partial', br3)
        self.assertNotIn("PROJ-21", br3)
        fr3 = self.row(page, "FR-3")
        self.assertIn('class="cov c-none">None', fr3)
        self.assertNotIn("PROJ-23", fr3)
        self.assertNotIn("PROJ-24", fr3)
        self.assertIn('class="cov c-none">None', self.row(page, "FR-1"))
        self.assertIn("PROJ-7</a> dropped CSV</div>", self.row(page, "FR-1"))
        self.assertIn("CF-02", page)
        unref = page.split('<section id="unref">')[1].split("</section>")[0]
        self.assertIn("PROJ-8", unref)
        self.assertIn("PROJ-22", unref)
        self.assertNotIn("PROJ-9", unref)
        self.assertNotIn("PROJ-21", unref)
        review = json.loads((st / "review.json").read_text(encoding="utf-8"))
        why = {x["req"]: x["why"] for x in review["requirements"]}
        self.assertEqual(why["BR-1"], ["PROJ-1 text changed", "Slide deck: slide 3 moved to 4"])
        self.assertEqual(why["BR-2"], ["Whiteboard: item w-2 changed or deleted"])
        self.assertEqual(why["BR-3"], ["PROJ-21 (mapped: upgrades none->partial) is cancelled", "Slide deck: slide 5 changed"])
        self.assertEqual(why["BR-4"], ["Slide deck: slide 8 changed"])
        self.assertEqual(why["FR-3"], ["PROJ-23: conflicts with FR-3", "PROJ-24 text changed since it was mapped "
                                       "(upgrades none->partial); re-map it", "PROJ-4 cancelled"])
        self.assertEqual(why["FR-1"], ["PROJ-1 text changed", "Slide deck: slide 3 moved to 4"])
        self.assertNotIn("FR-2", why)
        self.assertEqual(review["unreferenced_text_changed"], ["PROJ-8"])
        snap = {k: {"status": s, "text_hash": f"h{k[5:]}"} for k, s in (("PROJ-4", "Done"), ("PROJ-1", "Done"), ("PROJ-8", "To Do"))}
        self.assertEqual(review["reviewed"]["decks"], {"deck": {"md5": "d1"}})
        self.assertEqual(review["reviewed"]["whiteboards"], {"board": {"md5": "b1"}})
        self.assertEqual(review["reviewed"]["tracker"]["cancelled_keys"], {"PROJ-4": snap["PROJ-4"]})
        self.assertEqual(review["reviewed"]["tracker"]["text_changed_keys"], {k: snap[k] for k in ("PROJ-1", "PROJ-8")})
        self.assertEqual(sorted(review["reviewed"]["tracker"]["mappings"]), ["PROJ-21", "PROJ-23", "PROJ-24"])
        self.assertEqual(review["deck_new_slides"], {"deck": [6]})
        self.assertIn("NEEDS REVIEW: 9 (6 requirements whose source changed, 1 re-worded or re-opened items no requirement references, "
                      "1 new slides no citation covers, 1 new whiteboard items, 0 changed whiteboard items no citation "
                      "names, 0 item mappings to review, 0 sources never checked, 0 items not mapped)", r.stdout)
        self.assertNotIn("review", page.lower().split("<style>")[0])

    def test_override_needs_a_reason_and_integrity_runs_before_the_overlay(self):
        st = self.state()
        (st / "curated.json").write_text(json.dumps({"coverage_overrides": {"FR-1": {"coverage": "full"}}}), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("needs coverage full|partial|none and a reason", r.stderr)
        (st / "curated.json").unlink()
        p = self.run / "merge/coverage-summary.json"
        s = json.loads(p.read_text(encoding="utf-8"))
        s["per_req_type"]["BR"]["none"] = 0
        p.write_text(json.dumps(s), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIsNone(page)


    def test_flags_bind_to_sources_by_id(self):
        st = self.state()
        for name, sources in (
                ("no id", [dict(x, id=None) if x["kind"] == "deck" else x for x in self.manifest["sources"]]),
                ("other id", [dict(x, id="slides") if x["kind"] == "deck" else x for x in self.manifest["sources"]]),
                ("id on a source of another kind", [dict(x, kind="wiki") if x["kind"] == "deck" else x
                                                    for x in self.manifest["sources"]])):
            with self.subTest(name):
                r, page = self.build(refresh_state=str(st), sources=sources)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("match no manifest source", r.stderr)
                self.assertIsNone(page)
        bad = [dict(x, kind="slides") if x["kind"] == "deck" else x for x in self.manifest["sources"]]
        r, page = self.build(sources=bad)
        self.assertEqual(r.returncode, 1)
        self.assertIn("is not one of", r.stderr)

    def test_one_cancelled_set(self):
        st = self.state()
        (st / "state.json").write_text(json.dumps({"cancelled_statuses": ["Cancelled", "Canceled", "Won't Do"]}),
                                       encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("one set must govern both", r.stderr)
        r = subprocess.run([sys.executable, "-I", str(SCRIPTS / "stage" / "merge_trace.py"), str(self.run / "merge"),
                            "--trace", str(self.run / "merge/trace.csv"), "--issues", str(self.run / "merge/issues.json"),
                            "--exclude-status", "Cancelled,Canceled,Won't Do"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-20"]["status"] = "Won't Do"
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('class="cov c-none">None', self.row(page, "BR-2"))
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertIn("PROJ-20 (mapped: upgrades none->partial) is cancelled", why["BR-2"])

    def test_banned_text_hidden_by_cutting_or_encoding(self):
        evlog = self.run / "02-research/R1.md"
        orig = evlog.read_text(encoding="utf-8")
        for name, old, new, extra in (
                ("URL-encoded name", DECK_URL, "https://files.example.com/sites/Procter%20Gamble/deck.pptx", ["Procter Gamble"]),
                ("name only in a hover quote", '"Users export orders"', '"Users export orders for Procter & Gamble"',
                 ["Procter & Gamble"])):
            with self.subTest(name):
                evlog.write_text(orig.replace(old, new, 1), encoding="utf-8")
                (self.run / "06-final/baseline.html").unlink(missing_ok=True)
                r, page = self.build(**({"banned_patterns": extra} if extra else {}))
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("banned pattern", r.stderr)
                self.assertIsNone(page)
        evlog.write_text(orig.replace("ACME scope.pptx slide 3 → /tmp/x-staging/slide-003.md",
                                      r"ACME scope.pptx slide 3 (D:\Data Room\Client X\deck.pptx)", 1), encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("Room", page)
        self.assertNotIn("Client X", page)

    def test_slide_locator_spellings(self):
        import importlib.util
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("bb", SCRIPTS / "build_baseline.py")
        bb = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bb)
        for loc, want in (("slide 4", [4]), ("slides 3-5", [3, 4, 5]), ("slides 3–5", [3, 4, 5]), ("slides 3 to 5", [3, 4, 5]),
                          ("slides 3 through 5", [3, 4, 5]), ("slide 3, 4 and 6", [3, 4, 6]), ("slide #4", [4]),
                          ("slide: 4", [4]), ("Slide no. 4", [4]), ("slide (4)", [4]), ("deck.pptx#slide=4", [4]),
                          ("p. 4", [4]), ("pg. 4", [4]), ("pp. 4-5", [4, 5]), ("page 4", [4]), ("pages 2 & 7", [2, 7]),
                          ("board b1", [])):
            with self.subTest(loc):
                self.assertEqual(bb.slide_numbers(loc), want)

    def test_review_branches(self):
        st = self.state()
        (self.run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, widget w-2 | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        (self.run / "02-research/R1.md").write_text(research("R1", EV6, [
            f"| R1-1 | deck | ACME scope.pptx, the export slide | {DECK_URL} | 2026 | \"q\" |\n",
            f"| R1-2 | deck | slide 5 | {DECK_URL} | 2026 | \"q\" |\n",
            f"| R1-3 | deck | slide 9 | {DECK_URL} | 2026 | \"q\" |\n"]), encoding="utf-8")
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["whiteboards"]["board"] = {"md5": "b2", "changed": [], "deleted": ["w-1", "w-2"], "added_text": {}}
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertIn("Whiteboard: item w-1 changed or deleted", why["BR-1"])
        self.assertIn("Whiteboard: item w-2 changed or deleted", why["BR-2"])
        self.assertIn("Slide deck: the deck changed and the citation names no slide number", why["BR-1"])
        self.assertNotIn("BR-4", why)

    def test_a_mapping_naming_an_unknown_id_lifts_nothing(self):
        st = self.state()
        r, page = self.build(refresh_state=str(st))
        self.assertIn("PROJ-20", self.row(page, "FR-2"))
        rows = (st / "mappings.csv").read_text(encoding="utf-8").replace('"BR-2, FR-2"', '"BR-2, FR-2, XX-99"')
        (st / "mappings.csv").write_text(rows, encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("PROJ-20", self.row(page, "FR-2"))
        self.assertIn("PROJ-20", page.split('<section id="unref">')[1].split("</section>")[0])

    def test_unknown_ids_and_override_values(self):
        st = self.state()
        with open(st / "mappings.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["PROJ-23", "h23", "XX-99", "adds to existing coverage", "q", ""])
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stderr)
        unlinked = json.loads((st / "review.json").read_text(encoding="utf-8"))["mapping_problems_unlinked"]
        self.assertIn("names requirement id(s) ['XX-99'] that are in no catalogue", unlinked.get("PROJ-23", ""))
        self.assertIn("1 item mappings to review", r.stdout)
        (st / "curated.json").write_text(json.dumps({"coverage_overrides": {"FR-1": {"coverage": "complete",
                                                                                     "reason": "x"}}}), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("needs coverage full|partial|none", r.stderr)

    def test_whiteboard_citation_without_an_item_id(self):
        st = self.state()
        (self.run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1, widget w-1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, the Audit area | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertIn("Whiteboard: the whiteboard changed and the citation names no item id", why["BR-2"])
        self.assertNotIn("Whiteboard: the whiteboard changed and the citation names no item id", why["BR-1"])
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["whiteboards"]["board"] = {"md5": "b1", "changed": [], "deleted": [], "added": [], "added_text": {}}
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        self.build(refresh_state=str(st))
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertNotIn("BR-2", why)
        flags["whiteboards"]["board"].update(added=["w-9"], added_text={"w-9": "Encrypt exports"})
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        self.build(refresh_state=str(st))
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertIn("Whiteboard: the whiteboard changed and the citation names no item id", why["BR-2"])

    def test_cancelled_trace_keys_lower_coverage(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-2"] = {"key": "PROJ-2", "status": "Cancelled", "summary": "x", "in_export": True, "text_hash": "h2"}
        now["PROJ-3"] = {"key": "PROJ-3", "status": "To Do", "summary": "x", "in_export": True, "text_hash": "h3"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        write_csv(st / "mappings.csv", ["key", "text_hash", "req_ids", "effect", "quote", "note"], [])
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fr2 = self.row(page, "FR-2")
        self.assertIn('class="cov c-partial">Partial', fr2)
        self.assertNotIn("PROJ-2<", fr2)
        now["PROJ-3"]["status"] = "Cancelled"
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["cancelled_keys"] = ["PROJ-2", "PROJ-3"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertIn('class="cov c-none">None', self.row(page, "FR-2"))
        why = {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}
        self.assertIn("PROJ-2 cancelled", why["FR-2"])
        flags["cancelled_keys"] = []
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertIn('class="cov c-none">None', self.row(page, "FR-2"))

    def test_guid_in_a_link_is_not_an_account_id(self):
        guid = "https://files.example.com/_layouts/15/Doc.aspx?sourcedoc=%7B1a2b3c4d-5e6f-4a1b-8c9d-123456789012%7D&file=d.pptx"
        log = self.run / "02-research/R1.md"
        orig = log.read_text(encoding="utf-8")
        for url in (guid, guid.replace("%7B", "{").replace("%7D", "}"), guid.replace("5e6f-4a1b-8c9d", "1234-4567-8901")):
            with self.subTest(url):
                log.write_text(orig.replace(DECK_URL, url, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        log.write_text(orig.replace(DECK_URL, "https://files.example.com/acct/123456789012/deck.pptx", 1), encoding="utf-8")
        (self.run / "06-final/baseline.html").unlink()
        r, page = self.build()
        self.assertEqual(r.returncode, 1, r.stdout)
        log.write_text(orig.replace(DECK_URL, "https://files.example.com/acct/123456789012-abcd-4abc-8abc-abcdefabcdef/d", 1),
                       encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("(in R1-1", r.stderr)
        self.assertNotIn("123456789012", r.stderr)

    def test_home_path_locator_is_withheld_not_refused(self):
        log = self.run / "02-research/R1.md"
        orig = log.read_text(encoding="utf-8")
        for loc in ("/Users/John Smith Jr/deck.pptx slide 3", r"C:\Users\Jo Smith\Downloads\ACME scope.pptx slide 3",
                    "/home/jsmith/ACME scope.pptx slide 3", "/Volumes/Macintosh HD/Users/Jo Smith/deck.pptx slide 3",
                    "~jsmith/ACME scope.pptx slide 3", r"\\fs01\home$\Jo Smith\deck.pptx slide 3",
                    r"\\fs01\Users\jsmith\deck.pptx slide 3"):
            with self.subTest(loc):
                log.write_text(orig.replace("ACME scope.pptx slide 3 → /tmp/x-staging/slide-003.md", loc, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                self.assertIn("name a local home folder and are shown without the locator: ['R1-1']", r.stdout)
                for leak in ("Smith", "Jr/", "jsmith", "Users/", "Users\\", "Downloads"):
                    self.assertNotIn(leak, page)
                self.assertIn('title="&quot;Users export orders&quot;">slide 3</a>', self.row(page, "BR-1"))

    def test_duplicate_source_ids_refused(self):
        r, page = self.build(sources=[dict(x, id="deck") if x["kind"] in ("deck", "whiteboard") else x
                                      for x in self.manifest["sources"]])
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("source ids must be unique", r.stderr)

    def test_acknowledged_mapping_problems_leave_the_review(self):
        st = self.state()
        accept = [sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "tracker"]

        def why():
            self.build(refresh_state=str(st))
            return {x["req"]: x["why"] for x in json.loads((st / "review.json").read_text(encoding="utf-8"))["requirements"]}

        def effect(old, new):
            p = st / "mappings.csv"
            p.write_text(p.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
        self.assertIn("PROJ-23: conflicts with FR-3", why()["FR-3"])
        effect("conflicts with FR-3", "descopes FR-3")
        self.assertEqual(subprocess.run(accept, capture_output=True, text=True).returncode, 0)
        self.assertIn("PROJ-23: descopes FR-3", why()["FR-3"])
        self.assertEqual(subprocess.run(accept, capture_output=True, text=True).returncode, 0)
        w = why()
        self.assertNotIn("FR-3", w)
        self.assertFalse([x for x in w.get("BR-3", []) if "PROJ-21" in x])
        effect("descopes FR-3", "conflicts with FR-3")
        self.assertEqual(why()["FR-3"], ["PROJ-23: conflicts with FR-3"])

    def review(self, st):
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r, json.loads((st / "review.json").read_text(encoding="utf-8"))

    def test_new_text_no_citation_covers_is_reviewed(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["decks"]["deck"] = {"md5": "d1", "changed_slides": [4, 5], "moved_slides": [], "new_slides": [2, 6, 7, 10],
                                  "inserted_slides": [6], "edited": [{"cited": 5, "now": 2}, {"cited": 4, "now": 7}]}
        (self.run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1, widget w-1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, area a-1 | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        base = json.loads((st / "baseline.json").read_text(encoding="utf-8"))
        base["whiteboards"]["board"]["widgets"]["a-1"] = {"sig": "sa", "text": "Audit"}
        (st / "baseline.json").write_text(json.dumps(base), encoding="utf-8")
        flags["whiteboards"]["board"] = {"md5": "b1", "changed": ["w-5", "w-6"], "deleted": [], "added": ["w-7"],
                                         "added_text": {"w-7": "Audit exports too"}, "parents": {"w-6": "a-1", "w-7": "a-1"},
                                         "changed_text": {"w-5": {"old": "Nice to have: PDF", "new": "MUST: PDF"},
                                                          "w-6": {"old": "Log", "new": "Log nothing"}}}
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, review = self.review(st)
        self.assertEqual(review["deck_new_slides"], {"deck": [6, 7, 10]})
        why = {x["req"]: x["why"] for x in review["requirements"]}
        self.assertIn("Slide deck: slide 5 changed", why["BR-3"])
        self.assertIn("Whiteboard: item w-6 in cited area a-1 changed or deleted", why["BR-2"])
        self.assertIn("Whiteboard: item w-7 added to cited area a-1", why["BR-2"])
        self.assertEqual(review["whiteboard_changed_uncited"], {"board": {"w-5": {"old": "Nice to have: PDF", "new": "MUST: PDF"}}})
        self.assertIn("3 new slides no citation covers, 1 new whiteboard items, 1 changed whiteboard items no citation names", r.stdout)

    def test_every_review_worthy_mapping_is_listed(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-50"] = {"key": "PROJ-50", "status": "To Do", "summary": "SSO", "in_export": False, "text_hash": "h50"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        with open(st / "mappings.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["PROJ-50", "h50", "", "new requirement candidate", "users sign in with SSO", ""])
        r, review = self.review(st)
        self.assertEqual(review["mapping_problems_unlinked"], {"PROJ-50": "PROJ-50: new requirement candidate"})
        self.assertNotIn("PROJ-22", review["mapping_problems_unlinked"])
        self.assertIn("1 item mappings to review", r.stdout)
        accept = subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "tracker"],
                                capture_output=True, text=True)
        self.assertEqual(accept.returncode, 0, accept.stderr)
        r, review = self.review(st)
        self.assertEqual(review["mapping_problems_unlinked"], {})

    def test_a_source_never_checked_is_reported(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        del flags["decks"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, review = self.review(st)
        self.assertEqual(review["sources_unchecked"], ["Slide deck (deck deck)"])
        self.assertIn("WARN  Slide deck (deck deck) was never checked against the baseline", r.stdout)
        self.assertIn("1 sources never checked", r.stdout)
        flags["decks"] = {"deck": {"md5": "d1", "changed_slides": [], "moved_slides": [], "new_slides": [],
                                   "checked_at": "2026-10-13T10:00:00", "accepted": True}}
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, review = self.review(st)
        self.assertEqual(review["sources_unchecked"], [])
        self.assertIn("checked deck deck: 2026-10-13T10:00:00 (accepted)", r.stdout)

    def test_every_addend_of_needs_review_reaches_the_total(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["whiteboards"]["board"].update(changed=["w-2", "w-5"], changed_text={"w-5": {"old": "a", "new": "b"}})
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-50"] = {"key": "PROJ-50", "status": "To Do", "summary": "SSO", "in_export": False, "text_hash": "h50"}
        now["PROJ-60"] = {"key": "PROJ-60", "status": "To Do", "summary": "Never mapped", "in_export": False, "text_hash": "h60"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        with open(st / "mappings.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["PROJ-50", "h50", "", "new requirement candidate", "users sign in with SSO", ""])
        (st / "tomap.json").write_text(json.dumps([{"key": "PROJ-60", "text_hash": "h60"}]), encoding="utf-8")
        srcs = self.manifest["sources"] + [{"name": "Deck 2", "evidence_prefixes": ["R9"], "kind": "deck", "id": "deck2"}]
        r, page = self.build(refresh_state=str(st), sources=srcs)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("NEEDS REVIEW: 13 (6 requirements whose source changed, 1 re-worded or re-opened items no requirement "
                      "references, 1 new slides no citation covers, 1 new whiteboard items, 1 changed whiteboard items "
                      "no citation names, 1 item mappings to review, 1 sources never checked, 1 items not mapped)", r.stdout)

    def test_items_waiting_for_a_mapping_are_reviewed(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-22"]["text_hash"] = "h22-new"
        now["PROJ-60"] = {"key": "PROJ-60", "status": "To Do", "summary": "New", "in_export": False, "text_hash": "h60"}
        now["PROJ-61"] = {"key": "PROJ-61", "status": "Cancelled", "summary": "Gone", "in_export": False, "text_hash": "h61"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        (st / "tomap.json").write_text(json.dumps([{"key": k, "text_hash": h} for k, h in
                                                   (("PROJ-22", "h22-new"), ("PROJ-60", "h60"), ("PROJ-61", "h61"),
                                                    ("PROJ-20", "h20"))]), encoding="utf-8")
        r, review = self.review(st)
        self.assertIn("PROJ-22", review["mapping_problems_unlinked"])
        self.assertEqual(review["tracker_unmapped"], {"PROJ-60": "PROJ-60 is not mapped at its current text; map it"})
        self.assertIn("1 item mappings to review, 0 sources never checked, 1 items not mapped", r.stdout)
        now["PROJ-22"]["text_hash"] = "h22"
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        r, review = self.review(st)
        self.assertNotIn("PROJ-22", review["mapping_problems_unlinked"])

    def test_a_tracker_never_pulled_is_reported(self):
        st = self.state()
        (st / "state.json").write_text("{}", encoding="utf-8")
        r, review = self.review(st)
        self.assertIn("tracker (never pulled)", review["sources_unchecked"])
        self.assertIn("WARN  the tracker was never pulled", r.stdout)
        self.assertIn("1 sources never checked", r.stdout)
        (st / "state.json").write_text(json.dumps({"last_pull": {"at": "2026-10-13T09:00:00", "items": 9}}), encoding="utf-8")
        r, review = self.review(st)
        self.assertEqual(review["sources_unchecked"], [])
        self.assertIn("checked tracker: 2026-10-13T09:00:00 (9 items)", r.stdout)

    def test_area_children_moved_out_or_deleted_list_the_area(self):
        (self.run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1, widget w-1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, area a-1 | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        for case, f, msg in (
                ("deleted", {"changed": [], "deleted": ["w-5"], "added": [], "parents": {"w-5": "a-1"}},
                 "Whiteboard: item w-5 in cited area a-1 changed or deleted"),
                ("moved out", {"changed": ["w-5"], "deleted": [], "added": [], "parents": {}, "old_parents": {"w-5": "a-1"},
                               "changed_text": {"w-5": {"old": "x", "new": "x"}}},
                 "Whiteboard: item w-5 in cited area a-1 changed or deleted")):
            with self.subTest(case):
                flags["whiteboards"]["board"] = dict(md5="b1", **f)
                (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
                r, review = self.review(st)
                why = {x["req"]: x["why"] for x in review["requirements"]}
                self.assertIn(msg, why.get("BR-2", []))

    def test_home_forms_and_glued_ids_are_banned(self):
        br = self.run / "03-artifacts/cat/br.csv"
        orig = br.read_text(encoding="utf-8")
        for bad in ("Files land in /c/Users/jsmith/exports", "Files land in /mnt/c/Users/jsmith", "/cygdrive/c/Users/js/x",
                    "Copied to /home/jsmith nightly", "Share smb://fs01/Users/jsmith/x", "Share //fs01/home/js/x",
                    "Stage at C:/Users/js/x", "Stage at file://srv/Users/js/x", "Deploy as deploy_123456789012",
                    "Account acct123456789012", "Ref 1a2b3c4d-5e6f-4a1b-8c9d-123456789012-x"):
            with self.subTest(bad):
                br.write_text(orig.replace("Keep an audit trail", bad, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 1, r.stdout)
        for good in ("See https://example.com/users/42", "Copy to ~/exports", "Widget 1700000000001",
                     "Commit https://git.example.com/c/abcdef123456789012abcdefabcdefabcdefabcd",
                     "Ref {1a2b3c4d-5e6f-4a1b-8c9d-123456789012}"):
            with self.subTest(good):
                br.write_text(orig.replace("Keep an audit trail", good, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        log = self.run / "02-research/R1.md"
        br.write_text(orig, encoding="utf-8")
        lorig = log.read_text(encoding="utf-8")
        for loc in ("/c/Users/Jo Smith/deck.pptx slide 3", "/mnt/c/Users/Jo Smith/deck.pptx slide 3",
                    "smb://fs01/Users/Jo Smith/deck.pptx slide 3"):
            with self.subTest(loc):
                log.write_text(lorig.replace("ACME scope.pptx slide 3 → /tmp/x-staging/slide-003.md", loc, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                self.assertIn("shown without the locator: ['R1-1']", r.stdout)
                self.assertNotIn("Smith", page)

    def test_home_paths_are_found_by_segment_not_by_prefix(self):
        br = self.run / "03-artifacts/cat/br.csv"
        orig = br.read_text(encoding="utf-8")
        for bad in ("Data at /System/Volumes/Data/Users/jsmith/exports", "Mount /host_mnt/Users/jsmith",
                    "Mount /run/desktop/mnt/host/c/Users/jsmith", "Home /var/home/jsmith", "NFS /export/home/jsmith",
                    r"Saved to \Users\jsmith\Downloads", "Open vscode://file/Users/jsmith/notes.md",
                    "Share //fs01/home$/jsmith/x", "Share //fs01/users/jsmith", "Link https://x.example.com/a?path=/Users/js"):
            with self.subTest(bad):
                br.write_text(orig.replace("Keep an audit trail", bad, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("a home path in the", r.stderr)
        for good in ("API /api/v1/users/{id}/orders", "See https://host.example.com/a/home/x", "Users/admins export",
                     "Work from home/office", "Read https://example.com/Users/42", "Copy to ~/exports"):
            with self.subTest(good):
                br.write_text(orig.replace("Keep an audit trail", good, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        br.write_text(orig, encoding="utf-8")
        log = self.run / "02-research/R1.md"
        lorig = log.read_text(encoding="utf-8")
        log.write_text(lorig.replace("ACME scope.pptx slide 3 → /tmp/x-staging/slide-003.md",
                                     "/host_mnt/Users/Jo Smith/deck.pptx slide 3", 1), encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("shown without the locator: ['R1-1']", r.stdout)
        self.assertNotIn("Smith", page)

    def test_id_bans_hold_against_glue_on_both_sides(self):
        br = self.run / "03-artifacts/cat/br.csv"
        orig = br.read_text(encoding="utf-8")
        for bad in ("Log 123456789012_CloudTrail_x.json.gz", "Account x_123456789012", "Account acct1234-5678-9012",
                    "Account 1234-5678-9012x", "Key key_AKIAIOSFODNN7EXAMPLE", "Key AKIAIOSFODNN7EXAMPLE_old",
                    "Key 9ASIAIOSFODNN7EXAMPLE", "Run abcdefabcdefabcdefa123456789012"):
            with self.subTest(bad):
                br.write_text(orig.replace("Keep an audit trail", bad, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 1, r.stdout)
        for good in ("Widget 1700000000001", "Hash abcd123456789012abcdef0123456789",
                     "Code AKIAIOSFODNN7EXAMPLEX"):
            with self.subTest(good):
                br.write_text(orig.replace("Keep an audit trail", good, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_source_kind_with_no_checker_counts_until_re_read(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        del flags["by_hand"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        r, review = self.review(st)
        self.assertIn("Wiki (wiki Wiki, no checker: re-read it by hand)", review["sources_unchecked"])
        self.assertIn("WARN  Wiki (wiki) is not checked by a light refresh", r.stdout)
        self.assertIn("1 sources never checked", r.stdout)
        accept = subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "source",
                                 "--id", "Wiki"], capture_output=True, text=True)
        self.assertEqual(accept.returncode, 0, accept.stdout + accept.stderr)
        r, review = self.review(st)
        self.assertEqual(review["sources_unchecked"], [])
        self.assertIn("checked source Wiki:", r.stdout)

    def test_reopened_and_nested_area_changes_are_reviewed(self):
        (self.run / "02-research/R2.md").write_text(research("R2", EV6, [
            f"| R2-1 | whiteboard | board b1, widget w-1 | {BOARD_URL} | 2026-10-02 | \"Export also covers PROJ-7 scope\" |\n",
            "| R2-2 | whiteboard | board b1, area a-1 | n/a: no deep link | 2026-10-02 | \"Audit log\" |\n"]), encoding="utf-8")
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["reopened_keys"] = ["PROJ-4", "PROJ-30"]
        for case, chain, listed in (("grandchild of the cited area", ["a-2", "a-1"], True),
                                    ("sibling area", ["a-3", "a-9"], False)):
            with self.subTest(case):
                flags["whiteboards"]["board"] = {"md5": "b1", "changed": [], "deleted": ["w-6"], "added": [],
                                                 "parents": {"w-6": chain}}
                (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
                r, review = self.review(st)
                why = {x["req"]: x["why"] for x in review["requirements"]}
                self.assertEqual("Whiteboard: item w-6 in cited area a-1 changed or deleted" in why.get("BR-2", []), listed)
        self.assertIn("PROJ-30", review["unreferenced_text_changed"])
        self.assertTrue(any("PROJ-4 re-opened" in w for ws in why.values() for w in ws), why)

    def test_a_reopened_export_item_is_new_work_on_the_page(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-10"] = {"key": "PROJ-10", "status": "To Do", "summary": "Back again", "in_export": True,
                          "reopened": True, "text_hash": "h10"}
        now["PROJ-11"] = {"key": "PROJ-11", "status": "Done", "summary": "Item 11", "in_export": True,
                          "reopened": True, "text_hash": "h11"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        (st / "tomap.json").write_text(json.dumps([{"key": "PROJ-10", "text_hash": "h10"},
                                                   {"key": "PROJ-11", "text_hash": "h11"}]), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        unref = page.split('<section id="unref">')[1].split("</section>")[0]
        self.assertIn("PROJ-10", unref)
        self.assertNotIn("PROJ-11", unref)
        review = json.loads((st / "review.json").read_text(encoding="utf-8"))
        self.assertEqual(list(review["tracker_unmapped"]), ["PROJ-10"])
        self.assertIn("PROJ-11", json.loads((st / "traced-keys.json").read_text(encoding="utf-8")))

    def test_home_shares_by_segment_and_a_tilde_word(self):
        br = self.run / "03-artifacts/cat/br.csv"
        orig = br.read_text(encoding="utf-8")
        for bad in (r"Reports are saved to \\fs01\users$\jsmith\Reports", r"Scans in \\nas01\homes\jsmith\scans",
                    r"Old share \\fs01\homedirs$\jsmith", "Copy //fs01.corp.example.com/home/jsmith/x",
                    "Notes //wsl.localhost/Ubuntu/home/jsmith/notes.md", "Share smb://fs01/users/jsmith/x",
                    "Served at http://localhost:8888/files/home/jsmith/n.ipynb",
                    "Open file:///c:/users/jsmith/x", r"Profile C:\Users\jsmith\x", "NAS /volume1/homes/jsmith/x"):
            with self.subTest(bad):
                br.write_text(orig.replace("Keep an audit trail", bad, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("a home path in the", r.stderr)
                self.assertIn("BR-2", r.stderr)
                self.assertNotIn("jsmith", r.stderr)
        for good in ("Send the digest ~weekly to managers", "See https://example.com/users/42", "Copy to ~/exports",
                     "API /api/v1/users/{id}/orders",
                     r"Code in C:\src\UsersApi\Controllers\Orders.cs", r"Kept in \\fs01\Departments\Homecare\q3.xlsx",
                     r"Docs in D:\repos\users-service\docs\api.md", r"Policy \\fs01\shares\HomeOffice\policy.docx"):
            with self.subTest(good):
                br.write_text(orig.replace("Keep an audit trail", good, 1), encoding="utf-8")
                r, page = self.build()
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_refusal_names_a_ticket_or_conflict_carrier(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-22"]["summary"] = "Copied from /Users/jsmith/exports"
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("PROJ-22", r.stderr)
        self.assertNotIn("jsmith", r.stderr)
        now["PROJ-22"]["summary"] = "Item PROJ-22"
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        (st / "curated.json").write_text(json.dumps({"conflicts": [
            {"id": "CF-09", "severity": "Low", "topic": "Store", "side_a": "x", "side_b": "kept in /Users/jsmith/x"}]}),
            encoding="utf-8")
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("CF-09", r.stderr)

    def test_a_by_hand_source_is_accepted_only_as_listed_and_is_due_each_cycle(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        del flags["by_hand"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        srcs = self.manifest["sources"] + [{"name": "Spec file", "evidence_prefixes": ["R8"], "kind": "file", "id": "spec"}]
        r, page = self.build(refresh_state=str(st), sources=srcs)
        review = json.loads((st / "review.json").read_text(encoding="utf-8"))
        self.assertEqual(review["reviewed"]["by_hand"], ["Wiki", "spec"])
        self.assertIn("2 sources never checked", r.stdout)
        acc = lambda sid: subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "source",
                                          "--id", sid], capture_output=True, text=True)
        self.assertEqual(acc("wikki").returncode, 1)
        self.assertEqual(acc("Wiki").returncode, 0)
        self.assertEqual(acc("spec").returncode, 0)
        r, page = self.build(refresh_state=str(st), sources=srcs)
        self.assertIn("0 sources never checked", r.stdout)
        stj = json.loads((st / "state.json").read_text(encoding="utf-8"))
        stj["last_pull"]["at"] = json.loads((st / "flags.json").read_text(encoding="utf-8"))["by_hand"]["Wiki"]["checked_at"]
        (st / "state.json").write_text(json.dumps(stj), encoding="utf-8")
        r, page = self.build(refresh_state=str(st), sources=srcs)
        self.assertIn("Wiki (wiki Wiki", " ".join(json.loads((st / "review.json").read_text(encoding="utf-8"))["sources_unchecked"]))
        stj["last_pull"]["at"] = "2999-01-01T00:00:00"
        (st / "state.json").write_text(json.dumps(stj), encoding="utf-8")
        r, page = self.build(refresh_state=str(st), sources=srcs)
        self.assertIn("2 sources never checked", r.stdout)

    def test_the_build_writes_what_accept_and_apply_read(self):
        st = self.state()
        now = json.loads((st / "tracker/now.json").read_text(encoding="utf-8"))
        now["PROJ-30"] = {"key": "PROJ-30", "status": "To Do", "summary": "Back", "in_export": True, "reopened": True,
                          "text_hash": "h30"}
        (st / "tracker/now.json").write_text(json.dumps(now), encoding="utf-8")
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        flags["reopened_keys"] = ["PROJ-30"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        (st / "tomap.json").write_text(json.dumps([{"key": "PROJ-30", "text_hash": "h30", "summary": "Back",
                                                    "description": "Users export orders as PDF every night.", "ac": ""}]),
                                       encoding="utf-8")
        self.assertFalse((st / "review.json").exists() or (st / "requirement-ids.json").exists())
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        ids = json.loads((st / "requirement-ids.json").read_text(encoding="utf-8"))
        self.assertIn("BR-1", ids)
        m = st / "m.csv"
        for req, rc in (("BR-1", 0), ("BR-99", 1)):
            with self.subTest(req):
                write_csv(m, ["key", "text_hash", "req_ids", "effect", "quote", "note"],
                          [["PROJ-30", "h30", req, "upgrades none->partial", "Users export orders as PDF every night", ""]])
                a = subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "apply_mappings.py"), str(st), str(m)],
                                   capture_output=True, text=True)
                self.assertEqual(a.returncode, rc, a.stdout + a.stderr)
        acc = subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "tracker"],
                             capture_output=True, text=True)
        self.assertEqual(acc.returncode, 0, acc.stderr)
        self.assertEqual(json.loads((st / "flags.json").read_text(encoding="utf-8"))["reopened_keys"], [])

    def test_headerless_log_is_read_in_the_v03_order(self):
        log = self.run / "02-research/R4.md"
        log.write_text(log.read_text(encoding="utf-8").replace("| id | source | locator | date | quote |\n", ""), encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('title="Requirements page §2: &quot;Must keep an audit trail&quot;"', self.row(page, "FR-3"))

    def test_traced_keys_are_the_baseline_trace_only(self):
        st = self.state()
        r, page = self.build(refresh_state=str(st))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        traced = json.loads((st / "traced-keys.json").read_text(encoding="utf-8"))
        self.assertNotIn("PROJ-20", traced)
        self.assertIn("PROJ-4", traced)

    def test_duplicate_evidence_prefixes_refused(self):
        srcs = self.manifest["sources"] + [{"name": "Deck 2", "evidence_prefixes": ["R1"], "kind": "deck", "id": "deck2"}]
        r, page = self.build(sources=srcs)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("evidence prefixes must be unique", r.stderr)

    def test_an_unreadable_later_input_is_a_clean_error(self):
        (self.run / "merge/issues.json").write_text("{bad", encoding="utf-8")
        r, page = self.build()
        self.assertEqual(r.returncode, 1)
        self.assertIn("ERROR:", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_a_wide_slide_range_keeps_every_slide(self):
        sys.dont_write_bytecode = True
        sys.path.insert(0, str(SCRIPTS))
        import build_baseline
        self.assertIn(150, build_baseline.slide_numbers("slides 1-300"))

    def test_a_hand_check_needs_the_review_of_the_current_pull(self):
        st = self.state()
        flags = json.loads((st / "flags.json").read_text(encoding="utf-8"))
        del flags["by_hand"]
        (st / "flags.json").write_text(json.dumps(flags), encoding="utf-8")
        self.review(st)
        accept = lambda: subprocess.run([sys.executable, "-I", str(SCRIPTS / "refresh" / "accept.py"), str(st), "source",
                                         "--id", "Wiki"], capture_output=True, text=True)
        self.assertEqual(accept().returncode, 0)
        state = json.loads((st / "state.json").read_text(encoding="utf-8"))
        state["last_pull"]["at"] = "2099-01-01T00:00:00"
        (st / "state.json").write_text(json.dumps(state), encoding="utf-8")
        r = accept()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("pulled after this review", r.stderr)
        self.review(st)
        self.assertEqual(accept().returncode, 0)

    def test_a_malformed_effect_is_reviewed(self):
        st = self.state()
        rows = list(csv.reader((st / "mappings.csv").read_text(encoding="utf-8").splitlines()))
        rows = [r if r[0] != "PROJ-22" else r[:3] + ["no requirement but it exports"] + r[4:] for r in rows]
        write_csv(st / "mappings.csv", rows[0], rows[1:])
        r, review = self.review(st)
        self.assertIn("PROJ-22", review["mapping_problems_unlinked"])


if __name__ == "__main__":
    unittest.main()
