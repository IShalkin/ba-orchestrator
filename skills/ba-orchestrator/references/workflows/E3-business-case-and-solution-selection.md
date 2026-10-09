# WF-E3 — Business Case and Solution Selection (problem → options → recommended option with justification)

**Use when:** management must decide whether to invest and in which option: build, buy (COTS or vendor), change the process, or do nothing.
**Composes:** T1 (context, options, business case) + T5.5 (the key NFRs as selection criteria) + T3 (decision-makers) + T7.4 (acceptance criteria for a purchase).
**Deliverables:** strategic context, an option long-list and short-list, an evaluation matrix, a vendor or COTS assessment (if buying), a business case with financials and risks, and a decision memo.

## Waves
| Wave | Executors (parallel inside a wave) | Depends on |
|---|---|---|
| 1 | `swot-analysis` (or `pestle-analysis` when the external context is unknown) · `gap-analysis` · `empowered-decision-makers-and-decision-rules` | research |
| 2 | `options-identification` (must include "do nothing") · `non-functional-requirements-analysis` (selection-critical qualities only) | 1 |
| 3 | `feasibility-analysis` · `ready-made-cots-solution-selection` + `vendor-assessment` (if buying) · `option-evaluation-and-decision-analysis` | 2 |
| 4 | `cost-benefit-analysis` · `investment-appraisal-and-financial-analysis` · `risk-analysis-and-management` · `benefits-categorisation` | 3 |
| 5 | `business-case` (assembles waves 3–4) · `business-case-presentation` (when the case must be presented) | 4 |

## Gates
1. After wave 2: confirm the option long-list and the evaluation criteria and weights with the decision-maker role.
2. Financial inputs: every figure is `[E:]` or a labelled `[ASSUMPTION]` with a sensitivity range. Never present a single point estimate as fact.

## Next
The chosen option → WF-E2 (specify) or the WF-T5 tender form (SRS / PEGS); benefits → WF-T8.
