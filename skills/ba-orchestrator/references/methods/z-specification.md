---
id: z-specification
name: "Z Specification"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Z Specification

`T5 Requirements Specification › 5.8 Formal Specification`

**Also described as:** State-Based Formal Specification (Z Language)

## Problem Solved

Reduces ambiguity, structural vagueness, and unverified state transformations in complex object-oriented transactional systems.

## BA Lifecycle Phase

Specification / verification

## Input Artifacts

Object model entities, associations, system operations, domain invariants.

## Output Artifacts

Z specification document (given types, data schemas, initialization schemas, operation schemas).

## Participants & Roles

Formal Specification Engineer, BA, Software Architect.

## Prerequisites

Conceptual objects and operations are identified.

## Step-by-Step Procedure

Declare given types Book, Person.
2. Construct Data Schemas declaring state variables (sets, relations, functions) and framing state invariants.
3. Construct Initialization Schemas defining initial state values.
4. Construct Operation Schemas declaring input (?)/output (!) variables, Delta/Xi imported schemas, domain pre-conditions, and post-conditions relating primed (') output states to unprimed input states.
5. Compose schemas using schema calculus (conjunction, disjunction).

## Analyst Questions & Prompts

What state variables are modified (Delta) vs unchanged (Xi)? What is the exact mathematical relation defining this state transformation? What exception schemas must be disjoined to make this operation robust?

## Minimal Realistic Example

A Z schema 'Checkout' importing 'Delta LibrarySystem', taking 'p?: Person' and 'bc?: BookCopy', with pre-conditions 'bc? in Available' and post-conditions 'OnLoan' = OnLoan union {bc?}'.

## Quality Criteria & Verification

Type correctness; schema consistency; satisfaction of data invariants by operation post-conditions; completeness of disjoined exception schemas.

## Errors & Anti-Patterns

Omitting prime (') notation on modified state variables; failing to handle the frame problem for unmentioned variables; writing un-satisfiable pre-conditions.

## When NOT to Use

For reactive, real-time control systems where temporal ordering and event-driven triggers are dominant (use SCR or LTL instead).

## Alternatives & Complementary Methods

VDM, B-Method, Alloy, SCR, Real-Time LTL.

## Supported Decisions

Transactional software architecture, formal refinement to code, theorem proving.

## AI & Agentic Adaptation

Z type-checkers and SAT solvers (like Alloy) can automatically parse Z schemas, verify invariant preservation across operations, and generate counterexamples when pre-conditions fail.
