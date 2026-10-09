---
id: requirements-quality-verification-and-analysis
name: "Requirements Quality Verification and Analysis"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.1"
subtask_name: "Reviews and Inspections"
source_count: 3
---

# Requirements Quality Verification and Analysis

`T7 Validation and Acceptance › 7.1 Reviews and Inspections`

**Also described as:** Analyzing Requirements and Requirement Sets; Requirements Quality Verification; Requirements validation

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Prevents costly downstream software defects, project failures, and legal disputes by systematically evaluating requirements against 14 objective quality criteria.

**[Variant B]**

Verifies that requirements are correctly specified (Verification) and validates that they deliver real business value (Validation), reducing costly defects in delivered solutions.

**[Variant C]**

Identifies missing information, requirement conflicts, ambiguities, unfeasible features, unhandled exceptions, and bad assumptions before development starts.

## BA Lifecycle Phase

**[Variant A]**

Validation

**[Variant B]**

Define Requirements / Requirements Development / Quality Assurance

**[Variant C]**

Analysis / Validation

## Input Artifacts

**[Variant A]**

Draft Requirements Repository (Books P, E, G, S), stakeholder interview/workshop reports, regulatory constraints.

**[Variant B]**

Requirements Specification, Requirements Catalogue, Business Objectives, CRUD Matrix.

**[Variant C]**

Elicited draft requirements, User Stories, Use Cases, Business Rules, Quality Attributes, Models.

## Output Artifacts

**[Variant A]**

Requirements Quality Verification Report, issue logs, signed endorsement pages.

**[Variant B]**

Verified/Validated Requirements Document, Quality Review Logs, Sign-off Records.

**[Variant C]**

Refined/Decomposed Requirements, Feature Trees, Split User Stories/Epics, Acceptance Criteria, Analysis Checklists, Risk Analysis.

## Participants & Roles

**[Variant A]**

Requirements Engineer / Quality Auditor (Lead), Subject-Matter Experts, Lead Developers, Testers, Sponsor / Product Owner.

**[Variant B]**

BA, Quality Reviewers, Domain Experts, Business Owner, Sponsor.

**[Variant C]**

Business Analyst, Developers, Testers, Systems Architect, User Representatives.

## Prerequisites

**[Variant A]**

Completed initial draft of requirements books conforming to the Standard Plan.

**[Variant B]**

Documented draft requirements specification.

**[Variant C]**

Initial draft of requirements or backlog items gathered during elicitation.

## Step-by-Step Procedure

**[Variant A]**

Evaluate Environment and System requirements against domain reality and stakeholder intent (Correctness).
2. Verify that every project/system requirement traces to a goal or constraint (Justification, Traceability).
3. Perform the 6 completeness checks (Document, Goal, Scenario, Environment, Interface, Command-Query Completeness).
4. Inspect text for internal contradictions and terminology mismatches against the glossary (Consistency, Non-ambiguity).
5. Review technical feasibility with developers and assess schedule realism (Feasibility).
6. Verify that requirements specify 'what' not 'how', converting operational overspecifications into implementation hints (Abstractness).
7. Verify scope limits in G.6 (Delimitedness) and check readability rules (Readability).
8. Check auto-numbering/indexing for Modifiability and falsifiability/testability for Verifiability.
9. Verify that all system behaviors in S.2 have priority ratings in S.5 (Prioritization).
10. Obtain formal written sign-offs from key decision-makers (Endorsement).

**[Variant B]**

Check individual requirements against Quality Criteria (Unambiguous, Clear, Complete, Consistent, Testable, Feasible, etc.).
2. Check requirement set for completeness using CRUD matrix.
3. Conduct Necessity Checking against business goals.
4. Execute Static Testing (Peer reviews, Walkthroughs, Technical reviews, Inspections).
5. Obtain formal stakeholder sign-off.

**[Variant C]**

Analyze individual requirements for quality properties: Completeness, Correctness, Feasibility, Necessity, Priority, Unambiguity, Verifiability (or INVEST for stories).
2. Decompose large requirements/epics into finer granularity (e.g., using Feature Trees or story splitting).
3. Trace each requirement back to its origin and rationale; verify underlying assumptions and constraints.
4. Proactively identify exception conditions and safety/business risks.
5. Analyze sets of requirements for gaps, inconsistencies, redundancies, and dependencies.
6. Represent requirements in alternative forms (models, tables) to surface hidden disconnects.
7. Refine requirements and define clear acceptance criteria.

## Analyst Questions & Prompts

**[Variant A]**

"Is this requirement correct and justified? Can it be tested or falsified? Does it prescribe an implementation choice? Is it consistent with the glossary? Have all decision-makers endorsed it?"

**[Variant B]**

Is this requirement unambiguous and testable? Does it contribute to our business goals? Is it consistent with other requirements? Are there any missing CRUD aspects?

**[Variant C]**

"Why is this requirement present?", "What assumptions are we making?", "What exceptions or error conditions could prevent success?", "Does Requirement A contradict Requirement B?", "Can this be verified/tested?"

## Minimal Realistic Example

**[Variant A]**

Auditing a requirement 'The system shall display messages instantaneously' -> flagging it for ambiguity/unverifiability -> rewriting to 'display messages within 0.1s' -> verifying feasibility with developers.

**[Variant B]**

Conducting a formal Inspection review of a 50-item Requirements Catalogue against a quality checklist, uncovering 3 ambiguous statements and 2 missing delete operations.

**[Variant C]**

The BA examines an epic 'Order Placement' and uses a Feature Tree to decompose it into subfeatures (Order building, Order editing, Order cancellation). During analysis, an unhandled exception 'Attempting to order an out-of-stock item' is discovered and specified.

## Quality Criteria & Verification

**[Variant A]**

Compliance with all 14 Quality Criteria: Correct, Justified, Complete, Consistent, Unambiguous, Feasible, Abstract, Traceable, Delimited, Readable, Modifiable, Verifiable, Prioritized, Endorsed.

**[Variant B]**

Requirements satisfy all 18 quality criteria (Unambiguous, Clear, Complete, Consistent, etc.); documented defect log resolved; formal stakeholder sign-off achieved.

**[Variant C]**

Individual statements meet all quality criteria (SMART/INVEST); the requirement set is modifiable, traceable, complete, and consistent.

## Errors & Anti-Patterns

**[Variant A]**

Aiming for 'perfection' at the expense of system delivery (violating the Requirements Effort Principle); treating verification as a one-time Waterfall phase rather than an ongoing process.

**[Variant B]**

Confusing verification (doing things right) with validation (doing the right thing); skipping reviews due to schedule pressure; conducting reviews without checklists.

**[Variant C]**

Premature detailed analysis on volatile low-priority items; ignoring exception paths; accepting ambiguous words ('suitable', 'user-friendly'); duplicating text across multiple specification sections.

## When NOT to Use

**[Variant A]**

Quality verification principles apply to all projects, though the level of rigor scales with project risk.

**[Variant B]**

In informal exploratory brainstorming where quality filtering would choke creative idea generation.

**[Variant C]**

Always required; analysis is an essential bridge between elicitation and implementation.

## Alternatives & Complementary Methods

**[Variant A]**

SMART Criteria inspection, Fagan Inspection, Peer Review, Prototype Validation.

**[Variant B]**

Peer Reviews, Inspections, Walkthroughs, CRUD Matrix, Prototyping.

**[Variant C]**

Complementary: Practice #11 Models, Practice #12 Prototypes, Practice #13 Prioritization, Practice #18 Reviews and Testing.

## Supported Decisions

**[Variant A]**

Project phase-gate approvals, user acceptance test readiness, sign-off on legal/development contracts.

**[Variant B]**

Requirements baselining approval, quality gateway progression, development phase authorization.

**[Variant C]**

Estimation accuracy, sprint/iteration readiness (Definition of Ready), implementation scheduling, risk mitigation.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can continuously audit requirements repositories against the 14 quality criteria, detecting ambiguous words ('user-friendly', 'fast'), cross-reference errors, missing priorities, or orphan requirements.

**[Variant B]**

Static analysis AI tools audit requirements catalogue text against quality rules, flagging passive voice, ambiguity, contradictions, or un-testable statements automatically.

**[Variant C]**

AI agents can run automated ambiguity and quality scans on requirement documents, detect duplicated or conflicting statements across large backlogs, generate exception scenario candidates, and auto-populate INVEST checklists.
