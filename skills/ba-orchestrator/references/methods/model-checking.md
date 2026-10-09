---
id: model-checking
name: "Model Checking"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.3"
subtask_name: "Formal Model Verification"
source_count: 1
---

# Model Checking

`T7 Validation and Acceptance › 7.3 Formal Model Verification`

## Problem Solved

Reduces subtle concurrency errors, race conditions, deadlocks, and unhandled state combinations in complex reactive models.

## BA Lifecycle Phase

Quality assurance / verification

## Input Artifacts

Parallel state machine model (PROMELA, SMV, LTS), formal property to verify (LTL or CTL formula).

## Output Artifacts

Verification result ('Property holds' or 'Property violated'), concrete counterexample trace.

## Participants & Roles

Verification Specialist, Formal Methods Engineer, BA.

## Prerequisites

State machine model and target properties are fully formalized.

## Step-by-Step Procedure

Express system model as parallel state machines in model checker input language.
2. Formalize target safety/liveness property in LTL or CTL.
3. Execute model checker (e.g., SPIN, SMV, LTSA).
4. Tool exhaustively explores reachability graph.
5. If property holds, output 'Yes'. If property is violated, tool generates the shortest counterexample execution trace.
6. Analyze counterexample trace to pinpoint model defect and fix the specification.

## Analyst Questions & Prompts

Does this parallel state machine satisfy safety property P under all state combinations? What exact sequence of interleaving events led to the deadlock in this counterexample?

## Minimal Realistic Example

Model checking a train door/movement controller against 'Always(Moving => DoorsClosed)', producing a 5-step counterexample trace showing doors opening while moving due to a missing guard.

## Quality Criteria & Verification

Exhaustive reachability exploration; correctness of formalized target properties; validity of generated counterexample traces.

## Errors & Anti-Patterns

State explosion problem on overly large state spaces; misinterpreting long counterexample traces; formalizing incorrect properties leading to false confidence.

## When NOT to Use

For infinite-state systems without abstraction, or when models are informal and cannot be compiled into state machines.

## Alternatives & Complementary Methods

Theorem Proving, Bounded SAT Solving, Specification Animation.

## Supported Decisions

Safety/security verification sign-off, critical controller verification, bug elimination.

## AI & Agentic Adaptation

AI diagnostic agents can analyze long model checker counterexample traces, automatically isolate the root cause transition in the source statechart, and suggest the missing guard condition.
