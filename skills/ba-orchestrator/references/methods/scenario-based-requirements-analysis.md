---
id: scenario-based-requirements-analysis
name: "Scenario-Based Requirements Analysis"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 1
---

# Scenario-Based Requirements Analysis

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Scenario-Based Requirements Analysis (Use Cases and User Stories)

## Problem Solved

Reduces abstractness and communication gaps between non-technical stakeholders and developers by illustrating concrete, step-by-step usage paths through the system.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Stakeholder requests, workflow observations, draft Glossary, Goals Book.

## Output Artifacts

High-level usage scenarios in Goals Book (G.5), Detailed Usage Scenarios in System Book (S.4), User Stories, Epics, Use Case Slices.

## Participants & Roles

Business Analyst / Requirements Engineer (Author), Subject-Matter Experts / End Users (Inputs & Reviewers), Developers/Testers (Consumers).

## Prerequisites

Identified system scope and target user roles.

## Step-by-Step Procedure

Identify primary user roles and their operational objectives.
2. For high-level business paths, draft Use Cases in Chapter G.5 specifying primary actor, preconditions, triggers, main success scenario, success guarantees, and extensions.
3. For fine-grained development work items, draft User Stories in the standard template: 'As a role, I want feature, so that benefit'.
4. Verify User Stories against INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).
5. Group stories into Epics or decompose complex Use Cases into Use Case Slices.
6. Detail special/error handling paths as Use Case Extensions.
7. Use scenarios to derive test cases (S.6) and to extract abstract system behaviors (S.2).

## Analyst Questions & Prompts

"Who performs this action? What triggers it? What is the main success path? What can go wrong? What is the expected outcome?"

## Minimal Realistic Example

Writing a Use Case 'Process_loss_claim' (Primary Actor: Claims Adjuster, Trigger: Claim reported, Main Scenario: Register loss -> Assign agent -> Investigate -> Evaluate -> Set reserve -> Negotiate -> Close).

## Quality Criteria & Verification

INVEST criteria compliance for stories; scenario completeness (S.2 functionality covers all scenario steps); validation by SMEs.

## Errors & Anti-Patterns

Treating scenarios as full requirements specifications rather than illustrations/tests; operational overspecification; scenario explosion (trying to write an extension for every conceivable combination).

## When NOT to Use

As a substitute for abstract behavioral specifications or formal logic constraints.

## Alternatives & Complementary Methods

Object-Oriented Requirements with Contracts, Abstract Data Types, Business Process Model and Notation (BPMN), Statechart Diagrams.

## Supported Decisions

Sprint backlog construction, acceptance test design, UI workflow validation.

## AI & Agentic Adaptation

Agentic LLMs excel at generating initial use cases and user stories from interview transcripts, checking them against INVEST criteria, and auto-generating corresponding test scripts.
