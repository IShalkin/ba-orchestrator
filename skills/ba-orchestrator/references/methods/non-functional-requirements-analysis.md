---
id: non-functional-requirements-analysis
name: "Non-Functional Requirements Analysis"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 3
---

# Non-Functional Requirements Analysis

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

**Also described as:** Eliciting and Evaluating Quality Attributes (Nonfunctional Requirements / Planguage); Qualities and Constraints Analysis (NFR Analysis)

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Reduces solution failure risks related to quality of service by specifying constraints and operational attributes (e.g., performance, security, availability) that functional features must meet.

**[Variant B]**

Prevents late-stage product failures caused by poor performance, security breaches, safety hazards, unmaintainability, or regulatory non-compliance.

**[Variant C]**

Prevents delivery of software that functions correctly in tests but fails in production due to slowness, poor usability, unreliability, insecurity, or unscalability.

## BA Lifecycle Phase

**[Variant A]**

analysis / specification / Solution Evaluation

**[Variant B]**

Discovery / Analysis / Specification

**[Variant C]**

Elicitation / Analysis / Specification

## Input Artifacts

**[Variant A]**

Functional requirements, architectural constraints, regulatory standards, SLA objectives.

**[Variant B]**

Stakeholder goals, regulatory standards, industry compliance guidelines, NFR checklists

**[Variant C]**

Business Objectives, Stakeholder Profiles, Architecture diagrams, Corporate Security/Compliance Standards.

## Output Artifacts

**[Variant A]**

Non-functional requirements statements/matrices (quantified quality attributes and constraints).

**[Variant B]**

Non-Functional Requirements (NFR) specification, quality goals model, compliance matrix

**[Variant C]**

Nonfunctional Requirements Specifications (using Planguage or structured natural language), Acceptance Criteria / Fit Criteria, Quality Attribute Pairwise Matrix.

## Participants & Roles

**[Variant A]**

BA, Systems Architect, Developer, Tester, Security/Compliance Lead, Operational Support.

**[Variant B]**

BA, Architect, Safety Engineer, Security Specialist, Compliance/Legal, SME

**[Variant C]**

Business Analyst, Software Architect, End Users (various classes), Maintenance/Operations Staff, Security/Compliance Officers.

## Prerequisites

**[Variant A]**

Understood functional requirements and business context.

**[Variant B]**

Identified product context, operational environment, and applicable regulations.

**[Variant C]**

Understanding of business objectives and user task context.

## Step-by-Step Procedure

**[Variant A]**

Identify relevant non-functional categories (Availability, Security, Performance Efficiency, Usability, Maintainability, Scalability, Compliance, etc.).
2. Elicit specific quality expectations and constraints from business and technical stakeholders.
3. Quantify vague expectations into testable declarative statements (e.g., response time in seconds, uptime %)...
4. Evaluate context and potential conflicts between non-functional attributes (e.g., Security vs. Usability).
5. Document requirements in matrices or specifications alongside functional stories.
6. Validate testability with QA testers and architects.

**[Variant B]**

Review goals, domain standards, and customized NFR checklists (performance, safety, security, usability, etc.).
2. Decompose vague quality goals ('easy to use', 'safe') into specific sub-goals.
3. Translate quality sub-goals into concrete functional requirements or measurable physical/design constraints.
4. Specify environmental, physical, and development process constraints.
5. Assign global vs. local scope (e.g., attaching NFRs to specific use cases).
6. Define testable criteria for each non-functional requirement.

**[Variant C]**

Identify relevant quality attributes from standard catalogs (e.g., availability, performance, usability, security, maintainability).
2. Elicit specific stakeholder expectations using targeted probing questions rather than vague inquiries.
3. Analyze architectural and design implications of requested quality targets.
4. Analyze trade-offs among conflicting attributes and evaluate priorities (e.g., using Pairwise Comparison).
5. Specify nonfunctional requirements precisely using verifiable condition patterns like Planguage (Tag, Ambition, Scale, Meter, Goal, Stretch) or quantitative fit criteria.
6. Derive detailed functional requirements required to enable quality targets (e.g., password reset routines for security).

## Analyst Questions & Prompts

**[Variant A]**

"What is the maximum acceptable downtime for this system?", "How many concurrent users must the system support at peak load?", "What regulatory compliance standards (e.g., GDPR, HIPAA) apply?"

**[Variant B]**

How fast must this perform? What safety hazards exist? How secure must data be? What physical or environmental limits must the product withstand? What standards apply?

**[Variant C]**

"Is it more essential to have certain functions available than others?", "What time periods could be reserved for scheduled maintenance with minimal impact?", "What response time is required for 95% of user actions?", "What level of imperfection or downtime are stakeholders willing to tolerate given budget limits?"

## Minimal Realistic Example

**[Variant A]**

Requirement: 'The payment search function must return results in < 1.5 seconds for peak loads of up to 5,000 concurrent users with 99.9% uptime.'

**[Variant B]**

Decomposing an outdoor leisure device's 'Dependable' quality goal into 'Waterproof to 3 atmospheres', 'Shockproof (survive 1m drop)', and 'Operational temperature -50C to +60C'.

**[Variant C]**

Planguage entry: Tag: Availability.MaintenanceDowntime; Ambition: Minimize downtime impact; Scale: Minutes system is offline per month; Meter: System clock logs; Goal: Avg <= 1 hour/week; Stretch: Avg <= 1.5 hours/month.

## Quality Criteria & Verification

**[Variant A]**

Requirements are quantified and testable (e.g., specific metrics instead of 'fast'); clear constraints on solution architecture.

**[Variant B]**

Verifiability (each NFR has an explicit measurement method and pass/fail criteria), consistency across global/local scopes, and architectural feasibility modeling.

**[Variant C]**

Requirements must be Precise, Necessary, Measurable, Verifiable (testable), and Realistic; trade-offs between conflicting attributes are explicitly resolved.

## Errors & Anti-Patterns

**[Variant A]**

Using vague qualitative phrases like 'user-friendly' or 'system must be fast'; specifying overly strict targets that unnecessarily inflate cost.

**[Variant B]**

Using unmeasurable buzzwords ('user-friendly', 'high-speed', '100% safe'); treating NFRs as an afterthought; imposing unrealistic/prohibitive constraints.

**[Variant C]**

Writing vague statements like 'The system shall be fast and secure'; assuming 100% availability is attainable without assessing cost; treating nonfunctional requirements as isolated backlog items without architectural consideration.

## When NOT to Use

**[Variant A]**

Rarely omitted, though deep technical NFR specification may be deferred in very early conceptual prototypes.

**[Variant B]**

In lightweight internal utility scripts where operational qualities have minimal business impact.

**[Variant C]**

When defining throwaway internal proofs-of-concept where production quality is explicitly out of scope.

## Alternatives & Complementary Methods

**[Variant A]**

Complemented by Acceptance Criteria, SLA definitions, Prototyping, and Use Cases.

**[Variant B]**

ISO/IEC 9126, IEEE 830 templates, Quality Function Deployment (QFD), Planguage.

**[Variant C]**

Complementary: Practice #5 Decision Makers, Practice #13 Prioritization (Pairwise Matrix), Practice #14 Consistent Writing. Alternatives: FURPS+, ISO/IEC 25010 SQuaRE framework.

## Supported Decisions

**[Variant A]**

Technical architecture selection, infrastructure sizing, vendor platform evaluation, acceptance testing sign-off.

**[Variant B]**

Architecture selection, hardware component picking, security model design, compliance sign-off.

**[Variant C]**

System architecture design, infrastructure provisioning, technology stack selection, release readiness.

## AI & Agentic Adaptation

**[Variant A]**

AI agents can analyze functional specs to auto-suggest missing NFRs based on domain industry standards (e.g., security NFRs for fintech apps).

**[Variant B]**

Agents cross-reference proposed specifications against legal/regulatory constraint databases (e.g., ISO, GDPR, FAA), automatically flagging missing compliance and environmental NFRs for human safety/legal expert approval.

**[Variant C]**

AI agents can evaluate logged nonfunctional requirements against quality checklists (checking for verifiability and metric presence), auto-format vague statements into Planguage structures, and suggest synthetic performance test suites.
