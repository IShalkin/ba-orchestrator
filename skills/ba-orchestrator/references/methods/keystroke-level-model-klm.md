---
id: keystroke-level-model-klm
name: "Keystroke-Level Model (KLM)"
task: T5
task_name: "Requirements Specification"
subtask: "5.3"
subtask_name: "User Interface"
source_count: 1
---

# Keystroke-Level Model (KLM)

`T5 Requirements Specification › 5.3 User Interface`

## Problem Solved

Predicts and calculates the exact task execution time for experienced users on a computer interface without requiring user testing.

## BA Lifecycle Phase

analysis

## Input Artifacts

UI prototypes/screens, standard execution operators (Keystroke, Pointing, Homing, Mental preparation, System response).

## Output Artifacts

Calculated task execution time predictions.

## Participants & Roles

BA, UI designer, developer.

## Prerequisites

Defined UI interaction sequence for an experienced user.

## Step-by-Step Procedure

Break down the user's task interaction into standard primitive operators (K, P, H, M, R).
2. Assign standard time constants to each operator (e.g., K=0.2s, M=1.35s, H=0.4s).
3. Sum the operator times for the complete task sequence.
4. Add non-overlapped system response time (R).
5. Compare calculated times against usability efficiency targets.

## Analyst Questions & Prompts

How many keystrokes and mouse movements are required to complete this daily entry? Where do mental pauses occur?

## Minimal Realistic Example

Calculating 100 room entries: (3 Keystrokes × 0.3s + 1 Mental × 1.35s + 0.35s Response) × 100 = 260 seconds (4.3 minutes).

## Quality Criteria & Verification

Mathematical validation against standard KLM time tables.

## Errors & Anti-Patterns

Failing to account for mental preparation pauses (M=1.35s) or non-overlapped system response delays.

## When NOT to Use

Predicting learnability for novice users who do not follow predictable expert keystroke paths.

## Alternatives & Complementary Methods

Usability Testing (Task Time), Usability Requirements (Keystroke Counts).

## Supported Decisions

UI layout optimization, comparison of candidate UI designs for high-frequency tasks.

## AI & Agentic Adaptation

Auto-calculate KLM execution times for proposed screen workflows directly from wireframe UI models using AI scripts.
