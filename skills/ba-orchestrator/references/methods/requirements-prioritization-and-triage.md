---
id: requirements-prioritization-and-triage
name: "Requirements Prioritization and Triage"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 3
---

# Requirements Prioritization and Triage

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

**Also described as:** Prioritisation & Triage; Prioritization; Prioritizing Requirements (Relative Weighting, MoSCoW, Criteria Matrix)

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Reduces conflict and resource waste by determining the relative importance and implementation order of business analysis information based on value, risk, and constraints.

**[Variant B]**

Resolves conflicting stakeholder demands, aligns development sequence with budget/time constraints, and ensures maximum business value delivery.

**[Variant C]**

Prevents project overruns and failure by making hard, realistic choices on what features to build, defer, or reject based on stakeholder value, technical cost, and risk.

## BA Lifecycle Phase

**[Variant A]**

prioritisation / planning / Requirements Life Cycle Management

**[Variant B]**

Analysis / Prioritisation / Backlog Management

**[Variant C]**

Prioritisation / Change Management

## Input Artifacts

**[Variant A]**

Unprioritized requirements/backlog, business goals, risk logs, cost estimates, dependencies.

**[Variant B]**

Product Backlog, Use Cases, User Stories, Quality Attributes, Business Objectives, Risk assessments, Cost/effort estimates.

**[Variant C]**

Candidate goals/requirements, stakeholder preferences, cost/risk estimates from design options, dependency links

## Output Artifacts

**[Variant A]**

Prioritized requirements/designs (ranked, grouped, or budgeted).

**[Variant B]**

Prioritized Backlog / Requirements List, Pairwise Quality Attribute Matrix, Relative Weighting / Criteria Matrix Spreadsheets, MVP definition.

**[Variant C]**

Input priority ratings (MoSCoW, 9-3-2-1, monetary allocation), Output priority ratings (release roadmap, Cherry Stones phase assignments, release matrices)

## Participants & Roles

**[Variant A]**

BA, Product Owner/Sponsor, Customer, SME, Developer, Project Manager.

**[Variant B]**

Empowered Decision Makers / Product Owner, Business Analyst (facilitator), Key Stakeholders, Development Team (cost/risk estimators).

**[Variant C]**

BA, Product Manager, Sponsor, Architect, Lead Developer, Customer Representative

## Prerequisites

**[Variant A]**

Agreed prioritization criteria (benefit, penalty, cost, risk, dependencies, urgency).

**[Variant B]**

Items at a consistent level of granularity with cost/benefit estimates.

**[Variant C]**

List of discovered candidate requirements, estimated costs/risks from candidate designs, and identified requirement dependencies.

## Step-by-Step Procedure

**[Variant A]**

Agree on prioritization basis/criteria with key stakeholders (e.g., value, risk, cost).
2. Select prioritization approach: Grouping (High/Med/Low), Ranking (1 to N), Time-boxing/Budgeting, or Negotiation.
3. Evaluate requirements against selected basis and dependencies.
4. Facilitate stakeholder consensus and trade-off discussions.
5. Sequence requirements in order of priority.
6. Re-evaluate priorities continually as business context and constraints change.

**[Variant B]**

Identify empowered decision-makers and agree on prioritization criteria (value, urgency, cost, risk, compliance).
2. Select a prioritization method suited to the item count (MoSCoW, Three-level scale, Stack ranking, Pairwise comparison, WSJF, or Criteria Matrix).
3. Evaluate candidate requirements against established criteria (rating value/penalty, cost, risk on numeric scales).
4. Calculate relative priority scores or rank order items.
5. Sequence requirements into releases or development iterations based on dependencies and capacity.
6. Communicate rationale and priorities to all stakeholders.

**[Variant C]**

Determine input priority (value to stakeholders) using techniques like voting, $100 allocation, or card sorting.
2. Perform Input Triage: reject or defer low-value goals.
3. Map requirement dependencies (scenario and infrastructural dependencies) to ensure dependent items share priority.
4. Evaluate cost, technical risk, and design feasibility (supply side).
5. Perform Output Triage (Optioneering): allocate high-value, feasible requirements into release phases (e.g., Phase 1, Phase 2, Future, Never).
6. Publish the baseline release roadmap.

## Analyst Questions & Prompts

**[Variant A]**

"Which requirements deliver the highest value relative to cost?", "What is the penalty for not implementing feature X in this release?", "Which technical dependency requires requirement A to precede requirement B?"

**[Variant B]**

"What would you do if that feature weren't present?", "Is there a manual or automated workaround?", "What would be the cost or risk to the business if this feature were delayed or omitted?", "Which quality attribute is more critical: Security or Usability?"

**[Variant C]**

How important is this to the stakeholder? What happens if we do not include this in Phase 1? What infrastructure does this feature depend on? Can this requirement be deferred safely?

## Minimal Realistic Example

**[Variant A]**

A team uses MoSCoW grouping to classify 20 release features: 8 Must Haves, 6 Should Haves, 4 Could Haves, and 2 Won't Haves for current budget.

**[Variant B]**

Using a Criteria Matrix, 8 proposed features are rated across weighted criteria (Business Value 25%, Usage Frequency 20%, Cost 15%, Technical Risk 15%, Time Sensitivity 15%). Feature 1 scores highest (4.3) and is scheduled for Release 1, while Feature 5 scores lowest (1.2) and is deferred.

**[Variant C]**

A software team uses MoSCoW to grade input priorities, groups features by infrastructural dependency (e.g., 'User Login' must precede 'Saved Preferences'), and assigns output priorities: 'Phase 1' (Now), 'Phase 2' (Later).

## Quality Criteria & Verification

**[Variant A]**

Stakeholder consensus achieved on top priorities; prioritization criteria transparent and consistently applied; technical dependencies respected.

**[Variant B]**

Only items at similar levels of granularity are compared; cost and technical difficulty are evaluated by technical staff; decision rationale is transparent and linked to business objectives.

**[Variant C]**

Consistency across dependent requirements, balanced distribution of priorities (avoiding '100% Mandatory'), stakeholder and dev team alignment.

## Errors & Anti-Patterns

**[Variant A]**

Classifying 100% of requirements as 'High' priority; allowing vocal stakeholders to manipulate priorities without objective criteria.

**[Variant B]**

Classifying everything as 'High Priority'; letting the loudest voice dictate priority; ignoring technical dependencies or cost when ranking value; prioritizing hundreds of fine-grained items simultaneously.

**[Variant C]**

Labeling all requirements as 'Mandatory/Must Have'; prioritizing individual features without accounting for infrastructure dependencies; ignoring dev cost/risk during prioritization.

## When NOT to Use

**[Variant A]**

When all requirements are legally mandatory with unlimited budget and fixed hard deadline.

**[Variant B]**

When there is only one requirement, or when capacity far exceeds total request volume.

**[Variant C]**

When the project scope, budget, and implementation timeline are infinite or strictly fixed with a single monolithic release.

## Alternatives & Complementary Methods

**[Variant A]**

Complemented by Backlog Management, Decision Analysis, MoSCoW, Kano Analysis, and Financial Analysis.

**[Variant B]**

Complementary: Practice #2 Business Objectives, Practice #5 Decision Makers, Practice #19 Baselines. Alternatives: Kano Model, WSJF, Buy-a-Feature.

**[Variant C]**

MoSCoW, Cherry Stones method, Boston Matrix (Cost-Benefit Analysis), Analytic Hierarchy Process (AHP), QFD.

## Supported Decisions

**[Variant A]**

Release scope planning, budget allocation, iteration backlog ordering.

**[Variant B]**

Release scope allocation, iteration backlog order, MVP feature selection, trade-off choices during schedule pressure.

**[Variant C]**

Release planning, budget allocation, baseline scope sign-off, supplier contract negotiations.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can auto-score requirements against multi-criteria risk/value algorithms, presenting ranked backlogs for Product Owner review.

**[Variant B]**

AI agents can run initial prioritization models (WSJF, Criteria Matrix) by ingesting historical velocity, cost estimates, and tag metadata, suggesting backlog orderings and highlighting potential dependency locks for human review.

**[Variant C]**

Agentic dependency and roadmap optimization: AI algorithms analyze requirement dependency graphs, stakeholder weights, and cost/risk estimates to generate optimized release roadmaps, subject to human product manager approval.
