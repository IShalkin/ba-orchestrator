# Method Card Template

Every card in `methods/` uses the same fields. They come from the "Business Analysis Techniques Analysis Guide" structure. A card merges every description of one method that was collected. When there is more than one, each field lists one variant per description, labelled `[Variant A]`, `[Variant B]`, … The labels are consistent within a card: Variant B is the same description in every field.

| Field | Question it answers | How agents use it |
|---|---|---|
| Problem Solved | What problem does the method solve, and what uncertainty, error or conflict does it reduce? | **Selection.** Match it against the problem in the brief. |
| Uncertainty Reduced | What type of uncertainty does it remove? (mind map 8 only) | **Selection.** Refines the match. |
| BA Lifecycle Phase | Where in the lifecycle is it applied: discovery, elicitation, analysis, specification, prioritisation, validation or change management? | **Planning.** Places the method in a workflow stage. |
| Input Artifacts | What must exist before the method starts? | **Research.** Tells the researcher what to look for in project sources. |
| Output Artifacts | What does the method produce? | **Execution.** Defines the deliverable the executor must produce. |
| Participants & Roles | Who takes part? | **Execution.** Who to name in the artifact. An agent never invents real people; it names roles. |
| Prerequisites | What must be known, agreed or prepared first? | **Gate.** If a prerequisite is unmet, record a gap or reorder the plan. |
| Step-by-Step Procedure | What is the ordered algorithm (3–10 steps)? | **Execution.** The executor follows it step by step and records each step's result. |
| Analyst Questions & Prompts | What do the interview guides, workshop prompts and diagnostic questions contain? | **Execution and research.** Basis for question lists; the researcher uses them as search prompts. |
| Minimal Realistic Example | What does a short applied example look like? | **Execution.** Calibrates the shape and level of detail of the output. |
| Quality Criteria & Verification | What criteria, checklists or reviews show the output is good? | **Review.** The critic checks against every criterion. |
| Errors & Anti-Patterns | What are the typical failure modes? | **Review.** The critic looks for each one. The executor self-checks against them. |
| When NOT to Use | When should the method be skipped (low risk, known domain, no access, and so on)? | **Selection.** A hard filter during planning. |
| Alternatives & Complementary Methods | What to apply before, after or instead? | **Planning.** Fallbacks and sequencing. |
| Supported Decisions | Which decisions does it inform (scope, priority, architecture, release, acceptance, compliance)? | **Synthesis.** Links artifacts to the decisions in the brief. |
| AI & Agentic Adaptation | How can an agent help with this method (roles, inputs, risks, human-in-the-loop, guardrails)? | **Execution.** Use only the parts that an agent is actually allowed to do in this run. |

## Reading a multi-variant card

- Some variants say the opposite of each other on a field. When they disagree, follow the variant that best fits the brief's context and name the variant you followed in the artifact.
- If the variants complement each other (for example, two procedures with different steps), merge them into one procedure and record which steps came from which variant.
- `Not in source` means that description had nothing for that field. It does not mean the method has no such aspect.
