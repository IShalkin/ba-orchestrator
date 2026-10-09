---
id: usability-testing
name: "Usability Testing"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.2"
subtask_name: "Prototypes, Animation and Usability"
source_count: 1
---

# Usability Testing

`T7 Validation and Acceptance › 7.2 Prototypes, Animation and Usability`

**Also described as:** Usability Testing (Thinking Aloud & Problem Counts)

## Problem Solved

Identifies real user interface usability problems, task failures, and learnability roadblocks before code is locked in.

## BA Lifecycle Phase

validation

## Input Artifacts

Realistic task scenarios, UI prototypes/mockups, user profile definitions.

## Output Artifacts

Usability problem log (categorized by severity: Task Failure, Critical, Medium, Minor) and task time measurements.

## Participants & Roles

Facilitator, log keeper, test subject (end user), developer.

## Prerequisites

Paper mockup or functional UI prototype and representative end users.

## Step-by-Step Procedure

Prepare realistic, closed test tasks without giving step-by-step instructions.
2. Brief the representative test user on the session rules.
3. Instruct the user to perform tasks while thinking aloud.
4. Facilitate without guiding or helping the user prematurely.
5. Log all observed user hesitation, misunderstandings, and task failures.
6. Classify problem severity and prioritize repair based on cost/benefit.

## Analyst Questions & Prompts

What are you thinking right now? What do you expect will happen if you click that button?

## Minimal Realistic Example

Testing a hotel check-in prototype with 5 users, logging 3 task failures where users failed to locate the 'F10' search key.

## Quality Criteria & Verification

Problem list classification, verification testing on revised prototypes.

## Errors & Anti-Patterns

Conducting system demos instead of tests; using internal developers as test subjects; testing late in the project after code is written.

## When NOT to Use

Evaluating internal back-end algorithmic calculations with no human interface.

## Alternatives & Complementary Methods

Heuristic Evaluation, Keystroke-Level Model, Usability Requirements.

## Supported Decisions

UI design approval, front-end refactoring priorities, release readiness.

## AI & Agentic Adaptation

Analyze video/audio transcripts of usability sessions using AI to automatically extract and classify problem severity logs.
