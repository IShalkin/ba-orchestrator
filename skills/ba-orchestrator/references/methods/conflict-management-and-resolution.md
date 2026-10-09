---
id: conflict-management-and-resolution
name: "Conflict Management and Resolution"
task: T3
task_name: "Stakeholders"
subtask: "3.3"
subtask_name: "Engagement, Conflict and Negotiation"
source_count: 2
---

# Conflict Management and Resolution

`T3 Stakeholders › 3.3 Engagement, Conflict and Negotiation`

**Also described as:** Conflict Management and Resolution Tactics; Inconsistency Management and Conflict Resolution

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces contradiction, divergence, and misalignment among multi-stakeholder requirements and non-functional concerns.

**[Variant B]**

Reduces inconsistencies, divergence, and stakeholder disagreements between overlapping requirements or goals.

## BA Lifecycle Phase

**[Variant A]**

Evaluation / negotiation

**[Variant B]**

Evaluation / negotiation

## Input Artifacts

**[Variant A]**

Overlapping requirements, stakeholder win conditions, interaction matrices, goal models.

**[Variant B]**

Overlapping/conflicting requirements, interaction matrix, boundary conditions for divergence.

## Output Artifacts

**[Variant A]**

Conflict interaction matrix, boundary conditions, agreed conflict resolutions, weakened/revised requirements.

**[Variant B]**

Documented conflict logs, boundary conditions, agreed conflict resolutions (weakened/modified statements).

## Participants & Roles

**[Variant A]**

BA, Stakeholders (with conflicting views), Business Owner, Sponsor.

**[Variant B]**

Business Analyst, Conflicting Stakeholders, Project Decision Maker / Sponsor.

## Prerequisites

**[Variant A]**

Requirements or goals have been elicited from multiple sources and checked for overlaps.

**[Variant B]**

Identification and formal/informal detection of overlapping requirements or divergence.

## Step-by-Step Procedure

**[Variant A]**

Identify overlapping statements referring to common/interrelated concepts.
2. Detect conflicts/divergences (formally, heuristically, or informally) and identify boundary conditions making them inconsistent.
3. Document conflicts using interaction matrices or requirements database links.
4. Generate alternative resolutions using resolution tactics (Avoid boundary condition, Restore, Weaken, Drop lower priority, Specialize source/target).
5. Evaluate alternative resolutions against soft goals.
6. Negotiate with stakeholders to select the mutually agreed 'best' resolution.

**[Variant B]**

Identify overlapping statements referencing common domain phenomena.
2. Detect conflicts or calculate boundary conditions that make statements logically inconsistent.
3. Document conflicts using an interaction matrix or requirements database links.
4. Generate alternative conflict resolutions using resolution tactics (Avoid boundary condition, Restore statements, Weaken statements, Drop lower-priority statement, Specialize source/target).
5. Evaluate alternative resolutions against non-functional quality goals.
6. Negotiate with stakeholders to select and approve the best compromise.

## Analyst Questions & Prompts

**[Variant A]**

Under what boundary condition do these two statements become incompatible? Can we weaken statement A without violating its core objective? Which stakeholder win condition has higher priority?

**[Variant B]**

Under what specific conditions do these two requirements contradict each other? Can we weaken this requirement for lower-priority user groups? Can we restrict the scope of this rule to staff users only?

## Minimal Realistic Example

**[Variant A]**

Detecting a divergence between 'Return books within 2 weeks' and 'Keep books as long as needed' under the boundary condition 'Needing book > 2 weeks', and resolving it by allowing online loan renewals.

**[Variant B]**

Resolving a divergence between 'Borrowers return books in 2 weeks' and 'Borrowers keep books as long as needed' by applying the 'Avoid Boundary Condition' tactic—retaining reference-only copies on library shelves at all times.

## Quality Criteria & Verification

**[Variant A]**

Complete elimination of strong logical contradictions; stakeholder consensus on win-win trade-offs; formal consistency verification.

**[Variant B]**

Logical consistency verification of resolved statements; formal check that boundary condition can no longer hold; stakeholder sign-off on compromise.

## Errors & Anti-Patterns

**[Variant A]**

Resolving conflicts too prematurely before understanding root goals; ignoring weak conflicts (divergences) that only manifest under rare boundary conditions; overriding user concerns without authority.

**[Variant B]**

Resolving conflicts too prematurely before exploring stakeholder perspectives; ignoring weak conflicts (divergence) that only manifest under rare edge conditions; jumping to a single resolution without exploring options.

## When NOT to Use

**[Variant A]**

When statements do not overlap or when inconsistencies represent trivial terminology clashes (which should be solved via glossaries).

**[Variant B]**

When statements do not overlap or when apparent conflicts are merely terminology/designation clashes (which should be fixed via a glossary).

## Alternatives & Complementary Methods

**[Variant A]**

Goal refinement, risk analysis, multicriteria decision analysis.

**[Variant B]**

Complementary: Goal Modeling, Win-Win Negotiation, Analytic Hierarchy Process (AHP).

## Supported Decisions

**[Variant A]**

Scope trade-offs, priority setting, policy harmonization.

**[Variant B]**

Scope determination, policy trade-offs, priority ranking.

## AI & Agentic Adaptation

**[Variant A]**

Logic-based AI agents can automatically detect divergences using boundary condition generators, propose tactic-based resolutions, and simulate the trade-off impact on soft goals.

**[Variant B]**

Logic-based AI agents can detect formal divergences, compute boundary conditions, and automatically suggest tactical weakenings using pre-defined resolution patterns.
