---
id: requirements-baselines-and-version-control
name: "Requirements Baselines and Version Control"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.3"
subtask_name: "Organisation, Baselines and Reuse"
source_count: 2
---

# Requirements Baselines and Version Control

`T6 Prioritisation and Requirements Management › 6.3 Organisation, Baselines and Reuse`

**Also described as:** Establishing and Managing Requirements Baselines; Requirements Version Control and Baselining

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Prevents moving-target scope creep, uncontrolled schedule slippage, misaligned implementation expectations, and uncoordinated release commitments.

**[Variant B]**

Reduces miscommunication, lost changes, rework, and testing against obsolete specifications by maintaining unique identifier tracking and explicit baseline approvals.

## BA Lifecycle Phase

**[Variant A]**

Requirements Management / Release Planning

**[Variant B]**

change management / specification

## Input Artifacts

**[Variant A]**

Prioritized Backlog, SRS / Use Cases, Sizing/Effort estimates, Release Roadmap, Feature Tree.

**[Variant B]**

Draft SRS, user stories, change requests, review feedback.

## Output Artifacts

**[Variant A]**

Requirements Baseline (iteration or release baseline snapshot), Baseline Approval Record, Scope-Annotated Feature Tree / Models.

**[Variant B]**

Baselined SRS / backlog snapshot, document revision history, version-tagged requirements repository.

## Participants & Roles

**[Variant A]**

Business Analyst, Product Owner, Development Lead, QA Lead, Key Stakeholders / Approvers.

**[Variant B]**

Business Analyst (owner/lead), Project Manager, Stakeholder Approval Group / CCB, Developers, Testers.

## Prerequisites

**[Variant A]**

Prioritized and analyzed set of requirements ready for commitment.

**[Variant B]**

Completed requirements review and stakeholder agreement on a specific subset of requirements.

## Step-by-Step Procedure

**[Variant A]**

Select a baselining strategy: Time-bound (allocating prioritized items to fit a fixed timebox) or Scope-bound (defining a logical feature set and estimating schedule).
2. Uniquely identify the specific subset of requirements included in the baseline (using RM tool attributes, document versions, or backlog iteration tags).
3. Communicate scope visually using annotated Feature Trees, Context Diagrams, or Roadmaps.
4. Conduct baseline review and obtain explicit agreement/sign-off from designated approvers.
5. Establish the approved baseline as a immutable snapshot in time.
6. Enforce change control for any subsequent additions, deletions, or modifications to the baselined items.

**[Variant B]**

Uniquely identify every draft requirement or requirement document using a standardized versioning scheme (e.g., 'Version 1.0 draft 1').
2. Conduct peer review and validation on the draft requirements.
3. Upon formal approval, mark the set as a baseline (e.g., 'Version 1.0 approved') allocated to a specific release or iteration.
4. Place the baselined requirements under formal change control management.
5. Permit updates only by designated BAs following an approved change request.
6. Maintain a revision history capturing change date, author, specific changes made, and rationale.

## Analyst Questions & Prompts

**[Variant A]**

"Which subset of requirements can the team commit to delivering in this timebox?", "What would it take for you to approve this baseline?", "Are these stretch goals clearly separated from committed baseline items?"

**[Variant B]**

Which version of the SRS is currently baselined? Has this requirement change been formally approved? What was the rationale for modifying this requirement in version 1.2?

## Minimal Realistic Example

**[Variant A]**

A Feature Tree for a restaurant site is annotated with release tags (1, 2, 3). Release Baseline 1 is formally approved, encompassing core Order Building and User Account Creation, while Dynamic Menu Updates are assigned to Release Baseline 2.

**[Variant B]**

Archiving a marked-up Word specification 'v1.0 draft 3', accepting all revisions upon sign-off, and tagging the clean file 'v1.0 approved' in a version control repository to prevent developers from building canceled features.

## Quality Criteria & Verification

**[Variant A]**

Baseline contents are explicitly identified and unambiguous; designated approvers give documented agreement; changes to baselined items trigger formal change control.

**[Variant B]**

Every requirement has a persistent, unique identifier; all team members access the single authoritative baseline repository; clear revision logs accompany every revision.

## Errors & Anti-Patterns

**[Variant A]**

Assuming baselining means 'freezing' requirements permanently without a change path; building unapproved baselines; forcing developers to commit to scope-bound baselines without sizing estimates.

**[Variant B]**

Informal uncommunicated edits to baselined specifications; multiple BAs editing local un-synchronized document versions ('v1.2 conflict'); allowing developers to work from obsolete drafts.

## When NOT to Use

**[Variant A]**

For pure continuous delivery environments where individual micro-changes are deployed immediately upon completion without release batching, though iteration planning still utilizes micro-baselines.

**[Variant B]**

Early exploratory brainstorming stages prior to initial requirement agreement where formal versioning adds unnecessary overhead.

## Alternatives & Complementary Methods

**[Variant A]**

Complementary: Practice #13 Prioritization, Practice #15 Organization, Practice #20 Change Management. Alternatives: Kanban pull-system buffers.

**[Variant B]**

Requirements Management (RM) tools, Product Backlog management in Agile tools, Source Code Version Control systems.

## Supported Decisions

**[Variant A]**

Release delivery commitment, resource allocation, iteration scope lock, vendor contract milestones.

**[Variant B]**

Release content decisions, build baseline freezing, change control intake decisions.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can calculate team capacity against story points to suggest optimal time-bound baseline scopes, auto-generate baseline release notes, and track drift between planned baseline items and actual implemented code.

**[Variant B]**

Not in source
