---
id: scr-event-based-specification
name: "SCR Event-Based Specification"
task: T5
task_name: "Requirements Specification"
subtask: "5.8"
subtask_name: "Formal Specification"
source_count: 1
---

# SCR Event-Based Specification

`T5 Requirements Specification › 5.8 Formal Specification`

**Also described as:** Event-Based Formal Specification (SCR Method)

## Problem Solved

Reduces incompleteness, non-determinism, and unhandled event combinations in reactive software controllers.

## BA Lifecycle Phase

Specification / verification

## Input Artifacts

Four-variable model (monitored, controlled, input, output variables), mode classes, events, conditions.

## Output Artifacts

SCR requirements specification (Mode Transition Tables, Event Tables, Condition Tables).

## Participants & Roles

Software Requirements Engineer, Control Engineer, Verification Specialist.

## Prerequisites

Monitored and controlled variables identified; synchrony hypothesis assumed.

## Step-by-Step Procedure

Declare monitored, controlled, term, and mode class variables.
2. Construct Mode Transition Tables defining mode changes triggered by conditioned events (@T(V) WHEN C).
3. Construct Event Tables defining term/controlled variable outputs triggered by events in specific modes.
4. Construct Condition Tables defining output values as total functions of mode and conditions.
5. Perform automated consistency checks (disjointness and coverage) on every table row.

## Analyst Questions & Prompts

Under what mode does event X cause output Y? Are all condition entries in this table row pairwise disjoint? Do the condition entries in this row cover 100% of possible states?

## Minimal Realistic Example

An SCR Condition Table for 'DoorsState' defining output 'Open' when mode is 'Stopped' and condition is 'AtPlatform or Emergency', and 'Closed' when 'NOT AtPlatform and NOT Emergency'.

## Quality Criteria & Verification

Row disjointness (no non-determinism: C1 AND C2 = false); row coverage (no missing cases: C1 OR C2 OR ... = true); type correctness.

## Errors & Anti-Patterns

Violating row disjointness (causing non-deterministic outputs); omitting cases in condition tables (causing incomplete requirements); violating the synchrony hypothesis.

## When NOT to Use

For large, highly hierarchical transactional systems requiring complex object structuring and relational calculus.

## Alternatives & Complementary Methods

RSML, Statecharts, Real-time LTL, Z.

## Supported Decisions

Embedded software controller specification, automated tabular consistency checking, test case generation.

## AI & Agentic Adaptation

The SCR toolset automatically checks tabular disjointness and coverage using embedded tautology checkers, runs model checkers, and auto-generates C source code from validated tables.
