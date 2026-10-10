# Changelog

## 0.3.0

Fixes from a deep field run (19 researchers, 11 executors, 11 critics; many sources were diagrams and slide decks):

- **Source staging.** Researchers have no shell, so the orchestrator now stages binary and visual sources before the research wave: slide and page renders including hidden slides (with a slide-count versus page-count check), per-slide text layers with speaker notes, whiteboard widget listings with coordinates, authors, dates and connections, wiki exports, a deterministic issue-tracker export, and spreadsheets as markdown. Large downloads go to disk, and each download is checked for size and type (`source-access.md` §4, SKILL.md step 2).
- **Write early.** Researchers write their log skeleton before the first search and rewrite it every 8–10 tool calls, so an agent that hits `maxTurns` no longer loses all its work. `check_artifact.py research` fails a log that still carries `GAP: not yet searched` (in the common spellings and any case, `[GAP] not searched` included) or `needs staging` anywhere except the quote cell of an Evidence row (verbatim source text), so a capped researcher, or one waiting for a staged source, is not marked done, and a relaunch continues its partial log (`PREVIOUS LOG`) instead of overwriting it.
- **Per-agent size caps.** At most about 50 images and 150 KB of text per agent; larger scopes are split, one researcher per slice. A context-limit failure is a mechanical failure: split and relaunch.
- **`run_state.py budget`** raises a limit (agents, waves, revisions, attempts) after explicit user approval and logs the reason and approver, so a budget is never raised by editing `status.json`. Empty reasons and approvers are refused, and `show` prints every raise. The approver is recorded, not verified (`hardening.md` §4).
- **Executor output is a directory.** Executors are registered on `03-artifacts/<method-id>[--<scope>]`, so `verify-writes` no longer flags their companion files. `add` refuses a file path for an executor or synthesizer and an output nested inside another live output; `reconcile` requires `artifact.md` inside an executor's directory; `check_artifact.py artifact` accepts the directory.
- **Verified absences.** A critic must search for an evidence id or locator before calling it missing, and the orchestrator drops a missing-id finding for an artifact that passed `check_artifact.py` and re-checks any other claimed absence before acting on a blocker. Critics get the staged renders (`STAGED SOURCES`), and researchers record both the original and the staged locator.
- **Measured coverage counts.** Counts merged across split executors are computed by the orchestrator with a deterministic script (`scripts/stage/merge_trace.py` for traces), with id ranges expanded, and given to the synthesizer as `MEASURED COUNTS`.
- **Two dispatch modes.** Mode W (default, when the Workflow tool is callable) runs each wave as one Workflow invocation of a template in `scripts/workflows/` (`research.js`, `execute-wave.js`, `review.js`, `synthesize.js`). The templates take every per-run value from `args`, build the run-protocol §10 briefs, keep 5 agents running, retry an agent that returned no result once and report it as `retried`, so the orchestrator counts the retry as a launch. Mode A (fallback) uses the Agent tool, at most 5 at a time. The orchestrator still runs `run_state.py` and `check_artifact.py` around every wave (run-protocol §11). Every researcher, executor and critic brief now carries a `VISUAL:` line. `build/verify_skill.py` checks that each template exists, opens with its `meta` literal and passes `node --check` when node is on PATH.
- **Template args documented in full.** Run-protocol §11 lists every value the templates read (`planSection` and per-researcher `inputArtifacts`, the critics' `staged`, the synthesizer's `key`), and says to pass `key` explicitly for every synthesis after the first.
- **`verify-writes` hardened.** It loads only the snapshot logged in `status.json`, checked by hash, so a file dropped in `.snapshots/` is never trusted; it attributes each changed file to the longest registered output containing it (a final synthesizer cannot rewrite a partial); it logs every violation in `status.json`, where `show` prints it after the owner is re-run; it skips exactly its own files; it allows the outputs of agents relaunched after the snapshot, and reports changes under `00-intake/`, `01-plan/` and `06-final/` as `ORCHESTRATOR WRITE` lines instead of violations. A subagent writing there is reported, not blocked (`hardening.md` §4).
- **Revision cascade.** Executors and synthesizers are registered with `--depends-on` their upstream keys. `set running` is refused while an upstream is not `done`. After any revision, `run_state.py stale` lists the dependents launched before their upstream last changed, whichever finished first; each is re-run or accepted with a recorded reason (`show` prints `STALE ACCEPTED`), `completed` is refused while any is stale, `revise` or `failed`, and the final README lists the accepted ones. `add --output` must be relative to the run directory, without `..`.
- **Refresh mode (WF-R1).** A new workflow re-checks an existing baseline against changed sources: re-stage only what changed (tracker export first), re-run only traceability and quality audit against the baseline catalogues (no new requirements without change control), merge with `merge_trace.py`, and report drift against the baseline `coverage-summary.json` (`merge_trace.py --baseline`). `init --baseline` records the baseline's hash, so a change to it is reported and `completed` is refused. The drift report feeds change control (WF-T6 wave 3). Routed from SKILL.md; mentioned in the T6, E2 and E4 hand-offs.
- **Staging scripts.** `scripts/stage/` stages decks, whiteboard exports, tracker exports and workbooks, and merges split traces; `source-access.md` §4 gives one usage line each and the platform notes (renderer detection, a scripted desktop presentation app needs the foreground, hidden slides, download checks).
- **Budget estimate at plan time.** `run_state.py estimate` adds expected revisions and relaunches to the planned launches (defaults 0.7 revisions per executor and 0.1 failed launches, from the field run) and names the depth that fits; SKILL.md step 1.6 runs it.
- **Fixed trace schema.** Every traceability executor writes `trace.csv` with the columns `merge_trace.py` checks; large sets are split by capability and merged, and the synthesizer gets `coverage-summary.json` as `MEASURED COUNTS` (run-protocol §8, E2, E4, T6).
- **Format errors graded.** A Summary of 301–360 words is a WARN with no relaunch; a relaunch for form-only errors (`FAIL FORM-ONLY`: Summary over 360 words, a missing heading other than Summary and Output) asks only for the form fix, and still counts as a launch. A missing or empty Summary or Output is a content error (run-protocol §5). The templates take the error text in a per-item `errors` field.
- **Staging safeguards.** The tracker export refuses `http://` without `--allow-http` and any redirect to another origin, so the token stays with the named server. Decks, sheets, whiteboards and tracker exports refuse a non-empty output folder, so versions never mix. The whiteboard script fails when items have no id; formulas with no cached value are kept as `=<formula>`. `merge_trace.py` counts a duplicated requirement by its lowest coverage whatever the input order, refuses coverage values outside the schema, and lists ambiguous key separators as range errors.
- **Tests.** `build/test_run_state.py`, `build/test_check_artifact.py` and `build/test_stage.py` cover the budget raise, directory outputs, overlapping registrations, verify-writes, reconcile, the stale cascade, the unfinished-log and form-only checks, and the staging scripts. `build/verify_skill.py` checks that the four templates' shared block is identical.


### Known issues (not fixed in 0.3.0)

- Cancelling an executor in `revise` or `failed` clears the completion block while its artifact stays on disk; `terminal completed` then passes. Remove or quarantine the artifact by hand before `completed`.
- A replacement agent that regenerates a cancelled stale agent's output does not clear its STALE line, so such a run can only end `completed_with_defects`.
- `stage_deck.py` leaves partial files in OUT when a present renderer fails, so the advised `--render none` retry needs a fresh OUT.
- `synthesize.js` in final mode renders an empty artifact list as blank text instead of falling back to all of `03-artifacts`; `absList` keeps null entries.
- Marker spellings such as `GAP: not yet read` or `staging needed` are not caught by `check_artifact.py research`.

## 0.2.0

Three additions from delivery practice:

- **Client Expectations Capture and Management** (T3, 3.3): expectations are kept in their own log, separate from requirements, and re-checked at every gate. An expectation becomes a requirement only through change control. Wired into WF-T3 wave 3, WF-E1 wave 2, and a new "Expectations at gates" rule in SKILL.md.
- **Process Hierarchy, Process Design and End-to-End Scenarios** (T4, 4.1): top-down process work for large scopes (hierarchy, one design per process, end-to-end scenarios, coverage matrix). Switching rule added to WF-T4 wave 1 and WF-E5.
- **Consolidated Solution Design Document** (T5, 5.6): one review-ready document in 19 sections, with the reviewer focus and typical errors of each section. New SKILL.md step 4b assembles it after synthesis, so it can use the traceability matrix and open questions. WF-T5 wave 4 now chooses between this template and SRS/PEGS, and WF-E2 gets an optional wave 6. The brief records the deliverable format.
- 259 method cards; 7,152 field values verified, and no author or book attribution in generated files.

## 0.1.0

First pilot release.

- 256 method cards in an 8-task, 43-subtask taxonomy, generated from the method table and mind maps in `data/`. All 7,104 source field values are verified present in the cards (`build/verify_references.py`).
- 13 workflows: T1–T8 per task, plus E1–E5 end-to-end scenarios.
- 4 subagents: researcher, method executor, synthesizer, critic. The Agent tool is blocked in all of them, and each has `maxTurns`.
- `run_state.py`: run state machine, depth budgets, duplicate refusal, write-ownership detection, reconcile for resume, skill version recorded per run.
- `check_artifact.py`: deterministic format, evidence-id and companion checks.
- `find_methods.py`: keyword ranking of the method cards.
- Smoke-tested end to end in brief-only mode with the real agent types.
