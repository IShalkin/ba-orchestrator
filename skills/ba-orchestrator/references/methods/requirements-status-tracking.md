---
id: requirements-status-tracking
name: "Requirements Status Tracking"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.4"
subtask_name: "Traceability and Status"
source_count: 1
---

# Requirements Status Tracking

`T6 Prioritisation and Requirements Management › 6.4 Traceability and Status`

## Problem Solved

Reduces overoptimistic status reporting (e.g., '90% done syndrome') and provides precise visibility into project progress by tracking discrete functional requirements through defined lifecycle states.

## BA Lifecycle Phase

change management

## Input Artifacts

Baselined requirements list, test execution logs, implementation verification reports.

## Output Artifacts

Requirement status attributes, status distribution charts (burn-up/burn-down), burndown charts.

## Participants & Roles

Business Analyst (lead/owner), Project Manager, Developer, Tester.

## Prerequisites

Baselined set of discrete, uniquely labeled requirements assigned to a planned release.

## Step-by-Step Procedure

Define acceptable requirement status values (e.g., Proposed, Drafted, Approved, Implemented, Verified, Deferred, Deleted, Rejected).
2. Define explicit transition conditions required to move a requirement between states.
3. Assign status attributes to each individual requirement in an RM tool or tracking matrix.
4. Update status attributes as developers implement code and testers confirm acceptance criteria.
5. Summarize status distribution periodically across the release baseline.
6. Declare release/feature completion only when 100% of committed requirements reach 'Verified', 'Deleted', or 'Deferred' status.

## Analyst Questions & Prompts

What explicit state is requirement FR-12 in? Has requirement FR-12 passed its acceptance criteria to be marked Verified? Why is this requirement still marked In Progress?

## Minimal Realistic Example

Replacing vague developer progress claims with exact tracking: 'Of 84 subsystem requirements, 61 are Verified, 14 are Implemented, and 9 are Drafted.'

## Quality Criteria & Verification

Status changes occur strictly when predefined criteria are met; verified requirements trace directly to passed test cases.

## Errors & Anti-Patterns

Estimating progress via subjective percentage completion rather than discrete state transitions; failing to record rejected or deleted requirements, allowing them to resurface later.

## When NOT to Use

Extremely small single-person projects where individual requirement tracking overhead exceeds project duration.

## Alternatives & Complementary Methods

Agile Story Status Tracking (In Backlog, Defined, In Progress, Completed, Accepted), Iteration Burndown Charts.

## Supported Decisions

Release readiness decisions, schedule adjustment decisions, resource allocation.

## AI & Agentic Adaptation

Not in source
