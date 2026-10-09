---
id: attribute-driven-design-add
name: "Attribute-Driven Design (ADD)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Attribute-Driven Design (ADD)

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

## Problem Solved

Eliminates design uncertainty and arbitrary decision-making by systematically designing software architecture based on prioritized quality attribute requirements and architectural drivers.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Design purpose, primary functional requirements, quality attribute scenarios, constraints, architectural concerns.

## Output Artifacts

Architectural views (sketches of Module, C&C, Allocation views), instantiated elements with assigned responsibilities, documented design decisions and rationale, updated design backlog.

## Participants & Roles

Software Architect, Design Team, Technical Lead.

## Prerequisites

Prioritized architecturally significant requirements (ASRs) and clear definition of design purpose.

## Step-by-Step Procedure

Review inputs.
2. Establish iteration goal by selecting drivers.
3. Choose system elements to refine.
4. Choose design concepts (patterns/tactics) satisfying drivers.
5. Instantiate elements, allocate responsibilities, and define interfaces.
6. Sketch views and record design decisions.
7. Analyze current design and review goal achievement.

## Analyst Questions & Prompts

Which drivers are highest priority for this iteration? What patterns or tactics address these drivers? What responsibilities does each instantiated element hold? What interfaces are required?

## Minimal Realistic Example

In Iteration 1 for a web app, select 'High Availability' driver, choose 'Active Redundancy' pattern, instantiate primary and backup server elements, assign failover responsibilities, and sketch C&C view.

## Quality Criteria & Verification

Verification against selected drivers using lightweight architecture analysis, tactics questionnaires, or prototyping.

## Errors & Anti-Patterns

Big Design Up Front (BDUF); designing without explicit quality attribute drivers; failing to record design decisions and rationale.

## When NOT to Use

Trivial systems where standard reference architectures can be directly instantiated without adaptation or trade-offs.

## Alternatives & Complementary Methods

Domain-Driven Design (DDD), Rational Unified Process (RUP) architecture design, Agile Spikes.

## Supported Decisions

Structural decisions, technology stack selection, pattern and tactic adoption, interface specifications.

## AI & Agentic Adaptation

AI agents can analyze ASRs to recommend candidate design patterns/tactics and draft structural views. Human architects must review and approve final design trade-offs.
