---
id: onion-model
name: "Onion Model"
task: T3
task_name: "Stakeholders"
subtask: "3.1"
subtask_name: "Stakeholder Identification"
source_count: 1
---

# Onion Model

`T3 Stakeholders › 3.1 Stakeholder Identification`

**Also described as:** Onion Model (Stakeholder Analysis)

## Problem Solved

Reduces omission of critical non-operational stakeholders (regulators, beneficiaries, negative stakeholders) and clarifies project context/boundaries.

## BA Lifecycle Phase

Discovery

## Input Artifacts

Sponsor requests, organization charts, project vision, context models

## Output Artifacts

Stakeholder map (onion diagram), stakeholder matrix, influence diagrams, stakeholder responsibility lists

## Participants & Roles

BA, Sponsor, Client, SME, Product Manager, Architect

## Prerequisites

Project mission, sponsor brief, initial domain/context knowledge

## Step-by-Step Procedure

Place the product/service at the center of the concentric ring model.
2. Identify operational roles in the innermost ring ('The System').
3. Identify functional, financial, political, and social beneficiaries in 'The Containing System'.
4. Identify regulators, champions, purchasers, developers, and negative stakeholders in 'The Wider Environment'.
5. Label connections and draw influence/interaction arrows between roles.
6. Validate the diagram with project sponsors and domain experts.

## Analyst Questions & Prompts

Who has a valid interest in this product? Who will operate it? Who will benefit financially or functionally? Who regulates this domain? Who might oppose or be harmed by this system? Who interacts with or influences this role?

## Minimal Realistic Example

Mapping a city tram service: innermost system includes tram drivers and mechanics; containing system includes passengers (functional beneficiaries) and the tram operating firm (financial beneficiary); wider environment includes city councils, safety regulators, and local residents (potential negative stakeholders).

## Quality Criteria & Verification

Checked against context diagrams and interviews; covers operational, beneficiary, regulatory, and negative roles exhaustively; verified via stakeholder walkthroughs.

## Errors & Anti-Patterns

Focusing only on direct software users; treating surrogate roles as end-users without validation; ignoring negative stakeholders or regulatory bodies.

## When NOT to Use

In extremely trivial or well-understood internal tasks where stakeholders are strictly fixed and known.

## Alternatives & Complementary Methods

Organization charts, Soft Systems Methodology (Rich Pictures), Context Diagrams, i* Strategic Dependency Diagrams.

## Supported Decisions

Scope definition, stakeholder engagement strategy, project governance, resource allocation.

## AI & Agentic Adaptation

Agentic role discovery: LLM agents analyze project documentation, organizational charts, and regulations to automatically generate draft Onion Models and identify overlooked regulatory or security stakeholders. Human-in-the-loop validation is required to confirm stakeholder power and alignment.
