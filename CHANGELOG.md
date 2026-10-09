# Changelog

## 0.1.0

First pilot release.

- 256 method cards in an 8-task, 43-subtask taxonomy, generated from the method table and mind maps in `data/`. All 7,104 source field values are verified present in the cards (`build/verify_references.py`).
- 13 workflows: T1–T8 per task, plus E1–E5 end-to-end scenarios.
- 4 subagents: researcher, method executor, synthesizer, critic. The Agent tool is blocked in all of them, and each has `maxTurns`.
- `run_state.py`: run state machine, depth budgets, duplicate refusal, write-ownership detection, reconcile for resume, skill version recorded per run.
- `check_artifact.py`: deterministic format, evidence-id and companion checks.
- `find_methods.py`: keyword ranking of the method cards.
- Smoke-tested end to end in brief-only mode with the real agent types.
