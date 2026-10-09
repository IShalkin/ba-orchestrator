---
id: quality-attribute-utility-tree
name: "Quality Attribute Utility Tree"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.6"
subtask_name: "Architecture Analysis"
source_count: 1
---

# Quality Attribute Utility Tree

`T4 Modelling and Analysis › 4.6 Architecture Analysis`

**Also described as:** Quality Attribute Utility Tree Construction

## Problem Solved

Solves prioritization conflicts and lack of specificity in quality attribute requirements by organizing and quantifying them.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Business goals, quality attribute requirements, system context documents.

## Output Artifacts

Utility Tree (hierarchical structure mapping Utility -> Quality Attributes -> Attribute Refinements -> Concrete Scenarios with (Importance, Risk) ratings).

## Participants & Roles

Software Architect, Lead Analysts, Key Business/Technical Stakeholders.

## Prerequisites

High-level understanding of required quality attributes and business goals.

## Step-by-Step Procedure

Define 'Utility' as the root node representing overall system goodness.
2. Identify main quality attribute categories (e.g., Performance, Security).
3. Refine categories into specific sub-attributes.
4. Write concrete 6-part scenarios at the leaves.
5. Prioritize leaf scenarios based on Business Importance (H/M/L) and Technical Risk (H/M/L).

## Analyst Questions & Prompts

How do we define overall system utility? What specific quality sub-attributes drive success? What concrete stimulus-response scenario exemplifies this sub-attribute? What is its business value and technical risk?

## Minimal Realistic Example

Utility -> Performance -> Latency -> 'Under peak load, a user updates an address and receives confirmation in < 0.75s' rated as (High Importance, High Risk).

## Quality Criteria & Verification

Every leaf scenario must have a measurable response measure; high-importance/high-risk (H,H) scenarios must be explicitly highlighted for architectural focus.

## Errors & Anti-Patterns

Leaving leaf nodes as vague statements (e.g., 'High Availability') without 6-part concrete scenarios; failing to involve business decision-makers in importance rating.

## When NOT to Use

Extremely small systems with no significant or complex quality attribute requirements.

## Alternatives & Complementary Methods

Quality Attribute Workshop (QAW), Architecture Tradeoff Analysis Method (ATAM).

## Supported Decisions

Architectural driver selection, iteration goal setting, trade-off decisions between conflicting quality attributes.

## AI & Agentic Adaptation

LLMs can automatically generate draft utility trees from unstructured requirements specifications. Human-in-the-loop validation is required to assign risk and importance ratings.
