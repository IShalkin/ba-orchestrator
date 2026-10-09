---
id: collaboration-diagrams
name: "Collaboration Diagrams"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.3"
subtask_name: "Behaviour and Interactions"
source_count: 1
---

# Collaboration Diagrams

`T4 Modelling and Analysis › 4.3 Behaviour and Interactions`

## Problem Solved

Visualizes how software objects co-operate and exchange numbered message calls to complete a specific system function.

## BA Lifecycle Phase

design

## Input Artifacts

Class diagram, textual process descriptions, use cases.

## Output Artifacts

UML Collaboration Diagram (Object boxes, structural links, numbered message call arrows).

## Participants & Roles

System architect, developer.

## Prerequisites

Completed static class diagram.

## Step-by-Step Procedure

Identify the software objects involved in executing a specific function.
2. Draw structural link lines between co-operating objects.
3. Draw message arrows along the links indicating call direction.
4. Number messages sequentially (e.g., 1, 1.1, 1.1.1) to show call hierarchy.
5. Annotate messages with operation names and parameters.

## Analyst Questions & Prompts

Which object calls which method to gather this invoice line item? In what sequence do these sub-routine calls occur?

## Minimal Realistic Example

Object 'Stay' sends numbered message 1.1 *getService to 'Service', which in turn sends 1.1.1 getServicePrice to 'ServiceType'.

## Quality Criteria & Verification

Code walkthrough, object interaction testing.

## Errors & Anti-Patterns

Attempting to use collaboration diagrams for user interface requirements or non-technical stakeholder reviews.

## When NOT to Use

User interface requirements elicitation or high-level business process modeling.

## Alternatives & Complementary Methods

Sequence Diagrams, Activity Diagrams.

## Supported Decisions

Internal object interaction design, API internal sub-routine routing.

## AI & Agentic Adaptation

Parse multi-object execution traces into PlantUML collaboration diagrams automatically.
