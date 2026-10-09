---
id: quality-grid
name: "Quality Grid"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 1
---

# Quality Grid

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

## Problem Solved

Systematically prioritizes quality factors (non-functional requirements) and identifies critical business quality concerns before specifying metrics.

## BA Lifecycle Phase

elicitation

## Input Artifacts

List of quality factors (McCall, ISO 9126), project charter.

## Output Artifacts

Quality Grid table (Quality Factors vs. Priority levels: Critical, Important, As Usual, Unimportant) with annotated business concerns.

## Participants & Roles

BA, sponsor, business owner, architect, QA manager.

## Prerequisites

Understanding of business goals and overall project constraints.

## Step-by-Step Procedure

Select a comprehensive list of quality factors (e.g., McCall's 11 factors).
2. Evaluate and mark the priority level for each factor relative to normal standards.
3. Force stakeholders to balance priorities (not everything can be Critical).
4. For every 'Critical' or 'Important' factor, document the specific business concern behind the rating.
5. Use the prioritized grid to guide detailed quality metric selection.

## Analyst Questions & Prompts

Why is availability critical in this project? What specific business loss occurs if this quality factor is at a normal level?

## Minimal Realistic Example

Grid rating Reliability/Availability as 'Critical' with Concern: 'Hard to run hotel if system is down; room status not visible.'

## Quality Criteria & Verification

Sponsor sign-off, alignment with project budget and resource constraints.

## Errors & Anti-Patterns

Rating every quality factor as 'Critical' without budget justification, leading to unrealistic project scope.

## When NOT to Use

Small, trivial projects where quality needs are standard and self-evident.

## Alternatives & Complementary Methods

Planguage, Risk Assessment.

## Supported Decisions

Quality requirement prioritization, QA resource allocation, architectural trade-offs.

## AI & Agentic Adaptation

Prompt AI to evaluate project charters against quality taxonomies to draft initial candidate quality grids.
