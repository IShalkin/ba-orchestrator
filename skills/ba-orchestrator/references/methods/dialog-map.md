---
id: dialog-map
name: "Dialog Map"
task: T5
task_name: "Requirements Specification"
subtask: "5.3"
subtask_name: "User Interface"
source_count: 1
---

# Dialog Map

`T5 Requirements Specification › 5.3 User Interface`

## Problem Solved

Provides a high-level visual architecture of user interface display elements and screen navigation links without getting bogged down in visual screen layout details.

## BA Lifecycle Phase

analysis

## Input Artifacts

Use cases, user task flows, user class descriptions, dialog map whiteboard sketches

## Output Artifacts

Dialog Map Diagram (display states as rectangles, user actions/events as labeled transition arrows)

## Participants & Roles

BA, UI Designer, End Users, Developers, Testers

## Prerequisites

Defined use cases detailing actor actions and system responses.

## Step-by-Step Procedure

Identify all screen display elements (workspaces, menus, dialog boxes) needed for a use case.
2. Represent each screen/dialog element as a state rectangle.
3. Draw directional arrows representing allowed screen navigation pathways.
4. Label arrows with triggers (user actions, data values, or system conditions).
5. Include entry points (black circle) and exit points (encircled black circle).
6. Verify back-out and cancel options at key navigation points.

## Analyst Questions & Prompts

What display appears after taking this action? How can the user cancel or back out of this operation? What error display appears if input validation fails?

## Minimal Realistic Example

'Current Request List' screen links via 'add chemical' to 'List of Stockroom Containers' screen, which links via 'select container' back to 'Current Request List'.

## Quality Criteria & Verification

Trace use cases against the map to ensure all actions are navigable; verify absence of dead ends; review with users for intuitive task flow.

## Errors & Anti-Patterns

Including global shortcut keys (e.g., F1 Help) on every node; adding detailed layout elements like fonts and colors; omitting cancel/exit pathways.

## When NOT to Use

When designing backend processing logic or non-interactive batch systems.

## Alternatives & Complementary Methods

UML Activity Diagram, Navigation Map, UI Prototype, Wireframe, Storyboard.

## Supported Decisions

Architecture, release, acceptance.

## AI & Agentic Adaptation

Not in source
