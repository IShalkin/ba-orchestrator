---
id: formal-specification-overview-ltl-z-scr
name: "Formal Specification Overview (LTL, Z, SCR)"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Formal Specification Overview (LTL, Z, SCR)

`T5 Requirements Specification › 5.8 Formal Specification`

**Also described as:** Formal Specification (LTL, Z, SCR)

## Problem Solved

Eliminates ambiguity, noise, and incompleteness by providing a mathematically precise, machine-processable specification amenable to automated proof, model checking, and animation.

## BA Lifecycle Phase

Specification / formal verification

## Input Artifacts

Agreed system goals, requirements, assumptions, domain properties, ER conceptual structures.

## Output Artifacts

Formal specification schemas (Z), temporal logic assertions (LTL), tabular state machine functions (SCR), mathematical proof obligations.

## Participants & Roles

Formal Methods Specialist / Requirements Engineer, System Architect, Safety/Security Verifier.

## Prerequisites

Strong discrete mathematics background; well-defined domain concepts and boundaries.

## Step-by-Step Procedure

Define the mathematical domain of interpretation (given types, variables, state space).
2. (History-based / LTL) Formalize declarative goals using temporal operators (Always, Eventually, Until).
3. (State-based / Z) Define state variables and data schemas with invariants, then specify operations via pre- and post-conditions.
4. (Event-based / SCR) Define mode transition, event, and condition tables over monitored/controlled variables.
5. (Algebraic) Define signatures, generator operations, and equational composition laws.
6. Document precise designations mapping formal symbols to real-world domain phenomena.

## Analyst Questions & Prompts

What exact mathematical relation defines this operation's post-condition? Is this temporal requirement bounded by a specific time deadline? What is the explicit domain designation of symbol X?

## Minimal Realistic Example

Specifying train door safety in LTL: 'Always (Moving(tr) -> tr.Doors = closed)' or in Z: 'Checkout' schema defining post-condition 'Available' = Available \ {be?} AND Onloan' = Onloan U {be?}'.

## Quality Criteria & Verification

Automated type checking; mathematical consistency proof; exhaustiveness/disjointness table checks; theorem proving; model checking.

## Errors & Anti-Patterns

Failing to document domain designations (making math meaningless); overspecifying implementation details prematurely; creating unreadable nested temporal logic assertions.

## When NOT to Use

In low-risk, non-critical commercial projects where informal/semi-formal documentation suffices and formal verification costs are unjustified.

## Alternatives & Complementary Methods

Complementary: Semi-formal Diagrams, Model Animation, Inspections. Alternative: Structured Natural Language Templates.

## Supported Decisions

Safety/security certification, formal verification of critical software logic, exact contractual specifications.

## AI & Agentic Adaptation

Neural-symbolic AI agents can translate structured natural language requirements into formal LTL/Z specs and invoke automated SAT solvers to verify consistency.
