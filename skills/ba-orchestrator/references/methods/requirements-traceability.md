---
id: requirements-traceability
name: "Requirements Traceability"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.4"
subtask_name: "Traceability and Status"
source_count: 5
---

# Requirements Traceability

`T6 Prioritisation and Requirements Management › 6.4 Traceability and Status`

**Also described as:** Requirements Traceability & Status Management; Requirements Tracing (Traceability Matrix); Requirements traceability matrix; Traceability Management

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Tracks requirements bi-directionally (backwards to business sources/goals, forwards to design, code, and test cases), ensuring all requirements are delivered and no unneeded features are built.

**[Variant B]**

Reduces missing or unnecessary requirements, gold-plating, orphan code, and maintenance headaches by maintaining logical bidirectional links between requirements, designs, code, and tests.

**[Variant C]**

Reduces undocumented change impacts, orphan requirements, unverified design features, and costly maintenance overheads during system evolution.

**[Variant D]**

Reduces inconsistency, untraced impact, and maintenance costs during requirements evolution by documenting and navigating explicit links among requirements, goals, assumptions, and software lifecycle artifacts.

**[Variant E]**

Prevents requirements from being lost, unimplemented, or un-tested, and manages scope changes and implementation progress visuality.

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Requirements Development / Testing

**[Variant B]**

analysis / specification / validation / change management

**[Variant C]**

Change management / evolution

**[Variant D]**

Evolution / change management

**[Variant E]**

Change Management

## Input Artifacts

**[Variant A]**

Requirements Catalogue, Use Cases, System Design docs, Test Scripts.

**[Variant B]**

Business requirements, user requirements, functional requirements, design models, source code modules, test cases.

**[Variant C]**

RD items (goals, requirements, assumptions), downward software lifecycle items (architecture, code, test cases), traceability meta-model.

**[Variant D]**

Requirements Document, traceability meta-model, link types (Dependency, Variant, Revision, Use, Derivation), software artifacts.

**[Variant E]**

Requirements Repository, Test Cases, Implementation Units/Code Modules, Story Map, Kanban Board.

## Output Artifacts

**[Variant A]**

Requirements Traceability Matrix mapping Requirement ID -> Source -> Use Case -> Design Module -> Code Component -> Test Case ID -> Test Result.

**[Variant B]**

Requirements Traceability Matrix (RTM), suspect link reports.

**[Variant C]**

Traceability graph, traceability matrices/lists, impact analysis reports, coverage matrices.

**[Variant D]**

Traceability matrix/graph, traceability database, coverage reports, change impact logs.

**[Variant E]**

Traceability Matrix, Kanban Status Board, Requirements Status Reports, Change Impact Logs.

## Participants & Roles

**[Variant A]**

BA, Project Manager, System Architect, Developers, Testers.

**[Variant B]**

Business Analyst (coordinator/owner), System Engineer, Developer, Tester, QA Engineer.

**[Variant C]**

BA, Traceability Manager, Change Review Board, System Architect, Test Lead.

**[Variant D]**

Requirements Engineer, Change Control Board, Software Architect, Test Manager.

**[Variant E]**

Business Analyst, Project Manager / Product Owner, QA Lead, Developers.

## Prerequisites

**[Variant A]**

Uniquely identified requirements in a requirements catalogue.

**[Variant B]**

Uniquely and persistently labeled, fine-grained individual requirements.

**[Variant C]**

Traceable items have unique identifiers; project traceability policy is established.

**[Variant D]**

Defined project traceability policy (determining link granularity and scope); uniquely identified artifacts.

**[Variant E]**

Uniquely identified atomic requirements or stories, established test cases, and code modules.

## Step-by-Step Procedure

**[Variant A]**

Create standard matrix template.
2. Populate row IDs from Requirements Catalogue.
3. Map backward links to original business sources/goals.
4. Map forward links to Use Cases and Design modules as created.
5. Map forward links to Test Case IDs and code modules.
6. Update test result status.
7. Use matrix for impact analysis when changes occur.

**[Variant B]**

Establish a traceability matrix format (single matrix style or pair-wise matrices).
2. Assign unique identifiers to all requirements, design components, code modules, and test cases.
3. Link customer needs forward to functional requirements, and functional requirements forward to design elements, code modules, and test cases.
4. Maintain reverse trace links from code/tests back to functional and business requirements.
5. Update trace data continuously as work is completed (not merely planned).
6. Flag trace links as 'suspect' whenever an endpoint object is modified.
7. Review suspect links following changes to evaluate ripple effects and update connected artifacts.

**[Variant C]**

Establish project traceability policy (scope, granularity, link types).
2. Assign unique identifiers to all traceable items.
3. Establish bi-directional links between source and target items (Dependency, Variant, Revision, Use, Derivation) manually, via model database, or using automated link generators.
4. Record links in a traceability database or matrix.
5. Exploit links for impact analysis, rationale analysis, coverage analysis, and defect tracking.
6. Maintain and update links when items are created, modified, or deleted.

**[Variant D]**

Define a project traceability policy establishing scope, link types, and granularity based on project risk.
2. Assign unique identifiers (RefName) to all traceable items.
3. Establish horizontal links (Use) and vertical links (Derivation) between goals, requirements, assumptions, architecture, code, and test cases.
4. Record links in a traceability matrix, database, or model repository.
5. (Exploitation) Perform forward/backward impact analysis, coverage analysis, and rationale tracking when changes are requested.
6. Maintain and update links whenever items are created, modified, or deleted.

**[Variant E]**

Assign a unique ID to every requirement or story.
2. Map links forward from Business Events -> BUCs/Stories -> Atomic Requirements -> Implementation Units -> Test Cases.
3. Maintain a Traceability Matrix or tool-based link repository.
4. Set up a visual Kanban board with workflow columns (Proposed, Analyzing, Design, Backlog, Implementing, Validating, Deployed).
5. Establish pull limits for each column.
6. Track requirements movement and update statuses continuously.
7. Evaluate all requested changes via a formal change supremo triage process.

## Analyst Questions & Prompts

**[Variant A]**

Which business goal spawned this requirement? Which use case implements this requirement? Which test case verifies this requirement? What code/design components are impacted if this requirement changes?

**[Variant B]**

Why was this code written (what requirement does it trace to)? Which functional requirements satisfy this user requirement? Which test cases verify requirement FR-10? Is this requirement traced to design and code?

**[Variant C]**

Why does this requirement exist (backward traceability)? What design components and test cases are impacted if I change this requirement (forward traceability)? Is this requirement covered by test cases?

**[Variant D]**

What upward goals explain why this software module exists? What downward test cases must be re-run if requirement R1 changes? What requirements are impacted if assumption A1 is invalidated?

**[Variant E]**

"Which implementation unit satisfies requirement #75?", "Which test cases prove that this requirement is met?", "What is the current status of the requirements for Business Event #3?", "If we change this requirement, which other requirements, designs, and tests are impacted?"

## Minimal Realistic Example

**[Variant A]**

Mapping Requirement F-073 ('Book flight'): Source (Focus Group) -> Use Case (UC-04) -> Design Module (Mod-9) -> Test Case (TC-102) -> Result (Pass).

**[Variant B]**

Setting up a matrix linking Use Case UC-28 to functional requirement catalog.query.sort, class CatalogSort(), and test cases search.7 and search.8, ensuring no development gaps exist.

**[Variant C]**

Tracing goal 'Anywhere/anytime notification' to requirement 'SMS notification', then to architecture module 'SMSNotifier', and finally to test case 'TC-SMS-01'.

**[Variant D]**

Tracing goal 'G1: Safe Transportation' -> derived requirement 'R1: Doors closed when moving' -> derived architecture module 'DoorController' -> derived test case 'TC_Door_01'.

**[Variant E]**

Tracing Requirement #75 ("Record treated roads") to BUC #9, to code module 'TrkLog.cs', and to Test Case TC01, verifying its status as 'Validating' on the project Kanban board.

## Quality Criteria & Verification

**[Variant A]**

100% bi-directional traceability for every requirement; zero 'orphan' requirements without test cases or sources.

**[Variant B]**

Zero orphan requirements (requirements without tests/code); zero orphan code (code without parent requirements); periodic audits verifying trace data accuracy.

**[Variant C]**

100% coverage of critical requirements by test cases; accuracy of dependency links; bi-directional traversability.

**[Variant D]**

100% downward coverage of high-priority requirements by test cases and architecture modules; absence of orphan requirements.

**[Variant E]**

100% forward and backward traceability for all baseline requirements; zero orphan code modules or untested requirements; clear visual status visibility.

## Errors & Anti-Patterns

**[Variant A]**

Creating the matrix at the end of the project as a fake compliance exercise; maintaining complex matrices manually in flat spreadsheets without repository support.

**[Variant B]**

Attempting to trace everything at once without a cost-benefit focus; populating trace data at planning time rather than completion time; neglecting to maintain trace data until it becomes obsolete.

**[Variant C]**

Traceability overload (tracing everything at too fine a grain without policy); untracked manual link updates; vague link semantics.

**[Variant D]**

Traceability decay (failing to update links when requirements evolve); over-tracing trivial items causing unmanageable overhead ('traceability paralysis'); single-direction tracing.

**[Variant E]**

Allowing requirements to be changed directly by developers without change supremo approval; failing to update the matrix when code or tests change; excessive manual overhead in tracking without appropriate tool support.

## When NOT to Use

**[Variant A]**

In tiny, 1-week single-developer scripts where formal matrix tracking creates excessive overhead.

**[Variant B]**

Very small throwaway prototypes or short-lived un-maintained applications where lifecycle tracing costs exceed maintenance risk.

**[Variant C]**

Never skipped entirely, but restricted to coarse-grained items in low-risk, small-scale agile projects.

**[Variant D]**

Unselective fine-grained tracing on ultra-short, throwaway micro-projects where maintenance cost outweighs value.

**[Variant E]**

Disposable prototypes or ultra-short exploratory spikes.

## Alternatives & Complementary Methods

**[Variant A]**

Requirements Catalogue, CRUD Matrix, Use Case Diagrams.

**[Variant B]**

Requirements Mapping Matrix, Commercial RM Tool Automated Traceability, Pairwise Link Matrices.

**[Variant C]**

Traceability matrices, Feature diagrams, Traceability model databases, Information retrieval link generators.

**[Variant D]**

Complementary: Goal Modeling (Satisfaction Arguments), Configuration Management, Information Retrieval Link Mining.

**[Variant E]**

Impact Analysis, Automated Traceability in ALM Tools (e.g., Jira, Azure DevOps), Value Stream Mapping.

## Supported Decisions

**[Variant A]**

Scope verification sign-off, change impact assessment, test coverage validation.

**[Variant B]**

Change impact decisions, release verification/completeness decisions, compliance and regulatory certification acceptance.

**[Variant C]**

Change request approval, impact assessment, release coverage verification, compliance audit.

**[Variant D]**

Change impact assessment, release regression planning, compliance/certification auditing.

**[Variant E]**

Release readiness, scope change approval/rejection, defect root-cause analysis, project progress reporting.

## AI & Agentic Adaptation

**[Variant A]**

ALM AI systems parse requirements, architecture models, and automated test suites to maintain dynamic, bi-directional traceability matrices automatically.

**[Variant B]**

Not in source

**[Variant C]**

Information retrieval AI agents can analyze semantic similarity between requirement text and source code to auto-generate candidate traceability links with precision/recall scoring.

**[Variant D]**

AI agents using NLP/semantic similarity can automatically generate candidate traceability links across text specs, code, and tests, maintaining graph integrity continuously.

**[Variant E]**

Agentic ALM integrations automatically link code commits and automated test results to requirement IDs, dynamically updating traceability matrices and moving Kanban cards through pipeline stages.
