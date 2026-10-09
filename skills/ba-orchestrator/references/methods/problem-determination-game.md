---
id: problem-determination-game
name: "Problem Determination Game"
task: T2
task_name: "Situation Investigation and Elicitation"
subtask: "2.1"
subtask_name: "Problem and Scope Framing"
source_count: 1
---

# Problem Determination Game

`T2 Situation Investigation and Elicitation › 2.1 Problem and Scope Framing`

**Also described as:** The Problem Determination Game

## Problem Solved

Resolves multi-stakeholder conflicts, reduces noisy symptom lists, eliminates out-of-scope/unowned requests, and isolates the single real business problem to solve.

## BA Lifecycle Phase

Analysis / Discovery

## Input Artifacts

Unfiltered list of stakeholder complaints, change requests, and candidate problem statements.

## Output Artifacts

A single validated real problem statement, lists of out-of-scope issues, identified risks, and implied requirements.

## Participants & Roles

Business Analysts (facilitators/analysts), Problem Owner, Key Stakeholders.

## Prerequisites

Collection of multiple candidate problem statements from diverse business constituents.

## Step-by-Step Procedure

Step 1: Gather all candidate problem statements from stakeholders and brainstormed lists.
2. Step 2: Filter out problem candidates that are out of scope (issues no one in the project can fix).
3. Step 3: Filter out candidates not owned by the target business unit paying for/authorizing the solution.
4. Step 4: Filter out non-relevant candidates (future 'if' scenarios or temporary conditions; move them to the risk list).
5. Step 5: Distinguish problems from requirements/constraints (eliminate items with only one possible solution).
6. Step 6: Distinguish problems from symptoms by systematically comparing remaining candidates to see if solving one completely eliminates others.
7. Conclude with a single real problem statement or present mutually exclusive alternatives to management.

## Analyst Questions & Prompts

• Can anyone involved with the project do anything about this problem?
• Is the problem owner within our target business organization?
• Are you currently having this problem today?
• Can anyone identify more than one solution to this issue?
• When the problem identified in Statement A is solved, do Statements B, C, or D go away?

## Minimal Realistic Example

Faced with 12 complaints (e.g., 'too much overtime', 'broken monitors', 'inaccurate payment calculations', 'high turnover'), the analyst filters out broken monitors (IT owned) and overtime budget (future risk), leaving 'inflexible vendor database terms' as the sole problem whose resolution clears all remaining symptom complaints.

## Quality Criteria & Verification

The process must yield a single problem statement (or mutually exclusive set) stated in negative/constraining terms, stripped of pre-determined solutions, and verified to cause the listed secondary symptoms.

## Errors & Anti-Patterns

Selecting the problem definition based on executive hierarchy rather than systematic filtering; combining multiple unrelated problems using conjunctions ('and') instead of isolating the core problem.

## When NOT to Use

When there is already a single, clear, uncontested, and fully validated problem statement established.

## Alternatives & Complementary Methods

Five Whys, Root Cause Analysis, Pareto Analysis, Context-Free Questions.

## Supported Decisions

Project initiation, problem prioritization, product scope definition, business case development.

## AI & Agentic Adaptation

An agentic system can parse a repository of change requests, apply thematic clustering and dependency mapping to cross-reference items, and highlight potential root causes versus symptoms. Human analyst review is mandatory for final sign-off.
