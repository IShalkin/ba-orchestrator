---
id: five-whys
name: "Five Whys"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.2"
subtask_name: "Root Cause Analysis"
source_count: 1
---

# Five Whys

`T2 Situation Investigation and Elicitation › 2.2 Root Cause Analysis`

**Also described as:** The Five Whys Technique

## Problem Solved

Distinguishes superficial symptoms from underlying root causes during business problem investigation.

## BA Lifecycle Phase

Analysis / Elicitation

## Input Artifacts

Initial complaint, defect report, or stated operational symptom.

## Output Artifacts

Root cause statement, refined problem domain description.

## Participants & Roles

Business Analyst (investigator), Process Worker, SME, Problem Owner.

## Prerequisites

An initial reported operational issue or complaint from a process worker or stakeholder.

## Step-by-Step Procedure

Identify the specific symptom or problem voiced by the stakeholder.
2. Ask why the symptom occurs or why it is considered a problem.
3. Take the response and ask 'Why?' again in relation to that response.
4. Repeat the process iteratively (typically up to five times).
5. Stop when the underlying root cause is revealed or when the stakeholder can no longer provide deeper operational cause information.
6. Validate the identified root cause against business facts.

## Analyst Questions & Prompts

• Why does stated symptom/issue happen?
• Why do you think that is a problem?
• Why does it take too long / fail at that step?
• How do you know that this condition occurs?

## Minimal Realistic Example

A clerk states: 'Voucher entry takes too long.' Analyst asks why. Clerk: 'I have to work overtime.' Analyst asks why. Clerk: 'Because I can't enter vendor terms automatically.' Analyst asks why. Clerk: 'The current database doesn't support variant vendor payment terms.' (Root cause identified).

## Quality Criteria & Verification

The final identified cause, when addressed, must logically eliminate or significantly diminish all preceding reported symptoms.

## Errors & Anti-Patterns

Phraming 'Why?' accusatorily so the stakeholder feels challenged; continuing to ask 'Why?' after reaching a respondent's boundary of knowledge leading to cyclical or absurd answers.

## When NOT to Use

When the respondent lacks direct operational knowledge of the broader process domain, or when the problem is purely technical/structural and requires automated diagnostic logging.

## Alternatives & Complementary Methods

Fishbone (Ishikawa) Diagram, Root Cause Analysis, Problem Determination Game, Context-Free Questions.

## Supported Decisions

Root cause confirmation, scope boundary decisions, solution feature prioritization.

## AI & Agentic Adaptation

Agentic LLMs can iteratively prompt users with dynamic 'Why' questions based on textual analysis of previous answers, automatically tagging potential root causes in an issue-tracking system. Guardrails must prevent loop traps when user answers become circular.
