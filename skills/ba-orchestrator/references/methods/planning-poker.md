---
id: planning-poker
name: "Planning Poker"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.2"
subtask_name: "Backlog, Estimation and Release Planning"
source_count: 1
---

# Planning Poker

`T6 Prioritisation and Requirements Management › 6.2 Backlog, Estimation and Release Planning`

## Problem Solved

Estimates the relative size and complexity of user stories/requirements using consensus-based card voting, reducing individual estimator bias and unvetted estimates.

## BA Lifecycle Phase

Define Requirements / Elicitation / Analysis / Prioritisation

## Input Artifacts

User stories, Acceptance Criteria, baseline estimation unit.

## Output Artifacts

Agreed Story Point estimates per user story.

## Participants & Roles

Moderator/BA, Estimating Team (Developers, Testers, Designers), Product Owner.

## Prerequisites

Selected user stories with clear descriptions and acceptance criteria; decks of planning poker cards (Fibonacci sequence: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100).

## Step-by-Step Procedure

Moderator presents user story.
2. Team discusses requirement to clarify scope.
3. Each estimator privately selects a numbered card.
4. All cards revealed simultaneously.
5. High and low estimators explain their reasoning.
6. Group discusses insights (e.g. reusability, hidden complexity).
7. Re-vote until consensus is reached.

## Analyst Questions & Prompts

How complex is this story compared to our baseline? Why did you pick a 13 while others picked a 3? What hidden technical or business tasks exist?

## Minimal Realistic Example

A team plays Planning Poker for a payment story: initial votes range 2 to 8. Discussion reveals reusable code exists, leading to a second-round consensus estimate of 5 story points.

## Quality Criteria & Verification

Achieved through true team consensus and open dialogue rather than forced voting or manager imposition.

## Errors & Anti-Patterns

Converting story points directly into fixed developer hours; forcing a vote majority instead of consensus; allowing senior leads to dominate initial card selection.

## When NOT to Use

When well-understood, routine repetitive tasks with historical precise time data are being estimated.

## Alternatives & Complementary Methods

Wideband Delphi, Expert Judgment, Function Point Analysis.

## Supported Decisions

Iteration scope selection, velocity planning, release schedule estimating.

## AI & Agentic Adaptation

Estimation AI analyzes historical team velocity and past story complexity to offer baseline story point suggestions during poker sessions.
