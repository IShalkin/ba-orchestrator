# ba-orchestrator

A Claude Code skill that runs business-analysis work as multi-agent workflows. You give it a BA request: discovery, requirements, a business case, a requirements audit, stakeholder analysis or process redesign. It works through the request like this:

1. It **routes** the request to a workflow: 8 task workflows, 5 end-to-end scenarios, or a refresh of an existing baseline against changed sources.
2. It **plans** the methods from a catalogue of **259 BA method cards**, and shows you the plan.
3. It **fans out** subagents in dependency waves:
   - researchers search your project sources through MCP (Confluence, Jira, SharePoint, GitHub, transcripts, whiteboards) and local files;
   - executors apply one method each;
   - a synthesizer consolidates the results;
   - critics review each artifact.
4. It **verifies** every output with deterministic scripts, outside the model.
5. It **packages** evidence-labelled artifacts: every claim is `[E:id]`, `[ASSUMPTION]`, `[GAP]` or `[METHOD]`.

Status: **v0.3 (pilot)**. See [Limitations](#limitations).

## Repository layout

```
skills/ba-orchestrator/          the skill (copy to .claude/skills/ba-orchestrator/)
  SKILL.md                       orchestrator procedure, routing table, rules
  references/
    taxonomy.md                  8 tasks → 43 subtasks → 259 methods
    tasks/T1..T8-*.md            per-task selection guides ("solves … / not for …")
    methods/<id>.md              method cards (16 fields; one variant per source)
    workflows/T*.md, E*.md, R1   14 workflows: waves, default methods, switch rules, gates
    run-protocol.md              state machine, budgets, dispatch, verification, resume/cancel
    artifact-conventions.md      evidence labels; artifact / research / review formats
    source-access.md             finding and reading MCP and file sources, read-only
    hardening.md                 install-time controls and residual risks
  scripts/
    run_state.py                 run state machine, budgets, ownership checks, reconcile
    check_artifact.py            format and evidence-id checks for agent outputs
    find_methods.py              keyword ranking of method cards
    workflows/*.js               Workflow tool templates: research, execute-wave, review, synthesize
    stage/*.py                   staging (decks, whiteboards, tracker export, workbooks) and trace merging
agents/                          the 4 subagents (copy to .claude/agents/)
  ba-researcher.md  ba-method-executor.md  ba-synthesizer.md  ba-critic.md
build/                           regenerate and verify the method cards (see build/README.md)
data/                            source data for the build (taxonomy, method table, mind maps)
```

## Install

```bash
# in your project (or use ~/.claude for all projects)
mkdir -p .claude/skills .claude/agents
cp -r skills/ba-orchestrator .claude/skills/
cp agents/ba-*.md .claude/agents/
```

1. **Restart Claude Code** if `.claude/agents/` did not exist before. New agent directories are only picked up at start-up.
2. **Connect the MCP servers** for your sources.
3. **Apply [`hardening.md`](skills/ba-orchestrator/references/hardening.md):** read-only credentials and `permissions.deny` for MCP write tools. Do this before running against real sources.

Requires Python 3.9+ (standard library only) for the scripts.

## Use

```
Use ba-orchestrator: customers complain orders arrive late — find out why and who we need to talk to.
```

1. The orchestrator writes a brief and a plan under `ba-runs/<run>/` and asks you to confirm the plan.
2. It runs the waves.
3. It ends the run in an explicit terminal state, with `06-final/README.md`.

To continue an interrupted run, say "resume run `<name>`".

| Request | Workflow |
|---|---|
| New initiative: what is the problem, who is involved | E1 Initiative discovery |
| Specify an agreed feature | E2 Feature specification |
| Invest? Build or buy? Which vendor? | E3 Business case and solution selection |
| Is this spec or backlog ready? | E4 Requirements quality audit |
| Redesign a broken process | E5 Process improvement |
| Re-check an existing baseline against changed sources (for example weekly) | R1 Refresh against baseline |
| A single task area | T1 Strategy · T2 Situation investigation · T3 Stakeholders · T4 Modelling · T5 Specification · T6 Prioritisation and management · T7 Validation · T8 Change and benefits |

Without connected sources, the skill runs in **brief-only mode**: everything is labelled as an assumption, and each artifact lists the elicitation questions to ask.

**Dispatch modes.** When the Workflow tool is available, each wave runs as one Workflow invocation of a shipped template in `scripts/workflows/` (mode W, the default), with the run's values passed as `args`. Otherwise the orchestrator launches the same agents with the Agent tool, at most 5 at a time (mode A). The brief records the mode; staging, budgets, gates and verification are the same in both. In mode W the orchestrator still registers every agent before a wave and checks every output after it, and counts the one automatic retry a template makes when an agent dies on an infrastructure error.

## How it stays controlled

- **No nested agents.** The Agent tool is blocked in every agent's frontmatter. Only the orchestrator dispatches.
- **Run state outside the model.** `run_state.py` keeps the run in `status.json`. It refuses illegal transitions, duplicate assignments and launches beyond the budget, and records the skill version.
- **Outputs checked outside the model.** `check_artifact.py` runs after every agent. Agents' own "done" messages are not trusted.
- **File ownership.** Each agent writes only its own path. `run_state.py verify-writes` detects any other change, including changes to the skill itself.
- **Revision cascade.** Agents are registered with the keys they depend on; after a revision `run_state.py stale` lists every dependent built on the old version, and a run cannot end `completed` until each is re-run or explicitly accepted.
- **Bounded loops.** By default at most 2 revisions and 2 attempts per agent, raised only through `run_state.py budget` with a logged approver, and every agent has `maxTurns`.

## Limitations

- **One field run on live sources.** A single deep run (slide decks, diagrams, whiteboards, wiki pages, an issue tracker) has been done; its fixes are listed in the [CHANGELOG](CHANGELOG.md) under 0.3.0. There is no repeatable test against live sources; the `build/test_*.py` suites cover the scripts only.
- **Search is keyword-based.** `find_methods.py` uses keyword ranking. Final method choice comes from the workflows and task guides.
- **Guarantee limits.** The write checks detect after the fact and only inside the run and skill directories. A critic's PASS is a second check, not an independent guarantee. Details in [`hardening.md`](skills/ba-orchestrator/references/hardening.md) §4.
- **No routing eval set yet.** There is no test set of reference requests for routing and method selection.
