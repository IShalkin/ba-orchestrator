---
id: abstract-data-type-adt-specification
name: "Abstract Data Type (ADT) Specification"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Abstract Data Type (ADT) Specification

`T5 Requirements Specification › 5.8 Formal Specification`

## Problem Solved

Provides a purely external, mathematical specification of data types based strictly on available operations and axioms, eliminating overspecification and providing a formal definition of completeness.

## BA Lifecycle Phase

Specification

## Input Artifacts

Domain concept definitions, identified queries, commands, and creators.

## Output Artifacts

Formal ADT Specification comprising Functions & Signatures, Preconditions, and Axioms.

## Participants & Roles

Requirements Engineer / Systems Analyst (Author).

## Prerequisites

Basic set theory and discrete math concepts (functions, signatures, boolean logic).

## Step-by-Step Procedure

Name the new ADT (T) and identify required previous types (e.g., INTEGER, BOOLEAN).
2. Define function signatures for Creators (-> T), Queries (T -> PreviousType), and Commands (T -> T).
3. Identify partial functions and state their exact preconditions in the Preconditions section using total query functions.
4. Write algebraic Axioms defining the effect of every creator and command on every query.
5. Verify that preconditions are correct expressions.
6. Prove Sufficient Completeness: demonstrate that axioms allow reducing any correct query expression to a value of a previous type.

## Analyst Questions & Prompts

"What information can we ask about this object (queries)? What operations modify it (commands)? What creates it (creators)? What is the value of query Q after applying command C? Under what conditions is command C valid?"

## Minimal Realistic Example

Specifying ADT COUNTER: Creators: new -> COUNTER; Queries: item -> INTEGER; Commands: up, down -> COUNTER (partial); Preconditions: up(c) require item(c) < 10; Axioms: item(new) = 0, item(up(c)) = item(c) + 1.

## Quality Criteria & Verification

Proof of Sufficient Completeness (ability to reduce any correct query expression); ADT Precondition Rule compliance.

## Errors & Anti-Patterns

Specifying internal data representations (e.g., array vs linked list) instead of external operations; writing circular axioms; omitting preconditions for partial functions.

## When NOT to Use

Simple static configuration files or unstructured data blobs.

## Alternatives & Complementary Methods

Object-Oriented Classes with Contracts, Z Specification, Model-Based Formalisms.

## Supported Decisions

API contract specification, abstract domain modeling, proof of specification completeness.

## AI & Agentic Adaptation

AI agents can check ADT specifications for sufficient completeness by running term-rewriting reductions on sample query expressions and flagging un-axiomatized command-query pairs.
