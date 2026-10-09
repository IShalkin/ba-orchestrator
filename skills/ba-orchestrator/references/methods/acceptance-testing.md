---
id: acceptance-testing
name: "Acceptance Testing"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.4"
subtask_name: "Testing and Acceptance"
source_count: 3
---

# Acceptance Testing

`T7 Validation and Acceptance › 7.4 Testing and Acceptance`

**Also described as:** Acceptance Criteria and Acceptance Testing Definition; Business Acceptance Testing & Change Deployment; Business Analyst-Led Acceptance Testing

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Establishes explicit, objective criteria for when a feature or user story is considered 'done' and fit for business use, preventing scope/quality misunderstandings.

**[Variant B]**

Ensures the delivered solution actually solves the original business problem and satisfies business acceptance criteria rather than just passing technical unit/system specs.

**[Variant C]**

Reduces operational disruption, user rejection, solution defects, and failure to realize planned business benefits.

## BA Lifecycle Phase

**[Variant A]**

validation

**[Variant B]**

Validation / Quality Control

**[Variant C]**

Validation / Change Management

## Input Artifacts

**[Variant A]**

User stories, use cases, business requirements, SLAs, quality attributes

**[Variant B]**

Baselined solution document, vision statement, acceptance criteria, test scenarios/scripts, deployed candidate software.

**[Variant C]**

Validated requirements, acceptance criteria, 'to be' process designs, business case, solution architecture.

## Output Artifacts

**[Variant A]**

Acceptance Criteria Checklist (SMART conditions), Automated/Manual Acceptance Tests, User Acceptance Testing (UAT) Plan

**[Variant B]**

Acceptance test execution logs, defect logs with classification, formal business acceptance sign-off.

**[Variant C]**

Test scenarios/scripts, User acceptance sign-off, Business readiness assessment, Training materials, Benefits Realisation Report.

## Participants & Roles

**[Variant A]**

Product Owner/Customer Representative, BA, Developers, Testers, End Users

**[Variant B]**

Business Analyst (test designer/lead), Process Workers / End Users (testers), Problem Owner, QA Team.

**[Variant C]**

Sponsor, Business Owner, BA, Tester, End User, Change Manager.

## Prerequisites

**[Variant A]**

Defined user stories or use cases aligned with business objectives.

**[Variant B]**

Successful completion of system testing by the technical team and availability of acceptance criteria.

**[Variant C]**

Developed software/solution, defined acceptance criteria, readiness assessment tools (POPIT/CPPOLDAT).

## Step-by-Step Procedure

**[Variant A]**

For each user story/use case, ask: 'How will you judge whether the solution satisfies your need?'
2. Define SMART conditions of satisfaction (functional capabilities, performance bounds, defect thresholds).
3. Translate conditions into implementation-independent acceptance tests using plausible domain test data.
4. Automate execution of acceptance tests where feasible for rapid regression testing.
5. Execute acceptance tests during iterations and perform final User Acceptance Testing (UAT) prior to release.
6. Validate that all acceptance criteria are met before declaring victory.

**[Variant B]**

Step 1: Derive acceptance test scenarios and cases directly from the confirmed acceptance criteria, vision, and use cases.
2. Step 2: Establish the acceptable level of confidence and minimum passing threshold with the problem owner.
3. Step 3: Prepare the test environment and user test data representing real-world business scenarios.
4. Step 4: Guide end users/process workers through test scenario execution (or execute on their behalf as designated).
5. Step 5: Log all unexpected behaviors and evaluate each against requirements to categorize as a software bug, requirement defect, or test script error.
6. Step 6: Present defect impacts to the problem owner to decide fix priorities.
7. Step 7: Obtain formal business acceptance sign-off when all acceptance criteria pass.

**[Variant C]**

Agree testing scope and accept criteria.
2. Define test scenarios, test cases, and decision tables.
3. Support business staff during user acceptance testing (UAT).
4. Conduct business readiness assessment (using POPIT/CPPOLDAT).
5. Plan transition and deployment strategy (e.g., direct, parallel, pilot, phased).
6. Address human responses to change (managing the SARAH curve).
7. Deliver training and documentation.
8. Execute deployment and transition to operational support.
9. Conduct post-implementation and benefits realisation reviews.

## Analyst Questions & Prompts

**[Variant A]**

How would you judge whether the solution meets your needs? What conditions must be met for you to declare this story complete? What nonfunctional metrics must be satisfied?

**[Variant B]**

• How will you know the new system does what you want it to?
• What is the first operational function you are going to try when the system is delivered?
• What do you expect to happen when this end-to-end scenario executes?
• Is this reported discrepancy a defect in code, an error in requirements, or a new feature request?

**[Variant C]**

Does the solution satisfy the acceptance criteria? Is the business ready across People, Process, Organisation, and Technology? How will we support users through the SARAH emotional curve? Have the business benefits been realised?

## Minimal Realistic Example

**[Variant A]**

Acceptance criterion for user story 'Search Vendor Catalog': Keyword search takes < 5 seconds to return results, accurately displays pricing, and handles zero-result searches without crashing.

**[Variant B]**

The BA drafts 10 end-to-end test scenarios based on the A/P acceptance criteria ('Add vendor in <2 hours', '100% correct discount calculation'). The BA leads 3 clerks through testing, catches 2 calculation bugs, logs them for developer resolution, and re-tests until the problem owner signs off.

**[Variant C]**

Assisting customer service staff in executing UAT scripts derived from use case descriptions, evaluating business readiness via CPPOLDAT, and managing a phased rollout of a new CRM system.

## Quality Criteria & Verification

**[Variant A]**

SMART verification of criteria; objective pass/fail execution of tests using realistic test data; product owner sign-off.

**[Variant B]**

All acceptance criteria established at Checkpoint Alpha are 100% validated by passing test scenarios without critical unresolved business defects.

**[Variant C]**

Formal UAT sign-off, successful business readiness evaluation, realization of benefits tracked in the Benefits Realisation Report.

## Errors & Anti-Patterns

**[Variant A]**

Relying on subjective criteria ('must be easy'); treating acceptance tests as unit tests; conducting UAT with implausible or dummy test data; substituting UAT for thorough system testing.

**[Variant B]**

Abandoning end users to test without structured business scenarios; treating user-discovered scope changes as software bugs; testing only happy-path technical functions instead of business process goals.

**[Variant C]**

Treating UAT as a late, rushed phase; neglecting the emotional/human side of change; failing to track post-implementation benefit realization.

## When NOT to Use

**[Variant A]**

None; essential for verifying business readiness on all projects.

**[Variant B]**

For low-level technical unit or integration testing (which belongs strictly to developers/tech QA).

**[Variant C]**

When no business or human processes are changing (e.g., pure backend technical infrastructure upgrades requiring only automated technical testing).

## Alternatives & Complementary Methods

**[Variant A]**

Fit Criteria, Conceptual Testing, Planguage Goals.

**[Variant B]**

User Acceptance Testing (UAT), Exploratory Testing, Beta Testing, Test-Driven Development (TDD).

**[Variant C]**

CPPOLDAT, POPIT, Decision Tables, State Charts, SARAH Curve, Benefits Dependency Network.

## Supported Decisions

**[Variant A]**

Release baseline, acceptance, compliance.

**[Variant B]**

Release to production decision, final product acceptance, defect remediation priority, warranty entry.

**[Variant C]**

Release, acceptance, rollout strategy, benefits sign-off.

## AI & Agentic Adaptation

**[Variant A]**

Not in source

**[Variant B]**

Agentic test generators can convert natural-language use cases and acceptance criteria into automated UAT scripts or gherkin syntax (Given-When-Then), executing regression checks and surfacing business-logic anomalies to the analyst.

**[Variant C]**

AI agents can automatically generate UAT test scenarios directly from user stories and acceptance criteria, as well as predict user adoption risks based on system telemetry.
