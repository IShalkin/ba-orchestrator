---
id: root-cause-analysis
name: "Root Cause Analysis"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.2"
subtask_name: "Root Cause Analysis"
source_count: 2
---

# Root Cause Analysis

`T2 Situation Investigation and Elicitation › 2.2 Root Cause Analysis`

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Prevents superficial symptom-fixing by systematically identifying and evaluating the underlying fundamental origin of a problem.

**[Variant B]**

Treating symptoms instead of eliminating the true cause

## Uncertainty Reduced

**[Variant B]**

Not understanding the underlying nature of the problem

## BA Lifecycle Phase

**[Variant A]**

Discovery / analysis / Solution Evaluation

**[Variant B]**

Analysis, discovery

## Input Artifacts

**[Variant A]**

Problem statement, defect reports, performance variance data, process observation notes.

**[Variant B]**

Incidents, problems, stakeholder complaints

## Output Artifacts

**[Variant A]**

Fishbone (Ishikawa) Diagrams, 5 Whys analysis trace, corrective action plan.

**[Variant B]**

Result: cause-and-effect diagram, root cause. Artifacts: Ishikawa (fishbone) diagram, cause tree

## Participants & Roles

**[Variant A]**

BA, Facilitator, SME, Process Worker, Quality Engineer.

**[Variant B]**

BA, SME, Operational Support

## Prerequisites

**[Variant A]**

A clearly defined, observable problem statement.

## Step-by-Step Procedure

**[Variant A]**

Define Problem Statement clearly (describe issue, impact, and location).
2. Collect data regarding the magnitude and timing of the problem.
3. Choose technique: Fishbone Diagram (for category analysis) or 5 Whys (for iterative drill-down).
4. Fishbone: draw spine, add category bones (People, Process, Tools, Policy), brainstorm causes.
5. 5 Whys: repeatedly ask 'Why did this occur?' (typically 5 levels deep) until the fundamental root cause is reached.
6. Identify and evaluate corrective/preventive action plans to eliminate the root cause.

**[Variant B]**

1. Formulate the problem.
2. Ask 'Why?' five times (Fishbone / 5 Whys).
3. Determine the root cause.
4. Develop countermeasures.

## Analyst Questions & Prompts

**[Variant A]**

"Why did problem X occur?", "What is the fundamental underlying cause behind this symptom?", "Will addressing factor Y permanently prevent recurrence?"

**[Variant B]**

'Why did this happen?', 'What caused this deviation?'

## Minimal Realistic Example

**[Variant A]**

Problem: 'Invoice paid late'. Why 1: Delay in approval. Why 2: Manager missed email. Why 3: No auto-reminder system. Why 4: Process was never automated -> Root Cause: Lack of workflow automation.

**[Variant B]**

Analysing frequent product returns: supplier defects -> weak incoming inspection

## Quality Criteria & Verification

**[Variant A]**

Analysis identifies root causes rather than superficial symptoms; proposed corrective action permanently eliminates or mitigates recurrence.

**[Variant B]**

Experts confirm the cause-and-effect logic

## Errors & Anti-Patterns

**[Variant A]**

Stopping analysis at first-level symptoms; placing personal blame on workers instead of fixing faulty system/process designs.

**[Variant B]**

Stopping at intermediate symptoms, subjectivity

## When NOT to Use

**[Variant A]**

For simple, known one-off glitches where root cause is self-evident without investigation.

**[Variant B]**

The problem is obvious and needs an immediate fix

## Alternatives & Complementary Methods

**[Variant A]**

Complemented by Process Analysis, Fishbone Diagram, 5 Whys, Failure Mode & Effects Analysis (FMEA), and SWOT Analysis.

**[Variant B]**

Business event analysis, brainstorming

## Supported Decisions

**[Variant A]**

Corrective action plan selection, process redesign priorities, quality improvement investments.

**[Variant B]**

Scope, architecture, priority

## AI & Agentic Adaptation

**[Variant A]**

AI diagnostic agents can analyze error logs and operational data to automatically trace cause-and-effect chains and present draft 5 Whys trees to analysts.

**[Variant B]**

Automatic analysis of error logs with an LLM to find root causes
