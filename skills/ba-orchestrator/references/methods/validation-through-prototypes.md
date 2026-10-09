---
id: validation-through-prototypes
name: "Validation through Prototypes"
task: T7
task_name: "Validation and Acceptance"
subtask: "7.2"
subtask_name: "Prototypes, Animation and Usability"
source_count: 3
---

# Validation through Prototypes

`T7 Validation and Acceptance › 7.2 Prototypes, Animation and Usability`

**Also described as:** Creating and Evaluating Prototypes; Software Prototyping

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Exposes gaps, misunderstandings, and UI/UX issues by allowing stakeholders to directly experience and test interactive software mocks.

**[Variant B]**

Reduces 'IKIWISI' ('I'll know it when I see it') ambiguity, closes expectation gaps, and validates user interaction workflows prior to full construction.

**[Variant C]**

Confronts 'I'll Know It When I See It' (IKIWISI), resolves user interface/workflow uncertainty, and validates technical feasibility early.

## BA Lifecycle Phase

**[Variant A]**

Validation / Elicitation

**[Variant B]**

validation

**[Variant C]**

Analysis / Validation / Design

## Input Artifacts

**[Variant A]**

Selected critical requirements, prototype software/wireframes, user manual, scenario scripts

**[Variant B]**

Use cases, user stories, dialog maps, preliminary screen sketches

**[Variant C]**

Initial user requirements, use cases, wireframe concepts, technology stack proposals.

## Output Artifacts

**[Variant A]**

Auditor protocols, observation logs, consolidated change requests

**[Variant B]**

Paper Prototype / Storyboard, Wireframe, Electronic Throwaway Mock-up, or Evolutionary Prototype / Proof of Concept (Spike)

**[Variant C]**

Prototypes (Paper Sketches, Wireframes, Navigable Wireframes, Model Simulations, Executable Prototypes), Prototype Evaluation Scripts, Evaluation Feedback Logs.

## Participants & Roles

**[Variant A]**

Auditor/User, Observer/Requirements Engineer, Prototype Developer

**[Variant B]**

BA, UI/UX Designer, End Users/Product Champions, Developers

**[Variant C]**

Business Analyst, User Experience (UX) Designer, Developers, Target User Representatives (Evaluators).

## Prerequisites

**[Variant A]**

Implemented prototype (throw-away or evolutionary); prepared validation scenarios and checklists.

**[Variant B]**

Identified high-risk or uncertain requirement areas needing visual/interaction clarification.

**[Variant C]**

Uncertain user interface expectations, complex new workflows, or unproven technical approaches.

## Step-by-Step Procedure

**[Variant A]**

Select high-risk or critical requirements for prototyping.
2. Develop a throw-away or evolutionary prototype.
3. Prepare user instructions, test scenarios, and evaluation checklists.
4. Auditor independently executes scenarios on the prototype.
5. Observer documents user hesitation, errors, and feedback into an observation protocol.
6. Analyze results and formulate necessary requirement change requests.

**[Variant B]**

Explicitly define prototype scope (mock-up vs. proof-of-concept) and future use (throwaway vs. evolutionary).
2. Create low-fidelity paper sketches or electronic wireframes based on use cases.
3. Develop structured evaluation scripts detailing specific user tasks and diagnostic questions.
4. Conduct evaluation sessions: observe user interactions, note confusion points, and record feedback.
5. Refine textual requirements and dialog models based on prototype findings.
6. Either discard the throwaway prototype or iterate the evolutionary prototype into production code.

**[Variant C]**

Define explicit prototyping objectives and hypotheses to test (interaction design vs. technical feasibility).
2. Select the appropriate prototype fidelity class (e.g., low-fidelity paper sketch, mid-fidelity wireframe, or high-fidelity executable).
3. Construct the simplest possible prototype needed to answer the target questions.
4. Prepare task-based evaluation scripts with embedded diagnostic questions.
5. Observe target users executing tasks with the prototype without coaching them.
6. Capture usability feedback, missing requirements, exception flows, and false assumptions.
7. Decide the prototype's fate: discard throwaway prototypes or commit to planned evolutionary prototyping using production-quality code.

## Analyst Questions & Prompts

**[Variant A]**

"Does this screen layout match your expected workflow?", "What unexpected behavior did you observe during this step?"

**[Variant B]**

Does this prototype implement the task in the way you expected? What functionality is missing? Were you ever unsure of what action to take next?

**[Variant C]**

"Does this layout allow you to complete your task efficiently?", "What would you expect to happen if you clicked here?", "Is any information missing from this screen?", "How natural did this task flow feel?"

## Minimal Realistic Example

**[Variant A]**

An end user attempts to input a destination into a GUI prototype; the observer notes hesitation because the 'Confirm' button is placed non-intuitively.

**[Variant B]**

A paper mock-up of the 'Request a Chemical' workspace evaluated by chemists using a scenario script, revealing a missing requirement to confirm entire order cancellations.

**[Variant C]**

For Speak-Out.biz, a BA creates mid-fidelity mobile wireframes for the 'View Article Statistics' use case. User evaluation reveals that authors want an overview screen showing overall views before drilling into detailed social media share metrics.

## Quality Criteria & Verification

**[Variant A]**

Successful execution of validation scenarios; subjective user satisfaction; identification of hidden requirements.

**[Variant B]**

Evaluation scripts completed by representative users from multiple user classes; documentation of specific changes made to requirements based on user feedback.

**[Variant C]**

Prototyping objectives are established prior to building; evaluators represent actual user classes; throwaway code is explicitly segregated from production repositories unless written to production standards.

## Errors & Anti-Patterns

**[Variant A]**

Misinterpreting missing functionality as a bug when it was intentionally omitted from the prototype scope.

**[Variant B]**

Pressure to ship throwaway low-quality prototypes as production code; distraction by cosmetic visual details (fonts/colors) during requirements stage; realistic performance expectations inferred from simulated mock-ups.

**[Variant C]**

Distracting users with premature visual cosmetics; over-building prototypes beyond what is needed to answer specific questions; succumbing to pressure to release a fragile, unarchitected executable prototype to production.

## When NOT to Use

**[Variant A]**

When project budget/time constraints prohibit prototype creation or for simple, fully understood requirements.

**[Variant B]**

When requirements are already clear, well-understood, and low risk.

**[Variant C]**

When requirements are well understood, UI patterns are standard/routine, and technical feasibility is proven.

## Alternatives & Complementary Methods

**[Variant A]**

Use Case Specification, Perspective-Based Reading

**[Variant B]**

Dialog Map, UI Storyboard, Display-Action-Response Model, Acceptance Testing.

**[Variant C]**

Complementary: Practice #6 Usage-Centric Elicitation, Practice #11 Models, Practice #18 Validation. Alternatives: Storyboards, UI mockups.

## Supported Decisions

**[Variant A]**

UI acceptance, usability approval, feature scope refinement.

**[Variant B]**

Scope, architecture, acceptance, release.

**[Variant C]**

UI/UX design selection, technical architecture feasibility, build-vs-buy decisions, usability acceptance.

## AI & Agentic Adaptation

**[Variant A]**

AI code generators instantly generate UI wireframes from specifications; AI user agents test interaction flows autonomously.

**[Variant B]**

Not in source

**[Variant C]**

AI agents can generate functional frontend wireframe code (React/HTML) directly from text use cases, execute synthetic user journey simulations to identify navigation friction, and process recorded user session video/transcripts to compile UX feedback logs.
