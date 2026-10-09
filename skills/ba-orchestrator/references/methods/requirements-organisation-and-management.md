---
id: requirements-organisation-and-management
name: "Requirements Organisation and Management"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.3"
subtask_name: "Organisation, Baselines and Reuse"
source_count: 2
---

# Requirements Organisation and Management

`T6 Prioritisation and Requirements Management › 6.3 Organisation, Baselines and Reuse`

**Also described as:** Requirements management; Requirements organisation

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Structures, clusters, and links large sets of requirements, and resolves conflicting stakeholder requirements, reducing unmanageable, contradictory specifications.

**[Variant B]**

Applies configuration control, version numbering, baseline management, and formal change control to requirements, preventing scope creep and un-tracked modifications.

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Requirements Analysis

**[Variant B]**

Define Requirements / Requirements Management / Change Control

## Input Artifacts

**[Variant A]**

Raw elicited requirements list, stakeholder lists, domain maps.

**[Variant B]**

Requirements Catalogue, Change Requests, Baseline specifications, Traceability Matrix.

## Output Artifacts

**[Variant A]**

Structured Requirements Specification (clustered by Functional, Non-functional, General, Technical), documented requirement links, negotiated conflict agreements.

**[Variant B]**

Requirements Management Plan, Version-controlled Requirements Catalogue, Change Control Logs, Baseline Audit Trail.

## Participants & Roles

**[Variant A]**

BA, Sponsor, Stakeholders, Technical Leads.

**[Variant B]**

BA, Change Control Board / Approval Authority, Project Manager, Librarian.

## Prerequisites

**[Variant A]**

Elicited list of candidate requirements.

**[Variant B]**

Formal baselining of the initial requirements specification.

## Step-by-Step Procedure

**[Variant A]**

Cluster requirements into high-level groups (Functional, Non-functional, General, Technical).
2. Sub-group into lower-level categories (by business process, non-functional type, etc.).
3. Document links and dependencies between requirements.
4. Perform hierarchical decomposition.
5. Identify conflicting requirements.
6. Conduct 3-step negotiation (Discussion, Prioritisation, Agreement).

**[Variant B]**

Establish configuration identification rules (naming, version numbering, item levels).
2. Formally baseline the requirements set.
3. Place items in a controlled repository/library.
4. Process new Change Requests via 4 steps: Document request, Assess impact/cost/effort, Review by approval authority (Approve/Reject/Defer), Implement and update version numbers.

## Analyst Questions & Prompts

**[Variant A]**

Which category does this requirement belong to? What other requirements depend on this? How can we resolve the contradiction between User A and User B's requests?

**[Variant B]**

What version of the requirement is this? Has the baseline been formally established? What is the cost/effort impact of this proposed change? Was this change approved by the Change Board?

## Minimal Realistic Example

**[Variant A]**

Structuring 200 raw requirements into Functional (by booking process) and Non-functional (Performance/Security), resolving a conflict between open access vs tight security via role-based rules.

**[Variant B]**

A user requests a new report post-baseline: the BA logs Change Request CR-012, performs impact analysis (£5k cost, 3-day delay), the Change Board approves it, and the catalogue version advances to v2.1.

## Quality Criteria & Verification

**[Variant A]**

Logical partitioning; explicit dependency linking; complete resolution of conflicting requirements through consensus.

**[Variant B]**

Complete audit trail for every change; all stakeholders working to the identical current baseline version; zero unauthorized scope additions.

## Errors & Anti-Patterns

**[Variant A]**

Leaving requirements as an un-categorized flat list of 500 items; ignoring conflicts until technical build starts; mixing non-functional constraints inside functional requirements.

**[Variant B]**

Allowing informal 'off-the-record' scope changes without impact analysis; failing to baseline requirements; allowing developers to work from outdated document versions.

## When NOT to Use

**[Variant A]**

In micro-projects with under 10 straightforward requirements.

**[Variant B]**

During early discovery/elicitation before an initial baseline has been established.

## Alternatives & Complementary Methods

**[Variant A]**

Requirements Catalogue, MoSCoW Prioritisation, CRUD Matrix, Traceability Matrix.

**[Variant B]**

Configuration Management, Traceability Matrix, Change Control Board.

## Supported Decisions

**[Variant A]**

Requirements specification baseline, release packaging, conflict resolution.

**[Variant B]**

Change request approval/rejection/deferral, baseline release scope definition.

## AI & Agentic Adaptation

**[Variant A]**

Clustering AI parses unstructured requirement lists, automatically categorizing them into Functional/Non-functional buckets and flagging conflicting statements.

**[Variant B]**

Requirements management AI tools automatically track requirement edits, link change requests to impacted design modules, and assess downstream cost/schedule impacts.
