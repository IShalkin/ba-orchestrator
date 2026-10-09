---
id: activity-diagrams
name: "Activity Diagrams"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 2
---

# Activity Diagrams

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

**Also described as:** Activity diagrams

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Models detailed task steps, decision paths, and iterations using standardized UML flowchart notation, reducing procedural ambiguity in task execution.

**[Variant B]**

Models complex workflows involving parallel execution threads, swim lanes, and control/data synchronization across actors.

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Business Process Analysis / Specification

**[Variant B]**

analysis

## Input Artifacts

**[Variant A]**

Task descriptions, business rules, scenario scripts.

**[Variant B]**

Task descriptions, workflow models, event lists.

## Output Artifacts

**[Variant A]**

UML Activity Diagram (Start state, Activity steps, Decision diamonds with guard conditions, Merge points, End state).

**[Variant B]**

UML Activity Diagram (Swim lanes, Action barrels, Control flows, Objects, Fork/Join bars, Guard conditions).

## Participants & Roles

**[Variant A]**

BA, SMEs, System Users, Developers, Testers.

**[Variant B]**

BA, workflow architect, developer, SME.

## Prerequisites

**[Variant A]**

Identification of the specific task or procedure to be modeled.

**[Variant B]**

Identification of actors and workflow steps across boundaries.

## Step-by-Step Procedure

**[Variant A]**

Draw Start solid circle.
2. Draw rounded boxes for task steps in sequence.
3. Add decision diamonds where choices occur, labeling outbound flows with bracketed guard conditions e.g. code known.
4. Model iterations/loops where steps repeat.
5. Connect to End bulls-eye circle.

**[Variant B]**

Define swim lanes representing actors or subsystems.
2. Place action/activity rounded boxes in appropriate swim lanes.
3. Draw solid arrows showing sequential flow of control.
4. Add decision diamonds with guard conditions in brackets .
5. Add synchronization bars for parallel fork and join operations.
6. Draw dashed arrows for object/data flows between activities.

## Analyst Questions & Prompts

**[Variant A]**

What is the initial step? What choice occurs here? What is the guard condition for this path? Which steps repeat until a condition is met?

**[Variant B]**

Which steps occur in parallel? Which conditions trigger this branch? What data object is passed between these actors?

## Minimal Realistic Example

**[Variant A]**

Modeling a mail-order task: Ask customer for products -> Decision code known vs code unknown -> Display details -> Enter quantity -> Decision more products loop back vs no more -> Confirm order -> End.

**[Variant B]**

Workflow across 'Guest', 'Hotel', and 'Bank' swim lanes showing room checking, credit checks, and booking confirmation with fork/join synchronization.

## Quality Criteria & Verification

**[Variant A]**

Clear logical sequence; all decision diamond outbound paths labeled with mutually exclusive guard conditions; clear start and end points.

**[Variant B]**

Workflow walkthrough with SMEs, business process simulation.

## Errors & Anti-Patterns

**[Variant A]**

Missing guard conditions on decision branches; creating infinite loops without exit conditions; mixing high-level business workflow with micro-level task steps.

**[Variant B]**

Drawing control arrows across actor swim lanes instead of passing data objects; using activity diagrams as a replacement for structured programming flowcharts.

## When NOT to Use

**[Variant A]**

For high-level conceptual business activity mapping (use BAM instead) or static data structure design.

**[Variant B]**

Simple, single-user sequential screen interactions.

## Alternatives & Complementary Methods

**[Variant A]**

Flowcharting, Business Process Modelling, Task Analysis, Use Case Descriptions.

**[Variant B]**

Dataflow Diagrams, Task Descriptions, Sequence Diagrams.

## Supported Decisions

**[Variant A]**

Procedural task design, test script generation, user training manual documentation, exception handling logic.

**[Variant B]**

Workflow engine configuration, cross-system process integration, parallel processing architecture.

## AI & Agentic Adaptation

**[Variant A]**

Code-generation AI parses UML Activity Diagrams directly into executable workflow code and automated test scripts.

**[Variant B]**

Convert process descriptions into structured PlantUML activity diagrams complete with swimlanes and synchronization bars using LLMs.
