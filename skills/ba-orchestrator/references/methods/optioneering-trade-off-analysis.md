---
id: optioneering-trade-off-analysis
name: "Optioneering (Trade-Off Analysis)"
task: T1
task_name: "Strategy Analysis and Justification"
subtask: "1.4"
subtask_name: "Solution Options and Feasibility"
source_count: 1
---

# Optioneering (Trade-Off Analysis)

`T1 Strategy Analysis and Justification › 1.4 Solution Options and Feasibility`

## Problem Solved

Selects the optimal system design architecture among competing alternatives that best satisfies conflicting stakeholder requirements within cost, risk, and technical limits.

## BA Lifecycle Phase

Analysis / Prioritisation / Design Selection

## Input Artifacts

Input-prioritized stakeholder goals, proposed design options, engineering cost/risk estimates, evaluation criteria

## Output Artifacts

Trade-off evaluation matrix, QOC diagrams, Principal Component Analysis (PCA) biplots, output-prioritized product specification, baseline design selection rationale

## Participants & Roles

BA, Chief Architect, Systems Engineer, Product Manager, Sponsor, Domain Experts

## Prerequisites

Validated stakeholder goals (criteria) and candidate technical design options.

## Step-by-Step Procedure

Document input stakeholder goals (criteria).
2. Identify distinct technical design options (e.g., tram vs. subway vs. cablecar).
3. Convert goals into measurable evaluation criteria.
4. Score each design option against each criterion (quantitatively or via qualitative +/0/- scales).
5. Triage out options that fail mandatory constraints (e.g., safety limits).
6. Use qualitative decision frameworks (QOC, QFD) or statistical methods (PCA) to evaluate remaining options.
7. Select the winning design option through team/sponsor consensus.
8. Adjust requirements to match the capabilities of the winning design (setting output priorities).

## Analyst Questions & Prompts

Which design option best satisfies our top-priority goals? What are the cost, risk, and performance trade-offs of Option A versus Option B? Can we afford this design choice?

## Minimal Realistic Example

An urban transport project uses PCA to evaluate four transit options across 11 criteria (cost, capacity, safety, traffic impact). While a subway scores highest on capacity, its prohibitive construction cost causes it to be triaged out in favor of an aerial cablecar.

## Quality Criteria & Verification

Traceability of trade-off criteria to stakeholder goals, objective scoring validated by domain experts, mathematical validity of trade-off models (avoiding arbitrary naive weighting).

## Errors & Anti-Patterns

Using arbitrary weighted scoring to add 'apples and oranges'; solutioneering (picking a favorite design before evaluating requirements); failing to triage out unsafe options.

## When NOT to Use

When only one technical solution is feasible or pre-mandated by law/policy.

## Alternatives & Complementary Methods

QOC (Questions, Options, Criteria), QFD (Quality Function Deployment), PCA (Principal Component Analysis), Cost-Benefit Analysis, AHP.

## Supported Decisions

System architecture selection, vendor selection, release scope baseline, output priority assignment.

## AI & Agentic Adaptation

Agentic trade-off optimization: AI algorithms execute Principal Component Analysis (PCA) and multi-objective optimization across complex requirement/design option matrices, generating visual decision biplots and tradeoff summaries for executive review.
