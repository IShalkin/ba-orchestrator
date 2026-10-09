---
id: the-3-cs-card-conversation-confirmation
name: "The 3 Cs (Card, Conversation, Confirmation)"
task: T5
task_name: "Requirements Specification"
subtask: "5.1"
subtask_name: "User Stories and Story Mapping"
source_count: 1
---

# The 3 Cs (Card, Conversation, Confirmation)

`T5 Requirements Specification › 5.1 User Stories and Story Mapping`

## Problem Solved

Eliminates rigid, misinterpreted requirement documents by replacing them with collaborative discussions and explicit verification criteria.

## BA Lifecycle Phase

Elicitation / analysis / specification / validation

## Input Artifacts

User task/feature concept, persona context, business rules.

## Output Artifacts

Story card (title + short description), vacation photos (whiteboard drawings/sketches/notes), acceptance criteria (bulleted confirmation list).

## Participants & Roles

Product Owner / BA / UX Designer (representing value/usability), Developer (representing feasibility), Tester (representing edge cases and validation).

## Prerequisites

Identified backlog item or user task.

## Step-by-Step Procedure

Card: Write a brief title and description (Who, What, Why) on a physical card/note.
2. Conversation: Hold face-to-face/interactive discussion supported by sketches, personas, and examples to build shared understanding.
3. Confirmation: Agree on bulleted acceptance criteria and demonstration steps that prove the story is completed.

## Analyst Questions & Prompts

"As a type of user, I want to do something, so that get benefit?", "What will we check to see that we are done?", "How will we demonstrate this feature at product review?", "What about when things go wrong?"

## Minimal Realistic Example

Card: 'Upload promo image'. Conversation: Discussion between developer, BA, and tester reveals images could come from local drive or Flickr. Confirmation: '1. User can select PNG/JPG up to 5MB.
2. Preview displays instantly.
3. Errors shown for unsupported formats.'

## Quality Criteria & Verification

Shared mental model among participants; explicit testable acceptance criteria; confirmation tests passing upon software construction.

## Errors & Anti-Patterns

Treating the card as a standalone mini-spec document; skipping the conversation; 'Template Zombies' forcing every card into rigid text without dialogue; using the card catalog token as the entire requirement.

## When NOT to Use

Contractual fixed-price handoffs where direct conversation between builders and requestors is legally prohibited or impossible.

## Alternatives & Complementary Methods

Use Cases, Behavior-Driven Development (BDD), Specification by Example, Acceptance Test-Driven Development (ATDD).

## Supported Decisions

Definition of done, release readiness for individual stories, test case approval.

## AI & Agentic Adaptation

Not in source
