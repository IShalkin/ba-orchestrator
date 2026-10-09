---
id: roles-and-permissions-matrix
name: "Roles and Permissions Matrix"
task: T5
task_name: "Requirements Specification"
subtask: "5.5"
subtask_name: "Non-Functional Requirements"
source_count: 1
---

# Roles and Permissions Matrix

`T5 Requirements Specification › 5.5 Non-Functional Requirements`

## Problem Solved

Reduces security breaches, governance failures, and activity gaps by defining role authorities, data access permissions, and segregation of duties.

## BA Lifecycle Phase

analysis / specification / Solution Evaluation

## Input Artifacts

Org models, job descriptions, process models, use cases, security policies.

## Output Artifacts

Roles and Permissions Matrix (Role groups vs. Activities/Data; CRUD or RACI designations), authority delegation rules.

## Participants & Roles

BA, Security/Compliance Lead, System Admin, SME, Business Owner.

## Prerequisites

Identified organizational user roles and system activities/data entities.

## Step-by-Step Procedure

Identify distinct user roles sharing common functions and permissions.
2. Identify system activities, functions, or data entities (e.g., Create, Read, Update, Delete).
3. Map authority permissions for each role across each activity/data entity in a matrix.
4. Define security levels, segregation of duties, and authorization constraints.
5. Specify delegation and organizational hierarchy inheritance rules.
6. Validate permission matrix with security leads and business owners.

## Analyst Questions & Prompts

"Which roles are authorized to perform action X?", "Does role A have permission to Delete record Y?", "Are there segregation of duty conflicts between role A and B?"

## Minimal Realistic Example

A CRUD matrix defines that 'Sales Rep' role has 'Create/Read' permissions on 'Orders', while 'Sales Manager' has 'Create/Read/Update/Delete' permissions.

## Quality Criteria & Verification

All system activities covered; no security policy or segregation-of-duties violations; explicit authority for every role.

## Errors & Anti-Patterns

Creating an overly granular matrix that becomes an administrative nightmare; neglecting to define delegation and revoking procedures.

## When NOT to Use

On open-access public systems where all users possess identical, unrestricted permissions.

## Alternatives & Complementary Methods

Complemented by RACI Matrix, Organizational Modelling, Use Cases, and Security NFR Analysis.

## Supported Decisions

System security design, compliance/audit approval, user access control configuration.

## AI & Agentic Adaptation

AI agents can audit roles and permissions matrices automatically against corporate compliance rules, flagging segregation-of-duty policy violations.
