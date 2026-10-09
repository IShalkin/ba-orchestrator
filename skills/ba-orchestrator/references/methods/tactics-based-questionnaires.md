---
id: tactics-based-questionnaires
name: "Tactics-Based Questionnaires"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Tactics-Based Questionnaires

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

## Problem Solved

Rapidly identifies missing architectural mechanisms and design risks for a specific quality attribute.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Architecture design, code base locations, quality attribute specific tactics questionnaire.

## Output Artifacts

Completed tactics questionnaire documenting support status (Y/N), design locations, risk levels (H/M/L), and rationale.

## Participants & Roles

Software Architect, Technical Reviewer / Analyst.

## Prerequisites

Knowledge of system design decisions related to the target quality attribute.

## Step-by-Step Procedure

Select a quality attribute tactics questionnaire.
2. For each tactic question, determine if supported (Y/N).
3. If Yes, record design decisions and location in code/design.
4. Rate implementation risk (H/M/L).
5. Document rationale and assumptions for using or omitting the tactic.

## Analyst Questions & Prompts

Does the system use ping/echo to detect failure? Does the system support data encryption in transit and at rest? Does the system use heartbeat messages?

## Minimal Realistic Example

Asking 'Does the system encrypt data in transit?' reveals that data is XOR'ed rather than encrypted using standard algorithms, highlighting a high-risk security vulnerability.

## Quality Criteria & Verification

Complete coverage of all tactics in the questionnaire; explicit documentation of locations in code/artifacts for supported tactics.

## Errors & Anti-Patterns

Answering 'Yes' without verifying physical realization in code; treating omitted tactics automatically as defects without considering rationale.

## When NOT to Use

When holistic trade-off analysis across multiple competing quality attributes is required simultaneously.

## Alternatives & Complementary Methods

ATAM, Lightweight Architecture Evaluation, Static Code Analysis.

## Supported Decisions

Selection of specific architectural tactics, identification of technical debt, security/availability auditing.

## AI & Agentic Adaptation

LLM agents can scan code repositories and architecture documentation to auto-fill draft answers for tactics questionnaires, flagging unverified tactic implementations for human review.
