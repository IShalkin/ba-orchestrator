---
id: architecture-debt-analysis
name: "Architecture Debt Analysis"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Architecture Debt Analysis

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

**Also described as:** Architecture Debt Analysis via Hotspot Discovery

## Problem Solved

Identifies, quantifies, and calculates the ROI for refactoring architectural debt caused by design anti-patterns and high maintenance churn.

## BA Lifecycle Phase

Change Management

## Input Artifacts

Source code repository, version control revision history (commits/churn), issue tracking database (bugs/tickets).

## Output Artifacts

Design Structure Matrix (DSM), identified architectural anti-patterns/hotspots, quantified debt cost (person-months), refactoring ROI business case.

## Participants & Roles

Software Architect, Maintenance Leads, Software Engineering Manager.

## Prerequisites

Access to source code, commit history, and issue tracking history spanning a sufficient operational period.

## Step-by-Step Procedure

Extract static structural dependencies from source code.
2. Extract evolutionary co-change dependencies from revision history.
3. Build combined Design Structure Matrix (DSM).
4. Scan DSM for architecture anti-patterns (Cliques, Unhealthy Inheritance, Modularity Violations, Crossing, Unstable Interfaces).
5. Overlay bug/churn data from issue tracker onto identified hotspots.
6. Calculate refactoring effort vs. maintenance savings (ROI).

## Analyst Questions & Prompts

Which files change together frequently despite having no structural link? Are there cyclic dependencies among components? Which modules generate the highest proportion of defects?

## Minimal Realistic Example

Identifying an Unhealthy Inheritance anti-pattern between SSTable and SSTableReader with 68 co-commits; refactoring costs 14 person-months but saves 41 person-months annually.

## Quality Criteria & Verification

Hotspot identification validated by architect agreement; quantitative ROI calculation demonstrating positive financial payback for refactoring.

## Errors & Anti-Patterns

Focusing purely on static code metrics (e.g., LOC, cyclomatic complexity) while ignoring evolutionary co-change and defect history.

## When NOT to Use

New greenfield projects without sufficient commit or issue history.

## Alternatives & Complementary Methods

Code Refactoring Inspections, Static Code Analysis (e.g., SonarQube), Architecture Reconstruction.

## Supported Decisions

Refactoring prioritization, technical debt payoff justification, maintenance budget allocation.

## AI & Agentic Adaptation

Fully automatable pipeline where agentic scripts mine Git/Jira, build DSMs, flag anti-pattern hotspots, and generate refactoring ROI reports for architect approval.
