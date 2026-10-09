# WF-E2 — Feature / Product Specification (agreed scope → specified, prioritised, testable requirements)

**Use when:** the scope and goals are agreed, and the team needs a requirements package ready for delivery.
**Composes:** T4 (models) + T5 (specification) + T6 (prioritise, trace) + T7 (review).
**Deliverables:** models, a glossary, functional requirements (stories or use cases), rules and decision tables, NFRs, acceptance criteria and examples, a prioritised backlog or release plan, a traceability matrix, a review report, and, when the brief's deliverable format asks for it, one assembled document.

## Waves
| Wave | Executors (parallel inside a wave) | Depends on |
|---|---|---|
| 1 | `business-process-modelling-bpmn-swimlanes` (to-be, or as-is if missing) · `entity-relationship-and-data-modelling` · `glossary` | research |
| 2 | primary functional form (WF-T5 table: `user-stories` + `user-story-mapping`, or `use-cases`) · `business-rules-analysis` (+ `decision-tables-and-decision-trees`) · `crud-matrix` | 1 |
| 3 | `non-functional-requirements-analysis` (+ `quality-attribute-scenarios` at deep depth) · `acceptance-and-fit-criteria` · `specification-by-example` (when rules are example-rich) | 2 |
| 4 | `value-cost-risk-prioritization-matrix` (or `moscow` for a fixed timebox) · `requirements-traceability` | 3 |
| 5 | critic pass, plus `perspective-based-reading` executors (user, developer and tester perspectives) | 4 |
| 6 | assembly, only when the brief's deliverable format is a single document: `consolidated-solution-design-document` (requirements and solution design) or `requirements-specification-templates-srs` (requirements only), as in WF-T5 wave 4 | SYNTHESIZE (SKILL.md step 4b) |

## Research questions (seed)
WF-T5 seeds plus: the existing backlog or specification location and its conventions, and the definition of done.

## Gates
1. Plan gate: confirm the primary form (stories, use cases or SRS) and the depth.
2. After wave 4: confirm the priorities with the decision-maker role from the brief.
3. Before wave 6: confirm with the user which sections the assembled document keeps, merges or marks n/a for this scope.

## Next
WF-T7 acceptance planning before build; WF-T6 change control after the baseline.
