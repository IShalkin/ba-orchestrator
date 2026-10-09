---
id: requirement-writing-patterns
name: "Requirement Writing Patterns"
task: T5
task_name: "Requirements Specification"
subtask: "5.6"
subtask_name: "Requirements Documents and Phrasing"
source_count: 2
---

# Requirement Writing Patterns

`T5 Requirements Specification › 5.6 Requirements Documents and Phrasing`

**Also described as:** Requirement Patterns; Writing Requirements in Consistent Ways (Patterns & Planguage)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Eliminates ambiguity, misinterpretation, inconsistent granularity, unquantifiable targets, and confusion across diverse team audiences.

**[Variant B]**

Guides analysts in writing complete, precise, and well-structured requirements for common technical or functional topics without starting from a blank page.

## BA Lifecycle Phase

**[Variant A]**

Specification

**[Variant B]**

specification

## Input Artifacts

**[Variant A]**

Elicited requirements knowledge, use cases, quality expectations, business rules.

**[Variant B]**

Elicited domain information, system concepts

## Output Artifacts

**[Variant A]**

Structured Requirement Statements (shall-statements, User Stories, Given-When-Then criteria, Planguage specifications), Requirement Attributes metadata.

**[Variant B]**

Pattern-Based Requirement Specifications (incorporating Guidance, Content, Fill-in Template, Examples, Extra Requirements, and Development/Testing Considerations)

## Participants & Roles

**[Variant A]**

Business Analyst (author), Developers, Testers, Reviewers.

**[Variant B]**

BA (author), Developers, Testers

## Prerequisites

**[Variant A]**

Understood functional and nonfunctional needs requiring specification.

**[Variant B]**

Availability of an established catalog of requirement patterns.

## Step-by-Step Procedure

**[Variant A]**

Select standard writing patterns for functional requirements (e.g., 'The  shall be able to ' or 'When  the system shall ').
2. Consistently use a single keyword (e.g., 'shall') for mandatory requirements rather than mixing synonyms.
3. Write short, active-voice, declarative sentences with unique persistent identifiers.
4. Standardize User Stories using 'As a , I want to  so that '.
5. Specify quality attributes precisely using Planguage keywords (Tag, Ambition, Scale, Meter, Goal, Stretch, Wish).
6. Attach minimal required attributes (ID, Author, Origin, Rationale, Priority, Status, Acceptance Criteria) to each requirement.

**[Variant B]**

Identify the type of requirement to be written (e.g., report, user access, installability).
2. Select the corresponding requirement pattern from the catalog.
3. Review pattern guidance to understand considerations and context.
4. Populate the fill-in-the-blanks requirement template with specific project parameters.
5. Add optional extra requirements specified by the pattern to cover exceptions and details.
6. Review development and testing considerations provided by the pattern to verify completeness.

## Analyst Questions & Prompts

**[Variant A]**

"Who is the specific user class performing this action?", "How can this requirement be tested or verified?", "What is the exact quantitative goal for this quality attribute?", "What is the rationale behind including this requirement?"

**[Variant B]**

What template placeholders need to be populated for this requirement type? What extra exception requirements does this pattern recommend?

## Minimal Realistic Example

**[Variant A]**

Functional requirement: 'Security.Admin.1. The homeowner shall be able to change the security system's passcode.' Nonfunctional (Planguage): 'Tag: Availability.Downtime; Scale: Minutes offline/month; Meter: System clock; Goal: <= 60 mins/week.'

**[Variant B]**

Applying a 'Report Requirement Pattern' to populate parameterized templates for report content, sort order, totals, zero-data behavior, and export formats.

## Quality Criteria & Verification

**[Variant A]**

Requirement statements are concise, unambiguous, active-voice, uniquely tagged, and verifiable; consistent verb selection ('shall') is maintained throughout.

**[Variant B]**

Verification that all placeholders in the pattern template are filled; review against pattern testing considerations.

## Errors & Anti-Patterns

**[Variant A]**

Mixing shall/should/might arbitrarily; combining multiple requirements into long narrative paragraphs using 'and/or'; writing vague non-testable goals ('system shall be user-friendly').

**[Variant B]**

Ignoring pattern guidance and omitting critical exception considerations; forcing non-matching requirements into an ill-fitting pattern.

## When NOT to Use

**[Variant A]**

When non-textual representations (visual models, prototypes, decision tables) convey the specific rule or design more clearly and efficiently.

**[Variant B]**

For highly novel, unique business capabilities that do not match any standard recurring requirement pattern.

## Alternatives & Complementary Methods

**[Variant A]**

Complementary: Practice #9 Quality Attributes, Practice #15 Organization, Practice #18 Review & Test. Alternatives: Executable specifications (BDD).

**[Variant B]**

EARS Syntax, Reusable Requirements Repository, Planguage.

## Supported Decisions

**[Variant A]**

Contractual specification clarity, developer implementation scope, test plan design.

**[Variant B]**

Acceptance, architecture, compliance.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can parse natural language drafts and automatically rewrite them into standardized 'shall' or User Story formats, populate Planguage attribute tables, and flag ambiguous passive-voice statements for editing.

**[Variant B]**

Not in source
