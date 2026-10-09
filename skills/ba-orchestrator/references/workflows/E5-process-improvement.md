# WF-E5 — Process Improvement (as-is → causes → to-be → gaps → change plan)

**Use when:** an operational process is slow, error-prone, costly or frustrating, and the goal is to redesign it (with or without new software).
**Composes:** T2 (observe, measure, root causes) + T4.1 (process models) + T1.3 (gaps) + T5.4 (rules) + T8 (change).
**Deliverables:** an as-is process model with measured pain points, root causes, a to-be process, a gap list (people, process, information, technology), business rules, a change and transition plan, and benefit KPIs.

## Waves
| Wave | Executors (parallel inside a wave) | Depends on |
|---|---|---|
| 1 | `business-process-modelling-bpmn-swimlanes` (as-is) · `observation` plan or analysis · `data-collection` / `activity-sampling` (volumes and times, when data exist) | research |
| 2 | `root-cause-analysis` · `process-analysis` · `business-rules-analysis` (rules embedded in the as-is process) | 1 |
| 3 | `process-redesign-patterns` → to-be model (`business-process-modelling-bpmn-swimlanes` with scope suffix `--to-be`) | 2 |
| 4 | `gap-analysis` (as-is vs to-be) · `popit-model` (the change dimensions) · `critical-success-factors-and-kpis` (benefit measures) | 3 |
| 5 | `lewins-change-model` or `kotters-8-steps` · `sarah-model` (affected roles) · `benefits-management` | 4 |

Switching rule: when the redesign covers a whole business area or a chain of interlinked processes rather than one process, use `process-hierarchy-process-design-and-end-to-end-scenarios` in wave 1 (as-is) and wave 3 (to-be) instead of a single `business-process-modelling-bpmn-swimlanes` model. Run the root-cause and gap work per process group, and keep the end-to-end scenarios as the check that handoffs between processes still work after the redesign.

## Gates
1. After wave 2: confirm the root causes with the process-owner role, so that the redesign does not treat symptoms.
2. After wave 3: confirm the to-be process before the gap analysis and change planning.
