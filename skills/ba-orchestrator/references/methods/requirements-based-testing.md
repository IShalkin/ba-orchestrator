---
id: requirements-based-testing
name: "Requirements-Based Testing"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.4"
subtask_name: "Testing and Acceptance"
source_count: 1
---

# Requirements-Based Testing

`T7 Validation and Acceptance › 7.4 Testing and Acceptance`

**Also described as:** Requirements-Based Testing (Conceptual Testing)

## Problem Solved

Verifies requirements testability and discovers missing, ambiguous, or inconsistent logic by deriving test scenarios directly from user requirements before writing code.

## BA Lifecycle Phase

validation

## Input Artifacts

Use cases, functional requirements, dialog maps, business rules

## Output Artifacts

Conceptual Test Cases / Test Scenarios, Traceability matrix mapping tests to requirements and models

## Participants & Roles

BA, Test Lead/Testers, End Users

## Prerequisites

Documented user requirements or use cases outlining normal flows, alternative flows, and exceptions.

## Step-by-Step Procedure

Identify test conditions covering normal flows, alternative flows, and exceptions for each use case.
2. Express conceptual tests in implementation-independent inputs and expected outcomes.
3. Map conceptual tests to functional requirements to verify 100% functional coverage.
4. Trace test execution paths visually on analysis models (e.g., dialog maps or STDs).
5. Identify missing requirements or model branches where test execution path cannot be completed.
6. Refine requirements or correct tests based on disconnects found.

## Analyst Questions & Prompts

What expected outcome occurs if valid data is entered? What error message appears if the record is missing? Does this test path map to an existing functional requirement?

## Minimal Realistic Example

Tracing a test ('Enter valid chemical ID with 2 stockroom containers -> display container list -> select container -> add to current request') onto a dialog map to confirm navigation coverage.

## Quality Criteria & Verification

100% functional requirement coverage by tests; visual model path coverage; verification that all tests can be 'executed' against written requirements.

## Errors & Anti-Patterns

Waiting until development is complete to start designing tests; assuming code-based unit tests evaluate business requirement correctness.

## When NOT to Use

None; applicable across all project lifecycle types.

## Alternatives & Complementary Methods

Acceptance Criteria Definition, Inspection, Fit Criteria.

## Supported Decisions

Acceptance, release readiness, quality baseline.

## AI & Agentic Adaptation

Not in source
