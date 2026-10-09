---
id: goal-driven-object-modelling
name: "Goal-Driven Object Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 1
---

# Goal-Driven Object Modelling

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Goal-Driven Object Modeling (Class Diagram Derivation)

## Problem Solved

Reduces terminology ambiguity, missing conceptual state variables, and irrelevant domain clutter by deriving object models strictly from intentional goals.

## BA Lifecycle Phase

analysis

## Input Artifacts

Goal specifications, domain properties, assertions, interview transcripts

## Output Artifacts

Object Model (UML Class Diagram) with Entities, Associations, Attributes, Agents, Events, and Annotations (Def, DomInvar, Init)

## Participants & Roles

BA, System Architect, Database Designer, SME

## Prerequisites

Goal specifications and domain properties defined precisely or formally.

## Step-by-Step Procedure

Extract all conceptual items referenced in goal and domain property specifications.
2. Identify linking expressions to define associations and participating roles.
3. Apply decision heuristics: classify items as attributes vs. objects, and objects as entities, associations, agents, or events.
4. Attach attributes to appropriate objects or associations.
5. Identify specialization/generalization hierarchies using discriminant factors.
6. Decorate associations with multiplicities and domain invariants.
7. Generate glossary of terms.

## Analyst Questions & Prompts

What conceptual items are referenced in this goal statement? Is this item a state function or a first-class object? What is the exact domain invariant governing this concept?

## Minimal Realistic Example

Goal 'Maintain SpeedBelowBlockLimit' references 'Train', 'Block', 'Speed', and 'SpeedLimit'. This derives entities Train (attribute Speed) and Block (attribute SpeedLimit), and association 'On' linking Train and Block.

## Quality Criteria & Verification

Pertinence and completeness relative to the goal model; verification of association multiplicities; absence of pointer attributes; correct semantic definitions (Def/DomInvar) agreed by stakeholders.

## Errors & Anti-Patterns

Including implementation pointers as attributes; mixing dynamic state machine behaviors or agent interface links into structural object models.

## When NOT to Use

When building purely procedural or stateless scripts where structural state tracking is unnecessary.

## Alternatives & Complementary Methods

Domain Driven Design (DDD) Modeling, ER Modeling, Classic UML Class Modeling

## Supported Decisions

Database schema design, system vocabulary standardization, software architecture boundaries

## AI & Agentic Adaptation

LLM agents can parse natural language goal annotations, perform entity-relationship extraction, map entities to standardized schemas, and enforce anti-pattern guardrails automatically.
