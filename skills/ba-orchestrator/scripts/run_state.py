#!/usr/bin/env python3
"""Deterministic run state for ba-orchestrator: state machine, budgets, resume, write-ownership checks.

status.json in RUN_DIR is the single source of truth for a run. The orchestrator changes it ONLY
through this script, so transitions, budgets and duplicate checks are enforced outside the model.

Commands (all take RUN_DIR first):
  init RUN_DIR --depth light|standard|deep [--max-agents N] [--max-waves N] [--skill-dir DIR]
  phase RUN_DIR PHASE [--wave N]                 move the run to a phase (see PHASES)
  add RUN_DIR KEY --role ROLE --output REL [--method ID] [--scope S] [--wave N]
  set RUN_DIR KEY STATE [--task-id ID] [--note TEXT]
  terminal RUN_DIR STATE --reason TEXT           end the run (see TERMINAL)
  snapshot RUN_DIR [--skill-dir DIR]             hash files before a wave
  verify-writes RUN_DIR                          after a wave: any change outside the wave's outputs?
  reconcile RUN_DIR                              resume aid: compare status.json with files on disk
  show RUN_DIR

Exit codes: 0 ok, 2 usage/state error, 3 budget exhausted, 4 duplicate assignment, 5 write violation,
6 reconcile found inconsistencies.
"""
import argparse, hashlib, json, sys, time
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


def tree_hash(root, skip=()):
    h = hashlib.sha256()
    root = Path(root)
    for f in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = f.relative_to(root).as_posix()
        if "__pycache__" in rel or any(rel.startswith(s) for s in skip):
            continue
        h.update(rel.encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def file_hashes(root, skip=()):
    out = {}
    root = Path(root)
    for f in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = f.relative_to(root).as_posix()
        if "__pycache__" in rel or any(rel.startswith(s) for s in skip):
            continue
        out[rel] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


def agent(st, key):
    for a in st["agents"]:
        if a["key"] == key:
            return a
    die(2, f"unknown agent key {key}")


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
    if any(x["key"] == a.key for x in st["agents"]):
        die(4, f"duplicate key {a.key}")
    out = Path(a.output).as_posix().rstrip("/")
    for x in st["agents"]:
        if x["output"] == out and x["state"] not in ("cancelled", "failed"):
            die(4, f"duplicate assignment: {out} already owned by {x['key']} ({x['state']})")
    if st["launches"] >= st["budget"]["max_agents"]:
        die(3, f"budget_exhausted: {st['launches']} launches >= max_agents {st['budget']['max_agents']}")
    st["agents"].append({"key": a.key, "role": a.role, "method": a.method, "scope": a.scope,
                         "wave": a.wave if a.wave is not None else st["wave"], "output": out,
                         "state": "queued", "attempts": 0, "revisions": 0, "task_id": None, "notes": []})
    save(a.run, st, f"add {a.key} {a.role} -> {out}")
    print(f"added {a.key} ({a.role}) -> {out}")


def cmd_set(a):
    st = load(a.run)
    ensure_live(st)
    if a.state not in AGENT_STATES:
        die(2, f"state must be one of {AGENT_STATES}")
    x = agent(st, a.key)
    if a.state not in TRANSITIONS[x["state"]]:
        die(2, f"illegal transition {x['key']}: {x['state']} -> {a.state}")
    if a.state == "running":
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
    st["terminal"] = {"state": a.state, "reason": a.reason}
    save(a.run, st, f"terminal {a.state}: {a.reason}")
    print(f"run terminal: {a.state}")


def cmd_snapshot(a):
    st = load(a.run)
    snap = {"wave": st["wave"], "run": file_hashes(a.run, skip=("status.json", ".snapshots"))}
    skill = a.skill_dir or st["skill_version"]["skill_dir"]
    snap["skill_dir"] = skill
    snap["skill"] = file_hashes(skill)
    d = Path(a.run) / ".snapshots"
    d.mkdir(exist_ok=True)
    n = len(list(d.glob("*.json")))
    (d / f"{n:03d}-wave{st['wave']}.json").write_text(json.dumps(snap), encoding="utf-8")
    print(f"snapshot {n:03d}: {len(snap['run'])} run files, {len(snap['skill'])} skill files")


def changed(before, after):
    keys = set(before) | set(after)
    return sorted(k for k in keys if before.get(k) != after.get(k))


def cmd_verify_writes(a):
    st = load(a.run)
    d = Path(a.run) / ".snapshots"
    snaps = sorted(d.glob("*.json")) if d.exists() else []
    if not snaps:
        die(2, "no snapshot; run `snapshot` before launching the wave")
    snap = json.loads(snaps[-1].read_text(encoding="utf-8"))
    allowed = [x["output"] for x in st["agents"] if x["wave"] == snap["wave"]]
    run_changes = changed(snap["run"], file_hashes(a.run, skip=("status.json", ".snapshots")))
    skill_changes = changed(snap["skill"], file_hashes(snap["skill_dir"]))
    bad = [c for c in run_changes if not any(c == o or c.startswith(o + "/") for o in allowed)]
    bad += [f"SKILL_DIR/{c}" for c in skill_changes]
    print(f"wave {snap['wave']}: {len(run_changes)} changed run files; allowed outputs: {allowed}")
    if bad:
        for b in bad:
            print("  VIOLATION", b)
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
        exists = p.exists() and (p.is_file() or any(p.iterdir()))
        hint = ""
        if x["state"] == "done" and not exists:
            hint = "marked done but output missing -> set failed and relaunch"
        elif x["state"] == "running":
            hint = ("output exists: verify with check_artifact.py, then set done/failed" if exists
                    else "no output: the agent was probably lost; set failed and relaunch")
        elif x["state"] == "queued":
            hint = "not launched yet"
        elif x["state"] == "revise":
            hint = "relaunch the same agent role with the review file"
        if hint:
            issues.append(f"{x['key']} [{x['role']} {x['state']}] {x['output']}: {hint}")
    for i in issues:
        print("  ", i)
    if issues:
        sys.exit(6)
    print("consistent")


def cmd_show(a):
    st = load(a.run)
    b = st["budget"]
    print(f"run {st['run_id']}  depth={st['depth']}  phase={st['phase']}  wave={st['wave']}  terminal={st['terminal']}")
    print(f"launches {st['launches']}/{b['max_agents']}  max_waves {b['max_waves']}  version {st['skill_version']['skill_tree_sha']}")
    for x in st["agents"]:
        print(f"  {x['key']:6s} {x['role']:11s} w{x['wave']} {x['state']:9s} att={x['attempts']} rev={x['revisions']} {x['output']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("init"); p.add_argument("run"); p.add_argument("--depth", required=True, choices=list(DEPTH_BUDGET))
    p.add_argument("--max-agents", type=int); p.add_argument("--max-waves", type=int); p.add_argument("--skill-dir")
    p = sp.add_parser("phase"); p.add_argument("run"); p.add_argument("phase"); p.add_argument("--wave", type=int)
    p = sp.add_parser("add"); p.add_argument("run"); p.add_argument("key"); p.add_argument("--role", required=True)
    p.add_argument("--output", required=True); p.add_argument("--method"); p.add_argument("--scope"); p.add_argument("--wave", type=int)
    p = sp.add_parser("set"); p.add_argument("run"); p.add_argument("key"); p.add_argument("state")
    p.add_argument("--task-id"); p.add_argument("--note")
    p = sp.add_parser("terminal"); p.add_argument("run"); p.add_argument("state"); p.add_argument("--reason", required=True)
    p = sp.add_parser("snapshot"); p.add_argument("run"); p.add_argument("--skill-dir")
    for name in ("verify-writes", "reconcile", "show"):
        p = sp.add_parser(name); p.add_argument("run")
    a = ap.parse_args()
    {"init": cmd_init, "phase": cmd_phase, "add": cmd_add, "set": cmd_set, "terminal": cmd_terminal,
     "snapshot": cmd_snapshot, "verify-writes": cmd_verify_writes, "reconcile": cmd_reconcile,
     "show": cmd_show}[a.cmd](a)


if __name__ == "__main__":
    main()
