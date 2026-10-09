# T6. Prioritisation and Requirements Management

Selection guide: each line shows what the method solves and when NOT to use it (first variant; open the card for every variant's full text).

## 6.1 Prioritisation

- [MoSCoW](../methods/moscow.md) — Categorizes requirements into Must have, Should have, Could have, and Want to have (WONT) based on clear definitions, enabling flexible scope management during fixed timeboxes. *Not for:* When prioritizing a tiny list of 2 items where simple binary ranking is sufficient.
- [Value-Cost Prioritization (AHP)](../methods/value-cost-prioritization-ahp.md) — Reduces budget overruns, missed deadlines, and unmanaged scope creep by ordering requirements for phased/incremental release under limited resources. *Not for:* When all requirements are strictly mandatory legally, or when the total project scope is extremely small and fully funded.
- [Requirements Prioritization and Triage](../methods/requirements-prioritization-and-triage.md) — Reduces conflict and resource waste by determining the relative importance and implementation order of business analysis information based on value, risk, and constraints. *Not for:* When all requirements are legally mandatory with unlimited budget and fixed hard deadline.
- [Value-Cost-Risk Prioritization Matrix](../methods/value-cost-risk-prioritization-matrix.md) — Ranks requirements analytically by calculating priority scores derived from relative benefit, detriment, cost, and risk. *Not for:* When rapid ad-hoc prioritization is needed and time/resources do not permit multi-factor estimation.
- [Virtual Budgeting](../methods/virtual-budgeting.md) — Reduces 'criticality inflation' (where stakeholders mark all requested features as critical) and resolves priority conflicts by forcing realistic economic trade-offs. *Not for:* Safety-critical mandatory features where regulatory compliance makes prioritization non-negotiable.
- [Timeboxing](../methods/timeboxing.md) — Fixes delivery deadlines and budgets, flexing scope via prioritisation rather than allowing schedules to slip, ensuring timely delivery. *Not for:* When fixed-scope legal compliance mandates require 100% of all listed requirements to be delivered on a single non-negotiable date.
- [Quality Attribute Prioritization Grid](../methods/quality-attribute-prioritization-grid.md) — Exposes trade-offs and resolves conflicts among competing quality attributes (e.g., security vs. *Not for:* When a project has no conflicting quality demands or is a trivial utility application.

## 6.2 Backlog, Estimation and Release Planning

- [Product Backlog Management](../methods/product-backlog-management.md) — Maintains a dynamic, prioritized list of features, user stories, and bug fixes for development, providing a constant stream of prioritized work for development teams. *Not for:* In traditional rigid waterfall projects where scope is fixed upfront and change requests are strictly controlled via formal board procedures.
- [Dependency Stream Analysis](../methods/dependency-stream-analysis.md) — Reduces information overload in large models (>30 use cases) and clarifies cross-use-case workflow dependencies. *Not for:* Small systems with fewer than 10 straightforward, independent use cases.
- [Planning Poker](../methods/planning-poker.md) — Estimates the relative size and complexity of user stories/requirements using consensus-based card voting, reducing individual estimator bias and unvetted estimates. *Not for:* When well-understood, routine repetitive tasks with historical precise time data are being estimated.
- [Estimation](../methods/estimation.md) — Reduces budget and timeline forecasting uncertainty by using structured, mathematical, or expert-driven techniques to predict cost, effort, and duration. *Not for:* When scope is completely undefined with zero domain knowledge (conduct exploratory experiments first).

## 6.3 Organisation, Baselines and Reuse

- [Requirements Organisation and Management](../methods/requirements-organisation-and-management.md) — Structures, clusters, and links large sets of requirements, and resolves conflicting stakeholder requirements, reducing unmanageable, contradictory specifications. *Not for:* In micro-projects with under 10 straightforward requirements.
- [Requirements Baselines and Version Control](../methods/requirements-baselines-and-version-control.md) — Prevents moving-target scope creep, uncontrolled schedule slippage, misaligned implementation expectations, and uncoordinated release commitments. *Not for:* For pure continuous delivery environments where individual micro-changes are deployed immediately upon completion without release batching, though iteration planning…
- [Requirements Reuse](../methods/requirements-reuse.md) — Prevents 'reinventing the wheel', reduces requirements writing/review time, and enforces functional and architectural consistency across product lines and enterprise applications. *Not for:* In rapidly changing, highly novel domains where no legacy or reusable knowledge exists.
- [Unified PEGS Lifecycle](../methods/unified-pegs-lifecycle.md) — Eliminates the rigid, late-code risks of the Waterfall and the 'no-upfront-planning' chaos of extreme Agile by providing a flexible, iterative, sprint-based lifecycle model with balanced, evolving requirements. *Not for:* Replaced by lightweight DevOps continuous delivery for ultra-rapid cloud web maintenance, though underlying elaboration principles still apply.
- [Development Case Customization](../methods/development-case-customization.md) — Reduces process inefficiency, unnecessary bureaucracy, or project failure caused by misaligned process ceremony. *Not for:* Single-person, trivial 1-week tasks where process overhead exceeds work effort.

## 6.4 Traceability and Status

- [Requirements Traceability](../methods/requirements-traceability.md) — Tracks requirements bi-directionally (backwards to business sources/goals, forwards to design, code, and test cases), ensuring all requirements are delivered and no unneeded features are built. *Not for:* In tiny, 1-week single-developer scripts where formal matrix tracking creates excessive overhead.
- [Requirements Status Tracking](../methods/requirements-status-tracking.md) — Reduces overoptimistic status reporting (e.g., '90% done syndrome') and provides precise visibility into project progress by tracking discrete functional requirements through defined lifecycle states. *Not for:* Extremely small single-person projects where individual requirement tracking overhead exceeds project duration.
- [Issue and Item Tracking](../methods/issue-and-item-tracking.md) — Prevents open questions, missing requirements, TBDs, and stakeholder conflicts from slipping through the cracks or causing last-minute project derailments. *Not for:* None;

## 6.5 Requirements Change Management

- [Change Control](../methods/change-control.md) — Reduces unmonitored scope creep, unexpected budget overruns, and system instability caused by ad-hoc, un-evaluated requirement changes. *Not for:* In early exploratory prototyping phases before a formal requirement baseline has been established.
- [Change Impact Analysis](../methods/change-impact-analysis.md) — Prevents software surprises, uncoordinated schedule slips, and broken system dependencies by systematically identifying all work products and tasks affected by a proposed requirement modification. *Not for:* Trivial single-variable edits with zero ripple effect or un-baselined draft changes.

## 6.6 Requirements Risk and Process Improvement

- [Requirements Risk Management](../methods/requirements-risk-management.md) — Prevents requirements-related pitfalls (e.g., unstated needs, scope creep, lack of user involvement) from escalating into costly project crises or cancellations. *Not for:* When dealing with existing active problems (which should be handled via issue tracking) rather than future uncertainties.
- [Requirements Process Self-Assessment](../methods/requirements-process-self-assessment.md) — Prevents recurring project failures, schedule overruns, and quality defects by systematically diagnosing organizational BA process weaknesses and executing goal-oriented process improvements. *Not for:* When organization leadership refuses to provide time or resources to modify existing workflows.
