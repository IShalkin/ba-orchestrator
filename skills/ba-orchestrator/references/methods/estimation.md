---
id: estimation
name: "Estimation"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.2"
subtask_name: "Backlog, Estimation and Release Planning"
source_count: 2
---

# Estimation

`T6 Prioritisation and Requirements Management › 6.2 Backlog, Estimation and Release Planning`

**Also described as:** Requirements Effort Estimation (Three-Pronged Approach)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces budget and timeline forecasting uncertainty by using structured, mathematical, or expert-driven techniques to predict cost, effort, and duration.

**[Variant B]**

Prevents schedule underestimation and 'Betty's corner' pressure by triangulating BA effort using historical metrics and project sizing factors.

## BA Lifecycle Phase

**[Variant A]**

Planning / prioritisation / strategy / Solution Evaluation

**[Variant B]**

prioritisation

## Input Artifacts

**[Variant A]**

Work Breakdown Structure (WBS), user stories, scope models, historical project performance data.

**[Variant B]**

Count of project deliverables (process flows, screens, reports), total project budget, developer staff counts, project type, historical project effort data

## Output Artifacts

**[Variant A]**

Cost/effort estimates, confidence intervals (ROM or definitive ranges), estimation assumptions.

**[Variant B]**

BA Effort Estimate Spreadsheet Report (comparing % of Total Effort, Developer-to-BA Ratio, and Activity-Based Estimates)

## Participants & Roles

**[Variant A]**

BA, Project Manager, Developer, Tester, Implementation SME, Estimator.

**[Variant B]**

BA, Project Manager, Development Lead

## Prerequisites

**[Variant A]**

Decomposed work scope (WBS or feature list) and agreed estimation method.

**[Variant B]**

High-level understanding of project scope and planned deliverable counts.

## Step-by-Step Procedure

**[Variant A]**

Decompose scope into estimable work elements (WBS or backlog).
2. Select estimation method (Top-down, Bottom-up, Parametric, PERT, Delphi, ROM, Rolling Wave).
3. Gather historical performance data and consult experts.
4. Compute estimates and establish confidence intervals (ranges, e.g., PERT = (O + 4M + P)/6).
5. Document all underlying assumptions, risks, and constraints.
6. Revisit and refine estimates continuously as work progresses and uncertainty drops.

**[Variant B]**

Calculate Estimate 1: Allocate ~15% of total project effort/budget to BA requirements work.
2. Calculate Estimate 2: Apply a Developer-to-BA staffing ratio (~6:1 for custom, 3:1 for COTS).
3. Calculate Estimate 3: Perform bottom-up activity estimation based on counts of process flows, user stories, screens, and reports multiplied by historical activity hours.
4. Compare results across the three prongs on the summary spreadsheet.
5. Reconcile disconnects and adjust assumptions based on team experience or remote work factors.
6. Timebox or adjust scope if available BA hours fall short of estimated needs.

## Analyst Questions & Prompts

**[Variant A]**

"What is the optimistic, most likely, and pessimistic effort for task X?", "What historical data do we have for similar work?", "What confidence interval applies to this ROM estimate?"

**[Variant B]**

What is the expected ratio of developers to BAs on this project type? How many screens, process flows, and reports do we anticipate creating? How does our bottom-up estimate compare to 15% of total project work?

## Minimal Realistic Example

**[Variant A]**

Using PERT for a module design: Optimistic = 4 days, Most Likely = 6 days, Pessimistic = 14 days -> PERT Estimate = (4 + 24 + 14)/6 = 7 days.

**[Variant B]**

Estimating a custom project with 5 developers and 8 process flows / 8 screens / 4 reports yields  ~~0.8 BAs (~~  $77k-$ 113k budget), providing data to defend an 8-week analysis timeline.

## Quality Criteria & Verification

**[Variant A]**

Estimates express ranges/confidence intervals rather than single point figures; underlying assumptions are explicitly documented; history calibrates estimates.

**[Variant B]**

Reconciliation and convergence among the three independent estimation prongs; tracking actual hours against estimates to refine future baseline assumptions.

## Errors & Anti-Patterns

**[Variant A]**

Treating early Rough Order of Magnitude (ROM) estimates as fixed binding commitments; relying on single-person uncalibrated guesses.

**[Variant B]**

Giving top-of-the-head guesses ('got an hour?'); treating initial uncertain estimates as fixed promises; swaying estimates to match arbitrary management deadlines.

## When NOT to Use

**[Variant A]**

When scope is completely undefined with zero domain knowledge (conduct exploratory experiments first).

**[Variant B]**

None; necessary when planning requirements resource allocation for any project.

## Alternatives & Complementary Methods

**[Variant A]**

Complemented by Functional Decomposition, Relative Estimation (Story Points), PERT, and Financial Analysis.

**[Variant B]**

Story Point Estimation, Function Point Analysis, Use Case Points.

## Supported Decisions

**[Variant A]**

Project budgeting, iteration/release scheduling, resource allocation, business case justification.

**[Variant B]**

Project planning, staffing allocation, schedule commitments, release scope.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can analyze historic code commits or Jira ticket completion times to generate automated parametric effort estimates with probabilistic confidence bands.

**[Variant B]**

Not in source
