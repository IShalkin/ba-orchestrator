---
id: specification-by-example
name: "Specification by Example"
task: T5
task_name: "Requirements Specification"
subtask: "5.7"
subtask_name: "Specification by Example and Acceptance Criteria"
source_count: 3
---

# Specification by Example

`T5 Requirements Specification › 5.7 Specification by Example and Acceptance Criteria`

**Also described as:** Specification by Example (SBE) / Executable Acceptance Examples; Specification by Example (SBE) / Executable Specifications with Gherkin

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Eliminates miscommunication, functional gaps, unnecessary rework, and outdated documentation by establishing precise, testable, and collaboratively defined specifications.

**[Variant B]**

Reduces information asymmetry, misaligned business objectives, requirements ambiguity, domain concept misunderstandings, over-specification, hand-offs, under-documentation, speci-fiction (outdated specs), and test-inability.

**[Variant C]**

Bridging gaps between business, developers, and testers; eliminates ambiguity in business rules by providing testable, living documentation.

## BA Lifecycle Phase

**[Variant A]**

Discovery / elicitation / analysis / specification / prioritisation / validation / change management

**[Variant B]**

Discovery, elicitation, analysis, specification, prioritisation, validation, change management

**[Variant C]**

Specification / Validation

## Input Artifacts

**[Variant A]**

Business goals, stakeholder requests, existing documentation, user stories, use cases, legacy software data, customer feedback/emails

**[Variant B]**

Business goals, stakeholder requests, interviews, existing documentation, user stories, domain models, acceptance criteria, customer feedback, incident/bug reports

**[Variant C]**

Use cases, decision tables, atomic functional requirements.

## Output Artifacts

**[Variant A]**

Scope statement, specifications with examples, executable specifications, living documentation system, acceptance criteria

**[Variant B]**

Executable specifications (.feature files), living documentation, domain glossaries, Given-When-Then scenarios, scenario outlines with examples tables, context maps, user journey notes

**[Variant C]**

Concrete acceptance examples (e.g., Given/When/Then scenarios), living acceptance documentation.

## Participants & Roles

**[Variant A]**

Sponsor, business owner, SME, end user, BA, product manager, architect, developer, tester, compliance/legal

**[Variant B]**

Sponsor, business owner, domain expert/SME, end user/customer, BA/product manager, architect, developer, tester, compliance/legal

**[Variant C]**

Business Analyst, Product Manager/Owner, Developer, Tester.

## Prerequisites

**[Variant A]**

Access to business stakeholders or proxy SMEs, shared agreement on business goals, and willingness to collaborate across disciplines.

**[Variant B]**

High-level business goals/objectives, defined primary actors/personas, collaborative willingness across business and technical roles, access to domain knowledge

**[Variant C]**

Agreed functional requirement or rule scope.

## Step-by-Step Procedure

**[Variant A]**

Derive implementation scope collaboratively from high-level business goals.
2. Engage business stakeholders, BAs, developers, and testers in collaborative specification sessions (e.g., workshops or 'Three Amigos').
3. Illustrate specifications with concrete, realistic examples to clarify edge cases and business logic.
4. Refine raw examples into concise, self-explanatory specifications with examples using domain language.
5. Automate validation of the specifications without modifying the specification text.
6. Run automated executable specifications continuously via continuous integration environments.
7. Evolve executable specifications continuously into a structured, searchable living documentation system.

**[Variant B]**

Understand business goals and derive scope from goals (e.g., using impact mapping or feature injection).
2. Specify collaboratively through workshops or Three Amigos meetings involving business and technical roles.
3. Illustrate requirements with concrete, realistic examples (happy path, counterexamples, exploratory outcomes).
4. Capture conversations using the Given-When-Then template into Gherkin scenarios or scenario outlines.
5. Refine scenarios to remove redundancy, maintain proper abstraction, and focus on outcomes over UI details.
6. Automate scenarios by connecting Gherkin steps to test code via step definitions.
7. Execute and validate tests frequently within continuous integration to keep documentation alive.
8. Evolve living documentation over time with lexical/illustrative definitions, warning/context notes, and glossaries.
9. Organize scenarios into domain-driven structures (Abilities, Business Needs, Bounded Contexts).

**[Variant C]**

Discuss requirements collaboratively using concrete realistic examples.
2. Formulate examples using standard structures (Given-When-Then).
3. Refine examples to expose edge cases and boundary conditions.
4. Link examples to automated test suites to form living documentation.

## Analyst Questions & Prompts

**[Variant A]**

• What business goal are we trying to achieve with this feature?
• How would this proposed feature/requirement be useful to the user?
• Can you provide a concrete example of this rule in action?
• What is an alternative way to check or verify this functionality?
• What happens in edge cases (e.g., zero values, negative amounts, or missing dependencies)?
• Is there anything else that would happen when this action occurs?

**[Variant B]**

Why are we building this? Who are we building this for? What exactly are we going to build? How will we build it? Can you give a concrete example of this rule? What is the prerequisite needed before this happens? Is there a context that, for the same event, produces a different outcome? (Context questioning) Is there another outcome that also matters? (Outcome questioning) What happens on the angry/scary/embarrassing/delinquent/stressful/greedy/forgetful/desolate/indecisive path?

**[Variant C]**

Can you give a specific realistic data example? What is an example where this rule would fail? What is the exact expected result for this input?

## Minimal Realistic Example

**[Variant A]**

A business rule for 'Free Delivery' defined with examples: 'Free delivery is offered to VIP customers purchasing at least 5 books.' Examples Table: | Customer type | Cart contents | Delivery | | VIP | 5 books | Free, Standard | | VIP | 4 books | Standard | | Regular | 10 books | Standard |

**[Variant B]**

Feature: Scheduling Scenario: Creating a meeting Given Mike, a member of our team When Mike chooses 2 p.m. as a start time for his meeting Then he should be able to save his meeting

**[Variant C]**

Given a ready case missing proof of identity, when completeness is evaluated, then the status becomes More information required and proof of identity appears in the missing-category list.

## Quality Criteria & Verification

**[Variant A]**

Quality is verified when all executable specifications pass automatically during continuous validation runs; specifications must be concise, testable, written in ubiquitous domain language, and self-explanatory without needing technical execution details.

**[Variant B]**

Given-When-Then scenarios pass automated test execution (green); scenarios use ubiquitous domain language rather than UI buttons/fields; scenarios focus on single outcomes/user tasks; examples are realistic and representative; peer review/walkthrough in Three Amigos meetings; continuous integration verification.

**[Variant C]**

Examples are concrete, realistic, objective, and can be validated automatically or manually as acceptance tests.

## Errors & Anti-Patterns

**[Variant A]**

• Scripting instead of specifying (writing low-level UI steps like 'click button' rather than business rules).
• Treating test automation code as second-class, unmaintained code.
• Overspecifying examples by attempting to cover every single combinatorial permutation in one document.
• Coupling specifications tightly with software design or UI mechanics.
• Automating existing manual test scripts directly without refining them.

**[Variant B]**

Over-specification (up-front analysis paralysis); hand-offs without delivery team input; under-documentation; speci-fiction (unmaintained, false specifications); UI-focused scenarios; duplicate/redundant scenarios without scenario outlines; using classes of equivalence instead of boundary/Goldilocks examples; writing Gherkin steps that resemble raw SQL/database models; improper use of Backgrounds.

**[Variant C]**

Creating abstract examples without real values, treating examples as complete replacements for core requirement definitions, failing to maintain examples as living docs.

## When NOT to Use

**[Variant A]**

Not recommended when stakeholder access is completely absent with no proxy, on one-off throwaway prototypes, or for purely non-deterministic subjective requirements (such as game playability or visual aesthetics) that cannot be validated programmatically.

**[Variant B]**

Small risk/trivial changes with zero business uncertainty; single-developer exploratory spikes; situations where stakeholders are completely inaccessible and domain knowledge cannot be verified; ultra-low-level unit logic better suited for standard xUnit tests.

**[Variant C]**

Early exploratory research before domain concepts and rules are defined.

## Alternatives & Complementary Methods

**[Variant A]**

Complementary: Test-Driven Development (TDD), Product Backlog Refinement (PBR) workshops, Continuous Integration, User Story Mapping, Effect Mapping, Feature Injection.

**[Variant B]**

Impact Mapping, Feature Injection, User Story Mapping, Domain-Driven Design (DDD), Traditional Acceptance Test-Driven Development (ATDD), Behavior-Driven Development (BDD), Screenplay Pattern, Goldilocks Principle, Pairwise Testing, Five Whys.

**[Variant C]**

Quality-Attribute Scenarios, Decision Tables, Traceability Matrix.

## Supported Decisions

**[Variant A]**

Scope selection, feature prioritization, release readiness/acceptance, architectural refactoring safety, regulatory compliance, release sign-off.

**[Variant B]**

Scope definition, feature release approval, architecture/domain boundary design, release readiness, acceptance criteria sign-off, compliance and auditability.

**[Variant C]**

Acceptance, release readiness.

## AI & Agentic Adaptation

**[Variant A]**

For agentic and automated BA workflows: Inferred: AI agents can serve as automated facilitators to generate initial concrete examples from high-level user stories, cross-examine domain rules for missing boundary cases, generate test fixtures/glue code from business-language specifications, and perform automated checks against living documentation to detect shotgun surgery risks before code commits. Human-in-the-loop guardrails are strictly required for approving business goals, validating domain terminology, and signing off on living documentation boundaries.

**[Variant B]**

For agentic software engineering systems, Gherkin executable specs serve as unambiguous functional contracts and guardrails. LLM/Agent acts as developer/tester implementing step definitions and code to satisfy specs. Input: business goal prompt + structured Gherkin scenario. Human-in-the-loop: Product Owner/BA reviews and approves refined Gherkin specs before AI code generation. Guardrails: automated test runner (e.g., Cucumber) provides deterministic pass/fail execution output to the agent's feedback loop. Audit trail: git-versioned .feature files and test run results.

**[Variant C]**

Serves as validation datasets and prompt evaluation benchmarks (evals) for testing agent compliance.
