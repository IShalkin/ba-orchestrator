---
id: report-specification
name: "Report Specification"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 1
---

# Report Specification

`T4 Modelling and Analysis › 4.2 Data and Concepts`

## Problem Solved

Reduces layout rework, missing query parameters, and unfulfilled business decision needs when delivering system reports and dashboards.

## BA Lifecycle Phase

elicitation

## Input Artifacts

Existing reports, stakeholder decision needs, data models, business rules

## Output Artifacts

Report Specification Document / Template (sections: Purpose, Decisions Made, Users, Data Sources, Layout, Headers/Footers, Body Format, Security/Access Rules) or Mock-up Prototype

## Participants & Roles

BA, Report Users/SMEs, Data Analyst, BI Developer

## Prerequisites

Understood business objectives driving the need for the report.

## Step-by-Step Procedure

Identify the business decisions made using the report and who makes them.
2. Determine report type (static vs. dynamic/real-time) and delivery frequency/trigger.
3. Identify data sources, query selection criteria, user-selectable parameters, and calculations.
4. Specify layout properties: orientation, page breaks, sorting, grouping, subtotals, and totals.
5. Define display formatting for fields, handling of zero-data results, and overflow rules.
6. Specify security restrictions limiting report access or data scope.
7. Create a mock-up prototype using realistic data and validate with users.

## Analyst Questions & Prompts

What business decisions will be made from this report and by whom? Is this report static or dynamic? What query parameters can the user select? How should the system respond if no data is returned?

## Minimal Realistic Example

Report Specification for 'Laboratory Inventory Report': Lists chemical containers per lab, grouped by hazards, refreshed daily, accessible only to Lab Managers.

## Quality Criteria & Verification

Confirm data sources exist in the data dictionary; verify layout compliance against corporate/industry standards; review mock-up with target users.

## Errors & Anti-Patterns

Designing reports without knowing what business decisions depend on them; specifying hardcoded column layouts that fail when data grows; creating redundant variants of existing reports.

## When NOT to Use

When user needs are purely transactional and involve no data aggregation or reporting.

## Alternatives & Complementary Methods

Dashboard Specification, UI Prototype, Data Dictionary.

## Supported Decisions

Scope, compliance, acceptance, release.

## AI & Agentic Adaptation

Not in source
