---
id: creating-requirements-models-visual-analysis
name: "Creating Requirements Models (Visual Analysis)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.5"
subtask_name: "Decomposition and Systems Analysis"
source_count: 1
---

# Creating Requirements Models (Visual Analysis)

`T4 Modelling and Analysis › 4.5 Decomposition and Systems Analysis`

## Problem Solved

Overcomes cognitive overload from dense text ('sea of details'), surfaces missing/conflicting logic, and bridges communication gaps with visual learners.

## BA Lifecycle Phase

Analysis / Specification

## Input Artifacts

Draft text requirements, use case narratives, user stories, data dictionaries, process descriptions.

## Output Artifacts

Visual Models (Process Flows/Flowcharts, DFDs, ERDs, Decision Tables/Trees, State-Transition Diagrams, Feature Trees, Requirements Mapping Matrix).

## Participants & Roles

Business Analyst, End Users / Stakeholders, Developers, Systems Architect, Testers.

## Prerequisites

Unstructured or structured requirements text requiring validation or analysis.

## Step-by-Step Procedure

Select appropriate modeling notations based on the domain, problem complexity, and audience (e.g., Process Flow for workflows, STD for stateful objects).
2. Create initial draft ('strawman') models quickly using simple tools (whiteboards, sticky notes).
3. Walk through the models collaboratively with stakeholders to validate visual flows and spot errors or gaps.
4. Use strawman estimations (e.g., extreme values) to prompt stakeholders to provide accurate missing data.
5. Refine models and transfer them to formal diagramming tools (Visio, Lucidchart).
6. Cross-check multiple models against one another (e.g., compare DFD data stores to ERD entities, process steps to functional requirements) using a Requirements Mapping Matrix.

## Analyst Questions & Prompts

"Can an invoice go directly from Prepared to Canceled?", "What causes the system to transition from State A to State B?", "Does every process step in this flowchart have corresponding functional requirements?", "Does this diagram accurately depict your daily work?"

## Minimal Realistic Example

A BA draws a State-Transition Diagram for an Invoice object (Initiated -> Prepared -> Sent -> Partially Paid -> Paid). Reviewing the diagram with billing staff reveals a missing state 'Being Revised' when a customer requests job changes.

## Quality Criteria & Verification

Models adhere to standard notation syntax; all model elements map to text requirements/data dictionary items; cross-model consistency checks pass without discrepancies.

## Errors & Anti-Patterns

Inventing custom, non-standard visual notations that confuse readers; treating modeling as a one-time documentation exercise rather than an iterative analysis tool; modeling parts of the system that are simple and well-understood.

## When NOT to Use

When the logic, process, or data is extremely simple and can be unambiguously communicated in 1-2 plain text sentences.

## Alternatives & Complementary Methods

Complementary: Practice #8 Data Concepts, Practice #10 Requirement Analysis, Practice #12 Prototypes, Practice #18 Testing Models. Alternatives: Plain natural language text.

## Supported Decisions

Workflow redesign, architectural component allocation, test scenario mapping, feature scoping.

## AI & Agentic Adaptation

AI agents can convert text specifications directly into code-based diagrams (Mermaid, PlantUML), analyze visual model scripts for unreachable states or dead-end process paths, and highlight discrepancies between models and user stories.
