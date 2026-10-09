---
id: issue-and-item-tracking
name: "Issue and Item Tracking"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.4"
subtask_name: "Traceability and Status"
source_count: 2
---

# Issue and Item Tracking

`T6 Prioritisation and Requirements Management › 6.4 Traceability and Status`

**Also described as:** Item Tracking; Requirements Issue Tracking

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Prevents open questions, missing requirements, TBDs, and stakeholder conflicts from slipping through the cracks or causing last-minute project derailments.

**[Variant B]**

Reduces the risk of overlooked issues, requirements conflicts, and unaddressed stakeholder concerns by capturing, classifying, and tracking items to resolution.

## BA Lifecycle Phase

**[Variant A]**

analysis / change management

**[Variant B]**

Planning / elicitation / analysis / prioritisation / validation / change management

## Input Artifacts

**[Variant A]**

Requirements review logs, TBD flags in SRS, stakeholder questions, defect reports.

**[Variant B]**

Stakeholder concerns, review feedback, defect reports, change requests, risk logs.

## Output Artifacts

**[Variant A]**

Requirements issue log / database, issue burndown chart.

**[Variant B]**

Item Record / Tracker (unique ID, category, impact, priority, owner, resolver, status, resolution history).

## Participants & Roles

**[Variant A]**

Business Analyst (owner), Project Manager, Reviewers / Stakeholders, Assigned Issue Resolver.

**[Variant B]**

BA, Item Owner, Item Resolver, Sponsor, Stakeholders.

## Prerequisites

**[Variant A]**

Access to a shared issue-tracking tool or centralized log.

**[Variant B]**

Agreed item tracking tool/spreadsheet and defined escalation lifecycle.

## Step-by-Step Procedure

**[Variant A]**

Log all open requirement questions, TBDs, contradictions, and missing items into an issue-tracking tool as soon as they are identified.
2. Categorize each issue (e.g., Requirement Question, Missing Requirement, Incorrect Requirement, Implementation Question).
3. Assign a single owner and target resolution date to each issue.
4. Retain discussion logs and rationale for resolutions within the tool.
5. Monitor issue resolution rate using an issue burndown chart during project status reviews.
6. Resolve all critical open issues prior to baselining specifications for construction.

**[Variant B]**

Capture stakeholder concern or issue as a tracked item record.
2. Assess viability and classify item type (action, assumption, constraint, defect, risk, enhancement).
3. Assign priority, impact level, target resolution date, and item owner/resolver.
4. Formulate agreed strategy (e.g., accept, mitigate, resolve, avoid).
5. Track progress through status changes (Open, Assigned, Resolved, Closed).
6. Log resolution history and escalate to management if target date is missed.

## Analyst Questions & Prompts

**[Variant A]**

Who owns the resolution of this open question? What is the deadline for deciding on this TBD? What was the rationale behind resolving issue #42?

**[Variant B]**

"Who is the assigned owner for resolving issue X?", "What is the impact on project scope if this item is not resolved by date Y?", "What is the current status of concern Z?"

## Minimal Realistic Example

**[Variant A]**

Logging an open question about portal configuration during early reviews, assigning it to a technical lead, and tracking it to resolution before construction to avoid missing an entire subsystem.

**[Variant B]**

An issue raised during review ('Unclear tax calculation logic') is logged as Item #104, assigned to Tax SME, prioritized High, and tracked to resolution within 3 days.

## Quality Criteria & Verification

**[Variant A]**

Zero unresolved critical issues/TBDs at baseline date; clear ownership and audit trail for every logged issue.

**[Variant B]**

Every item has an assigned owner, target date, and priority; tracking log is accessible and regularly updated until all items reach closure.

## Errors & Anti-Patterns

**[Variant A]**

Writing open issues on erased whiteboards or personal notes instead of a central tool; allowing TBDs to persist unassigned into code construction.

**[Variant B]**

Logging excessive trivial details leading to tracking overhead; allowing items to remain open indefinitely without escalation.

## When NOT to Use

**[Variant A]**

None; open issue tracking is universally applicable across all project types.

**[Variant B]**

On minor tasks where informal direct communication resolves questions immediately without formal tracking overhead.

## Alternatives & Complementary Methods

**[Variant A]**

Defect tracking tools, Agile Product Backlog issue management.

**[Variant B]**

Complemented by Risk Management, Defect Tracking Systems, Backlog Management, and Reviews.

## Supported Decisions

**[Variant A]**

Baselining decisions, risk escalation, release readiness.

**[Variant B]**

Issue escalation, sign-off readiness, risk mitigation prioritization.

## AI & Agentic Adaptation

**[Variant A]**

Not in source

**[Variant B]**

Agents integrated into communication channels can detect unresolved questions in chat threads, auto-create tracked issues, assign team owners, and ping for status updates.
