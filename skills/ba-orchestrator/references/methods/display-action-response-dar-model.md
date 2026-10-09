---
id: display-action-response-dar-model
name: "Display-Action-Response (DAR) Model"
task: T5
task_name: "Requirements Specification"
subtask: "5.3"
subtask_name: "User Interface"
source_count: 1
---

# Display-Action-Response (DAR) Model

`T5 Requirements Specification › 5.3 User Interface`

## Problem Solved

Bridges user interface layout design with backend interactive behavior, preventing ambiguous screen requirements for complex or outsourced UI development.

## BA Lifecycle Phase

specification

## Input Artifacts

UI wireframes/mock-ups, use cases, business rules, data dictionary entries

## Output Artifacts

DAR Specification (Visual Screen Mock-up + UI Element Description Table + UI Element Behaviors Table with Preconditions, User Actions, and System Responses)

## Participants & Roles

BA, UI/UX Designer, Developers (especially outsourced/offshore), Testers

## Prerequisites

High-fidelity or low-fidelity mock-up of a screen display.

## Step-by-Step Procedure

Capture or draw the visual layout mock-up of the screen.
2. Assign a unique Screen ID and brief functional description.
3. Create the 'UI Element Description Table' listing preconditions and all visible screen widgets/controls.
4. Create the 'UI Element Behaviors Table'.
5. For each element, map Preconditions + User Action (e.g., click, type, select) -> Detailed System Response (e.g., error alert, data submission, navigation).
6. Verify that all exception scenarios and input validation behaviors are detailed.

## Analyst Questions & Prompts

What elements appear on this screen under Precondition X versus Precondition Y? What exact system response occurs when the user clicks Button Z with invalid field entries?

## Minimal Realistic Example

DAR Model for 'Submit a Pearl Page' specifying field controls, character counter behaviors, check box toggles, and error alert displays when required fields are left blank.

## Quality Criteria & Verification

Complete mapping of all screen widgets to explicit behavior entries; review by remote developers to ensure zero unstated assumptions; test script generation directly from the DAR table.

## Errors & Anti-Patterns

Documenting screen visuals without defining interactive behaviors; omitting exception responses for invalid user inputs.

## When NOT to Use

For non-interactive batch processes or simple static display pages.

## Alternatives & Complementary Methods

Dialog Map, UI Prototype, Wireframe, Use Case Specification.

## Supported Decisions

UI design, architecture, acceptance, release.

## AI & Agentic Adaptation

Not in source
