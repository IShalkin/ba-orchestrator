---
id: kpi-modelling-kpim
name: "KPI Modelling (KPIM)"
task: T1
task_name: "Strategy Analysis and Justification"
subtask: "1.2"
subtask_name: "Strategy, Goals and Measures"
source_count: 1
---

# KPI Modelling (KPIM)

`T1 Strategy Analysis and Justification › 1.2 Strategy, Goals and Measures`

**Also described as:** Key Performance Indicator Modeling (KPIM)

## Problem Solved

Reduces misalignment and wrong prioritization by directly quantifying process efficiency gains and linking requirements to measurable business metrics.

## BA Lifecycle Phase

analysis / prioritisation

## Input Artifacts

As-is process flows (flowcharts, swimlane diagrams, activity diagrams), success metrics from vision and scope document.

## Output Artifacts

KPIM diagrams (process models with KPI annotations overlaid on specific steps), prioritized requirement lists.

## Participants & Roles

Business Analyst, Business Owner / Sponsor, Subject Matter Expert.

## Prerequisites

Established baseline values for current business performance metrics and process models.

## Step-by-Step Procedure

Identify critical business performance metrics and KPIs (e.g., execution time, error rates).
2. Measure current baseline values for each KPI.
3. Overlay KPIs onto specific process steps in flowcharts or swimlane diagrams.
4. Prioritize process steps that show the highest impact on target KPIs.
5. Trace software requirements to process steps mapped to KPIs to establish implementation priority.
6. (Optional) Specify system functionality to periodically monitor KPIs post-implementation.

## Analyst Questions & Prompts

How long does it take to execute individual process steps? What is the current baseline value for this metric? Which performance metrics are most critical to maintain or improve? What performance trade-offs are acceptable?

## Minimal Realistic Example

Annotating a loan risk calculation flowchart with KPI-1: 'Reduce data aggregation time from 120 minutes to 2 minutes' and KPI-2: '100% error-free data inputs'.

## Quality Criteria & Verification

Clear linkage between process steps, KPIs, and software requirements; baseline metrics documented and validated by business stakeholders.

## Errors & Anti-Patterns

Automating decisions or steps where custom logic development costs far exceed the operational value gained; degrading critical quality attributes in pursuit of a single metric.

## When NOT to Use

When metrics data cannot be measured, or when process automation scope is trivial and metrics-driven trade-offs are unnecessary.

## Alternatives & Complementary Methods

Goal modeling, Planguage metric specification, Quality Function Deployment (QFD).

## Supported Decisions

Requirement prioritization decisions, release scope decisions, trade-off decisions between competing performance attributes.

## AI & Agentic Adaptation

Not in source
