# WF-T5 — Requirements Specification

**Use when:** the scope is agreed and needs must become precise, testable requirements: user stories, use cases, business rules, NFRs, a specification document, examples and acceptance criteria.
**Not when:** the problem or scope is still open (use WF-T2 first), or the task is only to audit an existing specification (use WF-T7 or WF-E4).
**Brief must contain:** the scope and the agreed needs (or the sources containing them), the delivery style (agile backlog, traditional SRS, regulated or contractual), the audience (developers, testers, vendor), and whether formal methods are required.
**Deliverables:** a requirements set in the chosen form, business rules and decision tables, NFRs with measurable targets, acceptance criteria and examples, and a glossary.

## Choosing the form (decide in the plan)
| Context | Primary form | Companion |
|---|---|---|
| Agile, iterative delivery | `user-stories` + `user-story-mapping` | `story-workshop-three-amigos`, `the-3-cs-card-conversation-confirmation`, `specification-by-example` |
| Complex multi-step interactions, many exceptions | `use-cases` (goal levels; `base-use-case-description` → `elaborated-use-case-description`) | `use-case-relationships-extend-include-generalization`, `instance-scenario-modelling` |
| Contract, tender, vendor or regulated delivery | `requirements-specification-templates-srs` or `pegs-standard-plan` | `ears`, `requirement-writing-patterns`, `feature-requirements` |
| Safety- or mission-critical behaviour | `formal-specification-overview-ltl-z-scr` (pick `z-specification` / `real-time-temporal-logic-ltl` / `scr-event-based-specification`) | `formal-picnic` as a bridge from natural language; `abstract-data-type-adt-specification`, `algebraic-specification` |

## Waves

### Wave 1 — Functional core and vocabulary (parallel)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 5.1 / 5.2 Functional | the primary form chosen above | `scenario-based-requirements-analysis` or `scenarios-and-storyboards-for-specification` to derive requirements from scenarios; `business-use-case-modelling` / `initial-conceptual-use-case-modelling` at the business level first |
| 5.6 Vocabulary | `glossary` | — (always) |
| 5.4 Rules | `business-rules-analysis` | `decision-tables-and-decision-trees` for condition combinations; `decision-modelling` to externalise decision logic; `textual-process-descriptions-mini-specs` for algorithms; `tabular-requirement-representation` for repetitive requirement sets |

### Wave 2 — Qualities and interface (parallel; needs wave 1)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 5.5 NFR | `non-functional-requirements-analysis` | `quality-attribute-scenarios` for architecture hand-off; `planguage` or `open-metric-and-open-target` for measurable targets; `quality-grid` to choose which qualities matter; `security-risk-assessment`, `roles-and-permissions-matrix` and `standards-as-requirements` as the domain requires |
| 5.3 UI (only if a UI is in scope) | `screens-and-prototypes` | `virtual-windows` or `conceptual-user-interface-design` before detailed screens; `dialog-map` for navigation; `display-action-response-dar-model` for screen behaviour; `keystroke-level-model-klm` for efficiency targets |

### Wave 3 — Testability (needs waves 1–2)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 5.7 Acceptance | `acceptance-and-fit-criteria` | `specification-by-example` (key examples, Given-When-Then) when the business rules are example-rich |
| 5.6 Phrasing pass | `ears` / `requirement-writing-patterns` over every textual requirement | `development-process-requirements` when uncertainty is so high that you specify the process instead of the product |
| 5.8 Trace to sources (only when the request compares the requirements with named sources) | `requirements-traceability` | — |

### Wave 4 — Assemble (needs wave 3; runs after SYNTHESIZE, see SKILL.md step 4b)
One executor assembles the document in the chosen template, referencing the artifacts. Never re-write their content in it.

| Brief's deliverable format | Template card |
|---|---|
| A requirements document for a team that designs the solution itself | `requirements-specification-templates-srs` or `pegs-standard-plan` |
| One review-ready document covering requirements and the solution design (design sign-off, hand-off to a vendor or delivery team, go-live readiness) | `consolidated-solution-design-document` |

The assembler also receives the synthesis outputs (`traceability.csv`, `open-questions.md`, `assumptions.md`, `conflicts.md`). They feed the traceability, risks and open-items sections. Sections with no feeding artifact are marked as gaps, never filled with invented design.

## Research questions (seed)
- Which agreed needs, decisions or epics exist, with their status? Use only approved or current ones as the baseline.
- Which business rules, policies, laws or calculation formulas apply (quote them)?
- Which quality expectations are stated (response time, availability, security, compliance)? Are any numbers given?
- Which interfaces, screens or reports already exist?

## Gates and checks
- Every requirement has an id, a source (`[E:]` or a link to a model or artifact), and acceptance criteria.
- No vague qualifiers ("fast", "user-friendly") without a measurable target. The critic checks this against the NFR and phrasing cards.
- UI detail is kept out of business rules and use case steps (anti-pattern in the use-cases and business-rules cards).
- The assembled document marks every section complete, partial (with reason) or n/a (with reason). The critic checks each section against the template card's Quality Criteria (for the consolidated document: the reviewer focus of each section).

## Hand-offs
The requirements set → WF-T6 (prioritise, baseline, trace) and WF-T7 (review, test).
