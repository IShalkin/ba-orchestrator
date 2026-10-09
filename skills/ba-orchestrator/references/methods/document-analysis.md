---
id: document-analysis
name: "Document Analysis"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 3
---

# Document Analysis

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

**Also described as:** Document analysis

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Systematically extracts data requirements, data structures, and business rules from existing forms, screens, and reports, reducing missing data requirements in new IT systems.

**[Variant B]**

Reduces elicitation gap risks and subject matter expert availability bottlenecks by extracting business analysis background information, business rules, and current state specs from existing artifacts.

**[Variant C]**

Lack of understanding of existing regulations and systems

## Uncertainty Reduced

**[Variant C]**

Missing background knowledge about the current state

## BA Lifecycle Phase

**[Variant A]**

Discovery / Elicitation / Analysis

**[Variant B]**

Discovery / elicitation / analysis / validation

**[Variant C]**

Discovery, elicitation, analysis

## Input Artifacts

**[Variant A]**

Existing paper forms, screen layouts, report specifications, user records.

**[Variant B]**

Existing documentation (policies, specs, user manuals, org charts, audit reports, regulations, contracts).

**[Variant C]**

Existing documentation, regulations, contracts, standards

## Output Artifacts

**[Variant A]**

Document Specification forms, Data Dictionary entries, candidate entities/attributes.

**[Variant B]**

Document analysis chart, research notes, current state specs, confirmed elicitation inputs, identified information gaps.

**[Variant C]**

Result: list of rules, extracted requirements, glossary. Artifacts: excerpts, summary tables, glossary

## Participants & Roles

**[Variant A]**

BA (Analyst), SME / Document Owner.

**[Variant B]**

BA, Domain SME (for clarification/validation).

**[Variant C]**

BA, Compliance/Legal, SME

## Prerequisites

**[Variant A]**

Access to sample completed forms, screens, and current system report outputs.

**[Variant B]**

Access to relevant, credible, and current documentation assets.

## Step-by-Step Procedure

**[Variant A]**

Gather sample filled-in documents/screens.
2. Log document metadata (Name, Filing sequence, Storage medium, Retention, Volumes).
3. Identify initial events and usage frequency.
4. Analyze each data item (Name, Description, Format, Value range, Source).
5. Map attributes to candidate data models.

**[Variant B]**

Identify and procure candidate background documentation sources.
2. Evaluate sources for relevance, currency, credibility, and authenticity.
3. Review material systematically and record findings/notes in a document analysis chart.
4. Identify duplicate notes, conflicts between documents, and knowledge gaps.
5. Transform findings into visual models or structured requirements.
6. Validate findings and resolve discrepancies with domain SMEs.

**[Variant C]**

1. Collect documents.
2. Read and highlight key fragments.
3. Synthesise the information.
4. Verify with an expert.

## Analyst Questions & Prompts

**[Variant A]**

Who completes this form? Where does this data item originate? How long is this document stored? What value ranges are valid?

**[Variant B]**

"What current state rules are documented in this manual?", "Is this system documentation still accurate?", "Where are the gaps between documented procedures and actual practices?"

**[Variant C]**

'Which rules in force are described?', 'What constraints are imposed by the regulator?'

## Minimal Realistic Example

**[Variant A]**

A BA analyzes a paper 'Training Record Sheet' (Form TR01), documenting its 7 data items (e.g. Payroll Number, Course Date, Result) to model the new HR database schema.

**[Variant B]**

A BA reviews an outdated system user manual and training guide to extract 30 baseline business rules for a legacy billing system migration.

**[Variant C]**

Analysing a supply contract to identify system constraints

## Quality Criteria & Verification

**[Variant A]**

Complete document specification covering all metadata and data attribute definitions, validated against live filled-in samples.

**[Variant B]**

Findings are validated against current SME practices; source references are cited; conflicts between docs are highlighted and resolved.

**[Variant C]**

Expert check of the completeness of the extracted data

## Errors & Anti-Patterns

**[Variant A]**

Analyzing blank forms instead of completed ones; missing undocumented data items added manually in margins by workers; ignoring retention/security rules.

**[Variant B]**

Assuming outdated documentation represents actual current state without verification; getting mired in information overload without focused objectives.

**[Variant C]**

Outdated documentation that does not reflect reality

## When NOT to Use

**[Variant A]**

When creating a radical greenfield system where legacy data models are obsolete and misleading.

**[Variant B]**

When documentation is completely absent, or when defining entirely novel future state capabilities with no existing baseline.

**[Variant C]**

Documentation is entirely absent or out of date

## Alternatives & Complementary Methods

**[Variant A]**

Entity Relationship Modelling, Class Modelling, Special-Purpose Records.

**[Variant B]**

Complemented by Observation, Interviews, Data Mining, and Process Modelling.

**[Variant C]**

Interviews, observation

## Supported Decisions

**[Variant A]**

Database architecture specification, data migration scope, user access privileges.

**[Variant B]**

Current state baseline definition, migration scope boundaries, gap analysis.

**[Variant C]**

Compliance, scope

## AI & Agentic Adaptation

**[Variant A]**

OCR and document-parsing AI tools automatically scan legacy forms/screens, extracting data fields, data types, and implicit validation rules into data dictionaries.

**[Variant B]**

LLMs excel at document analysis—scanning hundreds of PDF manuals to auto-extract business rules, interface parameters, and term definitions into structured tables in seconds.

**[Variant C]**

Using RAG systems to automatically extract entities from texts
