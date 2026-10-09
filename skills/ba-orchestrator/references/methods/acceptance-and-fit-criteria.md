---
id: acceptance-and-fit-criteria
name: "Acceptance and Fit Criteria"
task: T5
task_name: "Requirements Specification"
subtask: "5.7"
subtask_name: "Specification by Example and Acceptance Criteria"
source_count: 4
---

# Acceptance and Fit Criteria

`T5 Requirements Specification › 5.7 Specification by Example and Acceptance Criteria`

**Also described as:** Acceptance Criteria & QoS Measurement; Acceptance and Evaluation Criteria; Acceptance criteria definition; Fit Criteria & Acceptance Criteria Definition

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Eliminates ambiguity and subjectivity in requirements, making soft, vague, or complex functional/non-functional requirements testable and verifiable.

**[Variant B]**

Defines specific, objective, and measurable criteria for each requirement, bridging the gap between business needs and solution testing.

**[Variant C]**

Defines testable conditions to judge whether a solution is acceptable to stakeholders and provides a framework to compare and rank multiple alternative solutions or designs objectively.

**[Variant D]**

Prevents delivery of unprovable, ambiguous, or unsatisfactory products and services by establishing objective, testable verification metrics up front.

## BA Lifecycle Phase

**[Variant A]**

Specification

**[Variant B]**

Define Requirements / Requirements Development / Testing

**[Variant C]**

analysis / specification / prioritisation / validation / change management

**[Variant D]**

Specification / Validation

## Input Artifacts

**[Variant A]**

Requirement Descriptions, Rationales, User Stories, Business Rules, Quality Standards.

**[Variant B]**

Requirements Catalogue, User Stories, Scenarios, Use Case Descriptions.

**[Variant C]**

Requirements (specified and modelled), design options, business needs, contractual obligations.

**[Variant D]**

Functional requirements, use cases, quality requirements, constraints, service level agreements (SLAs)

## Output Artifacts

**[Variant A]**

Atomic Requirements with Fit Criteria (Volere Snow Cards), User Stories with Given/When/Then Acceptance Criteria, Test Cases.

**[Variant B]**

Measurable Acceptance Criteria / Fit Criteria per requirement (including PLUME usability metrics for non-functional items).

**[Variant C]**

Acceptance criteria (pass/fail statements), evaluation criteria (measurable parameters and scoring matrices), test plans/cases.

**[Variant D]**

Acceptance criteria, postconditions/guarantees, Quality of Service (QoS) metrics, verification matrix (Test, Demo, Inspection, Analysis, Certificate)

## Participants & Roles

**[Variant A]**

Business Analyst, Product Owner, Tester/QA Lead, SME, Developer.

**[Variant B]**

BA, Business Customer/Owner, Developers, Testers.

**[Variant C]**

Sponsor, business owner, SME, end user, BA, developer, tester, compliance/legal.

**[Variant D]**

BA, Tester/QA Lead, Architect, End User, Service Manager, Compliance Lead

## Prerequisites

**[Variant A]**

Draft requirement descriptions or user stories with clear business rationales.

**[Variant B]**

Identification and description of individual requirements.

**[Variant C]**

Agreed value attributes and stakeholder consensus on success measures/constraints.

**[Variant D]**

Draft functional, quality, and service requirements.

## Step-by-Step Procedure

**[Variant A]**

Take a requirement description or story.
2. Analyze its rationale ("So that...") to understand the core justification.
3. Determine the appropriate scale of measurement (time, accuracy, %, compliance standard).
4. Define a precise, unambiguous threshold or condition (Fit Criterion / Acceptance Criterion).
5. Review with testers and stakeholders to ensure objectivity and feasibility.
6. Formulate test cases based on the criteria.

**[Variant B]**

Review requirement description and scenarios.
2. Formulate specific, quantifiable benchmark criteria.
3. Define functional fit criteria (inputs, expected outputs, state changes).
4. Define non-functional criteria (response times, PLUME usability metrics: Productivity, Learnability, User satisfaction, Memorability, Error rates).
5. Validate criteria with customer and tester.

**[Variant C]**

Identify value attributes relevant to stakeholders (cost, usability, performance, etc.).
2. Formulate acceptance criteria as pass/fail conditions for a single solution.
3. Formulate evaluation criteria with continuous/discrete measurement scales for multiple solutions.
4. Design assessment tools, instructions, and scoring metrics.
5. Conduct evaluation or testing (e.g., UAT) against the defined criteria.
6. Record and process results to determine acceptance or rank solutions.

**[Variant D]**

Review each requirement/use case and ask 'How will we test/prove this?'.
2. Define quantitative thresholds or specific postconditions (success and minimal guarantees).
3. For services, define continuous or sampling-based Quality of Service (QoS) metrics (repeatable, objective, representative).
4. Assign an explicit verification method (Test, Demonstration, Inspection, Analysis, Certificate) to each item.
5. Review criteria with QA/test engineers to ensure testability and affordability.

## Analyst Questions & Prompts

**[Variant A]**

"How will we know if the delivered solution successfully satisfies this requirement?", "What is the scale of measurement for this quality attribute?", "What result would be considered a failure?", "Given context, when action, what is the expected then outcome?"

**[Variant B]**

How will we prove this requirement has been met? What specific quantifiable metric defines success? What is the exact response time limit? How will testers verify this?

**[Variant C]**

"What are the minimum conditions under which this solution is acceptable?", "How will we measure whether value attribute X is met?", "Which criteria take precedence when comparing trade-offs between options?"

**[Variant D]**

How will we know this requirement has been met? What specific output confirms success? How can we measure this service quality continuously? What is the pass/fail threshold?

## Minimal Realistic Example

**[Variant A]**

Converting the requirement "The product shall be user friendly" with rationale "To ensure rapid adoption" into the Fit Criterion: "80% of a test panel of casual users shall successfully complete order placement within 3 minutes on their first attempt without training."

**[Variant B]**

Defining acceptance criteria for 'Book a flight': 'System confirms booking by displaying reservation reference code, notes date/time, and response time <=10 seconds for 95% of transactions'.

**[Variant C]**

Evaluating two vendor CRM systems where acceptance requires 99.9% uptime (pass/fail) and evaluation ranks them on usability (1-5 scale) and implementation cost.

**[Variant D]**

For a radio tuning function: Requirement = 'Tune to radio channel within 3 seconds'. Acceptance Criterion = 'Correct audio plays within 3.0 seconds from channel selection, verified by Audio Bench Test'.

## Quality Criteria & Verification

**[Variant A]**

Criteria are binary (pass/fail); quantifiable or objectively verifiable against a clear standard or test; agreed upon by both customer and QA.

**[Variant B]**

Criteria are specific, objective, quantifiable, and testable; agreed by both business customer and testing lead.

**[Variant C]**

Criteria must be atomic, testable (true/false or measurable on a clear scale), unambiguous, and agreed upon by key stakeholders.

**[Variant D]**

Verifiability (100% of requirements have explicit pass/fail acceptance criteria and assigned verification methods), test team walkthroughs.

## Errors & Anti-Patterns

**[Variant A]**

Using unmeasurable adjectives ("fast", "intuitive", "secure", "flexible") without fit criteria; setting unrealistic or uncoordinated tolerance levels.

**[Variant B]**

Writing vague, unmeasurable criteria like 'system must be fast and user-friendly'; defining acceptance criteria after testing has already started.

**[Variant C]**

Defining untestable or vague criteria (e.g., 'system must be fast'); locking in rigid contractual criteria that cannot adapt to change.

**[Variant D]**

Using unmeasurable words ('promptly', 'efficiently'); setting statistical targets that require cost-prohibitive sample sizes; using easily gamed QoS metrics.

## When NOT to Use

**[Variant A]**

None; all valid requirements and stories require fit or acceptance criteria to be testable.

**[Variant B]**

During initial exploratory visioning workshops before specific requirements have been formulated.

**[Variant C]**

When requirements are highly exploratory, stakeholders cannot agree on value metrics, or formal acceptance is unnecessary for low-risk changes.

**[Variant D]**

During initial high-level goal brainstorming before technical feasibility and scope are understood.

## Alternatives & Complementary Methods

**[Variant A]**

Behavior-Driven Development (BDD), Test-Driven Development (TDD), Planguage.

**[Variant B]**

Fit Criteria, Test Cases, PLUME Usability Metrics, Scenarios.

**[Variant C]**

Complemented by Prototyping, Decision Analysis, User Stories (Acceptance Criteria), and Metric/KPI definitions.

**[Variant D]**

Test-Driven Development (TDD/BDD acceptance tests), Fit Criteria, Service Level Agreements (SLAs).

## Supported Decisions

**[Variant A]**

Requirement sign-off, QA test pass/fail determination, product release readiness, vendor compliance validation.

**[Variant B]**

User acceptance test sign-off, requirement completion validation, solution verification.

**[Variant C]**

Acceptance (sign-off) of a delivered solution, selection among vendor/design options, release readiness.

**[Variant D]**

Contractual sign-off, user acceptance, supplier payment authorization, service performance auditing.

## AI & Agentic Adaptation

**[Variant A]**

LLMs can suggest precise Given/When/Then acceptance criteria and test cases from user story descriptions; human testers and BAs review and adjust thresholds for domain realism.

**[Variant B]**

Test-generation AI engines parse acceptance criteria text directly to generate automated Gherkin test scripts (Given-When-Then) automatically.

**[Variant C]**

An AI agent can automatically convert user story statements into testable Gherkin-style acceptance criteria, run automated verification against designs, and prompt human-in-the-loop sign-off for policy compliance.

**[Variant D]**

Agentic test synthesis: AI agents automatically convert functional requirements and acceptance criteria into executable Gherkin/Cucumber test scripts or automated unit/integration tests, flagged for QA engineer verification.
