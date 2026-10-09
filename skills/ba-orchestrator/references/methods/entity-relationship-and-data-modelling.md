---
id: entity-relationship-and-data-modelling
name: "Entity-Relationship and Data Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 7
---

# Entity-Relationship and Data Modelling

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Assessing Data Concepts and Relationships (Data Modeling & Data Dictionary); Conceptual Modeling with Entity-Relationship (ER) / Class Diagrams; Data Model (Entity/Relationship Diagram); Data Modelling; Entity relationship modelling; Entity-Relationship Diagram (ERD); Entity-Relationship Diagrams (UML Class Diagrams)

This card merges 7 descriptions of the method, labelled Variant A–G in every field.

## Problem Solved

**[Variant A]**

Reduces structural ambiguity, concept duplication, and fuzzy data definitions across domain concepts.

**[Variant B]**

Models the conceptual data structure (entities, attributes, relationships, cardinalities) and business data rules of an organization, reducing database errors and redundant data.

**[Variant C]**

Specifies stored data structure and relationships precisely, reducing ambiguity about business entities and data logic.

**[Variant D]**

Resolves data structure ambiguity and data fragmentation by modeling business entities, their attributes, and their logical relationships.

**[Variant E]**

Reduces structural ambiguity and terminology clashes by defining domain concepts, their attributes, structural relationships, multiplicities, and specialization hierarchies.

**[Variant F]**

Reduces software and system design errors by defining the logical and physical data structures, attributes, and entity relationships required by a domain.

**[Variant G]**

Eliminates data corruption, mismatched interface formats, missing CRUD operations, duplicate data, and non-compliance with data governance or privacy laws.

## BA Lifecycle Phase

**[Variant A]**

Analysis / specification

**[Variant B]**

Define Requirements / Requirements Modelling

**[Variant C]**

analysis

**[Variant D]**

analysis

**[Variant E]**

Analysis / specification

**[Variant F]**

analysis / specification / architecture

**[Variant G]**

Elicitation / Analysis / Specification

## Input Artifacts

**[Variant A]**

Glossary of terms, goal definitions, domain properties, candidate concepts.

**[Variant B]**

Document analysis outputs, domain forms, business rules, requirements specification.

**[Variant C]**

Stakeholder interviews, domain concepts, existing forms/documents, database schemas.

**[Variant D]**

Data stores from DFDs, user requirements, business rules, enterprise data dictionaries

**[Variant E]**

Project glossary, goal specifications, interview transcripts, domain reports.

**[Variant F]**

Elicitation results, Concept Models, Data Dictionary, business rules, legacy database schemas.

**[Variant G]**

Context Diagram, Ecosystem Map, process descriptions, existing database schemas, regulatory policy documents.

## Output Artifacts

**[Variant A]**

Entity-Relationship diagrams, UML Class diagrams (entities, associations, attributes, multiplicities, generalization hierarchies).

**[Variant B]**

Entity Relationship Model / Diagram (Entities, Relationships, Cardinality, Optionality, Link Entities, Subtypes/Supertypes) and Supporting Entity/Attribute Descriptions.

**[Variant C]**

E/R diagram, class diagram, entity definitions.

**[Variant D]**

Entity-Relationship Diagram (using Chen, Martin, or UML Class notation) showing entities, attributes, relationships, and cardinalities.

**[Variant E]**

Entity-Relationship (ER) diagrams, UML Class diagrams, precise concept definitions.

**[Variant F]**

Entity-Relationship Diagrams (ERD) or UML Class Diagrams (Conceptual, Logical, Physical), object diagrams, metadata definitions.

**[Variant G]**

Conceptual Data Model / Entity Relationship Diagram (ERD), Data Flow Diagram (DFD), Data Dictionary (field metadata), CRUD Matrix.

## Participants & Roles

**[Variant A]**

BA, Data Architect, SME.

**[Variant B]**

BA, Data Architect, Database Designer, SMEs.

**[Variant C]**

BA, architect, developer, SME.

**[Variant D]**

BA, Data Architect, Database Designer, Business SMEs

**[Variant E]**

Business Analyst / Data Model Analyst, Domain SME, Database Architect.

**[Variant F]**

BA, Data Architect/Modeller, Developer, SME, Database Admin.

**[Variant G]**

Business Analyst, Data Analyst / Architect, Database Administrator, SME, Compliance/Legal Officers.

## Prerequisites

**[Variant A]**

Domain concepts and their relationships have been elicited or derived from goals.

**[Variant B]**

Identification of key business data items and operational business rules.

**[Variant C]**

Basic understanding of key domain entities and business concepts.

**[Variant D]**

Identified domain nouns and business concepts from elicitation.

**[Variant E]**

Elicited domain entities and terminology from domain understanding.

**[Variant F]**

Understanding of business domain entities, relationships, and attributes.

**[Variant G]**

Initial list of candidate domain terms and high-level business process understanding.

## Step-by-Step Procedure

**[Variant A]**

Identify entities (autonomous passive concepts) and define them.
2. Identify intrinsic attributes for each entity and define value ranges.
3. Identify associations (conceptual links) between entities, assigning role names and multiplicities (min..max).
4. Identify specialization/generalization hierarchies and apply default attribute inheritance.
5. Annotate diagram nodes/edges with precise Def, Has, and DomInvar textual specifications.

**[Variant B]**

Identify candidate Entities (nouns: physical, conceptual, active).
2. Identify Relationships between entities.
3. Determine Cardinality (one-to-one, one-to-many, many-to-many) and Optionality.
4. Resolve many-to-many relationships by inserting Link Entities.
5. Model Recursive or Exclusive relationships and Subtypes/Supertypes.
6. Define Entity attributes and primary keys.

**[Variant C]**

Identify core domain entities (boxes).
2. Define essential fields/attributes for each entity.
3. Identify relationships and connectors between entities.
4. Determine cardinalities (e.g., 1:m, m:m).
5. Normalize the model to remove duplicate data and fixed-size constraints.
6. Review and validate against domain rules and task needs.

**[Variant D]**

Identify domain entities (singular nouns representing physical items, actors, or aggregations).
2. Identify attributes describing each entity.
3. Identify relationships (verbs) connecting entity pairs.
4. Determine relationship cardinality (1:1, 1:M, M:N) and modality (optional vs. mandatory).
5. Represent entities in rectangles, relationships in diamonds (Chen) or connecting lines (Martin/UML), and cardinality with numbers or symbols.
6. Review ERD with business SMEs to ensure business rules and cardinalities are accurate.

**[Variant E]**

Identify key domain concepts (entities/classes) that have distinct identities and attributes.
2. Define intrinsic features (attributes) and value ranges for each entity.
3. Identify conceptual links (relationships/associations) between entities and assign role names.
4. Specify multiplicities (minimum/maximum bounds) for each relationship side.
5. Identify specialization hierarchies (superclasses/subclasses) for concept inheritance.
6. Annotate all entities and relationships with precise natural language definitions.
7. Derive/refine ER diagrams from system goal specifications.

**[Variant F]**

Identify core entities/classes (things about which data is kept).
2. Define attributes for each entity and specify unique primary identifiers.
3. Establish relationships/associations between entities.
4. Define cardinality/multiplicity (minimum and maximum occurrences, e.g., 0, 1, many).
5. Apply normalization rules for logical data models.
6. Validate model completeness with business SMEs and technical developers.

**[Variant G]**

Extract data entities (nouns) from business problem descriptions, use cases, context diagrams, and reports.
2. Model logical relationships between entities and define cardinalities (e.g., 1-to-1, 1-to-many) using Crow's Foot ERD notation.
3. Perform CRUD (or CRUDCLUMT) analysis on each entity to ensure processes exist to Create, Read, Update, and Delete data.
4. Draw Data Flow Diagrams (DFDs) showing how data flows between external entities, processes, and data stores.
5. Build a Data Dictionary detailing field-level attributes (name, data type, length, required status, unique constraint, business rules).
6. Elicit data governance, security (PII), retention, archiving, and privacy requirements.

## Analyst Questions & Prompts

**[Variant A]**

Is this concept an entity, attribute, or association? What is the minimum and maximum multiplicity on this side? What domain invariant constrains these linked objects?

**[Variant B]**

What things do we need to store data about (Entities)? How many B's can relate to one A (Cardinality)? Must an A have a B (Optionality)? What business rule governs this relationship?

**[Variant C]**

How many stays can a guest have? Is a company considered a guest or a separate entity? Can a room be used for multiple stays at once?

**[Variant D]**

What business objects do we need to track? How many instances of Entity B can be associated with one instance of Entity A? Is this relationship mandatory or optional?

**[Variant E]**

Is concept X an entity, an attribute, or a relationship? Can a patron borrow multiple book copies simultaneously? Is this multiplicity a physical domain property or an enforced requirement?

**[Variant F]**

"What data must we store about entity X?", "How many occurrences of entity B can relate to one instance of entity A?", "Is attribute Y dependent solely on the primary key?"

**[Variant G]**

"What data does each component require/produce?", "Which system or process 'owns' each data object as the single source of truth?", "Must an entity A always have at least one entity B?", "What policies apply regarding privacy, security, retention, and archiving?", "How should data type or length mismatches between systems be handled?"

## Minimal Realistic Example

**[Variant A]**

A class diagram showing 'Participant' (with attributes Name, Email) linked via a 'Constraints' association (attributes: excludedDates, preferredDates) to 'Meeting' (attribute: Date).

**[Variant B]**

Modeling a garage data domain: Car entity linked to Service entity via a resolved many-to-many Link Entity 'Car Service', connected to Technician.

**[Variant C]**

Entity 'Guest' with attributes (name, address) connected via 1:m relationship to entity 'Stay' with attributes (stay#, paymethod).

**[Variant D]**

Entity 'Requester' places (1:M) 'Chemical Request', which contains (1:M) 'Chemical Container', which is tracked by (1:1) 'Container History'.

**[Variant E]**

Modeling a 'Participant' entity with attributes Name/Email, linked via an 'Invitation' relationship (multiplicity 0.. ) to a 'Meeting' entity (multiplicity 1.. ).

**[Variant F]**

An ERD models 'Customer' (1) to 'Order' (0..*) relationship, where each Order must have exactly 1 Customer, and an Order contains multiple 'Order Items'.

**[Variant G]**

In a restaurant site, an ERD shows 'Customer Account' places zero or more 'Orders', and each 'Order' contains one or more 'Menu Items'. A Data Dictionary entry DD1 defines 'E-mail Address' as Alphanumeric, Required=Y, Unique=Y.

## Quality Criteria & Verification

**[Variant A]**

Precise Def/Has annotations for every element; accurate multiplicities reflecting domain laws; correct use of inheritance without semantic clashes.

**[Variant B]**

All many-to-many relationships resolved; correct cardinality and optionality reflecting real business data rules; primary keys defined.

**[Variant C]**

Normalization check, CRUD matrix check against user tasks, developer review.

**[Variant D]**

Cross-verification with DFD data stores and Data Dictionary primitives; SME review of cardinalities; ensuring all entities are used by at least one process.

**[Variant E]**

Checking ER diagrams against goal references (concern links); verifying multiplicities against physical domain properties vs prescriptive requirements; SME walkthroughs.

**[Variant F]**

Model accurately reflects business rules; logical model is normalized; entities and relationships are clearly named and documented.

**[Variant G]**

All data stores on DFDs match entities on the ERD; every entity has defined CRUD processes; field-level attributes match across interface boundaries without unhandled truncation.

## Errors & Anti-Patterns

**[Variant A]**

Modeling attributes as pointers to other objects; confusing domain properties with prescriptive requirements in multiplicities; creating non-structural dynamic links.

**[Variant B]**

Leaving unresolved many-to-many relationships in the model; confusing entity instances with entity classes; designing physical database tables prematurely.

**[Variant C]**

Over-modeling non-essential connection objects, mixing dynamic user roles into static sub-classes, failing to normalize variable-length data.

**[Variant D]**

Confusing logical analysis ERDs with physical database design tables; omitting many-to-many relationship resolution; introducing unneeded or unused data elements.

**[Variant E]**

Confusing entities with attributes; failing to distinguish domain properties from prescriptive requirements in multiplicities; modeling implementation data structures prematurely.

**[Variant F]**

Creating overly complex physical models prematurely during business analysis; violating normalization rules leading to data redundancies.

**[Variant G]**

Leaving data definitions entirely to developers without business analysis; failing to define data type/length transformations across integrations; missing data retention and regulatory rules.

## When NOT to Use

**[Variant A]**

For purely procedural/algorithmic problems involving no persistent conceptual data structures.

**[Variant B]**

When analyzing purely procedural workflow timing or non-data UI visual layouts.

**[Variant C]**

Standard off-the-shelf COTS purchasing where standard schema is fixed and unchangeable.

**[Variant D]**

When analyzing purely algorithmic processing logic or UI visual layouts.

**[Variant E]**

When the domain is purely procedural or algorithmic with negligible persistent data or domain concepts.

**[Variant F]**

When analyzing purely procedural workflows with no persistent data requirements.

**[Variant G]**

Rarely skipped; applicable whenever software creates, reads, updates, or deletes persistent information.

## Alternatives & Complementary Methods

**[Variant A]**

Goal-derived Object Modeling, SADT datagrams, Glossaries.

**[Variant B]**

Class Modelling, Data Dictionary, Document Analysis, CRUD Matrix.

**[Variant C]**

Data Dictionary, Virtual Windows, Data Expressions, Class Diagrams.

**[Variant D]**

UML Class Diagram, Data Dictionary, CRUD Matrix.

**[Variant E]**

Complementary: Goal Modeling (concern links), Glossary. Alternative: Dataflow Diagrams (for functional-only view).

**[Variant F]**

Complemented by Concept Modelling, Data Dictionary, Glossary, Class Diagrams, and State Modelling.

**[Variant G]**

Complementary: Practice #3 Define Boundaries, Practice #11 Models (ERD/DFD), Practice #16 Business Rules, Practice #17 Glossary. Alternatives: Class Diagrams, Data Vault modeling.

## Supported Decisions

**[Variant A]**

Data architecture design, database schema definition, domain rule enforcement.

**[Variant B]**

Database architecture specification, data migration design, enterprise data governance, business rule definition.

**[Variant C]**

Database architecture, data schema design, COTS fit-gap analysis.

**[Variant D]**

Architecture, database design, scope.

**[Variant E]**

Data architecture design, domain vocabulary standardization, database schema generation.

**[Variant F]**

Database architecture design, software system specification, application integration.

**[Variant G]**

Database architecture selection, interface integration design, data migration scope, compliance readiness.

## AI & Agentic Adaptation

**[Variant A]**

LLMs can extract entities, attributes, and relationships directly from goal definitions, auto-generate UML class diagrams in PlantUML syntax, and flag multiplicity inconsistencies.

**[Variant B]**

AI data-modeling engines parse business specs and legacy database schemas to generate normalized Entity Relationship Diagrams automatically.

**[Variant C]**

Prompt AI with domain entity descriptions to automatically draft normalized E/R diagrams and detect missing relationships.

**[Variant D]**

Not in source

**[Variant E]**

LLM agents can extract entities, attributes, and relationships from natural language goal specs and automatically produce valid UML Class Diagram code (e.g., PlantUML).

**[Variant F]**

AI agents can convert text requirements or form specs into normalized logical ERDs, generating database DDL scripts while requesting human review of complex relationships.

**[Variant G]**

AI agents can automatically parse requirements text to generate ERDs (in PlantUML/Mermaid), draft Data Dictionaries with inferred data types/lengths, and perform automated CRUD gap analysis across process flows.
