---
id: virtual-windows
name: "Virtual Windows"
task: T5
task_name: "Requirements Specification"
subtask: "5.3"
subtask_name: "User Interface"
source_count: 1
---

# Virtual Windows

`T5 Requirements Specification › 5.3 User Interface`

## Problem Solved

Bridging the communication gap between users and developers by visually representing stored domain data without committing to UI button/menu design prematurely.

## BA Lifecycle Phase

analysis

## Input Artifacts

E/R model, task descriptions, domain entities.

## Output Artifacts

Idealized screen representations showing realistic data layout without functional controls.

## Participants & Roles

BA, UI designer, SME, end user.

## Prerequisites

Preliminary data model and list of core user tasks.

## Step-by-Step Procedure

Identify data needs for a core user task.
2. Compose a visual virtual window containing all necessary fields with realistic sample data.
3. Expand existing windows or create new ones for subsequent tasks to minimize total screen count.
4. Perform an understandability test with users to verify data clarity.
5. Cross-check data coverage against the E/R data model.

## Analyst Questions & Prompts

Does this screen show all the information you need to make this decision? Can you understand what this sample data represents?

## Minimal Realistic Example

A 'Guest Window' displaying guest contact info, stays history, current room numbers, and room rates without any action buttons.

## Quality Criteria & Verification

Early user understandability test, CRUD verification against E/R model.

## Errors & Anti-Patterns

Designing functional UI components (buttons, dropdowns) too early; spending excessive time making mockups visually pretty.

## When NOT to Use

COTS acquisitions where existing screens cannot be altered.

## Alternatives & Complementary Methods

Data Model, Screens & Prototypes, Tasks with Data.

## Supported Decisions

UI architecture, confirmation of complete domain data modeling.

## AI & Agentic Adaptation

Agentic UI generators can take entity models and task goals to synthesize candidate virtual window layouts automatically.
