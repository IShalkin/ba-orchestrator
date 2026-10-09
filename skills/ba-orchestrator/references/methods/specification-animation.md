---
id: specification-animation
name: "Specification Animation"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.2"
subtask_name: "Prototypes, Animation and Usability"
source_count: 2
---

# Specification Animation

`T7 Validation and Acceptance › 7.2 Prototypes, Animation and Usability`

**Also described as:** Requirements Validation by Specification Animation

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces requirements inadequacy, misunderstanding of formal specifications, and unhandled operational edge-cases by visually demonstrating executable models to stakeholders.

**[Variant B]**

Reduces requirement inadequacy and customer expectation mismatches by converting formal specifications into interactive, visual simulations.

## BA Lifecycle Phase

**[Variant A]**

Quality assurance / validation

**[Variant B]**

Quality assurance / validation

## Input Artifacts

**[Variant A]**

Executable formal specification (statecharts, SCR tables, B models, LTS, temporal logic operationalizations), simulation scenarios, domain scene graphics.

**[Variant B]**

Executable formal/semi-formal specification (state machine, Z, SCR, LTL-derived model).

## Output Artifacts

**[Variant A]**

Visual animation execution traces, recorded animation test scenarios, identified adequacy defects, bug reports.

**[Variant B]**

Interactive simulation sessions, animation trace logs, domain scene visualizations, stakeholder validation feedback.

## Participants & Roles

**[Variant A]**

BA, End User, SME, Validation Engineer.

**[Variant B]**

Requirements Engineer / Animator, Domain SME, End Users / Stakeholders.

## Prerequisites

**[Variant A]**

Formal executable model extracted/compiled from specifications; animation tool with UI/domain scene capabilities.

**[Variant B]**

Formal/executable model of the system-to-be; animator tool with visualization interface.

## Step-by-Step Procedure

**[Variant A]**

Extract or compile an executable state machine model from formal specifications.
2. Instantiate model with specific test object instances.
3. Connect animator to visual domain scenes, control panels, or UI widgets.
4. Run simulation by feeding environment stimulus events (manually or via test scripts).
5. Observe dynamic evolution of highlighted states and visual domain scenes.
6. Identify adequacy defects with stakeholders and refine formal specifications.

**[Variant B]**

Extract or generate an executable state machine or transition model from formal specifications.
2. Configure animation parameters and domain-specific visual control panels/scenes.
3. Instantiate test scenarios with representative component instances.
4. Execute the model by submitting simulated environment events via control panels.
5. Observe system reactions visually in real-time domain scenes.
6. Gather stakeholder feedback on whether visual reactions match expectations and record violating trace logs.

## Analyst Questions & Prompts

**[Variant A]**

Does the system behave as you expect when this stimulus occurs? Why did the simulated train move while doors were open? Is this visual response acceptable?

**[Variant B]**

Is this visual behavior what you expect when the emergency button is pressed? Does the train doors visual open at the correct platform position?

## Minimal Realistic Example

**[Variant A]**

Simulating a train control model in FAUST where an analyst clicks 'start' on a panel and visually observes on a 2D track scene that the train moves while doors remain open, exposing a missing guard.

**[Variant B]**

Executing an SCR train specification in an animator: clicking 'Start' on a control panel visually shows the train moving on a graphical track scene while its doors remain closed, validating safety expectations visually.

## Quality Criteria & Verification

**[Variant A]**

Stakeholder validation of visual scene behaviors; complete coverage of key operational scenarios; absence of simulator execution deadlocks.

**[Variant B]**

Stakeholder sign-off on visual scenario replays; runtime property monitor assertions evaluating to True during animation.

## Errors & Anti-Patterns

**[Variant A]**

Animating non-representative test instances; relying on unvalidated simulation models that do not match the underlying formal specification; lack of stakeholder engagement during animation runs.

**[Variant B]**

Animating unrepresentative, trivial scenarios that fail to exercise edge cases; confusing animation success with full mathematical proof.

## When NOT to Use

**[Variant A]**

When no formal executable specification exists, or for purely non-functional static requirements (e.g., development cost).

**[Variant B]**

When no executable formal specification exists, or for purely non-functional static requirements (e.g., development cost limits).

## Alternatives & Complementary Methods

**[Variant A]**

Prototypes, Model Checking, Walkthroughs.

**[Variant B]**

Complementary: Model Checking, Inspections. Alternative: Throwaway Code Prototyping.

## Supported Decisions

**[Variant A]**

Requirements adequacy sign-off, operational workflow confirmation, acceptance test scripting.

**[Variant B]**

Validating behavioral adequacy, user acceptance of control logic, acceptance test data approval.

## AI & Agentic Adaptation

**[Variant A]**

Automated animators can generate edge-case event sequences, feed them into executable models, monitor for visual property violations, and auto-record failing animation traces for BA review.

**[Variant B]**

Agentic animation tools can autonomously generate edge-case event sequences, run batch animations, and highlight visual state assertion violations to stakeholders.
