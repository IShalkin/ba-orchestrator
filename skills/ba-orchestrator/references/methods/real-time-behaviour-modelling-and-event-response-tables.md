---
id: real-time-behaviour-modelling-and-event-response-tables
name: "Real-Time Behaviour Modelling and Event-Response Tables"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.3"
subtask_name: "Behaviour and Interactions"
source_count: 2
---

# Real-Time Behaviour Modelling and Event-Response Tables

`T4 Modelling and Analysis › 4.3 Behaviour and Interactions`

**Also described as:** Event-Response Table; Real-Time System Behavioral Modeling (STD and Event-Response Analysis)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces logical gaps, unhandled exception states, and timing hazards in hardware-controlling software by explicitly modeling allowed state changes, triggering events, and system responses.

**[Variant B]**

Identifies functional requirements for systems (especially real-time/control systems) that are driven by external inputs rather than user-driven workflows.

## BA Lifecycle Phase

**[Variant A]**

analysis / specification

**[Variant B]**

elicitation

## Input Artifacts

**[Variant A]**

System requirements, hardware interface constraints, sensor inputs, operational profiles.

**[Variant B]**

Context diagrams, hardware/software interface specs, system state specifications

## Output Artifacts

**[Variant A]**

State-Transition Diagrams (STD) / Statechart Diagrams, Event-Response Tables, State Tables, Interface Specifications.

**[Variant B]**

Event-Response Table (columns: Event ID, Event Name/Trigger, System State, System Response, Resulting State)

## Participants & Roles

**[Variant A]**

Business Analyst / Requirements Engineer, System Architect, Embedded Software Developer, Tester.

**[Variant B]**

BA, Systems/Hardware Engineers, Developers, Testers

## Prerequisites

**[Variant A]**

Known system boundary, external entities, and high-level operating states.

**[Variant B]**

Defined system boundary, identified external entities, and known system states.

## Step-by-Step Procedure

**[Variant A]**

Identify all operational states the system can inhabit (e.g., Power Off, Idle, Running, Paused, Error).
2. Identify events (business, signal/sensor, temporal) that impact the system.
3. Map allowed transitions between states on a State-Transition Diagram labeled with triggering conditions.
4. Construct an Event-Response Table detailing the system state, incoming event, explicit system response, and resulting state.
5. Analyze the models for missing transitions, unhandled error/exception conditions, or missing turn-off mechanisms.
6. Derive detailed functional and safety requirements from the resulting event-response matrix.

**[Variant B]**

Identify all external business events (user actions), signal events (hardware/software interrupts), and temporal events (time triggers).
2. List valid system states in which each event can occur.
3. Define expected system behaviors/responses for each event-state combination.
4. Add contextual details such as event frequency, data elements needed, and resulting system state.
5. Validate that all external triggers from the context diagram are accounted for in the table.

## Analyst Questions & Prompts

**[Variant A]**

What state must the system be in for this event to occur? What triggers a transition from State A to State B? What happens if an unexpected signal is received in this state? How does the system handle an error while running? What periodic control actions occur while in this state?

**[Variant B]**

What external events stimulate a response from the system? How should the system respond to this event if it is in State X versus State Y? What time-triggered events must occur periodically?

## Minimal Realistic Example

**[Variant A]**

Creating an event-response table for an exercise treadmill specifying that pressing 'Pause' while 'Running' stops the belt and starts a timer, whereas pressing 'Pause' while 'Idle' generates an error audio signal.

**[Variant B]**

Windshield Wiper System: Event 'Set wiper control to low speed' while System State is 'Wiper off' produces System Response 'Set wiper motor to low speed'.

## Quality Criteria & Verification

**[Variant A]**

Cross-verifying State-Transition Diagrams against Event-Response Tables to detect missing states/transitions; peer reviews by developers and testers; verifying timing tolerances and safety limits.

**[Variant B]**

Verification against context diagram terminators; complete coverage of all valid event-state combinations; direct mapping to test scenarios.

## Errors & Anti-Patterns

**[Variant A]**

Creating state diagrams without defining explicit guard conditions or responses; omitting error or power-down states; failing to account for combined multi-fault conditions.

**[Variant B]**

Specifying implementation details (e.g., physical switch hardware) rather than essential functional behavior; omitting temporal or exception events.

## When NOT to Use

**[Variant A]**

Simple CRUD business applications with no state-dependent logic or event-driven execution flows.

**[Variant B]**

For simple CRUD administrative applications driven solely by sequential user forms.

## Alternatives & Complementary Methods

**[Variant A]**

UML State Machine Diagrams, Decision Tables, Context Diagrams, Use Case Modeling.

**[Variant B]**

Use Case Specifications, State-Transition Diagrams, Decision Tables.

## Supported Decisions

**[Variant A]**

Software architecture decisions, safety mechanism selection, test case design, error-handling strategy.

**[Variant B]**

Scope, architecture, acceptance.

## AI & Agentic Adaptation

**[Variant A]**

Not in source

**[Variant B]**

Not in source
