---
id: moscow
name: "MoSCoW"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.1"
subtask_name: "Prioritisation"
source_count: 1
---

# MoSCoW

`T6 Prioritisation and Requirements Management › 6.1 Prioritisation`

**Also described as:** MoSCoW prioritisation

## Problem Solved

Categorizes requirements into Must have, Should have, Could have, and Want to have (WONT) based on clear definitions, enabling flexible scope management during fixed timeboxes.

## BA Lifecycle Phase

Define Requirements / Requirements Analysis / Prioritisation

## Input Artifacts

Requirements Catalogue, User Stories, Timebox constraints.

## Output Artifacts

Prioritised Requirements List categorized by M, S, C, and W.

## Participants & Roles

BA (Facilitator), Sponsor, Business Owner, Users, Developers.

## Prerequisites

Decomposed requirements defined in sufficient detail.

## Step-by-Step Procedure

Define MoSCoW rules clearly to stakeholders.
2. Evaluate 'Must haves' (M - critical minimum usable subset, guaranteed).
3. Evaluate 'Should haves' (S - important, short-term workaround exists).
4. Evaluate 'Could haves' (C - desirable, easily dropped).
5. Evaluate 'Want to have but WONT get this time' (W - valuable, deferred to future releases).
6. Ensure 'Must haves' do not exceed ~60% of total effort.

## Analyst Questions & Prompts

Is the system unusable without this (Must)? Is there a manual workaround for this (Should)? Can this be easily left out without major pain (Could)? Can this wait for a later release (WONT)?

## Minimal Realistic Example

Prioritizing bank balance features: 'View balance' (Must), 'Up-to-date daily transactions' (Should), 'View in Euros' (Could), 'Multi-language views' (WONT).

## Quality Criteria & Verification

'Must haves' comprise <=60% of total effort; unambiguous categorization backed by clear business criteria; agreement from all key stakeholders.

## Errors & Anti-Patterns

Classifying >80% of requirements as 'Must have'; treating 'Should haves' as optional fluff; prioritizing high-level undecomposed requirements.

## When NOT to Use

When prioritizing a tiny list of 2 items where simple binary ranking is sufficient.

## Alternatives & Complementary Methods

Timeboxing, Product Backlog, Planning Poker, Weighted Scoring.

## Supported Decisions

Release scope selection, timebox scope flexing, trade-off analysis.

## AI & Agentic Adaptation

Prioritization AI analyzes requirement descriptions against business goals and historical timebox velocity to suggest candidate MoSCoW tags.
