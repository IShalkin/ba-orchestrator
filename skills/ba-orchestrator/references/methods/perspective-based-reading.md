---
id: perspective-based-reading
name: "Perspective-Based Reading"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.1"
subtask_name: "Reviews and Inspections"
source_count: 1
---

# Perspective-Based Reading

`T7 Validation and Acceptance › 7.1 Reviews and Inspections`

## Problem Solved

Improves defect detection rates by having reviewers inspect requirements through specific stakeholder viewpoints (e.g., tester, architect, user).

## BA Lifecycle Phase

Validation / Elicitation

## Input Artifacts

Requirements document, perspective-specific instructions/checklists

## Output Artifacts

Perspective-specific defect logs, consolidated validation report

## Participants & Roles

Auditors/Reviewers (assigned to specific perspectives: User, Architect, Tester)

## Prerequisites

Defined reading perspectives and tailored instruction checklists for each perspective.

## Step-by-Step Procedure

Select relevant perspectives (e.g., User, Architect, Tester, Compliance).
2. Assign each auditor a specific perspective and provide corresponding directives/questions.
3. Auditors read and inspect requirements strictly through their assigned lens (e.g., tester builds test cases).
4. Collect responses to perspective questions and logged open issues.
5. Consolidate and analyze findings across all perspectives.

## Analyst Questions & Prompts

"From a tester's view: Is there sufficient detail to derive concrete test cases?", "From an architect's view: Are non-functional performance constraints fully specified?"

## Minimal Realistic Example

A test lead reads a SRS purely to build acceptance test cases, discovering that edge-case error conditions are completely missing.

## Quality Criteria & Verification

High defect yield per perspective; verification against specific domain/role checklists.

## Errors & Anti-Patterns

Reviewers drifting back into generic reading rather than maintaining strict focus on their assigned role perspective.

## When NOT to Use

When reviewers lack domain knowledge of the assigned perspective.

## Alternatives & Complementary Methods

Checklist Validation, Inspection, Prototypes

## Supported Decisions

Testability verification, architectural feasibility approval.

## AI & Agentic Adaptation

Deploying specialized LLM agents persona-prompted as 'Tester', 'Architect', and 'End User' to scan documents concurrently.
