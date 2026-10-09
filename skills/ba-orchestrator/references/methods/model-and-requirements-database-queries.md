---
id: model-and-requirements-database-queries
name: "Model and Requirements Database Queries"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.3"
subtask_name: "Formal Model Verification"
source_count: 2
---

# Model and Requirements Database Queries

`T7 Validation and Acceptance › 7.3 Formal Model Verification`

**Also described as:** Model Database Queries; Requirements Database Queries

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces structural inconsistencies, unlinked elements, orphan requirements, and incomplete cross-view specifications across large multi-view models.

**[Variant B]**

Reduces structural inconsistencies, unlinked elements, and incomplete diagrammatic models through automated database query engines.

## BA Lifecycle Phase

**[Variant A]**

Quality assurance / analysis

**[Variant B]**

Quality assurance / verification

## Input Artifacts

**[Variant A]**

Model database (populated with goal, object, agent, operation, and behaviour model instances), database schema derived from meta-model.

**[Variant B]**

Semi-formal diagrams maintained in a structured Requirements Database (repository).

## Output Artifacts

**[Variant A]**

Query result reports, inconsistency logs, orphan element lists, generated multi-view sub-models (e.g., load analysis views).

**[Variant B]**

Query result sets, structural error logs, missing link reports.

## Participants & Roles

**[Variant A]**

BA, Quality Assurance Specialist, System Architect.

**[Variant B]**

Requirements Engineer / BA, Tool Quality Analyst.

## Prerequisites

**[Variant A]**

Model fragments are recorded as meta-concept/relationship instances in a model database.

**[Variant B]**

Specification stored in a tool with an underlying meta-model schema (e.g., MOF, ER meta-database).

## Step-by-Step Procedure

**[Variant A]**

Select or write entity-relationship queries based on meta-model constraints (e.g., 'Find all leaf goals without assigned agents').
2. Execute query engine over the model database.
3. Analyze returned error/inconsistency sets.
4. Update the multi-view model to resolve highlighted structural gaps.
5. Re-run queries in press-button mode during model evolution.

**[Variant B]**

Define structural consistency and completeness rules at the meta-model level (e.g., intra- and inter-view rules).
2. Formulate corresponding database queries (using SQL, graph query languages, or predefined tool rule sets).
3. Execute queries against the requirements database in press-button mode.
4. Review returned result sets representing rule violations (e.g., unreferenced entities, unbalanced DFD flows).
5. Correct the underlying diagrammatic models to resolve detected violations.

## Analyst Questions & Prompts

**[Variant A]**

Which leaf goals have no operationalizing operations? Which objects in the object model are not concerned by any goal? Which agents are assigned responsibilities exceeding their capabilities?

**[Variant B]**

Is there any entity in the ER diagram that is not referenced by any goal or operation? Is there an output flow in a child DFD missing from the parent bubble?

## Minimal Realistic Example

**[Variant A]**

Executing a query 'unassignedGoals = Goal which not OR-RefTo Refinement and which not OR-AssTo Assignment' to flag all unassigned leaf goals.

**[Variant B]**

Running a pre-cooked query 'Unreferenced Entities' on a UML repository to automatically flag a 'PassengerLog' class that has no relationships or operational use cases.

## Quality Criteria & Verification

**[Variant A]**

Zero error results returned for mandatory structural consistency queries; complete meta-model coverage.

**[Variant B]**

Zero structural violations returned by standard verification query suites.

## Errors & Anti-Patterns

**[Variant A]**

Failing to execute queries after model changes; ignoring query warnings; writing queries with incorrect meta-model role names.

**[Variant B]**

Relying on database queries for semantic adequacy checks (queries only check structural syntax, not whether the requirement is what the customer actually wants).

## When NOT to Use

**[Variant A]**

When the model is tiny and easily inspected manually, or when no structured model database tool is used.

**[Variant B]**

When documentation is maintained purely as unrestricted natural language prose without a structured database repository.

## Alternatives & Complementary Methods

**[Variant A]**

Manual inspection checklists, Xlinkit rule checking, static semantics compiling.

**[Variant B]**

Complementary: Inspections, Model Checking. Alternative: Manual Checklist Review.

## Supported Decisions

**[Variant A]**

Model completeness sign-off, load balancing, structural QA verification.

**[Variant B]**

Model well-formedness verification, static semantics sign-off.

## AI & Agentic Adaptation

**[Variant A]**

Model database query engines can run continuously in the background of BA tools, auto-flagging structural violations as analysts edit diagrams and suggesting fix actions.

**[Variant B]**

Graph-database AI agents can continuously run background graph queries over requirement repositories to report broken traceability or orphan nodes in real time.
