---
id: planguage
name: "Planguage"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 2
---

# Planguage

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

**Also described as:** Planguage Quality Attribute Specification

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Defines quality requirements with extreme quantitative precision using a structured syntax for scales, meters, baseline values, and target benchmarks.

**[Variant B]**

Eliminates vague, ambiguous, and unverifiable nonfunctional quality goals (e.g., 'user-friendly', 'fast', '24x7 availability') by defining multi-level quantitative targets.

## BA Lifecycle Phase

**[Variant A]**

specification

**[Variant B]**

specification

## Input Artifacts

**[Variant A]**

Quality grid, stakeholder goals, benchmark metrics.

**[Variant B]**

Elicited quality expectations, SLAs, business objectives, architectural constraints

## Output Artifacts

**[Variant A]**

Planguage requirement statements (Tag, Gist, Scale, Meter, Must, Plan, Wish, Past).

**[Variant B]**

Planguage Statements (keywords: TAG, AMBITION, SCALE, METER, GOAL, STRETCH, WISH, FAIL, DEFINED)

## Participants & Roles

**[Variant A]**

BA, system architect, QA manager, vendor.

**[Variant B]**

BA, System Architect, Developers, Testers, Business Owner

## Prerequisites

**[Variant A]**

Identification of key quality factors needing quantitative control.

**[Variant B]**

Prioritized list of critical quality attributes for the project.

## Step-by-Step Procedure

**[Variant A]**

Define a unique Tag and brief Gist for the quality requirement.
2. Define the exact measurement Scale.
3. Define the practical test procedure (Meter).
4. Specify baseline historic performance (Past).
5. Define mandatory survival threshold (Must), target goal (Plan), and ideal goal (Wish).
6. Review parameters with stakeholders and suppliers.

**[Variant B]**

Assign a unique hierarchical TAG and state the high-level AMBITION.
2. Define the SCALE (units of measurement) for quantifying the attribute.
3. Define the METER (testing/measurement method or test setup).
4. Specify the GOAL (minimum acceptable level of achievement).
5. Optionally specify STRETCH (desirable target), WISH (ideal target), or FAIL conditions.
6. Explicitly define all domain specific terms used in the Planguage block (DEFINED).
7. Review criteria with architects and testers to ensure feasibility and verifiability.

## Analyst Questions & Prompts

**[Variant A]**

What is the worst acceptable performance before the system is rejected (Must)? How exactly will we measure this in practice (Meter)?

**[Variant B]**

What unit of measure quantifies this quality aspect? How will we measure or test it? What is the minimum acceptable performance level versus the stretch goal?

## Minimal Realistic Example

**[Variant A]**

Tag: Forecast Speed. Scale: Seconds from button push to report. Meter: Stopwatch during peak hours. Must: 8 min. Plan: Supplier fill. Wish: 2 min. Past: 1 hour.

**[Variant B]**

TAG: Performance.Report.ResponseTime | AMBITION: Fast report generation | SCALE: Elapsed seconds | METER: Stopwatch test on 30 sample reports | GOAL: <= 8 seconds for 95% of reports | STRETCH: <= 2 seconds.

## Quality Criteria & Verification

**[Variant A]**

Quantitative verification testing according to the defined Meter specification.

**[Variant B]**

Verification that goals are quantitative and SMART (Specific, Measurable, Attainable, Relevant, Time-sensitive); review by test leads for testability.

## Errors & Anti-Patterns

**[Variant A]**

Over-specifying Planguage for trivial quality factors, creating overly complex documents.

**[Variant B]**

Setting unrealistic 100% goals (e.g., 'five 9s' availability) without recognizing cost impacts; specifying goals without defining the METER (measurement method).

## When NOT to Use

**[Variant A]**

Simple projects where standard informal quality targets suffice.

**[Variant B]**

For simple functional requirements or low-risk nonfunctional aspects that require no quantitative trade-off analysis.

## Alternatives & Complementary Methods

**[Variant A]**

Open Metric & Open Target Requirements, Quality Grid.

**[Variant B]**

Fit Criteria, Acceptance Criteria, Quality Attribute Checklist.

## Supported Decisions

**[Variant A]**

Contractual acceptance criteria, architectural trade-offs, quantitative SLA definitions.

**[Variant B]**

Architecture, acceptance, compliance, release.

## AI & Agentic Adaptation

**[Variant A]**

Convert informal quality statements into fully structured Planguage parameter blocks using AI syntax templates.

**[Variant B]**

Not in source
