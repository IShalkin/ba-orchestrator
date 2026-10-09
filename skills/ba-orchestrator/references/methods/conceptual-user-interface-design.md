---
id: conceptual-user-interface-design
name: "Conceptual User Interface Design"
task: T5
task_name: "Requirements Specification"
subtask: "5.3"
subtask_name: "User Interface"
source_count: 1
---

# Conceptual User Interface Design

`T5 Requirements Specification › 5.3 User Interface`

**Also described as:** Conceptual User Interface Design (Transaction-Based)

## Problem Solved

Reduces premature GUI design lock-in, unaligned user mental models, and missing screen information elements.

## BA Lifecycle Phase

Analysis / specification

## Input Artifacts

Elaborated Use Cases, Analysis Object Model, Actor Glossary.

## Output Artifacts

User Interface Specification, Transaction Information Model, Logical Screen Layouts/Order.

## Participants & Roles

BA/System Analyst, UI/UX Designer, SME, End User.

## Prerequisites

Elaborated use cases with detailed interaction flows available.

## Step-by-Step Procedure

Partition use case model by Work Model (functional areas) or User Groups (roles/privileges).
2. Decompose use cases into discrete User Interface Transactions (System presents info -> User acts).
3. Determine precise information content for each transaction (attributes, operations, state, objects, relationships).
4. Establish logical screen ordering and consolidate similar transactions into single logical screens.
5. Map logical screens to physical UI prototypes.

## Analyst Questions & Prompts

What information does the user need to make this decision? What data is returned to the system?

## Minimal Realistic Example

Transaction UC130-2 presents Applicant Name, SSN, Credit Score, and History; accepts Loan Approval/Denial decision input.

## Quality Criteria & Verification

User walkthroughs of logical screen flows, usability prototype testing, traceability to use case transactions.

## Errors & Anti-Patterns

Arguing over physical GUI widgets (button placement, colors) during essential business requirements definition.

## When NOT to Use

Headless batch systems, back-end APIs, or systems without human user interfaces.

## Alternatives & Complementary Methods

Essential Use Case UI Modeling, Storyboarding, Wireframing.

## Supported Decisions

UI architecture, screen layout, user experience design approval.

## AI & Agentic Adaptation

Not specified in source.
