---
id: gap-analysis
name: "Gap Analysis"
task: T1
task_name: "Strategy Analysis and Justification"
subtask: "1.3"
subtask_name: "Current State, Capabilities and Gaps"
source_count: 3
---

# Gap Analysis

`T1 Strategy Analysis and Justification › 1.3 Current State, Capabilities and Gaps`

**Also described as:** Gap Analysis for Replacement & Enhancement Systems; Gap analysis

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Compares the current 'as is' business situation with the conceptual 'to be' desired model to identify required change actions across Process, IT, People, and Organization.

**[Variant B]**

Prevents missing vital legacy functionality, carrying forward unnecessary 'junk' features, or creating operational disruptions when replacing or enhancing existing systems.

**[Variant C]**

Not understanding the difference between the current and the target state

## Uncertainty Reduced

**[Variant C]**

No bridge between 'as-is' and 'to-be'

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Change Identification

**[Variant B]**

analysis

**[Variant C]**

Analysis, strategy analysis

## Input Artifacts

**[Variant A]**

Current state models (Rich Pictures, Mind Maps, 'As Is' Process Maps), Desired state models (BAM, 'To Be' Process Maps), Scope definition.

**[Variant B]**

Existing application user interfaces/code, user feedback, change requests, business objectives, process models

**[Variant C]**

Current state description, Future state description

## Output Artifacts

**[Variant A]**

Gap Analysis Report, categorized change actions list across POPIT (Process, IT, People, Organization).

**[Variant B]**

Gap Analysis Matrix / Feature Tree (categorized into: Requirements to Replicate, Requirements to Modify, Requirements to Add, Requirements to Drop)

**[Variant C]**

Result: list of gaps, plan for closing the gaps. Artifacts: gap matrix, list of transition requirements

## Participants & Roles

**[Variant A]**

BA, Business Owner, Sponsor, Enterprise Architect, Change Manager.

**[Variant B]**

BA, Business SMEs/Users, System Architect, Developers

**[Variant C]**

BA, Architect, Sponsor, SME

## Prerequisites

**[Variant A]**

Completion of both 'as is' investigation and 'to be' conceptual modeling.

**[Variant B]**

Defined business objectives justifying the enhancement or replacement project.

## Step-by-Step Procedure

**[Variant A]**

Compare each activity in the BAM against the current situation.
2. Categorize activities: Existing & Satisfactory, Existing & Unsatisfactory, or Missing.
3. Prioritize unsatisfactory and missing activities.
4. Analyze detailed process gaps and IT support needs.
5. Map required change actions across POPIT (Process, IT, People, Organization).
6. Compile list of change actions.

**[Variant B]**

Elicit and model the 'as-is' capabilities of the existing system.
2. Analyze feature usage data to identify rarely/never used capabilities.
3. Categorize candidate requirements into four buckets: Replicate, Modify, Add (new gaps), or Drop (obsolete).
4. Trace all retained and new requirements to current business objectives.
5. Define Key Performance Indicators (KPIs) to ensure the new system maintains required user throughput.
6. Prioritize the closure of high-value gaps for implementation.

**[Variant C]**

1. Describe the current state.
2. Describe the target state.
3. Compare the models.
4. Identify the missing elements.

## Analyst Questions & Prompts

**[Variant A]**

Does this desired activity exist today? Is it done satisfactorily? What are the gaps in process, technology, staff skills, or structure? What specific actions will close this gap?

**[Variant B]**

Do you use this specific menu function today? What will happen to your process if this feature is omitted? What new capabilities must be added to achieve our new business goals?

**[Variant C]**

'What is missing in the current system to achieve the goal?'

## Minimal Realistic Example

**[Variant A]**

Comparing a desired BAM activity 'Monitor staff performance' reveals it is 'Missing' currently, generating change actions to create a new reporting process (Process), build a KPI dashboard (IT), and train team leads (People).

**[Variant B]**

Gap analysis for a fulfillment system replacement isolates Inventory Management, dropping unused legacy reports, replicating core tracking, and adding real-time vendor API integrations.

**[Variant C]**

Comparing employees' current skills with the requirements of new software

## Quality Criteria & Verification

**[Variant A]**

Holistic coverage of gaps across all 4 POPIT dimensions; clear traceability from missing/unsatisfactory activities to proposed change actions.

**[Variant B]**

Verification that all retained and new features map to business objectives; validation of KPI throughput bounds; sign-off from current business users.

**[Variant C]**

Validating the gaps with architects and the business

## Errors & Anti-Patterns

**[Variant A]**

Focusing exclusively on IT system gaps while ignoring necessary changes to staff skills, business processes, or organizational structure.

**[Variant B]**

Defaulting to 'replicate everything the old system does' without validation; gold-plating replacement systems with unneeded new features; degrading critical operational KPIs.

**[Variant C]**

Superficial comparison that ignores hidden dependencies

## When NOT to Use

**[Variant A]**

When the project is a pure technical infrastructure replacement with zero change to business processes, human roles, or organization.

**[Variant B]**

For brand new 'green-field' projects with no existing legacy system baseline.

**[Variant C]**

Building a product from scratch (there is no current state)

## Alternatives & Complementary Methods

**[Variant A]**

POPIT Model, Process Redesign Patterns, Feasibility Analysis.

**[Variant B]**

Feature Tree, KPIM (Key Performance Indicator Model), Context Diagram, CRUD Matrix.

**[Variant C]**

SWOT analysis, business architecture

## Supported Decisions

**[Variant A]**

Business case option formulation, change initiative scoping, target operating model design.

**[Variant B]**

Scope, release baseline, process change, architecture.

**[Variant C]**

Scope, architecture, release

## AI & Agentic Adaptation

**[Variant A]**

AI agents compare current process logs against target capability maps to automatically highlight operational gap areas and draft proposed change action lists.

**[Variant B]**

Not in source

**[Variant C]**

Automatically matching specifications against the codebase with AI
