---
id: requirements-quality-gateway
name: "Requirements Quality Gateway"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.1"
subtask_name: "Reviews and Inspections"
source_count: 1
---

# Requirements Quality Gateway

`T7 Validation and Acceptance › 7.1 Reviews and Inspections`

**Also described as:** Requirements Quality Gateway & Peer Review

## Problem Solved

Prevents bad, ambiguous, incomplete, or out-of-scope requirements from passing into development, reducing costly downstream rework.

## BA Lifecycle Phase

Validation

## Input Artifacts

Snow Cards, User Stories, Requirements Specification, Work Context Diagram, Project Goals.

## Output Artifacts

Validated Requirements Repository, Quality Review Feedback/Defect Log, Approved Requirements/Backlog.

## Participants & Roles

Requirements Guardian / Senior BA, Product Owner, System Architect, QA/Tester.

## Prerequisites

Formulated requirements or stories containing descriptions, rationales, and fit/acceptance criteria.

## Step-by-Step Procedure

Submit candidate requirements to the Quality Gateway before adding them to the official repository/backlog.
2. Check for Scope Alignment using the Context Diagram.
3. Check for Relevancy against Project Goals.
4. Check for Completeness (all snow card fields or story attributes present).
5. Verify testability of Fit/Acceptance Criteria.
6. Check for consistency of terminology against the Data Dictionary.
7. Check for viability, gold plating, and potential conflicts.
8. Approve, reject, or request rework for the requirement.

## Analyst Questions & Prompts

"Is this requirement inside our context boundary?", "Does it directly contribute to our project goals?", "Is the fit criterion testable?", "Is this requirement gold-plating?", "Are the terms used defined consistently in the data dictionary?"

## Minimal Realistic Example

Rejecting a proposed requirement "The system shall play a greeting sound when the user logs in" because its customer dissatisfaction score is 1 (nobody cares if missing), identifying it as gold plating that adds cost without business value.

## Quality Criteria & Verification

Requirement passes 100% of gateway checklist tests (In Scope, Relevant, Complete, Testable, Consistent, Viable, Non-Gold-plated).

## Errors & Anti-Patterns

Bypassing the gateway due to schedule pressure; treating reviews as rubber-stamping; lacking clear objective criteria for requirement acceptance.

## When NOT to Use

Informal exploratory prototyping phases where ideas are explicitly disposable.

## Alternatives & Complementary Methods

Formal Fagan Inspections, Walkthroughs, BDD Specification by Example.

## Supported Decisions

Backlog approval, baseline specification sign-off, developer task assignment readiness.

## AI & Agentic Adaptation

AI agents can act as automated Quality Gateway auditors to instantly scan requirements for vagueness, missing rationales, or terminology inconsistencies against the data dictionary, flagging defects for human BA resolution.
