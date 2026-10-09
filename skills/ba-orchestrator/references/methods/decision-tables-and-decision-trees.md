---
id: decision-tables-and-decision-trees
name: "Decision Tables and Decision Trees"
task: T5
task_name: "Requirements Specification"
subtask: "5.4"
subtask_name: "Business Rules and Decision Logic"
source_count: 6
---

# Decision Tables and Decision Trees

`T5 Requirements Specification › 5.4 Business Rules and Decision Logic`

**Also described as:** Decision Tables; Decision Tables and Informal Rules Tables; Decision tables and decision trees; Structured Natural Language & Decision Tables

This card merges 6 descriptions of the method, labelled Variant A–F in every field.

## Problem Solved

**[Variant A]**

Models complex combinations of conditions and their resulting actions in a rigorous grid or tree format, eliminating logic gaps, ambiguities, and redundant rules.

**[Variant B]**

Specifies non-trivial business logic, conditional rules, and complex calculations unambiguously without writing code.

**[Variant C]**

Reduces ambiguity, logical noise, and omissions in complex natural language conditional statements by structuring logic into tabular input-output combinations.

**[Variant D]**

Eliminates ambiguity, missed combinations, and errors in rule-heavy domain logic, multi-condition workflows, and boundary conditions.

**[Variant E]**

Prevents missing requirements and undefined logic gaps when complex, multi-variable logic conditions dictate system behavior.

**[Variant F]**

Reduces natural language ambiguities, noises, misplaced remorse, missing cases, and unmeasurable specifications in requirement documentation.

## BA Lifecycle Phase

**[Variant A]**

Analyse Needs / Business Process Analysis / Specification

**[Variant B]**

analysis

**[Variant C]**

Specification / quality assurance

**[Variant D]**

Analysis / Specification

**[Variant E]**

analysis

**[Variant F]**

Specification and documentation

## Input Artifacts

**[Variant A]**

Business rules, task steps, policy specifications.

**[Variant B]**

Business policy documents, SME interview notes, pricing rules.

**[Variant C]**

Complex if-then conditional statements, inputs/outputs lists.

**[Variant D]**

Business rules, policies, stakeholder interviews, regulatory documents.

**[Variant E]**

Business rules, functional specifications, conditional user logic

**[Variant F]**

Agreed statements, elicitation notes, business rules.

## Output Artifacts

**[Variant A]**

Limited-entry or Extended-entry Decision Table (Condition stub/entries, Action stub/entries), or Decision Tree diagram.

**[Variant B]**

Decision tables (Conditions vs. Actions matrix) or informal business rule tables.

**[Variant C]**

Disjoint and exhaustive Decision Table, identified missing logic cases, cause-effect test cases.

**[Variant D]**

Decision table matrix (conditions, combinations, and explicit required results).

**[Variant E]**

Decision Table (matrix of true/false conditions and resulting system actions) or Decision Tree (graphical branching tree of decisions leading to outcomes)

**[Variant F]**

Disciplined requirements document sections, decision tables, standardized requirement templates with fit criteria.

## Participants & Roles

**[Variant A]**

BA, SMEs, Business Rules Developer, Tester.

**[Variant B]**

BA, SME, developer, tester.

**[Variant C]**

Business Analyst, Developer, Tester.

**[Variant D]**

Business Analyst, SME, Business Owner, Developer, Tester.

**[Variant E]**

BA, Business SME, Developers, Testers

**[Variant F]**

BA, Developer, Tester, Client.

## Prerequisites

**[Variant A]**

Identification of a task or process step containing multiple decision conditions.

**[Variant B]**

Identification of conditional business logic with multiple combinations.

**[Variant C]**

Identification of atomic input conditions and output actions.

**[Variant D]**

Identified condition inputs and possible system outcome actions.

**[Variant E]**

Identification of logical decision factors (conditions/questions) and the possible system actions/outcomes.

**[Variant F]**

Elicited statements and business rules are available for formalization/structuring.

## Step-by-Step Procedure

**[Variant A]**

Identify all decision conditions and list in Condition Stub.
2. Calculate required combinations (2^c for limited entry).
3. Populate Condition Entries systematically (Y/N patterns).
4. List all possible outcomes in Action Stub.
5. Check action boxes for each combination column.
6. Rationalize redundant columns if identical actions result.
7. Alternatively, draw as a branching Decision Tree.

**[Variant B]**

Identify all basic input conditions affecting the decision.
2. List all possible outcome actions.
3. Create a matrix grid with conditions on top and actions below.
4. Populate condition columns with Yes/No/Don't Care combinations.
5. Mark the corresponding actions for each condition column.
6. Check table for completeness, contradictions, and redundant rules.

**[Variant C]**

Identify all atomic input conditions and output actions.
2. Create a table with input conditions in top rows and output actions in bottom rows.
3. Populate top columns with all 2^N true/false combinations for N input conditions.
4. Specify corresponding output actions for each column.
5. Eliminate impossible columns based on known domain properties.
6. Merge redundant columns that yield identical outputs to simplify the table.
7. Check for missing columns (incompleteness) or extra columns (redundancy).

**[Variant D]**

Identify all condition variables and their possible values (e.g., Yes/No, ranges).
2. Calculate all potential condition combinations.
3. Determine the required system result for each combination.
4. Simplify/collapse redundant rules if logic permits.

**[Variant E]**

Identify all decision factors/conditions and their possible values (e.g., True/False, Yes/No).
2. Calculate total theoretical combinations (e.g., 2^N for N binary conditions).
3. List all possible system actions/outcomes.
4. Construct a table or tree mapping each condition combination to its corresponding action.
5. Combine or collapse redundant rules where certain condition values are don't-care/irrelevant.
6. Verify that every combination has an explicit, defined system action.

**[Variant F]**

Apply local technical writing stylistic rules (short sentences, 'shall' for mandatory, define concepts before use, single requirement per sentence).
2. For complex logic: (a) Construct a Decision Table with input conditions on top and output actions on bottom; (b) Enumerate all 2^N truth value combinations; (c) Simplify table by eliminating impossible domain cases and merging redundant columns; (d) Verify completeness (column count).
3. Instantiate predefined requirement templates, including unique ID, category, specification, fit criterion, source, rationale, and priority.

## Analyst Questions & Prompts

**[Variant A]**

What conditions affect this decision? What are the possible Y/N answers? What exact action results from this specific combination of conditions?

**[Variant B]**

What conditions determine this discount? What action happens if condition A is true but condition B is false?

**[Variant C]**

What are all the atomic conditions affecting this decision? What output must occur if condition 1 is True, condition 2 is False, and condition 3 is True?

**[Variant D]**

What happens if condition A is met but condition B fails? Are all possible logical combinations accounted for?

**[Variant E]**

What factors influence this decision? If Condition A is True and Condition B is False, what should the system do? Are there combinations of conditions that cannot occur in reality?

**[Variant F]**

Is this sentence ambiguous? What is the exact fit criterion to measure satisfaction? Are all 2^N combinations of input conditions accounted for in this rule?

## Minimal Realistic Example

**[Variant A]**

A rail fare decision table with 2 conditions ('Travel after 10am?', 'Aged 60+?') generating 4 condition columns mapping to 4 distinct ticket price actions (Full, Full-20%, Off-peak, Off-peak-20%).

**[Variant B]**

Matrix listing 6 discount conditions (e.g., 'Before 6pm', 'Hotel <50% booked') mapped to specific discount percentage actions (e.g., 'Room discount 25%').

**[Variant C]**

Structuring train braking rules into an 8-column table revealing a missing edge case: 'Train enters station block too fast AND preceding train is too close AND command is NOT outdated.'

**[Variant D]**

Matrix evaluating 'Evidence complete', 'Confidence above threshold', and 'Policy conflict' to yield outcomes: Request missing information, Analyst review, Specialist review, or Automated path.

**[Variant E]**

Evaluates Chemical Request Acceptance based on 4 binary conditions (Authorized User, Available Chemical, Hazardous, Trained User), condensing 16 combinations into 5 distinct rules.

**[Variant F]**

Replacing a vague 3-line paragraph on train braking with an 8-column decision table detailing exact full braking and alarm responses across combinations of speed, command age, and distance.

## Quality Criteria & Verification

**[Variant A]**

Completeness (all 2^c condition combinations accounted for); elimination of logical contradictions and redundant rules.

**[Variant B]**

Logical completeness check (2^N conditions check), test case generation covering all table columns.

**[Variant C]**

Mathematical check for completeness (column count matches 2^N before simplification); cause-effect test case generation.

**[Variant D]**

Completeness check (2^n rules represented or explicitly consolidated); no contradictory outputs for identical inputs.

**[Variant E]**

Completeness check ensuring all 2^N condition outcomes are accounted for; peer review by SMEs; test case generation directly from table columns.

**[Variant F]**

Completeness check on decision tables (column count = 2^N before reduction); non-ambiguity; testability via fit criteria; local style rule adherence.

## Errors & Anti-Patterns

**[Variant A]**

Creating massive un-nested tables for >5 conditions without using hierarchical sub-tables; missing condition combination columns.

**[Variant B]**

Attempting to model sequential program loops or procedural workflows inside decision tables.

**[Variant C]**

Including non-atomic or overlapping conditions; failing to document why an eliminated column is physically impossible.

**[Variant D]**

Overlooking negative combinations, leaving missing conditions blank, embedding rules implicitly inside unstructured prose.

**[Variant E]**

Overlooking undefined condition combinations in narrative text; failing to consolidate redundant 'don't care' cells; confusing business rules with functional processing steps.

**[Variant F]**

Mixing 'and'/'or' connectives resulting in logical tautologies; overspecifying algorithmic implementation details instead of declarative rules; omitting fit criteria.

## When NOT to Use

**[Variant A]**

For simple 1-condition binary choices (use a basic activity diagram decision diamond instead).

**[Variant B]**

Simple, unconditional functions or highly algorithmic code with loops.

**[Variant C]**

When the logic is sequential, time-series dependent, or involves simple non-combinatorial rules.

**[Variant D]**

Simple linear processes with no conditional branching or simple single-rule scenarios.

**[Variant E]**

For simple linear workflows without complex conditional branching.

**[Variant F]**

When full formal mathematical specification is required for ultra-critical safety proofs, or when informal quick notes suffice for low-risk agile iterations.

## Alternatives & Complementary Methods

**[Variant A]**

Activity Diagrams, Business Rules Analysis, Task Analysis.

**[Variant B]**

Textual Process Descriptions (Pseudo-code), Activity Diagrams.

**[Variant C]**

Complementary: Structured Natural Language, SCR Condition Tables. Alternative: Flowcharts, State Machine Diagrams.

**[Variant D]**

Decision Trees, Atomic Functional Requirements, Executable Acceptance Examples.

**[Variant E]**

Event-Response Table, Activity Diagram, Natural Language (EARS syntax).

**[Variant F]**

Free natural language prose, Diagrammatic notations (UML), Formal specification (Z, LTL, SCR).

## Supported Decisions

**[Variant A]**

Complex decision logic design, business rule automation, test case scenario generation.

**[Variant B]**

Business rules engine configuration, pricing logic specification, automated test case design.

**[Variant C]**

Verifying rule completeness, acceptance test case design.

**[Variant D]**

Acceptance, business logic compliance, release verification.

**[Variant E]**

Acceptance, compliance, architecture.

**[Variant F]**

Test case design, specification acceptance, baseline contract definition.

## AI & Agentic Adaptation

**[Variant A]**

AI rule-engine tools convert natural language policy documents directly into verified, gap-free Decision Tables and executable business rules code.

**[Variant B]**

Automatically generate complete decision tables from raw business policy text using AI logic parsers.

**[Variant C]**

LLM agents can ingest complex unstructured prose requirements, auto-generate decision tables, and output formal notices of missing logical combinations.

**[Variant D]**

Provides explicit guardrail evaluation matrix for routing agent outputs vs. requiring human escalation.

**[Variant E]**

Not in source

**[Variant F]**

LLM prompt pipelines can analyze unrestricted natural language requirements, rewrite them using controlled technical grammar, construct complete 2^N decision tables, and flag ambiguous logic.
