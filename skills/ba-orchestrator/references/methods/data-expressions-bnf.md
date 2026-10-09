---
id: data-expressions-bnf
name: "Data Expressions (BNF)"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 1
---

# Data Expressions (BNF)

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Data Expressions (BNF / Regular Expressions)

## Problem Solved

Reduces ambiguity in nested, sequence-dependent, or composite data structures and message protocols.

## BA Lifecycle Phase

analysis

## Input Artifacts

Interface descriptions, data flow inputs, message format definitions.

## Output Artifacts

Data expression formulas (BNF/Regular expressions).

## Participants & Roles

BA, system architect, developer, tester.

## Prerequisites

Identification of composite data flows or structured message protocols.

## Step-by-Step Procedure

Identify composite data elements or message exchanges.
2. Define sequential composition using concatenation operators (+ or implicit).
3. Mark optional data using brackets .
4. Mark repeated data structures using braces {}.
5. Define choices/alternatives using vertical bars ( | ).
6. Define literal value options.

## Analyst Questions & Prompts

In what order do these data fields appear? Which fields are optional? How many times can this group repeat?

## Minimal Realistic Example

booking request = guest data + period + room type; guest data = guest name + address + passport number.

## Quality Criteria & Verification

Verification against syntax rules; syntax-driven test case generation for boundary testing.

## Errors & Anti-Patterns

Attempting to model cyclic/recursive domain data structures leading to infinite loops.

## When NOT to Use

Describing large, non-sequential entity-relationship databases.

## Alternatives & Complementary Methods

Data Model, Data Dictionary, Sequence Diagrams.

## Supported Decisions

Technical message protocol design, API payload validation rules.

## AI & Agentic Adaptation

Utilize AI parser agents to translate raw interface specs or XML/JSON samples into BNF expressions.
