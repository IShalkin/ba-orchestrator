---
id: consolidated-solution-design-document
name: "Consolidated Solution Design Document"
task: T5
task_name: "Requirements Specification"
subtask: "5.6"
subtask_name: "Requirements Documents and Phrasing"
source_count: 1
---

# Consolidated Solution Design Document

`T5 Requirements Specification › 5.6 Requirements Documents and Phrasing`

## Problem Solved

Gives stakeholders one review-ready document instead of scattered analysis outputs, and prevents the rework and approval delays caused by insufficient detail, weak traceability and undocumented assumptions, by assembling the solution design in a fixed section order with explicit reviewer expectations for each section.

## BA Lifecycle Phase

Specification / validation

## Input Artifacts

Approved artifacts of the analysis (problem statement, scope, as-is and to-be processes, requirements, business rules, NFRs, data and integration models, stakeholder register, risks), the traceability matrix, open questions, assumptions and conflicts.

## Output Artifacts

Consolidated solution design document with these sections, each marked complete, partial (with reason) or n/a (with reason): 1 Business context; 2 Scope; 3 Current state; 4 Solution overview; 5 Operating model (ownership, governance, support); 6 Future-state processes; 7 Functional design (requirement-to-function mapping); 8 Application design; 9 Configuration design; 10 Environments and release path; 11 Data design and migration; 12 Integration design; 13 Security and controls; 14 Reporting and analytics; 15 User experience and adoption; 16 Non-functional requirements; 17 Test traceability; 18 Deployment and hypercare; 19 Risks, assumptions and dependencies. Plus a section-to-source map and a list of open items that block sign-off.

## Participants & Roles

BA or solution designer (author); solution architect, business owner, process owners, security and compliance, test lead, operations or support lead (reviewers); sponsor (approver).

## Prerequisites

Agreed scope; the upstream artifacts the document references exist; the audience and the approval path are known.

## Step-by-Step Procedure

1. Decide the depth: for small scopes merge sections (for example application with configuration design, environments with deployment) and mark the merges; keep all sections for large or contractual work.
2. Map each section to the artifacts that feed it and mark sections with no source as gaps.
3. Fill each section with its expected content, referencing the artifacts instead of re-writing them: business context (objectives, scope drivers, assumptions, success measures); scope (in and out statements, exclusions); current state (processes, pain points, workarounds, technology limits); solution overview (landscape, main components, architecture principles); operating model (future ownership, governance and support); future-state processes (flows, decision points, approvals, exceptions); functional design (workflows, validations, notifications, requirement-to-function mapping); application design (modules, dependencies, component interactions, at a lower level than the overview); configuration design (setup decisions, workflow rules, approval matrices, hierarchies, custom fields, with rationale); environments (dev, test and production strategy, promotion path, release controls, ownership); data (objects, sources, mappings, cleansing, validation, master-data ownership and lifecycle); integration (interfaces, APIs, schedules, monitoring, retries, error handling, support ownership); security (roles, permissions, single sign-on, segregation of duties, audit, regulatory controls); reporting (KPIs, dashboards, data sources, owners); user experience and adoption (personas, navigation, training, embedded guidance); NFRs (catalogue with measurable targets); test traceability (requirement, design, configuration and test matrix); deployment and hypercare (cutover, readiness criteria, rollback, hypercare, business readiness); risks (log with mitigations).
4. Self-review every section against its reviewer focus.
5. List the open items that block sign-off, each with an owner role.
6. Issue the document for review and record the review comments and decisions.

## Analyst Questions & Prompts

• Who signs off this document, and what will they check first?
• Which sections can be merged for this scope?
• Is every requirement traceable to a design element and a test?
• Who owns each environment, interface and data domain after go-live?
• What happens when an integration fails outside business hours, and who is alerted?
• What must be true before cutover, and how do we roll back?

## Minimal Realistic Example

Procurement platform rollout. Section 12 lists four interfaces (supplier master in, purchase orders out, invoices in, payments out), each with a schedule, the retry rule 'three retries, then alert the support queue' and an owner role. Section 17 has the matrix row 'REQ-031 > FD-12 > CFG-07 > TS-044'. Section 19 records the risk 'poor supplier data quality', mitigated by a cleansing sprint before migration.

## Quality Criteria & Verification

Reviewer focus per section: business context, the business need is clearly linked to the proposed solution; scope, boundaries are clear and scope creep is prevented; current state, there is a clear rationale for the future state; solution overview, the architecture is complete and aligned with the objectives; operating model, operational ownership is sustainable; future-state processes, processes are efficient and cover the requirements; functional design, traceable and complete; application design, architecturally consistent; configuration design, aligned with requirements and maintainable; environments, consistent, governed releases, supportable; data, quality, completeness and ownership accountability; integration, reliable, secure, supportable and monitored; security, compliant, audit-ready, controls effective; reporting, business value and measurability; user experience, effective for users and ready for adoption; NFRs, operational readiness; test traceability, full requirement coverage; deployment, go-live and organisational readiness; risks, delivery confidence. Across the document: content is referenced from artifacts rather than re-written; every section is complete, partial with a reason, or n/a with a reason.

## Errors & Anti-Patterns

Insufficient detail; weak traceability; undocumented assumptions; copying artifact content so that the document drifts from its sources; solution overview and application design saying the same thing at the same level; undefined environment ownership or promotion process; integration design without failure handling and support ownership; a technically sound design that ignores user adoption; silently dropping sections instead of marking them n/a.

## When NOT to Use

A pure requirements hand-off where the delivery team designs the solution (use Requirements Specification Templates (SRS) or PEGS Standard Plan instead); a small change that fits a one-page specification; discovery work with no agreed scope yet.

## Alternatives & Complementary Methods

Requirements Specification Templates (SRS) and PEGS Standard Plan for requirements-only documents; Requirements Traceability (feeds the test traceability section); Non-Functional Requirements Analysis (feeds the NFR section); Checkpoint Charley (Technical Design Review), Requirements Reviews and Inspections and Structured 4-Pass Specification Review to review the document.

## Supported Decisions

Design sign-off, build start, hand-off to a delivery team or vendor, go-live readiness, scope and risk acceptance.

## AI & Agentic Adaptation

An agent assembles the document from approved artifacts, maps sections to sources, flags empty sections as gaps and self-reviews each section against its reviewer focus; humans own the design decisions and the sign-off. The agent never fills a section with invented design content: it marks the section as a gap and states the question to ask.
