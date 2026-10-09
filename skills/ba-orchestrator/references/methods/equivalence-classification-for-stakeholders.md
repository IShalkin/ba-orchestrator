---
id: equivalence-classification-for-stakeholders
name: "Equivalence Classification for Stakeholders"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.5"
subtask_name: "Interviews, Questionnaires and Individual Techniques"
source_count: 1
---

# Equivalence Classification for Stakeholders

`T2 Situation Investigation and Elicitation › 2.5 Interviews, Questionnaires and Individual Techniques`

## Problem Solved

Reduces the time and cost of interviewing large populations of process workers without risking loss of representative operational requirements or variance data.

## BA Lifecycle Phase

Elicitation / Planning

## Input Artifacts

Stakeholder list, organizational charts, process worker demographics, system usage logs.

## Output Artifacts

Process Worker Classification Matrix, optimized Information-Gathering Plan (IGP).

## Participants & Roles

Business Analyst (planner), Business Unit Managers, Process Workers.

## Prerequisites

Identification of a large user/process worker population associated with the problem domain.

## Step-by-Step Procedure

Identify key usage attributes/dimensions across the process worker population (e.g., work shift, job tenure, frequency of system usage).
2. Construct a multi-dimensional matrix combining these classification attributes.
3. Map the total worker population into the intersecting matrix cells (equivalence classes).
4. Select a small representative sample (e.g., 1-2 workers) from each populated class for interview/observation.
5. Conduct information-gathering sessions for each class, treating class responses as representative of that entire group.

## Analyst Questions & Prompts

• How often do you use the system (dedicated, discretionary, casual)?
• How long have you performed this specific operational process?
• Which work shift or geographic location do you belong to?

## Minimal Realistic Example

An analyst faced with 500 A/P clerks creates a matrix based on Shift (Day/Night), Tenure (<1 yr, 1-10 yrs, >10 yrs), and Usage (Dedicated/Casual). This defines 18 equivalence classes; interviewing 1 representative per class reduces required sessions from 500 to 18 while covering all user variances.

## Quality Criteria & Verification

The resulting class sample must fully cover all operational edge cases, shifts, and tenure variations without omitting distinct operational sub-groups.

## Errors & Anti-Patterns

Assuming all process workers act identically without building a classification matrix; sampling only senior workers or manager-recommended 'favorite' employees.

## When NOT to Use

When the user population is small enough to interview every individual directly, or when role activities are completely standardized with zero variance.

## Alternatives & Complementary Methods

Surveys/Questionnaires, Persona Definition, User Role Modeling.

## Supported Decisions

Elicitation planning, resource allocation for discovery, sample selection for UAT.

## AI & Agentic Adaptation

Agentic analytics can cluster user telemetry and log data to automatically group system users into behavioral equivalence classes, suggesting an optimized sampling plan to the analyst.
