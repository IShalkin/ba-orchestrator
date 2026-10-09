---
id: concept-modelling-and-business-concept-mapping
name: "Concept Modelling and Business Concept Mapping"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 2
---

# Concept Modelling and Business Concept Mapping

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Business Concept Mapping; Concept Modelling

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces semantic ambiguity and vocabulary conflicts across stakeholders by organizing core domain terms and their structural connections independently of technical data design.

**[Variant B]**

Reduces semantic uncertainty, misunderstandings, and miscommunication across business departments and IT by establishing a valid, clear, and intuitive understanding of core business concepts, definitions, and relationships.

## BA Lifecycle Phase

**[Variant A]**

elicitation / analysis / specification / validation

**[Variant B]**

Discovery, elicitation, analysis, specification, change management

## Input Artifacts

**[Variant A]**

Glossary terms, domain SME input, regulatory texts, core business concepts.

**[Variant B]**

Tacit knowledge from stakeholders, business models, strategy documents, spreadsheets, charts of accounts, standard database schemas, reports, administrative guidelines, and regulatory/standard vocabularies.

## Output Artifacts

**[Variant A]**

Concept Model diagram/text (noun concepts, verb concepts, categorizations, roles).

**[Variant B]**

High-level, explorative, prototype, and solution-level Concept Maps; Business Vocabulary (written definitions document); Business Rules specification documents.

## Participants & Roles

**[Variant A]**

BA, Domain SME, Business Architect, Compliance/Legal.

**[Variant B]**

Executive Sponsor (e.g., CFO/Director of Sales), Business Project Anchor, Business Specialists/SME, Business Analyst/Synthesist (Facilitator), Scribe, IT Architect/Developer.

## Prerequisites

**[Variant A]**

Initial business glossary and commitment to design-independent semantic precision.

**[Variant B]**

Identification of a project business anchor, availability of knowledgeable domain experts, access to initial reference documents or existing operational spreadsheets, and setup of visual mapping tools (e.g., CmapTools with a data projector).

## Step-by-Step Procedure

**[Variant A]**

Identify core noun concepts (givens of the domain space).
2. Identify verb concepts connecting noun concepts to form basic structural statements.
3. Add categorizations, classifications, and roles to capture rich semantic meaning.
4. Define concepts cleanly without implementation or data-design biases.
5. Render the concept model graphically or textually.
6. Validate the model with business SMEs to ensure exact, unambiguous business language.

**[Variant B]**

Prepare initial draft concept maps from existing business documents and passive sources.
2. Hold a top-down first workshop with business managers to draw an overall high-level scope map (e.g., overlaying concepts on the Business Model Canvas).
3. Conduct explorative workshops with business specialists to map the as-is concepts, terms, and relationships.
4. Conduct ideation workshops to identify holes, resolve contradictions, re-engineer terminology, and sketch prototype solution concept maps.
5. Apply generalization or specialization techniques if stalled by excessive complexity or lack of detail.
6. Conduct implementation workshops to refine final detailed solution designs and documentational concept maps.
7. Review and secure formal approval/sign-off of the concept maps and vocabulary definitions from business stakeholders.

## Analyst Questions & Prompts

**[Variant A]**

"What are the core 'things' in this domain?", "How does noun A relate to noun B in natural business language?", "Is term X identical to term Y or is there a subtle distinction?"

**[Variant B]**

"What are we talking about when we use this term?", "What is the difference between Concept A and Concept B?", "What keeps management awake at night?", "Who does what with which objects?", "How is this calculated?", "What are the rules/exceptions for this relation?", "Is this general term or specific subtype necessary to run the business?"

## Minimal Realistic Example

**[Variant A]**

A concept model defines 'Member', 'Policy', and 'Claim', linking them via verb concepts: 'Member holds Policy', 'Claim is filed against Policy'.

**[Variant B]**

Mapping a kennel business: 'Puppy' (Business Object) --has for sale--> 'Kennel' (Business Object); 'Puppy' --can do--> 'Puppy Trick' (Business Object); 'Puppy' --has--> 'Puppy Name' (Property).

## Quality Criteria & Verification

**[Variant A]**

Model is free of technical database artifacts (foreign keys, physical types), rich in business semantics, and validated by SMEs.

**[Variant B]**

The concept map must be approved and validated by business stakeholders; diagrams must be readable in natural visual sentences (Subject-Predicate-Object propositions); definitions must be unambiguous, clear, and published on corporate platforms (e.g., Intranet).

## Errors & Anti-Patterns

**[Variant A]**

Confusing concept models with physical database ERDs; using overly technical terminology that alienates business stakeholders.

**[Variant B]**

Including live/volatile data or intricate logical condition statements directly inside diagrams (over-complicating maps); treating concept mapping as technical IT data modeling; cramming more than 20 concepts onto a single diagram page; attempting to map processes/workflows inside concept maps.

## When NOT to Use

**[Variant A]**

For simple systems with universally understood, non-complex terminology, or where data design normalization is the immediate goal.

**[Variant B]**

Do not use when specifying low-level software execution logic without established business definitions, or in trivial small-risk projects where domain terminology is already fully standardized and unambiguous.

## Alternatives & Complementary Methods

**[Variant A]**

Alternatives/Complements include Glossary, Data Dictionary, Data Modelling, and Business Rules Analysis.

**[Variant B]**

Complementary/Preceding methods: Business Model Canvas, Brainstorming, Data Profiling. Alternatives/Succeeding methods: UML Class Diagrams, Entity-Relationship (ER) Modeling, Fact Modeling/SBVR, SKOS/OWL Semantic Web Models, Multidimensional (Dimensional) Modeling.

## Supported Decisions

**[Variant A]**

Business terminology standardization, complex decision logic definition, compliance alignment.

**[Variant B]**

Decisions on project scope, business terminology standardization, business process/rule restructuring, data warehouse/BI architecture, master data management (MDM) hierarchy design, and software requirement acceptance.

## AI & Agentic Adaptation

**[Variant A]**

LLM agents can analyze domain documentation to automatically discover noun/verb concept triples and propose candidate concept maps for domain expert validation.

**[Variant B]**

Concept harvesting engines can use Natural Language Processing (NLP), text analytics, and machine learning to scan corporate documents, emails, and code to extract concept-relationship triples (triplets) automatically; Human-In-The-Loop (HITL) review by business analysts is required to filter, refine, and approve auto-generated graph triples to ensure semantic validity before integration.
