---
id: use-cases
name: "Use Cases"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 7
---

# Use Cases

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Scenarios & Use Cases; Use Case Writing (Goal-Oriented Method); Use Cases (UML & Essential); Use Cases and Scenarios; Use case diagrams and use case descriptions

This card merges 7 descriptions of the method, labelled Variant A–G in every field.

## Problem Solved

**[Variant A]**

Models IT system functional scope via Use Case Diagrams and details actor-system interactions via structured Use Case Descriptions, providing clear developer and user specifications.

**[Variant B]**

Specifies product-centric functional interactions and system boundary behaviors for software developers.

**[Variant C]**

Reduces requirements ambiguity by describing narrative step-by-step interactions between primary actors and a solution to achieve a specific goal.

**[Variant D]**

Reduces ambiguity regarding operational requirements, usability failures, unhandled exceptions, and misalignment between developers and end users.

**[Variant E]**

Resolves ambiguity in complex, multi-step interactions, permissions, recoveries, branching workflows, and exception paths across multiple systems.

**[Variant F]**

Reduces functional ambiguity, goal misalignment, unhandled exception/failure modes, scope creep, and communication barriers between technical teams, business stakeholders, and users.

**[Variant G]**

Imprecise description of the functional requirements for the system

## Uncertainty Reduced

**[Variant G]**

Not understanding the interaction between the user and the system

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Requirements Modelling / Specification

**[Variant B]**

analysis

**[Variant C]**

analysis / specification / Solution Evaluation

**[Variant D]**

Analysis / Specification / Validation

**[Variant E]**

Analysis / Specification

**[Variant F]**

elicitation / analysis / specification / prioritisation / validation

**[Variant G]**

Specification, requirements analysis

## Input Artifacts

**[Variant A]**

Context Diagram, Business Use Cases, Scenarios, User Analysis.

**[Variant B]**

Context diagrams, task descriptions, domain event lists.

**[Variant C]**

Elicitation results, actor profiles, scope models, process models.

**[Variant D]**

Goal models, event lists, user roles, domain definitions, business rules

**[Variant E]**

User story map, stakeholder requests, process maps.

**[Variant F]**

Vision Statement, In/Out List, Actor Profile Table, System Architecture/Scope Drawings, Usage Narratives, Stakeholder Request/Interviews

**[Variant G]**

Stakeholder requirements, business processes

## Output Artifacts

**[Variant A]**

Use Case Diagram (System Boundary, Actors, Use Cases, Associations, <>, <>) and Use Case Descriptions (Preconditions, Trigger, Guarantees, Main Success Scenario, Extensions).

**[Variant B]**

Use case diagrams, textual use case specifications (Actor/System interaction steps).

**[Variant C]**

Use Case Diagrams, Use Case Specifications (Name, Goal, Actors, Preconditions, Triggers, Basic Flow, Alternate Flows, Exception Flows, Post-conditions).

**[Variant D]**

User stories, storyboards, operational scenario step-lists, fully dressed use cases (including main/alternate/exception paths, preconditions, guarantees)

**[Variant E]**

Fully dressed use case specification (actors, triggers, preconditions, main success scenario, extensions/alternatives, postconditions).

**[Variant F]**

Actor-Goal List, Fully Dressed Use Case Specification, Casual Use Case, Use Case Briefs, Test Scenario Outlines, Requirements Matrix (Hub-and-Spoke)

**[Variant G]**

Result: use case diagram and detailed specifications (Use Case Descriptions). Artifacts: Use Case Diagram, Use Case Specification

## Participants & Roles

**[Variant A]**

BA, Business Users, System Architect, Developers, Testers.

**[Variant B]**

BA, system architect, developer, tester.

**[Variant C]**

BA, Primary/Secondary Actors, Developer, Tester, SME.

**[Variant D]**

BA, SME, End User, Developer, Tester, UI/UX Designer

**[Variant E]**

Business Analyst, Primary Actor (End User/SME), Architect, Developer, Tester.

**[Variant F]**

Primary Actor, Supporting/Secondary Actors, Offstage Stakeholders, Business Analyst / Use Case Author, Subject Matter Expert (SME), Developer / Architect, Tester / QA, Sponsor / Executive

**[Variant G]**

BA, Developer, Tester, End User

## Prerequisites

**[Variant A]**

Defined IT system boundary and user roles.

**[Variant B]**

Clear definition of system boundaries and actors.

**[Variant C]**

Identified system boundary, primary actors, and actor goals.

**[Variant D]**

Defined user roles and system boundary events.

**[Variant E]**

Identified primary actors and clear system boundary/scope.

**[Variant F]**

Defined System Scope (System Under Discussion), identified Primary Actors, identified Offstage Stakeholders and their key Interests, and agreed-upon writing standards/level of formality.

## Step-by-Step Procedure

**[Variant A]**

Draw System Boundary box and System Name.
2. Position Actors outside boundary (User roles, Other systems, Time).
3. Draw Use Case ovals inside boundary.
4. Draw un-arrowed Association lines.
5. Add <> (mandatory common sub-use cases) and <> (optional sub-use cases) links.
6. Write detailed Use Case Descriptions (Scope, Actors, Preconditions, Trigger, Guarantees, Main Success Scenario, Extensions).

**[Variant B]**

Identify actors and system boundaries.
2. Define use case bubbles representing product-provided functional units.
3. Specify interaction steps (User Action / System Response).
4. Detail preconditions, postconditions, and alternative execution branches.
5. (Optional) Define include and extend relationships between use cases.

**[Variant C]**

Identify actors and their specific goals interacting with the solution.
2. Create Use Case Diagram showing actors, use cases, <>, and <> relationships.
3. For each use case, write brief goal description, primary actor, preconditions, and triggers.
4. Document Basic/Primary Success Flow as chronological numbered steps.
5. Document Alternate Flows (optional success paths) and Exception Flows (failure paths).
6. Specify Post-conditions (minimal and success guarantees) and validate with stakeholders.

**[Variant D]**

Identify functional goals and primary roles (actors).
2. Draft the main success ('happy day') scenario as a numbered step-by-step sequence.
3. Brainstorm variation paths and exceptions for each step.
4. Write exception-handling scenarios (recovering or safe failure).
5. Define preconditions and success/minimal guarantees (postconditions).
6. Conduct walkthroughs, simulations, or prototypes to validate scenario flows.

**[Variant E]**

Identify actors and their goal levels.
2. Define triggers and preconditions.
3. Write the main success scenario step-by-step.
4. Identify and write alternative flows and failure/exception recoveries.
5. Define postconditions.

**[Variant F]**

Establish system boundaries using an In/Out List and Design Scope diagram.
2. Brainstorm and list all primary actors over the life of the system.
3. Brainstorm and exhaustively list user goals for each primary actor (Actor-Goal List).
4. Capture outermost summary-level use cases to set operational context.
5. Select a user-goal level use case to expand.
6. Identify stakeholders, interests, preconditions, and guarantees (minimal and success).
7. Write the Main Success Scenario (MSS) in 3 to 9 simple, action-oriented steps.
8. Brainstorm and exhaustively list failure and alternate extension conditions.
9. Write extension-handling steps detailing system recovery, fallback, or goal failure.
10. Extract complex subgoals into sub-use cases or merge trivial steps as needed.

**[Variant G]**

1. Identify the actors.
2. Define the actors' goals (Use Cases).
3. Describe the main flow of events.
4. Describe the alternative and exception flows.

## Analyst Questions & Prompts

**[Variant A]**

What does the user want the IT system to do? What is the main 'happy day' sequence between actor and system? What exceptions or alternative flows occur?

**[Variant B]**

What input does the user send to the system? What specific validation and response does the product execute?

**[Variant C]**

"What is the primary actor's goal?", "What step-by-step path achieves this goal?", "What exception occurs if input X is invalid?"

**[Variant D]**

What is the first step? What does the operator do next? How does the system respond? What could go wrong at this step? What must be true before/after this scenario runs?

**[Variant E]**

What triggers this interaction? What can go wrong at this step? How does the actor recover from failure? What must be true before and after?

**[Variant F]**

"Can the primary actor go away happy after having done this?" (Coffee break test) "Does your job performance depend on how many of these you do today?" "Why is the actor doing this?" (To raise goal level) "How is this goal accomplished?" (To lower goal level) "What would make this stakeholder unhappy at the end of a successful run?" (To find success guarantees) "What does the system detect when something goes wrong?" "What is the human backup to system failure?"

**[Variant G]**

'What task does the actor accomplish?', 'What happens if the system is unavailable?'

## Minimal Realistic Example

**[Variant A]**

Diagram for 'Project Control System' showing Project Manager actor linked to Use Cases 'Create project', 'Amend project' (including 'Identify project'), and optional extension 'Print assignment', supported by detailed tennis-match narrative descriptions.

**[Variant B]**

Use Case: Check in booked guest. User: Enters booking number. System: Displays guest details. User: Pushes checkin. System: Allocates room, displays room number.

**[Variant C]**

Use Case 'Withdraw Cash': Actor = Cardholder. Basic Flow: Insert Card -> Enter PIN -> Select Amount -> Dispense Cash. Exception 3a: Invalid PIN -> Eject Card -> End.

**[Variant D]**

Use Case 'Tune Radio' in a telematics system: Actor selects channel -> System tunes to frequency -> Audio plays. Exception: Signal lost -> System displays 'No Signal' and mutes audio output.

**[Variant E]**

Goal: Triage a submitted case. Trigger: Submission enters Ready for triage. Main flow: System extracts evidence and presents recommendation. Alternatives: Missing evidence, extraction failure.

**[Variant F]**

Use Case: Buy Stocks over the Web Primary Actor: Purchaser Scope: Personal Advisors / Finance package (PAF) Level: User Goal Precondition: User has PAF open. MSS:
1. Purchaser selects to buy stocks over the web.
2. PAF gets name of web site to use from user.
3. PAF opens web connection to site.
4. Purchaser buys stock from web site.
5. PAF intercepts response and updates portfolio.
6. PAF shows new portfolio standing. Extensions: 3a. Web failure during setup: System reports failure, backs up to step 2.

**[Variant G]**

Use Case 'Pay for an order by bank card'

## Quality Criteria & Verification

**[Variant A]**

Clear system boundary; user-perspective interaction narrative; complete exception coverage in extension section; unambiguous <> (mandatory) and <> (optional) usage.

**[Variant B]**

Developer code review, automated system test scripting.

**[Variant C]**

Written from actor's point of view; covers basic, alternate, and exception flows; post-conditions hold true; easily testable by QA.

**[Variant D]**

Scenario walkthroughs, user animation/simulation, 100% trace coverage of functional goals and acceptance test cases.

**[Variant E]**

Covers all exception paths; clear goal level; observable interactions between actor and system.

**[Variant F]**

Pass/Fail checklist against template fields: Active-verb goal title, black-box view of SuD, 3 to 9 MSS steps, clear actor intent without UI/GUI mechanics ('Who has the ball?'), complete coverage of detectable extension conditions, validation by stakeholder walkthrough and test-case derivation.

**[Variant G]**

Review with developers and testers (coverage of all scenario branches)

## Errors & Anti-Patterns

**[Variant A]**

Over-using <> and <> to turn diagrams into complex functional decomposition flowcharts; writing internal technical coding steps inside use case descriptions.

**[Variant B]**

Creating hundreds of trivial, tiny use cases (e.g., 'Enter name'); specifying premature UI dialog details in domain use cases.

**[Variant C]**

Embedding UI design details or business rules directly inside use case steps instead of referencing separate rule tables; creating overly complex nested flows.

**[Variant D]**

Writing use cases inside-out (making tiny UI button clicks separate use cases); omitting exception paths; overloading use cases with non-functional clutter.

**[Variant E]**

Writing internal design decisions instead of observable behavior; omitting failure branches; over-complicating simple CRUD interactions.

**[Variant F]**

Including UI mechanics (clicks, screen layouts) instead of user intent ('Too much UI'); missing system actions or missing primary actor actions; writing underwater/indigo subfunctions as standalone specs ('Fleas on fleas'); writing 'checks whether' instead of 'validates'; assuming unverified preconditions; missing failure recovery logic.

**[Variant G]**

Too much user-interface detail in the business logic

## When NOT to Use

**[Variant A]**

For purely non-functional infrastructure performance specifications or static database schema design.

**[Variant B]**

COTS acquisition projects where internal system interaction sequences are already built.

**[Variant C]**

When lightweight user stories are preferred in short-iteration agile teams without formal documentation requirements.

**[Variant D]**

When specifying pure algorithmic batch computations without user/system interaction.

**[Variant E]**

Simple, single-step operations or purely data-transformation logic without complex interaction.

**[Variant F]**

Small/zero-risk feature tweaks, purely algorithmic/mathematical processing (e.g., matrix calculations, compiler passes, batch data transformation without interactive logic), or when stakeholder communication is real-time/colocated with no requirement for durable specifications (e.g., raw XP user stories on index cards).

**[Variant G]**

Projects without software logic, purely organisational changes

## Alternatives & Complementary Methods

**[Variant A]**

Activity Diagrams, User Stories, Business Process Modelling, Task Analysis.

**[Variant B]**

Task Descriptions, Tasks & Support, Activity Diagrams.

**[Variant C]**

Alternatives/Complements include User Stories, Process Modelling, Sequence Diagrams, Prototyping, and Activity Diagrams.

**[Variant D]**

Flowcharts, Activity Diagrams, User Stories, State Machine Diagrams, Sequence Diagrams.

**[Variant E]**

User Story Mapping (for high-level view), Atomic Textual Requirements, State Models.

**[Variant F]**

Complementary Prior: Vision Statement, Usage Narratives, In/Out List, Domain Data Model. Complementary Subsequent: UI Design / Wireframes, Test Case Design, CRC Cards / Responsibility-Driven Design. Alternatives: User Stories (XP), Feature Lists, State Transition Diagrams, Activity Diagrams / BPMN.

**[Variant G]**

User Stories, functional decomposition

## Supported Decisions

**[Variant A]**

IT system scope approval, software architecture design, test case generation, user training documentation.

**[Variant B]**

Software object architecture, system test case design.

**[Variant C]**

Functional scope definition, test case design, user acceptance criteria verification.

**[Variant D]**

Software functional design, release planning, user acceptance test creation, user manual authoring.

**[Variant E]**

Scope, functional design, test scenarios.

**[Variant F]**

Scope inclusion/exclusion, release staging/prioritization, architecture/subsystem allocation, acceptance testing criteria, project effort estimation.

**[Variant G]**

Scope, architecture, acceptance

## AI & Agentic Adaptation

**[Variant A]**

Requirement AI tools generate complete Use Case Diagrams and structured Descriptions directly from input scenario transcripts.

**[Variant B]**

Convert user stories or task descriptions into formal UML use case specifications using AI agents.

**[Variant C]**

LLMs can convert narrative use case flows automatically into automated test scripts (Cucumber/Gherkin) or sequence diagrams.

**[Variant D]**

Agentic scenario expansion: AI agents generate exhaustive edge-case scenarios and exception flows from happy-day user stories, converting them into automated acceptance test scripts (BDD/Gherkin). Human review ensures domain relevance.

**[Variant E]**

Define human-in-the-loop review flows as explicit alternative branches when AI confidence falls below a configured threshold.

**[Variant F]**

Roles: Agentic AI as Primary Actor (autonomous caller) or Supporting Actor (external intelligence/llm service). Inputs: Structured JSON payloads or semantic prompts replacing free-form textual inputs. Guardrails: Deterministic verification steps (validation gates) explicitly added to handle LLM non-determinism or timeout/hallucination failures in extension steps. Human-in-the-loop: Escalation extension conditions where AI confidence drops below a threshold, routing execution to a human operator. Audit Trail: System logs must capture agent decisions, prompt context, and token outputs for compliance and rollback.

**[Variant G]**

Automatic generation of test cases from Use Case descriptions
