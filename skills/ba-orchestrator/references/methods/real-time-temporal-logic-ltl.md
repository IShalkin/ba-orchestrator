---
id: real-time-temporal-logic-ltl
name: "Real-Time Temporal Logic (LTL)"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# Real-Time Temporal Logic (LTL)

`T5 Requirements Specification › 5.8 Formal Specification`

**Also described as:** Real-Time Linear Temporal Logic (LTL) Specification

## Problem Solved

Reduces imprecision, ambiguous interpretations, and lack of mathematical verifyability in declarative goals, requirements, assumptions, and domain properties.

## BA Lifecycle Phase

Specification / verification

## Input Artifacts

Informal goal definitions, object model attributes/associations, time bounds.

## Output Artifacts

Formal LTL specifications, formalized goal models, formal domain properties.

## Participants & Roles

BA, Formal Methods Specialist, Verification Engineer.

## Prerequisites

Object model provides typed variables, attributes, and associations; critical goals are selected for formalization.

## Step-by-Step Procedure

Identify typed instance variables from the object model.
2. Formulate state assertions using first-order predicates, functions, and logical connectives.
3. Apply temporal operators (Always, Sooner-or-later, Until, Unless, Next, Previous) to specify state sequences over time.
4. Attach relative, absolute, or variable-dependent real-time bounds (e.g., <= 2s).
5. Match assertions against established goal specification patterns (Achieve, Maintain, Avoid) to ensure syntactic and semantic correctness.

## Analyst Questions & Prompts

Does this property hold in every future state or at least one future state? What is the exact relative time bound d? Is this variable evaluated in the current state or next state?

## Minimal Realistic Example

Formalizing 'MaintainWorstCaseStoppingDistance' as: 'forall tr1, tr2: Train, Always (Following(tr2, tr1) => Dist(tr2, tr1) > WCS-Dist(tr2))'.

## Quality Criteria & Verification

Well-formed syntax; precise mapping to domain phenomena; absence of contradiction; realizability by assigned agents.

## Errors & Anti-Patterns

Writing unbounded Achieve goals assigned to single agents (unrealizable); nesting temporal operators awkwardly without using proven patterns; omitting variable-dependent time bounds.

## When NOT to Use

For low-risk, non-critical requirements where structured natural language templates provide sufficient precision at lower cost.

## Alternatives & Complementary Methods

Structured natural language with fit criteria, Z specification, SCR tabular specification.

## Supported Decisions

Formal verification, safety case arguments, automated model checking.

## AI & Agentic Adaptation

LLM formalization agents can automatically translate structured natural language goal definitions into well-formed LTL assertions using pattern-matching libraries, flagging un-realizable temporal operators.
