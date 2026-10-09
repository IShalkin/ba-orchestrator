---
id: data-mining
name: "Data Mining"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.4"
subtask_name: "Domain, Document and Data Research"
source_count: 1
---

# Data Mining

`T2 Situation Investigation and Elicitation › 2.4 Domain, Document and Data Research`

## Problem Solved

Reduces decision uncertainty by extracting hidden patterns, correlations, and predictive insights from large datasets.

## BA Lifecycle Phase

Discovery / analysis / Solution Evaluation

## Input Artifacts

Large transactional datasets, historical logs, decision models, business objectives.

## Output Artifacts

Data mining models (descriptive, diagnostic, predictive), scorecards, discovered business rules, dashboards.

## Participants & Roles

BA, Data Analyst/Scientist, Business Owner, SME, IT/Database Admin.

## Prerequisites

Access to high-volume, high-quality data and clear decision requirements or pattern discovery goals.

## Step-by-Step Procedure

Establish goals/scope (top-down decision-driven or bottom-up pattern discovery).
2. Prepare analytical dataset by merging, cleaning, and partitioning data (training, testing, validation sets).
3. Analyze data distributions, missing values, and calculated characteristics.
4. Apply modelling techniques (decision trees, regression, clustering, neural networks).
5. Validate model accuracy on independent test datasets.
6. Deploy model as visual reports, mathematical formulas, or executable business rules.

## Analyst Questions & Prompts

"What historical patterns predict customer churn?", "Why does this performance variance exist?", "Which data fields offer the highest predictive value for fraud detection?"

## Minimal Realistic Example

A telecom firm mines 2 years of customer usage logs using decision trees, discovering that customers with >3 support calls and falling data usage have an 80% probability of churning.

## Quality Criteria & Verification

Model replicates successfully on independent validation data; insights are actionable and deployable within decision processes.

## Errors & Anti-Patterns

Applying data mining without understanding the business decision context; assuming correlation implies causation.

## When NOT to Use

When available dataset volume or quality is inadequate, or when business decision logic is simple and fully known.

## Alternatives & Complementary Methods

Complemented by Decision Modelling, Business Rules Analysis, Metrics & KPIs, and Root Cause Analysis.

## Supported Decisions

Automated operational decisions (credit scoring, fraud detection), marketing strategy, customer segmentation.

## AI & Agentic Adaptation

Agentic AI natively executes end-to-end data mining (data cleaning, feature engineering, AutoML model selection), outputting natural language insight summaries for analysts.
