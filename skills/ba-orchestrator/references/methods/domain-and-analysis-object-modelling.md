---
id: domain-and-analysis-object-modelling
name: "Domain and Analysis Object Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.5"
subtask_name: "Decomposition and Systems Analysis"
source_count: 1
---

# Domain and Analysis Object Modelling

`T4 Modelling and Analysis › 4.5 Decomposition and Systems Analysis`

**Also described as:** Domain & Analysis Object Modeling (Mapping Use Cases to Objects)

## Problem Solved

Reduces the risk of creating a purely functional, unmaintainable architecture by balancing dynamic behavior with static entity structure.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Base/Elaborated Use Cases, System Glossary.

## Output Artifacts

Domain Object Model / Analysis Object Model (Class Diagrams), System Glossary updates.

## Participants & Roles

BA/System Analyst, Architect, Developer.

## Prerequisites

System glossary and base use case descriptions created.

## Step-by-Step Procedure

Parse nouns and noun phrases in use case descriptions to find candidate domain objects.
2. Group objects into categories (tangible things, concepts, roles, external systems).
3. Filter out attributes, synonyms, or out-of-scope entities.
4. Define associations, multiplicities, and aggregations between objects.
5. Update glossary and maintain traceability between objects and use cases.

## Analyst Questions & Prompts

What business entities does this use case act upon? What data must be stored permanently?

## Minimal Realistic Example

From 'Submit Loan Request', candidate objects identified: Applicant, Loan Application, Credit Report, Account History, and Credit Score.

## Quality Criteria & Verification

Traceability walkthroughs ensuring every entity required by a use case exists in the object model with proper attributes and relationships.

## Errors & Anti-Patterns

Modeling implementation/database tables instead of conceptual business entities.

## When NOT to Use

In non-object-oriented procedural refactoring where static domain entity modeling adds no architectural value.

## Alternatives & Complementary Methods

Entity-Relationship Diagrams (ERD), Logical Data Models.

## Supported Decisions

Subsystem decomposition, data architecture, domain model baseline.

## AI & Agentic Adaptation

Not specified in source.
