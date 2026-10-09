---
id: data-collection
name: "Data Collection"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 2
---

# Data Collection

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces uncertainty regarding system performance metrics, costs, usage trends, and non-functional baseline numbers that are not documented.

**[Variant B]**

Reduces quantitative uncertainty regarding performance, usage patterns, costs, and marketing facts that are not explicitly documented.

## BA Lifecycle Phase

**[Variant A]**

Elicitation / analysis

**[Variant B]**

Elicitation / analysis

## Input Artifacts

**[Variant A]**

System logs, transaction databases, operational statistics, performance metrics.

**[Variant B]**

System usage logs, operational databases, marketing reports, population samples.

## Output Artifacts

**[Variant A]**

Statistical datasets, usage metrics, benchmark reports, performance constraints.

**[Variant B]**

Quantitative data sets, statistical summaries, baseline metrics for non-functional requirements.

## Participants & Roles

**[Variant A]**

BA, SME, System Administrator.

**[Variant B]**

Business Analyst, Domain SME, System Administrator / Data Analyst.

## Prerequisites

**[Variant A]**

Availability of quantitative data sources or access to operational metrics.

**[Variant B]**

Access to operational data, logs, or user populations suitable for sampling.

## Step-by-Step Procedure

**[Variant A]**

Identify missing quantitative facts (e.g., peak throughput, operational costs).
2. Select representative data sets or design statistical sampling methods.
3. Gather quantitative operational metrics or execute experimental data collection.
4. Analyze and interpret statistical results.
5. Derive non-functional requirements (performance, cost, usability targets).

**[Variant B]**

Identify missing quantitative facts (e.g., peak load, transaction frequencies, operational costs).
2. Define target populations or data sources.
3. Select representative data sets using statistical sampling methods or conduct experimental data gathering.
4. Analyze and interpret collected data.
5. Translate data insights into non-functional requirements (performance, usability, cost targets).

## Analyst Questions & Prompts

**[Variant A]**

What are the peak transaction volumes? What is the current average response time? What are the operational costs per transaction?

**[Variant B]**

What are the current transaction volumes during peak hours? What is the average cost per operation? How frequently is feature X utilized by users?

## Minimal Realistic Example

**[Variant A]**

Measuring the peak number of parallel meeting requests per hour during corporate planning cycles to set scalability requirements.

**[Variant B]**

Collecting server log data over a month to establish that the peak query volume for a library system is 500 requests per minute, used to set performance targets.

## Quality Criteria & Verification

**[Variant A]**

Statistical sampling representativeness, statistical significance, correct mathematical interpretation.

**[Variant B]**

Statistical validity, representativeness of sampling, correct data interpretation and cross-verification with domain SMEs.

## Errors & Anti-Patterns

**[Variant A]**

Drawing conclusions from non-representative or un-sampled data sets; misinterpreting operational metrics into incorrect non-functional targets.

**[Variant B]**

Drawing conclusions from unrepresentative or biased samples; misinterpreting statistical metrics.

## When NOT to Use

**[Variant A]**

When accurate operational metrics are already documented or when time constraints prevent deploying statistical sampling.

**[Variant B]**

When brand-new (greenfield) domains have no baseline data available or when quantitative precision is unnecessary at an early stage.

## Alternatives & Complementary Methods

**[Variant A]**

Background study, performance benchmarking, questionnaires.

**[Variant B]**

Complementary: Background Study, Questionnaires. Alternative: Benchmarking, Prototyping simulation.

## Supported Decisions

**[Variant A]**

Non-functional scope, performance criteria, capacity planning.

**[Variant B]**

Defining performance requirements, cost-benefit trade-offs, capacity planning.

## AI & Agentic Adaptation

**[Variant A]**

Agentic data pipelines can continuously extract and aggregate operational log data to predict capacity thresholds; human review ensures realistic constraint setting.

**[Variant B]**

Autonomous data-mining agents can extract log analytics and synthesize baseline operational metrics with anomaly detection guardrails.
