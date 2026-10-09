---
id: feasibility-prototyping
name: "Feasibility Prototyping"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.8"
subtask_name: "Prototypes and Scenarios for Elicitation"
source_count: 1
---

# Feasibility Prototyping

`T2 Situation Investigation and Elicitation › 2.8 Prototypes and Scenarios for Elicitation`

## Problem Solved

Reduces technical uncertainty, uncovers dependency risks ('dependency hell'), and verifies whether external technology components or unproven algorithms can actually deliver expected performance.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Required Technology Elements list (Chapter P.5), Risk Analysis (Chapter P.6), interface specifications.

## Output Artifacts

Feasibility Prototype Code, Feasibility Report integrated into Chapter P.6, updated technology choices in P.2/P.5.

## Participants & Roles

Requirements Engineer / System Architect / Lead Programmer (Developer), Business Analyst (Evaluator).

## Prerequisites

Identification of critical external software dependencies, hardware integrations, or novel algorithms with unverified capabilities.

## Step-by-Step Procedure

Identify critical, unproven external technologies or dependencies in Chapter P.5.
2. Formulate explicit risk hypotheses in Chapter P.6.
3. Design a targeted, small-scale mini-project (prototype) solely to test the specific capability or integration point.
4. Implement and run the prototype ('tracer code' or benchmark).
5. Measure performance, compatibility, stability, and dependency constraints.
6. Evaluate results against requirements criteria.
7. Update Risk Analysis (P.6) with mitigation strategies or select alternative technology choices (P.2/P.5).

## Analyst Questions & Prompts

"Can Library X really process 10,000 transactions per second? Does API Y support mobile platforms? Will upgrading to Version Z break existing dependencies?"

## Minimal Realistic Example

Building a 2-day prototype to test if a third-party PDF rendering library can process 500-page invoice files within 2 seconds before committing it to Chapter P.5.

## Quality Criteria & Verification

Explicit risk reduction in P.6; objective benchmark metrics demonstrating technical feasibility.

## Errors & Anti-Patterns

Confusing feasibility prototypes with shippable code; skipping feasibility checks and discovering technical roadblocks late in construction.

## When NOT to Use

Standard, well-understood technologies with proven track records in the organization.

## Alternatives & Complementary Methods

Tracer Code, Architectural Spikes, Benchmarking, Literature/Vendor Review.

## Supported Decisions

Architecture selection, third-party library adoption, risk mitigation strategies, project schedule estimation.

## AI & Agentic Adaptation

AI agents can automatically generate synthetic test spikes, execute micro-benchmarks against external APIs, and summarize performance risks into Chapter P.6.
