---
id: ears
name: "EARS"
task: T5
task_name: "Requirements Specification"
subtask: "5.6"
subtask_name: "Requirements Documents and Phrasing"
source_count: 2
---

# EARS

`T5 Requirements Specification › 5.6 Requirements Documents and Phrasing`

**Also described as:** EARS (Easy Approach to Requirements Syntax); Easy Approach to Requirements Syntax (EARS) / Atomic Textual Requirements

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces ambiguity, subjective phrasing, compound obligations, and unstructured natural language requirements.

**[Variant B]**

Reduces ambiguity, subjective phrasing, passive-voice confusion, and inconsistent grammatical structures in natural language requirement statements.

## BA Lifecycle Phase

**[Variant A]**

Specification

**[Variant B]**

specification

## Input Artifacts

**[Variant A]**

Use cases, business rules, stakeholder requests.

**[Variant B]**

Elicited user needs, use case flows, event triggers, system states, conditional logic

## Output Artifacts

**[Variant A]**

Atomic functional requirements records with standardized structure.

**[Variant B]**

Structured functional requirement statements using standardized syntax templates

## Participants & Roles

**[Variant A]**

Business Analyst, Architect, Developer, Tester, Compliance.

**[Variant B]**

BA, developers, testers

## Prerequisites

**[Variant A]**

Glossary, clear domain concepts, defined system boundaries.

**[Variant B]**

Clear understanding of the actor/system taking action, preconditions, trigger events, and expected observable responses.

## Step-by-Step Procedure

**[Variant A]**

Identify specific system triggers, states, or conditions.
2. Select applicable EARS pattern (Ubiquitous, Event-driven, State-driven, Unwanted behaviour, Optional).
3. Draft requirement using pattern: Condition/trigger, the system shall observable response object qualifier.
4. Perform quality checks (singular, unambiguous, verifiable).

**[Variant B]**

Identify whether the requirement describes system behavior or user capability.
2. Identify optional preconditions or state conditions.
3. Identify optional triggering events.
4. Apply the generic system structure: 'optional precondition optional trigger event the system shall expected system response'.
5. Apply the generic user structure: 'The user class shall be able to do something to some object'.
6. Ensure active voice and a standard keyword (such as 'shall') are consistently applied.

## Analyst Questions & Prompts

**[Variant A]**

When does this happen? While in what state? What exact response must the system produce? How will we test this?

**[Variant B]**

What event triggers this system behavior? What precondition must be true before the system responds? Which specific user class is performing this action?

## Minimal Realistic Example

**[Variant A]**

FR-TRI-02: If one or more mandatory evidence categories are absent, the Triage Service shall set the case status to More information required and identify every absent category.

**[Variant B]**

If the requested chemical is found in the chemical stockroom, the system shall display a list of all containers of the chemical that are currently in the stockroom.

## Quality Criteria & Verification

**[Variant A]**

Requirement characteristics (Necessary, Appropriate, Unambiguous, Complete, Singular, Feasible, Verifiable, Correct, Conforming).

**[Variant B]**

Verify that requirements follow explicit syntax rules, contain no fuzzy/subjective terms, are written in active voice, and are individually testable.

## Errors & Anti-Patterns

**[Variant A]**

Using vague words ('user-friendly', 'fast', 'seamless', 'appropriate'), passive voice, design pre-determination, combining multiple triggers/obligations into one sentence.

**[Variant B]**

Using imprecise verbs like 'should' or 'may' to connote priority; using double/triple negatives; using slash constructs ('A/B') that create ambiguous options; combining multiple requirements into compound 'and/or' sentences.

## When NOT to Use

**[Variant A]**

High-level goal setting or open-ended exploratory product discovery.

**[Variant B]**

Complex multi-variable decision rules (where tabular representations work better) or visual workflow processes better described with models.

## Alternatives & Complementary Methods

**[Variant A]**

Decision Tables (for rule combinations), State Models, Acceptance Examples.

**[Variant B]**

Tabular requirement representation, Decision Tables, User Stories, Planguage.

## Supported Decisions

**[Variant A]**

Acceptance, architecture, compliance.

**[Variant B]**

Architecture, release, acceptance.

## AI & Agentic Adaptation

**[Variant A]**

Add metadata fields for guardrails, audit logging requirements, and specific automated fallback behaviors.

**[Variant B]**

Not in source
