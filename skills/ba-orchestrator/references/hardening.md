# Hardening (install-time controls on the target machine)

The prompts tell agents to stay read-only and write only their own paths. These controls make that hold **outside the model**. Apply them where the project sources are connected. Prompt rules alone failed once during development: confused agents spawned duplicates and overwrote each other's files.

## 1. Read-only access to sources (primary control)

Give the MCP servers **read-only credentials**. A token that cannot write is the only control that holds even if every other layer fails.

| Source | Read-only setup |
|---|---|
| Confluence / Jira (Atlassian) | API token of a user or service account with *browse/view* permission only on the needed spaces and projects; no create, edit or transition permission |
| SharePoint / OneDrive (Microsoft Graph) | App registration with `Sites.Read.All` / `Files.Read.All` (or `Sites.Selected` with read), never `*.ReadWrite.*` |
| GitHub | Fine-grained PAT with **Contents: Read** and **Issues/Pull requests: Read**, limited to the needed repos |
| Mural / Miro | Scopes `*:read` only |
| Meeting transcripts | Export them to a read-only folder, or use a read scope on the meeting tool's API |
| Local files | Run the session where the sources folder is read-only for the OS user, or point the agents at a copy |

## 2. Deny write tools in Claude Code (second layer)

After connecting the MCP servers, list their tools (`/mcp`, or ask Claude to list `mcp__*` tools). Add every tool that creates, updates, deletes, comments, transitions or uploads to the `deny` list in the project `.claude/settings.json`:

```json
{
  "permissions": {
    "deny": [
      "mcp__<atlassian-server>__<create_page>",
      "mcp__<atlassian-server>__<update_page>",
      "mcp__<atlassian-server>__<transition_issue>",
      "mcp__<atlassian-server>__<add_comment>",
      "mcp__<github-server>__<create_or_update_file>",
      "mcp__<github-server>__<create_issue>"
    ]
  }
}
```

Replace the placeholders with the **exact tool names** your servers expose. Whether wildcard patterns (for example `mcp__server__create*`) work in `deny` rules is unverified: check the current Claude Code permissions documentation before relying on one, and prefer explicit names.

Optionally, add the same names to `disallowedTools` in `.claude/agents/ba-researcher.md` and `ba-critic.md`, the two agents that inherit MCP tools.

## 3. What is already enforced by the skill

| Control | Where | Enforced by |
|---|---|---|
| No nested agent spawning | `disallowedTools: Agent` / tool allowlists in all four agents | Claude Code (outside the model) |
| No shell for the agents that touch sources | `disallowedTools: …, Bash` on researcher and critic | Claude Code |
| Turn budget per agent | `maxTurns` in each agent | Claude Code |
| Launch, wave, revision and attempt budgets; duplicate assignments; legal transitions | `scripts/run_state.py` | Deterministic script (the orchestrator must call it; see the residual risks) |
| Writes outside an agent's output, and any change to the skill directory | `run_state.py snapshot` / `verify-writes` (violations logged in `status.json`) | Deterministic detection after each wave |
| A dependent launched before its upstream is done; a dependent built on an old upstream | `run_state.py set … running` / `stale` / `terminal` | Deterministic script |
| Artifact format, evidence-id existence, companion links, Summary budget | `scripts/check_artifact.py` | Deterministic script |

## 4. Residual risks (not guaranteed)

- **Detection, not prevention, for file writes.** Executors and the synthesizer can technically write anywhere. `verify-writes` detects changes inside `RUN_DIR` and `SKILL_DIR` only, after the fact. Writes elsewhere on disk are not detected. Mitigation: run in a project directory under version control and review `git status` after a run.
- **The orchestrator itself is a model.** It could skip calling `run_state.py` or `check_artifact.py`. The scripts make violations visible when they are called; they do not force the calls. Mitigation: the final README must include `run_state.py show` output, and a missing `status.json` means the run is untrustworthy.
- **A budget raise is recorded, not authorised.** `run_state.py budget` stores whatever `--approved-by` says; it cannot tell the user from the orchestrator. Mitigation: `run_state.py show` prints every raise with its approver and reason, and the final README lists them.
- **`verify-writes` trusts its own files.** It skips exactly `status.json`, `status.json.tmp`, `.snapshots/` and anything inside a `__pycache__` directory (`RUN_SKIP` and `skipped()` in `run_state.py`). It loads only the snapshot logged in `status.json` and checks its hash, so a dropped or rewritten snapshot file is caught, but an agent that edits `status.json` itself can still hide its other writes. Mitigation: review `git status` after a run.
- **A baseline is checked only when registered.** A refresh run (WF-R1) records the baseline's tree hash with `init --baseline`; `reconcile` reports a change and `completed` is refused. `verify-writes` also checks SKILL_DIR; any other directory outside RUN_DIR is unchecked.
- **Orchestrator paths are reported, not blocked.** Changes under `00-intake/`, `01-plan/` and `06-final/` print as `ORCHESTRATOR WRITE` lines rather than violations, because the orchestrator writes there between waves. A subagent that writes there is therefore only reported. Mitigation: the orchestrator confirms every such line and treats an unexplained one as a violation.
- **Relaunched agents widen the allowed set.** An earlier agent set `running` after the snapshot may write its own output during the wave. Its output is allowed; nothing else of it is.
- **Evidence existence is not evidence truth.** `check_artifact.py` proves an `[E:id]` exists in a log, not that the quote supports the claim. The critic's re-check at source covers a sample, not every claim.
- **Correlated reviewers.** The critic shares the executor's model family (see run-protocol §7).
- **Prompt injection through sources** is mitigated by instructions and read-only credentials, not eliminated. A poisoned document can still bias an artifact. Mitigation: evidence quotes are visible for human review.
