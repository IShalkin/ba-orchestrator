---
id: document-and-system-archaeology
name: "Document and System Archaeology"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 3
---

# Document and System Archaeology

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

**Also described as:** Document Archaeology; Reverse Engineering & Archaeology; System Archaeology

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Uncovers hidden, implicit, or forgotten business rules, data attributes, and requirements buried in existing documentation, legacy screens, and paper forms.

**[Variant B]**

Recovers lost or unwritten requirements from legacy systems, competitors' products, old manuals, and problem report databases during 'brown-field' development.

**[Variant C]**

Recovers lost explicit domain/business logic and prevents missing legacy functionalities when building a replacement system.

## BA Lifecycle Phase

**[Variant A]**

Elicitation

**[Variant B]**

Discovery / Analysis

**[Variant C]**

Elicitation / Discovery

## Input Artifacts

**[Variant A]**

Legacy system specifications, user manuals, paper forms, reports, screenshots, support ticket logs, existing policy documents.

**[Variant B]**

Legacy code, system user manuals, fault/defect databases, competitor products, old specification documents

**[Variant C]**

Legacy system source code, legacy documentation, database schemas

## Output Artifacts

**[Variant A]**

Extracted Data Dictionary Entries, Legacy Business Rules, Functional Requirements, Candidate Entities and Attributes.

**[Variant B]**

Extracted business rules, functional requirement lists, bug-fix requirements, competitive feature matrix

**[Variant C]**

Detailed functional requirements, extracted business rules catalog

## Participants & Roles

**[Variant A]**

Business Analyst, SME, Legacy System Maintainer, Compliance/Legal Lead.

**[Variant B]**

BA, Systems Engineer, Maintenance Programmer, SME, Competitor Intelligence Analyst

**[Variant C]**

Requirements Engineer (System Archaeologist)

## Prerequisites

**[Variant A]**

Access to existing system documentation, forms, or legacy artifacts.

**[Variant B]**

Access to legacy systems, codebases, user manuals, defect databases, or competitor samples.

**[Variant C]**

Access to legacy codebases, technical documentation, or executable legacy software.

## Step-by-Step Procedure

**[Variant A]**

Collect samples of all relevant forms, reports, manuals, files, and screens.
2. Inspect documents to extract nouns (potential data entities and attributes).
3. Question each extracted element (Who uses it? Why? Where does it come from?).
4. Identify repeating groups, business rules, and hidden constraints.
5. Cross-check extracted elements against business use cases and data models.
6. Distinguish essential business data/rules from outdated technological fossils.

**[Variant B]**

Analyze legacy documentation ('archaeology') to extract original rationale, business rules, and error codes.
2. Systematically execute legacy software or simulators to map out existing operational capabilities.
3. Mine bug report databases and customer support logs to translate frequent user pain points into new requirements.
4. Analyze competitor products ('benchmarking') by testing user interfaces to identify innovative missing requirements.
5. Validate extracted requirements with current domain experts to weed out obsolete features.

**[Variant C]**

Obtain legacy software artifacts (code, specs, database schemas).
2. Analyze code structure, business rules, and logic paths.
3. Extract implicit functional rules and algorithms.
4. Document extracted behaviors into natural language or model specifications.
5. Validate extracted rules with current domain experts.

## Analyst Questions & Prompts

**[Variant A]**

"What is the business purpose of this field/report column?", "Who uses this document and what decision does it support?", "Which business event creates or updates this information?", "Is this field still needed, or is it a technological fossil?"

**[Variant B]**

What does the legacy system do when this error occurs? Why was this business rule originally implemented? What features do competitors offer that our users request?

**[Variant C]**

"What logic handles this edge condition in the current code?", "Are all legacy calculation formulas accounted for in the new specification?"

## Minimal Realistic Example

**[Variant A]**

Analyzing legacy paper invoice forms and user manuals for a shoe manufacturer, extracting data attributes (material codes, sizes, order dates) and discovering an unrecorded business rule regarding bulk discounts.

**[Variant B]**

A BA mines 500 support tickets from an existing retail system, discovering that users frequently fail to complete returns due to an unstated authorization rule, which is then formally specified as a requirement for the upgrade.

**[Variant C]**

A BA reads through legacy COBOL code of an old navigation server to extract the exact mathematical formulas used for traffic congestion estimation.

## Quality Criteria & Verification

**[Variant A]**

All extracted data elements defined in the data dictionary; essential business rules verified with current SMEs; technological fossils identified and removed.

**[Variant B]**

Verification of extracted logic against legacy execution, SME validation of current business relevance.

**[Variant C]**

100% functional equivalence coverage for critical business logic; elimination of obsolete technical workarounds.

## Errors & Anti-Patterns

**[Variant A]**

Blindly copying outdated legacy forms into the new system without questioning their current validity; mistaking legacy technology constraints for essential requirements.

**[Variant B]**

Assuming legacy documentation is 100% accurate and up-to-date; blindly copying obsolete legacy bugs/limitations into new specifications; illegal/unethical code disassembly.

**[Variant C]**

Extremely laborious; blindly copying outdated technological decisions and suboptimal legacy processes into the new system.

## When NOT to Use

**[Variant A]**

Completely novel greenfield projects in brand-new domains with no prior artifacts.

**[Variant B]**

In pure 'green-field' domains where no legacy systems, analogous products, or competitors exist.

**[Variant C]**

When the new system intentionally radically changes operational paradigms and retains no legacy functionality.

## Alternatives & Complementary Methods

**[Variant A]**

Apprenticing / Job Shadowing, Reverse Engineering, Interface Analysis.

**[Variant B]**

Competitor Benchmarking, Code Refactoring Analysis, Document Analysis, Change Management.

**[Variant C]**

Field Observation, Perspective-Based Reading

## Supported Decisions

**[Variant A]**

Legacy migration scope, data dictionary definitions, business rule baselining.

**[Variant B]**

Legacy replacement scope, product upgrade roadmap, competitive feature parity.

**[Variant C]**

Migration scope, legacy deprecation, detailed algorithm design.

## AI & Agentic Adaptation

**[Variant A]**

OCR and LLM document processing agents can automatically parse thousands of legacy PDFs, forms, and manuals, extracting draft data dictionaries and business rule catalogs for human BA validation.

**[Variant B]**

Agentic code and document archaeology: LLMs scan millions of lines of legacy code, system logs, and outdated PDFs to automatically extract business rules, decision tables, and data dictionaries for human BA review.

**[Variant C]**

LLM code-analysis agents parse legacy source code and automatically output modern natural-language requirements and decision tables.
