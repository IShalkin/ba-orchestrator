---
id: understanding-the-problem-before-the-solution
name: "Understanding the Problem Before the Solution"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.1"
subtask_name: "Problem and Scope Framing"
source_count: 1
---

# Understanding the Problem Before the Solution

`T2 Situation Investigation and Elicitation › 2.1 Problem and Scope Framing`

**Also described as:** Understanding the Problem Before Converging on a Solution (Root Cause Analysis / Problem Statement)

## Problem Solved

Prevents teams from building features or products that go unused or fail because they solve the wrong problem, address only symptoms, or jump prematurely to a suboptimal solution.

## BA Lifecycle Phase

Discovery / Analysis

## Input Artifacts

Initial project ideas, business cases, project charters, senior leadership or customer requests, stated problems, proposed solution descriptions.

## Output Artifacts

Root Cause Analysis Diagram (Fishbone / Ishikawa Diagram), Problem Statement document/section.

## Participants & Roles

Business Analyst (facilitator/analyst), Executive Sponsor, Lead Customer, Product Visionary, Key Stakeholders, SMEs.

## Prerequisites

A proposed initiative, business need, user complaint, or proposed solution provided by stakeholders.

## Step-by-Step Procedure

Receive a stated problem or proposed solution request from a stakeholder.
2. Ask 'Why' repeatedly (e.g., using the 5 Whys technique) to trace backward from the symptoms or proposed solution to true underlying root causes.
3. Identify primary causes and contributing factors.
4. (Optional) Draw a Fishbone (Ishikawa) diagram placing the problem at the head and contributing causes along diagonal branches.
5. Evaluate all implications and determine whether the proposed solution actually addresses the root cause or if alternative/interim solutions are required.
6. Formulate a Problem Statement defining the Situation, Problem, Implication, Benefit, and Vision.

## Analyst Questions & Prompts

"Why do we need to combine them / do this?", "Why is that a problem?", "Why are we not already achieving that goal today?", "If  is the answer, what was the question?", "Why do you think that's the right solution?"

## Minimal Realistic Example

A stakeholder asks to combine four independent backend systems into one. Asking 'Why' reveals two root causes: customers are frustrated by logging in repeatedly across sites (losing 25% to competitors), and maintaining four separate programming languages is costly. The BA proposes single sign-on as a rapid interim fix for user churn while planning system consolidation.

## Quality Criteria & Verification

Verify that every identified root cause is actionable; ensure the problem statement explicitly covers Situation, Problem, Implication, Benefit, and Vision; check that key stakeholders explicitly agree on the core problem statement.

## Errors & Anti-Patterns

Assuming a presented solution or initial problem description is automatically correct; solving symptoms instead of root causes; 'project success but product failure' (delivering what was asked for on time, but no one uses it).

## When NOT to Use

When the problem domain and root causes are already fully understood, clear, and validated by data, or for trivial low-risk bug fixes.

## Alternatives & Complementary Methods

Complementary: Practice #2 Define Business Objectives, Practice #3 Define Solution Boundaries, Practice #13 Prioritize Requirements. Alternatives: Impact Mapping, 5 Whys standalone.

## Supported Decisions

Scope definition, solution selection (e.g., build vs. buy, interim vs. long-term fix), project go/no-go.

## AI & Agentic Adaptation

An AI agent can be prompted with initial user request texts to perform automated 5 Whys decomposition, generate fishbone structure in Markdown/JSON, draft structured Problem Statements, and flag potential mismatched assumptions between proposed solutions and stated goals. Human-in-the-loop validates root causes with domain SMEs.
