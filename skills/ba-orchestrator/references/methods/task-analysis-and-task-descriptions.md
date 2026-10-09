---
id: task-analysis-and-task-descriptions
name: "Task Analysis and Task Descriptions"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 4
---

# Task Analysis and Task Descriptions

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

**Also described as:** High-Level Tasks (BPR Tasks); Task Analysis; Task Descriptions; Tasks with Data

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Defines the detailed execution steps, input/output data, triggers, prerequisites, and business rules for a single business process task, reducing operational ambiguity.

**[Variant B]**

Specifies user work requirements at the domain level without restricting product design or specifying premature user interface mechanics.

**[Variant C]**

Identifies overarching client business processes to enable Business Process Re-engineering (BPR) and avoid local sub-optimization.

**[Variant D]**

Ensures that all visible data required by a user to complete each sub-task variant is explicitly identified for screen design and verification.

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Business Process Analysis / Specification

**[Variant B]**

analysis

**[Variant C]**

elicitation

**[Variant D]**

analysis

## Input Artifacts

**[Variant A]**

Business Process Model, task list, business rules, document specs.

**[Variant B]**

User interviews, workplace observations, business process models.

**[Variant C]**

Business goals, client journey maps, high-level process flows.

**[Variant D]**

Task descriptions, E/R data model, Virtual Windows.

## Output Artifacts

**[Variant A]**

Task Description document (Identifier, Name, Actor, Prerequisites, Trigger, Inputs, Outputs, Goals, Performance Measures, Steps, Rules).

**[Variant B]**

Structured task descriptions (Purpose, Trigger/Preconditions, Frequency, Criticality, Sub-tasks, Variants).

**[Variant C]**

High-level task descriptions centered around the end-client's total business case.

**[Variant D]**

Three-column table listing Sub-tasks/Variants, Visible Data Needs, and Related Screen Windows.

## Participants & Roles

**[Variant A]**

BA, Task Actor / SME.

**[Variant B]**

BA, SME, end user, developer, vendor.

**[Variant C]**

BA, business owner, client/end-user, consultant.

**[Variant D]**

BA, UI designer, SME, developer.

## Prerequisites

**[Variant A]**

Identification of the task within a business process model.

**[Variant B]**

Identification of user roles and closed business work goals.

**[Variant C]**

Identification of end-clients and strategic business goals.

**[Variant D]**

Completed task descriptions and draft E/R data model.

## Step-by-Step Procedure

**[Variant A]**

Record task identifier (e.g., 2/1) and name ('imperative verb noun').
2. Identify actor role and prerequisites.
3. Identify triggering business event (distinct from inputs).
4. List input and output information/documents.
5. Define task goals and performance measures.
6. Document detailed steps (using text or Activity Diagram) and embedded business rules.

**[Variant B]**

Identify closed user work goals (closure rule).
2. Describe work environment and user profile in the work area header.
3. Define task purpose, triggers, frequency, and critical scenarios.
4. Detail essential sub-tasks (domain level: human and computer combined).
5. List realistic sub-task variants and exception cases.

**[Variant C]**

Identify the ultimate end-client's goal (e.g., 'A stay at the hotel').
2. Outline client sub-tasks from start to finish.
3. Identify client pain points and operational bottlenecks across sub-tasks.
4. Brainstorm radical BPR solutions (e.g., self-service Web options).
5. Decompose validated high-level tasks into operational user tasks.

**[Variant D]**

Take sub-tasks and sub-task variants from task descriptions.
2. For each sub-task/variant, detail the specific data items the user must see or enter.
3. Cross-check data items against the E/R model.
4. Map data needs to candidate screen windows and search criteria.
5. Review mappings with UI designers.

## Analyst Questions & Prompts

**[Variant A]**

What triggers you to start this specific task? What must be true before you start? What information do you need? What steps do you take? What rules govern your decision?

**[Variant B]**

What is the ultimate goal of this work session? When do you feel this task is complete? What special or unusual cases happen?

**[Variant C]**

What is the client trying to achieve from start to finish? Where do clients experience delays or friction in this journey?

**[Variant D]**

What exact pieces of data do you need to see on the screen to decide which room to choose?

## Minimal Realistic Example

**[Variant A]**

Documenting Task 2/1 'Review complaint' performed by Customer Services Manager, triggered by 'Formal complaint received', requiring account/call records, outputting decision/compensation.

**[Variant B]**

Task 1.2: Checkin. Purpose: Give guest a room, mark occupied. Trigger: Guest arrives. Sub-tasks:
1. Find room 2. Record guest 3. Deliver key. Variants: 1a. Guest pre-booked.

**[Variant C]**

Task 1: A stay at the hotel. Client Sub-tasks:
1. Select hotel 2. Book 3. Check in 4. Receive service 5. Check out 6. Reimburse expenses.

**[Variant D]**

Sub-task 1a (No suitable room): Visible Data = All free rooms, price, available discounts; Virtual Window = Rooms (Criteria: dates).

## Quality Criteria & Verification

**[Variant A]**

Clear distinction between triggering event and input data; measurable performance targets; complete step-by-step procedural description covering exceptions.

**[Variant B]**

User validation walkthrough, CRUD matrix check, task execution walkthrough during system test.

**[Variant C]**

Traceability matrix connecting high-level tasks to business goals and operational sub-tasks.

**[Variant D]**

Traceability check against E/R model fields; UI layout verification during prototype reviews.

## Errors & Anti-Patterns

**[Variant A]**

Confusing input data arrival with the actual triggering event; omitting prerequisites; failing to document embedded business decision rules.

**[Variant B]**

Writing low-level programming steps instead of domain goals; defining tasks that lack closure (e.g., 'enter text').

**[Variant C]**

Designing system features around existing clerical staff steps without considering the client's high-level workflow.

**[Variant D]**

Listing technical database fields instead of user-perceived domain information.

## When NOT to Use

**[Variant A]**

For high-level corporate strategic option planning or macro value chain mapping.

**[Variant B]**

Purchasing low-level technical components or maintenance projects focused strictly on isolated software bug fixes.

**[Variant C]**

Small maintenance projects or minor software enhancements.

**[Variant D]**

Projects purchasing standard COTS software without custom screen development.

## Alternatives & Complementary Methods

**[Variant A]**

Task modelling, Activity Diagrams, Use Case Descriptions, Decision Tables.

**[Variant B]**

Tasks & Support, Use Cases, Activity Diagrams.

**[Variant C]**

Tasks & Support, Value Stream Mapping, Goal-Domain Tracing.

**[Variant D]**

Virtual Windows, Task Descriptions, CRUD Matrix.

## Supported Decisions

**[Variant A]**

Job description design, user training curriculum, operational performance target setting, automated user interface requirements.

**[Variant B]**

COTS vendor selection, business process redesign, user acceptance test planning.

**[Variant C]**

Business process re-engineering, strategic IT investment choices, system scope boundaries.

**[Variant D]**

UI screen layout, UI data binding specifications.

## AI & Agentic Adaptation

**[Variant A]**

AI task-capture assistants log user desktop actions to draft initial task step descriptions, inputs, and outputs automatically.

**[Variant B]**

Analyze user transcriptions or observation logs to generate structured task templates with variants.

**[Variant C]**

Map end-to-end customer journey maps to high-level BPR tasks using strategic AI prompts.

**[Variant D]**

Map entity model attributes automatically to sub-task steps using domain reasoning prompts.
