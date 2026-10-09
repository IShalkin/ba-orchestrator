---
id: process-analysis
name: "Process Analysis"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 1
---

# Process Analysis

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

## Problem Solved

Reduces operational waste, bottlenecks, and hand-off errors by systematically evaluating a business process for efficiency, effectiveness, and alignment.

## BA Lifecycle Phase

analysis / Discovery / Solution Evaluation

## Input Artifacts

Current state process models, performance metrics, cycle time data, pain points.

## Output Artifacts

Gap analysis report, root cause identification, process improvement options, VSM/SIPOC maps.

## Participants & Roles

BA, Process Owner, Process Analyst, Process Participants, Operational Support.

## Prerequisites

Documented current state process flow and baseline performance metrics.

## Step-by-Step Procedure

Identify gaps and non-value-added steps in current process.
2. Perform root cause analysis on identified bottlenecks and error points.
3. Apply specialized methods (SIPOC, Value Stream Mapping, Cycle-time analysis, Value Added analysis).
4. Evaluate hand-offs between roles to eliminate wait times and redundant steps.
5. Generate and analyze process improvement options (automation, task simplification).
6. Formulate future state process recommendations.

## Analyst Questions & Prompts

"Which steps in this process add value for the customer?", "Where does work sit waiting in queue (bottle-neck)?", "What is the root cause of rework in step X?"

## Minimal Realistic Example

Value Stream Analysis reveals that an invoice approval process takes 5 days total, but actual work processing time is only 15 minutes (99.8% wait time waste).

## Quality Criteria & Verification

Distinguishes value-add vs non-value-add steps; root causes of bottlenecks identified; improvement options backed by quantitative cycle time data.

## Errors & Anti-Patterns

Automating a bad process without fixing underlying process flaws ('automating waste'); analyzing processes without involving actual frontline workers.

## When NOT to Use

On highly ad-hoc, creative, non-repeatable human processes where fixed workflow analysis cannot apply.

## Alternatives & Complementary Methods

Complemented by Process Modelling, Root Cause Analysis, SIPOC, Value Stream Mapping, and Benchmarking.

## Supported Decisions

Process re-engineering scope, automation target selection, operational cost reduction strategy.

## AI & Agentic Adaptation

Process mining agents can ingest system event logs (e.g., SAP/Salesforce logs) to construct accurate real-time process execution maps and pinpoint exact bottleneck latencies automatically.
