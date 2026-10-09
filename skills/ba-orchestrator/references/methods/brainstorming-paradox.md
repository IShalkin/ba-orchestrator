---
id: brainstorming-paradox
name: "Brainstorming Paradox"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.6"
subtask_name: "Group and Creative Sessions"
source_count: 1
---

# Brainstorming Paradox

`T2 Situation Investigation and Elicitation › 2.6 Group and Creative Sessions`

## Problem Solved

Identifies system risks early and establishes proactive countermeasures by focusing on unwanted events.

## BA Lifecycle Phase

Elicitation / Discovery / Analysis

## Input Artifacts

Problem domain context, high-level project goals

## Output Artifacts

List of prohibited events/risks, list of protective countermeasures and requirements

## Participants & Roles

Moderator, Stakeholders

## Prerequisites

Understanding of project objectives and risk boundaries.

## Step-by-Step Procedure

Assemble stakeholders and define the focus area.
2. Ask participants to generate events that must  never  occur.
3. Moderator records all negative events without judgment.
4. Group analyzes the list of negative events.
5. Develop system requirements and protective measures to prevent those events.

## Analyst Questions & Prompts

"What is the absolute worst thing that could happen when using this system?", "What events must never occur under any circumstances?"

## Minimal Realistic Example

Stakeholders brainstorm nightmare scenarios for an autonomous navigation system, such as "giving route directions onto oncoming traffic lanes," then define rules to prevent it.

## Quality Criteria & Verification

Identification of critical edge cases and security/safety risks; actionable preventive requirements.

## Errors & Anti-Patterns

Focusing only on catastrophic risks while ignoring standard functional requirements.

## When NOT to Use

When the team is trying to define routine user workflows or optimistic product vision features.

## Alternatives & Complementary Methods

Classic Brainstorming, Mind Mapping

## Supported Decisions

Risk mitigation, safety requirements definition, architecture constraints.

## AI & Agentic Adaptation

Agentic red-teaming to simulate worst-case failure modes and automatically draft defensive guardrail requirements.
