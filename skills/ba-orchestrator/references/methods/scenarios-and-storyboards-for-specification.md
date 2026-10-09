---
id: scenarios-and-storyboards-for-specification
name: "Scenarios and Storyboards for Specification"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 1
---

# Scenarios and Storyboards for Specification

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Scenarios & Storyboards

## Problem Solved

Converts complex, abstract business use case flows into easily understood, visual, or narrative step-by-step stories for stakeholders.

## BA Lifecycle Phase

Specification

## Input Artifacts

Business Use Case summaries, user interviews, process observations.

## Output Artifacts

Normal Case Scenarios, Exception Scenarios, Alternative Scenarios, Storyboards, Misuse/Negative Scenarios.

## Participants & Roles

Business Analyst, SME, End User, UX Designer, Facilitator.

## Prerequisites

Identified Business Use Case and target user roles.

## Step-by-Step Procedure

Identify the BUC, trigger, actors, and preconditions.
2. Draft a 3–10 step narrative/visual (storyboard) sequence for the Normal Case (happy path).
3. Review the Normal Case with stakeholders to reach consensus.
4. Abstract away current technology to reveal the essential scenario.
5. Systematically examine each step to identify Alternatives (wanted business choices).
6. Systematically examine each step to identify Exceptions (unwanted errors/failures) and write recovery steps.
7. Identify Misuse Cases (antagonist abuse/fraud) and specify protective steps.

## Analyst Questions & Prompts

"What is the first step when this event occurs?", "What happens next?", "What could go wrong at this step?", "What choices does the user have here?", "How could a hostile actor abuse this step?"

## Minimal Realistic Example

Writing a 8-step scenario for airport international flight check-in, identifying alternatives (checking in online vs counter) and exceptions (invalid passport, dead phone battery).

## Quality Criteria & Verification

3–10 steps per scenario level; clear trigger and outcome; full coverage of normal path, key alternatives, and critical exceptions; validated by end users.

## Errors & Anti-Patterns

Writing scenario steps with excessive low-level technical detail; chasing rare exceptions before agreeing on the normal path.

## When NOT to Use

Pure mathematical algorithms or background system jobs with no sequential step structure.

## Alternatives & Complementary Methods

BPMN Activity Diagrams, User Story Mapping, Use Case Specifications, Wireframe Walkthroughs.

## Supported Decisions

Workflow approval, exception handling design, user interface structure, test case generation.

## AI & Agentic Adaptation

LLMs can generate comprehensive list of potential exception and misuse scenarios for any given normal path scenario; human analysts validate relevance with domain SMEs.
