---
id: requirements-risk-management
name: "Requirements Risk Management"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.6"
subtask_name: "Requirements Risk and Process Improvement"
source_count: 1
---

# Requirements Risk Management

`T6 Prioritisation and Requirements Management › 6.6 Requirements Risk and Process Improvement`

**Also described as:** Software Requirements Risk Management

## Problem Solved

Prevents requirements-related pitfalls (e.g., unstated needs, scope creep, lack of user involvement) from escalating into costly project crises or cancellations.

## BA Lifecycle Phase

prioritisation / change management / project planning

## Input Artifacts

Vision and scope document, draft SRS, stakeholder feedback, historical project risk lists.

## Output Artifacts

Risk Item Tracking Log/Database, Risk Management Plan, Condition-Consequence Risk Statements.

## Participants & Roles

Project Manager, Business Analyst, Risk Item Owner, Key Stakeholders / Product Champions.

## Prerequisites

Project initiation and awareness of potential requirements failure modes.

## Step-by-Step Procedure

Brainstorm and identify requirements-related risks using established risk taxonomy checklists across elicitation, analysis, specification, validation, and management.
2. Document each risk in a 'Condition-Consequence' format ('If condition, then consequence').
3. Assess probability (0.1 to 1.0) and relative impact (1 to 10) for each item.
4. Calculate Risk Exposure (Probability x Impact) and rank order the risk list.
5. Develop a Risk Management Plan containing mitigation actions (to lower probability or impact) and contingency plans for top exposure items.
6. Assign a single owner and due date to each risk mitigation task.
7. Periodically monitor and track risk status during regular project status reviews, retiring resolved risks.

## Analyst Questions & Prompts

What requirements-related conditions could cause project failure? What is the likelihood of this risk materializing? What is the potential impact in time or money? What mitigation action reduces this probability?

## Minimal Realistic Example

Documenting Risk #1: 'If user involvement in elicitation is insufficient, then extensive UI rework will be required after beta testing.' Exposure: 4.2. Mitigation: Conduct weekly workshops with product champions and build throwaway UI mock-ups.

## Quality Criteria & Verification

All risk statements follow condition-consequence structure; top risks are reviewed periodically; risk exposure decreases over time as mitigations take effect.

## Errors & Anti-Patterns

Confusing current issues with potential risks; assuming risks are controlled simply because they were listed; spending more on risk mitigation than the potential loss value.

## When NOT to Use

When dealing with existing active problems (which should be handled via issue tracking) rather than future uncertainties.

## Alternatives & Complementary Methods

Fault Tree Analysis, Hazard Analysis, Issue Tracking, Project Retrospectives.

## Supported Decisions

Project continuation/cancellation decisions, schedule buffer allocations, resource planning.

## AI & Agentic Adaptation

Not in source
