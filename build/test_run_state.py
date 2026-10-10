"""Behaviour tests for scripts/run_state.py and check_artifact.py (budget raise, directory outputs, verify-writes,
partial and final synthesizers, stale dependents, estimate, unfinished research skeleton). Stdlib only."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "skills" / "ba-orchestrator" / "scripts"
RS = SCRIPTS / "run_state.py"
CA = SCRIPTS / "check_artifact.py"


def rs(*args, script=RS):
    return subprocess.run([sys.executable, "-I", str(script), *map(str, args)], capture_output=True, text=True)


class RunStateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.run = Path(self.tmp.name) / "run"
        skill = Path(self.tmp.name) / "skill"  # isolated, so concurrent edits to the real skill cannot flake verify-writes
        skill.mkdir()
        r = rs("init", self.run, "--depth", "light", "--skill-dir", skill)
        self.assertEqual(r.returncode, 0, r.stderr)

    def tearDown(self):
        self.tmp.cleanup()

    def status(self):
        return json.loads((self.run / "status.json").read_text(encoding="utf-8"))

    def budget(self, *extra):
        return rs("budget", self.run, *extra)

    def test_raise_records_event(self):
        r = self.budget("--max-agents", 20, "--max-attempts", 4, "--reason", "outage", "--approved-by", "alice")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("'max_agents': 20", r.stdout)
        st = self.status()
        self.assertEqual((st["budget"]["max_agents"], st["budget"]["max_attempts"]), (20, 4))
        evs = [{k: e[k] for k in ("type", "field", "from", "to", "approved_by", "reason")}
               for e in st["events"] if e.get("type") == "budget_override"]
        self.assertEqual(evs, [
            {"type": "budget_override", "field": "max_agents", "from": 8, "to": 20, "approved_by": "alice", "reason": "outage"},
            {"type": "budget_override", "field": "max_attempts", "from": 2, "to": 4, "approved_by": "alice", "reason": "outage"}])
        self.assertTrue(all("t" in e for e in st["events"]))
        out = rs("show", self.run).stdout
        self.assertIn("BUDGET RAISED", out)
        self.assertIn("max_attempts 2 -> 4", out)
        self.assertIn("'alice'", out)

    def test_refusals(self):
        before = self.status()["budget"]
        cases = [  # (name, args, expected stderr fragment) -- the fragment proves the refusal is budget's own
            ("lower", ["--max-agents", 2, "--reason", "x", "--approved-by", "u"], "can only be raised"),
            ("equal", ["--max-waves", before["max_waves"], "--reason", "x", "--approved-by", "u"], "can only be raised"),
            ("no limit", ["--reason", "x", "--approved-by", "u"], "give at least one"),
            ("no approver", ["--max-agents", 20, "--reason", "x"], "--approved-by"),
            ("no reason", ["--max-agents", 20, "--approved-by", "u"], "--reason"),
            ("empty reason", ["--max-agents", 20, "--reason", " ", "--approved-by", "u"], "must not be empty"),
            ("empty approver", ["--max-agents", 20, "--reason", "x", "--approved-by", ""], "must not be empty"),
        ]
        for name, args, msg in cases:
            with self.subTest(name):
                r = self.budget(*args)
                self.assertEqual(r.returncode, 2)
                self.assertNotIn("invalid choice", r.stderr)
                self.assertIn(msg, r.stderr)
        self.assertEqual(self.status()["budget"], before)

    def test_below_launches_refused(self):
        st = self.status()
        st["launches"] = 30  # a status.json already past its limit, e.g. from an earlier hand edit
        (self.run / "status.json").write_text(json.dumps(st), encoding="utf-8")
        r = self.budget("--max-agents", 20, "--reason", "x", "--approved-by", "u")
        self.assertEqual(r.returncode, 2)
        self.assertIn("launches", r.stderr)

    def test_terminal_refused(self):
        self.assertEqual(rs("terminal", self.run, "cancelled", "--reason", "stop").returncode, 0)
        r = self.budget("--max-agents", 20, "--reason", "x", "--approved-by", "u")
        self.assertEqual(r.returncode, 2)
        self.assertIn("already terminal", r.stderr)

    def test_add_refuses_file_path_and_directory_owns_companions(self):
        for key, role, out in (("E1", "executor", "03-artifacts/m1/artifact.md"), ("S1", "synthesizer", "04-synthesis/synthesis.md")):
            with self.subTest(role):
                r = rs("add", self.run, key, "--role", role, "--output", out, "--wave", 1)
                self.assertEqual(r.returncode, 2)
                self.assertIn("register the", r.stderr)
        self.assertEqual(self.status()["agents"], [])  # refused before registering: the same key can be re-added
        r = rs("add", self.run, "E2", "--role", "executor", "--output", "03-artifacts/m2", "--wave", 1)
        self.assertEqual(r.returncode, 0, r.stderr)
        r = rs("add", self.run, "E3", "--role", "executor", "--output", "03-artifacts/m3--v1.2", "--wave", 1)
        self.assertEqual(r.returncode, 0, r.stderr)  # a dot in a scope is not a file
        r = rs("add", self.run, "R1", "--role", "researcher", "--output", "02-evidence/r1.md", "--wave", 1)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(rs("phase", self.run, "EXECUTE", "--wave", 1).returncode, 0)
        self.assertEqual(rs("snapshot", self.run).returncode, 0)
        d = self.run / "03-artifacts" / "m2"
        d.mkdir(parents=True)
        for name in ("artifact.md", "trace.csv", "flow.mmd"):
            (d / name).write_text("x", encoding="utf-8")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # controls: a companion next to a FILE registration, and a sibling directory sharing the prefix
        f = self.run / "02-evidence"
        f.mkdir(parents=True)
        (f / "r1.md").write_text("x", encoding="utf-8")
        (f / "r1.csv").write_text("x", encoding="utf-8")
        sib = self.run / "03-artifacts" / "m2--teamA"
        sib.mkdir(parents=True)
        (sib / "artifact.md").write_text("x", encoding="utf-8")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5)
        self.assertIn("VIOLATION 02-evidence/r1.csv", r.stdout)
        self.assertIn("VIOLATION 03-artifacts/m2--teamA/artifact.md", r.stdout)
        self.assertNotIn("VIOLATION 02-evidence/r1.md", r.stdout)

    def wave2_after_wave1(self):
        """E1 registered and done in wave 1; E2 registered in wave 2; snapshot taken for wave 2."""
        for key, wave in (("E1", 1), ("E2", 2)):
            self.assertEqual(rs("add", self.run, key, "--role", "executor", "--output", f"03-artifacts/{key}", "--wave", wave).returncode, 0)
        rs("set", self.run, "E1", "running")
        rs("set", self.run, "E1", "done")
        self.assertEqual(rs("phase", self.run, "EXECUTE", "--wave", 2).returncode, 0)
        self.assertEqual(rs("snapshot", self.run).returncode, 0)

    def write(self, rel):
        p = self.run / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("x", encoding="utf-8")

    def test_only_the_logged_snapshot_is_trusted(self):
        self.wave2_after_wave1()
        self.write("03-artifacts/E1/artifact.md")  # a real violation
        fake = {"wave": 2, "events": 0, "run": {"03-artifacts/E1/artifact.md": "x"}, "skill_dir": "/nonexistent", "skill": {}}
        (self.run / ".snapshots" / "999-wave2.json").write_text(json.dumps(fake), encoding="utf-8")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5, r.stdout + r.stderr)  # the newer-looking stray file is never loaded
        self.assertIn("VIOLATION 03-artifacts/E1/artifact.md", r.stdout)
        snap = self.run / ".snapshots" / "000-wave2.json"
        snap.write_text(snap.read_text(encoding="utf-8").replace('"wave": 2', '"wave": 1'), encoding="utf-8")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5)
        self.assertIn("modified after it was taken", r.stderr)
        self.assertEqual(rs("snapshot", self.run).returncode, 0)  # numbering follows the log, not the directory
        self.assertTrue((self.run / ".snapshots" / "001-wave2.json").exists())

    def test_lookalike_of_own_files_is_checked(self):
        self.wave2_after_wave1()
        for rel in (".snapshots-old/x.json", "status.json.bak"):
            self.write(rel)
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5)
        self.assertIn("VIOLATION .snapshots-old/x.json", r.stdout)
        self.assertIn("VIOLATION status.json.bak", r.stdout)

    def test_violation_is_logged_and_survives_owner_relaunch(self):
        self.wave2_after_wave1()
        self.write("03-artifacts/E1/artifact.md")
        self.assertEqual(rs("verify-writes", self.run).returncode, 5)
        rs("set", self.run, "E1", "revise")
        rs("set", self.run, "E1", "running")
        self.assertEqual(rs("verify-writes", self.run).returncode, 0)  # now allowed: E1 is relaunched
        self.assertIn("WRITE VIOLATION", rs("show", self.run).stdout)  # but the earlier finding stays on record
        self.assertIn("03-artifacts/E1/artifact.md", rs("show", self.run).stdout)

    def test_revision_of_earlier_wave_allowed_only_when_relaunched(self):
        self.wave2_after_wave1()
        self.write("03-artifacts/E1/artifact.md")
        r = rs("verify-writes", self.run)  # control: E1 was not running in the window
        self.assertEqual(r.returncode, 5, r.stdout)
        self.assertIn("VIOLATION 03-artifacts/E1/artifact.md", r.stdout)
        rs("set", self.run, "E1", "revise")
        self.assertEqual(rs("set", self.run, "E1", "running").returncode, 0)
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_relaunch_before_snapshot_does_not_count(self):
        self.assertEqual(rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/E1", "--wave", 1).returncode, 0)
        for s in ("running", "done", "revise", "running", "done"):
            rs("set", self.run, "E1", s)
        rs("phase", self.run, "EXECUTE", "--wave", 2)
        rs("snapshot", self.run)
        self.write("03-artifacts/E1/artifact.md")
        self.assertEqual(rs("verify-writes", self.run).returncode, 5)

    def test_orchestrator_paths_listed_not_violations(self):
        self.wave2_after_wave1()
        for rel in ("00-intake/brief.md", "01-plan/plan.md", "06-final/README.md"):
            self.write(rel)
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for rel in ("00-intake/brief.md", "01-plan/plan.md", "06-final/README.md"):
            self.assertIn(f"ORCHESTRATOR WRITE {rel}", r.stdout)
        self.write("01-planx/plan.md")  # control: a prefix lookalike is still a violation
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5)
        self.assertIn("VIOLATION 01-planx/plan.md", r.stdout)

    def test_overlapping_outputs_refused(self):
        self.assertEqual(rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/m").returncode, 0)
        for key, out in (("E2", "03-artifacts/m/sub"), ("E3", "03-artifacts"), ("E4", "03-artifacts/m")):
            with self.subTest(out):
                r = rs("add", self.run, key, "--role", "executor", "--output", out)
                self.assertEqual(r.returncode, 4)
                self.assertIn("overlaps", r.stderr)
        self.assertEqual(rs("add", self.run, "E5", "--role", "executor", "--output", "03-artifacts/m--b").returncode, 0)

    def test_reconcile_needs_executor_artifact(self):
        rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/m")
        rs("set", self.run, "E1", "running")
        rs("set", self.run, "E1", "done")
        d = self.run / "03-artifacts" / "m"
        d.mkdir(parents=True)
        (d / "trace.csv").write_text("x", encoding="utf-8")
        r = rs("reconcile", self.run)
        self.assertEqual(r.returncode, 6, r.stdout)
        self.assertIn("output missing", r.stdout)

    def test_final_synthesizer_contains_done_partials(self):
        for key in ("S1", "S2"):
            self.assertEqual(rs("add", self.run, key, "--role", "synthesizer", "--output", f"04-synthesis/wave-{key[1]}").returncode, 0)
        rs("set", self.run, "S1", "running")
        rs("set", self.run, "S1", "done")
        r = rs("add", self.run, "SF", "--role", "synthesizer", "--output", "04-synthesis")
        self.assertEqual(r.returncode, 4)  # control: S2 is still queued, a live owner inside the directory
        self.assertIn("S2", r.stderr)
        rs("set", self.run, "S2", "running")
        rs("set", self.run, "S2", "done")
        r = rs("add", self.run, "SF", "--role", "synthesizer", "--output", "04-synthesis")
        self.assertEqual(r.returncode, 0, r.stderr)
        rs("set", self.run, "S1", "revise")  # a partial re-opened under the final is live again
        r = rs("add", self.run, "SG", "--role", "executor", "--output", "04-synthesis/wave-1/x")
        self.assertEqual(r.returncode, 4)

    def test_final_synthesizer_may_not_rewrite_a_partial(self):
        rs("add", self.run, "S1", "--role", "synthesizer", "--output", "04-synthesis/wave-1", "--wave", 1)
        for s in ("running", "done"):
            rs("set", self.run, "S1", s)
        rs("phase", self.run, "SYNTHESIZE", "--wave", 2)
        rs("add", self.run, "SF", "--role", "synthesizer", "--output", "04-synthesis", "--wave", 2)
        rs("snapshot", self.run)
        rs("set", self.run, "SF", "running")
        self.write("04-synthesis/synthesis.md")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)  # control: its own file
        self.write("04-synthesis/wave-1/synthesis.md")
        r = rs("verify-writes", self.run)
        self.assertEqual(r.returncode, 5, r.stdout)
        self.assertIn("VIOLATION 04-synthesis/wave-1/synthesis.md", r.stdout)

    def test_output_path_spellings(self):
        for out in ("/abs/03-artifacts/m1", "03-artifacts/zz/../m1", "../outside", "."):
            with self.subTest(out):
                r = rs("add", self.run, "E9", "--role", "executor", "--output", out)
                self.assertEqual(r.returncode, 2, r.stderr)
        self.assertEqual(rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/m1/").returncode, 0)
        for out in ("03-artifacts/m1", "./03-artifacts/m1", "03-artifacts//m1"):
            with self.subTest(out):
                self.assertEqual(rs("add", self.run, "E2", "--role", "executor", "--output", out).returncode, 4)

    def test_baseline_is_read_only(self):
        base = Path(self.tmp.name) / "baseline"
        base.mkdir()
        (base / "catalogue.md").write_text("FR-1", encoding="utf-8")
        run2 = Path(self.tmp.name) / "run2"
        self.assertEqual(rs("init", run2, "--depth", "light", "--skill-dir", Path(self.tmp.name) / "skill",
                            "--baseline", base).returncode, 0)
        self.assertNotIn("baseline", rs("reconcile", run2).stdout)  # control: unchanged
        (base / "catalogue.md").write_text("FR-1\nFR-2 added without change control", encoding="utf-8")
        r = rs("reconcile", run2)
        self.assertEqual(r.returncode, 6)
        self.assertIn("baseline", r.stdout)
        r = rs("terminal", run2, "completed", "--reason", "x")
        self.assertEqual(r.returncode, 2)
        self.assertIn("baseline", r.stderr)

    def test_reconcile_final_synthesizer_needs_own_files(self):
        rs("add", self.run, "S1", "--role", "synthesizer", "--output", "04-synthesis/wave-1")
        for s in ("running", "done"):
            rs("set", self.run, "S1", s)
        rs("add", self.run, "SF", "--role", "synthesizer", "--output", "04-synthesis")
        for s in ("running", "done"):
            rs("set", self.run, "SF", s)
        self.write("04-synthesis/wave-1/synthesis.md")
        r = rs("reconcile", self.run)  # the partial's files are not the final's output
        self.assertEqual(r.returncode, 6, r.stdout)
        self.assertIn("SF [synthesizer done] 04-synthesis: marked done but output missing", r.stdout)
        self.write("04-synthesis/synthesis.md")
        r = rs("reconcile", self.run)
        self.assertNotIn("output missing", r.stdout)

    def test_key_with_whitespace_refused(self):
        for key in ("E 1", "E1\t", " E1"):
            with self.subTest(repr(key)):
                r = rs("add", self.run, key, "--role", "executor", "--output", "03-artifacts/x")
                self.assertEqual(r.returncode, 2)
                self.assertIn("whitespace", r.stderr)
        self.assertEqual(self.status()["agents"], [])

    def cascade(self):
        """E1 done, then C1 (depends on E1) done."""
        self.assertEqual(rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/e1").returncode, 0)
        r = rs("add", self.run, "C1", "--role", "critic", "--output", "05-review/c1.md", "--depends-on", "E1")
        self.assertEqual(r.returncode, 0, r.stderr)
        for key in ("E1", "C1"):
            rs("set", self.run, key, "running")
            rs("set", self.run, key, "done")

    def test_depends_on_unknown_key_refused(self):
        rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/e1")
        r = rs("add", self.run, "C1", "--role", "critic", "--output", "05-review/c1.md", "--depends-on", "E1,E9")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("unrecognized", r.stderr)
        self.assertIn("unknown", r.stderr)
        self.assertIn("E9", r.stderr)
        self.assertEqual([a["key"] for a in self.status()["agents"]], ["E1"])

    def test_revision_makes_dependent_stale_until_rerun(self):
        self.cascade()
        self.assertEqual(rs("stale", self.run).stdout, "")  # control: nothing changed after C1 finished
        for s in ("revise", "running"):
            rs("set", self.run, "E1", s)
        self.assertEqual(rs("stale", self.run).stdout, "")  # not changed until the revision is done
        rs("set", self.run, "E1", "done")
        r = rs("stale", self.run)
        self.assertEqual(r.returncode, 0)
        self.assertIn("C1", r.stdout)
        self.assertIn("E1", r.stdout)
        self.assertIn("STALE C1", rs("show", self.run).stdout)
        r = rs("reconcile", self.run)
        self.assertIn("STALE C1", r.stdout)
        self.assertEqual(r.returncode, 6)
        r = rs("terminal", self.run, "completed", "--reason", "x")
        self.assertEqual(r.returncode, 2)
        self.assertIn("C1", r.stderr)
        for s in ("revise", "running", "done"):
            self.assertEqual(rs("set", self.run, "C1", s).returncode, 0)
        self.assertEqual(rs("stale", self.run).stdout, "")
        self.assertEqual(rs("terminal", self.run, "completed", "--reason", "x").returncode, 0)

    def test_dependent_cannot_run_before_upstream_is_done(self):
        rs("add", self.run, "X1", "--role", "executor", "--output", "03-artifacts/x1")
        rs("add", self.run, "X2", "--role", "executor", "--output", "03-artifacts/x2", "--depends-on", "X1")
        rs("set", self.run, "X1", "running")
        r = rs("set", self.run, "X2", "running")  # the same wave as its upstream
        self.assertEqual(r.returncode, 2)
        self.assertIn("depends on X1 (running)", r.stderr)
        rs("set", self.run, "X1", "done")
        self.assertEqual(rs("set", self.run, "X2", "running").returncode, 0)

    def test_upstream_revised_while_dependent_ran_is_stale_in_either_finish_order(self):
        for first, second in (("X1", "X2"), ("X2", "X1")):
            with self.subTest(f"{first} done first"):
                run = Path(self.tmp.name) / f"order-{first}"
                rs("init", run, "--depth", "light", "--skill-dir", Path(self.tmp.name) / "skill")
                rs("add", run, "X1", "--role", "executor", "--output", "03-artifacts/x1")
                rs("add", run, "X2", "--role", "executor", "--output", "03-artifacts/x2", "--depends-on", "X1")
                for k, s in (("X1", "running"), ("X1", "done"), ("X2", "running"), ("X1", "revise"), ("X1", "running")):
                    rs("set", run, k, s)
                rs("set", run, first, "done")  # X2 read the old X1; whichever finishes first, X2 is stale
                rs("set", run, second, "done")
                self.assertIn("STALE X2", rs("stale", run).stdout)
                self.assertEqual(rs("terminal", run, "completed", "--reason", "x").returncode, 2)

    def test_completed_refused_while_revise_or_failed(self):
        rs("add", self.run, "E1", "--role", "executor", "--output", "03-artifacts/e1")
        for s in ("running", "done", "revise"):
            rs("set", self.run, "E1", s)
        r = rs("terminal", self.run, "completed", "--reason", "x")
        self.assertEqual(r.returncode, 2)
        self.assertIn("revise or failed", r.stderr)
        self.assertEqual(rs("terminal", self.run, "completed_with_defects", "--reason", "E1 listed").returncode, 0)

    def test_failed_relaunch_ending_done_makes_dependent_stale(self):
        self.cascade()
        rs("set", self.run, "E1", "revise")
        for s in ("running", "failed", "running", "done"):
            rs("set", self.run, "E1", s)
        self.assertIn("C1", rs("stale", self.run).stdout)

    def test_stale_accepted_with_note(self):
        self.cascade()
        for s in ("revise", "running", "done"):
            rs("set", self.run, "E1", s)
        r = rs("set", self.run, "C1", "done")  # control: a bare done -> done stays illegal
        self.assertEqual(r.returncode, 2)
        r = rs("set", self.run, "C1", "done", "--note", "accepted stale: ")
        self.assertEqual(r.returncode, 2)  # an empty reason is no acceptance
        r = rs("set", self.run, "C1", "done", "--note", "accepted stale: change was a typo fix")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(rs("stale", self.run).stdout, "")
        self.assertTrue(any("accepted stale: change was a typo fix" in e["msg"] for e in self.status()["events"]))
        self.assertIn("STALE ACCEPTED", rs("show", self.run).stdout)
        self.assertIn("change was a typo fix", rs("show", self.run).stdout)
        self.assertEqual(rs("set", self.run, "C1", "done", "--note", "accepted stale: again").returncode, 2)

    def test_completed_with_defects_allowed_while_stale(self):
        self.cascade()
        for s in ("revise", "running", "done"):
            rs("set", self.run, "E1", s)
        r = rs("terminal", self.run, "completed_with_defects", "--reason", "C1 stale, listed")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_estimate(self):
        r = rs("estimate", "--researchers", 19, "--executors", 11, "--critics", 11)
        self.assertEqual(r.returncode, 0, r.stderr)
        # base 19+11+11+1=42; revisions 11*0.7=7.7; relaunches 49.7*0.1=4.97; total ceil(54.67)=55
        for frag in ("base launches: 42", "expected revisions: 7.7", "expected relaunches: 5.0", "total: 55",
                     "none"):
            self.assertIn(frag, r.stdout)
        r = rs("estimate", "--researchers", 2, "--executors", 10, "--critics", 0, "--synthesizers", 0,
               "--revise-rate", 0.7, "--failure-rate", 0)
        self.assertIn("total: 19", r.stdout)  # 12 + 10 x 0.7, no relaunches
        self.assertIn("fits: standard", r.stdout)
        r = rs("estimate", "--researchers", 2, "--executors", 2, "--critics", 2, "--synthesizers", 0,
               "--revise-rate", 0, "--failure-rate", 0)
        self.assertIn("fits: light", r.stdout)
        self.assertEqual(rs("estimate", "--researchers", -1, "--executors", 1, "--critics", 1).returncode, 2)

    def test_unfinished_research_skeleton_fails(self):
        log = Path(self.tmp.name) / "R1.md"
        body = ("# R1\n\nSources searched: wiki\n\n## Findings by research question\n### RQ1\n{rq1}\n"
                "### RQ2\nGAP: nothing in wiki\n\n## Evidence\n| id | source | locator | date | quote |\n|---|---|---|---|---|\n"
                "| R1-1 | wiki | page 1 | 2026 | \"text\" |\n")
        log.write_text(body.format(rq1="GAP: not yet searched"), encoding="utf-8")
        r = rs("research", log, script=CA)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("not yet searched", r.stdout)
        log.write_text(body.format(rq1="Found it [E:R1-1]."), encoding="utf-8")  # control: the finished log passes
        r = rs("research", log, script=CA)
        self.assertEqual(r.returncode, 0, r.stdout)


if __name__ == "__main__":
    unittest.main()
