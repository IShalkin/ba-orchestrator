# Build and verify

| File | Purpose |
|---|---|
| `../data/taxonomy.py` | The tree: task → subtask → canonical method → source rows |
| `../data/framework-table1.repaired.json` | The method table: 434 rows × 17 fields. Column shifts from the original sheet export are repaired |
| `../data/mindmap-*.md` | Transcriptions of the three NotebookLM mind maps (6: template, 7: overview, 8: 13 methods, in Russian) |
| `mm8_en.py` | English translation of the 13 mind map 8 methods |
| `build_references.py` | Generates `references/methods/`, `references/tasks/`, `references/taxonomy.md` and `references/methods-index.json` |
| `verify_references.py` | Checks that every source field value (7,152) is present in its card, every link resolves, and the index matches the cards |
| `test_run_state.py` | Behaviour tests for `run_state.py`: budget raises and refusals, directory outputs, overlapping registrations, verify-writes, reconcile, the stale cascade, unfinished research logs |
| `test_check_artifact.py` | Behaviour tests for `check_artifact.py`: Summary band, form-only versus content errors, unanswered research markers |
| `test_stage.py` | Behaviour tests for `scripts/stage/`: decks, whiteboards, sheets, tracker export, trace merge |
| `verify_skill.py` | Checks method ids in the workflows, the paths in SKILL.md, subtask coverage, the agent frontmatter (Agent and Bash blocks, `maxTurns`, untrusted-content rule), that the scripts run, and that the Workflow templates parse and share an identical common block |

```bash
cd build
python -I build_references.py ../skills/ba-orchestrator
python -I verify_references.py ../skills/ba-orchestrator
python -I verify_skill.py ../skills/ba-orchestrator ../agents
python -I test_run_state.py
python -I test_check_artifact.py
python -I test_stage.py
```

`build_references.py` only overwrites the generated files. SKILL.md, the workflows, the protocols and the scripts are hand-written and left untouched. After renaming or removing a method in `taxonomy.py`, run `verify_skill.py`: it flags workflow references to ids that no longer exist.
