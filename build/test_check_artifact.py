"""Behaviour tests for scripts/check_artifact.py: Summary length band and FORM-ONLY errors. Stdlib only."""
import subprocess, sys, tempfile, unittest
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
        # the evidence label adds one word to the Summary
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
        r = self.check(artifact(10, drop="Assumptions").replace("[E:R1-1]", "[E:R9-9]"))  # control
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
                "| id | source | locator | date | quote |\n|---|---|---|---|---|\n")
        for m in ("GAP: not searched — turn cap", "GAP: Not yet searched", "[GAP: needs staging — deck.pptx]",
                  "gap:  not  searched", "[GAP] not yet searched — slides 51-120", "GAP - needs staging: board.json",
                  "Sources unavailable: deck.pptx — binary, cannot read — needs staging"):
            with self.subTest(m):
                r = self.research(body.format(m=m))
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        r = self.research(body.format(m="GAP: searched the wiki, nothing found"))  # control
        self.assertEqual(r.returncode, 0, r.stdout)
        quoted = body.format(m="Found [E:R2-1].") + ("| R2-1 | wiki | p1 | 2026 | \"the deck needs staging; "
                                                      "GAP: not yet searched\" |\n")
        r = self.research(quoted)  # source text quoted verbatim in Evidence is not a marker
        self.assertEqual(r.returncode, 0, r.stdout)
        r = self.research(quoted.replace("## Evidence", "## Sources unavailable\n[GAP: needs staging — a.pdf]\n\n## Evidence"))
        self.assertIn("unanswered marker", r.stdout)  # control: the same file with a real marker outside Evidence
        for tail in ("\nImage cap reached; unread items:\n- [GAP: not yet searched — deck.pptx slides 51-120]\n",
                     "\n### Sources unavailable\n- [GAP: needs staging — board.json]\n"):
            with self.subTest(tail):  # an unread list after the table is inside ## Evidence but not a table row
                r = self.research(quoted + tail)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("unanswered marker", r.stdout)
        for m in ("GAP:     not yet searched", "**[GAP]:** not yet searched"):
            with self.subTest(m):
                self.assertEqual(self.research(body.format(m=m)).returncode, 1)
        for row in ("| R7-98 | deck.pptx | slides 51-120 | GAP | needs staging: render to PNG |",
                    "| R7-99 | deck.pptx | slides 51-120 | 2026 | GAP: not yet searched (image cap) |",
                    "| R5-2 | deck.pptx (needs staging) | slide 3 | 2026 | \"Y\" |"):
            with self.subTest(row):  # a marker in any cell of an Evidence row other than the quote counts
                r = self.research(body.format(m="Found [E:R2-1].") + row + "\n")
                self.assertEqual(r.returncode, 1, r.stdout)
        r = self.research(body.format(m="x").replace("## Evidence", "## Sources"))
        self.assertIn("FAIL research", r.stdout)  # a research or review section is content, never form-only
        self.assertNotIn("FORM-ONLY", r.stdout)

    def test_review_without_defects_is_not_form_only(self):
        rv = self.run / "c.md"
        rv.write_text("Verdict: PASS\n\n## Notes\nx\n", encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(CA), "review", str(rv)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("FORM-ONLY", r.stdout)


if __name__ == "__main__":
    unittest.main()
