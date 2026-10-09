---
id: background-study
name: "Background Study"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 2
---

# Background Study

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

**Also described as:** Background Study (Content Analysis)

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces domain uncertainty, lack of foundational business context, and improper use of domain terminology before interacting with busy stakeholders.

**[Variant B]**

Reduces uncertainty and lack of domain knowledge by acquiring background information, understanding organizational structures, terminology, and historical deficiencies from existing documentation.

## BA Lifecycle Phase

**[Variant A]**

Discovery / elicitation

**[Variant B]**

Discovery / elicitation

## Input Artifacts

**[Variant A]**

Organizational charts, business plans, policy manuals, financial reports, minutes of meetings, job descriptions, business forms, industry books, regulations, past system defect reports, complaints, change requests, user manuals.

**[Variant B]**

Organizational charts, business plans, policy manuals, financial reports, minutes of meetings, job descriptions, business forms, domain books, surveys, regulations, reports on similar systems, defect/complaint reports, user manuals.

## Output Artifacts

**[Variant A]**

Initial background sections of a preliminary draft proposal, domain glossary of terms.

**[Variant B]**

Initial sections of a preliminary draft proposal, glossary of terms.

## Participants & Roles

**[Variant A]**

BA (Analyst).

**[Variant B]**

Business Analyst / Requirements Engineer (conducting the study).

## Prerequisites

**[Variant A]**

Access to existing organizational, regulatory, and system documentations.

**[Variant B]**

Availability of relevant organizational, domain, or system documentation.

## Step-by-Step Procedure

**[Variant A]**

Acquire meta-knowledge to identify required vs unnecessary information.
2. Prune the documentation space.
3. Collect relevant documents (business, domain, system-as-is).
4. Read, analyze, and synthesize document contents.
5. Extract core concepts, regulations, policies, and reported weaknesses.
6. Draft initial proposal sections and establish a glossary of domain terms.

**[Variant B]**

Acquire meta-knowledge to identify what needs to be known and prune the documentation space.
2. Collect relevant documentation (organizational, domain, system-as-is, legacy software).
3. Read, analyze, and synthesize the documentation.
4. Extract key information, terminology, policies, and reported problems.
5. Establish a preliminary draft proposal and a baseline glossary of terms.

## Analyst Questions & Prompts

**[Variant A]**

What do I need to know vs not need to know? What is the structure, business objectives, and policies of the organization? What terminology is standard in this domain? What defects and complaints were reported for the system-as-is?

**[Variant B]**

What do I need to know and what can I skip? What is the official terminology used? What business rules and regulations apply? What complaints or defects were recorded for the current system?

## Minimal Realistic Example

**[Variant A]**

A business analyst reviews a university's library policy manuals and past patron complaints to understand loan periods, fine rules, and missing book issues prior to interviewing library staff.

**[Variant B]**

A BA reads the existing library policy manual and legacy software manual before interviewing staff, extracting terms like 'patron' and 'borrowing limit' to populate the project glossary.

## Quality Criteria & Verification

**[Variant A]**

Document currency and accuracy verification; meta-knowledge filtering to ensure pruning of irrelevant documentation; consensus on extracted glossary definitions.

**[Variant B]**

Source accuracy check, cross-referencing information across multiple documents, review meetings with stakeholders to validate synthesized knowledge.

## Errors & Anti-Patterns

**[Variant A]**

Getting overwhelmed by massive volumes of documentation (data-mining problem); relying on outdated or inaccurate documentation without verification.

**[Variant B]**

Information overload (getting lost in a mass of irrelevant details); relying on outdated, inaccurate, or obsolete documentation.

## When NOT to Use

**[Variant A]**

Rarely skipped entirely, but restricted when documentation is completely absent, untrustworthy, or obsolete.

**[Variant B]**

When documentation is completely non-existent, radically inaccurate, or when time constraints make reading voluminous obsolete reports counterproductive.

## Alternatives & Complementary Methods

**[Variant A]**

Data collection, questionnaires, interviews, observation, model-driven meta-knowledge filtering.

**[Variant B]**

Complementary: Data Collection, Interviews, Observation. Alternative: Direct stakeholder interviews when no documents exist.

## Supported Decisions

**[Variant A]**

Scope delimitation, baseline terminology definition, interview targeting.

**[Variant B]**

Scoping the elicitation process, defining target stakeholders to interview, establishing standard terminology.

## AI & Agentic Adaptation

**[Variant A]**

LLMs can ingest large document corpora to automatically draft domain glossaries, summarize system defect reports, and highlight regulatory constraints; human-in-the-loop validates accuracy and resolves document contradictions.

**[Variant B]**

AI agents can perform automated content analysis/RAG over large document repositories, extracting glossaries, business rules, and domain entities with Human-in-the-loop validation for accuracy.
