# Changelog

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
