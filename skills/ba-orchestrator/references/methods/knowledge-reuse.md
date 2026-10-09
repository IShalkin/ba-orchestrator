---
id: knowledge-reuse
name: "Knowledge Reuse"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 2
---

# Knowledge Reuse

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces elicitation time, incomplete requirements discovery, and reinventing the wheel by leveraging pre-existing domain structures, taxonomies, and patterns.

**[Variant B]**

Reduces requirements elicitation effort and prevents errors by reusing domain-independent taxonomies, meta-models, or domain-specific abstractions (patterns) from past projects.

## BA Lifecycle Phase

**[Variant A]**

Discovery / elicitation

**[Variant B]**

Discovery / elicitation / specification

## Input Artifacts

**[Variant A]**

Requirements taxonomies, domain-independent meta-models, abstract domain patterns (e.g., resource management), past project specifications.

**[Variant B]**

Requirements taxonomies, meta-models, abstract domain patterns (e.g., Resource Management, Asset Tracking).

## Output Artifacts

**[Variant A]**

Transposed requirements, domain properties, candidate goals, structured system models.

**[Variant B]**

Instantiated, domain-specific requirements, domain properties, and system models.

## Participants & Roles

**[Variant A]**

BA, Domain Architect, SME.

**[Variant B]**

Business Analyst / Requirements Engineer.

## Prerequisites

**[Variant A]**

Availability of reusable catalogues, meta-models, or abstract domain frameworks.

**[Variant B]**

Availability of structured reusable repositories, abstract domain patterns, or standardized taxonomies.

## Step-by-Step Procedure

**[Variant A]**

Retrieve relevant knowledge fragments (taxonomies, meta-models, or abstract domains like 'resource management').
2. Match target problem world concepts with abstract concepts.
3. Transpose abstract knowledge fragments by specialization and domain-specific renaming.
4. Validate transposed specifications with stakeholders.
5. Adapt, complete, and integrate the transposed fragments into the system model.

**[Variant B]**

Identify the abstract domain(s) matching the target system (e.g., specializing 'Resource Management' for a Library System).
2. Retrieve relevant abstract knowledge fragments (concepts, tasks, goals, properties).
3. Transpose abstract fragments to the target domain through specialization, parameter instantiation, and renaming.
4. Validate transposed specifications with stakeholders for local adequacy.
5. Adapt and integrate the transposed fragments into the system model.

## Analyst Questions & Prompts

**[Variant A]**

Is there any requirement of Taxonomy Class X in my system? How does target concept Y specialize abstract concept Z? What non-functional constraints usually apply to this pattern?

**[Variant B]**

Is there a requirement in class X (e.g., Privacy, Availability) relevant to this system? How does this generic resource reservation pattern apply to our library book copy concept?

## Minimal Realistic Example

**[Variant A]**

Transposing the abstract domain 'Resource Management' (resource unit, user, checkout) to the 'Library System' (book copy, patron, borrow) to automatically inherit loan limitation rules.

**[Variant B]**

Specializing the abstract concept 'Resource Unit' to 'Book Copy' and inheriting the abstract domain property 'A resource unit can be used by at most one user at a time' into 'A book copy can be borrowed by at most one patron at a time.'

## Quality Criteria & Verification

**[Variant A]**

Adequacy and accuracy of transposed specifications in the target context; domain expert validation of instantiated rules.

**[Variant B]**

Validation of inherited properties against local domain reality; consistency check of integrated fragments.

## Errors & Anti-Patterns

**[Variant A]**

Forcing inappropriate abstract features onto a mismatched domain; spending excessive effort in tricky adaptations rather than fresh elicitation; lack of tool support for analogical matching.

**[Variant B]**

Forcing inappropriate generic patterns onto a unique domain; spending excessive effort adapting ill-fitting abstractions.

## When NOT to Use

**[Variant A]**

For radical design projects or highly novel domains where no past experience, patterns, or abstractions exist.

**[Variant B]**

In highly novel, radical design projects with no existing conceptual precedents or domain analogies.

## Alternatives & Complementary Methods

**[Variant A]**

Background study, analogical model reuse, domain modeling.

**[Variant B]**

Complementary: Goal Modeling, Problem Frames. Alternative: Greenfield interview-driven elicitation.

## Supported Decisions

**[Variant A]**

Architecture selection, domain rule adoption, comprehensive feature identification.

**[Variant B]**

Selecting system architecture patterns, defining complete non-functional requirement sets.

## AI & Agentic Adaptation

**[Variant A]**

Agentic systems can automatically search pattern libraries using semantic matching to retrieve relevant abstract models and auto-rename variables to fit the target glossary.

**[Variant B]**

RAG-driven AI agents can automatically retrieve matching analysis patterns or IEEE templates from corporate knowledge bases and propose pre-populated requirements specifications.
