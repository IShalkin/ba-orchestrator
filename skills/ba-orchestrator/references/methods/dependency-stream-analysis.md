---
id: dependency-stream-analysis
name: "Dependency Stream Analysis"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.2"
subtask_name: "Backlog, Estimation and Release Planning"
source_count: 1
---

# Dependency Stream Analysis

`T6 Prioritisation and Requirements Management › 6.2 Backlog, Estimation and Release Planning`

**Also described as:** Business Function Packaging & Dependency Stream Analysis

## Problem Solved

Reduces information overload in large models (>30 use cases) and clarifies cross-use-case workflow dependencies.

## BA Lifecycle Phase

Analysis / prioritisation / change management

## Input Artifacts

Base/Elaborated Use Cases, Preconditions, Postconditions.

## Output Artifacts

Business Function Packages, Dependency Stream Diagrams (Activity/State diagrams).

## Participants & Roles

BA/System Analyst, Architect, Project Manager.

## Prerequisites

Large set of initial/base use cases identified.

## Step-by-Step Procedure

Group related use cases into functional packages (e.g., Loan Origination, Billing, Portfolio Management).
2. Analyze preconditions and postconditions of use cases across packages.
3. Link use cases into sequential Dependency Streams where Postcondition(UC A) = Precondition(UC B).
4. Map dependency streams using Activity Diagrams to visualize end-to-end business workflows.
5. Identify missing use cases where preconditions do not match any existing postcondition.

## Analyst Questions & Prompts

Which use case must execute before this one can start? What functional package does this belong to?

## Minimal Realistic Example

'Submit Loan Request' -> 'Validate References' -> 'Evaluate Loan Request' -> 'Book New Loan' form a continuous Dependency Stream.

## Quality Criteria & Verification

Validation that all dependency preconditions are satisfied by prior postconditions; logical completeness of end-to-end work flows.

## Errors & Anti-Patterns

Creating artificial circular dependencies or forcing non-dependent use cases into strict linear sequences.

## When NOT to Use

Small systems with fewer than 10 straightforward, independent use cases.

## Alternatives & Complementary Methods

Superordinate/Subordinate Use Cases, Business Process Modeling Notation (BPMN).

## Supported Decisions

Release planning, iterative increment scheduling, subsystem partitioning.

## AI & Agentic Adaptation

Not specified in source.
