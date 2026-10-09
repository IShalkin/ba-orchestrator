---
id: open-metric-and-open-target
name: "Open Metric and Open Target"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 1
---

# Open Metric and Open Target

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

**Also described as:** Open Metric and Open Target Requirements

## Problem Solved

Prevents arbitrary or unrealistically expensive quality targets by inviting suppliers to specify achievable metrics or performance targets based on their expertise.

## BA Lifecycle Phase

specification

## Input Artifacts

Quality grid, stakeholder expectation notes.

## Output Artifacts

Textual quality requirements with open blanks for suppliers to fill in, combined with customer expectation anchors.

## Participants & Roles

BA, customer project manager, vendor.

## Prerequisites

Identification of a non-mandatory or soft quality factor.

## Step-by-Step Procedure

Identify a quality factor where the exact target value is uncertain or cost-sensitive.
2. Define the measurement scale and test procedure.
3. Leave the target value blank for the supplier to specify in their proposal.
4. Optionally append the customer's benchmark expectation in parentheses.
5. Evaluate supplier proposals during tender based on offered target vs. price.

## Analyst Questions & Prompts

What response time can your standard product guarantee? What forecast accuracy can you commit to for a business of our size?

## Minimal Realistic Example

R5: Product shall compute a room occupation forecast within ___ minutes. (Customer expects one minute.)

## Quality Criteria & Verification

Verification testing against supplier's proposed value during system/acceptance testing.

## Errors & Anti-Patterns

Using open targets for physically mandatory constraints (e.g., real-time valve control) where a fixed limit is non-negotiable.

## When NOT to Use

Hard real-time technical systems where targets are governed strictly by physical laws.

## Alternatives & Complementary Methods

Planguage, Standard Quality Requirements.

## Supported Decisions

Vendor proposal comparison, cost vs. quality trade-offs, contract target negotiations.

## AI & Agentic Adaptation

Analyze vendor response proposals to automatically extract and benchmark filled-in open targets across competitors.
