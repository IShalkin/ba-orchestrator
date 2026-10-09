---
id: data-flow-diagrams
name: "Data Flow Diagrams"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 5
---

# Data Flow Diagrams

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Data Flow Diagram (DFD); Dataflow Diagrams (DFD); Dataflow Diagrams (DFD) and SADT; SADT Diagrams & Dataflow Diagrams (DFD)

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Reduces ambiguity regarding operational data transformations, inputs/outputs, and data dependencies between processes.

**[Variant B]**

Reduces functional and data boundary ambiguity by visually portraying how data is transformed by processes, stored, and exchanged with external entities.

**[Variant C]**

Models processes, data stores, and data flows to specify exact data transformations and information movements across domain or product boundaries.

**[Variant D]**

Reduces operational opacity by mapping information transformations, processing operations, data repositories, and functional data dependencies.

**[Variant E]**

Reduces functional decomposition ambiguity by illustrating how data moves through a system, gets transformed by processes, and flows between internal data stores and external entities.

## BA Lifecycle Phase

**[Variant A]**

Specification / analysis

**[Variant B]**

analysis / specification / Discovery

**[Variant C]**

analysis

**[Variant D]**

Specification / functional modeling

**[Variant E]**

analysis

## Input Artifacts

**[Variant A]**

System activities, data flows, repositories, external components.

**[Variant B]**

Elicitation results, existing process documentation, system interfaces, Data Dictionary.

**[Variant C]**

Context diagram, event lists, data expressions, existing process docs.

**[Variant D]**

Elicited business processes, task descriptions, input/output data sets.

**[Variant E]**

Context diagram, process specs, customer interviews, input/output data flows

## Output Artifacts

**[Variant A]**

SADT Actigrams/Datagrams, Dataflow Diagrams (DFDs), process decomposition hierarchies.

**[Variant B]**

Context Diagram (Level 0), Level 1+ Data Flow Diagrams (Gane-Sarson or Yourdon notation).

**[Variant C]**

Dataflow diagrams (Bubbles, Data Stores, Data Flows, External Entities) and Data Expressions.

**[Variant D]**

SADT Actigrams/Datagrams, Dataflow Diagrams (DFDs), process specs.

**[Variant E]**

Context Diagram (Level -1/0 abstraction), Level 0 DFD, Child DFDs (Level 1, Level 2)

## Participants & Roles

**[Variant A]**

BA, Systems Engineer, Developer.

**[Variant B]**

BA, Systems Analyst, Developer, SME, Operational Support.

**[Variant C]**

BA, system architect, developer.

**[Variant D]**

Business Analyst, Business Process SME, Software Architect.

**[Variant E]**

BA, SME/Product Champions, System Architect, Developers

## Prerequisites

**[Variant A]**

System operations and data stores are identified.

**[Variant B]**

Understanding of system boundaries, inputs, outputs, and external actors.

**[Variant C]**

Defined context boundary and system interfaces.

**[Variant D]**

Identified system operations and data stores.

**[Variant E]**

Identification of external entities, major system boundary, and primary inputs and outputs.

## Step-by-Step Procedure

**[Variant A]**

For SADT: (a) Construct Actigrams showing activities with Input (West), Output (East), Control (North), and Mechanism (South) arrows; (b) Construct dual Datagrams; (c) Perform hierarchical decomposition.
2. For DFD: (a) Identify process bubbles, data stores (double bars), external entities (boxes), and dataflows (arrows); (b) Refine complex bubbles into lower-level DFDs.
3. Verify interface consistency across refinement levels.

**[Variant B]**

Identify externals (entities/sources/sinks) outside the system.
2. Create a Context Diagram (Level 0) depicting the system as a single process with external data flows.
3. Decompose into Level 1 diagram showing major processes, data stores, and data flows.
4. Further decompose complex processes into Level 2+ diagrams as needed.
5. Ensure all data flows connect to/from a process and are labelled with nouns.
6. Verify diagram consistency against data dictionaries and process models.

**[Variant C]**

Identify external entities and top-level process bubbles.
2. Draw data flow arrows carrying named data structures between processes, stores, and entities.
3. Specify incoming and outgoing data flows using data expressions.
4. Decompose complex bubbles into second-level dataflow diagrams.
5. (For product level) Split domain bubbles into separate user and computer bubbles.

**[Variant D]**

Identify main system operations (data transformation processes/bubbles).
2. Identify external origin/destination components (boxes) and data repositories (double bars).
3. Connect operations via directed arrows representing input/output data flows.
4. (SADT) Specify Actigrams (inputs, outputs, controls, mechanisms) and dual Datagrams.
5. Hierarchically refine complex operations into child DFD diagrams.
6. Annotate leaf processes with concise operational specifications.

**[Variant E]**

Draw the Context Diagram representing the entire system as a single process bubble connected to external terminators.
2. Decompose the single context bubble into a Level 0 DFD with 3 to 10 major process bubbles, data stores, and data flows.
3. Assign verb-object names to processes and unique hierarchical numbers (e.g., 1.0, 2.0).
4. Balance data flows between child diagrams and parent bubbles.
5. Continue progressive decomposition until primitive processes can be described succinctly in text, pseudocode, or activity diagrams.

## Analyst Questions & Prompts

**[Variant A]**

What data is required as input to produce this output? What activity controls this data store? Are all inputs in the parent process accounted for in the child DFD?

**[Variant B]**

"Where does input data X originate?", "What transformation process modifies data X into output Y?", "Where is data stored for future use?"

**[Variant C]**

What data enters this process? Where is this data stored? What transformed data leaves this function?

**[Variant D]**

What data is required to perform this operation? Where does this dataflow originate? What store holds this information?

**[Variant E]**

What information do you need to perform this step? What information does this step produce that we should store? Where does this data come from and where does it go?

## Minimal Realistic Example

**[Variant A]**

A DFD showing 'AskConstraints' receiving 'meetingRequest' from 'Initiator' and storing 'copyOfConstraintsRequest' into a 'meetingConstraints' repository.

**[Variant B]**

A Level 1 DFD shows 'Customer' sending 'Order Data' to process '1.0 Validate Order', which checks 'Customer DB' data store and outputs 'Valid Order' to '2.0 Process Payment'.

**[Variant C]**

Bubble 'FindFreeRoom' receives 'period+room type' from user, queries 'Rooms' data store, and outputs 'free rooms' list to user.

**[Variant D]**

Drawing a DFD bubble 'Schedule Meeting' receiving 'meetingRequest' from Initiator and 'individualConstraints' from 'Participant' store, outputting 'meetingNotification' to Participant.

**[Variant E]**

Process 1.0 'Place a chemical request' receives 'request for chemical' from external entity 'Requester', reads 'chemical catalog' from store 'Vendor Catalog', and writes to 'Chemical Request' store.

## Quality Criteria & Verification

**[Variant A]**

Conservation of dataflow across hierarchical decomposition levels; absence of black holes (processes with inputs but no outputs) or miracles (outputs without inputs).

**[Variant B]**

Diagrams follow strict notation rules (no flow directly between two stores or two externals); inputs and outputs balance across levels.

**[Variant C]**

Data balance checks between hierarchy levels, CRUD check against data stores.

**[Variant D]**

Parent-child dataflow balance checks (input/output consistency across hierarchy levels); verifying that all data stores connect to processes; database query checks.

**[Variant E]**

Ensure diagram balancing across levels; verify process bubbles have both inputs and outputs; ensure processes connect to processes via data stores (no direct store-to-store or entity-to-store flows); review with customer representatives.

## Errors & Anti-Patterns

**[Variant A]**

Including control flow/sequencing logic in DFDs; interface mismatch between parent and child bubbles; unlabelled dataflows.

**[Variant B]**

Including sequence/timing logic in DFDs (confusing DFD with flowchart); over-complicating diagrams with too many levels.

**[Variant C]**

Over-specifying strict process execution sequences inside DFDs (DFDs show data flow, not control flow).

**[Variant D]**

Infinite sinks/sources (data disappearing or created out of nowhere); control-flow branching confused with dataflow; overly complex non-decomposed diagrams.

**[Variant E]**

Showing sequence or control logic on a DFD; creating 'black holes' (inputs only) or 'miracles' (outputs only); cluttering a single diagram with more than 8-10 processes.

## When NOT to Use

**[Variant A]**

When object-oriented encapsulated designs are strictly enforced and functional decomposition is forbidden, or for purely event-driven reactive state machines.

**[Variant B]**

When the sequence of activities or timing/workflow control is the primary focus of analysis (use Process Modelling instead).

**[Variant C]**

Describing event-driven user interface screens with complex, non-sequential user interactions.

**[Variant D]**

When specifying object-oriented design encapsulation or strict reactive event timing where state machines are required.

**[Variant E]**

When modeling real-time control timing, state-dependent control logic, or user interface menu navigation.

## Alternatives & Complementary Methods

**[Variant A]**

UML Use Cases, Goal-derived Operation Models, Activity diagrams.

**[Variant B]**

Alternatives/Complements include Process Modelling, Use Cases, Interface Analysis, and Sequence Diagrams.

**[Variant C]**

Activity Diagrams, Task Descriptions, Use Cases.

**[Variant D]**

Complementary: ER Diagrams, State Machine Diagrams. Alternative: UML Use Case Diagrams, Activity Diagrams.

**[Variant E]**

Swimlane Diagram, Activity Diagram, Use Case Specification, ERD.

## Supported Decisions

**[Variant A]**

Functional decomposition, interface design, data dependency mapping.

**[Variant B]**

System boundary definition, data architecture design, scope allocation.

**[Variant C]**

System architecture, system data interface definitions, workflow engine configuration.

**[Variant D]**

Functional decomposition, data transformation interface design.

**[Variant E]**

Scope, architecture.

## AI & Agentic Adaptation

**[Variant A]**

Static analysis tools can automatically check DFD hierarchical levelling consistency and detect orphaned data stores or unlinked processes in a model database.

**[Variant B]**

AI agents can parse process specifications or user stories to construct draft DFDs, verifying data conservation (balancing inputs and outputs) automatically.

**[Variant C]**

Convert process descriptions into structured DFD dataflow connections and syntax trees using LLMs.

**[Variant D]**

Agents can analyze process specifications to construct functional DFD models and run automated balance checks across hierarchical levels.

**[Variant E]**

Not in source
