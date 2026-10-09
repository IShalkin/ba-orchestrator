# WF-T7 — Validation and Acceptance

**Use when:** requirements, models or a delivered solution must be checked for correctness, completeness, consistency, testability and fitness: a review before sign-off, test planning, or acceptance.
**Not when:** nothing has been written yet.
**Brief must contain:** what is under review (paths or ids), the baseline it is checked against, the review perspectives needed (user, developer, tester, compliance), and the acceptance authority.
**Deliverables:** a defect log (anchored, prioritised), a quality-criteria scorecard, prototype or usability findings, a test conditions and acceptance test plan, and a sign-off readiness statement.

## Waves

### Wave 1 — Static review (parallel, one executor per perspective)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 7.1 Inspect | `requirements-reviews-and-inspections` | `perspective-based-reading`: one executor each for the user, designer and tester perspectives; `structured-4-pass-specification-review` against superficial sign-off; `requirements-quality-gateway` as an intake filter for new requirements; `walk-through` for shared understanding; `paraphrased-solution-review` to confirm stakeholder understanding |
| 7.1 Quality metrics | `requirements-quality-verification-and-analysis` | — |
| 7.3 Model checks (only when models exist) | `model-and-requirements-database-queries` | `model-checking` or `theorem-proving` for formal specifications |

### Wave 2 — Dynamic validation (needs wave 1; only when a prototype or solution exists)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 7.2 Validate | `validation-through-prototypes` | `usability-testing` with real tasks; `specification-animation` for formal or executable specifications |

### Wave 3 — Test and accept (needs waves 1–2)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 7.4 Tests | `requirements-based-testing` | `use-case-driven-test-planning` when use cases exist |
| 7.4 Acceptance | `acceptance-testing` | `checkpoint-charley-technical-design-review` to check a technical design against the business solution before build |

## Research questions (seed)
- Which version of the artifact is under review, and what is the approved baseline?
- Which defects, review comments or test results already exist?
- Which acceptance criteria and sign-off rules are documented, and who signs?

## Gates and checks
- Every defect is anchored (document, section or line, requirement id) and tied to a criterion or anti-pattern from a card.
- Reviewers never fix the artifact under review. They report, and the owner revises (run protocol, ownership rule).
- The sign-off readiness statement lists open blockers explicitly. Never declare readiness when blockers remain.

## Hand-offs
Defects → back to the owners of the WF-T5 or WF-T4 artifacts. The acceptance plan → WF-T8 (deployment readiness).
