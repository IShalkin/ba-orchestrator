---
id: r-net-diagrams
name: "R-net Diagrams"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.3"
subtask_name: "Behaviour and Interactions"
source_count: 1
---

# R-net Diagrams

`T4 Modelling and Analysis › 4.3 Behaviour and Interactions`

## Problem Solved

Reduces ambiguity regarding all required parallel and conditional operational responses triggered by a single external stimulus.

## BA Lifecycle Phase

Specification / analysis

## Input Artifacts

External stimulus events, conditional decision rules, operational responses.

## Output Artifacts

R-net diagrams (response-net trees).

## Participants & Roles

BA, Real-time Systems Engineer.

## Prerequisites

External stimuli and required operational responses are identified.

## Step-by-Step Procedure

Identify an external stimulus event and place it as the hexagon root of the R-net tree.
2. Define operational response nodes (boxes) triggered by the stimulus.
3. Insert condition decision points (circles) to branch responses based on guard conditions.
4. Connect operations and decision points in precedence order.
5. Terminate branches with end-state or event-generation markers.

## Analyst Questions & Prompts

What are all the required system responses when stimulus X occurs? Under what specific condition is response Y required vs response Z?

## Minimal Realistic Example

An R-net rooted on 'MeetingRequest' branching via an 'Authorized' decision node to 'ValidateMeetingData' or 'DenyRequest'.

## Quality Criteria & Verification

Exhaustive coverage of all conditional response paths for the stimulus; consistency with state machine transitions.

## Errors & Anti-Patterns

Omitting required conditional response paths; confusing stimulus events with internal system actions.

## When NOT to Use

For non-real-time systems where stimulus-response dynamics are irrelevant.

## Alternatives & Complementary Methods

State Machine diagrams, Use Cases, Decision tables.

## Supported Decisions

Real-time stimulus handling, event-driven architecture design.

## AI & Agentic Adaptation

Automated tools can cross-check R-net response branches against decision tables to ensure every conditional response path is completely specified.
