---
id: value-cost-prioritization-ahp
name: "Value-Cost Prioritization (AHP)"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 2
---

# Value-Cost Prioritization (AHP)

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

**Also described as:** Requirements Prioritization (Value-Cost / AHP); Requirements Prioritization (Value-Cost AHP)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces budget overruns, missed deadlines, and unmanaged scope creep by ordering requirements for phased/incremental release under limited resources.

**[Variant B]**

Reduces project failure risks due to budget overruns or missed deadlines by ranking independent requirements into relative priority levels for phased release planning.

## BA Lifecycle Phase

**[Variant A]**

Prioritisation / change management

**[Variant B]**

Prioritisation

## Input Artifacts

**[Variant A]**

Elicited independent requirements/goals at comparable granularity, project cost estimates, business value criteria.

**[Variant B]**

Candidate requirements list (at uniform granularity), value and cost criteria.

## Output Artifacts

**[Variant A]**

Pairwise comparison matrices, normalized value/cost distribution percentages, Value-Cost priority diagrams (High, Medium, Low priority tiers).

**[Variant B]**

AHP pairwise comparison matrices, value/cost percentage allocations, value-cost scatter plot, prioritized release tiers.

## Participants & Roles

**[Variant A]**

BA, Product Manager, Sponsor, Customer, Lead Developer/Architect.

**[Variant B]**

Business Analyst, Product Manager, Customer / User Representatives, Lead Developer / Architect.

## Prerequisites

**[Variant A]**

Requirements are well-defined, comparable in granularity, and mutually independent.

**[Variant B]**

Comparable, independent requirements list; cost estimates from developers and value estimates from customers.

## Step-by-Step Procedure

**[Variant A]**

Select comparable and independent requirements.
2. Apply Analytic Hierarchy Process (AHP) for Value: (a) Perform pairwise comparisons of requirements on a 1-9 scale of relative value; (b) Construct n x n matrix and compute reciprocals; (c) Normalize columns and average across rows to get relative value % for each requirement.
3. Repeat AHP for Cost (using developer estimates) to get relative cost % for each requirement.
4. Plot requirements on a Value-Cost diagram (x=Cost %, y=Value %).
5. Partition diagram into priority tiers (High, Medium, Low) in consultation with stakeholders.

**[Variant B]**

Verify that candidate requirements are at similar levels of abstraction and independent.
2. Apply AHP Step 1 (Value): Construct a pairwise comparison matrix (1-9 scale) estimating relative customer value between requirement pairs.
3. Apply AHP Step 2 (Value): Normalize matrix columns and average rows to derive the percentage value contribution of each requirement.
4. Apply AHP Steps 1 & 2 (Cost): Repeat the pairwise comparison process with developers estimating relative implementation cost to derive cost percentages.
5. Plot each requirement on a Value-Cost diagram (x=Cost %, y=Value %).
6. Partition the diagram into High, Medium, and Low priority tiers and negotiate final release increments with stakeholders.

## Analyst Questions & Prompts

**[Variant A]**

Does Requirement A contribute slightly, strongly, or extremely more value than Requirement B? What is the relative implementation cost of Requirement A vs B?

**[Variant B]**

Does requirement R1 contribute slightly, strongly, or extremely more to customer value than requirement R2? What is the relative implementation cost of R1 compared to R2?

## Minimal Realistic Example

**[Variant A]**

Prioritizing 5 scheduler features using AHP, revealing 'Produce Optimal Dates' (49% value, 18% cost -> High Priority) vs 'Multi-lingual Support' (5% value, 22% cost -> Low Priority).

**[Variant B]**

Applying AHP to 5 meeting scheduler features shows 'Produce Optimal Dates' yields 49% of total value for 20% of cost (High Priority), while 'Multilingual Support' yields 4% value for 22% cost (Low Priority).

## Quality Criteria & Verification

**[Variant A]**

Transitivity and consistency ratio check on pairwise comparison matrices; stakeholder agreement on priority tiers.

**[Variant B]**

AHP consistency ratio check (must be within acceptable mathematical thresholds); stakeholder agreement on release boundaries.

## Errors & Anti-Patterns

**[Variant A]**

Comparing items at different granularity levels; prioritizing dependent requirements independently; subjective ad-hoc ranking without cost vs value balancing.

**[Variant B]**

Comparing items at mismatched granularities (e.g., a whole subsystem vs a button tweak); treating non-independent requirements as separate; using overly granular quantitative scales (e.g., 100 priority levels).

## When NOT to Use

**[Variant A]**

When all requirements are strictly mandatory legally, or when the total project scope is extremely small and fully funded.

**[Variant B]**

When all requirements are strictly mandatory for legal/safety reasons, or in micro-projects with very few simple features.

## Alternatives & Complementary Methods

**[Variant A]**

MoSCoW method, Group brainstorming/voting, Goal-model-based prioritization.

**[Variant B]**

Complementary: Goal Model Refinement. Alternative: Simple Qualitative Group Ranking (High/Medium/Low), MoSCoW.

## Supported Decisions

**[Variant A]**

Release planning, budget allocation, scope pruning during change management.

**[Variant B]**

Release planning, scope reduction, budget allocation, conflict resolution by dropping low-priority items.

## AI & Agentic Adaptation

**[Variant A]**

AHP prioritization algorithms can be embedded in BA tools to calculate consistency ratios automatically, flag intransitive stakeholder ratings, and auto-plot Value-Cost matrices.

**[Variant B]**

AI agents can pre-calculate AHP matrices from raw stakeholder feedback logs, perform mathematical consistency ratio validation, and plot automated value-cost release charts.
