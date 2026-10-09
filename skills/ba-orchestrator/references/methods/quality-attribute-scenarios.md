---
id: quality-attribute-scenarios
name: "Quality Attribute Scenarios"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 1
---

# Quality Attribute Scenarios

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

**Also described as:** Quality-Attribute Scenarios

## Problem Solved

Converts vague quality claims (e.g., 'scalable', 'fast', 'secure') into precise, measurable, verifiable architecture-significant obligations.

## BA Lifecycle Phase

Analysis / Specification / Architecture Handoff

## Input Artifacts

Non-functional requirements, architectural risks, business constraints.

## Output Artifacts

6-part Quality-Attribute Scenario statements (Source, Stimulus, Environment, Artifact, Response, Response Measure).

## Participants & Roles

Business Analyst, Architect, Developer, Tester, Security/Compliance.

## Prerequisites

Understanding of solution context, operational environments, and critical quality attributes.

## Step-by-Step Procedure

Identify quality attribute concern (e.g., performance, security, availability).
2. Specify Source of Stimulus and Stimulus.
3. Define Environment context and affected Artifact boundary.
4. Define system Response and precise numerical Response Measure.

## Analyst Questions & Prompts

Who or what triggers the event? Under what operational state? Which component responds? How fast/reliable must it be measured over what interval?

## Minimal Realistic Example

During normal operation, when an analyst opens a evaluated case, the Case Review interface shall display recommendation within 2 seconds for at least 95% of requests over a rolling 15-minute interval.

## Quality Criteria & Verification

Scenario contains all 6 elements; includes measurable, non-subjective acceptance threshold.

## Errors & Anti-Patterns

Using unmeasurable adjectives ('user-friendly', 'robust'); analyst inventing arbitrary targets without stakeholder or technical validation.

## When NOT to Use

Low-risk, non-critical features where standard system baseline performance/security defaults suffice.

## Alternatives & Complementary Methods

Fit Criteria (Volere), Non-Functional Requirements Catalog.

## Supported Decisions

Architecture design, release criteria, SLA compliance.

## AI & Agentic Adaptation

Specifies thresholds for AI latency, confidence levels, hallucination tolerance, and security audit logging response times.
