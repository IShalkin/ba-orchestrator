---
id: pegs-standard-plan
name: "PEGS Standard Plan"
task: T5
task_name: "Requirements Specification"
subtask: "5.6"
subtask_name: "Requirements Documents and Phrasing"
source_count: 1
---

# PEGS Standard Plan

`T5 Requirements Specification › 5.6 Requirements Documents and Phrasing`

**Also described as:** The PEGS Standard Plan for Requirements

## Problem Solved

Replaces outdated requirements document structures (like IEEE 830) with a modern, comprehensive 4-book structure addressing missing domain context, unstated assumptions, poor project planning, and fragmented system scope.

## BA Lifecycle Phase

Specification

## Input Artifacts

Stakeholder requests, existing process documentation, regulatory texts, interviews, workshops, meeting minutes.

## Output Artifacts

Requirements Repository organized into four core books: Goals Book (G), Environment Book (E), System Book (S), and Project Book (P).

## Participants & Roles

Business Analyst / Requirements Engineer (Lead), Subject-Matter Experts (SMEs), Project Manager, Sponsor/Product Owner, System Architects, Testers, Compliance/Legal.

## Prerequisites

Access to key stakeholders, initial project charter or business mandate, identified domain constraints.

## Step-by-Step Procedure

Set up the Requirements Repository with templates for books P, E, G, S.
2. Draft Goals Book (G.1-G.7) capturing business context, current state, expected benefits, and high-level usage scenarios.
3. Draft Environment Book (E.1-E.6) establishing the domain glossary, environment components, constraints, assumptions, effects, and invariants.
4. Draft System Book (S.1-S.6) defining system architecture/clusters, detailed functionality, external interfaces, usage scenarios, priorities, and acceptance criteria.
5. Draft Project Book (P.1-P.7) detailing roles, technical choices, schedule, tasks, deliverables, technology dependencies, risks, and process logs.
6. Establish cross-references across books adhering to valid reference rules.
7. Review, verify quality criteria, and obtain formal stakeholder endorsements.

## Analyst Questions & Prompts

"Why is this project needed? What business problem are we solving? What external laws, domain rules, or engineering constraints limit us? What assumptions facilitate development? What must the system do, and what is explicitly out of scope?"

## Minimal Realistic Example

Structuring an e-commerce refund system into Goals (reducing manual processing by 20%), Environment (payment gateway APIs, GDPR privacy rules), System (automated refund calculation, refund UI), and Project (milestones, technical stack choices).

## Quality Criteria & Verification

Verification against 14 quality criteria (Correct, Justified, Complete, Consistent, Unambiguous, Feasible, Abstract, Traceable, Delimited, Readable, Modifiable, Verifiable, Prioritized, Endorsed); formal sign-offs in front/back matter.

## Errors & Anti-Patterns

Creating a rigid linear document rather than a living repository; confusing environment constraints with system decisions; omitting out-of-scope limits; skipping justification for technical choices.

## When NOT to Use

Trivial micro-projects where formal specifications incur unnecessary overhead and full 4-book structure is excessive.

## Alternatives & Complementary Methods

IEEE 830 / ISO 29148 templates, Planguage, Goal-oriented RE (KAOS/i*), User Story Mapping.

## Supported Decisions

Scope determination, release architecture, compliance verification, milestone planning, acceptance testing.

## AI & Agentic Adaptation

Prompt AI agents to parse raw stakeholder transcripts into specific PEGS books/chapters, using automated consistency-checking guardrails across constraints and requirements.
