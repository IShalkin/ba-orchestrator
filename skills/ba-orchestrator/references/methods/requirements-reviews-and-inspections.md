---
id: requirements-reviews-and-inspections
name: "Requirements Reviews and Inspections"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.1"
subtask_name: "Reviews and Inspections"
source_count: 6
---

# Requirements Reviews and Inspections

`T7 Validation and Acceptance › 7.1 Reviews and Inspections`

**Also described as:** Requirements Inspection; Requirements Inspection (Formal Peer Review); Requirements Inspections and Reviews; Requirements Review and Risk Assessment; Reviewing and Testing Requirements (Peer Reviews, Fit Criteria, Acceptance Tests); Reviews

This card merges 6 descriptions of the method, labelled Variant A–F in every field.

## Problem Solved

**[Variant A]**

Reduces defect leaks and quality errors by systematically evaluating business analysis work products with peers and stakeholders.

**[Variant B]**

Reduces defects, omissions, contradictions, ambiguities, and inaccuracies across all specification formats through structured human peer review.

**[Variant C]**

Systematically detects requirements defects (ambiguities, contradictions, incompleteness) using a formal, multi-role review process.

**[Variant D]**

Detects major requirement defects, ambiguities, omissions, and inconsistencies early, avoiding expensive downstream defect rework during testing or deployment.

**[Variant E]**

Finds requirement defects, ambiguities, omissions, and un-testable logic early before code construction, avoiding expensive late-stage rework.

**[Variant F]**

Validates requirements completeness, correctness, and feasibility prior to contracting, identifying high-risk requirements for mitigation.

## BA Lifecycle Phase

**[Variant A]**

validation / verification / Requirements Life Cycle Management

**[Variant B]**

Quality assurance / consolidation

**[Variant C]**

Validation

**[Variant D]**

validation

**[Variant E]**

Validation

**[Variant F]**

validation

## Input Artifacts

**[Variant A]**

Work product / deliverable package (requirements spec, models, user stories), review checklist, objectives.

**[Variant B]**

Requirements Document (RD), review guidelines, inspection checklists (defect-based, quality-specific, domain-specific, language-based).

**[Variant C]**

Requirements specification/document, defect logging sheets, review guidelines

**[Variant D]**

Requirements document/SRS to inspect, predecessor artifacts (vision/scope, use cases), defect checklist, entry criteria checklist

**[Variant E]**

Draft Requirements Specifications, Use Cases, User Stories, Visual Models, Quality Attributes.

**[Variant F]**

Draft requirements specification, review checklists, risk rating scales.

## Output Artifacts

**[Variant A]**

Logged defects, review findings report, approved deliverable, requested rework items.

**[Variant B]**

Inspection reports, defect logs, list of false positives, consolidated/revised Requirements Document.

**[Variant C]**

Consolidated error list, inspection protocol, approved requirements baseline

**[Variant D]**

Inspection Issue/Defect Log, Inspection Summary Report, Exit Criteria Sign-off

**[Variant E]**

Inspection/Review Defect Logs, Acceptance Criteria / Acceptance Tests (Given-When-Then), Fit Criteria, Highlighted Model Test Traces.

**[Variant F]**

Review defect log, Risk Assessment Matrix (Customer Risk vs. Developer Risk per requirement), risk mitigation plan.

## Participants & Roles

**[Variant A]**

Author (BA), Reviewer(s) (Peer, SME, Tester, Architect), Facilitator, Scribe.

**[Variant B]**

Inspection Leader/Moderator, Author(s) of RD, Independent Reviewers (Domain SME, User, Developer, QA Specialist).

**[Variant C]**

Organizer, Moderator, Author, Reader, Inspectors, Minute-taker

**[Variant D]**

BA (author), Moderator (facilitator), Reader (paraphraser), Recorder (scribe), Inspectors (developers, testers, user representatives/SMEs)

**[Variant E]**

Business Analyst (author), Peer BAs, User Representatives / Product Champions, Developers, Software Testers.

**[Variant F]**

BA, customer review team, developer review team, QA manager.

## Prerequisites

**[Variant A]**

Completed draft work product and defined review objectives/checklists.

**[Variant B]**

Availability of a complete draft RD and structured inspection checklists.

**[Variant C]**

Documented requirements available; formal review team assigned and prepared.

**[Variant D]**

Document meets entry criteria (formatting complete, line numbers added, TBDs logged, pre-inspection sample check passed); inspectors perform individual preparation.

**[Variant E]**

Documented draft requirements or analysis models ready for evaluation.

**[Variant F]**

Completed draft requirements specification.

## Step-by-Step Procedure

**[Variant A]**

Define review objectives and select technique (Inspection, Formal Walkthrough, Single Issue Review, Desk Check, Pass Around, Ad-hoc).
2. Identify participants (Author, Reviewers, Facilitator, Scribe) and distribute work product in advance.
3. Reviewers individually inspect work product against checklists and log preliminary defects.
4. Conduct joint review meeting: walk through document, discuss findings, and log agreed defects/action items.
5. Author performs required rework to correct logged defects.
6. Facilitator/Reviewers verify rework and approve final deliverable.

**[Variant B]**

(Planning) Select independent inspection team (min. 3), define scope, and distribute material.
2. (Individual Reviewing) Inspectors read RD individually in free, checklist-based, or process-based (role-based) mode, logging detected defects.
3. (Review Meeting) Inspectors meet (max. 2 hours) to evaluate logged defects, discard false positives, analyze root causes, and agree on recommendations.
4. (Documentation) Produce an official inspection report signed by all inspectors.
5. (Consolidation) Authors revise the RD to fix agreed defects.

**[Variant C]**

Planning: Define goals, inspect artifacts, and assign roles.
2. Overview: Author presents the requirements to ensure common baseline understanding.
3. Individual/Team Error Detection: Inspectors search the text/models for defects.
4. Error Collection & Consolidation: Convene a meeting to collect, filter, and document true defects into an error list.
5. Defect Correction: Author fixes logged issues.

**[Variant D]**

Planning: Author and Moderator select inspection team, schedule meetings, and set pacing rate (2-4 pages/hour).
2. Preparation: Inspectors independently examine the document using defect checklists to log initial issues.
3. Meeting: Reader paraphrases requirements one by one; inspectors present defects; Recorder logs issues; Moderator keeps focus on defect finding (max 2 hours).
4. Rework: Author resolves logged defects and edits specification.
5. Follow-up: Moderator verifies that all rework was completed correctly and checks exit criteria.

**[Variant E]**

Select review/validation technique based on risk (Peer Deskcheck, Passaround, Team Review, Inspection, or Test Generation).
2. Assemble a review team including information providers (users/SMEs) and information consumers (developers/testers).
3. Conduct structured reviews using defect checklists to identify ambiguities, gaps, and un-testable statements.
4. Write conceptual acceptance tests (e.g., Given-When-Then format) or quantitative Fit Criteria directly from requirements/use cases.
5. Compare derived tests against requirements text to reveal missing functionality or invalid assumptions.
6. 'Execute' tests on visual analysis models by tracing execution paths with highlighters to find missing paths or dead ends.
7. Log defects, revise requirements and models, and verify fixes.

**[Variant F]**

Customer and developer teams review draft spec independently.
2. Customer rates each requirement for risk (risk of not getting real needs met).
3. Developers rate each requirement for risk (risk of cost overruns or technical unfeasibility).
4. Conduct joint review meeting to log defects and discuss high-risk requirements.
5. Apply risk mitigation strategies (change requirement style, specify prototypes, isolate risk).
6. Update requirements specification.

## Analyst Questions & Prompts

**[Variant A]**

"Does this requirement conform to our quality standards?", "Are there ambiguous or untestable statements in section X?", "Do all reviewers agree on the correctness of model Y?"

**[Variant B]**

Is this requirement measurable with a fit criterion? Does this assumption contradict domain property X? Are all failure/exception cases specified for this operation?

**[Variant C]**

"Does this requirement satisfy all specified quality criteria?", "Is there any contradiction with existing system constraints?"

**[Variant D]**

Is this requirement ambiguous or open to multiple interpretations? Is it verifiable by a test? Does it conflict with any other requirement or business rule?

**[Variant E]**

"How will we judge whether this requirement is satisfied?", "What test scenario would demonstrate this use case works?", "Is there any ambiguous phrasing that could be interpreted in multiple ways?", "What happens if we execute Test X on Process Flow Y?"

**[Variant F]**

Are you confident you can deliver this at a fixed price? Does this requirement truly reflect your operational need?

## Minimal Realistic Example

**[Variant A]**

A 1-hour formal walkthrough of a Software Requirements Specification (SRS) with a Lead Developer and Tester catches 4 missing edge-case exceptions prior to development.

**[Variant B]**

A 3-person team (SME, Developer, QA) uses a safety checklist to inspect a train control RD, discovering that the exception handling for sensor signal loss was omitted.

**[Variant C]**

A 5-person team (moderator, reader, author, tester, architect) conducts a formal 2-hour session to inspect a 30-page Software Requirements Specification, logging 14 defects.

**[Variant D]**

An inspection team (BA, developer, tester, 2 SMEs) reviews a 50-page SRS at 3 pages/hour, discovering 223 defects including ambiguous terminal timeout rules.

**[Variant E]**

Given-When-Then test AT-1: 'Given I am logged in AND have published articles, When I request to view statistics, Then a graph of view stats from past 30 days is displayed AND a list of statistics is displayed in reverse chronological order.' Tracing a test on a process flow highlights a missing decision box for empty cart handling.

**[Variant F]**

Review flagging a rigid 0.5s max response time requirement as high-risk for developers, resulting in a change to a 95% statistical response time style.

## Quality Criteria & Verification

**[Variant A]**

Defects identified and logged objectively; work product checked against quality characteristics (atomic, unambiguous, testable); sign-off achieved.

**[Variant B]**

Defect detection rate; verification that all logged inspection report defects are resolved in the consolidated RD.

**[Variant C]**

Defect detection rate, strict adherence to roles/process, resolution of all logged defects.

**[Variant D]**

Exit criteria check (all logged issues addressed, changes verified, open items assigned); inspection defect density tracking; peer sign-off.

**[Variant E]**

Reviewers include both users/SMEs and developers/testers; every requirement has associated testable acceptance criteria/fit criteria; all logged defects are resolved.

**[Variant F]**

Checklist sign-off, removal of high-risk items.

## Errors & Anti-Patterns

**[Variant A]**

Turning reviews into personal attacks on the author; conducting walkthroughs without advance reviewer preparation.

**[Variant B]**

Lack of independent reviewers (authors inspecting their own work); reviews degenerating into personal attacks; holding overly long, exhausting meetings (> 2 hours); skimming without checklists.

**[Variant C]**

Combining defect detection with defect correction during the review meeting; author acting as reader/moderator.

**[Variant D]**

Holding the meeting without individual prep work; combining author and reader/moderator roles; attempting to solve problems during the meeting; inviting management to defect-finding sessions.

**[Variant E]**

Treating executive 'sign-off' as a substitute for true validation; reviewing requirements without testers or end-user representatives; delaying test design until after code is written.

**[Variant F]**

Debating solutions during the review meeting instead of logging defects; ignoring developer feasibility concerns.

## When NOT to Use

**[Variant A]**

When work products are in early, highly volatile brainstorming draft stages where formal review adds rigid friction.

**[Variant B]**

Never—inspections apply to all projects; however, formal heavy meetings can be streamlined to lightweight walkthroughs in small agile projects.

**[Variant C]**

When requirements are extremely volatile/early concept stage where lightweight commenting suffices.

**[Variant D]**

For very low-risk, non-critical, or minor routine requirement updates where informal deskchecks suffice.

**[Variant E]**

Always applicable; every requirement set must be validated prior to implementation commitment.

**[Variant F]**

None; mandatory prior to signing delivery contracts.

## Alternatives & Complementary Methods

**[Variant A]**

Alternatives/Complements include Verification checklists, Approval tasks, and Inspection.

**[Variant B]**

Complementary: Automated Database Queries, Animation, Model Checking. Alternative: Informal Walkthroughs.

**[Variant C]**

Walk-Through, Commenting, Perspective-Based Reading

**[Variant D]**

Peer Deskcheck, Walkthrough, Passaround, Acceptance Testing.

**[Variant E]**

Complementary: Practice #10 Analysis, Practice #11 Models, Practice #12 Prototypes. Alternatives: Formal Formal Specifications, Automated BDD frameworks (Cucumber).

**[Variant F]**

Prototype Testing, Walkthroughs, Checklists.

## Supported Decisions

**[Variant A]**

Requirement baseline sign-off, deliverable verification, quality gate approval.

**[Variant B]**

RD baseline approval, release sign-off, software readiness for development.

**[Variant C]**

Baseline approval, readiness for architectural design and implementation.

**[Variant D]**

Quality baseline, release readiness, acceptance.

**[Variant E]**

Requirement baseline sign-off, iteration readiness, definition of done/ready, software acceptance.

**[Variant F]**

Contract sign-off, risk mitigation strategy, requirement style selection.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can pre-screen requirement docs against verification quality checklists (checking for ambiguous terms, passive voice, missing test criteria) before human peer review.

**[Variant B]**

LLM review agents can perform automated preliminary checklist inspections, highlighting potential ambiguities, passive voice, or missing exception clauses prior to human review meetings.

**[Variant C]**

Automated LLM inspectors perform pre-checks for ambiguity and rule violations before human inspection meetings.

**[Variant D]**

Not in source

**[Variant E]**

AI agents can automatically generate Given-When-Then acceptance tests from draft use cases, run dry-run test execution paths on Mermaid process models, and perform automated defect checking against requirements review checklists.

**[Variant F]**

Scan requirements specifications against quality checklists to flag ambiguities, missing sections, and high-risk phrasing automatically.
