"""Static integrity checks for the ba-orchestrator skill and its agents. Exit 1 on failure."""
import json, re, sys
from pathlib import Path

SKILL = Path(sys.argv[1]).resolve()
AGENTS = Path(sys.argv[2]).resolve()
REF = SKILL / "references"
fails = []
idx = json.loads((REF / "methods-index.json").read_text(encoding="utf-8"))
ids = {e["id"] for e in idx}
sub_of = {e["id"]: e["subtask"] for e in idx}

# 1. method ids referenced in workflows / SKILL.md / agents exist
# agents do not reference method ids (their backticked tokens are status labels), so scan only routing docs
docs = [SKILL / "SKILL.md", *sorted((REF / "workflows").glob("*.md"))]
referenced = {}
for d in docs:
    for tok in re.findall(r"`([a-z0-9][a-z0-9-]+)`", d.read_text(encoding="utf-8")):
        if "-" in tok and tok not in ("ba-runs",) and not tok.startswith(("ba-", "mcp")):
            referenced.setdefault(tok, set()).add(d.name)
unknown = {t: sorted(f) for t, f in referenced.items() if t not in ids}
print(f"1) backticked method ids referenced: {len(referenced)}; unknown: {len(unknown)}")
for t, f in unknown.items():
    print("   UNKNOWN", t, f)
fails += [f"unknown method id {t}" for t in unknown]

# 2. paths referenced from SKILL.md exist
skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
paths = set(re.findall(r"`((?:references|scripts)/[^`<>*]+?)`", skill_md))
missing = sorted(p for p in paths if not (SKILL / p).exists())
print(f"2) concrete paths in SKILL.md: {len(paths)}; missing: {missing}")
fails += [f"missing path {p}" for p in missing]
for agent in ("ba-researcher", "ba-method-executor", "ba-synthesizer", "ba-critic"):
    if f"`{agent}`" not in skill_md and agent not in skill_md:
        fails.append(f"agent {agent} not mentioned in SKILL.md")
    if not (AGENTS / f"{agent}.md").exists():
        fails.append(f"agent file {agent}.md missing")

# 3. every subtask covered by >=1 workflow method reference
covered = {sub_of[t] for t in referenced if t in sub_of}
all_subs = sorted({e["subtask"] for e in idx}, key=lambda s: [int(x) for x in s.split(".")])
uncovered = [s for s in all_subs if s not in covered]
print(f"3) subtasks covered by workflows: {len(covered)}/{len(all_subs)}; uncovered: {uncovered}")
fails += [f"subtask {s} not referenced by any workflow" for s in uncovered]
print(f"   methods referenced by workflows: {len(set(referenced) & ids)}/{len(ids)}")

# 4. agent frontmatter sanity
for a in sorted(AGENTS.glob("ba-*.md")):
    t = a.read_text(encoding="utf-8")
    fm = t.split("---")[1] if t.startswith("---") else ""
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not name or name.group(1) != a.stem:
        fails.append(f"{a.name}: name mismatch")
    tools = re.search(r"^tools:\s*(.+)$", fm, re.M)
    no_agent = re.search(r"^disallowedTools:.*\bAgent\b", fm, re.M) or (tools and "Agent" not in tools.group(1))
    print(f"4) {a.stem}: tools={tools.group(1) if tools else 'inherit-all'}; Agent blocked={bool(no_agent)}")
    if not no_agent:
        fails.append(f"{a.name}: Agent tool not blocked")

    if not re.search(r"^maxTurns:\s*\d+", fm, re.M):
        fails.append(f"{a.name}: maxTurns missing")
    if "never instructions" not in t:
        fails.append(f"{a.name}: untrusted-content rule missing")
    if a.stem in ("ba-researcher", "ba-critic") and not re.search(r"^disallowedTools:.*\bBash\b", fm, re.M):
        fails.append(f"{a.name}: Bash not blocked for a source-reading agent")
    if re.search(r"\bindependent\b", fm.split("description:")[1].split("\n")[0], re.I) and "not an independent" not in fm:
        fails.append(f"{a.name}: description claims independence")

# 5. scripts present and runnable; no stale references to the old status.md
import subprocess
for s in ("run_state.py", "check_artifact.py", "find_methods.py"):
    p = SKILL / "scripts" / s
    ok = p.exists() and subprocess.run([sys.executable, "-I", str(p), "--help"], capture_output=True).returncode == 0
    print(f"5) scripts/{s}: {'ok' if ok else 'MISSING/BROKEN'}")
    if not ok:
        fails.append(f"script {s} missing or broken")
stale = [str(f.relative_to(SKILL)) for f in SKILL.rglob("*.md") if "status.md" in f.read_text(encoding="utf-8")]
stale += [f.name for f in AGENTS.glob("ba-*.md") if "status.md" in f.read_text(encoding="utf-8")]
print(f"   stale 'status.md' references: {stale}")
fails += [f"stale status.md reference in {s}" for s in stale]
rp = (REF / "run-protocol.md").read_text(encoding="utf-8")
for term in ("completed_with_defects", "budget_exhausted", "reconcile", "verify-writes", "cancelled"):
    if term not in rp:
        fails.append(f"run-protocol missing {term}")

# 6. Workflow templates: present, meta first with name/description, and parse under node when available
import shutil, tempfile
node = shutil.which("node")
shared = {}  # the shared block (pool, retry, paths, fixed brief lines) must stay byte-identical across templates
for t in ("research.js", "execute-wave.js", "review.js", "synthesize.js"):
    p = SKILL / "scripts" / "workflows" / t
    if not p.exists():
        fails.append(f"workflow template {t} missing")
        continue
    src = p.read_text(encoding="utf-8")
    blk = re.search(r"^// Shared block:.*?^const VISUAL = [^\n]*$", src, re.M | re.S)
    shared[t] = blk.group(0) if blk else None
    meta = src.split("\n}", 1)[0]
    if not src.startswith("export const meta = {") or not re.search(r"^\s*name:", meta, re.M) \
            or not re.search(r"^\s*description:", meta, re.M):
        fails.append(f"workflow template {t}: must start with 'export const meta = {{' carrying name and description")
    status = "node absent, syntax not checked"
    if node:
        # the body runs in an async context with a top-level return, so wrap it before checking
        with tempfile.TemporaryDirectory() as d:
            m = Path(d) / (p.stem + ".mjs")
            m.write_text("const __wf = async () => {\n" + src.replace("export const meta", "const meta", 1) + "\n}\n",
                         encoding="utf-8")
            r = subprocess.run([node, "--check", str(m)], capture_output=True, text=True)
        status = "node --check ok" if r.returncode == 0 else "node --check FAILED"
        if r.returncode:
            err = [l for l in r.stderr.splitlines() if "Error" in l] or ["syntax error"]
            fails.append(f"workflow template {t}: {err[0].strip()}")
    print(f"6) scripts/workflows/{t}: {status}")

if None in shared.values() or len(set(shared.values())) > 1:
    fails.append(f"workflow templates: the shared block differs or is missing ({sorted(k for k, v in shared.items() if v != shared.get('research.js'))})")
print(f"6) shared block identical in {len(shared)} templates: {None not in shared.values() and len(set(shared.values())) == 1}")

print("RESULT:", "PASS" if not fails else f"FAIL ({len(fails)})")
for f in fails:
    print("  ", f)
sys.exit(1 if fails else 0)
