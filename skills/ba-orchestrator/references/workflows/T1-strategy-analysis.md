# WF-T1 — Strategy Analysis and Justification

**Use when:** the question is *whether* and *why* to act: market or strategic position, goals and measures, current capabilities versus the target, solution options, investment justification.
**Not when:** scope and the business case are already approved and the work is defining requirements; use WF-T4 or WF-T5 instead.
**Brief must contain:** the decision to be made (invest / select / prioritise), the organisation or unit in scope, the time horizon, and any financial constraints.
**Deliverables:** a strategic context summary, goals and KPIs, a capability or gap view, an option long-list and short-list, and a business case.

## Waves

### Wave 1 — Context (parallel)
| Subtask | Default method | Switch to … when … |
|---|---|---|
| 1.1 External environment | `pestle-analysis` | `porters-five-forces` when the competitive dynamics of one industry dominate; `benchmarking-and-market-analysis` when there are peer data to compare against |
| 1.2 Strategy and goals | `business-objectives-vision-and-scope` | `most-analysis` when the stated mission and tactics may be misaligned; `impact-mapping` when the goal must be linked to actors and deliverables; `business-model-canvas` for a new product or business model |
| 1.3 Current state | `capability-modelling` | `popit-model` for a holistic change view (people, organisation, process, information, technology); `value-chain-analysis` or `value-streams` when the question is where value is created or lost |

### Wave 2 — Synthesis of position (needs wave 1)
| 1.1 Position | `swot-analysis` (built from the PESTLE and capability outputs) | `boston-box` for portfolio decisions; `ansoffs-matrix` for growth-direction choices |
| 1.2 Measures | `critical-success-factors-and-kpis` | `balanced-scorecard` when non-financial drivers must be balanced; `kpi-modelling-kpim` for analytics or reporting initiatives |
| 1.3 Gap | `gap-analysis` (current state against the goals) | skip when there is no current state (greenfield); see the card's When NOT to Use |

### Wave 3 — Options (needs wave 2)
| 1.4 Options | `options-identification`, then `feasibility-analysis` | `ready-made-cots-solution-selection` and `vendor-assessment` when buying is an option; `optioneering-trade-off-analysis` or `option-evaluation-and-decision-analysis` for multi-criteria choices; `force-field-analysis` when organisational resistance decides feasibility |

### Wave 4 — Business case (needs wave 3)
| 1.5 Business case | `business-case` (with `cost-benefit-analysis`, `investment-appraisal-and-financial-analysis` and `risk-analysis-and-management` as parallel inputs) | add `benefits-categorisation` when benefits are mostly intangible; `business-impact-analysis` for organisational and cultural impacts; `business-case-presentation` and `4as-communication-model` when the case must be presented |

## Research questions (seed)
- What strategy, goals, OKRs or KPIs are documented, and by whom and when?
- What market, competitor or regulatory facts are cited in the sources?
- What is the current-state capability and its known pain points (incidents, complaints, costs)?
- Which options have already been considered or rejected, and why?
- What cost, benefit or effort figures exist? Never estimate figures without labelling them `[ASSUMPTION]`.

## Gates and checks
- **Gate after wave 2:** confirm the goals and KPIs with the user before generating options. Options built on wrong goals waste the rest of the run.
- The business case must include a "do nothing" option (an anti-pattern listed in several sources).
- Every financial figure is `[E:]` or `[ASSUMPTION]` with its estimating basis.

## Hand-offs
Goals → WF-T4 (`goal-modelling-kaos-gore`), WF-T6 (prioritisation criteria). The chosen option → WF-T5 scope. Benefits → WF-T8 (`benefits-management`).
