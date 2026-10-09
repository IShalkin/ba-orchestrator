---
id: glossary
name: "Glossary"
task: T5
task_name: "Requirements Specification"
subtask: "5.6"
subtask_name: "Requirements Documents and Phrasing"
source_count: 3
---

# Glossary

`T5 Requirements Specification › 5.6 Requirements Documents and Phrasing`

**Also described as:** Creating a Glossary; Glossary Development

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Reduces semantic ambiguity, misunderstandings, and defects caused by 'kidnapped words' (ordinary words used in a specialized domain sense), acronym confusion, or conflicting terminology among stakeholders.

**[Variant B]**

Reduces miscommunication and terminology conflicts by defining key business terms and acronyms in a single, accessible repository.

**[Variant C]**

Eliminates term ambiguities, conflicting jargon, multi-meaning acronyms, and miscommunication across stakeholders, developers, and vendors.

## BA Lifecycle Phase

**[Variant A]**

Discovery

**[Variant B]**

Discovery / elicitation / specification / architecture

**[Variant C]**

Elicitation / Specification / Management

## Input Artifacts

**[Variant A]**

Domain documents, stakeholder interview transcripts, legacy documentation, regulatory texts.

**[Variant B]**

Elicitation results, domain documentation, regulatory texts, stakeholder conversations.

**[Variant C]**

Elicited notes, data models, domain literature, legacy documentation, vendor contracts.

## Output Artifacts

**[Variant A]**

Glossary (Chapter E.1 of the Environment Book), establishing standardized terminology, definitions, and acronym expansions.

**[Variant B]**

Glossary (alphabetical list of domain terms, definitions, acronyms, and synonyms).

**[Variant C]**

Project Glossary, Enterprise Glossary (reusable terms, acronyms, abbreviations, synonyms, domain definitions).

## Participants & Roles

**[Variant A]**

Business Analyst / Requirements Engineer (Compiler), Subject-Matter Experts (Domain Authorities/Endorsers).

**[Variant B]**

BA, Domain SME, Glossary Owner/Data Steward, All Stakeholders.

**[Variant C]**

Business Analyst, Business SMEs, End Users, Developers, External Vendors, Technical Writers.

## Prerequisites

**[Variant A]**

Initial elicitation discussions or domain documentation containing domain-specific jargon or repurposed terms.

**[Variant B]**

Early initiative agreement to maintain standardized terminology.

**[Variant C]**

Identification of domain-specific vocabulary and ambiguous terms.

## Step-by-Step Procedure

**[Variant A]**

Identify technical terms, acronyms, and everyday words used in a specialized sense during elicitation.
2. Question SMEs persistently to uncover exact meanings of 'obvious' or 'kidnapped' words.
3. Draft concise, unambiguous definitions for each term.
4. For acronyms, include both the official expansion and an explanatory description of the underlying concept.
5. Document entries in Chapter E.1 (Glossary) of the Environment Book.
6. Obtain formal endorsement from qualified SMEs.
7. Hyperlink all occurrences of defined terms across all requirements specifications.

**[Variant B]**

Identify terms unique to the domain, terms with multiple definitions, or acronyms.
2. Draft clear, concise definitions for each term.
3. Resolve definition conflicts among different stakeholder groups.
4. Document standard synonyms and acronym expansions.
5. Publish glossary in a centralized, easily accessible location.
6. Assign an owner for continuous glossary maintenance throughout the lifecycle.

**[Variant C]**

Identify specialized domain jargon, acronyms, abbreviations, stakeholder role names, and terms with multiple meanings during elicitation.
2. Extract candidate terms from data model entity boxes and data dictionary definitions.
3. Resolve conflicting definitions and reconcile synonyms used by different departments.
4. Document precise, agreed-upon definitions for each term in a centralized tabular Glossary.
5. Publish the glossary to a shared, accessible repository (wiki, SRS section, RM tool).
6. Enforce consistent terminology across all project specifications, code comments, and user interfaces.
7. Harvest project terms into an Enterprise Glossary for future organizational reuse.

## Analyst Questions & Prompts

**[Variant A]**

"What exactly do you mean by term X? Is 'vat' the same as 'tank'? Does 'student' mean undergraduate or PhD researcher? What does this acronym stand for and what concept does it represent?"

**[Variant B]**

"What does term X mean in this business context?", "Are there conflicting definitions for word Y across departments?", "What does acronym Z stand for?"

**[Variant C]**

"What is the exact difference between Term A and Term B?", "Do all departments define 'Customer' in the same way?", "What does this acronym stand for in your domain?", "Are these two terms synonyms for the same concept?"

## Minimal Realistic Example

**[Variant A]**

Defining 'PhD Student' in a university system as 'a junior scientific collaborator/employee' rather than a standard student, preventing incorrect system permissions.

**[Variant B]**

Glossary entry: 'Premium' - The periodic payment required to keep an insurance policy active. Synonym: 'Policy Fee'. Not to be confused with 'Premium Service'.

**[Variant C]**

A project glossary defines 'Active Directory (AD) Group', 'CMS' (Customer Management System), 'COGS' (Cost of Goods Sold), and explicitly defines 'No Regrets Work' to prevent an external vendor from misinterpreting it as low-priority work.

## Quality Criteria & Verification

**[Variant A]**

No-Synonym Principle (one concept = one name); full coverage of all domain-specific terms; SME endorsement of definitions.

**[Variant B]**

Definitions are concise, clear, agreed upon by diverse stakeholders, and continuously maintained by a single owner.

**[Variant C]**

Terms are defined unambiguously; synonyms are listed but a single canonical term is chosen for documentation; glossary is accessible to all team members.

## Errors & Anti-Patterns

**[Variant A]**

Defining acronyms by expansion alone without concept explanation; using synonyms interchangeably in requirements texts; assuming ordinary meanings for 'kidnapped' domain terms.

**[Variant B]**

Failing to maintain the glossary so it becomes obsolete; allowing multiple uncoordinated glossaries to exist across business units.

**[Variant C]**

Varying terms creatively in specifications to avoid repetition; assuming everyone shares the same definition for common words; creating project glossaries that are inaccessible or never updated.

## When NOT to Use

**[Variant A]**

Never omit; a glossary is mandatory for all non-trivial domains.

**[Variant B]**

Rarely inappropriate, though minimal effort is needed if an industry-standard ontology is already universally adopted without variation.

**[Variant C]**

Always applicable; every domain has specialized vocabulary or potential term ambiguities.

## Alternatives & Complementary Methods

**[Variant A]**

Data Dictionary, Domain Model, Conceptual Class Diagram.

**[Variant B]**

Complemented by Data Dictionary, Concept Modelling, and Business Rules Analysis.

**[Variant C]**

Complementary: Practice #8 Data Dictionary, Practice #14 Consistent Writing, Practice #15 Organization. Alternatives: Domain Ontologies, Taxonomy catalogs.

## Supported Decisions

**[Variant A]**

Data modeling, API field naming, user interface terminology, domain-specific logic specifications.

**[Variant B]**

Domain vocabulary alignment, requirements validation, stakeholder communication.

**[Variant C]**

Domain modeling, database naming conventions, contract agreement alignment.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can scan requirements text to identify undefined acronyms or inconsistent synonym usage, automatically proposing glossary entries grounded in domain corpora.

**[Variant B]**

AI agents can continuously monitor project chats and spec docs, auto-detecting undefined jargon or ambiguous terms and drafting glossary entries for SME confirmation.

**[Variant C]**

AI agents can continuously scan project documentation and chat channels to detect undefined acronyms, highlight inconsistent term usages, auto-draft candidate glossary entries from context, and flag semantic mismatches across sub-teams.
