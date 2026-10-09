---
id: atam
name: "ATAM"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# ATAM

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

**Also described as:** Architecture Tradeoff Analysis Method (ATAM)

## Problem Solved

Uncovers architectural risks, sensitivity points, and tradeoff points that threaten business goals before system deployment.

## BA Lifecycle Phase

Validation

## Input Artifacts

Architecture documentation, business goals presentation, quality attribute requirements.

## Output Artifacts

ATAM evaluation report containing identified risks, non-risks, sensitivity points, tradeoff points, risk themes, and refined utility tree.

## Participants & Roles

Evaluation Team (Leader, Scribe, Questioners), Project Decision Makers (Architect, Project Manager, Customer), Architecture Stakeholders (Developers, Testers, Users).

## Prerequisites

Documented or presentable software architecture and available business/technical stakeholders.

## Step-by-Step Procedure

Present ATAM.
2. Present business goals.
3. Present architecture.
4. Identify architectural approaches.
5. Generate quality attribute utility tree.
6. Analyze architectural approaches.
7. Brainstorm and prioritize scenarios with stakeholders.
8. Re-analyze architectural approaches against top brainstormed scenarios.
9. Present results and risk themes.

## Analyst Questions & Prompts

How does the architecture satisfy scenario X? Which architectural decisions affect this response? What is the impact if a component fails or load doubles?

## Minimal Realistic Example

Analyzing a switch failover scenario reveals a risk: 'No backup data channel exists', exposing a tradeoff between hardware cost reduction and 0.999999 availability.

## Quality Criteria & Verification

Traceability of risks to business goals, agreement among stakeholders on prioritized scenarios, clear justification of sensitivity and tradeoff points.

## Errors & Anti-Patterns

Evaluating without an architect present; treating evaluation as an adversarial audit; failing to convert discovered risks into actionable remediation plans.

## When NOT to Use

Very early stages before any candidate architecture exists, or on small, low-risk systems where evaluation cost exceeds system risk exposure.

## Alternatives & Complementary Methods

Lightweight Architecture Evaluation (LAE), Tactics-based Questionnaires, Peer Reviews.

## Supported Decisions

Architecture acceptance, risk mitigation planning, refactoring priorities, resource reallocation.

## AI & Agentic Adaptation

AI agents can pre-screen architecture documentation using tactics-based rules to detect potential risks and sensitivity points prior to the workshop. Human facilitation remains necessary for stakeholder consensus.
