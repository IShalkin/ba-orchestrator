---
id: user-stories
name: "User Stories"
task: T5
task_name: "Requirements Specification"
subtask: "5.1"
subtask_name: "User Stories and Story Mapping"
source_count: 3
---

# User Stories

`T5 Requirements Specification › 5.1 User Stories and Story Mapping`

**Also described as:** User stories

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Captures system requirements as short, simple user-focused sentences supported by conversations and confirmation criteria, reducing bloated, unreadable specification documents.

**[Variant B]**

Reduces heavy documentation overhead and rigid upfront scoping by capturing concise statements of stakeholder value to invite ongoing collaborative exploration.

**[Variant C]**

Bureaucracy of heavy specifications in Agile

## Uncertainty Reduced

**[Variant C]**

Gap between the business need and the developers' understanding

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Elicitation / Analysis / Specification

**[Variant B]**

prioritisation / specification / analysis / planning

**[Variant C]**

Specification, backlog management, elicitation

## Input Artifacts

**[Variant A]**

User analysis, Scenarios, Product Backlog, business goals.

**[Variant B]**

Stakeholder needs, personas, product vision, backlog.

**[Variant C]**

User goals, product backlog, concept

## Output Artifacts

**[Variant A]**

User Story Cards ('As a role, I want feature, So that benefit'), Acceptance Criteria / Confirmations, Story Point estimates.

**[Variant B]**

User Stories ('As a , I need to , so that '), detailed Acceptance Criteria, story maps.

**[Variant C]**

Result: User Story cards with acceptance criteria. Artifacts: product backlog, story cards, acceptance criteria

## Participants & Roles

**[Variant A]**

BA, Business User / Product Owner, Developer, Tester.

**[Variant B]**

Product Owner, BA, Agile Team (Developers, Testers), Customer/User.

**[Variant C]**

Product Owner, BA, Developer, Tester, End User

## Prerequisites

**[Variant A]**

Identification of user roles and required business features.

**[Variant B]**

Understood user personas and product vision.

## Step-by-Step Procedure

**[Variant A]**

Write user story using standard format ('As a... I want to... So that...').
2. Conduct collaborative Conversations between BA, users, developers, and testers to explore detail.
3. Document Confirmations (Acceptance Criteria / business rules).
4. Estimate Story Points (using Planning Poker).
5. Verify story against INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).

**[Variant B]**

Identify user role or persona (Who).
2. Express necessary action, behavior, or feature desired (What).
3. Express business value or benefit received (Why).
4. Format as standard sentence: 'As a , I need to , so that '.
5. Attach testable Acceptance Criteria (e.g., Given/When/Then format).
6. Refine, elaborate, and decompose stories iteratively during team discussions.

**[Variant C]**

1. Phrase the story using the template (As a... I want... So that...).
2. Define the acceptance criteria (INVEST).
3. Prioritise in the backlog.

## Analyst Questions & Prompts

**[Variant A]**

Who needs this feature? What specific feature is needed? What business value or benefit does it deliver? What specific acceptance criteria prove it works?

**[Variant B]**

"Who needs this feature?", "What goal are they trying to accomplish?", "What is the measurable benefit delivered?", "How do we know when this story is complete (acceptance criteria)?"

**[Variant C]**

'What value does this bring to the user?', 'How will we verify that the task is done?'

## Minimal Realistic Example

**[Variant A]**

Writing Story 150: 'As a customer, I want to amend my credit card payment details so that I can continue to purchase items via the website', with rules on card security and order despatch states.

**[Variant B]**

'As a Shopper, I want to save items to a wishlist, so that I can purchase them later.' Acceptance Criteria: Wishlist holds max 50 items; accessible across logins.

**[Variant C]**

'As a registered user, I want to reset my password by email so that I can log in to my account'

## Quality Criteria & Verification

**[Variant A]**

Adheres to INVEST criteria; includes clear confirmation rules/acceptance criteria; estimated in story points; captures a conversation rather than acting as a static specification.

**[Variant B]**

Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable); clear acceptance criteria attached.

**[Variant C]**

Compliance with the INVEST criteria, agreement with the PO

## Errors & Anti-Patterns

**[Variant A]**

Writing bloated technical specifications on cards; omitting the 'So that' business value statement; treating cards as static documentation without holding conversations; missing acceptance criteria.

**[Variant B]**

Treating user stories as rigid specs without team discussion; omitting the 'Why' (statement of value); writing huge monolithic stories ('epics') that cannot fit in an iteration.

**[Variant C]**

Stories that are too large (epics instead of stories), missing acceptance criteria

## When NOT to Use

**[Variant A]**

For complex legal contracts or heavy outsourcing agreements where formal legally binding written specifications are required upfront.

**[Variant B]**

For long-term knowledge retention, or highly regulated contractual specs requiring comprehensive formal documentation upfront.

**[Variant C]**

Rigid regulated systems with a fixed contract (Waterfall)

## Alternatives & Complementary Methods

**[Variant A]**

Use Case Descriptions, Requirements Catalogue, Planning Poker, Product Backlog.

**[Variant B]**

Complemented by Acceptance Criteria, Story Mapping, Personas, Use Cases, and Backlog Management.

**[Variant C]**

Use Cases, SRS documents

## Supported Decisions

**[Variant A]**

Iteration planning, backlog prioritization, development scope allocation, test case design.

**[Variant B]**

Iteration scope selection, feature prioritization, developer work estimation.

**[Variant C]**

Scope, priority, release, acceptance

## AI & Agentic Adaptation

**[Variant A]**

GenAI assistants convert scenario transcripts into INVEST-compliant User Stories complete with candidate acceptance criteria.

**[Variant B]**

AI agents can generate user stories and Gherkin acceptance criteria from high-level feature prompts, estimating relative story point complexity based on historical team velocity.

**[Variant C]**

AI assistant that decomposes epics into User Stories and generates acceptance criteria
