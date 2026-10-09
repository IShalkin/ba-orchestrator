---
id: textual-process-descriptions-mini-specs
name: "Textual Process Descriptions (Mini-Specs)"
task: T5
task_name: "Requirements Specification"
subtask: "5.4"
subtask_name: "Business Rules and Decision Logic"
source_count: 1
---

# Textual Process Descriptions (Mini-Specs)

`T5 Requirements Specification › 5.4 Business Rules and Decision Logic`

**Also described as:** Textual Process Descriptions (Mini-Specs / Pseudo-Code)

## Problem Solved

Provides precise algorithmic specifications for semi-complex functions, buttons, or methods where developer guessing is risky.

## BA Lifecycle Phase

specification

## Input Artifacts

UI prototypes, event lists, decision tables, data dictionary.

## Output Artifacts

Textual mini-specifications / pseudo-code detailing Input, Entry State, State Changes, and Output.

## Participants & Roles

BA, developer, tester.

## Prerequisites

Selected UI screens or defined product-level functions.

## Step-by-Step Procedure

Identify non-trivial product functions or UI event buttons.
2. Specify input parameters and explicit/implicit entry state conditions.
3. Write algorithmic steps detailing state changes (database updates).
4. Specify output parameters or screen state updates.
5. Review pseudo-code with developers for clarity.

## Analyst Questions & Prompts

What entry state is required before this function runs? What exact database updates occur step-by-step?

## Minimal Realistic Example

Function Checkin(CurrentStay, CurrentRooms): If CurrentStay is booked, record rooms as occupied. If guest not recorded, check data complete, record guest.

## Quality Criteria & Verification

Developer code review, unit test execution against algorithm steps.

## Errors & Anti-Patterns

Over-specifying obvious, trivial functions (e.g., standard field entry); attempting to specify mathematically impossible or expert-level algorithms.

## When NOT to Use

Trivial CRUD functions or highly complex expert-level algorithms (e.g., 3D graphics rendering).

## Alternatives & Complementary Methods

Decision Tables, Activity Diagrams, Sequence Diagrams.

## Supported Decisions

Detailed program logic design, unit test case creation.

## AI & Agentic Adaptation

Translate pseudo-code specifications directly into candidate programming code blocks or test scripts.
