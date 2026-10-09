---
id: elaborated-use-case-description
name: "Elaborated Use Case Description"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 1
---

# Elaborated Use Case Description

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Elaborated Use Case Description (Alternative Flows & Conditional Logic)

## Problem Solved

Reduces edge-case failure, logic omission, and missed operational exception requirements.

## BA Lifecycle Phase

Analysis / specification

## Input Artifacts

Base Use Case Descriptions, System Glossary.

## Output Artifacts

Elaborated Use Case Descriptions, Alternative Flow Descriptions, Activity Diagrams.

## Participants & Roles

BA/System Analyst, SME, Developer, Tester.

## Prerequisites

Base use case flow of events is drafted and agreed upon.

## Step-by-Step Procedure

Walk through base flow steps to identify decision points and failure modes.
2. Document major variations/exceptions as text-based conditional logic or separate Alternative Flow Descriptions.
3. Specify exact insertion points and return points for alternative paths.
4. Map complex branching/loops using Activity Diagrams if text becomes unreadable.
5. Adjust postconditions to cover alternative outcomes.

## Analyst Questions & Prompts

What if the credit check fails? What if data is missing? What if the user cancels mid-process?

## Minimal Realistic Example

In 'Evaluate Loan Request', if applicant credit is unacceptable, system executes Alternative Flow A1: generates rejection letter, updates status to Disapproved, and halts processing.

## Quality Criteria & Verification

Completeness review against business rules, test scenario coverage, peer review.

## Errors & Anti-Patterns

Over-nesting conditional logic (pseudocode) making text unreadable; treating simple exceptions as full extend relationships.

## When NOT to Use

Simple linear processes with zero decision points or branching logic.

## Alternatives & Complementary Methods

Decision Tables, State Machine Diagrams, Activity Diagrams.

## Supported Decisions

Architecture exception handling, test design, acceptance.

## AI & Agentic Adaptation

Not specified in source.
