---
id: unified-pegs-lifecycle
name: "Unified PEGS Lifecycle"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.3"
subtask_name: "Organisation, Baselines and Reuse"
source_count: 1
---

# Unified PEGS Lifecycle

`T6 Prioritisation and Requirements Management › 6.3 Organisation, Baselines and Reuse`

**Also described as:** The Unified PEGS Lifecycle Model Management

## Problem Solved

Eliminates the rigid, late-code risks of the Waterfall and the 'no-upfront-planning' chaos of extreme Agile by providing a flexible, iterative, sprint-based lifecycle model with balanced, evolving requirements.

## BA Lifecycle Phase

Change Management

## Input Artifacts

Project Plan (Book P), Goals Book (Book G), Sprint Backlogs, Cluster Architecture.

## Output Artifacts

Iterative Sprint Deliverables, continuously updated Requirements Repository (Books P, E, G, S), User Acceptance Test Plans.

## Participants & Roles

Project Manager, Business Analyst / Requirements Engineer, System Architect, Lead Developers, Testers, Product Owner.

## Prerequisites

Minimum upfront requirements outcome (G.1, G.3, G.7, S.1, S.2, E.3, P.4, P.5) and cluster division.

## Step-by-Step Procedure

Produce initial upfront version of the requirements repository (Minimum Requirements Outcome) during early sprints.
2. Divide system into logical Clusters (e.g., Model, View, Controller).
3. Structure development into fixed-duration time-boxed Sprints.
4. Apply the NASACE Principle: ensure early sprints focus on definition/architecture + UI/feasibility prototypes; middle sprints focus on cluster implementation; final sprints focus on system verification.
5. Each sprint executes a definition phase (goals, environment, project planning, cluster definition) followed by an implementation phase (cluster construction and verification).
6. Apply reversibility: update requirements and design repository elements whenever implementation reveals new domain insights.
7. Execute final acceptance verification based on updated requirements.

## Analyst Questions & Prompts

"What are the minimum upfront requirements needed to start coding? Which clusters are most critical/risky? How do we update requirements based on lessons from the latest sprint?"

## Minimal Realistic Example

Sprint 1: Draft overall PEGS requirements + build UI prototype; Sprint 2: Refine requirements, define architecture, start core Model cluster; Sprints 3-N: Continue cluster builds + update specs; Final Sprint: System verification & bug fixes.

## Quality Criteria & Verification

Adherence to Requirements Elaboration Principle; continuous alignment between code and requirements repository; successful UAT execution.

## Errors & Anti-Patterns

Freezing requirements upfront (Waterfall trap); doing zero upfront requirements and writing user stories on the fly (Agile trap); shipping throwaway prototypes; ignoring reversibility.

## When NOT to Use

Replaced by lightweight DevOps continuous delivery for ultra-rapid cloud web maintenance, though underlying elaboration principles still apply.

## Alternatives & Complementary Methods

Rational Unified Process (RUP), Agile Scrum, Spiral Model, Cluster Model.

## Supported Decisions

Sprint planning, release scheduling, change request management, resource re-allocation.

## AI & Agentic Adaptation

AI systems can manage repository updates across sprints, automatically re-tracing requirements changes to impacted test suites and code modules after each iteration.
