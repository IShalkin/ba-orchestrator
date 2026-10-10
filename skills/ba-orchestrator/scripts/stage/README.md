# Staging and counting helpers

Run by the orchestrator, never by a subagent, between waves (`source-access.md` §4, run-protocol §8). Each script takes its output directory as an argument, prints a manifest of the files it wrote with their sizes, and exits non-zero on any failure. The deck, sheet and whiteboard scripts write into `OUT/<input stem>/`; that folder, and the tracker's `OUT`, must be absent or empty, so a re-staged source never mixes with an older version. Python stdlib only; `--help` prints the full usage. Stage into a directory outside every registered output, for example `ba-runs/<run>-staging/`, and list the staged files in the researcher and critic briefs.

| Script | Input | Writes |
|---|---|---|
| `stage_deck.py DECK.pptx OUT` | slide deck | in `OUT/<stem>/`: per slide `slide-NNN.md` (hidden flag, slide-shape text, speaker notes), `deck.pdf` and `slide-NNN.png`, hidden slides included |
| `stage_whiteboard.py WIDGETS.json OUT [--name N]` | whiteboard widget export | in `OUT/<stem or N>/`: `widgets.md` (absolute coordinates, authors, dates, text, connections), `board.html` |
| `stage_tracker.py OUT --base-url URL --jql JQL --token-env VAR --ac-field F` | Jira-compatible REST API v2 | `issues.json`, `index.md`, `bodies-NNN.md` (parts of about 400 KB; one issue larger than that stays whole) |
| `stage_sheet.py BOOK.xlsx OUT` | workbook | in `OUT/<stem>/`: `NN-<sheet>.md` per sheet, with its visible or hidden state |
| `merge_trace.py OUT --trace A.csv B.csv [--catalogue C.csv] [--issues issues.json] [--baseline OLD.json]` | split executors' `trace.csv` | `trace-merged.csv`, `coverage-summary.json` (pass as `MEASURED COUNTS`; with `--baseline` it adds the drift against an earlier summary) |

Notes that cost a wrong conclusion when missed:

- **Decks.** Rendering uses an external tool found at runtime: LibreOffice (`soffice`), or on macOS Microsoft PowerPoint through `osascript` (it must come to the foreground; the script unhides every slide on a temporary copy and closes it unsaved). PNGs need `pdftoppm` or the `pypdfium2` and Pillow packages; without one the PDF is written and the script says so. With no renderer, pass `--pdf` with an export that includes hidden slides, or `--render none` for the text layer only. The slide count is always compared with the page count, and a mismatch fails: an export can drop hidden slides silently.
- **Decks.** The text layer holds the slide's own shapes only; SmartArt, chart and embedded-object text is only in the render.
- **Sheets.** Cached formula values are used; a formula with no cached value is written as `=<formula>`.
- **Whiteboards.** A child's x/y are relative to its parent; the listing adds the offsets. An item with no id under the paths tried, or nested in a `children` list, is counted and fails the run, so an empty listing never reads as a staged board. `FIELDS` at the top of the script maps each field to the paths tried in order (flat and nested export shapes); add a path with `--map FIELD=PATH`. A connection is written `CONNECTS a <-> b`: it records a link, not a direction.
- **Trackers.** The token comes from the environment variable named by `--token-env`, never the command line. Name the acceptance-criteria field (`--ac-field customfield_NNNNN`, or `none`): on some servers `*all` does not return every custom field, and the script warns when no issue carries the named field. HTTPS is verified; `SSL_CERT_FILE` or `REQUESTS_CA_BUNDLE` adds a CA bundle to the default trust store. An `http://` base URL needs `--allow-http`, and a redirect to another scheme, host or port is refused, because the token would travel with it.
- **Traces.** Key ranges (`ABC-10..ABC-20`, `ABC-10..20`, en dash, `to`) are expanded up to a span of 200; between keys only a list separator is accepted, and anything else (`...`, a dash, `through`, `ABC-10-12`) is listed under `range_errors`, not guessed. `coverage` must be `full`, `partial` or `none` (any case), else the merge fails. Counts are over distinct `req_id`s; a duplicated id counts once with its lowest coverage, whatever the input order, and every duplicate is listed with each occurrence.

Tests: `python3 -I build/test_stage.py`.
