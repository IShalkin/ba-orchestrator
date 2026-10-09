---
id: security-risk-assessment
name: "Security Risk Assessment"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 1
---

# Security Risk Assessment

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

## Problem Solved

Identifies threat vulnerabilities, estimates financial losses per incident, and calculates annual expected losses to prioritize security safeguards.

## BA Lifecycle Phase

analysis

## Input Artifacts

System context diagram, threat catalogs, business asset values.

## Output Artifacts

Security Risk Assessment Table (Threats, Annual Frequency, Loss per Hit, Total Loss per Year, Proposed Safeguards).

## Participants & Roles

BA, security specialist, business owner, IT operations manager.

## Prerequisites

Identification of critical system assets and data flows.

## Step-by-Step Procedure

List potential threats across Input, Storage, and Output processes.
2. Estimate annual occurrence frequency for each threat (e.g., 10, 1, 0.1).
3. Estimate financial loss per hit ( $).
4. Multiply frequency by loss per hit to calculate total expected annual loss ($ /year).
5. Identify high-loss threat areas and evaluate cost-effective safeguards (Prevention, Detection, Repair).

## Analyst Questions & Prompts

What is the financial impact if our database is completely lost? How frequently do we expect virus or credit fraud attacks?

## Minimal Realistic Example

Threat: Disk crash. Frequency: 0.3/year. Loss per hit: $100,000. Annual Loss: $30,000/year. Proposed Safeguard: RAID mirrored disks.

## Quality Criteria & Verification

Review by certified security auditors, financial risk alignment.

## Errors & Anti-Patterns

Ignoring soft threats (like internal fraud) while over-investing in extreme, low-probability threats (like nuclear attack).

## When NOT to Use

Minor non-critical applications holding no sensitive data or financial assets.

## Alternatives & Complementary Methods

Quality Grid, Threat and Safeguard Catalogs.

## Supported Decisions

Security budget allocation, safeguard selection, disaster recovery planning.

## AI & Agentic Adaptation

Analyze system architecture diagrams using security AI agents to automatically flag threat vectors and estimate risk scores.
