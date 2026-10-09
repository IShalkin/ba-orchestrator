---
id: state-machine-modelling
name: "State Machine Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.3"
subtask_name: "Behaviour and Interactions"
source_count: 7
---

# State Machine Modelling

`T4 Modelling and Analysis › 4.3 Behaviour and Interactions`

**Also described as:** State Diagrams; State Machine Diagrams & UML Statecharts; State Machine Diagrams / Statecharts; State Modelling; State machine diagrams; State-Transition Diagram (STD) and State Table; State-Transition Matrices

This card merges 7 descriptions of the method, labelled Variant A–G in every field.

## Problem Solved

**[Variant A]**

Reduces incompleteness and ambiguity in reactive component behaviors across all possible event occurrences and state transitions.

**[Variant B]**

Models the permissible states, state transitions, triggering events, and guard conditions for a specific business entity/class over its lifecycle, eliminating invalid state changes.

**[Variant C]**

Reduces logic gaps and invalid status transition errors by analyzing the distinct lifecycle states of an entity, allowed transitions, and triggering events.

**[Variant D]**

Models entity life cycles and identifies missing state-transition functions or illegal event sequences.

**[Variant E]**

Reduces behavioral uncertainty in reactive systems by formalizing all admissible state transitions, event triggers, and guard conditions for controlled system components.

**[Variant F]**

Resolves uncertainty and prevents missing/disallowed state transition logic in object or system life cycles.

**[Variant G]**

Exhaustively analyzes all combinations of states and events to uncover hidden requirements, edge cases, and illegal operations.

## BA Lifecycle Phase

**[Variant A]**

Specification / validation / verification

**[Variant B]**

Define Requirements / Requirements Modelling / Specification

**[Variant C]**

analysis / specification / architecture

**[Variant D]**

analysis

**[Variant E]**

Specification / behavioral modeling

**[Variant F]**

analysis

**[Variant G]**

analysis

## Input Artifacts

**[Variant A]**

Controlled state variables, events, guard conditions, operations, scenarios.

**[Variant B]**

Class Model, Task Descriptions, Business Rules, Use Cases.

**[Variant C]**

Data Models, business rules, process models, use cases.

**[Variant D]**

Data model, event list, business rules.

**[Variant E]**

Controlled system variables, interaction scenarios, event definitions.

**[Variant F]**

Use cases, functional requirements, entity definitions, business rules

**[Variant G]**

State diagram, event list, data model.

## Output Artifacts

**[Variant A]**

State Machine diagrams, UML Statecharts, Labelled Transition Systems (LTS), concurrent/hierarchical state diagrams.

**[Variant B]**

State Machine Diagram / Statechart (Initial state, States, Transition arrows, Events, Guard conditions, Actions, Final state).

**[Variant C]**

State Transition Diagram, State Table (States, Transitions, Events, Conditions, Actions).

**[Variant D]**

State transition diagram (State boxes, Event transition arrows, Start/End markers).

**[Variant E]**

State Machine (SM) diagrams, Statecharts, transition matrices.

**[Variant F]**

State-Transition Diagram (boxes/circles for states, arrows for transitions) or State Table (matrix of states vs. states with transition triggers)

**[Variant G]**

State-Transition Matrix (Events on Y-axis, States on X-axis, cell actions/next-states).

## Participants & Roles

**[Variant A]**

BA, Software Engineer, Control Engineer, Verification Specialist.

**[Variant B]**

BA, System Architect, Business Rules SME, Developers, Testers.

**[Variant C]**

BA, Systems Analyst, Domain SME, Developer, Tester.

**[Variant D]**

BA, system architect, developer, SME.

**[Variant E]**

Requirements Engineer / Behavioral Analyst, Embedded Systems / Software Architect.

**[Variant F]**

BA, SMEs/Users, Developers, Testers

**[Variant G]**

BA, system architect, developer, tester.

## Prerequisites

**[Variant A]**

Controlled state variables, events, and candidate state transitions are identified.

**[Variant B]**

Identification of a complex entity/class with multiple lifecycle states.

**[Variant C]**

Identification of a complex business entity with multiple distinct status states.

**[Variant D]**

Identification of entities with multi-state life cycles.

**[Variant E]**

Identified controlled state variables and external triggering events.

**[Variant F]**

Identification of key business objects with multi-stage life cycles (e.g., requests, orders, accounts).

**[Variant G]**

Complete list of entity states and possible system events.

## Step-by-Step Procedure

**[Variant A]**

Identify state variables controlled by the agent.
2. Define SM states as classes of snapshot states.
3. Define transitions between states, labelled by triggering events, guard conditions brackets, and auxiliary actions /slash.
4. Decompose complex states into sequential sub-states or parallel concurrent sub-states.
5. Define initial and final sub-states for entry/exit control.
6. Verify determinism, reachability, and absence of deadlocks.

**[Variant B]**

Draw Initial state (solid circle).
2. Identify valid lifecycle States (rounded boxes).
3. Draw directional Transition arrows between valid states.
4. Label transitions with syntax: Event Guard condition / Action.
5. Draw Final state (bulls-eye circle).
6. Verify illegal transitions are blocked.

**[Variant C]**

Identify the core entity with complex lifecycle behaviour (e.g., Order, Claim, Account).
2. Elicit all possible valid states the entity can inhabit from creation to retirement.
3. Identify initial start state and final end state.
4. Define valid transitions from one state to another.
5. Specify events, guard conditions, and resulting actions for each transition.
6. Document visually via State Diagram or structurally via State Table, and validate with SMEs.

**[Variant D]**

Select a complex entity or dialog object.
2. Identify all valid operational states of the entity (rounded boxes).
3. Draw arrows between states representing allowable event transitions.
4. Annotate arrows with the triggering event names.
5. Identify dead ends, missing transition events, or unreachable states.
6. Validate life cycle transitions with SMEs.

**[Variant E]**

Identify the controlled variable and its discrete equivalence states (e.g., doorsClosed, doorsOpen).
2. Define the initial state and final states.
3. Identify external triggering events causing state changes.
4. Define guarded transitions: 'If in State S1 and Event EV occurs when Guard G holds, move to State S2.'
5. (Statecharts) Organize concurrent sub-states using parallel composition to avoid state explosion.
6. Verify determinism (no multiple outgoing transitions with identical triggers/guards).

**[Variant F]**

List all valid states an object can assume from creation to termination.
2. Create an N x N matrix (State Table) or visual STD layout with state nodes.
3. For each state pair, evaluate if a direct transition is permissible.
4. Label valid transitions with the triggering event, condition, and resulting system response.
5. Verify termination states (nodes with incoming arrows but no outgoing arrows).
6. Cross-check STD paths against state tables to ensure no valid transition is omitted and no illegal transition is permitted.

**[Variant G]**

List all entity states along the horizontal axis.
2. List all possible system events along the vertical axis.
3. Systematically evaluate every intersecting matrix cell.
4. Specify the resulting new state, error action, or invalid indicator (-) in each cell.
5. Add explanatory footnotes for complex cell actions or edge cases.
6. Review edge cases with SMEs.

## Analyst Questions & Prompts

**[Variant A]**

What state is the component in? What event triggers this transition? What guard condition must hold for this transition to fire? What concurrent sub-states evolve in parallel?

**[Variant B]**

What states can this object exist in? What event triggers a transition from State A to State B? What guard condition must be true? What state transitions are illegal?

**[Variant C]**

"What states can entity X be in?", "What event triggers a transition from state A to state B?", "Under what condition is a transition prohibited?"

**[Variant D]**

What state does this room enter when cancelled? Can a booked room transition directly to repair?

**[Variant E]**

What state is the component in initially? What event triggers a transition from state A to B? What guard condition prevents this transition?

**[Variant F]**

What states can this object exist in? What event triggers a state change from State A to State B? Are there states where no further transition is allowed?

**[Variant G]**

What happens if a 'Cancel' event arrives while the room is in 'Occupied' state? What if 'ChangeRoom' occurs during 'Booked' state?

## Minimal Realistic Example

**[Variant A]**

A statechart for 'Train' showing parallel states 'MovementState' (Stopped, Moving) and 'DoorsState' (Closed, Open), where 'Open' is guarded by Speed = 0.

**[Variant B]**

Modeling 'Order' class: Placed -> Picked -> Despatched -> Delivered -> If <28 days Refunded vs 28 days after delivery -> Finalised, blocking 'Cancel' after 'Despatched'.

**[Variant C]**

An 'Order' entity states: 'New' -> (event: Payment Received) -> 'Paid' -> (event: Ship) -> 'Shipped' -> (event: Deliver) -> 'Closed'. If Payment Fails -> 'Cancelled'.

**[Variant D]**

Entity 'RoomState' with states (Free, Booked, Occupied, Repair) connected by event arrows (book, checkin, checkout, cancel, repair).

**[Variant E]**

Modeling a train door state machine: From 'doorsClosed' state, receiving event 'opening' when speed = 0 transitions component to 'doorsOpen' state.

**[Variant F]**

A Chemical Request moves through states: InPreparation -> Postponed -> Accepted -> Placed -> Back-Ordered -> Fulfilled / Canceled.

**[Variant G]**

Matrix with 4 states and 7 events; cell for Event 'Checkin' in State 'Booked' transitions to State 'Occupied' with footnote explaining stay date handling.

## Quality Criteria & Verification

**[Variant A]**

Determinism (no identical event/guard causing multiple transitions from one state); reachability of all states; coverage of all valid event occurrences; absence of race conditions.

**[Variant B]**

Complete lifecycle coverage from initial to final state; explicit guard conditions on conditional transitions; impossible illegal transitions explicitly prevented.

**[Variant C]**

All valid entity states accounted for; no 'dead end' states (except final state); transitions governed by explicit events/rules.

**[Variant D]**

Verification against developer implementation code, state coverage test design.

**[Variant E]**

Determinism verification; deadlock/unreachable state detection; model checking against temporal safety goals; coverage of scenario traces.

**[Variant F]**

Complete coverage of all matrix cells in the state table; verification that termination states do not allow exit transitions; test coverage derived from all allowed state transition paths.

**[Variant G]**

100% matrix cell coverage check, edge-case test suite generation.

## Errors & Anti-Patterns

**[Variant A]**

Combinatorial explosion of states due to flat representation of concurrent variables; non-deterministic transition definitions; un-synchronized parallel state machines causing implied scenarios.

**[Variant B]**

Creating state charts for simple entities with only 2 trivial states; cluttering diagrams with obvious redundant event labels; missing exit guard conditions.

**[Variant C]**

Confusing state diagrams with process flow diagrams; missing exception transition paths.

**[Variant D]**

Creating state diagrams for simple entities that have trivial two-state life cycles (Exists/Deleted).

**[Variant E]**

Combinatorial state explosion due to monolithic design without parallel statecharts; non-deterministic transitions; confusing states (durations) with events (instantaneous).

**[Variant F]**

Missing vital states; permitting disallowed transitions; failing to document requirements for what system processing causes state changes.

**[Variant G]**

Applying to huge systems with hundreds of states, resulting in massive, sparse, unreadable matrices.

## When NOT to Use

**[Variant A]**

For simple, non-reactive data-transformation applications without state-dependent behaviors.

**[Variant B]**

For simple stateless data lookups or static reference tables with no lifecycle state changes.

**[Variant C]**

For simple entities that possess no complex status changes or lifecycle rules.

**[Variant D]**

Simple data entities without multi-state transitions.

**[Variant E]**

For simple sequential data-processing batch applications where state transitions are irrelevant.

**[Variant F]**

For systems or objects that are stateless or whose behavior is purely procedural without defined status life cycles.

**[Variant G]**

Simple entities or large systems where a state diagram gives a cleaner visual overview.

## Alternatives & Complementary Methods

**[Variant A]**

Decision tables, R-net diagrams, Goal-derived State Machines.

**[Variant B]**

Statecharts, State Transition Diagrams, Activity Diagrams, Business Rules Analysis.

**[Variant C]**

Complemented by Data Modelling, Business Rules Analysis, Process Modelling, and Use Cases.

**[Variant D]**

State-Transition Matrices, Activity Diagrams, Sequence Diagrams.

**[Variant E]**

Complementary: Event Trace Diagrams, Goal Models, SCR. Alternative: Decision Tables.

**[Variant F]**

UML State Machine Diagram, Event-Response Table, Decision Table.

**[Variant G]**

State Diagrams, Decision Tables.

## Supported Decisions

**[Variant A]**

Reactive controller design, code generation, model checking verification.

**[Variant B]**

Entity lifecycle business rule specification, system state validation logic, negative test case generation.

**[Variant C]**

System status logic specification, data lifecycle governance, exception handling design.

**[Variant D]**

Entity life cycle design, UI navigation map design, event validation logic.

**[Variant E]**

Reactive controller logic design, safety verification, state-based system testing.

**[Variant F]**

Architecture, acceptance, release.

**[Variant G]**

Robust event handling architecture, error handling design, complete test suite generation.

## AI & Agentic Adaptation

**[Variant A]**

Model checkers (SPIN, NuSMV) can automatically parse statechart specifications, explore reachability graphs containing millions of states, and generate concrete counterexample traces when safety goals are violated.

**[Variant B]**

AI code generators convert State Machine Diagrams directly into executable state-machine software classes and negative test scripts.

**[Variant C]**

AI agents can analyze entity specs to generate state transition tables automatically, verifying that no invalid state transitions or orphan states exist.

**[Variant D]**

Extract entity states and valid transition triggers from requirement text to construct PlantUML state diagrams automatically.

**[Variant E]**

Model-checking AI tools can verify statecharts for deadlocks, synthesize state machines directly from event trace scenarios, and output counterexamples.

**[Variant F]**

Not in source

**[Variant G]**

Automatically populate state-transition matrix cells and flag undefined state-event combinations using AI logic engines.
