---
id: checkpoint-charley-technical-design-review
name: "Checkpoint Charley (Technical Design Review)"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.4"
subtask_name: "Testing and Acceptance"
source_count: 1
---

# Checkpoint Charley (Technical Design Review)

`T7 Validation and Acceptance › 7.4 Testing and Acceptance`

## Problem Solved

Prevents solution drift, technical gold-plating, and developer-introduced requirement changes from reaching production without business analyst and stakeholder awareness.

## BA Lifecycle Phase

Change Management / Validation / Solution Monitoring

## Input Artifacts

Baselined solution document/requirements, completed technical design specifications, system architecture models.

## Output Artifacts

Updated baseline requirements document, verified technical design alignment log, business change requests (if needed).

## Participants & Roles

Business Analyst (reviewer/owner of requirements), Technical Lead/System Analyst (presenter), Developers, Solution Architect.

## Prerequisites

Completion of the detailed technical design by the development team prior to or during full code construction.

## Step-by-Step Procedure

Schedule a formal Checkpoint Charley meeting once technical system design is complete.
2. The technical lead presents the technical design to the business analyst, explaining how it implements the solution.
3. The business analyst evaluates the design against the baselined solution document requirements.
4. Identify any design trade-offs, technical shortcuts, or added unrequested features ('gilding the lily').
5. If technical changes alter business functionality, the analyst logs them and updates the requirements baseline.
6. If changes significantly impact business expectations or scope, the analyst takes the changes back to the problem owner for formal approval.

## Analyst Questions & Prompts

• How does this technical design component specifically fulfill Requirement X?
• Were any business rules or user workflows altered to accommodate system performance?
• Are there any unrequested features added in this design?
• Does this technical approach introduce any new operational constraints for the end user?

## Minimal Realistic Example

The Tech Lead shows that to optimize database performance, voucher entry will require a batch job overnight instead of real-time display. The BA catches this at Checkpoint Charley, identifies that it violates the real-time UAT criteria, and negotiates a design compromise before coding starts.

## Quality Criteria & Verification

Zero unaccounted variances exist between the technical system design and the baselined business requirements document.

## Errors & Anti-Patterns

Skipping technical design reviews and allowing developers to 'go dark' until UAT; allowing developers to change business workflows unilaterally without updating requirements.

## When NOT to Use

In pure agile/Scrum environments where the BA/product owner sits collocated with developers daily and reviews working code every sprint.

## Alternatives & Complementary Methods

Checkpoint Beta, Sprint Review, Architecture Review Board, Traceability Matrix Audit.

## Supported Decisions

Authorization to proceed to coding/build, requirement baseline updates, scope change control.

## AI & Agentic Adaptation

An AI agent can perform automated static analysis comparing technical design documentation or API schemas directly against natural-language requirement files, flagging discrepancies for the BA prior to the Checkpoint Charley meeting.
