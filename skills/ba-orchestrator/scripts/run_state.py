#!/usr/bin/env python3
"""Deterministic run state for ba-orchestrator: state machine, budgets, resume, write-ownership checks.

status.json in RUN_DIR is the single source of truth for a run. The orchestrator changes it ONLY
through this script, so transitions, budgets and duplicate checks are enforced outside the model.

Commands (all take RUN_DIR first):
  init RUN_DIR --depth light|standard|deep [--max-agents N] [--max-waves N] [--skill-dir DIR] [--baseline DIR]
                                                 --baseline: a read-only earlier run; its tree hash is recorded,
                                                 reconcile reports a change and `terminal completed` refuses one
  phase RUN_DIR PHASE [--wave N]                 move the run to a phase (see PHASES)
  add RUN_DIR KEY --role ROLE --output REL [--method ID] [--scope S] [--wave N] [--depends-on KEY[,KEY...]]
                                                 REL may be a directory: the agent then owns every file
                                                 under it. Executors and the synthesizer MUST register a
                                                 directory (artifact plus companion .csv/.mmd files). A
                                                 final synthesizer's directory may contain DONE partial ones.
                                                 REL is relative to RUN_DIR; absolute paths and `..` are refused
  set RUN_DIR KEY STATE [--task-id ID] [--note TEXT]
                                                 `running` is refused while a --depends-on upstream is not done
                                                 `set KEY done --note "accepted stale: <reason>"` on a done,
                                                 stale agent records an explicit acceptance and clears it
  stale RUN_DIR                                  agents whose --depends-on upstream reached done after they
                                                 were last set running; re-run them or accept (see set)
  terminal RUN_DIR STATE --reason TEXT           end the run (see TERMINAL); `completed` is refused while
                                                 any agent is stale, revise or failed, or the baseline changed
  budget RUN_DIR [--max-agents N] [--max-waves N] [--max-revisions N] [--max-attempts N]
         --reason TEXT --approved-by TEXT
                                                 RAISE limits; only with explicit user approval
  snapshot RUN_DIR [--skill-dir DIR]             hash files before a wave; the snapshot's hash is logged
  verify-writes RUN_DIR                          after a wave: any change outside the wave's outputs?
                                                 a changed file belongs to the longest registered output
                                                 containing it; allowed: owners in this wave or set running
                                                 since the snapshot (revisions); 00-intake/, 01-plan/,
                                                 06-final/ are listed as orchestrator writes. Violations
                                                 are logged in status.json and printed by `show`
  reconcile RUN_DIR                              resume aid: compare status.json with files on disk
  show RUN_DIR
  estimate --researchers N --executors N --critics N [--synthesizers N] [--revise-rate R] [--failure-rate F]
                                                 expected launches and the depth whose budget fits; no run dir

Exit codes: 0 ok, 2 usage/state error, 3 budget exhausted, 4 duplicate assignment, 5 write violation,
6 reconcile found inconsistencies.
"""
import argparse, hashlib, json, math, posixpath, re, sys, time
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

PHASES = ["INTAKE", "PLAN", "AWAIT_PLAN_APPROVAL", "RESEARCH", "EXECUTE", "AWAIT_GATE",
          "SYNTHESIZE", "REVIEW", "PACKAGE"]
TERMINAL = ["completed", "completed_with_defects", "needs_user_input", "insufficient_evidence",
            "dependency_failed", "budget_exhausted", "cancelled", "policy_denied"]
ROLES = ["researcher", "executor", "synthesizer", "critic"]
AGENT_STATES = ["queued", "running", "done", "revise", "failed", "cancelled"]
TRANSITIONS = {
    "queued": {"running", "cancelled"},
    "running": {"done", "failed", "cancelled"},
    "done": {"revise"},
    "revise": {"running", "cancelled"},
    "failed": {"running", "cancelled"},
    "cancelled": set(),
}
DEPTH_BUDGET = {"light": (8, 4), "standard": (25, 6), "deep": (50, 8)}
MAX_REVISIONS = 2
MAX_ATTEMPTS = 2
ACCEPT_STALE = "accepted stale:"
REVISE_RATE, FAILURE_RATE = 0.7, 0.1  # defaults for `estimate`, observed in a deep field run
FILE_SUFFIXES = (".md", ".csv", ".mmd", ".json", ".txt", ".html")
RUN_SKIP = ("status.json", "status.json.tmp", ".snapshots/")  # run_state.py's own files
ORCHESTRATOR_PATHS = ("00-intake/", "01-plan/", "06-final/")  # run-protocol §1: orchestrator only


def die(code, msg):
    print(msg, file=sys.stderr)
    sys.exit(code)


def load(run):
    p = Path(run) / "status.json"
    if not p.exists():
        die(2, f"no status.json in {run}; run `init` first")
    return json.loads(p.read_text(encoding="utf-8"))


def save(run, st, event=None):
    if event:
        st["events"].append({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "msg": event})
    p = Path(run) / "status.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(p)


def skipped(rel, skip):
    """skip entries are exact paths, or directory prefixes ending in '/'."""
    return "__pycache__" in rel or any(rel == s or (s.endswith("/") and rel.startswith(s)) for s in skip)


def tree_hash(root, skip=()):
    h = hashlib.sha256()
    for rel, digest in file_hashes(root, skip).items():
        h.update(rel.encode())
        h.update(digest.encode())
    return h.hexdigest()[:16]


def file_hashes(root, skip=()):
    out = {}
    root = Path(root)
    for f in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = f.relative_to(root).as_posix()
        if not skipped(rel, skip):
            out[rel] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


def agent(st, key):
    for a in st["agents"]:
        if a["key"] == key:
            return a
    die(2, f"unknown agent key {key}")


def stale_agents(st):
    """(agent, upstream key, when upstream changed): the upstream reached done after the agent was last set
    running (so it may have read the old upstream), and no acceptance was recorded since."""
    changed, read_at = {}, {}
    for i, e in enumerate(st["events"]):
        w = e["msg"].split()
        if len(w) >= 3 and w[0] == "set" and w[2] == "running":
            read_at[w[1]] = i
        elif len(w) >= 3 and w[0] == "set" and w[2] == "done":
            if e.get("type") == "stale_accepted":  # an acceptance changes no content downstream
                read_at[w[1]] = i
            else:
                changed[w[1]] = (i, e["t"])
    return [(x, u, changed[u][1]) for x in st["agents"] for u in x.get("depends_on", [])
            if x["key"] in read_at and u in changed and changed[u][0] > read_at[x["key"]]]


def stale_lines(st):
    return [f"STALE {x['key']}: upstream {u} changed (done again) at {t}; re-run {x['key']} or "
            f'`set {x["key"]} done --note "{ACCEPT_STALE} <reason>"`' for x, u, t in stale_agents(st)]


def ensure_live(st):
    if st.get("terminal"):
        die(2, f"run already terminal: {st['terminal']['state']}")


def cmd_init(a):
    run = Path(a.run)
    run.mkdir(parents=True, exist_ok=True)
    if (run / "status.json").exists():
        die(2, "status.json exists; use `reconcile` to resume this run")
    max_agents, max_waves = DEPTH_BUDGET[a.depth]
    skill = Path(a.skill_dir) if a.skill_dir else Path(__file__).resolve().parent.parent
    idx = skill / "references" / "methods-index.json"
    baseline = None
    if a.baseline:
        if not Path(a.baseline).is_dir():
            die(2, f"--baseline {a.baseline} is not a directory")
        baseline = {"dir": str(Path(a.baseline).resolve()), "tree_sha": tree_hash(a.baseline)}
    st = {
        "run_id": run.name, "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "depth": a.depth,
        "skill_version": {
            "skill_dir": str(skill),
            "skill_tree_sha": tree_hash(skill),
            "methods_index_sha": hashlib.sha256(idx.read_bytes()).hexdigest()[:16] if idx.exists() else None,
        },
        "budget": {"max_agents": a.max_agents or max_agents, "max_waves": a.max_waves or max_waves,
                   "max_revisions": MAX_REVISIONS, "max_attempts": MAX_ATTEMPTS},
        "phase": "INTAKE", "wave": 0, "terminal": None, "agents": [], "launches": 0, "events": [],
        "baseline": baseline,
    }
    save(run, st, "init")
    print(f"initialised {run / 'status.json'}  budget={st['budget']}  version={st['skill_version']['skill_tree_sha']}")


def cmd_phase(a):
    st = load(a.run)
    ensure_live(st)
    if a.phase not in PHASES:
        die(2, f"phase must be one of {PHASES}")
    if a.wave is not None:
        if a.wave > st["budget"]["max_waves"]:
            die(3, f"budget_exhausted: wave {a.wave} > max_waves {st['budget']['max_waves']}")
        st["wave"] = a.wave
    st["phase"] = a.phase
    save(st=st, run=a.run, event=f"phase {a.phase} wave {st['wave']}")
    print(f"phase={a.phase} wave={st['wave']}")


def cmd_add(a):
    st = load(a.run)
    ensure_live(st)
    if a.role not in ROLES:
        die(2, f"role must be one of {ROLES}")
    if not a.key or any(c.isspace() for c in a.key):
        die(2, f"agent key {a.key!r} must be non-empty and contain no whitespace (events are split on spaces)")
    if any(x["key"] == a.key for x in st["agents"]):
        die(4, f"duplicate key {a.key}")
    deps = [k.strip() for k in (a.depends_on or "").split(",") if k.strip()]
    unknown = [k for k in deps if k not in {x["key"] for x in st["agents"]}]
    if unknown:
        die(2, f"--depends-on: unknown agent key(s) {unknown}; register them first")
    out = posixpath.normpath(Path(a.output).as_posix())
    if posixpath.isabs(out) or out == "." or ".." in out.split("/") or ".." in Path(a.output).as_posix().split("/"):
        die(2, f"--output {a.output!r} must be a path relative to RUN_DIR without '..'")
    for x in st["agents"]:
        o = x["output"]
        if x["state"] in ("cancelled", "failed") or not (o == out or out.startswith(o + "/") or o.startswith(out + "/")):
            continue
        if x["state"] == "done" and x["role"] == a.role == "synthesizer" and o.startswith(out + "/"):
            continue  # the final synthesizer's directory holds the finished partial syntheses (wave-<n>/)
        die(4, f"duplicate assignment: {out} overlaps {o} owned by {x['key']} ({x['state']})")
    if st["launches"] >= st["budget"]["max_agents"]:
        die(3, f"budget_exhausted: {st['launches']} launches >= max_agents {st['budget']['max_agents']}")
    if a.role in ("executor", "synthesizer") and out.lower().endswith(FILE_SUFFIXES):
        die(2, f"{out} is a file; register the {a.role}'s directory so its companion files are covered: "
               f"--output {Path(out).parent.as_posix()} (nothing was registered; re-run add with the same key)")
    st["agents"].append({"key": a.key, "role": a.role, "method": a.method, "scope": a.scope,
                         "wave": a.wave if a.wave is not None else st["wave"], "output": out,
                         "state": "queued", "attempts": 0, "revisions": 0, "task_id": None, "notes": [],
                         "depends_on": deps})
    save(a.run, st, f"add {a.key} {a.role} -> {out}")
    print(f"added {a.key} ({a.role}) -> {out}")


def cmd_set(a):
    st = load(a.run)
    ensure_live(st)
    if a.state not in AGENT_STATES:
        die(2, f"state must be one of {AGENT_STATES}")
    x = agent(st, a.key)
    if a.state == x["state"] == "done" and (a.note or "").startswith(ACCEPT_STALE):
        if not a.note[len(ACCEPT_STALE):].strip():
            die(2, f'give a reason: --note "{ACCEPT_STALE} <reason>"')
        ups = [u for y, u, _ in stale_agents(st) if y["key"] == x["key"]]
        if not ups:
            die(2, f"{x['key']} is not stale; nothing to accept")
        x["notes"].append(a.note)
        st["events"].append({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "msg": f"set {x['key']} done ({a.note})",
                             "type": "stale_accepted", "upstream": ups})
        save(a.run, st)
        print(f"{x['key']}: stale accepted (upstream {', '.join(ups)})")
        return
    if a.state not in TRANSITIONS[x["state"]]:
        die(2, f"illegal transition {x['key']}: {x['state']} -> {a.state}")
    if a.state == "running":
        waiting = [f"{u} ({agent(st, u)['state']})" for u in x.get("depends_on", []) if agent(st, u)["state"] != "done"]
        if waiting:
            die(2, f"{x['key']} depends on {', '.join(waiting)}: run it in a later wave, after the upstream is done")
        if x["state"] == "revise":
            if x["revisions"] >= st["budget"]["max_revisions"]:
                die(3, f"budget_exhausted: {x['key']} already revised {x['revisions']} times")
            x["revisions"] += 1
        elif x["state"] == "failed" and x["attempts"] >= st["budget"]["max_attempts"]:
            die(3, f"budget_exhausted: {x['key']} already attempted {x['attempts']} times")
        if x["state"] in ("queued", "failed", "revise"):
            if st["launches"] >= st["budget"]["max_agents"]:
                die(3, f"budget_exhausted: {st['launches']} launches >= max_agents {st['budget']['max_agents']}")
            st["launches"] += 1
            x["attempts"] += 1 if x["state"] != "revise" else 0
    x["state"] = a.state
    if a.task_id:
        x["task_id"] = a.task_id
    if a.note:
        x["notes"].append(a.note)
    save(a.run, st, f"set {x['key']} {a.state}" + (f" ({a.note})" if a.note else ""))
    print(f"{x['key']}: {a.state}  attempts={x['attempts']} revisions={x['revisions']}  launches={st['launches']}/{st['budget']['max_agents']}")


def cmd_terminal(a):
    st = load(a.run)
    ensure_live(st)
    if a.state not in TERMINAL:
        die(2, f"terminal state must be one of {TERMINAL}")
    running = [x["key"] for x in st["agents"] if x["state"] in ("running", "queued")]
    if running and a.state.startswith("completed"):
        die(2, f"cannot complete while agents are queued/running: {running}")
    stale = stale_lines(st)
    if stale and a.state == "completed":
        die(2, "cannot complete while agents are stale (re-run or accept them, or end completed_with_defects "
               "and list them in the README):\n" + "\n".join(stale))
    open_ = [f"{x['key']} ({x['state']})" for x in st["agents"] if x["state"] in ("revise", "failed")]
    if open_ and a.state == "completed":
        die(2, f"cannot complete while agents are revise or failed: {open_}; re-run or cancel them, or end "
               "completed_with_defects")
    if a.state == "completed" and baseline_changed(st):
        die(2, f"cannot complete: the baseline {st['baseline']['dir']} changed during the run")
    for line in stale:
        print(line)
    st["terminal"] = {"state": a.state, "reason": a.reason}
    save(a.run, st, f"terminal {a.state}: {a.reason}")
    print(f"run terminal: {a.state}")


def cmd_budget(a):
    st = load(a.run)
    ensure_live(st)
    new = {k: v for k, v in (("max_agents", a.max_agents), ("max_waves", a.max_waves),
                             ("max_revisions", a.max_revisions), ("max_attempts", a.max_attempts)) if v is not None}
    if not new:
        die(2, "give at least one of --max-agents, --max-waves, --max-revisions, --max-attempts")
    if not a.reason.strip() or not a.approved_by.strip():
        die(2, "--reason and --approved-by must not be empty")
    b = st["budget"]
    for k, v in new.items():
        if v <= b[k]:
            die(2, f"budget can only be raised: {k} {b[k]} -> {v}")
    if "max_agents" in new and new["max_agents"] < st["launches"]:
        die(2, f"max_agents {new['max_agents']} < launches already made {st['launches']}")
    for k, v in new.items():
        old, b[k] = b[k], v
        st["events"].append({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "msg": f"budget {k} {old} -> {v}",
                             "type": "budget_override", "field": k, "from": old, "to": v,
                             "approved_by": a.approved_by, "reason": a.reason})
    save(a.run, st)
    print(f"budget={b}")


def baseline_changed(st):
    b = st.get("baseline")
    return bool(b) and tree_hash(b["dir"]) != b["tree_sha"]


def cmd_snapshot(a):
    st = load(a.run)
    snap = {"wave": st["wave"], "events": len(st["events"]),  # event-log position: who is launched after this
            "run": file_hashes(a.run, skip=RUN_SKIP)}
    skill = a.skill_dir or st["skill_version"]["skill_dir"]
    snap["skill_dir"] = skill
    snap["skill"] = file_hashes(skill)
    d = Path(a.run) / ".snapshots"
    d.mkdir(exist_ok=True)
    n = sum(e.get("type") == "snapshot" for e in st["events"])
    name, data = f"{n:03d}-wave{st['wave']}.json", json.dumps(snap)
    (d / name).write_text(data, encoding="utf-8")
    # the snapshot used by verify-writes is the one logged here, checked by hash: a file dropped in
    # .snapshots/ is never loaded
    st["events"].append({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "msg": f"snapshot {name}", "type": "snapshot",
                         "file": name, "sha": hashlib.sha256(data.encode("utf-8")).hexdigest()})
    save(a.run, st)
    print(f"snapshot {n:03d}: {len(snap['run'])} run files, {len(snap['skill'])} skill files")


def changed(before, after):
    keys = set(before) | set(after)
    return sorted(k for k in keys if before.get(k) != after.get(k))


def cmd_verify_writes(a):
    st = load(a.run)
    logged = [e for e in st["events"] if e.get("type") == "snapshot"]
    if not logged:
        die(2, "no snapshot; run `snapshot` before launching the wave")
    f = Path(a.run) / ".snapshots" / logged[-1]["file"]
    data = f.read_bytes() if f.is_file() else b""
    if hashlib.sha256(data).hexdigest() != logged[-1]["sha"]:
        die(5, f"snapshot {f.name} is missing or was modified after it was taken; the wave cannot be verified")
    snap = json.loads(data)
    # this wave's agents, plus earlier agents (re)launched since the snapshot: revise/failed -> running
    relaunched = set()
    for e in st["events"][snap["events"]:]:
        w = e["msg"].split()
        if len(w) >= 3 and w[0] == "set" and w[2] == "running":
            relaunched.add(w[1])
    owners = [x for x in st["agents"] if x["state"] != "cancelled"]
    allowed = [x["output"] for x in owners if x["wave"] == snap["wave"] or x["key"] in relaunched]

    def owner(c):  # the longest registered output containing c: a final synthesizer does not own wave-<n>/
        hits = [x for x in owners if c == x["output"] or c.startswith(x["output"] + "/")]
        return max(hits, key=lambda x: len(x["output"]), default=None)

    run_changes = changed(snap["run"], file_hashes(a.run, skip=RUN_SKIP))
    skill_changes = changed(snap["skill"], file_hashes(snap["skill_dir"]))
    orch = [c for c in run_changes if c.startswith(ORCHESTRATOR_PATHS)]
    bad = [c for c in run_changes if c not in orch and (owner(c) is None or owner(c)["output"] not in allowed)]
    bad += [f"SKILL_DIR/{c}" for c in skill_changes]
    print(f"wave {snap['wave']}: {len(run_changes)} changed run files; allowed outputs: {allowed}")
    for c in orch:
        print("  ORCHESTRATOR WRITE", c, "(orchestrator-owned path; confirm the orchestrator made it)")
    if bad:
        for b in bad:
            print("  VIOLATION", b)
        # logged, so a later relaunch of the owner (which would allow the path) cannot erase it
        st["events"].append({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "msg": f"verify-writes {len(bad)} violation(s)",
                             "type": "write_violation", "snapshot": logged[-1]["file"], "files": bad})
        save(a.run, st)
        die(5, f"{len(bad)} write(s) outside assigned outputs")
    print("no write violations")


def cmd_reconcile(a):
    st = load(a.run)
    run = Path(a.run)
    issues = []
    print(f"run {st['run_id']} phase={st['phase']} wave={st['wave']} terminal={st['terminal']}")
    print(f"skill version at init {st['skill_version']['skill_tree_sha']}; now {tree_hash(st['skill_version']['skill_dir'])}")
    if tree_hash(st["skill_version"]["skill_dir"]) != st["skill_version"]["skill_tree_sha"]:
        issues.append("skill files changed since the run started (cards/workflows may differ)")
    for x in st["agents"]:
        p = run / x["output"]
        if x["role"] == "executor":
            p = p / "artifact.md"  # companions alone do not make an executor's output
        # a final synthesizer's directory also holds the partial ones (wave-<n>/): only its own files count
        exists = p.exists() and (p.is_file() or any(f.is_file() or x["role"] != "synthesizer" for f in p.iterdir()))
        hint = ""
        if x["state"] == "done" and not exists:
            hint = "marked done but output missing -> set failed and relaunch"
        elif x["state"] == "running":
            hint = (f"output exists: verify with check_artifact.py on {p.relative_to(run).as_posix()}, then set done/failed" if exists
                    else "no output: the agent was probably lost; set failed and relaunch")
        elif x["state"] == "queued":
            hint = "not launched yet"
        elif x["state"] == "revise":
            hint = "relaunch the same agent role with the review file"
        if hint:
            issues.append(f"{x['key']} [{x['role']} {x['state']}] {x['output']}: {hint}")
    issues += stale_lines(st)
    if baseline_changed(st):
        issues.append(f"baseline {st['baseline']['dir']} changed since init (it is read-only input)")
    for i in issues:
        print("  ", i)
    if issues:
        sys.exit(6)
    print("consistent")


def cmd_show(a):
    st = load(a.run)
    b = st["budget"]
    print(f"run {st['run_id']}  depth={st['depth']}  phase={st['phase']}  wave={st['wave']}  terminal={st['terminal']}")
    print(f"launches {st['launches']}/{b['max_agents']}  max_waves {b['max_waves']}  max_revisions {b['max_revisions']}  "
          f"max_attempts {b['max_attempts']}  version {st['skill_version']['skill_tree_sha']}")
    for e in st["events"]:
        if e.get("type") == "budget_override":
            print(f"  BUDGET RAISED {e['t']} {e['field']} {e['from']} -> {e['to']}  approved_by={e['approved_by']!r}  reason={e['reason']!r}")
        elif e.get("type") == "stale_accepted":
            print(f"  STALE ACCEPTED {e['t']} {e['msg']}  upstream={e['upstream']}")
        elif e.get("type") == "write_violation":
            print(f"  WRITE VIOLATION {e['t']} snapshot {e['snapshot']}: {', '.join(e['files'])}")
    for x in st["agents"]:
        print(f"  {x['key']:6s} {x['role']:11s} w{x['wave']} {x['state']:9s} att={x['attempts']} rev={x['revisions']} {x['output']}")
    for line in stale_lines(st):
        print(" ", line)


def cmd_stale(a):
    for line in stale_lines(load(a.run)):
        print(line)


def cmd_estimate(a):
    n = (a.researchers, a.executors, a.critics, a.synthesizers)
    if min(n) < 0 or a.revise_rate < 0 or a.failure_rate < 0:
        die(2, "counts and rates must not be negative")
    base = sum(n)
    revisions = a.executors * a.revise_rate
    relaunches = (base + revisions) * a.failure_rate
    total = math.ceil(base + revisions + relaunches)
    fits = next((f"{d} (max_agents {m})" for d, (m, _) in DEPTH_BUDGET.items() if m >= total),
                "none — pass --max-agents at init")
    print(f"base launches: {base} ({a.researchers} researchers + {a.executors} executors + {a.critics} critics "
          f"+ {a.synthesizers} synthesizers)")
    print(f"expected revisions: {revisions:.1f} ({a.executors} executors x {a.revise_rate})")
    print(f"expected relaunches: {relaunches:.1f} (({base} + {revisions:.1f}) x {a.failure_rate})")
    print(f"total: {total}")
    print(f"fits: {fits}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("init"); p.add_argument("run"); p.add_argument("--depth", required=True, choices=list(DEPTH_BUDGET))
    p.add_argument("--max-agents", type=int); p.add_argument("--max-waves", type=int); p.add_argument("--skill-dir")
    p.add_argument("--baseline", help="read-only baseline run dir (refresh runs)")
    p = sp.add_parser("phase"); p.add_argument("run"); p.add_argument("phase"); p.add_argument("--wave", type=int)
    p = sp.add_parser("add"); p.add_argument("run"); p.add_argument("key"); p.add_argument("--role", required=True)
    p.add_argument("--output", required=True); p.add_argument("--method"); p.add_argument("--scope"); p.add_argument("--wave", type=int)
    p.add_argument("--depends-on", help="comma-separated keys whose revision makes this agent stale")
    p = sp.add_parser("set"); p.add_argument("run"); p.add_argument("key"); p.add_argument("state")
    p.add_argument("--task-id"); p.add_argument("--note")
    p = sp.add_parser("terminal"); p.add_argument("run"); p.add_argument("state"); p.add_argument("--reason", required=True)
    p = sp.add_parser("budget", help="raise limits; only with explicit user approval")
    p.add_argument("run"); p.add_argument("--max-agents", type=int); p.add_argument("--max-waves", type=int)
    p.add_argument("--max-revisions", type=int); p.add_argument("--max-attempts", type=int); p.add_argument("--reason", required=True)
    p.add_argument("--approved-by", required=True, help="who approved the raise (the user)")
    p = sp.add_parser("snapshot"); p.add_argument("run"); p.add_argument("--skill-dir")
    p = sp.add_parser("estimate", help="expected launches for a plan; no run dir")
    for r in ("researchers", "executors", "critics"):
        p.add_argument(f"--{r}", type=int, required=True)
    p.add_argument("--synthesizers", type=int, default=1)
    p.add_argument("--revise-rate", type=float, default=REVISE_RATE)
    p.add_argument("--failure-rate", type=float, default=FAILURE_RATE)
    for name in ("verify-writes", "reconcile", "show", "stale"):
        p = sp.add_parser(name); p.add_argument("run")
    a = ap.parse_args()
    {"init": cmd_init, "phase": cmd_phase, "add": cmd_add, "set": cmd_set, "terminal": cmd_terminal,
     "budget": cmd_budget,
     "snapshot": cmd_snapshot, "verify-writes": cmd_verify_writes, "reconcile": cmd_reconcile,
     "show": cmd_show, "stale": cmd_stale, "estimate": cmd_estimate}[a.cmd](a)


if __name__ == "__main__":
    main()
