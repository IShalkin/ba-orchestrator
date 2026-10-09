---
id: goal-domain-tracing-qfd
name: "Goal-Domain Tracing (QFD)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 1
---

# Goal-Domain Tracing (QFD)

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Goal-Domain Tracing (and QFD)

## Problem Solved

Verifies that every business goal is supported by specific domain tasks/requirements, and that every specified task serves a business purpose.

## BA Lifecycle Phase

analysis

## Input Artifacts

Business goals list, task descriptions / work areas list.

## Output Artifacts

Goal-Domain Matrix (Goals vs. Work Areas/Tasks) or Quality Function Deployment (QFD) House of Quality matrix.

## Participants & Roles

BA, business owner, QA manager, system architect.

## Prerequisites

Explicit list of business goals and defined domain tasks.

## Step-by-Step Procedure

List business goals along matrix rows.
2. List domain work areas, tasks, or quality factors along matrix columns.
3. Evaluate intersections and mark cells where a task supports a goal.
4. Check for unlinked goals (missing requirements) and unlinked tasks (unjustified scope).
5. (For QFD) Add goal values, support weights, and function cost calculations.

## Analyst Questions & Prompts

Which specific task enables us to achieve this business goal? Why are we building this feature if it supports no stated goal?

## Minimal Realistic Example

Matrix mapping Goal 'Use experience data for quotation' to Tasks 'Quotation' and 'Cost Registration', revealing that experience data capture was missing.

## Quality Criteria & Verification

100% trace coverage for all business goals; sign-off by business owner.

## Errors & Anti-Patterns

Confusing functional requirements with business goals inside the QFD rows.

## When NOT to Use

Small, simple projects where business goals and features are directly obvious.

## Alternatives & Complementary Methods

Goal-Requirements Analysis, Traceability Matrix.

## Supported Decisions

Scope verification, detection of missing requirements, feature justification.

## AI & Agentic Adaptation

Automatically map business goals to candidate task descriptions using semantic matching prompts.
