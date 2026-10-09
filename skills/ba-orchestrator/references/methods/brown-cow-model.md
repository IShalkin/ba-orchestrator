---
id: brown-cow-model
name: "Brown Cow Model"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.1"
subtask_name: "Business Processes and User Work"
source_count: 1
---

# Brown Cow Model

`T4 Modelling and Analysis › 4.1 Business Processes and User Work`

**Also described as:** The Brown Cow Model

## Problem Solved

Eliminates confusion during requirements discovery between current physical implementations and future essential requirements.

## BA Lifecycle Phase

Analysis

## Input Artifacts

Existing documentation, user interviews, process observations, target goals.

## Output Artifacts

How-Now Model (Current Physical), What-Now Model (Current Essential), Future-What Model (Future Essential), Future-How Model (Future Physical).

## Participants & Roles

Business Analyst, Business Owner, SME, Architect, UX Designer.

## Prerequisites

Understanding of the business scope and objectives.

## Step-by-Step Procedure

Model the current physical implementation ("How-Now") if needed to baseline.
2. Abstract away current technology, people, and organizational structures to uncover the current essential business policy ("What-Now").
3. Add new business goals, innovations, and policy changes to define the desired future essential state ("Future-What").
4. Apply modern technology, human roles, and ready-made components to design the future physical solution ("Future-How").

## Analyst Questions & Prompts

"How do you do this job today?" (How-Now), "Why do you do this activity? What is the underlying business policy?" (What-Now), "What should the business policy be in the future, independent of technology?" (Future-What), "What technology/people will implement this future policy?" (Future-How)

## Minimal Realistic Example

Analyzing a luggage check-in process: moving from paper boarding passes and counter staff (How-Now) to verifying reservation and passenger identity (What-Now), adding self-service identity matching (Future-What), and implementing facial recognition kiosks (Future-How).

## Quality Criteria & Verification

Clear separation between 'above-the-line' (essential) and 'below-the-line' (physical) models; elimination of technological fossils from the future essential model.

## Errors & Anti-Patterns

Jumping directly from How-Now to Future-How (rushing from one technology implementation to another without finding the essential business policy); getting stuck indefinitely in How-Now modeling.

## When NOT to Use

Pure greenfield initiatives with zero existing legacy processes or completely novel product domains where no current baseline exists.

## Alternatives & Complementary Methods

Essential Systems Analysis, As-Is / To-Be Process Mapping, Value Stream Mapping.

## Supported Decisions

Business process re-engineering, technology selection, legacy system replacement strategy, core business rule definition.

## AI & Agentic Adaptation

AI agents can analyze legacy code or process logs to extract essential business rules ("What-Now") automatically, freeing human analysts to focus on innovative "Future-What" design.
