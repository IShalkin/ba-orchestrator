---
id: change-case-modelling
name: "Change Case Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.5"
subtask_name: "Decomposition and Systems Analysis"
source_count: 1
---

# Change Case Modelling

`T4 Modelling and Analysis › 4.5 Decomposition and Systems Analysis`

**Also described as:** Change Case Modeling

## Problem Solved

Reduces architectural brittleness and costly rework caused by anticipated future business, legal, or technical changes.

## BA Lifecycle Phase

Analysis / specification / change management

## Input Artifacts

Vision Document, Industry Trends, Regulatory Requirements, Use Case Model.

## Output Artifacts

Change Cases (oval with delta symbol), Architecture Extension Specifications.

## Participants & Roles

Sponsor, BA/System Analyst, Architect, Business Owner.

## Prerequisites

Base use case model and architecture baseline established.

## Step-by-Step Procedure

Brainstorm potential future changes (market shifts, regulatory changes, technology upgrades).
2. Document each potential future requirement as a Change Case.
3. Mark change cases with distinct visual notation (delta symbol) to separate from current scope.
4. Evaluate architectural resilience against change cases.
5. Adapt core architecture to ensure future extensibility without implementing full code prematurely.

## Analyst Questions & Prompts

What business rules or laws might change next year? What new markets or channels might we enter?

## Minimal Realistic Example

Change Case 'Process Web-Based Loan Payment' created to anticipate future online payment processing while building initial manual booking system.

## Quality Criteria & Verification

Architectural review ensuring system design supports change cases without incurring scope creep in current delivery release.

## Errors & Anti-Patterns

Treating change cases as immediate release scope (leading to bloated budgets) or ignoring future trends entirely (leading to rigid architecture).

## When NOT to Use

Disposable short-term prototypes or low-cost throwaway utility scripts.

## Alternatives & Complementary Methods

Architecture Tradeoff Analysis Method (ATAM), Scenario-Based Architecture Analysis.

## Supported Decisions

System architecture design, long-term product roadmap, risk management.

## AI & Agentic Adaptation

Not specified in source.
