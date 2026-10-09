---
id: client-expectations-capture-and-management
name: "Client Expectations Capture and Management"
task: T3
task_name: "Stakeholders"
subtask: "3.3"
subtask_name: "Engagement, Conflict and Negotiation"
source_count: 1
---

# Client Expectations Capture and Management

`T3 Stakeholders › 3.3 Engagement, Conflict and Negotiation`

## Problem Solved

Prevents the gap between what the client expects from the engagement (value, experience, way of working, solution preferences) and what is formally scoped, by capturing expectations separately from requirements and revisiting them as they shift; expectations change informally over time, requirements change only through change control.

## BA Lifecycle Phase

Discovery / elicitation / change management

## Input Artifacts

Stakeholder register, scope statement or scope baseline, stakeholder or communication management plan, history of the client's earlier projects with the delivery team, meeting notes.

## Output Artifacts

Expectations log (id, expectation in the holder's words, holder role, category: value / experience / solution, must or preference, scope position: in / out / unclear, status: confirmed / changed / retired / converted to requirement, last confirmed date, linked requirement or change request id); outcome summary shared with the client and the team; list of misaligned or unrealistic expectations with an agreed handling action.

## Participants & Roles

Delivery or engagement lead (owner), BA, business architect, solution architect, product owner, client sponsor and key client stakeholders.

## Prerequisites

Key client stakeholders identified; a scope baseline exists to compare expectations against; access to client decision-makers for validation.

## Step-by-Step Procedure

1. Prepare: review the scope baseline, the stakeholder register and any history with this client; draft hypotheses per stakeholder group about value, experience and solution expectations.
2. Hold expectation conversations with each key stakeholder group; ask open questions and record expectations in the holder's words, not the analyst's interpretation.
3. Classify each expectation (value / experience / solution, must or preference) and compare it with the scope baseline: in scope, out of scope or unclear.
4. Validate the consolidated log with the stakeholders; flag misaligned or unrealistic expectations and agree a handling action (accept, reframe, escalate, raise a change request).
5. Share the outcomes with the client and the delivery team.
6. Revisit the log at every milestone or gate: re-confirm, mark changed or retired items, and convert an expectation into a requirement only through formal change control.

## Analyst Questions & Prompts

• What would make this engagement a success for you personally?
• What should working with the delivery team feel like week to week?
• What worked or did not work in earlier projects with a delivery partner?
• Are there technologies, vendors or approaches you expect us to use or to avoid?
• Which of these expectations is a must, and which is a preference?
• What has changed since we last discussed your expectations?

## Minimal Realistic Example

Log entries: 'E-04 | Head of Operations | Experience | Must | "A weekly demo of working software, not slides" | In scope (delivery approach) | Confirmed at gate 1'. 'E-07 | CFO | Solution | Preference | "Keep using the existing finance reports" | Out of scope | Handling: reframe at the next steering meeting'. At gate 2, E-07 is re-checked, marked Changed, and raised as change request CR-12.

## Quality Criteria & Verification

Expectations are kept separate from requirements; every key stakeholder group is covered; each entry has a holder role, category, scope position and status; every misaligned expectation has a handling action and an owner role; the log is re-confirmed at each milestone and the date is recorded; no expectation became a requirement without change control.

## Errors & Anti-Patterns

Treating expectations as requirements, which creates scope creep without change control; capturing expectations once at kick-off and never revisiting them; talking only to the sponsor (insufficient stakeholder coverage); ignoring stated technology preferences; leaving outdated expectations marked as confirmed; recording the analyst's interpretation instead of the holder's words; hiding unrealistic expectations instead of handling them openly.

## When NOT to Use

A very short, fixed-scope task with a single known stakeholder and no relationship component; purely internal work with no client or sponsor whose satisfaction is at stake.

## Alternatives & Complementary Methods

Stakeholder Identification and Analysis (before); Stakeholder Management Planning (complementary, uses the log for engagement actions); Business Objectives, Vision and Scope (the formal, requirements-side counterpart); Interviews (main instrument); Change Control (when an expectation must become a requirement).

## Supported Decisions

Engagement approach and communication cadence, scope negotiation, handling of change requests, steering escalations, client satisfaction risk.

## AI & Agentic Adaptation

An agent drafts expectation hypotheses from meeting notes and e-mails, classifies them and compares them with the scope baseline; a human validates them with the stakeholders. At each gate an agent compares the log with recent notes and flags expectations that appear to have shifted. The agent quotes sources and never invents stakeholder statements.
