---
id: quality-attribute-prioritization-grid
name: "Quality Attribute Prioritization Grid"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 1
---

# Quality Attribute Prioritization Grid

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

## Problem Solved

Exposes trade-offs and resolves conflicts among competing quality attributes (e.g., security vs. performance, ease of use vs. ease of learning) through pairwise ranking.

## BA Lifecycle Phase

prioritisation

## Input Artifacts

Taxonomy of internal and external quality attributes, project objectives, stakeholder profiles

## Output Artifacts

Prioritized Quality Attribute Matrix with calculated relative importance scores

## Participants & Roles

BA, Product Champions, System Architect, Developers, Maintenance/Support Staff

## Prerequisites

Selected candidate quality attributes relevant to the project.

## Step-by-Step Procedure

Start with a broad taxonomy of external and internal quality attributes.
2. Filter out non-applicable attributes and document rationale.
3. Construct a pairwise comparison matrix of remaining attributes.
4. For each intersecting pair, evaluate: 'If I could have only one of these two attributes, which is more important to success?'
5. Record pairwise preferences (< or ^) in the grid cells.
6. Calculate total relative scores for each attribute.
7. Use scores to guide architectural trade-offs when attribute conflicts occur during development.

## Analyst Questions & Prompts

If forced to choose between higher security and faster response times, which takes priority? Which internal quality factors are most critical for future product maintainability?

## Minimal Realistic Example

Airport check-in kiosk pairwise comparison yields Security (score 7), Integrity (6), Usability (5), and Performance (4), dictating that security/integrity take precedence when design conflicts arise.

## Quality Criteria & Verification

Review grid scores across diverse stakeholder groups (including maintenance/support staff); confirm that high-scoring attributes align with primary business objectives.

## Errors & Anti-Patterns

Declaring all quality attributes top priority; failing to include technical maintainers in quality prioritization; ignoring documented priorities when resolving design trade-offs.

## When NOT to Use

When a project has no conflicting quality demands or is a trivial utility application.

## Alternatives & Complementary Methods

QFD (Quality Function Deployment), $100 Prioritization, MoSCoW.

## Supported Decisions

Architecture, priority, release, acceptance.

## AI & Agentic Adaptation

Not in source
