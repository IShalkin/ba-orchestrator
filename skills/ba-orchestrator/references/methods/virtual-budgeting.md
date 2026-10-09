---
id: virtual-budgeting
name: "Virtual Budgeting"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 1
---

# Virtual Budgeting

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

**Also described as:** Virtual Budgeting (Prioritization Game)

## Problem Solved

Reduces 'criticality inflation' (where stakeholders mark all requested features as critical) and resolves priority conflicts by forcing realistic economic trade-offs.

## BA Lifecycle Phase

Prioritisation

## Input Artifacts

Candidate features list (Chapter S.2), estimated development effort, theoretical budget allocation rules.

## Output Artifacts

Prioritized Feature List in Chapter S.5 (categorized into Critical/Show-stopper, Important, Nice-to-have, with numerical weightings).

## Participants & Roles

Business Analyst (Facilitator), Stakeholders / Product Owner / Client Representatives (Participants).

## Prerequisites

Delimited list of proposed system features extracted from elicitation.

## Step-by-Step Procedure

Compile the list of candidate system features (S.2).
2. Provide participants with a virtual budget (e.g., $100) and set minimum/maximum investment rules per feature.
3. Instruct stakeholders to distribute their budget across features based on true business value.
4. Aggregate results across participants to compute relative importance scores.
5. Categorize features into Critical (show-stoppers), Important, and Nice-to-have.
6. Document priorities in Chapter S.5 of the System Book.
7. Validate prioritization against project feasibility and development effort with developers.

## Analyst Questions & Prompts

"If you only had $100 to buy features for the first release, how much would you spend on feature X versus feature Y? Which feature can you live without if budget gets cut by 20%?"

## Minimal Realistic Example

Stakeholders allocating $100 across 5 proposed features: 'Export to PDF' gets $45, 'Email Alerts' gets $35, while 'Dark Mode UI' gets $5, clearly marking Dark Mode as 'nice-to-have'.

## Quality Criteria & Verification

Categorization completeness (every S.2 feature has an S.5 entry); alignment between business value and development cost estimates; Product Owner endorsement.

## Errors & Anti-Patterns

Allowing stakeholders to declare everything 'Critical'; ignoring developer effort estimates; failing to document priorities before project crises occur.

## When NOT to Use

Safety-critical mandatory features where regulatory compliance makes prioritization non-negotiable.

## Alternatives & Complementary Methods

MoSCoW Method (Must/Should/Could/Won't), Kano Model Analysis, 100-Point Method, Pairwise Comparison.

## Supported Decisions

Scope slicing for sprints/releases, deferred functionality choices during schedule cuts, resource allocation.

## AI & Agentic Adaptation

Agentic systems can automatically run interactive virtual budgeting web tools, aggregate stakeholder votes, perform multi-criteria trade-off optimization, and draft S.5 priority chapters.
