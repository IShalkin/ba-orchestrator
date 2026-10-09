---
id: problem-frames-and-scope-diagrams
name: "Problem Frames and Scope Diagrams"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.3"
subtask_name: "Boundaries and Context"
source_count: 2
---

# Problem Frames and Scope Diagrams

`T2 Situation Investigation and Elicitation › 2.3 Boundaries and Context`

**Also described as:** Context Diagrams and Problem Diagrams (Problem Frames); System Scope Diagrams (Context, Problem, and Frame Diagrams)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces uncertainty regarding system scope, software-environment boundaries, shared phenomena, and misaligned machine assumptions.

**[Variant B]**

Reduces boundary ambiguity by defining the problem world components, the machine solution, shared interface phenomena, and the domain properties/requirements constraining them.

## BA Lifecycle Phase

**[Variant A]**

Specification / analysis

**[Variant B]**

Specification / domain modeling

## Input Artifacts

**[Variant A]**

System components, external devices, environmental phenomena, generic problem frames.

**[Variant B]**

Elicited system components, environmental phenomena, generic problem frames.

## Output Artifacts

**[Variant A]**

Context diagrams, problem diagrams, instantiated frame diagrams.

**[Variant B]**

Context diagrams, Problem diagrams, instantiated Frame diagrams.

## Participants & Roles

**[Variant A]**

BA, System Architect, SME.

**[Variant B]**

Requirements Engineer / Business Analyst, System Architect.

## Prerequisites

**[Variant A]**

System components, physical devices, and core interaction phenomena are known.

**[Variant B]**

Identified candidate system components (causal, biddable, lexical) and machine boundaries.

## Step-by-Step Procedure

**[Variant A]**

Identify the machine component to be built and surrounding environment components (causal, biddable, lexical).
2. Identify shared phenomena at component interfaces (events, state variables, commands).
3. Construct a Context Diagram showing components and directed shared phenomena.
4. Upgrade to a Problem Diagram by adding explicit requirement ovals, showing which components are referenced or constrained.
5. Alternatively, select a generic Frame Diagram (e.g., Simple Workpieces, Information Display), match parameters, and instantiate component/phenomena labels.

**[Variant B]**

Identify domain components (people, devices, legacy software) and the machine to be built.
2. Identify shared interface phenomena (events, signals, data) between components.
3. Draw a Context Diagram connecting components via shared phenomena edges.
4. Expand into a Problem Diagram by highlighting the Machine (double stripe), environment components (single stripe), and adding dashed ovals for requirements.
5. Annotate links showing which phenomena are monitored, controlled, or constrained by requirements.
6. (Frame Diagrams) Match the problem against generic frames (e.g., Simple Workpieces, Information Display) and instantiate typed parameters.

## Analyst Questions & Prompts

**[Variant A]**

What phenomena are controlled by the machine vs monitored by the environment? Which components are constrained by this requirement? Which generic problem frame matches this domain problem?

**[Variant B]**

Which component controls this event? Which environmental phenomena does the machine monitor? What requirement constrains this physical device?

## Minimal Realistic Example

**[Variant A]**

Instantiating the 'Information Display' frame for a meeting scheduler where the Machine monitors Date/Location from the Real World and issues Notifications to a Display component.

**[Variant B]**

Drawing a problem diagram showing the 'Scheduler' machine controlling 'meetingNotification' events monitored by the 'Participant' biddable domain component, constrained by a 'Convenient Date' requirement.

## Quality Criteria & Verification

**[Variant A]**

Clear separation of machine vs environment phenomena; accurate control/monitor interface labels; explicit mapping of requirements to constrained components.

**[Variant B]**

Verification that all machine interface phenomena are monitored/controlled by valid domain components; view integration checks against sequence diagrams.

## Errors & Anti-Patterns

**[Variant A]**

Confounding machine phenomena with world phenomena; omitting environmental components; fuzzy interface definitions.

**[Variant B]**

Confusing machine-internal phenomena with problem-world phenomena; drawing unclear component boundaries without explicit phenomenon labels.

## When NOT to Use

**[Variant A]**

When system boundaries and environmental interfaces are already rigidly fixed and fully specified.

**[Variant B]**

For internal software architectural design where problem-world domain components are irrelevant.

## Alternatives & Complementary Methods

**[Variant A]**

UML Use Case diagrams, Dataflow diagrams, Goal-derived Context diagrams.

**[Variant B]**

Complementary: Agent Diagrams, Use Case Diagrams. Alternative: High-level System Architecture Diagrams.

## Supported Decisions

**[Variant A]**

System scope boundary, automation boundary, interface specification.

**[Variant B]**

Defining the software-environment boundary, allocation of system vs software responsibilities.

## AI & Agentic Adaptation

**[Variant A]**

Agentic modeling tools can parse natural language problem statements, classify environment components by frame type, and auto-generate problem diagrams with interface control annotations.

**[Variant B]**

Agentic tools can parse problem text to identify causal/biddable entities and autogenerate problem frame diagrams in graphical formats.
