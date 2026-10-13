"""Behaviour tests for scripts/check_artifact.py: Summary length band, FORM-ONLY errors, research markers and the
header-driven Evidence table (url column, legacy header). Stdlib only."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

CA = Path(__file__).resolve().parent.parent / "skills" / "ba-orchestrator" / "scripts" / "check_artifact.py"
SECTIONS = ["Purpose and decision supported", "Procedure log", "Output", "Assumptions", "Open questions", "Self-check"]


def artifact(words, drop=None):
    fm = "---\nmethod: m\nscope: s\nsource_variant: v\ninputs: i\nstatus: done\n---\n"
    body = "## Summary\n" + " ".join(["w"] * words) + " [E:R1-1]\n"
    body += "".join(f"## {s}\nx\n" for s in SECTIONS if s != drop)
    return fm + body


class CheckArtifactTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        run = Path(self.tmp.name)
        (run / "02-research").mkdir()
        (run / "02-research" / "R1.md").write_text("## Evidence\n| id | s |\n|---|---|\n| R1-1 | x |\n", encoding="utf-8")
        self.art = run / "03-artifacts" / "m"
        self.art.mkdir(parents=True)
        self.run = run

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, text):
        (self.art / "artifact.md").write_text(text, encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(CA), "artifact", str(self.art), "--run-dir", str(self.run)],
                              capture_output=True, text=True)

    def test_summary_band(self):
        for words, code, frag in ((299, 0, "warnings=0"), (329, 0, "WARN"), (359, 0, "warnings=1"), (360, 1, "ERROR")):
            with self.subTest(words + 1):
                r = self.check(artifact(words))
                self.assertEqual(r.returncode, code, r.stdout)
                self.assertIn(frag, r.stdout)
        r = self.check(artifact(360))
        self.assertIn("FORM-ONLY", r.stdout)
        self.assertIn("FAIL FORM-ONLY", r.stdout)

    def test_missing_heading_is_form_only(self):
        r = self.check(artifact(10, drop="Assumptions"))
        self.assertEqual(r.returncode, 1)
        self.assertIn("ERROR FORM-ONLY", r.stdout)
        self.assertIn("FAIL FORM-ONLY", r.stdout)

    def test_evidence_error_is_not_form_only(self):
        r = self.check(artifact(10, drop="Assumptions").replace("[E:R1-1]", "[E:R9-9]"))
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("FAIL FORM-ONLY", r.stdout)
        self.assertNotIn("FORM-ONLY [E:]", r.stdout)
        self.assertIn("FORM-ONLY section missing", r.stdout)

    def test_missing_or_empty_summary_or_output_is_content(self):
        empty_output = artifact(10).replace("## Output\nx\n", "## Output\n\n")
        for name, text in (("no Output", artifact(10, drop="Output")), ("empty Output", empty_output),
                           ("no Summary", artifact(10).replace("## Summary", "## Notes"))):
            with self.subTest(name):
                r = self.check(text)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("did not finish", r.stdout)
                self.assertNotIn("FAIL FORM-ONLY", r.stdout)

    def research(self, text):
        log = self.run / "02-research" / "R2.md"
        log.write_text(text, encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(CA), "research", str(log)], capture_output=True, text=True)

    def test_research_unanswered_markers_fail_in_any_spelling(self):
        body = ("Sources searched: wiki\n\n## Findings by research question\n### RQ1\n{m}\n\n## Evidence\n"
                "| id | source | locator | url | date | quote |\n|---|---|---|---|---|---|\n")
        for m in ("GAP: not searched — turn cap", "GAP: Not yet searched", "[GAP: needs staging — deck.pptx]",
                  "gap:  not  searched", "[GAP] not yet searched — slides 51-120", "GAP - needs staging: board.json",
                  "Sources unavailable: deck.pptx — binary, cannot read — needs staging"):
            with self.subTest(m):
                r = self.research(body.format(m=m))
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        r = self.research(body.format(m="GAP: searched the wiki, nothing found"))
        self.assertEqual(r.returncode, 0, r.stdout)
        quoted = body.format(m="Found [E:R2-1].") + ("| R2-1 | wiki | p1 | https://wiki.example.com/p/1 | 2026 | "
                                                      "\"the deck needs staging; GAP: not yet searched\" |\n")
        r = self.research(quoted)
        self.assertEqual(r.returncode, 0, r.stdout)
        r = self.research(quoted.replace("## Evidence", "## Sources unavailable\n[GAP: needs staging — a.pdf]\n\n## Evidence"))
        self.assertIn("unanswered marker", r.stdout)
        for tail in ("\nImage cap reached; unread items:\n- [GAP: not yet searched — deck.pptx slides 51-120]\n",
                     "\n### Sources unavailable\n- [GAP: needs staging — board.json]\n"):
            with self.subTest(tail):
                r = self.research(quoted + tail)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        for m in ("GAP:     not yet searched", "**[GAP]:** not yet searched"):
            with self.subTest(m):
                self.assertEqual(self.research(body.format(m=m)).returncode, 1)
        for row in ("| R2-1 | deck.pptx | slides 51-120 | n/a: binary | GAP: needs staging | \"render to PNG\" |",
                    "| R2-1 | deck.pptx (needs staging) | slide 3 | n/a: binary | 2026 | \"Y\" |",
                    "| R2-1 | deck.pptx | slide 3 | n/a: GAP: not yet searched | 2026 | \"Y\" |"):
            with self.subTest(row):
                r = self.research(body.format(m="Found [E:R2-1].") + row + "\n")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        r = self.research(body.format(m="x").replace("## Evidence", "## Sources"))
        self.assertIn("FAIL research", r.stdout)
        self.assertNotIn("FORM-ONLY", r.stdout)

    EV = ("Sources searched: wiki\n\n## Findings by research question\n### RQ1\nFound [E:R2-1].\n\n## Evidence\n"
          "| id | source | locator | url | date | quote |\n|---|---|---|---|---|---|\n")

    def row(self, url, locator="p1", quote="\"text\""):
        return self.research(self.EV + f"| R2-1 | wiki | {locator} | {url} | 2026 | {quote} |\n")

    def test_research_url_cell(self):
        for url in ("https://wiki.example.com/pages/123#Scope", "http://tracker.example.com/browse/PROJ-123",
                    "n/a: no addressable url", "N/A: whiteboard tool gives no deep link",
                    "/tmp/run-staging/deck/slide-003.md", "staging/deck/slide-003.md", "~/staging/board/widgets.md",
                    r"C:\run-staging\deck\slide-003.md", "file:///tmp/a.md", "./staged/notes.txt",
                    "https://git.example.com/acme/app/compare/v1.0...v2.0", "https://wiki.example.com/display/TODO/Home",
                    "https://tracker.example.com/issues/?filter=none", "https://tracker.example.com/q?status=none#x",
                    "https://api.example.com/v1/null.html", "https://wiki.example.com/page/TODO", "http://localhost:8080/a",
                    "http://192.168.1.10/source/42", "deck.pptx"):
            with self.subTest(url):
                r = self.row(url)
                self.assertEqual(r.returncode, 0, r.stdout)
                self.assertNotIn("url", r.stdout.split("OK")[0])
        for url in ("", "n/a", "n/a:", "N/A -", "slide 3", "TBD/unknown", "and/or", "ftp://files.example.com/a.pdf",
                    "http://", "see wiki", "https://...", "https://wiki.example.com/...", "http://TBD", "https://TBD/x",
                    "https://wiki.example.com/pages/<id>", "https://wiki.example.com/pages/{id}", "TBD/", "n/a/", "/none",
                    "//", "/", "C:", "https://localhost.", "https://x", "staging/none/a.md", "https://wiki.example.com/p…",
                    "https://wiki.example.com/.../page", "https://none.example.com/x", "n/a: <reason>", "n/a: TODO", "n/a: ...",
                    "v1.0", "http://999.1.1.1.1/a"):
            with self.subTest(url):
                r = self.row(url)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("is not an http(s) URL", r.stdout)

    def status(self, release):
        sv = {"skill_tree_sha": "x"} if release is None else {"skill_tree_sha": "x", "release": release}
        (self.run / "status.json").write_text(json.dumps({"skill_version": sv}), encoding="utf-8")

    def test_research_legacy_header_only_for_an_older_run(self):
        legacy = self.EV.replace("| url ", "").replace("|---|---|---|---|---|---|", "|---|---|---|---|---|")
        row = "| R2-1 | wiki | p1 | 2026 | \"text\" |\n"
        r = self.research(legacy + row)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no url column", r.stdout)
        self.status("0.4.0")
        r = self.research(legacy + row)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no url column", r.stdout)
        for rel in (None, "0.3.0"):
            with self.subTest(rel):
                self.status(rel)
                r = self.research(legacy + row)
                self.assertEqual(r.returncode, 0, r.stdout)
                self.assertIn("WARN  legacy evidence table", r.stdout)
        r = self.research(legacy + "| R2-1 | wiki | p1 | 2026 |  |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("needs 5 columns incl. quote", r.stdout)
        r = self.research(legacy + row + "| R2-2 | wiki | p2 | https://x.example.com/2 | 2026 | \"t\" |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("looks like a v0.4 row", r.stdout)
        for name, body in (("pipe in a quote", legacy + "| R2-1 | wiki | p1 | 2026 | \"a | b\" |\n"),
                           ("no header", legacy.replace("| id | source | locator | date | quote |\n", "") + row),
                           ("other header", legacy.replace("| locator |", "| where |") + row)):
            with self.subTest(name):
                r = self.research(body)
                self.assertEqual(r.returncode, 0, r.stdout)
        r = self.research(legacy + row + "| R2-2 | wiki | p2 | https://x.example.com/2 | 2026 | \"GAP: not yet searched x\" |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertNotIn("unanswered marker", r.stdout)
        r = self.research(legacy + "| R2-1 | wiki | p1 | 2026 | \"a\" | needs staging |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("unanswered marker", r.stdout)
        for head in ("link", "web url", "permalink", "uri", "href", "address"):
            with self.subTest(head):
                renamed = self.EV.replace("| url |", f"| {head} |")
                r = self.research(renamed + "| R2-1 | wiki | p1 | none | 2026 | \"text\" |\n")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("url column under another name", r.stdout)
        r = self.research(self.EV.replace("| url |", "| URL (web) |") + "| R2-1 | wiki | p1 | none | 2026 | \"t\" |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("is not an http(s) URL", r.stdout)
        r = self.row("https://wiki.example.com/p/1")
        self.assertNotIn("legacy", r.stdout)

    def test_research_header_missing_column_or_header(self):
        r = self.research(self.EV.replace("| date ", "").replace("|---|---|---|---|---|---|", "|---|---|---|---|---|")
                          + "| R2-1 | wiki | p1 | https://x.example.com/1 | \"text\" |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("lacks column(s) ['date']", r.stdout)
        no_head = self.EV.replace("| id | source | locator | url | date | quote |\n", "")
        r = self.research(no_head + "| R2-1 | wiki | p1 | https://x.example.com/1 | 2026 | \"text\" |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no header row", r.stdout)

    def test_research_marker_scan_follows_the_header(self):
        r = self.row("https://x.example.com/1", quote="\"slides still need staging\"")
        self.assertEqual(r.returncode, 0, r.stdout)
        r = self.row("https://x.example.com/1", quote="\"a | b, GAP: not yet searched\"")
        self.assertEqual(r.returncode, 0, r.stdout)
        for url, loc in (("n/a: needs staging", "p1"), ("https://x.example.com/1", "slide 3, needs staging")):
            with self.subTest(url=url, locator=loc):
                r = self.row(url, locator=loc)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        moved = self.EV.replace("| id | source | locator | url | date | quote |", "| id | source | locator | quote | date | url |")
        r = self.research(moved + "| R2-1 | wiki | p1 | \"needs staging\" | 2026 | https://x.example.com/1 |\n")
        self.assertEqual(r.returncode, 0, r.stdout)
        r = self.research(moved + "| R2-1 | wiki | p1 | \"text\" | 2026 | n/a: needs staging |\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("unanswered marker", r.stdout)

    def test_evidence_ids_by_header(self):
        (self.run / "02-research" / "R1.md").write_text(
            "## Evidence\n| source | id | locator | url | date | quote |\n|---|---|---|---|---|---|\n"
            "| wiki | R1-1 | p | n/a: x | 2026 | \"q\" |\n", encoding="utf-8")
        self.assertEqual(self.check(artifact(10)).returncode, 0)

    def test_review_without_defects_is_not_form_only(self):
        rv = self.run / "c.md"
        rv.write_text("Verdict: PASS\n\n## Notes\nx\n", encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(CA), "review", str(rv)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("FORM-ONLY", r.stdout)


if __name__ == "__main__":
    unittest.main()
