---
id: use-case-driven-test-planning
name: "Use Case-Driven Test Planning"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.4"
subtask_name: "Testing and Acceptance"
source_count: 1
---

# Use Case-Driven Test Planning

`T7 Validation and Acceptance › 7.4 Testing and Acceptance`

**Also described as:** Use Case-Driven Test Planning & Test Case Generation

## Problem Solved

Reduces untested requirements, late-stage defect discovery, and unaligned testing scope.

## BA Lifecycle Phase

Validation / change management

## Input Artifacts

Base/Elaborated Use Cases, Instance Scenarios, Architecture Specifications.

## Output Artifacts

Test Plan, Functional Test Cases, Interaction Test Matrix.

## Participants & Roles

BA/System Analyst, Tester/QA Lead, Architect.

## Prerequisites

Baseline use cases and scenario paths defined.

## Step-by-Step Procedure

Number/identify all decision points and flow paths in a use case.
2. Convert path trees into functional test cases (positive and negative).
3. Map preconditions to Test Setup and postconditions to Test Teardown.
4. Substitute concrete test data for abstract flow variables.
5. Build interaction tests by cross-referencing shared objects (Read-before-Create / Read-after-Delete).

## Analyst Questions & Prompts

What steps lead to success? What steps trigger exceptions? What preconditions must be set up before execution?

## Minimal Realistic Example

Test Case 'TC-105 Approve Loan Request': Setup with applicant Joe Smith ($1k debt); Execute Officer Approval; Result: Status = Approved, Log created.

## Quality Criteria & Verification

Requirement coverage verification (100% path coverage for high-priority use cases), peer review by QA.

## Errors & Anti-Patterns

Testing only the 'sunny day' path while omitting negative boundary and exception paths.

## When NOT to Use

Non-functional load/stress testing unrelated to discrete user transactions.

## Alternatives & Complementary Methods

Boundary Value Analysis, Decision Table Testing, State Transition Testing.

## Supported Decisions

Acceptance, release readiness, quality sign-off.

## AI & Agentic Adaptation

Not specified in source.
