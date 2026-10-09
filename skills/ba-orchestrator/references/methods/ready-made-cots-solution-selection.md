---
id: ready-made-cots-solution-selection
name: "Ready-Made / COTS Solution Selection"
task: T1
task_name: "Strategy Analysis and Justification"
subtask: "1.4"
subtask_name: "Solution Options and Feasibility"
source_count: 2
---

# Ready-Made / COTS Solution Selection

`T1 Strategy Analysis and Justification › 1.4 Solution Options and Feasibility`

**Also described as:** COTS Package Selection & Evaluation Matrix; Ready-Made (Off-The-Shelf) Solution Evaluation & RFP

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Prevents organizations from buying ready-made software that fails to fit their business processes, or incurring unexpected, massive customization costs.

**[Variant B]**

Prevents acquiring expensive packaged software that fails to meet business needs, exhibits data model disconnects, or requires excessive custom extension.

## BA Lifecycle Phase

**[Variant A]**

Analysis

**[Variant B]**

elicitation

## Input Artifacts

**[Variant A]**

Work Context Diagram, Business Event List, Data Dictionary, Non-Functional Requirements, Constraints.

**[Variant B]**

Business requirements, user stories/use cases, business rules, quality attributes, vendor RFPs / product literature

## Output Artifacts

**[Variant A]**

Request for Proposal (RFP) / Request for Information (RFI), Vendor Evaluation Matrix/Scoring Sheet, Fit-Gap Analysis, Purpose-Based Alignment Quadrant.

**[Variant B]**

Weighted COTS Evaluation Matrix (rows = weighted requirements, columns = candidate COTS packages, cells = scores/match comments)

## Participants & Roles

**[Variant A]**

Business Analyst, Product Owner, System Architect, Procurement/Legal Lead, Vendor Representatives.

**[Variant B]**

BA, Procurement/Legal, Business SMEs, IT Architect, Vendor Representatives

## Prerequisites

**[Variant A]**

Defined work context, clear data definitions, and prioritized business events.

**[Variant B]**

Defined and prioritized user requirements and business objectives.

## Step-by-Step Procedure

**[Variant A]**

Define the work scope context diagram and data dictionary for the problem space.
2. Compile an RFP containing context models, business event list, expected outcomes, and key non-functional constraints.
3. Issue RFP / RFI to candidate vendors or download open-source candidates.
4. Evaluate responses by mapping ready-made capabilities against business event outcomes.
5. Score fit (4=out-of-the-box, 3=configured, 2=minor customization, 1=major customization, 0=no fit).
6. Apply Purpose-Based Alignment Model to decide whether to Configure, Customize, or adapt the Organization.
7. Select the optimal ready-made solution.

**[Variant B]**

Identify candidate COTS/SaaS packages through initial market research.
2. Compile evaluation criteria based on prioritized use cases, business rules, data structures, and quality attributes.
3. Assign relative weightings (1-10) to evaluation criteria based on business importance.
4. Rate candidates (1.0 = full fit, 0.5 = partial fit/workaround, 0 = no fit) via literature, RFP responses, and direct hands-on testing.
5. Calculate weighted evaluation scores for each product.
6. Evaluate vendor viability, licensing/cloud costs, integration hooks, and required custom extensions.
7. Select the optimal package or conduct a multi-stage pilot evaluation.

## Analyst Questions & Prompts

**[Variant A]**

"Does this ready-made produce the required outcome for this business event out-of-the-box?", "How much configuration vs customization is required?", "Is this business event a market differentiator (warranting customization) or parity (warranting configuration)?", "Will this ready-made take us out of the vendor's upgrade path?"

**[Variant B]**

Does this package satisfy our non-negotiable business rules out of the box? What custom adapters or extensions will be required? How easily can standard reports be customized?

## Minimal Realistic Example

**[Variant A]**

Evaluating a ready-made Warehouse Management System against 11 business events, scoring each event's outcome fit, and using Purpose-Based Alignment to decide to configure standard picking flows while customizing unique packaging rules.

**[Variant B]**

Evaluating 16 Requirements Management Tools against 200 weighted features using a matrix, revealing that batch Excel import is supported out-of-the-box (1.0) while visual diagramming requires a workaround (0.5).

## Quality Criteria & Verification

**[Variant A]**

RFP based on essential outcomes rather than rigid technical solution specs; vendor scoring incorporates full lifecycle integration and disruption costs; clear decision on configure vs customize.

**[Variant B]**

Validation of vendor claims using hands-on scenario scripts on real project data; consistent evaluation scoring overseen by a core review team.

## Errors & Anti-Patterns

**[Variant A]**

Buying an off-the-shelf system before understanding the business scope; over-customizing ready-made code until future upgrades become impossible; ignoring organizational change/disruption costs.

**[Variant B]**

Selecting COTS packages based solely on vendor sales pitches; forcing custom development requirements into non-configurable COTS architectures; treating all evaluation criteria as equally weighted.

## When NOT to Use

**[Variant A]**

Building 100% custom, highly proprietary core IP algorithms with zero commercial software equivalents.

**[Variant B]**

When custom software development is already mandated or when purchasing minor, low-cost utility tools.

## Alternatives & Complementary Methods

**[Variant A]**

Custom Build vs Buy Analysis, Proof of Concept Spikes, Purpose-Based Alignment Modeling.

**[Variant B]**

RFP (Request for Proposal), Operational Profile Scenario Testing, Gap Analysis.

## Supported Decisions

**[Variant A]**

Software procurement, Build vs Buy vs Borrow decisions, vendor selection, customization budget approval.

**[Variant B]**

Procurement/Buy vs. Build, vendor selection, architecture, scope.

## AI & Agentic Adaptation

**[Variant A]**

AI procurement agents can ingest vendor RFP responses and automatically cross-reference them against requirements specifications, generating initial fit-gap scores and highlighting compliance risks for human BA review.

**[Variant B]**

Not in source
