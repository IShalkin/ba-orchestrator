---
id: business-process-modelling-bpmn-swimlanes
name: "Business Process Modelling (BPMN, Swimlanes)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 5
---

# Business Process Modelling (BPMN, Swimlanes)

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

**Also described as:** Business Process Modeling (As-Is and To-Be Modeling); Business Process Modelling / BPMN; Business process modelling; Process Modelling; Swimlane Diagram (Cross-Functional Flowchart)

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Models cross-functional end-to-end workflows across actor swimlanes, reducing functional silo bottlenecks, handoff failures, and lack of customer focus.

**[Variant B]**

Reduces operational ambiguity and alignment gaps by creating a visual, standardized sequential flow of work across roles, tasks, and system boundaries.

**[Variant C]**

Reduces uncertainty and misalignment in business process automation by identifying current process bottlenecks, manual inefficiency, and gaps before building software.

**[Variant D]**

Clarifies multi-actor business processes, role responsibilities, cross-departmental handoffs, and system-user interactions.

**[Variant E]**

Not understanding the sequence of work and the areas of responsibility

## Uncertainty Reduced

**[Variant E]**

Chaos in operations, loops and bottlenecks

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Business Process Analysis / Specification

**[Variant B]**

Discovery / elicitation / analysis / specification / architecture

**[Variant C]**

elicitation / analysis / specification

**[Variant D]**

elicitation

**[Variant E]**

Analysis, specification, design definition

## Input Artifacts

**[Variant A]**

Business Events, Value Chain, Task descriptions, stakeholder input.

**[Variant B]**

Elicitation notes, worker interviews, observation logs, current procedures.

**[Variant C]**

Organization charts, current operational documentation, user interview notes, industry process standards.

**[Variant D]**

Elicitation interviews, business process documentation, DFD processes, ecosystem map

**[Variant E]**

Interviews, regulations, observations, business goals

## Output Artifacts

**[Variant A]**

Business Process Model / Swimlane Diagram (Event trigger, Actor swimlanes, Tasks, Decisions, Sequences, Outcomes, Timeline).

**[Variant B]**

Process Maps / Flowcharts (BPMN, UML Activity Diagrams, Swimlane Diagrams, As-Is/To-Be models).

**[Variant C]**

As-is process flows, to-be process flows, swimlane diagrams, activity diagrams, flowcharts, use cases.

**[Variant D]**

Swimlane diagram with visual lanes for actors/systems, process rectangles, decision diamonds, and transition arrows.

**[Variant E]**

Result: 'as-is' and 'to-be' process models with swimlanes. Artifacts: BPMN diagram, role matrix

## Participants & Roles

**[Variant A]**

BA (Facilitator), Actors / SMEs from participating departments.

**[Variant B]**

BA, Process Modeller, Process Owner, Process Participants, Developer.

**[Variant C]**

Business Analyst (lead), SME / End User (process actors), Business Owner / Sponsor, Developer.

**[Variant D]**

BA, Business Owners/SMEs, Process Execution Staff, Developers

**[Variant E]**

BA, Process Owner, End User, Developer

## Prerequisites

**[Variant A]**

Identification of the initiating business event and expected process outcome.

**[Variant B]**

Understanding of process trigger events, participating roles, activities, and outcomes.

**[Variant C]**

Documented business objectives linked to business processes, identified affected organizations and user classes.

**[Variant D]**

Identified process scope, boundary events (trigger and outcome), and participating roles or system components.

## Step-by-Step Procedure

**[Variant A]**

Define initiating business event and end outcome.
2. Identify participating actor roles and create horizontal swimlanes.
3. Plot tasks in appropriate actor swimlanes in sequential flow order.
4. Add decision points and alternative pathways.
5. Rationalize steps into discrete tasks.
6. Add timeline performance measures.
7. Number tasks hierarchically.

**[Variant B]**

Identify process boundary (trigger event, initial inputs, final outputs/outcomes).
2. Identify participating roles and represent them as swimlanes or pools.
3. Map sequential activities, tasks, and sub-processes in chronological flow.
4. Add decision gateways (exclusive/parallel) and conditional branching logic.
5. Annotate data inputs/outputs and data store interactions.
6. Validate model flow ('As-Is' or 'To-Be') with process participants and owners.

**[Variant C]**

Understand business objectives and link each objective to specific processes.
2. Identify affected organizations and potential user classes via organization charts.
3. Identify all relevant business processes involving those user classes.
4. Document as-is business processes using flowcharts, activity diagrams, or swimlane diagrams.
5. Analyze as-is processes to identify bottlenecks and automation opportunities (optionally overlay metrics via KPIM).
6. Walk through as-is process flows with stakeholders to elicit software requirements for each step.
7. Trace software requirements to process flow steps to confirm scope.
8. Document to-be process flows and use cases to detail future interactions and transition requirements.

**[Variant D]**

Identify the visual lanes corresponding to participating roles, departments, or systems.
2. Map the trigger/start event in the appropriate lane.
3. Sequence process steps (rectangles) chronologically across lanes.
4. Add decision diamonds with labeled outgoing branches for alternative paths.
5. Draw directional arrows representing process transitions between steps and across lanes.
6. Review flow with cross-functional stakeholders to verify step handoffs.

**[Variant E]**

1. Define the process boundaries and triggers.
2. Record the steps and decisions.
3. Add roles (swimlanes).
4. Analyse the bottlenecks.

## Analyst Questions & Prompts

**[Variant A]**

What event starts this process? Who performs the first task? To whom is the work handed off next? What decision routes exist? What is the final outcome?

**[Variant B]**

"What event triggers this process?", "Who is responsible for executing step X?", "What decision rule governs this gateway branch?"

**[Variant C]**

How do users currently perform these tasks? Where are the major delays or bottlenecks? Which process steps are manual versus automated? What transition gaps or manual steps need to be retired?

**[Variant D]**

Who performs this step? What decision choices exist at this point? What system or role receives the output of this action?

**[Variant E]**

'What triggers the process?', 'Who makes the decision at this branch point?'

## Minimal Realistic Example

**[Variant A]**

A 'Record booking' process model showing initiating event 'Booking received' in Sales Clerk swimlane, handoff to Event Organiser swimlane for 'Complete booking arrangements', leading to end outcome.

**[Variant B]**

A BPMN diagram maps 'Order Processing': 'Customer' places order -> 'Sales Swimlane' validates order -> 'Gateway' checks inventory -> 'Warehouse Swimlane' ships product.

**[Variant C]**

Mapping a loan application process showing risk managers spending hours assembling spreadsheet data manually, then designing a to-be flow where data inputs are pulled automatically into the calculation tool.

**[Variant D]**

'Order a chemical' process mapped across 'Requester', 'Stockroom', 'Buyer', and 'Vendor' lanes showing request creation, approval routing, vendor order placement, and container shipping.

**[Variant E]**

Modelling the customer order-handling process from creation to shipment

## Quality Criteria & Verification

**[Variant A]**

Cross-functional visibility across swimlanes; clear event start and outcome end; rationalized tasks (one actor at one point in time); hierarchical task numbering.

**[Variant B]**

Follows standard notation syntax (e.g., BPMN 2.0); clear start/end events; validated for accuracy by actual process workers.

**[Variant C]**

Process models are walkable with stakeholders for validation; all in-scope process steps have requirements traced to them; end users confirm accuracy of steps and roles.

**[Variant D]**

Ensure all process paths lead to valid end states; verify data inputs and outputs match corresponding DFD process flows; perform stakeholder walkthroughs.

**[Variant E]**

Walking through an end-to-end scenario with the process owner

## Errors & Anti-Patterns

**[Variant A]**

Over-detailing micro-steps inside swimlanes instead of rationalizing into tasks; creating 'silo' models contained in a single swimlane; omitting handoff triggers.

**[Variant B]**

Mixing process flow with complex embedded business rules (make decision rules separate); drawing unwieldy monolithic diagrams without sub-process decomposition.

**[Variant C]**

Over-modeling the as-is state down to irrelevant details; automating a broken manual process without redesigning it; assuming software alone will fix process shortcomings without process/culture change.

**[Variant D]**

Including entities that fall outside system scope without reconciling with context diagrams; misrepresenting system-automated steps as manual role actions.

**[Variant E]**

Excessive detail or omitted exceptions

## When NOT to Use

**[Variant A]**

For static data modeling or high-level conceptual business activity mapping.

**[Variant B]**

When describing static entity relationships (use Data Modelling) or high-level organizational structures (use Org Modelling).

**[Variant C]**

When process problems stem purely from lack of operational execution or missing roles rather than system gaps, or when minor low-risk changes do not justify formal flow modeling.

**[Variant D]**

When attempting to detail data structures, complex numerical logic, or object state changes without clear sequential workflows.

**[Variant E]**

Static, non-process tasks; creative research

## Alternatives & Complementary Methods

**[Variant A]**

Swimlane diagrams, Process maps, Activity Diagrams, Value Streams.

**[Variant B]**

Complemented by Business Rules Analysis, Decision Modelling, Use Cases, Value Stream Mapping, and Sequence Diagrams.

**[Variant C]**

Data Flow Diagrams (DFDs), Key Performance Indicator Model (KPIM), Use Case Modeling, Value Stream Mapping.

**[Variant D]**

UML Activity Diagram, Data Flow Diagram, Use Case Specification.

**[Variant E]**

Textual scenarios, functional decomposition

## Supported Decisions

**[Variant A]**

End-to-end process redesign, handoff optimization, job role design, SLA definition, IT automation boundaries.

**[Variant B]**

Target operating model design, automation workflow spec, role responsibility assignment.

**[Variant C]**

Scope determination (which process steps to automate vs. keep manual), release phase planning, operational process change decisions.

**[Variant D]**

Scope, acceptance, process change.

**[Variant E]**

Scope, architecture, acceptance

## AI & Agentic Adaptation

**[Variant A]**

Process mining tools automatically ingest cross-departmental log data to generate 'as is' swimlane models and highlight real-world handoff delays.

**[Variant B]**

AI models can translate natural language process descriptions directly into valid BPMN XML diagrams, validating structural syntax automatically.

**[Variant C]**

Not in source

**[Variant D]**

Not in source

**[Variant E]**

Generating BPMN diagrams from textual descriptions with an LLM
