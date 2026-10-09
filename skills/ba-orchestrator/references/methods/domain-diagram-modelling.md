---
id: domain-diagram-modelling
name: "Domain Diagram Modelling"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.3"
subtask_name: "Boundaries and Context"
source_count: 1
---

# Domain Diagram Modelling

`T2 Situation Investigation and Elicitation › 2.3 Boundaries and Context`

**Also described as:** Domain Diagram Modeling

## Problem Solved

Provides a holistic, broad view of the current business process ('as-is' problem domain) to prevent point-solution failures, uncover hidden dependencies, and isolate root causes.

## BA Lifecycle Phase

Analysis / Discovery

## Input Artifacts

Elicited process information, operational documentation, interview notes, observation records.

## Output Artifacts

Domain Diagram Model (visual map detailing Goal, Results, Requestor/Beneficiary, Trigger/Setup, Pre/Post-conditions, Supporting Resources/Information, and Internal Activities).

## Participants & Roles

Business Analyst (modeler), Process Workers, SMEs, Business Unit Managers.

## Prerequisites

Initial information gathered regarding the target operational business process.

## Step-by-Step Procedure

Step 1: Define the overarching process goal (verb phrase) of the target process.
2. Step 2: Identify the tangible, persistent result(s) produced that satisfy the goal, and identify the beneficiary role.
3. Step 3: Identify the requestor role and the specific event trigger (plus setup conditions) that launches the process.
4. Step 4: Identify all preconditions (must be true before start) and post-conditions (environmental changes upon completion).
5. Step 5: Map supporting resources (human/system mechanisms) and supporting information consumed during execution.
6. Step 6: Step inside the process boundary to map internal process worker roles, activities, and event-driven transformations.
7. Review the model with process workers to confirm accuracy and identify process gaps/loopholes.

## Analyst Questions & Prompts

• What is the main goal of this business process?
• What tangible result proves the process was successful?
• What exact event triggers this process to start?
• What preconditions must be true before execution begins?
• Who receives the final output (beneficiary)?
• What information or human resources support this process during execution?

## Minimal Realistic Example

A diagram is drawn for Accounts Payable: Goal = 'Pay invoices to receive maximum discount'; Trigger = 'Receipt of voucher batch'; Precondition = 'Purchasing authorization attached'; Result = 'Vendor check & A/P Journal'; Beneficiary = 'Vendor'. Mapping reveals missing terms in setup, causing late checks.

## Quality Criteria & Verification

The domain model must clearly show complete inputs, triggers, outputs, and internal event-activity transformations, and be fully verified by operational process workers.

## Errors & Anti-Patterns

Designing deep technical system interactions before defining the broad business process; omitting preconditions or neighboring process interfaces.

## When NOT to Use

When making an isolated, pure technical fix that has zero impact on business workflows or process worker roles.

## Alternatives & Complementary Methods

Data Flow Diagrams (DFD), BPMN Process Maps, UML Activity Diagrams, Value Stream Mapping.

## Supported Decisions

Business process re-engineering, gap analysis, solution scoping, impact assessment.

## AI & Agentic Adaptation

LLMs can parse unstructured operational SOPs or interview transcripts and auto-generate structured Domain Diagram specifications (e.g., in Mermaid.js format) for analyst validation.
