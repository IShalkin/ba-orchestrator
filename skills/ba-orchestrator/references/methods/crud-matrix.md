---
id: crud-matrix
name: "CRUD Matrix"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 5
---

# CRUD Matrix

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** CRUD Analysis (Create, Read, Update, Delete Check); CRUD Matrix Check; CRUD Matrix Mapping (Basic & Expanded / UCOM); CRUD matrix

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Cross-references system use cases against data entities/classes to map Create, Read, Update, and Delete operations, ensuring data-process model completeness and consistency.

**[Variant B]**

Uncovers missing user tasks, missing system functions, or unmaintained database entities by systematically cross-checking data lifecycle operations.

**[Variant C]**

Reduces gaps between functional flows and data entities; prevents orphan objects or unassigned object responsibilities.

**[Variant D]**

Identifies missing business events, missing requirements, and orphan data entities across the system.

**[Variant E]**

Detects missing requirements, orphaned data entities, or incomplete process logic by checking Create, Read, Update, and Delete coverage across system functions.

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Requirements Modelling / Validation

**[Variant B]**

analysis

**[Variant C]**

Analysis

**[Variant D]**

Validation

**[Variant E]**

analysis

## Input Artifacts

**[Variant A]**

Use Case Diagrams, Class Models / Entity Relationship Models.

**[Variant B]**

Data model (entities), task descriptions / event list.

**[Variant C]**

Use Cases, Analysis Object Model.

**[Variant D]**

Business Data Model / Class Diagram, Business Event List, Work Context Diagram.

**[Variant E]**

ERD data entities, DFD processes, use cases, event lists

## Output Artifacts

**[Variant A]**

CRUD Matrix (Classes/Entities on vertical axis, Use Cases on horizontal axis, populated with C, R, U, D letters).

**[Variant B]**

CRUD Matrix (Tasks/Events vs. Database Entities) with identified lifecycle gaps.

**[Variant C]**

Basic CRUD Matrix, Use Case Object Model (UCOM) Matrix.

**[Variant D]**

CRUD Matrix (Table linking Data Classes/Entities with Business Events), Updated Event List, Updated Context Diagram.

**[Variant E]**

CRUD Matrix (rows = use cases/events, columns = data entities, cells = C, R, U, D actions)

## Participants & Roles

**[Variant A]**

BA, System Architect, Developers, Testers.

**[Variant B]**

BA, developer, tester.

**[Variant C]**

BA/System Analyst, Architect.

**[Variant D]**

Business Analyst, Data Architect, SME, System Analyst.

**[Variant E]**

BA, System Architect, Developers, Testers

## Prerequisites

**[Variant A]**

Draft Use Case Model and draft Data Model.

**[Variant B]**

Draft data model and draft task descriptions/event list.

**[Variant C]**

List of use cases and draft list of domain objects available.

**[Variant D]**

Draft Business Data Model (or entity list) and Business Event List.

**[Variant E]**

Identified list of key system data entities and identified set of use cases or system events.

## Step-by-Step Procedure

**[Variant A]**

List Classes/Entities down vertical matrix rows.
2. List Use Cases across horizontal matrix columns.
3. For each intersection, indicate whether the use case Creates (C), Reads (R), Updates (U), or Deletes (D) instances of the class.
4. Check rows: ensure every class has at least one C and D.
5. Check columns: ensure every use case accesses data.

**[Variant B]**

List database entities along columns.
2. List user tasks or system functions along rows.
3. Populate cells with C (Create), R (Read), U (Update), D (Delete), or O (Overview).
4. Analyze bottom summary row for each entity.
5. Flag entities missing Create, Update, or Delete coverage.
6. Add missing tasks or retention requirements to resolve gaps.

**[Variant C]**

Lay out use cases on horizontal axis and domain objects on vertical axis.
2. For basic CRUD, evaluate each cell and mark Create (C), Read (R), Update (U), or Delete (D).
3. For expanded UCOM, replace simple letters with specific object responsibility descriptions.
4. Verify every object has at least one 'C' and at least one 'R'.
5. Identify missing use cases or redundant objects based on blank rows/columns.

**[Variant D]**

List all business data classes/entities along the vertical axis of a matrix.
2. List all business events along the horizontal axis.
3. For each entity, map which events Create (C), Read (R), Update (U), or Delete (D) instances of that entity.
4. Analyze empty rows and columns.
5. If an entity is never Created, find the missing creation business event.
6. If an entity is Created but never Read, determine if it is unneeded or if a reading event is missing.
7. Update the event list, context diagram, and data model to resolve gaps.

**[Variant E]**

List data entities across table columns.
2. List use cases, tasks, or system events down table rows.
3. For each cell, indicate whether the row action Creates (C), Reads (R), Updates (U), or Deletes (D) the column entity.
4. Inspect each column: verify that every entity has at least one 'C', one 'R', one 'U', and one 'D' across the system.
5. If an entity is updated or read but never created, identify missing creation requirements.
6. If an entity is created but never read, evaluate whether it is extraneous or missing a read function.

## Analyst Questions & Prompts

**[Variant A]**

Does this use case create, read, update, or delete this data class? Are there any data classes that are never created or never deleted by any use case?

**[Variant B]**

How does this entity get created? Which task allows a user to update or delete this record?

**[Variant C]**

Where is this object created? Which use case reads or updates it?

**[Variant D]**

"What business event creates instances of this data class?", "Which events read or reference this data?", "When and why is this data updated?", "What business rule or event permits deletion or archiving of this data?"

**[Variant E]**

Which use case creates this entity? Where is this data entity updated or deleted? Are there entities that are never read by any system task?

## Minimal Realistic Example

**[Variant A]**

Mapping a library system: 'New borrower' use case Creates Borrower class; 'Borrow book' Reads Borrower, Updates Book, and Creates Loan class.

**[Variant B]**

Matrix check revealing that 'Guest' entities had no 'Delete' task, leading to the creation of a data retention requirement.

**[Variant C]**

'Book New Loan' reads 'Loan Request' and 'Loan Agreement', and creates 'Loan Account'.

**[Variant D]**

Building a CRUD matrix for a Road Deicing System and discovering that the 'Invoice' entity is created by 'Time for invoices to be sent' but never read by any event, revealing a missing event or interface with an external accounting system.

**[Variant E]**

Entity 'Requester' has 'C' in 'Edit Requesters' use case, 'R' in 'Place Order' use case, but no 'D' in any use case, uncovering a missing delete/deactivate requirement.

## Quality Criteria & Verification

**[Variant A]**

Every class has at least one 'C' (Create) and 'D' (Delete) across its row; every use case interacts with at least one data class.

**[Variant B]**

100% CRUD lifecycle coverage for all database entities.

**[Variant C]**

Completeness check: no orphan objects (missing C or R), clear responsibility allocation for every interaction.

**[Variant D]**

Every data class has at least one Create and at least one Read event mapped in the matrix; no orphaned data or dangling references remain.

**[Variant E]**

Verify every entity column contains 'C', 'R', 'U', and 'D' entries across the row set (unless omission is a validated business rule); review matrix with business domain experts.

## Errors & Anti-Patterns

**[Variant A]**

Failing to check for orphan classes with no Create or Read operations; ignoring CRUD validation until late in software testing.

**[Variant B]**

Performing CRUD checks late in the development cycle after database schemas are frozen.

**[Variant C]**

Creating CRUD matrices without specifying exact responsibility descriptions on complex systems.

**[Variant D]**

Performing CRUD analysis on physical database tables instead of essential business data classes; omitting housekeeping/lifecycle events (archiving, deletion).

**[Variant E]**

Failing to check for missing deletion/archiving functions; leaving orphan entities created by processes but never retrieved.

## When NOT to Use

**[Variant A]**

In simple projects with under 3 use cases and 2 data tables where manual inspection is trivial.

**[Variant B]**

None; essential analysis technique for all data-centric applications.

**[Variant C]**

Extremely small systems with fewer than 3 use cases and 2 domain entities.

**[Variant D]**

Small stateless applications that do not store or persist business data.

**[Variant E]**

For simple applications with trivial 1-to-1 mappings between a single form and a single database table.

## Alternatives & Complementary Methods

**[Variant A]**

Requirements Traceability Matrix, Use Case Modelling, Class Modelling.

**[Variant B]**

Data Model, Tasks with Data, Event List.

**[Variant C]**

Sequence Diagrams, Collaboration Diagrams, Traceability Matrices.

**[Variant D]**

Information Engineering Data Flow Analysis, Domain-Driven Design Event Storming.

**[Variant E]**

Traceability Matrix, DFD balancing.

## Supported Decisions

**[Variant A]**

Model completeness validation, development iteration sequencing, work package packaging, effort estimation.

**[Variant B]**

Completeness verification, missing task discovery, data retention policy definitions.

**[Variant C]**

Subsystem boundary design, object responsibility assignment, gap analysis.

**[Variant D]**

Data model completeness approval, system integration boundary verification, missing functional requirement identification.

**[Variant E]**

Scope, acceptance, architecture.

## AI & Agentic Adaptation

**[Variant A]**

Modeling AI engines automatically compare Use Case text against Class Diagrams to compile verified CRUD matrices and highlight missing data operations.

**[Variant B]**

Evaluate entity models against task lists to auto-detect missing CRUD operations using logic agents.

**[Variant C]**

Not specified in source.

**[Variant D]**

AI data analysis agents can automatically construct and cross-check CRUD matrices from draft event specs and data models, immediately highlighting missing C, R, U, or D operations.

**[Variant E]**

Not in source
