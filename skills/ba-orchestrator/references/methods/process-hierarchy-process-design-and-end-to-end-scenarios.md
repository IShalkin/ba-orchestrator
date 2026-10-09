---
id: process-hierarchy-process-design-and-end-to-end-scenarios
name: "Process Hierarchy, Process Design and End-to-End Scenarios"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 1
---

# Process Hierarchy, Process Design and End-to-End Scenarios

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

## Problem Solved

Prevents fragmented, inconsistent process models and missed handoffs in large scopes by building a complete process taxonomy top-down, designing every process with one template, and validating the whole with end-to-end scenarios that chain processes together.

## BA Lifecycle Phase

Analysis / specification / validation

## Input Artifacts

Capability model or business area map, scope item list, as-is process descriptions, future-state goals, workshop notes, security and compliance standards.

## Output Artifacts

Process hierarchy (levels: business area, capability, process group, process; unique ids; owner role per process); process design per leaf process (purpose, trigger, inputs and outputs, steps, decision points, business rules, roles, exceptions, system touchpoints, KPIs); end-to-end business scenarios (named chains of processes with the handoffs and data passed between them); coverage matrix (process x scenario) with orphans listed.

## Participants & Roles

BA (owner), business architect, process owners, SMEs, solution architect, test lead.

## Prerequisites

Agreed scope boundary; a high-level view of the capabilities or business areas in scope; access to process owners for workshops.

## Step-by-Step Procedure

1. Obtain or draft the high-level view of the capabilities in scope.
2. Decompose it top-down into a process hierarchy with consistent levels and unique ids, and assign an owner role to each process.
3. Run workshops per process group to detail the future-state processes.
4. Write a process design for each leaf process using one template (trigger, steps, decision points, rules, roles, exceptions, systems, KPIs).
5. Define end-to-end scenarios that chain processes across the hierarchy for the key business situations (for example request-to-pay or order-to-cash).
6. Build the coverage matrix: every leaf process appears in at least one scenario and every scenario step maps to a leaf process; resolve the orphans in both directions.
7. Validate the scenarios with the process owners and keep the set as a living baseline for scope changes, estimates, use cases and test cases.

## Analyst Questions & Prompts

• What are the main business areas in scope, and which capabilities sit under each?
• Who owns this process?
• What triggers it, and what does it hand over to the next process?
• Which end-to-end business situations matter most?
• Where do handoffs between teams or systems break today?
• Is every process used by at least one real scenario, and if not, why is it in scope?

## Minimal Realistic Example

Hierarchy: 'P2 Procurement > P2.1 Sourcing > P2.1.3 Run tender'. Process design P2.1.3: trigger 'approved sourcing request', six steps, rule 'tenders above the approval threshold need two approvers', exception 'no valid bids'. Scenario 'Request-to-Pay': P2.1.1 > P2.1.3 > P2.2.1 > P3.4.2, with the data handed over at each step. The coverage matrix shows P2.3.4 in no scenario, so it is flagged: either out of scope or a missing scenario.

## Quality Criteria & Verification

Decomposition levels are consistent; every process has a unique id and an owner role; every leaf process has a design in the same template; every leaf process appears in at least one scenario and every scenario step maps to a leaf process; handoffs state what passes between processes; as-is and to-be are labelled separately; the scenarios are validated by the process owners.

## Errors & Anti-Patterns

Detailing processes before the hierarchy exists, which produces inconsistent granularity and duplicates; mixing levels in one model; designing processes in isolation without scenarios, which misses handoffs; turning scenarios into test scripts too early; processes without owners; mixing as-is and to-be; letting the hierarchy go stale after scope changes.

## When NOT to Use

The scope is a single process or one small change (model it directly with Business Process Modelling); the scope is purely data or algorithmic, with no business process.

## Alternatives & Complementary Methods

Capability Modelling (before); Business Process Modelling (BPMN, Swimlanes) as the notation for each process design; Process Analysis and Process Redesign Patterns to improve individual processes; Functional Decomposition for the systems view; Use Cases and Use Case-Driven Test Planning derived from the scenarios; CRUD Matrix to cross-check against the data model.

## Supported Decisions

Scope baseline and change impact, estimation, solution design, release grouping, test scenario design, process ownership.

## AI & Agentic Adaptation

An agent drafts the hierarchy from capability maps and documents, drafts a process design per leaf process from workshop notes, and computes the coverage matrix to flag orphans; process owners validate. Keep ids stable so that traceability survives revisions.
