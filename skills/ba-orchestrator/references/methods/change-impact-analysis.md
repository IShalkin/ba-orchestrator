---
id: change-impact-analysis
name: "Change Impact Analysis"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.5"
subtask_name: "Requirements Change Management"
source_count: 1
---

# Change Impact Analysis

`T6 Prioritisation and Requirements Management › 6.5 Requirements Change Management`

## Problem Solved

Prevents software surprises, uncoordinated schedule slips, and broken system dependencies by systematically identifying all work products and tasks affected by a proposed requirement modification.

## BA Lifecycle Phase

change management / analysis

## Input Artifacts

Change Request, baselined SRS, Requirements Traceability Matrix, design models, code files, test suites.

## Output Artifacts

Impact Analysis Summary Report, effort estimation worksheet, task dependency list.

## Participants & Roles

Evaluator (BA, Developer, or Tester assigned by CCB), CCB, Project Manager.

## Prerequisites

Detailed change request description, accessible traceability data.

## Step-by-Step Procedure

Analyze change proposal against implications checklist (conflict with business objectives, quality attributes, risks).
2. Trace affected requirements forward and backward using the Traceability Matrix to identify impacted user interface, design, code, build, database, test, and documentation artifacts.
3. Identify all specific tasks required to execute the change across all affected work products.
4. Estimate labor hours required for each task using an impact estimation worksheet.
5. Sum total effort and evaluate schedule, cost, and resource constraints.
6. Sequence tasks and identify trade-offs (e.g., dropping lower-priority requirements).
7. Submit formal Impact Analysis Report to CCB for decision-making.

## Analyst Questions & Prompts

Does this change conflict with existing requirements or business goals? What user interface screens, database fields, or source files must be modified? How many new unit and system tests must be written? What is the lost investment in work already completed?

## Minimal Realistic Example

Analyzing a simple error message change proposal, revealing that while English text is simple, German text exceeds database field limits, requiring schema changes, UI re-layouts, and regression testing.

## Quality Criteria & Verification

Comparing actual implementation effort against estimated impact effort over time to continuously refine checklists; thorough accounting of testing and documentation rework.

## Errors & Anti-Patterns

Skipping impact analysis to start coding immediately, turning task size into a major schedule surprise; relying on a single individual's guess rather than structured task identification checklists.

## When NOT to Use

Trivial single-variable edits with zero ripple effect or un-baselined draft changes.

## Alternatives & Complementary Methods

Automated RM tool impact reporting, Requirements Mapping Matrix, Cause-and-Effect Analysis.

## Supported Decisions

CCB approval/rejection decisions, commitment renegotiation (schedule, budget, scope).

## AI & Agentic Adaptation

Not in source
