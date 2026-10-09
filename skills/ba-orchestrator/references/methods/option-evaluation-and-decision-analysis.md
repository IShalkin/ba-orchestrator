---
id: option-evaluation-and-decision-analysis
name: "Option Evaluation and Decision Analysis"
task: T1
task_name: "Strategy Analysis and Justification"
subtask: "1.4"
subtask_name: "Solution Options and Feasibility"
source_count: 4
---

# Option Evaluation and Decision Analysis

`T1 Strategy Analysis and Justification › 1.4 Solution Options and Feasibility`

**Also described as:** Decision Analysis; Decision Matrix; Evaluating Alternative Options (Decision Making / NFR Framework); Option Evaluation (Qualitative NFR & Quantitative Weighted Matrices)

This card merges 4 descriptions of the method, labelled Variant A–D in every field.

## Problem Solved

**[Variant A]**

Reduces arbitrary or sub-optimal decision making when choosing among competing system proposals, goal refinements, responsibility assignments, or architecture styles.

**[Variant B]**

Reduces decision uncertainty when choosing among alternative goal refinements, architectural options, risk countermeasures, or responsibility assignments.

**[Variant C]**

Reduces decision bias and uncertainty when evaluating complex, high-risk alternatives with conflicting objectives and multi-criteria outcomes.

**[Variant D]**

Provides a quantitative, objective scoring framework to select the best solution alternative among competing options.

## BA Lifecycle Phase

**[Variant A]**

Evaluation / analysis

**[Variant B]**

Evaluation / decision making

**[Variant C]**

Strategy / prioritisation / Solution Evaluation / change management

**[Variant D]**

Negotiation / Prioritisation

## Input Artifacts

**[Variant A]**

Alternative options (refinements, assignments, resolutions), soft goals (quality requirements), fit criteria, evaluation criteria.

**[Variant B]**

Alternative system options, non-functional requirements (NFRs), criteria weights.

**[Variant C]**

Problem statement, solution options, risk assessment results, evaluation criteria, financial estimates.

**[Variant D]**

Solution alternatives, weighted decision criteria (from CAF)

## Output Artifacts

**[Variant A]**

NFR contribution graphs, qualitative satisficing labels (++, +, -, --, S, D, C, U), weighted decision matrices, selected 'best' option proposal.

**[Variant B]**

NFR contribution tables (+/++/-/-- labels), weighted decision matrices, selected 'best' system option.

**[Variant C]**

Simple/weighted decision matrices, decision trees, trade-off rankings, recommended action report.

**[Variant D]**

Completed decision matrix table with numerical scores and winning option

## Participants & Roles

**[Variant A]**

BA, System Architect, Business Owner, Sponsor, Stakeholders.

**[Variant B]**

Business Analyst, System Architect, Key Stakeholders / Decision Makers.

**[Variant C]**

Decision Maker, Sponsor, BA, SME, Project Manager.

**[Variant D]**

Requirements Engineer / Facilitator, Key Stakeholders / Decision Makers

## Prerequisites

**[Variant A]**

Alternative system options and non-functional soft goals have been identified.

**[Variant B]**

Elicited non-functional quality goals to serve as evaluation criteria; identified mutually exclusive alternatives.

**[Variant C]**

Clearly defined problem statement, list of alternatives, and pre-agreed evaluation criteria.

**[Variant D]**

Clear set of solution alternatives and established evaluation criteria.

## Step-by-Step Procedure

**[Variant A]**

Identify evaluation criteria from non-functional soft goals.
2. For Qualitative Reasoning (NFR Framework): (a) Assess individual positive/negative contributions (+, ++, -, --) of options to leaf soft goals; (b) Propagate labels (S, D, C, U) upwards along goal contribution paths to evaluate top-level goal satisficing; (c) Select the option best satisficing top goals.
3. For Quantitative Reasoning (Weighted Matrices): (a) Assign relative weights to criteria; (b) Score each option (% satisfaction or gauge variables); (c) Compute total weighted score; (d) Select the highest-scoring option.

**[Variant B]**

Identify the mutually exclusive alternative options to be evaluated.
2. Establish evaluation criteria based on elicitation of non-functional quality requirements.
3. Assign relative importance weights to each criterion.
4. (Qualitative) Map the positive or negative contribution (+, ++, -, --) of each option to each NFR criterion and propagate along goal graphs.
5. (Quantitative) Score each option's satisfaction percentage against each criterion and compute total weighted scores: TotalScore = Sum(Score_i * Weight_i).
6. Select the highest-scoring option and document the decision rationale.

**[Variant C]**

Clearly define the decision problem statement.
2. Identify all possible alternatives or courses of action.
3. Establish decision criteria and assign importance weightings.
4. Evaluate each alternative against criteria using decision matrices or decision trees.
5. Eliminate dominated alternatives and evaluate trade-offs.
6. Select the optimal alternative to implement and document rationale.

**[Variant D]**

Create a matrix table with solution alternatives in columns and decision criteria in rows.
2. Assign weight/importance ratings to each criterion if applicable.
3. Evaluate each alternative against each criterion using a standardized point scale (e.g., 0 to 10).
4. Sum the total scores for each column.
5. Select the alternative with the highest total score.

## Analyst Questions & Prompts

**[Variant A]**

How does alternative X contribute to soft goal Y? Which option maximizes overall weighted satisficing of our quality requirements? What is the cumulative cost vs benefit of this assignment?

**[Variant B]**

How does option A impact our usability goal compared to option B? What weight should we give to response time vs operational cost? Which alternative offers the optimal trade-off?

**[Variant C]**

"What are the key criteria governing this decision and their relative weights?", "What is the expected value of option A under uncertain condition X?", "Which alternative dominates the others?"

**[Variant D]**

"How does Alternative 1 rate against Criterion 2 on a scale of 0 to 10?", "Are all decision criteria included in the matrix?"

## Minimal Realistic Example

**[Variant A]**

Comparing 'e-mail request' vs 'e-agenda access' options against soft goals 'Fast Response', 'Reliable Response', and 'Minimal Inconvenience', leading to selecting 'e-agenda' due to higher convenience and speed.

**[Variant B]**

Evaluating 'Constraints via E-mail' vs 'Constraints via E-agenda'. E-agenda scores 100% on 'Minimal Inconvenience' but 30% on 'Reliable Accuracy', resulting in a lower weighted total score than the E-mail option.

**[Variant C]**

A weighted decision matrix evaluates 3 ERP vendors across Cost (weight 5), Usability (weight 3), and Security (weight 4); Option 2 wins with a score of 40 vs 37 and 28.

**[Variant D]**

Stakeholders evaluate 3 routing algorithm designs across 'Cost', 'Speed', and 'Accuracy'. Alternative 1 scores 18 total points, beating Alternative 2 (13) and 3 (17).

## Quality Criteria & Verification

**[Variant A]**

Consistently assigned scores/weights grounded in expert judgment; clear traceability from selected options to non-functional goals.

**[Variant B]**

Sensitivity analysis of weights/scores in spreadsheets; stakeholder consensus on assigned criteria weights.

**[Variant C]**

Evaluation criteria are agreed upon up-front; trade-off calculations are transparent and reproducible; decision maker accepts remaining uncertainty.

**[Variant D]**

Objective, repeatable numerical evaluation; explicit justification for individual scores.

## Errors & Anti-Patterns

**[Variant A]**

Selecting technical options without mapping them to non-functional quality criteria; subjective score assignment without consistency checks; ignoring cross-cutting impacts of choices.

**[Variant B]**

Failing to make non-functional evaluation criteria explicit; manipulating scores artificially to justify a biased preference.

**[Variant C]**

Analysis paralysis by spending excessive effort on probabilistic modelling; forcing emotional decisions into a matrix to justify a preconceived choice.

**[Variant D]**

Manipulating score points to favor a personal preference regardless of objective criteria.

## When NOT to Use

**[Variant A]**

When there is only one feasible way to satisfy a requirement, or when options carry identical risk and quality profiles.

**[Variant B]**

When one option is strictly mandatory due to absolute legal, regulatory, or hard technical constraints.

**[Variant C]**

When decisions must be made instantaneously in emergencies, or when information is too scarce to establish meaningful criteria.

**[Variant D]**

When decision criteria cannot be quantified or when stakeholders agree informally without complex math.

## Alternatives & Complementary Methods

**[Variant A]**

Analytic Hierarchy Process (AHP), Cost-Benefit Analysis, Multi-Criteria Decision Analysis (MCDA).

**[Variant B]**

Complementary: Goal Modeling (NFR framework), DDP. Alternative: Analytic Hierarchy Process (AHP).

**[Variant C]**

Alternatives/Complements include Decision Modelling, Business Cases, Financial Analysis, and SWOT Analysis.

**[Variant D]**

Plus-Minus-Interesting, AHP (Analytic Hierarchy Process)

## Supported Decisions

**[Variant A]**

Architecture style selection, automation boundary decisions, goal refinement path selection.

**[Variant B]**

System boundary selection, architectural style choice, conflict resolution trade-offs.

**[Variant C]**

Vendor selection, design option selection, change strategy recommendations, risk treatment response.

**[Variant D]**

Architecture selection, feature baseline inclusion, vendor choice.

## AI & Agentic Adaptation

**[Variant A]**

Agentic systems can evaluate option trade-offs by executing qualitative label propagation rules across complex goal models and running multi-criteria scoring algorithms based on telemetry data.

**[Variant B]**

AI decision-support agents can run automated multi-criteria sensitivity analysis and generate natural language rationale summaries for trade-off options.

**[Variant C]**

Agents can evaluate multi-attribute decision matrices automatically based on parsed vendor proposals, conducting sensitivity analysis to highlight key trade-off variables.

**[Variant D]**

Decision matrices auto-calculated by agentic evaluation models with rationale citations provided for every score assignment.
