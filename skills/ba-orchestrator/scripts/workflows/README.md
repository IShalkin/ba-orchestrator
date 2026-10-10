# Workflow templates

Generic scripts for the Claude Code Workflow tool, used in dispatch mode W (run-protocol §11). One invocation runs one wave. Pass every per-run value through `args`; never edit a template for a run. Each template runs its agents in a pool of 5, retries an agent that returned no result once, and returns `[{key, reply, retried}]`.

The scripts cannot touch the filesystem or run state. Before each invocation the orchestrator runs `RS snapshot`, `RS add` and `RS set <key> running` for every item; afterwards it runs `CA` and `RS set done|failed` per item, counts every `retried: true` item (`RS set <key> failed`, then `running`), and runs `RS verify-writes`. Set `retry: false` on an item that has no attempt or launch headroom left.

`skillDir` and `runDir` must be absolute (the template refuses otherwise). Every other path in `args` may be absolute or relative to `runDir`; the template resolves it, so every brief carries absolute paths. A path list is an array or a comma-separated string. Every template takes `skillDir`, `runDir` and, per item, an optional `retry: false` and `errors`: free text (the `check_artifact.py` errors of a relaunch) added to the brief as `ERRORS TO FIX`, never treated as a path.

## research.js

| Arg | Meaning |
|---|---|
| `planSection` | Plan section the researchers read (default `research`) |
| `researchers[].id` | Item key; also names the default output `02-research/<id>.md` |
| `researchers[].output` | Output file, if not the default |
| `researchers[].sources` | Sources to search (text) |
| `researchers[].questions` | Research questions: an array (numbered RQ1..) or one string |
| `researchers[].staged` | Path list of staged renders and text extracts |
| `researchers[].previousLog` | Log to continue rather than overwrite |
| `researchers[].inputArtifacts` | Path list of input artifacts to look for (default: the cards named in the plan) |

```
Workflow({scriptPath: '<skill dir>/scripts/workflows/research.js', args: {
  skillDir: '<skill dir>', runDir: '<run dir>', planSection: '2',
  researchers: [
    {id: 'R1', sources: 'wiki space X, issue tracker project Y',
     questions: ['Which steps of the process fail most often? (feeds: root-cause-analysis)'],
     staged: ['<staging dir>/deck-a/slide-001.png', '<staging dir>/deck-a/slide-001.md']},
    {id: 'R2', sources: 'meeting transcripts in <dir>', questions: ['...'],
     previousLog: '02-research/R2.md'}
  ]}})
```

## execute-wave.js

| Arg | Meaning |
|---|---|
| `executors[].key` | Item key |
| `executors[].method` | Method id; names the card and the output directory `03-artifacts/<method>[--<scope>]/` |
| `executors[].scope` | Scope slug for the output directory |
| `executors[].scope_text` | Scope as the executor reads it |
| `executors[].upstream` | Path list of upstream artifacts |
| `executors[].instructions` | Source variant guidance (text) |
| `executors[].revision` | Path of the review to revise against |

Dependencies are not an arg: give them to `RS add --depends-on` before the run. A dependent goes in a later wave than its upstream (`RS set running` refuses it otherwise).

For method `requirements-traceability` the brief also carries the fixed `trace.csv` header: `req_id,req_type,capability,jira_keys,coverage,jira_statuses,mvp_class_source,mvp_class_jira,conflict_flags,gap_note,evidence`.

```
Workflow({scriptPath: '<skill dir>/scripts/workflows/execute-wave.js', args: {
  skillDir: '<skill dir>', runDir: '<run dir>',
  executors: [
    {key: 'X1', method: '<method-id>', scope: 'billing', scope_text: 'The billing sub-process only',
     upstream: '03-artifacts/<other-method-id>/artifact.md', instructions: 'Use the second source variant'},
    {key: 'X2', method: '<method-id>', scope: 'returns', scope_text: 'The returns sub-process',
     revision: '05-review/<method-id>--returns.md'},
    {key: 'X3', method: '<method-id>', scope: 'refunds', scope_text: 'The refunds sub-process',
     errors: 'FORM-ONLY section missing: ## Assumptions'}
  ]}})
```

## review.js

| Arg | Meaning |
|---|---|
| `critics[].key` | Item key |
| `critics[].artifact_dir` | Directory name under `03-artifacts` (a path is reduced to its last segment) |
| `critics[].method` | Method id of the artifact's card |
| `critics[].out` | File name under `05-review` (default `artifact_dir`; a path is reduced to its last segment) |
| `critics[].focus` | Extra focus for the critic (text) |
| `critics[].model` | Different model for a second-opinion critic (run-protocol §7) |
| `critics[].staged` | Path list of staged renders to re-open |

```
Workflow({scriptPath: '<skill dir>/scripts/workflows/review.js', args: {
  skillDir: '<skill dir>', runDir: '<run dir>',
  critics: [
    {key: 'C1', artifact_dir: '<method-id>--billing', method: '<method-id>'},
    {key: 'C1b', artifact_dir: '<method-id>--billing', method: '<method-id>',
     out: '<method-id>--billing--second', model: 'sonnet', focus: 'Second opinion on the decision-critical claims'}
  ]}})
```

## synthesize.js

| Arg | Meaning |
|---|---|
| `key` | Item key; default `S-final` (final) or `S-w<wave>` (partial), so two syntheses never collide |
| `mode` | `final` (default) or `partial` |
| `wave` | Wave number; required for `partial`, names `04-synthesis/wave-<wave>/` |
| `artifacts` | Path list of artifacts whose Summaries to read (default all of `03-artifacts`) |
| `decisions` | Decisions the synthesis supports (text; default from the brief) |
| `measuredCounts` | Path list of the count files computed by script (run-protocol §8) |
| `retry` | `false` when no attempt or launch headroom is left |
| `errors` | `check_artifact.py` errors of a relaunch (text) |

```
Workflow({scriptPath: '<skill dir>/scripts/workflows/synthesize.js', args: {
  skillDir: '<skill dir>', runDir: '<run dir>', mode: 'final',
  decisions: 'Go or no-go on the redesign',
  measuredCounts: ['<run dir>-staging/counts/coverage-summary.json']}})
```
