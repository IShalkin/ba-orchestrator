# WF-T4 — Modelling and Analysis

**Use when:** needs exist but their structure is unclear: processes, data, behaviour, goals, or system decomposition. Models expose gaps and conflicts that text hides.
**Not when:** the request is a single small change that is already well understood.
**Brief must contain:** the scope (processes, systems or domains), the elicited needs or sources to model from, and the purpose of the modelling (automation, redesign, specification, integration, architecture).
**Deliverables:** the selected models (as Mermaid or tables), a glossary or data dictionary, a CRUD cross-check, a goal model, and an issues list.

## Waves

### Wave 1 — Structure (parallel; choose only what the purpose needs)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 4.1 Process | `business-process-modelling-bpmn-swimlanes` (as-is) | `business-event-analysis` first when triggers are unclear; `activity-diagrams` for detailed task logic; `task-analysis-and-task-descriptions` or `tasks-and-support` for user work at domain level; `business-use-case-buc-analysis` and `brown-cow-model` to separate essence from current implementation |
| 4.2 Data | `entity-relationship-and-data-modelling` | `concept-modelling-and-business-concept-mapping` when vocabulary conflicts dominate; `class-modelling` for OO designs; `data-flow-diagrams` for data transformations; `decision-driven-analytics-requirements` or `report-specification` for BI and reporting |
| 4.4 Goals | `goal-modelling-kaos-gore` | `rationale-and-assumptions-modelling` when gold-plating or lost rationale is the risk; `goal-domain-tracing-qfd` to check business-goal coverage |

### Wave 2 — Dynamics and cross-checks (needs wave 1)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 4.1 Improve | `process-analysis` | `process-redesign-patterns` or `business-process-improvement` when a to-be process is required |
| 4.2 Cross-check | `crud-matrix` (processes or use cases × entities) | always run it when both process and data models exist |
| 4.2 Vocabulary | `data-dictionary` | `data-expressions-bnf` for composite or message structures |
| 4.3 Behaviour | `state-machine-modelling` for entities with life cycles | `sequence-diagrams` for interactions; `real-time-behaviour-modelling-and-event-response-tables` for real-time or embedded systems; `behaviour-modelling-via-scenarios-and-state-machines` with KAOS |
| 4.4 Risks to goals | `obstacle-and-risk-analysis-ddp-fault-trees` | `goal-refinement-patterns` to complete a goal tree; `responsibility-modelling`, `goal-operationalization` and `goal-driven-object-modelling` for the full KAOS path |

### Wave 3 — Systems view (only for system-building scopes)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 4.5 Decompose | `functional-decomposition` | `interface-analysis` for integrations; `requirements-allocation-and-architectural-partitioning` for multi-subsystem products; `domain-and-analysis-object-modelling` and `object-oriented-requirements-analysis-with-contracts` for OO analysis; `change-case-modelling` for anticipated change |
| 4.6 Architecture | `quality-attribute-workshop-qaw` → `quality-attribute-utility-tree` | `palm-business-goals-for-architecture` to tie architecture to business goals; `attribute-driven-design-add` for design; `atam` or `lightweight-architecture-evaluation` to evaluate a design; `tactics-based-questionnaires` for quick risk discovery; `architecture-debt-analysis` for refactoring decisions |

## Research questions (seed)
- Which process descriptions, regulations, screens, reports or data schemas exist? (They are the inputs for models.)
- What entities, states and status values appear in tickets, APIs and databases?
- Where do sources disagree on terms (the same word with different meanings)?

## Gates and checks
- Every model element traces to `[E:]` evidence or is marked `[ASSUMPTION]`.
- As-is and to-be models are kept separate and labelled.
- The CRUD cross-check results (orphan entities, missing events) go to the synthesizer as gaps.

## Hand-offs
Models → WF-T5 (use cases, rules, NFRs derive from them), WF-T7 (model-based validation). Glossary → every later artifact.
