# T7. Validation and Acceptance

Selection guide: each line shows what the method solves and when NOT to use it (first variant; open the card for every variant's full text).

## 7.1 Reviews and Inspections

- [Requirements Reviews and Inspections](../methods/requirements-reviews-and-inspections.md) — Reduces defect leaks and quality errors by systematically evaluating business analysis work products with peers and stakeholders. *Not for:* When work products are in early, highly volatile brainstorming draft stages where formal review adds rigid friction.
- [Requirements Quality Gateway](../methods/requirements-quality-gateway.md) — Prevents bad, ambiguous, incomplete, or out-of-scope requirements from passing into development, reducing costly downstream rework. *Not for:* Informal exploratory prototyping phases where ideas are explicitly disposable.
- [Walk-Through](../methods/walk-through.md) — Establishes a common understanding of requirements and identifies quality flaws through an informal, author-guided group session. *Not for:* When formal compliance sign-off or contract-bound rigorous validation is mandatory (use formal Inspection).
- [Perspective-Based Reading](../methods/perspective-based-reading.md) — Improves defect detection rates by having reviewers inspect requirements through specific stakeholder viewpoints (e.g., tester, architect, user). *Not for:* When reviewers lack domain knowledge of the assigned perspective.
- [Structured 4-Pass Specification Review](../methods/structured-4-pass-specification-review.md) — Prevents superficial sign-offs and missing flaws by replacing single unfocused approvals with structured, multi-perspective reviews. *Not for:* Extremely minor baseline changes or bug fixes where informal peer review is sufficient.
- [Paraphrased Solution Review](../methods/paraphrased-solution-review.md) — Prevents passive, superficial document sign-offs where stakeholders approve solution specifications without truly reading or understanding them. *Not for:* For pure technical infrastructure specifications where business stakeholders have no operational interaction.
- [Requirements Quality Verification and Analysis](../methods/requirements-quality-verification-and-analysis.md) — Prevents costly downstream software defects, project failures, and legal disputes by systematically evaluating requirements against 14 objective quality criteria. *Not for:* Quality verification principles apply to all projects, though the level of rigor scales with project risk.

## 7.2 Prototypes, Animation and Usability

- [Validation through Prototypes](../methods/validation-through-prototypes.md) — Exposes gaps, misunderstandings, and UI/UX issues by allowing stakeholders to directly experience and test interactive software mocks. *Not for:* When project budget/time constraints prohibit prototype creation or for simple, fully understood requirements.
- [Specification Animation](../methods/specification-animation.md) — Reduces requirements inadequacy, misunderstanding of formal specifications, and unhandled operational edge-cases by visually demonstrating executable models to stakeholders. *Not for:* When no formal executable specification exists, or for purely non-functional static requirements (e.g., development cost).
- [Usability Testing](../methods/usability-testing.md) — Identifies real user interface usability problems, task failures, and learnability roadblocks before code is locked in. *Not for:* Evaluating internal back-end algorithmic calculations with no human interface.

## 7.3 Formal Model Verification

- [Model and Requirements Database Queries](../methods/model-and-requirements-database-queries.md) — Reduces structural inconsistencies, unlinked elements, orphan requirements, and incomplete cross-view specifications across large multi-view models. *Not for:* When the model is tiny and easily inspected manually, or when no structured model database tool is used.
- [Model Checking](../methods/model-checking.md) — Reduces subtle concurrency errors, race conditions, deadlocks, and unhandled state combinations in complex reactive models. *Not for:* For infinite-state systems without abstraction, or when models are informal and cannot be compiled into state machines.
- [Theorem Proving](../methods/theorem-proving.md) — Reduces unverified claims, subtle mathematical errors, and inconsistency in infinite-state declarative specifications. *Not for:* When finite-state verification (model checking) can do the job automatically, or when team expertise in formal logic is absent.

## 7.4 Testing and Acceptance

- [Requirements-Based Testing](../methods/requirements-based-testing.md) — Verifies requirements testability and discovers missing, ambiguous, or inconsistent logic by deriving test scenarios directly from user requirements before writing code. *Not for:* None;
- [Acceptance Testing](../methods/acceptance-testing.md) — Establishes explicit, objective criteria for when a feature or user story is considered 'done' and fit for business use, preventing scope/quality misunderstandings. *Not for:* None;
- [Use Case-Driven Test Planning](../methods/use-case-driven-test-planning.md) — Reduces untested requirements, late-stage defect discovery, and unaligned testing scope. *Not for:* Non-functional load/stress testing unrelated to discrete user transactions.
- [Checkpoint Charley (Technical Design Review)](../methods/checkpoint-charley-technical-design-review.md) — Prevents solution drift, technical gold-plating, and developer-introduced requirement changes from reaching production without business analyst and stakeholder awareness. *Not for:* In pure agile/Scrum environments where the BA/product owner sits collocated with developers daily and reviews working code every sprint.
