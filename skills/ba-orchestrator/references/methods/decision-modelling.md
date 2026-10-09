---
id: decision-modelling
name: "Decision Modelling"
task: T5
task_name: "Requirements Specification"
subtask: "5.4"
subtask_name: "Business Rules and Decision Logic"
source_count: 1
---

# Decision Modelling

`T5 Requirements Specification › 5.4 Business Rules and Decision Logic`

## Problem Solved

Reduces process complexity and maintainability issues by extracting repeatable operational decision logic and business rules out of process flows into standalone models.

## BA Lifecycle Phase

analysis / specification / architecture

## Input Artifacts

Business rules, process models, data elements, business knowledge sources.

## Output Artifacts

Decision Tables, Decision Trees, Decision Requirements Diagrams (DRD).

## Participants & Roles

BA, Business Rules Developer, Domain SME, Compliance Lead.

## Prerequisites

Identification of discrete operational decision points within a process.

## Step-by-Step Procedure

Identify discrete decision points within business processes.
2. Decompose complex decisions into input data, sub-decisions, and business knowledge models.
3. Create a Decision Requirements Diagram (DRD) linking decisions, inputs, and knowledge sources.
4. Represent atomic decision logic using Decision Tables or Decision Trees.
5. Ensure decision tables cover all input condition combinations without gaps or overlaps.
6. Link decision models to process models and business rules engines.

## Analyst Questions & Prompts

"What decision is made at step X in the process?", "What input data is required to make this decision?", "What combination of rules leads to outcome Y?"

## Minimal Realistic Example

A Decision Table evaluates 'Loan Amount' and 'Applicant Age': If Amount <= $1,000 and Age > 18 -> Outcome = 'Eligible'; If Age <= 18 -> Outcome = 'Ineligible'.

## Quality Criteria & Verification

Decision tables are complete (no missing condition rows) and consistent (no conflicting outcomes for identical inputs); standalone readability by business SMEs.

## Errors & Anti-Patterns

Mixing process flow logic with decision logic; capturing decision rules without standardizing underlying business terminology.

## When NOT to Use

For one-off strategic decisions (use Decision Analysis instead) or simple processes with no conditional branching.

## Alternatives & Complementary Methods

Complemented by Business Rules Analysis, Process Modelling, Concept Modelling, and Data Dictionary.

## Supported Decisions

Automated operational decisions (loan approval, pricing, claim validation, tax calculation).

## AI & Agentic Adaptation

AI agents can convert decision requirements diagrams directly into DMN-compliant XML for automated execution, verifying table completeness programmatically.
