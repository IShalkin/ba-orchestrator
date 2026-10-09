---
id: formal-picnic
name: "Formal Picnic"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Formal Picnic

`T5 Requirements Specification › 5.8 Formal Specification`

**Also described as:** Formal Specification via Formal Picnic

## Problem Solved

Eliminates subtle ambiguities, internal contradictions, falsehoods, and edge-case oversights in critical requirements by deriving precise mathematical models and converting them back into crystal-clear natural language.

## BA Lifecycle Phase

Specification

## Input Artifacts

Informal natural-language requirements, domain assumptions, mathematical notation conventions.

## Output Artifacts

Formal Mathematical Specification (Sets, Predicates, Functions, Relations, Axioms) and 'Back-from-the-Picnic' Natural-Language Specification.

## Participants & Roles

Requirements Engineer / Formal Methods Specialist (Author), Stakeholders / SMEs / Programmers (Reviewers).

## Prerequisites

High-school/undergraduate discrete mathematics (logic, sets, functions, relations, sequences).

## Step-by-Step Procedure

Identify critical requirements parts where ambiguities or high risks exist.
2. Define mathematical types/sets for domain entities.
3. Formulate operations as mathematical relations or functions (signatures, domains, ranges).
4. Express behavioral constraints and business logic as formal predicate expressions or minimization/optimization formulas.
5. Formulate and formally prove key requirements theorems (e.g., Feasibility Theorem).
6. Translate the formal specification back into plain, highly structured, unambiguous natural language ('Formal Picnic').
7. Include both the formal model and picnic text in the specification, explicitly designating which is binding.

## Analyst Questions & Prompts

"What is the exact set of elements? Is this function total or partial? Under what precise mathematical conditions does a solution exist? How do we formalize 'as many as possible'?"

## Minimal Realistic Example

Formalizing text reformatting as a minimization formula over the set of 'recast' strings (S1: min newlines among recasts with line length <= M), proving the Feasibility Theorem, and deriving a 9-clause picnic specification.

## Quality Criteria & Verification

Mathematical proof of correctness/feasibility theorems; Non-ambiguity; Command-Query / Sufficient Completeness.

## Errors & Anti-Patterns

Failing to translate formal models back for non-math stakeholders; overcomplicating math models with operational algorithm details; confusing mathematical specs with program code.

## When NOT to Use

Non-critical, rapidly changing UI prototype ideas where mathematical rigor offers little ROI.

## Alternatives & Complementary Methods

Z, B Method, TLA+, Alloy, Abstract Data Types.

## Supported Decisions

Verification of safety-critical logic, algorithm feasibility proofs, unambiguous contract definitions for sub-contractors.

## AI & Agentic Adaptation

Agentic LLMs can formalize natural-language statements into first-order logic/set theory, run automated theorem provers/model checkers (e.g., Alloy/Z3), and generate picnic-style natural language summaries.
