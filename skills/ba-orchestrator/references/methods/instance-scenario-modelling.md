---
id: instance-scenario-modelling
name: "Instance Scenario Modelling"
task: T5
task_name: "Requirements Specification"
subtask: "5.2"
subtask_name: "Use Cases and Scenarios"
source_count: 1
---

# Instance Scenario Modelling

`T5 Requirements Specification › 5.2 Use Cases and Scenarios`

**Also described as:** Instance Scenario Modeling

## Problem Solved

Reduces abstract ambiguity, clarifies complex business rules, and bridges requirements to acceptance/system test cases.

## BA Lifecycle Phase

Analysis / validation

## Input Artifacts

Base/Elaborated Use Cases.

## Output Artifacts

Instance Scenario Descriptions (Primary 'Sunny Day' and Secondary 'Rainy Day').

## Participants & Roles

BA/System Analyst, End User, SME, Tester.

## Prerequisites

Draft use cases available.

## Step-by-Step Procedure

Select a use case and define concrete real-world input values and environmental conditions.
2. Walk through the exact execution path step-by-step using these concrete data values.
3. Record exact outputs and post-state changes.
4. Repeat for 'sunny day' paths and key 'rainy day' exception paths (5-7 instances max per key use case).
5. Use instances to validate business logic with end users.

## Analyst Questions & Prompts

What happens specifically when Joe Smith applies for a $20,000 car loan with a 750 credit score?

## Minimal Realistic Example

Scenario 'Joe Smith applies for loan': Input $20,000 amount, income $65k. Credit bureau returns 0 bad debts. Result: Credit score 85, auto-approved.

## Quality Criteria & Verification

User verification walkthroughs; complete traceability from scenario inputs/outputs to system test cases.

## Errors & Anti-Patterns

Attempting to document an infinite number of scenario instances instead of focusing on high-risk/key path instances.

## When NOT to Use

When requirements are already fully crystallized and easily verified without concrete examples.

## Alternatives & Complementary Methods

User Interface Prototypes, Test Cases.

## Supported Decisions

User validation sign-off, system test design, release acceptance criteria.

## AI & Agentic Adaptation

Not specified in source.
