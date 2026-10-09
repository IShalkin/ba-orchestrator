# WF-T2 — Situation Investigation and Elicitation

**Use when:** the problem, the scope or the real needs are unclear: a new initiative, recurring complaints, "we think we need system X", or stakeholders who describe symptoms rather than causes.
**Not when:** the requirements already exist and need specifying (use WF-T5) or checking (use WF-T7).
**Brief must contain:** the trigger (request, incident, idea), who raised it, the sources reachable in this session, and the time budget.
**Deliverables:** a problem statement, root causes, a context diagram or scope, elicitation plans and instruments (interview guides, workshop agendas, questionnaires), and elicited needs with evidence.

## Waves

### Wave 1 — Frame (parallel)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 2.1 Problem and scope | `situation-investigation-and-problem-analysis` | `project-blastoff` at project kick-off; `problem-determination-game` when stakeholders give long, conflicting symptom lists; `context-free-problem-definition-questions` for a first conversation with the requester; `cynefin` when it is unclear whether the situation is simple, complicated, complex or chaotic |
| 2.4 Domain research | `background-study` + `document-analysis` | `document-and-system-archaeology` for legacy systems with lost knowledge; `data-collection`, `activity-sampling` or `special-purpose-records` when volumes and times matter; `knowledge-reuse` when similar past projects exist |

### Wave 2 — Bound and diagnose (needs wave 1)
| 2.3 Boundaries | `context-diagram` | `rich-pictures` for messy, political, human situations; `problem-frames-and-scope-diagrams` for software-environment boundaries; `mind-mapping` to structure raw notes |
| 2.2 Root causes | `root-cause-analysis` | `five-whys` for a single causal chain; `fishbone-diagram` for multi-category causes; skip when the problem is obvious and needs an immediate fix |

### Wave 3 — Elicitation design (needs waves 1–2; stakeholder input from WF-T3 if run)
| 2.5 Individual | `information-gathering-plan`, then `interviews` (interview guide) | `questionnaires-and-surveys` for large or dispersed populations; `equivalence-classification-for-stakeholders` to sample from large groups; `repertory-grids-and-card-sorts` for tacit domain concepts; `protocol-analysis` for expert decision-making |
| 2.6 Group | `requirements-workshops` (agenda and exercises) | `focus-groups` for attitudes and adoption; `brainstorming` or `creativity-workshops-and-triggers` for solution ideas; `collaborative-games` when hidden assumptions block progress; `design-studio` for UI ideation |
| 2.7 Observation | `observation` | `shadowing-and-apprenticing` for a whole role; `ethnographic-studies` for culture over a long period. Not feasible remotely without screen sharing |
| 2.8 Make it concrete | `storyboards-and-scenarios` | `prototyping-for-elicitation` or `wireframes` when users "will know it when they see it"; `customer-journey-mapping` for customer-facing flows; `usage-centric-elicitation` to move from features to user tasks |

### Wave 4 — Elicitation results (only when transcripts, notes or recordings exist in the sources)
Run the same methods again in *analysis* mode: executors extract needs, issues and quotes from the elicitation records into the method's Output Artifacts. Without records, wave 3's instruments are the deliverable.

## Research questions (seed)
- Who raised the need, what exactly did they say, and when? (quote)
- What incidents, complaints, tickets or metrics show the problem? How often, and how costly?
- What documents describe the current process or system, and are they current?
- Which earlier attempts or analyses exist?

## Gates and checks
- **Gate after wave 2:** confirm the problem statement and scope with the user before designing elicitation.
- Every interview or workshop instrument targets named **roles**, never invented people.
- Distinguish symptoms from causes explicitly. The critic checks this against the root-cause-analysis anti-patterns.

## Hand-offs
Stakeholders → WF-T3. Elicited needs → WF-T4 (models) and WF-T5 (specification). Problem statement → WF-T1 (options, business case).
