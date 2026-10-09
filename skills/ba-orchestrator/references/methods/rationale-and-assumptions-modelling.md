---
id: rationale-and-assumptions-modelling
name: "Rationale and Assumptions Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 1
---

# Rationale and Assumptions Modelling

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Rationale & Assumptions Modeling

## Problem Solved

Eliminates unjustified or 'gold-plated' requirements, prevents loss of decision history during staff turnover, and protects key requirements from arbitrary deletion.

## BA Lifecycle Phase

Analysis / Specification / Change Management

## Input Artifacts

Vision statements, proposed requirements, change requests, risk logs, technical notes

## Output Artifacts

Justification fields, assumption lists, rationale models (warrant/rebuttal graphs), Satisfaction Arguments, GSN/CAE safety cases

## Participants & Roles

BA, Architect, Sponsor, Domain Specialist, Safety/Compliance Lead

## Prerequisites

Draft requirements or proposed design choices requiring justification.

## Step-by-Step Procedure

Analyze proposed features and ask 'Why is this needed?' or scan texts for giveaway words ('will', 'assumes').
2. List explicit real-world assumptions underlying each requirement.
3. Model supporting arguments (warrants) and opposing arguments (rebuttals).
4. Invert identified risks into defensive functional/quality requirements.
5. Construct Satisfaction Arguments connecting requirements to parent goals.
6. Link requirements to their rationale via attributes or database traces.

## Analyst Questions & Prompts

Why do we need this requirement? What are we assuming about the operating environment? What happens if this assumption fails? What is the rebuttal to this argument?

## Minimal Realistic Example

Justifying heating elements for a handheld device's CMOS processor: Assumption 1 ('Temperatures drop to -50C in mountains') + Assumption 2 ('CMOS fails below -20C') -> Requirement ('Provide internal processor heater'). Rebuttal ('Heater drains battery') -> Countermeasure ('Use insulated casing').

## Quality Criteria & Verification

Completeness of rationale logic, validity of underlying assumptions, peer review of satisfaction arguments.

## Errors & Anti-Patterns

Circular justification ('Required because the client requested it'); documenting rationale for trivial self-evident items; duplicating rationale text across multiple items without tracing.

## When NOT to Use

For standardized, self-explanatory, low-risk functional requirements.

## Alternatives & Complementary Methods

Assumption-Based Planning (ABP), Goal Structuring Notation (GSN), QOC (Questions, Options, Criteria), Toulmin Argumentation.

## Supported Decisions

Requirement prioritization, design option selection, risk mitigation, audit/compliance sign-offs.

## AI & Agentic Adaptation

LLM agents monitor change requests and specifications to automatically extract implicit assumptions, construct Toulmin/GSN rationale graphs, and flag broken assumptions when project parameters change. Human approval validates argument logic.
