---
id: runtime-requirements-monitoring
name: "Runtime Requirements Monitoring"
task: T8
task_name: "Change Deployment and Solution Evaluation"
subtask: "8.3"
subtask_name: "Benefits and Outcome Evaluation"
source_count: 2
---

# Runtime Requirements Monitoring

`T8 Change Deployment and Solution Evaluation › 8.3 Benefits and Outcome Evaluation`

**Also described as:** Runtime Requirements Monitoring and Dynamic Adaptation

This card merges 2 descriptions of the method, labelled Variant A–B in every field.

## Problem Solved

**[Variant A]**

Reduces system failure when real-world environment assumptions are violated or change dynamically after system deployment.

**[Variant B]**

Reduces system failures caused by changing or unexpected environmental assumptions at system runtime through continuous self-monitoring and dynamic reconfiguration.

## BA Lifecycle Phase

**[Variant A]**

Change management / runtime evolution

**[Variant B]**

Evolution / runtime management

## Input Artifacts

**[Variant A]**

Mission-critical goals, volatile environment assumptions, formal temporal logic specifications, event logs.

**[Variant B]**

Formal temporal logic goal assertions, unstable environment assumptions, alternative design courses of action, reconfiguration rules.

## Output Artifacts

**[Variant A]**

Generated runtime assertion monitors, violation event logs, compensator reconfiguration rules, dynamic adaptation actions.

**[Variant B]**

Software monitors, violation logs, runtime compensator, reconfigured software state.

## Participants & Roles

**[Variant A]**

BA, System Architect, Software Engineer, Runtime Adaptation Engine.

**[Variant B]**

Requirements Engineer (specifier), Software Architect, Runtime System Monitor / Compensator Engine.

## Prerequisites

**[Variant A]**

Critical/volatile environment assumptions are formally specified in temporal logic; alternative courses of action are designed.

**[Variant B]**

Formalized critical requirements/assumptions; identified alternative operational courses of action.

## Step-by-Step Procedure

**[Variant A]**

Identify critical/volatile assumptions or requirements at RE time.
2. Formalize assertions in temporal logic.
3. Compile formal assertions into software monitors (as statecharts or event pattern checkers).
4. Design alternative recovery courses of action (compensators).
5. Deploy software with integrated monitors.
6. At runtime, monitor watches event streams; upon detecting assumption violation, it triggers compensator rules to dynamically reconfigure system behavior.

**[Variant B]**

At RE time, identify mission-critical requirements or volatile assumptions subject to runtime violation.
2. Formalize assertions (e.g., in LTL) and compile them into automated software monitors (state machines or pattern matchers).
3. Design alternative courses of action and dynamic reconfiguration rules (e.g., threshold-based rules).
4. Deploy software together with concurrent monitors and compensator engine.
5. At runtime, monitors track system events; upon detecting assertion violations, the compensator executes reconfiguration rules to shift to alternative courses of action on the fly.

## Analyst Questions & Prompts

**[Variant A]**

Which environment assumption is most likely to be violated at runtime? What alternative course of action should the software execute if assumption A fails?

**[Variant B]**

What assumption is volatile at runtime? What threshold of violation should trigger dynamic reconfiguration? What alternative workflow should execute if assumption A fails?

## Minimal Realistic Example

**[Variant A]**

Monitoring the assumption 'Participant returns constraints within 3 days'; if violated > 3 times, the compensator engine automatically switches to fetching constraints directly from the participant's e-agenda.

**[Variant B]**

Monitoring assumption 'Invited participant responds to email within 3 days'. If monitor detects 3 consecutive missed deadlines, compensator automatically switches workflow to query the participant's electronic agenda directly.

## Quality Criteria & Verification

**[Variant A]**

100% detection rate of specified assumption violations by monitors; correct rule-based execution of compensator reconfigurations; minimal runtime performance overhead.

**[Variant B]**

Real-time assertion detection correctness; mathematical proof that monitor compilation preserves original LTL property semantics.

## Errors & Anti-Patterns

**[Variant A]**

Monitoring non-critical stable assumptions (causing excessive runtime overhead); failing to design alternative recovery actions; un-bounded monitoring loops.

**[Variant B]**

Monitoring non-critical low-risk parameters causing high runtime CPU overhead; endless reconfiguration loops between unstable alternatives.

## When NOT to Use

**[Variant A]**

For simple static systems operating in fully controlled, unchanging environments where assumptions never fail.

**[Variant B]**

In static, fully predictable environments where operational assumptions never change, or in legacy systems without dynamic plug-in architectures.

## Alternatives & Complementary Methods

**[Variant A]**

Static risk analysis, manual software updates, fault-tolerant architecture design.

**[Variant B]**

Complementary: Goal Modeling, LTL Formal Specification, Exception Handling. Alternative: Static Off-line Change Control.

## Supported Decisions

**[Variant A]**

Dynamic software reconfiguration, automated exception recovery, adaptive service execution.

**[Variant B]**

Dynamic system reconfiguration, runtime fault tolerance, adaptive user customization.

## AI & Agentic Adaptation

**[Variant A]**

Runtime monitoring agents can continuously evaluate streaming telemetry against formal LTL goal assertions, using machine learning to dynamically adjust reconfiguration thresholds.

**[Variant B]**

Autonomous agentic architectures use ML monitors to detect assumption drifts in real time and dynamically synthesize new compensator workflows without human intervention.
