---
id: requirements-reuse
name: "Requirements Reuse"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.3"
subtask_name: "Organisation, Baselines and Reuse"
source_count: 1
---

# Requirements Reuse

`T6 Prioritisation and Requirements Management › 6.3 Organisation, Baselines and Reuse`

**Also described as:** Requirements Reuse Management

## Problem Solved

Prevents 'reinventing the wheel', reduces requirements writing/review time, and enforces functional and architectural consistency across product lines and enterprise applications.

## BA Lifecycle Phase

specification

## Input Artifacts

Enterprise data dictionaries, business rules repositories, standard security/compliance requirements, existing SRS documents, requirement patterns

## Output Artifacts

Reusable Requirements Repository / Library, Shared Glossary, Centralized Business Rules, Reusable Acceptance Test Suites

## Participants & Roles

BA, Reuse Repository Manager, System Architect, Compliance Officers

## Prerequisites

High-quality, well-structured existing requirements; enterprise repository/tool infrastructure.

## Step-by-Step Procedure

Identify candidates for reuse (security rules, glossaries, compliance constraints, generic features).
2. Abstract requirements to the appropriate generalization level to fit multiple applications.
3. Store assets in a searchable repository with unique identifiers, domain tags, and traceability links.
4. When starting a new project, search the repository for candidate requirements before writing new text.
5. Reuse assets by reference (hyperlinking/pointing) or by managed copy/cloning.
6. Maintain and refine reused requirements as new project insights are gained.

## Analyst Questions & Prompts

Have we written requirements for this capability on a previous project? Can this requirement be generalized for use across our product family? What regulatory or security standards apply universally?

## Minimal Realistic Example

Reusing a standardized set of User Authentication & Password Security requirements across all mobile apps in a product line by linking to the central tool repository.

## Quality Criteria & Verification

Verification that reused assets are maintained in a central location; validation that cross-references do not break; periodic auditing of repository quality.

## Errors & Anti-Patterns

Ad hoc 'copy-and-paste' reuse without tracking origins or context; over-specifying hyper-detailed requirements that fit only one product; 'Not Invented Here' (NIH) bias.

## When NOT to Use

In rapidly changing, highly novel domains where no legacy or reusable knowledge exists.

## Alternatives & Complementary Methods

Requirement Patterns, Enterprise Data Dictionary, Business Rules Repository.

## Supported Decisions

Architecture, compliance, release baseline.

## AI & Agentic Adaptation

Not in source
