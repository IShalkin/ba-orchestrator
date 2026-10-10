# WF-R1 — Refresh Against a Baseline (changed sources → drift report for change control)

**Use when:** a baseline run already exists (its requirement catalogues, `trace.csv` files and `coverage-summary.json` are `done`), and its sources have changed since: for example a weekly re-check of the issue tracker against the agreed requirements.
**Not when:** there is no baseline run (use WF-E2 or WF-E4 first), or the scope or goals changed (that is a new run, not a refresh).
**Composes:** T6.4 (traceability) + T7 (quality audit) + T6.5 (change control).
**Brief must contain:** the baseline run directory, which sources changed and since when, and who owns change control.
**Deliverables:** a refreshed merged trace, a new `coverage-summary.json`, and a drift report against the baseline.

## Rules
- **The baseline is read-only input.** Executors trace against the baseline run's requirement catalogues; they do not add, split or reword requirements. A candidate new requirement is listed in the drift report and goes to change control. It enters the catalogue only when change control approves it, in a separate run.
- **Re-stage only what changed**, issue-tracker export first (`source-access.md` §4), into a new staging directory. Unchanged staged sources are reused by path from the baseline run.
- New run directory, `RS init … --baseline <baseline run dir>`: the baseline's tree hash is recorded, `RS reconcile` reports any change to it and `completed` is refused. The brief names the baseline run. Register every executor with `--depends-on` its upstream keys (run-protocol §4).

## Waves
| Wave | Executors (parallel inside a wave) | Depends on |
|---|---|---|
| 0 | researchers on the changed sources only | staging |
| 1 | `requirements-traceability`, one per capability scope of the baseline, against the baseline catalogues, each writing `trace.csv` with the fixed columns (run-protocol §8) · `requirements-quality-verification-and-analysis` on the changed or new issues | research |
| 2 | orchestrator, by script: `merge_trace.py OUT --trace <new trace.csv files> --issues <current issues.json> --baseline <baseline>/…/coverage-summary.json` writes the new `coverage-summary.json`. Its `drift` section diffs requirement coverage only (coverage changed from → to, requirement ids added, removed); it does not diff capability, scope, issue status or conflicts | 1 |
| 3 | `change-impact-analysis` for each `drift` item, and for each re-scoped or re-labelled issue the wave 1 quality executor reported (scope drift is not in the script diff, so it arrives only that way) | 2 |
| 4 | synthesizer with both coverage summaries as `MEASURED COUNTS`: the drift report | 3 |

## Drift report (in the synthesis)
Measured by script, counts used as given:
- Requirements whose coverage changed (from → to), added or removed: the wave 2 `drift` section, with the issues that caused each change.
- Current issues that reference no baseline requirement: `unreferenced_issues` in the new summary.
- Current conflict rows: `conflict_rows` in the new summary.

Reported by executors, with evidence, and labelled as not script-measured (no script diffs these against the baseline):
- Issues cancelled, closed, re-labelled or re-scoped since the baseline.
- Conflicts opened and conflicts closed, by comparing the current `conflict_rows` with the baseline's.
- Candidate new requirements, each marked for change control.

## Gates
- Plan gate: confirm the baseline run and the changed sources.
- At the end: hand the drift report to the change-control owner. The output feeds WF-T6 wave 3 (`change-control`, `change-impact-analysis`); this workflow does not update the baseline (`requirements-baselines-and-version-control`).
