---
id: goal-refinement-patterns
name: "Goal Refinement Patterns"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 2
---

# Goal Refinement Patterns

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Goal Elicitation via Category-Specific Refinement Trees (Model Reuse); Uncontrollability-Driven Refinement Pattern

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces completeness uncertainty and missing requirements by reusing proven, standardized goal decomposition templates (e.g., satisfaction, safety, security).

**[Variant B]**

Resolves goal uncontrollability when an agent expected to be in charge of a goal condition cannot physically control that condition.

## BA Lifecycle Phase

**[Variant A]**

elicitation

**[Variant B]**

analysis

## Input Artifacts

**[Variant A]**

Preliminary goal model, goal categories taxonomy (satisfaction, safety, security, etc.)

**[Variant B]**

Goal model, system objective specifications, agent responsibilities

## Output Artifacts

**[Variant A]**

Instantiated category-specific goal refinement tree, identified missing sub-goals or alternative options

**[Variant B]**

Refined goal model (AND-refinement tree with controllable sub-goals and accuracy/expectation goals)

## Participants & Roles

**[Variant A]**

BA, Domain Expert, SME

**[Variant B]**

BA, Architect, System Actuators/Agents

## Prerequisites

**[Variant A]**

Preliminary goals categorized into specific taxonomic types (e.g., satisfaction, safety).

**[Variant B]**

Identification of a goal condition that is unmonitored or uncontrollable by the assigned agent.

## Step-by-Step Procedure

**[Variant A]**

Introduce a preliminary goal into the system model and classify its goal category.
2. Browse reusable refinement trees corresponding to that goal category.
3. Instantiate the generic concepts and conditions in system-specific terms.
4. Adapt the tree as necessary to fit specific domain constraints, or reject non-applicable sub-goals.
5. Compare the instantiated tree against existing goal branches to identify missing sub-goals or alternative refinements.

**[Variant B]**

Identify a goal condition that an assigned agent cannot physically control.
2. Introduce a new intermediate condition that is directly controllable by the target agent.
3. Create an accuracy/expectation goal assigned to an actuator or environment agent to mirror the controllable condition into the physical condition.
4. Structure the decomposition as an AND-refinement tree in the goal model.

## Analyst Questions & Prompts

**[Variant A]**

What category does this goal belong to? Are there standard service request, guard, or alarm mechanisms for this goal category that we missed?

**[Variant B]**

Can the assigned agent physically control this goal condition? If not, what intermediate condition can it control, and what actuator agent can ensure the physical condition matches?

## Minimal Realistic Example

**[Variant A]**

For a meeting scheduling satisfaction goal ('RequestIssued'), reusing a generic satisfaction refinement tree highlights missing sub-goals related to scheduler appointment and issuing service responses.

**[Variant B]**

A train controller cannot physically close train doors directly (DoorsClosed condition). The uncontrollability-driven refinement pattern introduces a controllable condition 'DoorsStateClosed' assigned to the train controller, along with an expectation assigned to the doors actuator agent to keep doors state accurate.

## Quality Criteria & Verification

**[Variant A]**

Check for model completeness by verifying that instantiated sub-goals cover all essential phases (request, appointment, delivery, guard response) of the specific goal category.

**[Variant B]**

The resulting refinement must be complete, minimal, and consistent with known domain properties. Verify that the assigned software agent controls its designated variable and the expectation on the environment agent is feasible.

## Errors & Anti-Patterns

**[Variant A]**

Blinded reuse without adaptation to domain constraints; forcing irrelevant sub-goals into system specifications.

**[Variant B]**

Assigning goals to agents that lack physical controllability over the goal variables; assuming an over-ideal system where environment agents always execute perfectly without explicit expectations.

## When NOT to Use

**[Variant A]**

In novel, highly unstandardized domains where pre-existing category refinement patterns do not apply.

**[Variant B]**

When the assigned agent already has direct control over all state variables involved in the goal formulation.

## Alternatives & Complementary Methods

**[Variant A]**

Keyword-based goal elicitation, Interviewing, Problem analysis of system-as-is

**[Variant B]**

Unmonitorability-driven refinement pattern, Guard-introduction pattern, Milestone-driven pattern

## Supported Decisions

**[Variant A]**

Scope determination, functional coverage, release planning

**[Variant B]**

Architecture decisions, system boundary definition, agent responsibility assignments

## AI & Agentic Adaptation

**[Variant A]**

Agentic systems can automatically map identified high-level intents to domain-specific goal templates and pre-populate requirement trees for human-in-the-loop validation.

**[Variant B]**

For autonomous AI agents, apply this pattern when an LLM or agent system cannot directly alter an external environment state; introduce an agent-controllable action command combined with a specialized executor or tool agent to enforce accuracy.
