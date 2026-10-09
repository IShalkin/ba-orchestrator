---
id: class-modelling
name: "Class Modelling"
task: T4
task_name: "Modelling and Analysis"
subtask: "4.2"
subtask_name: "Data and Concepts"
source_count: 2
---

# Class Modelling

`T4 Modelling and Analysis › 4.2 Data and Concepts`

**Also described as:** Class Diagrams (UML Static Structure); Class modelling

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Models object-oriented data structures, attributes, associations, multiplicities, and operations, providing an enriched data specification for modern software architectures.

**[Variant B]**

Models internal software object structures by encapsulating data attributes and operational methods into object classes.

## BA Lifecycle Phase

**[Variant A]**

Define Requirements / Requirements Modelling / Specification

**[Variant B]**

design

## Input Artifacts

**[Variant A]**

Entity Relationship Models, Document Analysis, Use Cases, domain rules.

**[Variant B]**

Data model, process descriptions, system architecture notes.

## Output Artifacts

**[Variant A]**

Class Diagram (Classes with Name, Attribute, and Operation compartments, Multiplicities, Association Classes, Reflexive Associations, Generalizations).

**[Variant B]**

UML Class Diagram (Class boxes with attributes and operations, Association lines with numeric cardinalities).

## Participants & Roles

**[Variant A]**

BA, System Architect, Software Developer, Data Architect.

**[Variant B]**

System architect, developer, BA.

## Prerequisites

**[Variant A]**

Identification of domain objects, attributes, and system functionality.

**[Variant B]**

Detailed understanding of object-oriented software design.

## Step-by-Step Procedure

**[Variant A]**

Identify Classes (3-compartment box: Name, Attributes, Operations).
2. Draw Association lines between classes.
3. Specify Multiplicity (e.g. 0..*, 1..1, 0..4).
4. Create Association Classes for many-to-many relationships holding attributes.
5. Model Generalizations (inheritance super-classes) and Reflexive associations.

**[Variant B]**

Identify object classes based on system domain or software artifacts.
2. List class attributes and data types in the middle compartment.
3. List operations/methods and parameters in the bottom compartment.
4. Connect classes with association lines annotated with explicit numeric cardinalities (e.g., 1..*).
5. (For business applications) Separate data objects from complex service/observer objects.

## Analyst Questions & Prompts

**[Variant A]**

What are the object classes? What attributes describe them? What are the minimum and maximum association numbers (Multiplicity)? What general super-class unites these sub-classes?

**[Variant B]**

What methods operate on this data? Which class is responsible for executing this calculation?

## Minimal Realistic Example

**[Variant A]**

Class diagram showing Car class linked 0..* to Service class via Association Class CarService (holding dateOfService, recordedMileage), connected 0..4 to Technician class.

**[Variant B]**

Class 'Stay' with attributes (stay#, paymethod) and operations (checkout, recordService) connected 1..* to Class 'RoomState'.

## Quality Criteria & Verification

**[Variant A]**

Correct UML lower/upperCamelCase naming syntax; accurate multiplicity numbers; clear generalisation hierarchies.

**[Variant B]**

Object design review, automated unit test coverage.

## Errors & Anti-Patterns

**[Variant A]**

Over-populating operations prematurely before software design; confusing UML class multiplicity notation with SSADM entity relationship crow's foot notation.

**[Variant B]**

Mixing human domain tasks into object methods; attempting to encapsulate complex business logic directly inside database data objects.

## When NOT to Use

**[Variant A]**

When working in non-object-oriented legacy relational database environments where traditional ERD notation is preferred.

**[Variant B]**

Domain-level requirements specifications for business application procurement.

## Alternatives & Complementary Methods

**[Variant A]**

Entity Relationship Modelling, Data Dictionary, CRUD Matrix.

**[Variant B]**

Data Model (E/R), Collaboration Diagrams, Sequence Diagrams.

## Supported Decisions

**[Variant A]**

Object-oriented software design, database schema design, application architecture.

**[Variant B]**

Object-oriented software architecture, database persistence framework design.

## AI & Agentic Adaptation

**[Variant A]**

UML AI assistants parse user story descriptions to auto-generate class diagrams with candidate attributes and multiplicity associations.

**[Variant B]**

Auto-generate class diagrams and Java/C++ class boilerplates from pseudo-code specs using coding AI agents.
