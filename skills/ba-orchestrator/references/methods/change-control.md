---
id: change-control
name: "Change Control"
task: T6
task_name: "Prioritisation and Requirements Management"
subtask: "6.5"
subtask_name: "Requirements Change Management"
source_count: 5
---

# Change Control

`T6 Prioritisation and Requirements Management › 6.5 Requirements Change Management`

**Also described as:** Change Control Process; Change Request Management Process; Formal Requirements Change Control Process; Managing Changes to Requirements Effectively (Change Control Process & Impact Analysis)

This card merges 5 descriptions of the method, labelled Variant A–E in every field.

## Problem Solved

**[Variant A]**

Reduces unmonitored scope creep, unexpected budget overruns, and system instability caused by ad-hoc, un-evaluated requirement changes.

**[Variant B]**

Reduces scope creep, undocumented system decay, and architectural instability by enforcing a disciplined review procedure for all proposed requirement modifications.

**[Variant C]**

Controls scope creep, prevents chaos from unvetted feature requests, evaluates cost/schedule ripple impacts, and maintains alignment across baseline updates.

**[Variant D]**

Channels, evaluates, and controls proposed modifications to requirements baselines to prevent scope creep.

**[Variant E]**

Eliminates uncontrolled scope creep, informal 'backdoor' developer promises, and uncoordinated modifications by evaluating business impact and obtaining formal approval for all baseline changes.

## BA Lifecycle Phase

**[Variant A]**

Change management

**[Variant B]**

Evolution / change management

**[Variant C]**

Requirements Management / Change Management

**[Variant D]**

Change Management / Management

**[Variant E]**

change management

## Input Artifacts

**[Variant A]**

Change requests, wishlists, existing RD baseline, impact analysis reports, traceability graph.

**[Variant B]**

Wishlist, motivated Change Request forms, impact analysis reports, traceability graph.

**[Variant C]**

Change Requests, Existing Baselines, Traceability Matrix, Architecture Models, Cost/Effort Estimation models.

**[Variant D]**

Change Request document (ID, Title, Description, Justification, Priority, Applicant)

**[Variant E]**

Submitted Change Request (with description, origin, rationale, priority), baselined SRS/backlog.

## Output Artifacts

**[Variant A]**

Evaluated/approved change requests, prioritized change log, baselined new RD version, change audit trail.

**[Variant B]**

Change Evaluation log, approved/rejected/deferred change decisions, baselined RD revision/variant.

**[Variant C]**

Change Control Process Flow, Change Request Logs/Status, Impact Analysis Reports, Updated Baselines.

**[Variant D]**

Impact analysis report, CCB decision log, updated requirements baseline, change assignment

**[Variant E]**

Change Request Log / Database, Impact Analysis Report, Updated Baseline Artifacts, CCB Decision Record.

## Participants & Roles

**[Variant A]**

Change Review Board (CRB), BA, Project Manager, Sponsor, System Architect, Lead Developer.

**[Variant B]**

Change Control Board (CCB) - Decision Makers, BA, Architect, SME, Customer Representative.

**[Variant C]**

Change Control Board (CCB) / Product Owner, Business Analyst (impact analyst), Requestor, Development & QA Leads.

**[Variant D]**

Applicant, Change Manager, Change Control Board (CCB: Contractor, Architect, Developer, PM, QA, RE)

**[Variant E]**

Change Control Board (CCB Chair, BA, PM, Dev Lead, Test Lead, Business/Customer Rep), Originator, Evaluator, Modifier, Verifier.

## Prerequisites

**[Variant A]**

An approved baseline version of the RD exists; traceability links are established.

**[Variant B]**

Traceable requirements baseline; established CCB review authority and policies.

**[Variant C]**

An established, approved requirements baseline.

**[Variant D]**

Formally established requirements baseline; active Change Control Board.

**[Variant E]**

Established requirements baseline, documented change control process description, defined CCB charter.

## Step-by-Step Procedure

**[Variant A]**

Initiate change: Collect change wishes and submit a structured Change Request (description, rationale, urgency, initial cost/impact estimate).
2. Evaluate change: CRB reviews request, assesses well-foundedness, traces forward/backward impact, detects conflicts, and estimates cost/feasibility.
3. Prioritize approved changes.
4. Consolidate change: Propagate approved changes through the RD, re-verify consistency, update traceability graph, and baseline the new RD version.
5. Implement changes in software revisions/variants.

**[Variant B]**

(Initiation) Collect proposed changes into a motivated Change Request detailing rationale, urgency, and affected items.
2. (Evaluation) CCB reviews the request, uses traceability graphs to assess forward impact on architecture, costs, and schedules, and checks for conflicts with existing goals.
3. (Prioritization) Prioritize approved changes against project resources.
4. (Decision) CCB formally approves, rejects, or defers changes.
5. (Consolidation) Propagate approved changes through the RD, re-verify consistency, update traceability graphs, and baseline the new RD version.

**[Variant C]**

Define and document a lightweight Change Control Process answering who submits, who analyzes, and who decides.
2. Receive formal change requests and log them with a unique ID and 'Submitted' status.
3. Perform Impact Analysis: BA analyzes scope, technical ripple effects, regulatory risks, cost/effort, and schedule trade-offs across ecosystem maps and traceability matrices.
4. Present impact assessment to the Change Control Board (CCB) or Product Owner.
5. CCB evaluates request against business objectives and capacity buffers, making a decision (Approve, Reject, Defer).
6. Log decision and rationale; communicate decision to submitter and affected team members.
7. If approved, update requirement text, models, and attributes, increment version numbers, and establish a new baseline snapshot.

**[Variant D]**

Applicant submits a formal Change Request.
2. Change Manager/CCB pre-classifies request (Corrective, Adaptive, Exceptional).
3. Conduct Impact Analysis: estimate total effort across affected requirements and downstream artifacts.
4. CCB evaluates request: compare effort/cost vs. business benefit.
5. CCB decides (Approve / Reject).
6. If approved: prioritize change and assign to a specific release/project.
7. If rejected: communicate rationale to applicant.

**[Variant E]**

Originator submits a change request containing required attributes via an approved channel/tool.
2. Request Receiver registers the request and assigns a unique ID.
3. CCB Chair assigns an Evaluator to perform change impact analysis.
4. Evaluator analyzes technical feasibility, effort, cost, and ripple effects across work products, reporting findings to CCB.
5. CCB meets to evaluate benefits vs. impacts and formally decides (Approve, Reject, Defer, Modify).
6. If approved, CCB allocates change to a release/iteration, updates priority, and assigns a Modifier.
7. Modifier updates affected requirements, designs, code, and trace links.
8. Verifier conducts peer review or testing to confirm change correctness.
9. CCB Chair closes request and notifies all affected stakeholders.

## Analyst Questions & Prompts

**[Variant A]**

What is the rationale and urgency of this change? What other requirements and architectural components are impacted? Is the benefit worth the implementation cost?

**[Variant B]**

What is the business rationale for this change? What architectural components are affected? What is the cost of implementing this change vs the risk of not changing?

**[Variant C]**

"Does this proposed change contribute to our stated business objectives?", "What other systems, interfaces, or requirements will be impacted if we make this change?", "What is the cost and schedule trade-off if we accept this request?", "Which baseline does this change apply to?"

**[Variant D]**

"What downstream artifacts are affected by this change?", "What is the total implementation effort across design, code, and test cases?"

**[Variant E]**

What is the business value and rationale for this change? What work products (code, test, design, SRS) are impacted? What are the cost, schedule, and quality implications? What requirements are deferred if we accept this new request?

## Minimal Realistic Example

**[Variant A]**

Evaluating a change request to add 'SMS notification' alongside 'e-mail notification', assessing its architectural impact on the 'Notifier' module, approving it, and updating the RD baseline.

**[Variant B]**

Submitting a Change Request to add 'SMS Notification'. The CCB evaluates impact using traceability links, determines a $10k cost and 2-week schedule extension, approves it, and baselines RD Revision 2.1.

**[Variant C]**

A request arrives to change a vendor integration URL to prevent timeouts. Impact analysis by the BA reveals it requires invasive code revisions across three separate systems. The CCB determines the risk is too high for the current release, rejects the request for now, and defines an operational workaround.

**[Variant D]**

A customer requests adding real-time weather overlays; CCB performs impact analysis (40 hours effort), approves it as an adaptive change, and assigns it to Release 2.0.

**[Variant E]**

A customer requests a new catalog query feature; the developer estimates 6 hours informally, but formal impact analysis reveals 3 days across multiple database files. The CCB decides to defer it to Release 2 to protect the current launch date.

## Quality Criteria & Verification

**[Variant A]**

Formal CRB approval sign-off; complete forward propagation across all dependent artifacts; maintained consistency in the new RD baseline.

**[Variant B]**

Formal CCB sign-off logs; zero undocumented requirement changes in production code; full propagation of approved changes across all dependent artifacts.

**[Variant C]**

Every change request is logged and status-tracked; impact analysis precedes all approval decisions; approved changes are reflected in updated baseline documentation.

**[Variant D]**

Traceable documentation of all decisions; accurate impact analysis; zero unapproved scope changes.

**[Variant E]**

100% of baseline changes trace to an approved Change Request; impact analysis is completed prior to decision; decision rationale is documented in database.

## Errors & Anti-Patterns

**[Variant A]**

Bypassing the CRB via informal developer-client agreements; failing to propagate changes to test cases and user manuals; un-documented change rationale.

**[Variant B]**

Bypassing CCB via informal developer-customer side agreements ('scope creep'); holding up critical bug fixes due to overly bureaucratic CCB procedures.

**[Variant C]**

Allowing informal 'backdoor' changes directly to developers without impact analysis; implementing overly bureaucratic change processes that team members bypass; failing to update specification documentation after making changes.

**[Variant D]**

Implementing changes informally without CCB approval; ignoring downstream artifact impacts during effort estimation.

**[Variant E]**

Bypassing process for favored stakeholders ('Bruce always says yes'); unmanaged growth of approved backlog changes that will never be delivered; cumbersome processes that force teams to abandon change control.

## When NOT to Use

**[Variant A]**

In early exploratory prototyping phases before a formal requirement baseline has been established.

**[Variant B]**

In early exploratory greenfield prototyping where requirements are still in raw discovery mode before the first baseline.

**[Variant C]**

Before initial requirements baseline approval (pre-baseline exploration is informal iteration, not change control).

**[Variant D]**

In early discovery phases prior to creating an initial requirement baseline.

**[Variant E]**

Early elicitation phases prior to baselining; minor internal individual tasks that do not impact external interfaces, commitments, or other team members.

## Alternatives & Complementary Methods

**[Variant A]**

Agile backlog grooming, Configuration management, Feature toggles.

**[Variant B]**

Complementary: Traceability Management, Goal Modeling, Version Control Systems.

**[Variant C]**

Complementary: Practice #5 Decision Makers, Practice #10 Analysis, Practice #19 Baselines. Alternatives: Agile Backlog Refinement / Reprioritization.

**[Variant D]**

Traceability Matrix/Graph (used during Impact Analysis)

**[Variant E]**

Agile Product Backlog Reprioritization, Fast-Path Change Execution, Issue-Tracking Systems.

## Supported Decisions

**[Variant A]**

RD baselining, release scope adjustments, change request approval/rejection.

**[Variant B]**

Scope baseline changes, budget/schedule adjustments, release versioning.

**[Variant C]**

Scope adjustment approvals, schedule buffer consumption, release trade-off choices, budget adjustments.

**[Variant D]**

Scope changes, release content adjustments, budget/schedule re-baselining.

**[Variant E]**

Scope adjustment decisions, release date/budget renegotiation, resource allocation.

## AI & Agentic Adaptation

**[Variant A]**

Change management agents can automatically parse incoming change requests, run forward impact analysis queries across the model database, and generate preliminary cost-benefit summaries for CRB review.

**[Variant B]**

AI agents can automatically parse Change Requests, run automated impact analysis across code repositories using traceability graphs, and draft CCB cost-impact reports.

**[Variant C]**

AI agents can analyze change request text against codebase indices and dependency models to auto-generate impact analysis drafts, trace potential affected requirements, predict effort estimates, and keep change request status logs updated.

**[Variant D]**

Automated impact analysis where AI traces requirement dependencies across the codebase and drafts effort estimates for CCB review.

**[Variant E]**

Not in source
