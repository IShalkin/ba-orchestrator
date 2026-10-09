---
id: responsibility-modelling
name: "Responsibility Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 1
---

# Responsibility Modelling

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Responsibility Modeling & Context Diagram Derivation

## Problem Solved

Reduces unclear operational boundaries, unassigned goals, and system interface mismatches between software and environment agents.

## BA Lifecycle Phase

specification

## Input Artifacts

Goal model, Object model (attributes/associations)

## Output Artifacts

Agent Diagram, Context Diagram, Dependency Diagram (i* style), Capability & Responsibility Declarations

## Participants & Roles

BA, System Architect, Software Engineer, Organizational SME

## Prerequisites

Leaf goals in the goal model identified and mapped to candidate system or environment agents.

## Step-by-Step Procedure

Map leaf goals to candidate agents based on monitoring and control capabilities.
2. Verify goal realizability for assigned agents (can the agent monitor evaluated variables and control constrained variables?).
3. Enforce the Unique Controller constraint (each variable controlled by at most one agent).
4. Specify instance responsibility and capability annotations.
5. Derive the Context Diagram by connecting agents whose controlled variables are monitored by other agents.
6. Conduct vulnerability analysis on agent dependency chains.

## Analyst Questions & Prompts

Which agent controls the variables constrained by this goal? Can this agent monitor all required input conditions? What happens to depender goals if this dependee agent fails?

## Minimal Realistic Example

TrainController agent controls Command.Speed and monitors TrainInfo.Position. TrackSystem controls TrainInfo.Position. The derived context diagram shows a directed interface edge from TrackSystem to TrainController labelled Position.

## Quality Criteria & Verification

Goal realizability verified for every assignment; Unique Controller constraint satisfied; context diagram data flows match goal inputs/outputs completely.

## Errors & Anti-Patterns

Assigning goals to agents lacking monitoring/control capabilities; assigning a single controlled variable to multiple concurrent agents; confusing process stakeholders with system agents.

## When NOT to Use

Single-agent monolithic systems where no interface boundaries exist.

## Alternatives & Complementary Methods

Use Case Actor Modeling, RACI Matrix, Interface Definition Languages (IDL)

## Supported Decisions

Software/environment boundary definition, load distribution, architectural allocation, vulnerability mitigation

## AI & Agentic Adaptation

Agentic orchestrators can parse goal variable dependencies to generate agent capability graphs, verify monitoring/control bounds, and flag unrealizable agent goals in multi-agent workflows.
