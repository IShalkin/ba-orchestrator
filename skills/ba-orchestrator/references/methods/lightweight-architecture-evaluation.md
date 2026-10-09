---
id: lightweight-architecture-evaluation
name: "Lightweight Architecture Evaluation"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Lightweight Architecture Evaluation

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

**Also described as:** Lightweight Architecture Evaluation (LAE)

## Problem Solved

Provides a low-cost, fast-turnaround peer review mechanism to detect architectural risks during iterative development.

## BA Lifecycle Phase

Validation

## Input Artifacts

Current architecture sketches/documentation, updated utility tree, recent design changes.

## Output Artifacts

List of discovered architectural risks, non-risks, sensitivities, and trade-offs.

## Participants & Roles

Lead Architect (Facilitator), Peer Developers, Testers, Internal Technical Stakeholders.

## Prerequisites

Existing architectural baseline and familiarity of participants with system context.

## Step-by-Step Procedure

Review business goals.
2. Review architecture changes.
3. Review/update quality attribute utility tree.
4. Brainstorm/select high-priority scenarios.
5. Analyze architectural approaches against scenarios.
6. Capture risks, non-risks, and action items.

## Analyst Questions & Prompts

What architectural changes were made in the recent iteration? Do these changes introduce risks for our top quality attribute scenarios?

## Minimal Realistic Example

A 2-hour peer review analyzes a new database caching layer and identifies a risk regarding stale data during concurrent writes.

## Quality Criteria & Verification

Peer consensus on identified risks and agreement on remediation actions for high-priority drivers.

## Errors & Anti-Patterns

Superficial review without probing design decisions; cognitive bias/groupthink due to lack of external perspective.

## When NOT to Use

High-risk, mission-critical systems requiring formal external validation, or initial architecture reviews of complex systems.

## Alternatives & Complementary Methods

ATAM, Tactics-Based Questionnaires, Code Reviews.

## Supported Decisions

Iteration sign-off, refactoring identification, local design adjustments.

## AI & Agentic Adaptation

Agentic systems can automatically track architecture modifications between iterations and generate targeted evaluation prompts for the peer review team.
