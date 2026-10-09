---
id: obstacle-and-risk-analysis-ddp-fault-trees
name: "Obstacle and Risk Analysis (DDP, Fault Trees)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.4"
subtask_name: "Goals, Obstacles and Rationale"
source_count: 3
---

# Obstacle and Risk Analysis (DDP, Fault Trees)

`T4 Modelling and Analysis › 4.4 Goals, Obstacles and Rationale`

**Also described as:** Obstacle Analysis (Goal-Anchored Risk Analysis); Risk Analysis and Control (Fault Trees / DDP); Risk Analysis and Management (DDP / Obstacle Analysis)

This card merges 3 descriptions of the method, labelled Variant A–C in every field.

## Problem Solved

**[Variant A]**

Reduces requirements incompleteness, unhandled operational risks, and false confidence arising from over-idealized system assumptions.

**[Variant B]**

Reduces over-idealism, unhandled exceptions, safety hazards, security threats, and operational failure risks in system requirements and environmental assumptions.

**[Variant C]**

Reduces product- and process-related risks, safety hazards, and security threats by identifying failure modes, evaluating exposures, and adding robust countermeasure requirements.

## BA Lifecycle Phase

**[Variant A]**

analysis

**[Variant B]**

Evaluation / analysis

**[Variant C]**

Evaluation / analysis

## Input Artifacts

**[Variant A]**

Goal model (leaf goals and assumptions), domain properties, obstacle taxonomies

**[Variant B]**

Goal model, environmental assumptions, domain properties, risk checklists, fault/threat trees.

**[Variant C]**

System objectives, goal models, risk checklists, component architecture, fault/threat trees.

## Output Artifacts

**[Variant A]**

Obstacle Diagram (AND/OR risk trees), Countermeasure Goals integrated into Goal Model

**[Variant B]**

Risk assessment tables, impact/effectiveness matrices (DDP), obstacle diagrams, countermeasure requirements.

**[Variant C]**

Risk assessment tables, fault trees, cut sets, impact/effectiveness matrices (DDP), countermeasure requirements.

## Participants & Roles

**[Variant A]**

BA, Risk Analyst, SME, Architect, Compliance/Legal

**[Variant B]**

BA, Risk Analyst, SME, System Architect, Safety/Security Specialist.

**[Variant C]**

Requirements Engineer, Safety/Security SME, System Architect, Domain Expert.

## Prerequisites

**[Variant A]**

A developed goal model with leaf goals and domain hypotheses explicitly specified.

**[Variant B]**

System goals, requirements, and environment assumptions have been initially formulated.

**[Variant C]**

Initial system goals and proposed functional capabilities identified.

## Step-by-Step Procedure

**[Variant A]**

SELECT: Pick critical leaf goals or domain hypotheses in the goal model.
2. IDENTIFY: Negate the selected assertion to form the root obstacle. Refine it via AND/OR links using tautologies, domain properties, or obstruction patterns until elementary obstacles are reached.
3. ASSESS: Estimate likelihood and criticality for each leaf obstacle.
4. CONTROL: Formulate alternative countermeasures (prevention, reduction, restoration, mitigation, goal weakening, agent substitution) and inject selected resolutions as new goals into the goal model.

**[Variant B]**

Identify product/process risks and obstacles (via checklists, component inspection, fault/threat trees, or regressing goal negations).
2. Assess risk likelihood and severity of consequences to calculate risk exposure or criticality.
3. Populate DDP impact and effectiveness matrices.
4. Explore alternative countermeasures using risk-reduction tactics (Reduce likelihood, Avoid risk, Mitigate consequence, Restore).
5. Calculate Risk Reduction Leverage (RRL) or DDP effectiveness vs cost.
6. Select cost-effective countermeasures and integrate them as new/revised goals in the goal model.

**[Variant C]**

Identify potential product/process risks using risk checklists, component inspection, fault/threat trees, or scenario WHAT-IF analysis.
2. Construct risk trees linking top-level failures to root causes via AND/OR logical nodes.
3. Assess risk likelihood and consequence severity qualitatively or quantitatively (calculating Risk Exposure = Likelihood x Severity).
4. Explore alternative countermeasures using risk-reduction tactics (Reduce likelihood, Avoid risk, Mitigate consequence).
5. Evaluate countermeasures using Risk Reduction Leverage (RRL) or DDP effectiveness matrices.
6. Select cost-effective countermeasures and integrate them as new system goals/requirements.

## Analyst Questions & Prompts

**[Variant A]**

What could go wrong to prevent this goal from being satisfied? What domain properties can fail? How likely and severe is this failure?

**[Variant B]**

What could go wrong with this assumption? What is the likelihood and severity of this hazard? Which countermeasure provides the highest risk-reduction leverage for its cost?

**[Variant C]**

What could go wrong if this component fails? What is the worst-case consequence of inaccurate speed data? How much does this countermeasure reduce our risk exposure?

## Minimal Realistic Example

**[Variant A]**

Negating the goal 'Train stopped at stop signal' yields obstacle 'Driver unresponsive'. Assessing its criticality as catastrophic leads to injecting the countermeasure goal 'Send periodic responsiveness checks'.

**[Variant B]**

Identifying the obstacle 'Train driver unresponsive' to the safety goal 'Stop at red signal', evaluating its catastrophic severity, and introducing the countermeasure requirement 'Send periodic driver responsiveness prompts'.

**[Variant C]**

Analyzing the risk 'Train doors open while moving' using a fault tree to reveal the cause 'Emergency signal raised while moving', leading to a countermeasure requirement: 'Door actuator shall ignore manual emergency signals unless speed = 0.'

## Quality Criteria & Verification

**[Variant A]**

Domain completeness of OR-refinements; domain consistency and minimality of AND-refinements; feasibility of leaf obstacles verified by domain experts.

**[Variant B]**

Domain completeness of identified obstacles; cost-effectiveness of selected countermeasures (RRL); elimination or mitigation of catastrophic risk exposures.

**[Variant C]**

Completeness of cut sets; quantitative balance verification via DDP optimization; hazard/threat validation by domain SMEs.

## Errors & Anti-Patterns

**[Variant A]**

Analyzing high-level goals directly instead of leaf goals; assuming environment agents behave ideally without exception.

**[Variant B]**

Assuming an over-ideal world where environment components never fail; subjective/inconsistent risk scoring without domain expert grounding; ignoring unstated environmental assumptions.

**[Variant C]**

Assuming over-ideal system behavior where nothing fails; treating qualitative risk scores as absolute mathematical facts; ignoring process risks like requirements volatility.

## When NOT to Use

**[Variant A]**

For non-critical features where obstacle occurrence carries minimal risk and cost-benefit analysis favors 'do nothing'.

**[Variant B]**

When the system is trivial, non-critical, and carries negligible financial, safety, or operational risk.

**[Variant C]**

In trivial, non-critical greenfield administrative software where risk exposure is negligible and development costs dictate minimal ceremony.

## Alternatives & Complementary Methods

**[Variant A]**

Fault Tree Analysis (FTA), Threat Tree Modeling, Failure Mode and Effects Analysis (FMEA)

**[Variant B]**

FMEA, Fault Tree Analysis (FTA), Threat Modeling (Anti-goals), Goal-oriented obstacle analysis.

**[Variant C]**

Complementary: Obstacle Analysis, Anti-Goal Modeling, FMEA. Alternative: Qualitative Risk Matrices.

## Supported Decisions

**[Variant A]**

System robustness decisions, architecture selection, risk control strategies, release acceptance

**[Variant B]**

Countermeasure selection, architecture robustness choices, release readiness.

**[Variant C]**

Safety/security architecture decisions, countermeasure scope selection, release readiness.

## AI & Agentic Adaptation

**[Variant A]**

Agentic systems can automatically negate temporal logic goal statements, query domain knowledge bases for potential pre-conditions of failure, and propose automated guardrails/countermeasures with Human-in-the-Loop review.

**[Variant B]**

Risk-reasoning AI agents can regress goal negations through domain properties to auto-generate obstacle trees, quantify risk exposures using historical data, and run simulated annealing algorithms to select optimal countermeasure packages under budget constraints.

**[Variant C]**

Agentic safety tools can automatically generate fault trees from structural goal models, run simulated annealing for optimal DDP countermeasure selection, and monitor risk thresholds.
