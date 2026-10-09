---
id: business-rules-analysis
name: "Business Rules Analysis"
task: T5
task_name: "Requirements Specification"
subtask: "5.4"
subtask_name: "Business Rules and Decision Logic"
source_count: 4
---

# Business Rules Analysis

`T5 Requirements Specification › 5.4 Business Rules and Decision Logic`

**Also described as:** Business rules analysis; Identifying and Documenting Business Rules (Decision Tables & Mapping Matrix)

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Identifies and categorizes operational constraints, policies, and statutory laws that govern business decisions and process execution, reducing compliance failures and invalid decisions.

**[Variant B]**

Reduces ambiguity and operational inconsistency by identifying, expressing, and managing actionable, testable business directives separately from processes and technology.

**[Variant C]**

Prevents business policy violations in software, eliminates hardcoded volatile business logic, avoids duplicate rule specifications, and ensures regulatory compliance.

**[Variant D]**

Unstructured policy and decision-making logic

## Uncertainty Reduced

**[Variant D]**

Implicit constraints scattered across documents

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Business Process Analysis / Specification

**[Variant B]**

analysis / specification / validation

**[Variant C]**

Elicitation / Analysis / Specification

**[Variant D]**

Analysis, specification

## Input Artifacts

**[Variant A]**

Legal regulations, corporate policy documents, process models, data models.

**[Variant B]**

Business policies, regulations, contracts, subject matter expertise, current process models.

**[Variant C]**

Corporate policies, laws, regulations, existing source code (reverse engineering), data models, interview transcripts.

**[Variant D]**

Regulations, laws, interviews with specialists

## Output Artifacts

**[Variant A]**

Business Rules Catalogue categorized by Statutory/Regulatory, Organizational Policy, and Operational Procedures.

**[Variant B]**

Business rules catalog/repository, definitional and behavioral rules statements, decision tables/trees.

**[Variant C]**

Business Rules Catalog (Terms, Facts, Constraints, Action Enabler, Inferences, Computations), Decision Tables, Decision Trees, Requirements Mapping Matrix (tracing rules to functional requirements).

**[Variant D]**

Result: business rules catalogue, decision tables, decision trees. Artifacts: decision tables, rules catalogue

## Participants & Roles

**[Variant A]**

BA, Compliance/Legal Officer, Business Owner, Policy SME.

**[Variant B]**

BA, Domain SME, Business Owner, Compliance/Legal, Developer, Tester.

**[Variant C]**

Business Analyst, Subject Matter Experts (SMEs), Legal/Compliance Officers, Developers, Database Architects.

**[Variant D]**

BA, Legal/Compliance, Domain SME, Developer

## Prerequisites

**[Variant A]**

Identification of business processes, decisions, or data structures.

**[Variant B]**

Established business glossary and vocabulary relevant to the domain.

**[Variant C]**

Access to business policies, domain experts, or compliance standards.

## Step-by-Step Procedure

**[Variant A]**

Identify external Legal/Regulatory constraints (non-negotiable).
2. Identify internal Organizational Policy constraints (strategic).
3. Identify internal Operational Procedures (tactical/flexible).
4. Document rules explicitly.
5. Challenge operational procedures to eliminate legacy bad habits.
6. Map rules to process decision points and data model relationships.

**[Variant B]**

Elicit business policies and directives from documentation or SMEs.
2. Distinguish definitional rules (knowledge/inferences) from behavioral rules (governing conduct).
3. Express rules at an atomic level using standard, business-friendly terminology.
4. Specify enforcement levels for behavioral rules (e.g., strictly enforced, override with explanation).
5. Map rules to the business decisions and processes they constrain or enable.
6. Validate rules for consistency, completeness, and non-contradiction in a repository.

**[Variant C]**

Active listen during elicitation for keywords indicating business logic ('only', 'must', 'may not', 'if/then').
2. Extract rules from external regulations, policy manuals, and data cardinalities.
3. Classify rules into standard types (Facts, Constraints, Action Enablers, Inferences, Computations).
4. Assign unique persistent IDs (e.g., RET-1, DISC-1) and store rules in an enterprise asset catalog separate from project documents.
5. Write constraints clearly using ' must/may only ' and action enablers using 'If  then '.
6. Document complex multi-condition logic using Decision Tables or Decision Trees to ensure complete condition coverage.
7. Trace derived functional requirements back to source business rules using a Requirements Mapping Matrix.

**[Variant D]**

1. Identify the constraints and conditions.
2. Classify the rules (terms, facts, actions).
3. Express them as tables or expressions.

## Analyst Questions & Prompts

**[Variant A]**

What law compels us to do this? What corporate policy dictates this rule? Is this rule a strict policy or just an old habit? What rule determines this data relationship?

**[Variant B]**

"What rule determines whether a customer is eligible for discount X?", "Is this directive a definitional fact or a behavioral constraint?", "What is the consequence/enforcement if this rule is violated?"

**[Variant C]**

"What corporate policy or regulation dictates this behavior?", "What happens if a user attempts to violate this rule?", "Are there exceptions to this restriction?", "Does this computation or discount logic change frequently?"

**[Variant D]**

'Under what conditions does this discount apply?', 'Which law or norm governs this rule?'

## Minimal Realistic Example

**[Variant A]**

Analyzing ticket booking rules: identifying mandatory legal age limits (Statutory), group booking limits (Policy), and discount eligibility rules (Operational Procedure).

**[Variant B]**

Definitional rule: 'A customer placing >10 orders/month is a Preferred Customer.' Behavioral rule: 'Orders over $1,000 must not be placed without manager override.'

**[Variant C]**

Discount business logic with multiple order totals and club membership conditions is represented in a Decision Table (DISC-1 through DISC-6) mapping conditions to outcomes (10% discount, 20% discount, free shipping), preventing missing boundary logic.

**[Variant D]**

Credit-rating calculation table based on length of employment and income

## Quality Criteria & Verification

**[Variant A]**

Clear categorization by constraint type; explicit mapping to corresponding process decision points and data model cardinality constraints.

**[Variant B]**

Rules are atomic, practicable (no further interpretation needed), declarative, single-sourced, and free from implementation logic.

**[Variant C]**

Decision tables cover all  $2^N$  condition combinations; rules avoid double negatives; every software-enforced rule traces to specific functional requirements or a business rules engine.

**[Variant D]**

Checking the table for consistency and completeness of combinations

## Errors & Anti-Patterns

**[Variant A]**

Mistaking long-standing informal habits for unchangeable corporate policies; failing to challenge outdated operational procedures; mixing non-negotiable legal rules with flexible operational guidelines.

**[Variant B]**

Embedding business rules directly into process flow diagrams or code; creating long lists of ambiguous, contradictory rules.

**[Variant C]**

Confounding business rules with software requirements; embedding volatile rules directly into source code instead of databases/rule engines; duplicating rule text across multiple specifications.

**[Variant D]**

Mixing business rules with technical implementation constraints

## When NOT to Use

**[Variant A]**

In unconstrained creative brainstorming or visioning sessions where rules are deliberately set aside.

**[Variant B]**

When business operations are completely ad-hoc and non-repeatable, or when procedural workflow matters more than decision logic.

**[Variant C]**

When the application contains no business logic, policy restrictions, regulatory mandates, or complex decision calculations.

**[Variant D]**

No complex logic or variability in decision making

## Alternatives & Complementary Methods

**[Variant A]**

Constraints Analysis, Decision Tables, Decision Trees, Entity Relationship Modelling.

**[Variant B]**

Complemented by Concept Modelling, Decision Modelling, Decision Analysis, Data Dictionary, and Glossary.

**[Variant C]**

Complementary: Practice #8 Data Concepts, Practice #10 Requirement Analysis, Practice #14 Writing Requirements. Alternatives: Business Rules Engines (BRE), Rule books.

**[Variant D]**

Textual requirements, flowcharts

## Supported Decisions

**[Variant A]**

Compliance validation, process logic design, database integrity constraint specification.

**[Variant B]**

Operational business decisions, compliance verification, business process logic execution.

**[Variant C]**

Software design architecture (hardcoded vs. database/rule-engine driven), compliance verification, exception handling workflow design.

**[Variant D]**

Compliance, architecture, acceptance

## AI & Agentic Adaptation

**[Variant A]**

Regulatory-compliance AI engines scan new statutory legislation text to extract candidate business rules and flag impacted corporate process steps automatically.

**[Variant B]**

Agents can parse regulatory documents to extract candidate declarative rules, run cross-validation checks for rule conflicts, and feed verified rules into automated Business Rules Management Systems (BRMS).

**[Variant C]**

AI agents can analyze policy documents or legacy source code to discover implied business rules, automatically fill out complete decision tables from narrative text, and highlight boundary logic gaps for SME verification.

**[Variant D]**

Automatic extraction of decision tables from the text of regulations
