---
id: quality-attribute-workshop-qaw
name: "Quality Attribute Workshop (QAW)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Quality Attribute Workshop (QAW)

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

## Problem Solved

Reduces uncertainty and ambiguity regarding architecturally significant quality attribute requirements prior to completing the architecture design.

## BA Lifecycle Phase

Elicitation

## Input Artifacts

Business/mission context, high-level system requirements, initial architectural plans (if available).

## Output Artifacts

Consolidated and prioritized quality attribute scenarios, list of key architectural drivers, refined 6-part quality attribute scenarios.

## Participants & Roles

Facilitators, Architect, Business/Mission Stakeholders, Project Manager, Developers, Testers.

## Prerequisites

Identified system stakeholders and a presentation of the business/mission vision and goals.

## Step-by-Step Procedure

Present QAW overview.
2. Present business/mission needs.
3. Present architectural plan.
4. Identify architectural drivers.
5. Brainstorm quality attribute scenarios.
6. Consolidate similar scenarios.
7. Prioritize scenarios using voting.
8. Refine top scenarios into six-part scenario format.

## Analyst Questions & Prompts

What stimulus initiates the scenario? What is the source of the stimulus? What environment is the system in? What artifact is affected? What is the expected response? How is the response measured?

## Minimal Realistic Example

Stakeholders brainstorm and refine a scenario: 'When a peak load of 2,000 requests occurs during normal operation, the system processes all requests with an average latency of under 2 seconds.'

## Quality Criteria & Verification

Six-part scenario completeness check, stakeholder consensus, voting results, review of response measures for testability.

## Errors & Anti-Patterns

Creating untestable scenarios, focusing exclusively on functional features instead of quality attributes, lack of key stakeholder representation.

## When NOT to Use

Small projects with trivial quality requirements or well-known, fully established domains without stakeholder uncertainty.

## Alternatives & Complementary Methods

Quality Attribute Utility Trees, Requirements Document Mining, PALM (Pedigreed Architecture Analysis Method for Business Goals).

## Supported Decisions

Scope definition, prioritization of quality attribute drivers, preliminary architectural design strategy.

## AI & Agentic Adaptation

An AI agent can ingest raw stakeholder transcripts to auto-generate 6-part scenarios, suggest scenario consolidations, and run automated ambiguity/testability checks. Human-in-the-loop is required for final scenario prioritization and validation.
