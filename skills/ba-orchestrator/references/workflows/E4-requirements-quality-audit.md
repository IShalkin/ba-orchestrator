# WF-E4 — Requirements Quality Audit (existing spec or backlog → defects, gaps, traceability, fix plan)

**Use when:** a specification, backlog or set of user stories already exists, and the question is "is it good enough to build, buy or sign?"
**Composes:** T7 (review, quality) + T6.4 (traceability) + T5.5 / T5.7 (NFR and acceptance coverage) + T4.2 (model cross-checks).
**Deliverables:** a defect log by severity, a quality scorecard per criterion, missing NFRs and acceptance criteria, a traceability gap report, terminology conflicts, and a prioritised fix plan.

## Waves
| Wave | Executors (parallel inside a wave) | Depends on |
|---|---|---|
| 1 | `requirements-quality-verification-and-analysis` · `glossary` (extract terms and find conflicts) · `requirements-traceability` (reverse-engineer from what exists) | research |
| 2 | `perspective-based-reading` ×3 (user / developer / tester scope suffixes) · `structured-4-pass-specification-review` | 1 |
| 3 | `non-functional-requirements-analysis` (coverage check, not authoring) · `acceptance-and-fit-criteria` (coverage check) · `crud-matrix` (when data and functions can be cross-referenced) | 1 |
| 4 | synthesizer: merge the defects, deduplicate, rank, and draft the fix plan | 2, 3 |

Waves 2 and 3 run in parallel; both depend only on wave 1.

## Gates
- Audit executors **do not rewrite** the audited specification. They report defects with anchors (document, section, requirement id).
- At the end: show the fix plan to the user. Fixing is a separate WF-T5 run, and only if the user asks for it.
