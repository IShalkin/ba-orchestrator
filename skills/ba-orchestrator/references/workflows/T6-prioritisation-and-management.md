# WF-T6 — Prioritisation and Requirements Management

**Use when:** there are more requirements than capacity, scope keeps growing, changes arrive without impact analysis, or there is no traceability or baseline.
**Not when:** nothing has been elicited or specified yet (use WF-T2 or WF-T5 first).
**Brief must contain:** the requirement set or backlog location, the capacity or deadline constraints, who decides priorities (see WF-T3), and the change process if one exists.
**Deliverables:** a prioritised set with its rationale, a release or backlog plan, estimates, a baseline, a traceability matrix, a change-control procedure, and an impact analysis of pending changes.

## Waves

### Wave 1 — Prioritise (parallel)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 6.1 Prioritise | `moscow` for a fixed timebox | `value-cost-risk-prioritization-matrix` or `value-cost-prioritization-ahp` for analytical ranking; `requirements-prioritization-and-triage` for overloaded scope; `virtual-budgeting` when every stakeholder marks everything critical; `quality-attribute-prioritization-grid` for competing qualities; `timeboxing` to flex scope against fixed dates |
| 6.2 Estimate | `estimation` | `planning-poker` for team-relative sizing |

### Wave 2 — Plan and baseline (needs wave 1)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 6.2 Plan | `product-backlog-management` | `dependency-stream-analysis` for large models with dependencies |
| 6.3 Baseline | `requirements-baselines-and-version-control` | `requirements-organisation-and-management` for large unstructured sets; `requirements-reuse` across products; `unified-pegs-lifecycle` or `development-case-customization` to tailor the process |
| 6.4 Trace | `requirements-traceability`, with the fixed `trace.csv` columns (run-protocol §8); split by capability when large and merge with `merge_trace.py` | `requirements-status-tracking` and `issue-and-item-tracking` when status reporting is unreliable |

### Wave 3 — Control change (needs wave 2)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 6.5 Change | `change-control` (procedure) | `change-impact-analysis` for each pending change request |
| 6.6 Risk and process | `requirements-risk-management` | `requirements-process-self-assessment` when the process itself fails repeatedly |

## Research questions (seed)
- Where is the backlog or requirement set, how many items does it have, and what are their status and priority fields?
- What capacity, velocity, budget or deadline figures exist?
- Which change requests are pending, and who raised them? What do they affect?
- Which links already exist between requirements, design, code and tests (Jira links, test management tools, repo references)?

## Gates and checks
- The prioritisation rationale names its criteria and who applied them. Priorities are never invented. An agent may propose a ranking, but it is labelled `[ASSUMPTION]` until a decision-maker confirms it.
- The traceability matrix lists orphans (requirements without a source or test) explicitly.
- Impact analysis covers requirements, design, code, tests, documentation, schedule and cost. Unknown items are marked `[GAP]`.

## Hand-offs
The baseline → WF-T7 (validation against the baseline). The change procedure → WF-T8 (deployment governance). Once a baseline exists, a weekly or ad-hoc re-check against changed sources → WF-R1, whose drift report comes back to wave 3 (6.5) as change requests.
