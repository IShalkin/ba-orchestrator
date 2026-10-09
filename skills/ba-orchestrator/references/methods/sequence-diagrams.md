---
id: sequence-diagrams
name: "Sequence Diagrams"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.3"
subtask_name: "Behaviour and Interactions"
source_count: 4
---

# Sequence Diagrams

`T4 Modelling and Analysis › 4.3 Behaviour and Interactions`

**Also described as:** Analysis Sequence Diagramming / Role Playing; Event Trace Diagrams & UML Sequence Diagrams

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Reduces confusion regarding the temporal sequence, message passing, and event ordering during component interactions.

**[Variant B]**

Reduces object interaction and logic errors in technical software design by visually depicting message exchanges between objects/systems over time in a chronological scenario.

**[Variant C]**

Specifies dynamic, time-ordered message sequences, synchronous/asynchronous events, and protocol handshakes between actors or technical components.

**[Variant D]**

Reduces ambiguous interactions and unassigned dynamic responsibilities by mapping step-by-step object message passing for a use case.

## BA Lifecycle Phase

**[Variant A]**

Elicitation / specification / validation

**[Variant B]**

analysis / specification / architecture

**[Variant C]**

design

**[Variant D]**

Analysis / specification

## Input Artifacts

**[Variant A]**

System scenarios, agent instances, interaction events.

**[Variant B]**

Use cases, scenarios, Class Diagrams, interface specs.

**[Variant C]**

Use cases, interface specifications, event lists.

**[Variant D]**

Base/Elaborated Use Cases, Analysis Object Model, CRC Cards.

## Output Artifacts

**[Variant A]**

Event Trace diagrams, Message Sequence Charts (MSCs), UML Sequence Diagrams.

**[Variant B]**

Sequence Diagram (Lifelines, Activation Boxes, Synchronous/Asynchronous Messages, Calls, Responses, Destruction).

**[Variant C]**

UML Sequence Diagram (Actor lifelines, activation bars, synchronous/asynchronous arrows, reply lines).

**[Variant D]**

Analysis Sequence Diagrams, Collaboration Diagrams, updated CRC Cards.

## Participants & Roles

**[Variant A]**

BA, System Architect, Developer, Tester.

**[Variant B]**

BA, Systems Analyst, Software Developer, Systems Architect.

**[Variant C]**

System architect, developer, integration engineer.

**[Variant D]**

BA/System Analyst, Architect, Developer, SME.

## Prerequisites

**[Variant A]**

Interacting agent instances and candidate interaction events are identified.

**[Variant B]**

Defined use case scenario and participating software objects/classes.

**[Variant C]**

Identification of communicating components and message types.

**[Variant D]**

Base flow of events and candidate domain objects defined.

## Step-by-Step Procedure

**[Variant A]**

Identify participating agent instances and represent them as vertical lifelines.
2. Arrange interaction events chronologically down the lifelines as horizontal directed arrows.
3. Annotate event arrows with event names and data attributes.
4. Represent optional/alternative branches using frames (opt, alt, neg).
5. Decorate lifelines with explicit state condition lists (monitored and controlled variables) if needed for synthesis or analysis.

**[Variant B]**

Identify scenario/use case path to model.
2. Lay out participating objects/systems as boxes horizontally across top.
3. Draw vertical dashed lifelines descending from each object.
4. Draw activation boxes on lifelines to show when operation executes.
5. Draw horizontal message arrows between lifelines in top-down chronological order.
6. Label messages (synchronous calls, asynchronous signals, return responses, destruction).

**[Variant C]**

Place communicating actors/components horizontally across the top.
2. Draw vertical dashed lifelines extending downwards representing time.
3. Draw horizontal message arrows between lifelines in chronological order.
4. Use solid black arrowheads for synchronous calls and half arrowheads for asynchronous messages.
5. Add activation boxes on lifelines showing execution duration.
6. Draw dashed return arrows for reply messages.

**[Variant D]**

Lay out participating objects (Entity, Interface, Control) across top horizontal axis.
2. Draw lifeline for each object vertically.
3. Walk through use case steps and model message requests sequentially from top to bottom.
4. Assign message names corresponding to receiving object's responsibilities.
5. Add return messages and explanatory margin text where needed.

## Analyst Questions & Prompts

**[Variant A]**

Which agent controls this event? Which agent monitors it? What is the exact sequence of messages exchanged in this scenario?

**[Variant B]**

"Which object initiates the first message in this scenario?", "Is this call synchronous (blocking) or asynchronous?", "What response message is returned to object A?"

**[Variant C]**

Does the sender wait for a reply before continuing? What exact data payload is returned in the handshake reply?

**[Variant D]**

Which object receives this request? What responsibility must it execute to return the expected result?

## Minimal Realistic Example

**[Variant A]**

A sequence diagram showing 'Initiator' sending 'meetingRequest(dateRange)' to 'Scheduler', followed by 'Scheduler' sending '?constraints' to 'Participant'.

**[Variant B]**

Sequence diagram shows 'User' -> (submits login) -> 'UI' -> (validates) -> 'Auth Server' -> (returns token) -> 'UI' -> (displays dashboard) -> 'User'.

**[Variant C]**

Sequence showing 'Product' sending 'Transfer' event to 'Account System', receiving 'OK' reply, followed by sequential data packet messages and a 'Done' notification.

**[Variant D]**

Applicant sends 'Submit Application' -> Boundary Object -> Control Object -> Credit Bureau Object 'Request Credit Report' -> returns report.

## Quality Criteria & Verification

**[Variant A]**

Total ordering of events along individual lifelines; correct event attribute labeling; alignment with higher-level goals or state machines.

**[Variant B]**

Strict UML notation syntax; chronological top-down message order; logic matches use case scenario steps accurately.

**[Variant C]**

Protocol conformance testing, interface verification testing.

**[Variant D]**

Peer review; verify that every message maps to a valid object responsibility and covers the complete use case flow.

## Errors & Anti-Patterns

**[Variant A]**

Including non-instantaneous macro-events without decomposition; depicting interactions controlled by agents incapable of controlling them; partial scenario misinterpretation as global system rules.

**[Variant B]**

Over-complicating diagrams by trying to represent every possible alternate flow in a single diagram; creating sequence diagrams for non-technical business stakeholders.

**[Variant C]**

Failing to distinguish synchronous blocking calls from asynchronous events; using for broad, flexible user workflows.

**[Variant D]**

Premature technical design (e.g., adding database connection pools, socket protocols, language-specific code).

## When NOT to Use

**[Variant A]**

For specifying complete, exhaustive system-wide state transition rules (use State Machines instead).

**[Variant B]**

When communicating high-level business process workflows to non-technical business users (use BPMN or Flowcharts instead).

**[Variant C]**

Flexible, non-deterministic user interface screen workflows.

**[Variant D]**

Simple CRUD use cases with trivial single-object assignments.

## Alternatives & Complementary Methods

**[Variant A]**

State Machines, Use Cases, Storyboards.

**[Variant B]**

Alternatives/Complements include Use Cases, Activity Diagrams, Data Flow Diagrams, and Interface Analysis.

**[Variant C]**

Collaboration Diagrams, Activity Diagrams, State Diagrams.

**[Variant D]**

Collaboration Diagrams, Activity Diagrams, CRC Card Simulation.

## Supported Decisions

**[Variant A]**

Communication protocol design, interaction validation, test case generation.

**[Variant B]**

Detailed software design specification, API call structure, technical feasibility verification.

**[Variant C]**

Technical interface protocol design, dynamic API sequencing, sub-system integration design.

**[Variant D]**

Detailed architectural design, class method signature baseline, responsibility allocation.

## AI & Agentic Adaptation

**[Variant A]**

State machine synthesizers can ingest collections of sequence diagrams, automatically convert them into candidate Labelled Transition Systems (LTS), and ask interactive scenario questions to prune over-generalizations.

**[Variant B]**

AI agents can generate PlantUML or Mermaid sequence diagram code directly from narrative use case steps automatically.

**[Variant C]**

Generate PlantUML sequence diagrams automatically from API documentation or message trace logs using AI agents.

**[Variant D]**

Not specified in source.
