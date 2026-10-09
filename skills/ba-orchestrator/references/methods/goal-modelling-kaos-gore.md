---
id: goal-modelling-kaos-gore
name: "Goal Modelling (KAOS / GORE)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 5
---

# Goal Modelling (KAOS / GORE)

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Goal Model Elaboration (HOW / WHY Elicitation & Decomposition); Goal Modeling; Goal-Oriented Model Building (KAOS Method); Goal-Oriented Requirements Analysis; Goal-Oriented Requirements Engineering (KAOS / Goal Modeling)

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Provides a constructive, systematic method to build a complete, consistent, pertinent, and traceable multi-view system model combining WHY, WHAT, and WHO dimensions.

**[Variant B]**

Reduces requirements incompleteness, irrelevance, lack of rationale, and stakeholder misalignment by systematically modeling system objectives, alternative refinements, conflicts, risks, and responsibility assignments.

**[Variant C]**

Resolves lack of clarity on project purpose, uncovers hidden conflicts between stakeholder desires, and prevents scope creep.

**[Variant D]**

Address stakeholder conflicts, missing rationale, unexpected obstacles, and misalignment between high-level business goals and software functions.

**[Variant E]**

Reduces scope ambiguity, goal conflicts, and missing functional/non-functional requirements by systematically exploring abstractions and decompositions.

## BA Lifecycle Phase

**[Variant A]**

Discovery / elicitation / analysis / specification / validation

**[Variant B]**

Discovery / elicitation / analysis / specification / prioritisation / validation / change management

**[Variant C]**

Discovery / Analysis / Prioritisation

**[Variant D]**

Discovery / Analysis

**[Variant E]**

analysis

## Input Artifacts

**[Variant A]**

Preliminary documentations, interview transcripts, complaints, problem statements.

**[Variant B]**

Elicited stakeholder wishes, domain background documents, interview transcripts, problem logs, scenarios.

**[Variant C]**

Mission statements, vision documents, stakeholder interview notes, problem statements

**[Variant D]**

Business problem statement, stakeholder requests, high-level vision.

**[Variant E]**

Business goals, problem complaints about system-as-is, strategic objectives, interview transcripts

## Output Artifacts

**[Variant A]**

System Model (Goal model, Obstacle model, Object model, Agent model, Operation model, Behaviour model), generated Requirements Document.

**[Variant B]**

Goal Model (AND/OR diagrams), Obstacle Model, Agent Model, Object Model, Operation Model, consolidated Requirements Document.

**[Variant C]**

Goal diagrams, goal hierarchy tree, i* strategic dependency/rationale diagrams, list of obstacles and threats

**[Variant D]**

Goal model/tree, obstacle and mitigation set, conflict resolution protocol.

**[Variant E]**

Goal Model (AND/OR graph, Goal Diagram) annotated with precise goal specifications, priorities, and assignments

## Participants & Roles

**[Variant A]**

BA, System Architect, SME, Business Owner, Developers, Testers.

**[Variant B]**

Requirements Engineer / BA, System Architect, Stakeholders, SMEs, System Agents.

**[Variant C]**

BA, Sponsor, Product Manager, Business Owner, SME, End User, Compliance/Legal

**[Variant D]**

Business Analyst, Sponsor, Business Owner, Domain SME, Architect.

**[Variant E]**

BA, Business Owner, Sponsor, Architect, SME

## Prerequisites

**[Variant A]**

Access to domain stakeholders and initial problem descriptions.

**[Variant B]**

Identification of problem world boundaries and key stakeholder perspectives.

**[Variant C]**

Identified list of key stakeholders and project mission.

**[Variant D]**

Defined business vision and access to key decision-makers.

**[Variant E]**

Access to strategic business goals, complaints about system-as-is, or preliminary interview transcripts.

## Step-by-Step Procedure

**[Variant A]**

System-as-is: (a) Build preliminary goal model illustrated by scenarios; (b) Derive preliminary object model.
2. System-to-be: (a) Update goal model with new goals and scenarios; (b) Derive updated object model; (c) Analyze obstacles, threats, and conflicts; (d) Analyze responsibilities and build agent model; (e) Make choices among alternative options; (f) Operationalize goals in operation model; (g) Build and analyze behaviour model (sequence and state diagrams); (h) Package model and generate requirements document.

**[Variant B]**

Elicit preliminary goals using keywords, problem analysis, or taxonomies.
2. Build goal refinement trees top-down (asking HOW) and bottom-up (asking WHY) using AND/OR nodes and reusable patterns (Milestone, Case-driven, Guard-introduction).
3. Refine goals until leaf nodes are reached that can be assigned as Requirements to single software agents or Expectations to single environment agents.
4. Identify and resolve goal conflicts (divergence) and obstacles.
5. Derive Object Models (class diagrams), Agent Models, and Operation Models (use cases) directly from leaf goals.
6. Generate the structured Requirements Document from the integrated goal model.

**[Variant C]**

Identify the top-level mission or business goal.
2. Decompose high-level goals into sub-goals (functional or quality) by asking 'How?'.
3. Trace sub-goals upwards to parent goals by asking 'Why?'.
4. Identify goal dependencies, support (+), and conflicts (-).
5. Identify obstacles and threats impeding goals.
6. Reconcile goal conflicts through design trade-offs or stakeholder negotiation.

**[Variant D]**

Identify high-level business goals and refine them into sub-goals (AND/OR decomposition).
2. Assign goals to agents (human or system).
3. Analyze potential obstacles to goal satisfaction.
4. Define mitigations/resolutions for obstacles and stakeholder goal conflicts.

**[Variant E]**

Identify preliminary strategic and domain-specific objectives from documents and transcripts.
2. Ask 'HOW' questions to build refinement paths downwards into sub-goals until goals are assignable to single agents.
3. Ask 'WHY' questions to build abstraction paths upwards toward high-level goals.
4. Ask 'HOW ELSE' questions to uncover alternative refinements (OR-links).
5. Annotate each leaf goal with precise definitions, fit criteria, priority, and assign it to a single system or environment agent.

## Analyst Questions & Prompts

**[Variant A]**

WHY is this goal needed? HOW can this goal be satisfied? WHO is capable of being responsible for this leaf goal? WHAT operations are required to operationalize this goal?

**[Variant B]**

WHY is this requirement needed (what higher goal does it serve)? HOW can this goal be satisfied? What sub-goals are missing for complete refinement? WHO (which agent) is responsible for this leaf goal?

**[Variant C]**

What are you trying to achieve? Why do you want this feature? What does success look like? What could get in the way of achieving this goal?

**[Variant D]**

Why is this goal needed? What obstacles could prevent achieving this outcome? How do we resolve conflict between stakeholder goal A and goal B?

**[Variant E]**

HOW can this goal be satisfied? WHY is this sub-goal needed? HOW ELSE can we achieve this higher-level objective?

## Minimal Realistic Example

**[Variant A]**

Building a complete mine safety control model: refining 'Avoid Miners In Flooded Mine' down to 'PumpOnIfHighWater', deriving object 'Pump', assigning responsibility to 'SafetyController', operationalizing into 'SwitchPumpOn', and generating state diagrams.

**[Variant B]**

Refining 'AchieveBookRequestSatisfied' into AND-subgoals 'AchieveCopyBorrowedIfAvailable' and 'AchieveCopyDueSoonIfUnavailable', assigning the former requirement to the 'LibrarySoftware' agent.

**[Variant C]**

A spacecraft mission has a top-level goal 'Do Worthwhile Space Science'. Sub-goals include 'Carry Many Scientific Instruments' and 'Ensure Long Lifetime', which conflict through mass and power constraints with 'Affordable Launch Price'.

**[Variant D]**

Goal: Reduce manual triage. Obstacle: Unsupported automatic decisions due to low AI confidence. Mitigation: Route low confidence cases to manual review queue.

**[Variant E]**

Asking WHY 'Train stops at block signal' yields high-level safety goal 'Avoid collisions'; asking HOW yields sub-goals 'Driver reacts to stop signal' and 'Brake system functions'.

## Quality Criteria & Verification

**[Variant A]**

Completeness of goal refinements; realizability of leaf goals by assigned agents; correctness of operation operationalizations; structural consistency across all views via meta-model rules.

**[Variant B]**

Refinement completeness proof ({Subgoals, Dom} | = ParentGoal); 100% requirement pertinence; boundary completeness; formal verification.

**[Variant C]**

Goals must be agreed upon by stakeholders, verifiable when refined into requirements, and free of unhandled conflicts.

**[Variant D]**

Goal tree is complete; all leaf goals are assigned to agents; all identified obstacles have explicit mitigations.

**[Variant E]**

Goal refinements must be complete, minimal, and consistent with valid domain properties. Leaf goals must be assignable to single agents.

## Errors & Anti-Patterns

**[Variant A]**

Confusing goals with operations; mixing case analysis with alternative options; building object models with non-structural dynamic links; omitting environment expectations.

**[Variant B]**

Confusing goals (declarative intents) with operations (single-state transition actions); confusing case-driven AND-refinements with alternative OR-refinements; creating unassignable multi-agent leaf goals.

**[Variant C]**

Mistaking premature design solutions for goals; ignoring negative goals/threats; failing to resolve goal conflicts prior to specification.

**[Variant D]**

Focusing solely on functional features without understanding goals/rationale; ignoring stakeholder goal conflicts.

**[Variant E]**

Confusing functional services/operations with intentional goals; stopping refinement before single-agent assignability is reached.

## When NOT to Use

**[Variant A]**

For extremely small, low-risk, short-lived scripts or minor bug fixes where comprehensive multi-view modeling overhead is unjustified.

**[Variant B]**

Never—goal orientation applies universally across system engineering; however, formal temporal logic annotations can be skipped for non-critical, simple applications.

**[Variant C]**

When the project scope, technical solution, and requirements are fully known, standardized, and routine.

**[Variant D]**

Small projects with trivial changes, well-known domain context, and no stakeholder disagreement.

**[Variant E]**

When system scope and technical requirements are completely fixed and deterministic with no alternative execution options or agent choices.

## Alternatives & Complementary Methods

**[Variant A]**

Use-case-driven analysis, Structured Analysis (SA), Tropos, NFR Framework.

**[Variant B]**

Complementary: UML Diagrams, Scenarios, Use Cases, Risk Analysis. Alternative: Flat unstructured requirements lists.

**[Variant C]**

Problem Pyramid, Soft Systems Methodology, Rationale Modeling, Trade-Off Analysis (Optioneering).

**[Variant D]**

Problem/Opportunity Statement, Context Diagrams, Use Case Modeling.

**[Variant E]**

Use Case Modeling, Problem Frames, User Story Mapping

## Supported Decisions

**[Variant A]**

System scope, automation boundary, architecture selection, risk countermeasure selection, release sign-off.

**[Variant B]**

Defining system scope, selecting architectural options, assigning agent responsibilities, resolving conflicts, verifying completeness.

**[Variant C]**

Scope baseline, feature inclusion, design trade-offs, release priority.

**[Variant D]**

Scope determination, architectural direction, risk mitigation strategy.

**[Variant E]**

Scope boundary, system architecture, release scope, responsibility assignments

## AI & Agentic Adaptation

**[Variant A]**

Agentic RE platforms can orchestrate the entire KAOS pipeline: ingesting transcripts to build draft goal models, running automated obstacle/conflict regressors, generating UML class/sequence diagrams, and auto-formatting IEEE-830 compliant specifications.

**[Variant B]**

Agentic RE frameworks can parse multi-stakeholder text to auto-generate KAOS AND/OR goal graphs, invoke SAT solvers to check refinement completeness, and auto-translate goals into executable B/Z specs.

**[Variant C]**

LLM agents extract goals and implicit conflicts from stakeholder transcripts and documentation, building automated Goal/Obstacle graphs. Human-in-the-loop review resolves trade-offs and negotiates conflicting objectives.

**[Variant D]**

Analyzes risks of agentic autonomy failures, defining guardrails and fallback mechanisms as explicit obstacle mitigations.

**[Variant E]**

AI agents can analyze transcript inputs to formulate candidate WHY/HOW trees and present alternative goal branches to analysts.
