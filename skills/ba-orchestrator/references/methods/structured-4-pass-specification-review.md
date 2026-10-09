---
id: structured-4-pass-specification-review
name: "Structured 4-Pass Specification Review"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.1"
subtask_name: "Reviews and Inspections"
source_count: 1
---

# Structured 4-Pass Specification Review

`T7 Validation and Acceptance › 7.1 Reviews and Inspections`

**Also described as:** Structured Specification Review (4-Pass Walkthrough)

## Problem Solved

Prevents superficial sign-offs and missing flaws by replacing single unfocused approvals with structured, multi-perspective reviews.

## BA Lifecycle Phase

Validation / Governance

## Input Artifacts

Draft specification artifacts (use cases, requirements set, decision tables, quality scenarios, examples).

## Output Artifacts

Review defects log, quality gateway approval, updated requirement status.

## Participants & Roles

Business Analyst, Sponsor/Business Owner, Engineering/Architect, Tester/QA.

## Prerequisites

Complete draft requirement specification set and review checklist.

## Step-by-Step Procedure

Conduct Pass 1 (Business Validation): Verify problem fit and value.
2. Conduct Pass 2 (Requirements Quality Review): Check ambiguity, completeness, singularity.
3. Conduct Pass 3 (Engineering Review): Validate interface, dependency, and architecture feasibility.
4. Conduct Pass 4 (Testability Review): Verify testability and boundary coverage via walkthrough scenarios.

## Analyst Questions & Prompts

Does this behavior solve the intended business problem? Can this obligation be verified by a clear test method? Are negative cases covered?

## Minimal Realistic Example

A team walks through realistic case intake scenarios to verify that manual triage exceptions are correctly routed before baseline sign-off.

## Quality Criteria & Verification

Verification against ISO 29148 individual/set criteria and checklist sign-off across all 4 distinct review perspectives.

## Errors & Anti-Patterns

Asking stakeholders to sign off on massive unread documents without realistic scenario walkthroughs.

## When NOT to Use

Extremely minor baseline changes or bug fixes where informal peer review is sufficient.

## Alternatives & Complementary Methods

Peer Review, Prototype Walkthrough, Quality Gateway Checklist.

## Supported Decisions

Baseline sign-off, release readiness, architectural acceptance.

## AI & Agentic Adaptation

Includes automated syntax check guardrails followed by Human-in-the-Loop review for logic and governance safety.
