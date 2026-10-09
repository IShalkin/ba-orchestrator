---
id: object-oriented-requirements-analysis-with-contracts
name: "Object-Oriented Requirements Analysis with Contracts"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.5"
subtask_name: "Decomposition and Systems Analysis"
source_count: 1
---

# Object-Oriented Requirements Analysis with Contracts

`T4 Modelling and Analysis › 4.5 Decomposition and Systems Analysis`

## Problem Solved

Prevents premature time-ordering overspecification, handles combinatorial case explosions, and provides stable, modifiable, and reusable requirements architectures.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Elicited scenarios (use cases/user stories), domain glossary (E.1), environment component list (E.2).

## Output Artifacts

Object-Oriented Requirements Specification consisting of Class Definitions, Feature Signatures (Queries, Commands, Creators), and Contracts (Preconditions, Postconditions, Class Invariants).

## Participants & Roles

Business Analyst / Requirements Engineer (Architect), Subject-Matter Experts (Reviewers).

## Prerequisites

Domain vocabulary defined in Glossary; fundamental understanding of object-oriented modeling principles.

## Step-by-Step Procedure

Identify object types (classes) from the environment and system domain (e.g., Concrete Environment, Abstract Environment).
2. For each class, identify applicable Queries (information retrieval) and Commands (state modifications).
3. Define class interfaces without implementation details, marking features as deferred.
4. Attach Contracts to features: Preconditions (require) for commands, Postconditions (ensure) for state changes, and Class Invariants for persistent properties.
5. Establish inter-class relations: Client-Supplier and Inheritance.
6. Categorize classes into the 7 Kinds of Class.
7. Use scenario classes (specification drivers) to validate that valid execution sequences satisfy feature preconditions.

## Analyst Questions & Prompts

"What types of objects exist in this domain? What questions can we ask about an object (queries)? What operations modify it (commands)? What must be true before an operation can run (precondition)? What is guaranteed afterward (postcondition)?"

## Minimal Realistic Example

Defining class INSURANCE_CLAIM with query is_investigated, command evaluate (require is_investigated; ensure is_evaluated), and invariant (is_evaluated implies is_investigated).

## Quality Criteria & Verification

Command-Query completeness; contract consistency; abstractness (no implementation leakage); seamless reversibility.

## Errors & Anti-Patterns

Confusing classes with implementation code; omitting preconditions; forcing rigid sequential ordering instead of logical constraints; premature optimization.

## When NOT to Use

Simple procedural batch scripts with no complex domain object lifecycle.

## Alternatives & Complementary Methods

Abstract Data Types (ADTs), Formal Specification Languages (Z, B), Entity-Relationship Modeling.

## Supported Decisions

System architecture decomposition, class API design, modular work assignment, seamless transition to design and code.

## AI & Agentic Adaptation

AI agents can parse natural language use cases into formal OO class definitions with Eiffel-style contracts, automatically verifying contract consistency and query completeness.
