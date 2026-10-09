---
id: use-case-relationships-extend-include-generalization
name: "Use Case Relationships (Extend, Include, Generalization)"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 3
---

# Use Case Relationships (Extend, Include, Generalization)

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Extend Relationship Modeling; Include Relationship Modeling; Use Case Generalization Modeling

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Reduces complexity and clutter in base use cases by factoring out optional, conditional, or complex incremental additions.

**[Variant B]**

Reduces redundancy and maintenance effort by encapsulating shared, reusable behavioral sequences across multiple use cases.

**[Variant C]**

Reduces structural duplication when multiple use cases or actors share common goals/behaviors but specialize implementation details.

## BA Lifecycle Phase

**[Variant A]**

Analysis / specification

**[Variant B]**

Analysis / specification

**[Variant C]**

Analysis / specification

## Input Artifacts

**[Variant A]**

Base Use Case Descriptions, Elaborated Use Cases.

**[Variant B]**

Base/Elaborated Use Case Descriptions.

**[Variant C]**

Base Use Case Descriptions, Actor Glossary.

## Output Artifacts

**[Variant A]**

Extending Use Case Descriptions, updated Use Case Diagrams with <> lines.

**[Variant B]**

Included Use Case Descriptions, updated Use Case Diagrams with <> lines.

**[Variant C]**

Parent and Child Use Cases, updated Use Case Diagram with generalization arrows.

## Participants & Roles

**[Variant A]**

BA/System Analyst, Architect.

**[Variant B]**

BA/System Analyst, Architect.

**[Variant C]**

BA/System Analyst, Architect.

## Prerequisites

**[Variant A]**

Base use cases defined; clear distinction between basic flow and optional extension.

**[Variant B]**

Multiple use cases identified containing identical sub-sequences of behavior.

**[Variant C]**

Conceptual similarity between multiple actors or use cases discovered.

## Step-by-Step Procedure

**[Variant A]**

Identify optional/conditional behavior that augments a base use case.
2. Define specific Extension Points in the base use case.
3. Create an Extending Use Case describing the additional flow.
4. Define the Guard Condition (precondition) on the extend relationship.
5. Connect with directed dashed arrow pointing from extending use case to base use case.

**[Variant B]**

Scan flow of events across all use cases to detect duplicated logic.
2. Factor out common sub-sequence into a new abstract Included Use Case.
3. Replace duplicated text in base use cases with an explicit call/reference to the included use case.
4. Draw directed dashed arrow with <> from base use cases pointing to the included use case.

**[Variant C]**

Identify shared structure/goals among specialized use cases (or actors).
2. Create an abstract Parent Use Case containing shared attributes and steps.
3. Create Child Use Cases that inherit parent flows and specify specialized/added steps.
4. Draw solid directed line with open arrowhead from child to parent.
5. Annotate inherited vs. specialized steps in child use case descriptions.

## Analyst Questions & Prompts

**[Variant A]**

Is this behavior optional? Does the base use case make sense and complete its goal without this behavior?

**[Variant B]**

Is this sub-process performed in the exact same way across multiple use cases?

**[Variant C]**

Are these use cases specialized variations of a broader conceptual event?

## Minimal Realistic Example

**[Variant A]**

Base UC 'Evaluate Loan Request' is extended by 'Refer to Loan Committee' at Extension Point 'Step 4' if loan amount exceeds officer approval limit.

**[Variant B]**

'Submit Loan Request' and 'Offer Line of Credit' both <> abstract Use Case 'Perform Credit Check'.

**[Variant C]**

Parent UC 'Submit Loan Request' is generalized by Child UCs 'Submit Consumer Loan Request' and 'Submit Business Loan Request'.

## Quality Criteria & Verification

**[Variant A]**

Check that the base use case remains fully functional when the extension is removed.

**[Variant B]**

Verify that included use cases encapsulate discrete, non-redundant units of behavior and that base use cases correctly depend on their outcome.

**[Variant C]**

Child use cases must inherit all behaviors, extension points, and relationships of the parent while cleanly overriding/adding specialized steps.

## Errors & Anti-Patterns

**[Variant A]**

Using extend for mandatory sequential steps or normal alternative flows that do not return to the insertion point.

**[Variant B]**

Functional decomposition into trivial 1-step use cases (e.g., 'Click Button').

**[Variant C]**

Over-engineering complex inheritance hierarchies that confuse non-technical business stakeholders.

## When NOT to Use

**[Variant A]**

When the added behavior is mandatory for the base goal or is a simple inline exception.

**[Variant B]**

When a behavior sequence is unique to a single use case and not reusable.

**[Variant C]**

When differences between use cases are minor conditional branches rather than distinct specialized structures.

## Alternatives & Complementary Methods

**[Variant A]**

Inline conditional logic, Subordinate Use Cases, Activity Diagrams.

**[Variant B]**

Activity Behavior Descriptions, Shared Subroutines/Services.

**[Variant C]**

Extend relationships, Parameterized Use Cases.

## Supported Decisions

**[Variant A]**

Release packaging, incremental development allocation, architecture design.

**[Variant B]**

Architecture/framework derivation, component reuse, release prioritization.

**[Variant C]**

Object model class hierarchy mapping, domain structuring.

## AI & Agentic Adaptation

**[Variant A]**

Not specified in source.

**[Variant B]**

Not specified in source.

**[Variant C]**

Not specified in source.
