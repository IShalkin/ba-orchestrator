---
id: storyboards-and-scenarios
name: "Storyboards and Scenarios"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.8"
subtask_name: "Prototypes and Scenarios for Elicitation"
source_count: 5
---

# Storyboards and Scenarios

`T2 Situation Investigation and Elicitation › 2.8 Prototypes and Scenarios for Elicitation`

**Also described as:** Scenarios; Storyboarding

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Reduces ambiguity, misunderstandings, and disconnects between abstract textual descriptions and real-world operational interactions across stakeholders.

**[Variant B]**

Reduces miscommunication, tacit knowledge gaps, and abstraction errors by using concrete, narrative examples of interaction sequences to explore problem worlds and define expected system behavior.

**[Variant C]**

Walks through concrete examples of specific situation threads from a user's perspective, uncovering missing requirements, edge cases, and tacit knowledge.

**[Variant D]**

Provides vivid illustration of real-world user situations to sharpen developer intuition and create realistic test cases.

**[Variant E]**

Illustrates navigation routes and screen sequences for user scenarios using low-fidelity visual sketches or index cards, reducing misinterpretation of user interface workflows.

## BA Lifecycle Phase

**[Variant A]**

Elicitation / specification / validation

**[Variant B]**

Elicitation / analysis / validation

**[Variant C]**

Define Requirements / Elicitation / Validation

**[Variant D]**

elicitation

**[Variant E]**

Define Requirements / Elicitation / Specification

## Input Artifacts

**[Variant A]**

Initial problem world descriptions, stakeholder interaction goals, user roles.

**[Variant B]**

Narrative outlines, user goals, UI sketches, mock screenshots, sequence traces.

**[Variant C]**

Process models, user analysis, business events, context diagrams.

**[Variant D]**

User stories, workplace observation logs, critical incident reports.

**[Variant E]**

Scenarios, User analysis, Context definitions, UI layout ideas.

## Output Artifacts

**[Variant A]**

Storyboards (snapshots, sketches), sequence diagrams, event trace diagrams, normal/abnormal interaction scenarios, acceptance test cases.

**[Variant B]**

Storyboards, positive/negative scenarios, normal/abnormal scenarios, UML sequence/event trace diagrams.

**[Variant C]**

Scenario Descriptions (Background/Situation narrative, Script step sequence, Exceptions), Scenario Coverage Model.

**[Variant D]**

Vivid narrative case stories or specific instance test cases.

**[Variant E]**

Storyboard diagram / slide deck showing sequential interface frames, user actions, and system navigation links.

## Participants & Roles

**[Variant A]**

BA, End User, SME, Developer, Tester.

**[Variant B]**

Business Analyst, End User, Domain SME, Developer.

**[Variant C]**

BA, Business Users, SMEs, Testers.

**[Variant D]**

BA, end user, developer, tester.

**[Variant E]**

BA, Solution Designer, UX Designer, Business Users.

## Prerequisites

**[Variant A]**

Key system components and user roles are identified.

**[Variant B]**

Identification of key system actors and high-level usage goals.

**[Variant C]**

Identification of key business events and user tasks.

**[Variant D]**

Basic understanding of user tasks and work environment.

**[Variant E]**

Defined user scenarios and key interface interaction goals.

## Step-by-Step Procedure

**[Variant A]**

Identify the interaction goal and participating components/players.
2. Outline the normal sequence of interaction steps (who does what, how, and why).
3. Identify potential deviations and exceptional situations (abnormal scenarios).
4. Document concrete examples using text, sequence diagrams, or visual storyboards.
5. Review scenarios with stakeholders in passive (explanation) or active (exploration) mode.
6. Extract underlying implicit goals, requirements, and domain properties.

**[Variant B]**

Identify the specific interaction context and participating actors.
2. Walk through a concrete step-by-step sequence of interaction events (normal course).
3. Ask probing questions ('What if...?', 'What could go wrong?') to discover abnormal/exceptional courses.
4. Document positive scenarios (desired behavior) and negative scenarios (unacceptable behavior/counter-examples).
5. Extract underlying implicit goals, requirements, and domain assumptions from the concrete narrative.
6. Generalize scenarios into behavioural models.

**[Variant C]**

Select specific task/event.
2. Define background situation (role, frequency, specific context).
3. Draft step-by-step user script (happy day flow).
4. Identify exception threads at specific steps.
5. Validate script with business users.
6. Build Scenario Coverage Model (user population, environment, frequency) to ensure comprehensive test coverage.

**[Variant D]**

Identify a critical, frequent, or stressful work situation.
2. Write a narrative story detailing a specific user acting in a realistic context.
3. Incorporate realistic details (time, stress, environment, interrupts).
4. Use narrative to derive domain requirements, variants, or test cases.

**[Variant E]**

Input user scenario.
2. Brainstorm UI ideas on whiteboards/Post-its.
3. Select top ideas.
4. Sketch sequential screen frames showing pictures, text, buttons, and navigation arrows.
5. Walk through storyboard frames with business users to validate navigation flow.
6. Convert to digital slides if helpful.

## Analyst Questions & Prompts

**[Variant A]**

Who are the players? What happens to them? How does it happen? Why does this happen? What if such and such an event occurs? What could go wrong?

**[Variant B]**

Who initiates this interaction? What happens next? What if the user submits invalid data? What should happen if the connection fails at step 3?

**[Variant C]**

Can you walk me through a specific example of this task? What happens first? What if the customer doesn't have a loyalty card? What exceptions occur?

**[Variant D]**

Can you tell me a story about a particularly difficult shift you had recently? What happened step-by-step?

**[Variant E]**

What does the user see first? What button do they click next? What screen appears in response? How do they navigate back?

## Minimal Realistic Example

**[Variant A]**

A 6-step interaction scenario showing a meeting initiator submitting a request, the scheduler asking participants for constraints, participants responding, and the scheduler issuing a date notification.

**[Variant B]**

Tracing a meeting scheduling scenario: Initiator requests meeting -> Scheduler requests constraints from invitees -> Invitees reply -> Scheduler calculates optimal date -> Scheduler sends notification.

**[Variant C]**

Writing a scenario for 'Customer buying fuel & shop items using credit card with separate VAT receipt', walking through attendant actions, credit card swipe, and VAT receipt generation exceptions.

**[Variant D]**

Story of receptionist Doug preparing for 50 bus tourists at 7 PM while handling a walk-in family asking for adjoining rooms.

**[Variant E]**

Creating a 6-frame travel agent storyboard: Customer enquiry -> Main booking screen -> Flight details popup -> Location map -> Insurance window -> Final airline ticket generation.

## Quality Criteria & Verification

**[Variant A]**

Coverage of normal and exceptional courses; validation by stakeholders; consistency across scenario granularity levels; explicitly extracting underlying implicit requirements.

**[Variant B]**

Scenario walkthroughs with stakeholders, coverage of abnormal cases, checking scenario consistency against goal models.

**[Variant C]**

Written from user perspective; covers happy day and exceptions; validated against Scenario Coverage Model to ensure sufficient coverage across frequent, critical, and difficult tasks.

**[Variant D]**

Verification as valid test cases during usability or acceptance testing.

**[Variant E]**

Demonstrates clear navigation sequences; validated by business users as accurately reflecting their scenario workflow.

## Errors & Anti-Patterns

**[Variant A]**

Combinatorial explosion due to enumerating every interaction combination; premature commitment to interaction sequencing (overspecification); leaving underlying requirements implicit.

**[Variant B]**

Combinatorial explosion of scenario variations; premature overspecification (prescribing UI or exact ordering prematurely); keeping requirements implicit without abstracting them from scenarios.

**[Variant C]**

Focusing only on 'happy day' paths while ignoring exceptions; writing abstract general descriptions instead of specific concrete examples; neglecting low-frequency critical events.

**[Variant D]**

Treating vivid narrative scenarios as formal requirements specifications.

**[Variant E]**

Getting bogged down in fine graphic design details (fonts, colors) instead of focusing on navigation and functional sequence; designing in isolation without user feedback.

## When NOT to Use

**[Variant A]**

Should never be skipped entirely, but caution is needed to avoid over-relying on scenarios for capturing complete system-wide declarative rules.

**[Variant B]**

As a sole specification method, because scenarios are inherently partial and capture single paths rather than complete system coverage.

**[Variant C]**

When analyzing purely static data structures or high-level strategic corporate goal definitions.

**[Variant D]**

Formal contractual specifications requiring complete coverage.

**[Variant E]**

For non-visual, non-interactive back-end database scripts or batch processing systems.

## Alternatives & Complementary Methods

**[Variant A]**

Use cases, state machines, prototyping, goal modeling.

**[Variant B]**

Complementary: Goal Modeling, Use Cases, State Machine Diagrams, Prototyping.

**[Variant C]**

Use Case Descriptions, Storyboarding, Prototyping, Activity Diagrams.

**[Variant D]**

Task Descriptions, Use Cases, Activity Diagrams.

**[Variant E]**

Wireframes, Prototyping, Scenarios, Activity Diagrams.

## Supported Decisions

**[Variant A]**

User interaction design, exception handling design, acceptance test criteria.

**[Variant B]**

Defining operational workflows, error-handling requirements, interaction boundary determination.

**[Variant C]**

Requirements specification validation, test script design, user acceptance criteria definition, training scenario creation.

**[Variant D]**

Test case generation, developer domain orientation.

**[Variant E]**

UI navigation flow design, prototype scope selection, scenario validation.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can automatically generate sequence diagrams from textual meeting transcripts, hypothesize abnormal exception scenarios, and trace scenario steps to formal goals.

**[Variant B]**

AI agents can generate synthetic edge-case scenarios from user stories, analyze scenario coverage, and auto-translate natural language scenarios into UML sequence diagrams.

**[Variant C]**

Generative AI parses business event maps to auto-generate comprehensive scenario scripts covering edge cases and exception branches for analyst review.

**[Variant D]**

Generate realistic persona-driven narrative stories from structured task descriptions using LLMs.

**[Variant E]**

AI design tools automatically convert text scenario scripts into visual interactive Storyboard slide decks.
