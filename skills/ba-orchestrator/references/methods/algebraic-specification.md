---
id: algebraic-specification
name: "Algebraic Specification"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Algebraic Specification

`T5 Requirements Specification › 5.8 Formal Specification`

## Problem Solved

Reduces implementation bias and state-representation overhead by defining domain concepts abstractly through equations on operation compositions.

## BA Lifecycle Phase

Specification / analysis

## Input Artifacts

Domain concepts, operations (generators, modifiers, observers), composition rules.

## Output Artifacts

Algebraic specification units (signatures, conditional equations, pre-conditions).

## Participants & Roles

Formal Specification Engineer, Software Mathematician.

## Prerequisites

Domain concepts and applicable operations are identified.

## Step-by-Step Procedure

Declare given types and parameterized type constructors.
2. Declare operation signatures (input/output sets).
3. Classify operations into Generators (minimal constructors), Modifiers, and Observers.
4. Construct conditional equations by systematically pairing every Observer and non-generator Modifier with every Generator.
5. Define equations for base cases (empty generator) and recursive cases (non-empty generator).
6. Specify pre-conditions or exception outputs for partial operations.

## Analyst Questions & Prompts

What is the minimal set of generator operations? What is the effect of applying observer X to generator Y? What equation defines the composition of modifier A with generator B?

## Minimal Realistic Example

Algebraically specifying a library stack where 'CopyExists(AddCopy(lib, bc'), bc)' evaluates to 'true' if bc = bc', and to 'CopyExists(lib, bc)' if bc != bc'.

## Quality Criteria & Verification

Completeness of operation pairings; consistency of equations; termination of term rewriting rules.

## Errors & Anti-Patterns

Failing to cover all Observer-Generator pairings; writing non-terminating recursive equations; over-complicating equations due to missing generators.

## When NOT to Use

When system state dynamics and temporal event sequences are the primary concern of requirements engineering.

## Alternatives & Complementary Methods

Z, VDM, LARCH, OBJ.

## Supported Decisions

Abstract data type design, executable prototyping via term rewriting.

## AI & Agentic Adaptation

Term-rewriting engines (e.g., OBJ, MAUDE) can execute algebraic equations automatically to provide rapid functional prototypes and verify equational consistency.
