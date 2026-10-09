---
id: decision-driven-analytics-requirements
name: "Decision-Driven Analytics Requirements"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 1
---

# Decision-Driven Analytics Requirements

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Decision-Driven Analytics Requirements Elicitation

## Problem Solved

Reduces uncertainty and feature creep in business intelligence and reporting projects by focusing on the specific decisions stakeholders need to make rather than just collecting lists of requested reports or fields.

## BA Lifecycle Phase

elicitation / analysis / specification

## Input Artifacts

Business objectives, stakeholder requests for reports/data, regulatory or policy constraints.

## Output Artifacts

Decision statements, report specifications, dashboard designs, display-action-response models, data transformation requirements, formula specifications.

## Participants & Roles

Business Analyst, Executive / Business Decision Maker, Data Specialist / Architect, System Analyst.

## Prerequisites

Defined business objectives establishing the problem space.

## Step-by-Step Procedure

Elicit and state the core business decisions stakeholders must make to achieve business objectives.
2. Prioritize business decisions based on their contribution to business objectives.
3. Decompose each decision into underlying diagnostic questions and precursor sub-questions.
4. Determine the information delivery mechanism (e.g., dashboard, portal, email), format, and required interactivity/flexibility (filters, drill-downs).
5. Specify data requirements (sources, volume, refresh rates, retention, security).
6. Define data transformation and computational logic (formulas, decision tables/trees) required to convert raw data into insights.

## Analyst Questions & Prompts

Why do you think an analytics solution will help you achieve desired outcomes? What specific business decisions will you make using output from this system? Why do you need that information and how will you use that report? What time frame are you analyzing: past, present, or future? What formula or business rule defines this calculation?

## Minimal Realistic Example

Defining a decision statement for a marketing VP needing quarterly regional budget allocation based on current sales, leading to specific dashboard requirements with regional and product-line drill-down filters.

## Quality Criteria & Verification

Every analytics report/dashboard traces directly to an identified business decision; calculation formulas are fully specified with clear variables and sources; data latency and security constraints are defined.

## Errors & Anti-Patterns

Focusing solely on specifying data fields without understanding usage; delivering static data when ad-hoc exploration is needed; overbuilding analytics capabilities beyond stakeholder readiness; assuming traditional use cases alone capture decision-making complexity.

## When NOT to Use

When the system requires standard operational transactional capabilities with simple, static reporting needs.

## Alternatives & Complementary Methods

Decision Tables / Decision Trees, Decision Models, Display-Action-Response (DAR) models, Report Tables.

## Supported Decisions

Scope definition for analytics projects, decision automation vs. human-in-the-loop decisions, release iteration content.

## AI & Agentic Adaptation

Not in source
