# WF-T8 — Change Deployment and Solution Evaluation

**Use when:** a solution is going live or has gone live, and the questions are about people, organisation and benefits: readiness, resistance, training, benefits tracking, lessons learned, and runtime monitoring.
**Not when:** the solution has not been defined yet.
**Brief must contain:** what changes, for whom and when; the benefits promised (from the business case); the deployment approach; and post-implementation data (if any).
**Deliverables:** a cultural and change-readiness assessment, a change plan, a people transition and training plan, a benefits plan and a benefits realisation review, lessons learned, and a monitoring plan.

## Waves

### Wave 1 — Readiness (parallel)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 8.1 Organisation | `cultural-analysis` | — |
| 8.1 Change approach | `kotters-8-steps` for large transformations | `lewins-change-model` for bounded changes (unfreeze, change, refreeze) |
| 8.2 People | `sarah-model` (emotional journey by affected group) | — |

### Wave 2 — Enable (needs wave 1)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 8.2 Learning | `learning-cycle` | `conscious-competence-model` to stage training and support |
| 8.3 Benefits plan | `benefits-management` | — |

### Wave 3 — Evaluate (only after go-live, with real data)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 8.3 Realisation | `benefits-realisation` | — |
| 8.3 Learn | `lessons-learned` | — |
| 8.3 Monitor | `runtime-requirements-monitoring` | when environment assumptions may break at runtime |

## Research questions (seed)
- Which benefits, KPIs and targets were promised, and where? (business case, charter)
- Which groups are affected, and how? What resistance or adoption signals exist (surveys, tickets, usage data)?
- What training, support or communication plans exist?
- After go-live: which actual metrics exist for the promised benefits?

## Gates and checks
- Every benefit has an owner role, a metric, a baseline, a target and a measurement date. Missing items are marked `[GAP]`.
- Benefits realisation compares against the *promised* figures (`[E:]` from the business case), never against figures invented after the fact.
- Lessons learned name causes and actions, not blame.

## Hand-offs
Lessons and monitoring findings → WF-T6 (`change-control`, `requirements-process-self-assessment`) and the next WF-T1 cycle.
