---
id: data-dictionary
name: "Data Dictionary"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 4
---

# Data Dictionary

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Project Dictionary & Data Modeling

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Reduces data inconsistency and misinterpretation across solutions and stakeholders by standardizing definitions, primitive elements, and composite structures.

**[Variant B]**

Eliminates ambiguity regarding individual data fields, special values, domain business rules, and field lengths.

**[Variant C]**

Eliminates duplicate, conflicting, or inconsistent variable names, lengths, validation rules, and composite structures across development teams.

**[Variant D]**

Prevents severe miscommunication, ambiguity, and software defects caused by synonyms, homonyms, domain jargon, and inconsistent data definitions.

## BA Lifecycle Phase

**[Variant A]**

analysis / specification

**[Variant B]**

specification

**[Variant C]**

specification

**[Variant D]**

Analysis / Specification

## Input Artifacts

**[Variant A]**

Elicitation results, source system data specs, domain terminology, Data Models.

**[Variant B]**

Domain concepts, draft data models, SME interviews, existing user interface screens.

**[Variant C]**

Input/output data flows from DFDs, ERD attributes, report fields, UI form fields

**[Variant D]**

Interview notes, domain documents, regulations, legacy database schemas, interface standards

## Output Artifacts

**[Variant A]**

Data Dictionary / Metadata Repository (defining primitive elements and composite structures).

**[Variant B]**

Structured textual data catalog with entity and attribute descriptions.

**[Variant C]**

Data Dictionary Repository / Catalog (columns: Data Element Name, Description, Composition / Data Type, Length, Allowed Values, Hyperlinks)

**[Variant D]**

Project dictionary (glossary designations, term definitions, acronym lists), Roles & Responsibilities matrix, UML Class Diagrams / ER Diagrams, data element catalog

## Participants & Roles

**[Variant A]**

BA, Data Analyst/Architect, Developer, SME.

**[Variant B]**

BA, SME, developer, tester.

**[Variant C]**

BA, Data Analyst, Developers, Testers

**[Variant D]**

BA, Data Modeller, Architect, SME, Developer

## Prerequisites

**[Variant A]**

Identification of data elements requiring standardization across solutions.

**[Variant B]**

Basic list of entities and fields identified.

**[Variant C]**

Elicited data elements and structures from models and specifications.

**[Variant D]**

Identified domain concepts, user roles, and system interfaces.

## Step-by-Step Procedure

**[Variant A]**

Identify target data elements (primitive and composite).
2. For primitive elements, document Name, Aliases, Description, and allowable Values/Meanings.
3. For composite elements, define structural compositions (sequences, repetitions, optional elements).
4. Validate definitions with domain SMEs and data stewards.
5. Store definitions in a centralized metadata repository or spreadsheet.
6. Maintain the dictionary continuously throughout the solution life cycle.

**[Variant B]**

List entity classes alphabetically or by structural grouping.
2. Define each entity class with synonyms, purpose, and realistic examples.
3. List all attributes for each entity.
4. Specify data type, size, allowable values, and special value handling.
5. Explain non-trivial business logic, origin, and usage for each attribute.

**[Variant C]**

List all domain data elements alphabetically.
2. Classify elements as primitive (indivisible) or composite structures.
3. Define primitives with data type, character length, format, allowed values, and default values.
4. Define composite structures using composition syntax: '+' for AND, '()' for optional, '{}' for repeating groups (with min:max bounds).
5. Embed hyperlinks between composite structure components and their primitive dictionary entries.
6. Maintain the dictionary centrally to serve as an ongoing enterprise asset.

**[Variant D]**

Capture unfamiliar terms, acronyms, and operational roles during elicitation.
2. Identify and resolve synonyms (different words for the same thing) and homonyms (same word with multiple meanings).
3. Create precise definitions (internal relationships) and designations (real-world pointers).
4. Define operational roles and map their functional responsibilities in a matrix.
5. Model business data entities, attributes, and relationships using UML Class or ER diagrams.
6. Express structural business rules directly as data model multiplicity and constraints.
7. Mark up terms in italicized text across specifications to link with the dictionary.

## Analyst Questions & Prompts

**[Variant A]**

"What is the exact definition and format of data element X?", "What are the allowed values for field Y?", "How is composite structure Z constructed from primitive fields?"

**[Variant B]**

Where do these values originate? What is the maximum character length needed? What happens if this field is left blank?

**[Variant C]**

Is this data element primitive or composite? What are its valid value ranges or allowed options? Is this field optional or mandatory?

**[Variant D]**

What exactly do you mean by this term? Are 'Customer' and 'Client' identical here? What attributes compose this data item? Who is authorized to execute this transaction?

## Minimal Realistic Example

**[Variant A]**

Data Dictionary defines 'Customer Name' = First Name (min 2 chars) + Middle Name (optional) + Last Name (min 2 chars).

**[Variant B]**

Class: Guest. Attribute: 'name' (Text, 50 chars), stated by guest, truncated at registration to prevent printout overflow.

**[Variant C]**

'Chemical Request' = Request ID + Requester + Request Date + Charge Number + 1:10{Requested Chemical}.

**[Variant D]**

Resolving 'Equivalence' in a railway safety upgrade by defining 'Physical Equivalence' (identical hardware circuit board) vs. 'Functional Equivalence' (same decision-making logic in software).

## Quality Criteria & Verification

**[Variant A]**

Definitions are complete, clear, consistent across systems, and actively maintained by designated stewards.

**[Variant B]**

Peer review, SME walkthrough, checking completeness against non-trivial questions guide.

**[Variant C]**

Ensuring every element in a composite structure is defined elsewhere in the dictionary; verifying consistency with ERD attributes and DFD stores; peer review by developers.

**[Variant D]**

Absence of unlinked/undefined italicized terms, absence of unresolved homonyms/synonyms, data model walkthroughs with SMEs.

## Errors & Anti-Patterns

**[Variant A]**

Failing to maintain the dictionary over time, leading to obsolete metadata; documenting fields in isolation without considering enterprise reuse.

**[Variant B]**

Writing trivial definitions (e.g., 'guestName is the name of the guest') instead of capturing domain logic.

**[Variant C]**

Mixing data definitions into the project glossary; storing redundant definitions in individual use cases; failing to define precise validation/formatting rules.

**[Variant D]**

Relying on generic corporate glossaries; creating redundant local definitions; allowing implicit unstated data constraints in models without explaining them to business stakeholders.

## When NOT to Use

**[Variant A]**

On small, single-use scripts or throw-away prototypes where formal data stewardship adds unnecessary overhead.

**[Variant B]**

Small, trivial domain where field meanings are completely self-explanatory.

**[Variant C]**

None; essential whenever software processes data.

**[Variant D]**

In brief exploratory spikes or small single-person scripts with no domain complexity.

## Alternatives & Complementary Methods

**[Variant A]**

Complemented by Glossary, Data Modelling, Concept Modelling, and Business Rules Analysis.

**[Variant B]**

Data Model, Data Expressions, Virtual Windows.

**[Variant C]**

Glossary, UML Class Diagram, Database Schema.

**[Variant D]**

Domain Driven Design (Ubiquitous Language), Entity-Relationship Modeling, UML Class Diagrams, CRUD Matrices.

## Supported Decisions

**[Variant A]**

System integration design, data migration scope, compliance/data governance enforcement.

**[Variant B]**

Database schema design, input validation logic, UI field constraints.

**[Variant C]**

Architecture, compliance, acceptance.

**[Variant D]**

Database schema design, user authorization design, software domain class design.

## AI & Agentic Adaptation

**[Variant A]**

Agents can scan database schemas and sample datasets to auto-generate baseline data dictionaries including inferred data types, nullability, and field formats.

**[Variant B]**

Feed AI raw data samples to auto-generate data dictionary entries including inferences on field types, constraints, and descriptions.

**[Variant C]**

Not in source

**[Variant D]**

Agentic glossary extraction: LLM agents scan all project artifacts to detect undefined acronyms, homonyms, and candidate data entities, populating a draft Project Dictionary and flagging naming conflicts for human BA resolution.
