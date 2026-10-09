---
id: base-use-case-description
name: "Base Use Case Description"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 1
---

# Base Use Case Description

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

## Problem Solved

Reduces ambiguity and functional gaps by detailing ideal step-by-step user-system interactions without getting bogged down in edge cases.

## BA Lifecycle Phase

Analysis / specification

## Input Artifacts

Initial Use Case Descriptions, System Glossary, Actor Glossary.

## Output Artifacts

Base Use Case Descriptions (structured text template).

## Participants & Roles

BA/System Analyst, SME, Primary/Secondary Actors, Architect.

## Prerequisites

Initial use cases and system glossary established.

## Step-by-Step Procedure

Define scope via Preconditions and Postconditions.
2. Document the primary flow of events as numbered steps (actor actions and system responses).
3. Identify secondary actors involved in supporting interactions.
4. Note nonbehavioral requirements, assumptions, and open issues.
5. Assign development priority.

## Analyst Questions & Prompts

What initiates the flow? What does the system do in response? What state must the system be in before and after?

## Minimal Realistic Example

UC 'Evaluate Loan Request': Step 1: Officer selects request; Step 2: System presents credit score/history; Step 3: Officer approves; Step 4: System updates status to Approved.

## Quality Criteria & Verification

Peer review, stakeholder walkthrough, verifiability of preconditions and postconditions.

## Errors & Anti-Patterns

Functional decomposition, introducing GUI layout details prematurely, writing monolithic 10-page use cases.

## When NOT to Use

High-uncertainty early exploratory spikes or pure non-functional architectural changes.

## Alternatives & Complementary Methods

Collaboration Cases, System Sequence Diagrams, Essential Use Cases.

## Supported Decisions

Scope, release planning, test case generation, interface design.

## AI & Agentic Adaptation

Not specified in source.
