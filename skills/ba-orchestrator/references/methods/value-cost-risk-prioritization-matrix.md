---
id: value-cost-risk-prioritization-matrix
name: "Value-Cost-Risk Prioritization Matrix"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 2
---

# Value-Cost-Risk Prioritization Matrix

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

**Also described as:** Prioritization Matrix; Value-Cost-Risk Prioritization Spreadsheet Model

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Ranks requirements analytically by calculating priority scores derived from relative benefit, detriment, cost, and risk.

**[Variant B]**

Removes political noise, 'decibel prioritization', and subjective guesswork by calculating a semi-quantitative priority rank based on relative business value, cost, and technical risk.

## BA Lifecycle Phase

**[Variant A]**

Prioritisation / Management

**[Variant B]**

prioritisation

## Input Artifacts

**[Variant A]**

Set of requirements (same abstraction level), weight factors for benefit, detriment, cost, and risk

**[Variant B]**

Feature tree, list of use cases or user stories, business objectives

## Output Artifacts

**[Variant A]**

Prioritization matrix with calculated relative ranks

**[Variant B]**

Prioritization Spreadsheet Matrix (columns: Feature, Relative Benefit, Relative Penalty, Total Value, Value %, Relative Cost, Cost %, Relative Risk, Risk %, Calculated Priority)

## Participants & Roles

**[Variant A]**

Requirements Engineer, Project Manager, Customer/Business Representatives, Developers

**[Variant B]**

BA/Project Manager (facilitator), Customer Representatives/Product Champions (benefit/penalty raters), Developers (cost/risk raters)

## Prerequisites

**[Variant A]**

Requirements selected at a uniform level of detail; weights defined for Benefit, Detriment, Cost, Risk.

**[Variant B]**

Discretionary features list formulated at a consistent level of abstraction.

## Step-by-Step Procedure

**[Variant A]**

Define relative weight factors (WeightBenefit, WeightDetriment, WeightCost, WeightRisk).
2. Estimate Relative Benefit and Relative Detriment (scale 1-9) for each requirement.
3. Calculate Value% for each requirement: Benefit x WeightBenefit + Detriment x WeightDetriment.
4. Estimate Relative Cost and Relative Risk (scale 1-9) and compute Cost% and Risk%.
5. Compute Priority score: Priority = Value% / (Cost% x WeightCost + Risk% x WeightRisk).
6. Rank requirements based on calculated Priority scores.

**[Variant B]**

List candidate features or user stories at a consistent abstraction level.
2. Customer representatives rate Relative Benefit (1-9) and Relative Penalty (1-9) for each item.
3. Developers rate Relative Cost (1-9) and Relative Technical Risk (1-9) for each item.
4. Calculate Total Value % = (Benefit Weight + Penalty Weight) / Sum(Values).
5. Calculate Cost % and Risk % relative to totals.
6. Compute Priority = Value % / (Cost % * Weight + Risk % * Weight).
7. Sort items in descending order of calculated priority and review relative groupings with stakeholders.

## Analyst Questions & Prompts

**[Variant A]**

"What is the business loss if this is omitted?", "What is the relative implementation risk score from 1 to 9?"

**[Variant B]**

On a 1-9 scale, what business benefit does this feature provide? What penalty or downside occurs if this feature is omitted? What is the technical implementation risk/complexity?

## Minimal Realistic Example

**[Variant A]**

Five core navigation requirements are scored in a spreadsheet; Requirement 1 achieves a priority score of 0.941, earning Rank 1 over Requirement 5 (score 0.489, Rank 5).

**[Variant B]**

Prioritizing 10 Chemical Tracking System features: 'Print MSDS' achieves highest priority (1.22) due to high penalty/low cost, whereas 'Import Chemical Structure Drawing' scores lowest (0.33) due to high cost/risk.

## Quality Criteria & Verification

**[Variant A]**

Math consistency in percentage distributions; reduction of subjective bias in ranking.

**[Variant B]**

Calibration against completed projects; consensus on 1-9 rating inputs; validation that top priority items directly align with key business goals.

## Errors & Anti-Patterns

**[Variant A]**

Mixing high-level goals with fine-grained technical requirements in the same matrix.

**[Variant B]**

Over-interpreting minor numerical differences between close scores; including mandatory compliance items that are non-discretionary; gaming the ratings by assigning '9' to all benefit scores.

## When NOT to Use

**[Variant A]**

When rapid ad-hoc prioritization is needed and time/resources do not permit multi-factor estimation.

**[Variant B]**

For mandatory regulatory features, core architectural infrastructure, or simple informal prioritization on tiny projects.

## Alternatives & Complementary Methods

**[Variant A]**

Kano Classification, Single-Criterion Classification, Ranking, Top-Ten

**[Variant B]**

Three-Level Scale (Importance/Urgency), $100 Method, Objective Chain Technique, MoSCoW.

## Supported Decisions

**[Variant A]**

Release planning, budget allocation, backlog refinement.

**[Variant B]**

Scope, priority, release planning.

## AI & Agentic Adaptation

**[Variant A]**

Machine learning models estimate relative cost and risk inputs based on historical repository data to populate the matrix automatically.

**[Variant B]**

Not in source
