---
id: context-diagram
name: "Context Diagram"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.3"
subtask_name: "Boundaries and Context"
source_count: 5
---

# Context Diagram

`T2 Situation Investigation and Elicitation › 2.3 Boundaries and Context`

**Also described as:** Context Diagramming & Event Analysis; Context diagram; Defining the Solution's Boundaries (Context Diagram & Ecosystem Map); System Boundary Definition (Context Diagramming)

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Defines the high-level scope and boundary of an IT or business system and its external interfacing actors, reducing scope creep and missed system interfaces.

**[Variant B]**

Defines product boundaries (scope) and reduces misunderstandings regarding external systems and user group interfaces.

**[Variant C]**

Eliminates scope creep by defining strict hard-system boundaries, external interfaces, and incoming/outgoing events.

**[Variant D]**

Reduces uncertainty regarding system scope, unaligned stakeholder expectations, and undefined external system interfaces.

**[Variant E]**

Prevents scope ambiguity, unbudgeted integration effort, interface mismatches, and uncoordinated upstream/downstream system impact.

## BA Lifecycle Phase

**[Variant A]**

Discovery / Specification / Documenting Results

**[Variant B]**

elicitation

**[Variant C]**

Discovery / Analysis / Specification

**[Variant D]**

Discovery / elicitation

**[Variant E]**

Discovery / Analysis / Specification

## Input Artifacts

**[Variant A]**

Project scope statement, stakeholder list, system boundary definition.

**[Variant B]**

Stakeholder lists, project inception documents, interface lists.

**[Variant C]**

Rich pictures, validated stakeholder list, domain boundary agreements

**[Variant D]**

Vision Document, Business Process Reengineering (BPR) results, stakeholder analysis, existing project documentation.

**[Variant E]**

Business Objectives, Product Vision, Solution Concept, existing system catalogs, corporate architecture diagrams.

## Output Artifacts

**[Variant A]**

Context Diagram showing central system box, surrounding external actors (user roles, other systems, time), and association lines.

**[Variant B]**

Black-box system context diagram with external entities and data/event flows.

**[Variant C]**

Context diagram, in/out scope list, incoming/outgoing event inventory, condition-action tables, 'when' requirements

**[Variant D]**

Context Diagram, system boundary definition section.

**[Variant E]**

Context Diagram, Ecosystem Map, Release Objectives Table / Scope Statement.

## Participants & Roles

**[Variant A]**

BA, System Architect, Business Users, Project Manager.

**[Variant B]**

BA, system architect, project manager, sponsor.

**[Variant C]**

BA, Architect, Developer, SME, Systems Engineer

**[Variant D]**

Sponsor, BA/System Analyst, SME, Facilitator.

**[Variant E]**

Business Analyst, Systems Architect, Product Owner, Owners of Connected Systems, Key Business Stakeholders.

## Prerequisites

**[Variant A]**

High-level understanding of the proposed system's intent and environment.

**[Variant B]**

High-level understanding of system purpose and surrounding environment.

**[Variant C]**

Agreed-upon soft system scope and identified external system neighbours.

**[Variant D]**

High-level understanding of system goals and business problem.

**[Variant E]**

Agreed-upon business objectives and refined solution concept.

## Step-by-Step Procedure

**[Variant A]**

Draw a central box representing the system.
2. Identify external user role actors (stick figures).
3. Identify other interfacing system actors (boxes).
4. Identify time-triggered actors (time boxes).
5. Draw un-arrowed association lines connecting actors to the system boundary.
6. Review boundary with stakeholders.

**[Variant B]**

Draw the product as a central black box.
2. Identify surrounding user groups and external technical systems.
3. Draw arrows representing data or event flows entering and leaving the central system.
4. Annotate each arrow with clear data descriptions.
5. Review and validate scope boundaries with stakeholders.

**[Variant C]**

Draw the proposed system/product as a single central box/circle.
2. Draw external entities (users, neighbouring hardware/software systems) outside the boundary.
3. Draw labeled data/signal/physical flow arrows crossing the boundary.
4. Compile an exhaustive event list for all incoming stimuli (external events and time triggers).
5. Define functional event-handling responses using 'When' statements or condition-action tables.
6. Explicitly document excluded items in an Out-of-Scope list.

**[Variant D]**

Draw a large circle representing the system.
2. Identify external entities surrounding the circle.
3. Identify interactions/information flows between external entities and system.
4. Draw directed lines showing the direction and nature of interactions.
5. Review and validate boundaries with stakeholders.

**[Variant E]**

Refine the high-level solution concept by determining which business processes are automated versus manual.
2. Identify the central system of interest and draw a circle representing the system boundary.
3. Identify all direct external entities (user classes, external systems, hardware devices) interacting with the system and place them outside the boundary.
4. Draw and label high-level data flows (arrows) connecting external entities and the system to form a Context Diagram.
5. Expand to an Ecosystem Map by depicting all interconnected systems in the domain and their data flows (APIs, files, queues).
6. Analyze interfaces to identify scope boundaries, derived integration requirements, and multi-release implementation objectives.

## Analyst Questions & Prompts

**[Variant A]**

What is the boundary of our system? Who are the human user roles interacting with it? What other IT systems send or receive data? What time events trigger system action?

**[Variant B]**

Is system X included inside our deliverable or is it external? What exact information flows between the user and the system?

**[Variant C]**

What external systems connect to this product? What exact signals/data cross the boundary? What events wake the system up? What items are explicitly out of scope?

**[Variant D]**

Who or what interacts with the system from the outside? What information flows in and out? What hardware or external systems must we connect to?

**[Variant E]**

"Which business processes, functions, and events will be part of the solution? Which ones will remain outside it?", "Who will use or derive benefits from the solution? Who is excluded?", "Which software systems will be part of the solution? What will the interfaces look like?", "Where do each system's responsibilities begin and end?", "How do we fit our solution into the rest of our universe?"

## Minimal Realistic Example

**[Variant A]**

A Context Diagram for a 'Project Control System' showing interactions with Project Manager, Team Member, System Administrator, Finance System, and a Friday 22:00 time trigger.

**[Variant B]**

Central 'Hotel System' box connected via arrows to 'Receptionist' (booking data), 'Guest' (invoice), and 'Accounting System' (account records).

**[Variant C]**

An aircraft baggage system context diagram showing external entities (Air Traffic Control, Baggage Handling System, Refueling), boundary flows ('bags to load', 'fuel level'), and event-handling functions.

**[Variant D]**

Loan Processing System interacts with Applicants (submits application), Credit Bureau (requests report), and Accounts Management System (retrieves history).

**[Variant E]**

An Online Ordering Site is drawn at the center of a Context Diagram. Arrows show 'menu items' flowing from an existing Menu Repository, 'orders' flowing to Restaurant Order Placement, and 'payment info/confirmation' exchanged with an external Online Payment Processing system.

## Quality Criteria & Verification

**[Variant A]**

Accurate system boundary definition; complete representation of all external interfacing actors without internal system detail.

**[Variant B]**

Stakeholder review, boundary confirmation against project scope statement.

**[Variant C]**

Exhaustive coverage of boundary flows; agreement with owners of external systems on interface specifications; event-handling logic verified against condition-action tables.

**[Variant D]**

Stakeholder walkthrough; check if all external entities and high-level interaction flows are captured without detailing internal system logic.

**[Variant E]**

Context Diagram contains exactly one central circle (the system under design); all external interfaces and data flows are labeled; cross-check ecosystem map data flows against system architecture and database interfaces.

## Errors & Anti-Patterns

**[Variant A]**

Adding directional data flow arrows or internal system process detail inside the central system box.

**[Variant B]**

Including internal system functions or internal modules inside the context box.

**[Variant C]**

Drawing internal functional boxes inside the context circle; confusing use case actors with system boundary interfaces; omitting out-of-scope boundaries.

**[Variant D]**

Failing to define a clear boundary, leading to scope creep or forced inclusion of manual/external processes inside system scope.

**[Variant E]**

Drawing internal system components inside a context diagram (violating boundary abstraction); failing to consult owners of connected external systems; creeping scope due to missing interface boundaries.

## When NOT to Use

**[Variant A]**

When detailed internal process workflow or internal algorithmic logic needs to be documented.

**[Variant B]**

When the project scope is entirely isolated and has zero external actors or systems.

**[Variant C]**

When organizational problem boundaries remain ill-defined, highly political, or fluid.

**[Variant D]**

When the system scope and boundaries are already fully known and agreed upon by all stakeholders.

**[Variant E]**

When the project is a standalone application with zero external user classes, zero hardware interfaces, and zero external software integrations.

## Alternatives & Complementary Methods

**[Variant A]**

Use Case Diagrams, Level-0 Data Flow Diagrams, Use Case Modelling.

**[Variant B]**

Use Case Diagrams, High-level Dataflow Diagrams.

**[Variant C]**

Use Case Diagrams, Rich Pictures, Enterprise Architecture Models, Data Flow Diagrams.

**[Variant D]**

Use Case Diagrams, Stakeholder Analysis.

**[Variant E]**

Complementary: Practice #8 Assess Data Concepts, Practice #11 Create Requirements Models (DFD). Alternatives: Architecture block diagrams, Use Case diagrams.

## Supported Decisions

**[Variant A]**

System scope approval, interface architecture definition, project boundary agreement.

**[Variant B]**

Project scope boundaries, external API integration requirements, vendor responsibility boundaries.

**[Variant C]**

System architecture boundaries, project cost/effort estimation, interface contract definitions.

**[Variant D]**

Scope determination, preliminary architecture boundary decisions.

**[Variant E]**

Scope boundaries, release planning/roadmapping, system responsibility allocation, vendor interface constraints.

## AI & Agentic Adaptation

**[Variant A]**

Architecture-parsing AI generates initial Context Diagrams by scanning system integration documentation and user access role matrices.

**[Variant B]**

Extract external actors and data exchanges from project charters using LLMs to automatically generate Mermaid or PlantUML context diagrams.

**[Variant C]**

Agentic parsing of interface documentation, API specs, and domain standards to generate precise Context Diagrams and Event-Handling tables, with automated verification of boundary completeness.

**[Variant D]**

Not specified in source.

**[Variant E]**

AI agents can analyze existing architecture specs or codebases to automatically draft Mermaid/PlantUML context diagrams and ecosystem maps, highlighting missing data flows or unmapped external systems for human verification.
