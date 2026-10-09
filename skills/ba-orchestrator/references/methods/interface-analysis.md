---
id: interface-analysis
name: "Interface Analysis"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.5"
subtask_name: "Decomposition and Systems Analysis"
source_count: 1
---

# Interface Analysis

`T4 Modelling and Analysis › 4.5 Decomposition and Systems Analysis`

## Problem Solved

Reduces system integration failures and missing requirements by identifying where, what, why, when, how, and for whom data/messages are exchanged across solution boundaries.

## BA Lifecycle Phase

analysis / specification / architecture

## Input Artifacts

Context diagrams, solution scope models, existing system specs, stakeholder requirements.

## Output Artifacts

Interface specs (inputs, outputs, validation rules, message formats, triggers, communication frequency).

## Participants & Roles

BA, Systems Architect, Developer, SME, External Vendor/Regulator.

## Prerequisites

Identification of connecting solution components, hardware, external systems, or user roles.

## Step-by-Step Procedure

Identify all potential interfaces (user, external system, hardware, API, business process) using context diagrams.
2. For each interface, clarify the purpose (why) and participants (who/what).
3. Define message content (what information is exchanged) and volume.
4. Specify timing, event triggers, and frequency of data exchange (when).
5. Define exchange mechanism, protocol, and message format (how).
6. Specify input/output validation rules and exception handling flows.

## Analyst Questions & Prompts

"What data must be passed across this boundary?", "What event triggers the interface exchange?", "What happens if the receiving system fails to respond?"

## Minimal Realistic Example

Interface spec defines an API connecting Web Portal to Payment Gateway: sends 'Order ID + Amount' via HTTPS POST on 'Checkout Click'; expects 'Success/Fail Code' within 2 seconds.

## Quality Criteria & Verification

Interface inputs and outputs are explicitly defined; validation and error/exception paths are fully specified.

## Errors & Anti-Patterns

Focusing solely on happy-path data exchange while omitting error/timeout handling; defining technical implementation details prematurely.

## When NOT to Use

When analyzing standalone monolithic applications with zero external connections, human workflows, or hardware interactions.

## Alternatives & Complementary Methods

Complemented by Context Diagrams, Data Flow Diagrams, Sequence Diagrams, and Use Cases.

## Supported Decisions

System architecture allocation, vendor integration scope, non-functional performance design.

## AI & Agentic Adaptation

AI agents can analyze API schemas (e.g., OpenAPI specs) and UI wireframes to auto-generate structured interface mappings and edge-case validation rules.
