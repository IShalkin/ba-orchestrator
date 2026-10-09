---
id: usage-centric-elicitation
name: "Usage-Centric Elicitation"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.8"
subtask_name: "Prototypes and Scenarios for Elicitation"
source_count: 1
---

# Usage-Centric Elicitation

`T2 Situation Investigation and Elicitation › 2.8 Prototypes and Scenarios for Elicitation`

**Also described as:** Understanding What Users Need to Do (Usage-Centric Elicitation: Use Cases & User Stories)

## Problem Solved

Prevents feature-centric thinking that results in missing capabilities, gold-plating, unused functionality, and poor user experience.

## BA Lifecycle Phase

Elicitation / Analysis / Specification

## Input Artifacts

Vision Statement, Business Objectives, Stakeholder Catalog / User Classes, Context Diagram.

## Output Artifacts

User Requirements Document / Use Case Specifications, User Stories (with acceptance criteria), Epics, Feature Trees.

## Participants & Roles

Business Analyst (facilitator), User Representatives / Product Champions, End Users, Product Owner, Developers, Testers.

## Prerequisites

Identified user classes and defined solution scope.

## Step-by-Step Procedure

Conduct usage-centric elicitation sessions with representatives of specific user classes.
2. Ask users to describe the goals they need to accomplish and their typical interactive sessions with the solution.
3. Identify use cases, giving each a descriptive name starting with an action verb (e.g., 'Draft an Article').
4. For each use case, elicit the Main Success Scenario (normal flow / happy path).
5. Probe for alternative flows (variations leading to success) and exceptions (error conditions).
6. Document use cases using a structured template (ID, Primary Actor, Pre/Postconditions, Flows) or break them into User Stories (As a... I want to... So that...).
7. Abstract or decompose usage descriptions across appropriate levels (Epics -> Features -> Use Cases / User Stories -> Functional Requirements).

## Analyst Questions & Prompts

"What do you need to do with the solution?", "Please describe a session you might have with the product... What would you be trying to accomplish?", "How do you imagine your dialogue with the system would go?", "What could go wrong at this step, and how should the system assist you?"

## Minimal Realistic Example

For Speak-Out.biz, the Author user class has the use case 'View Article Statistics'. Elicitation reveals a user story: 'As an author, I want to view page-view statistics for my published articles so that I can see which topics my readers enjoy most.'

## Quality Criteria & Verification

Use case names start with an active verb; alternative flows and exceptions are explicitly defined; functional requirements and acceptance tests can be derived completely from scenarios.

## Errors & Anti-Patterns

Focusing elicitation on system features ('What do you want the system to do?') instead of user goals; omitting exception flows; writing user stories without underlying context or user class clarity.

## When NOT to Use

For pure middleware, background batch jobs, real-time embedded sensor routines, or hardware drivers where direct user interaction is minimal or absent.

## Alternatives & Complementary Methods

Complementary: Practice #7 Events and Responses, Practice #11 Modeling (Process Flows), Practice #18 Testing Requirements. Alternatives: Story Mapping, Job-To-Be-Done (JTBD).

## Supported Decisions

Functional scope, iteration backlog breakdown, UI/UX workflow design, test case creation.

## AI & Agentic Adaptation

AI agents can analyze narrative user session transcripts to auto-generate Use Case drafts or User Stories in standard formats, extract potential exception paths, and generate candidate test cases for human review.
