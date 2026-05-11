# Pre-Write Backup SOP — Systems Architect Role
<!-- Locked 21-Apr-26 21:00 UK by Richard. -->

## Doctrine

**Before any tool that mutates a non-trivial file, snapshot it first.** No exceptions.

This SOP exists because:
- Edit tool truncates files >~800KB silently (broke the dashboard 20-Apr-26).
- Idempotent patchers can still corrupt structure on the rare anchor-mismatch.
- A "small" patch of a 28KB Python script can introduce regressions that aren't caught until the next build.
- Lost work is the most expensive failure mode in this system.

The cost of a snapshot is ~50ms and a few KB. The cost of losing the file is the rest of the day.

## When to snapshot — MANDATORY

Snapshot any file BEFORE any of the following operations:

| Operation | Snapshot first? | Why |
|---|---|---|
| `Edit` on file >50KB | **Yes** | Edit tool truncation risk |
| `Write` overwriting an existing file | **Yes** | Total replacement; no rollback otherwise |
| `Write` to a NEW file path | No | No prior content to preserve |
| Bash heredoc / Python script that rewrites a file | **Yes** | Even idempotent scripts can fail mid-write |
| Marker-wrapped patcher run (e.g. `patch_X.py`) | **Yes** | Anchor-mismatch can corrupt JS/CSS/JSON structure |
| Append-only operations (e.g. tail-appending to a log) | No | Original content untouched |
| Rerunning a patcher on a file you patched 5min ago | **Yes — fresh snapshot every time** | Each run is a separate risk |

## Where to put snapshots

Two acceptable patterns — pick the one that matches the workflow:

### Pattern A — sidecar `.bak-pre-{operation}-{ts}` (preferred for individual files)

Same directory as the original. Name: `{originalname}.bak-pre-{operation}-{YYYYMMDD-HHMMSS}.{ext}`.

Examples:
- `databases/ic-ratings-dashboard-v2.html.bak-pre-section-a-v3-20260421-210045.html`
- `databases/memos/NVTK/Triaging.json.bak-pre-wirewc-20260421-200823.json`

Used by: every script in `databases/scripts/` that modifies a file. This is already the in-script convention.

### Pattern B — snapshot folder `snapshots/{date}-{HHMM}-{description}/` (preferred for multi-file batches)

For operations touching 2+ related files. Folder under `databases/snapshots/`. Copy each touched file in.

Examples:
- `databases/snapshots/2026-04-21-2029-cii4-momentum-table-live/` (dashboard + 3 NVTK JSONs + 5 scripts)
- `databases/snapshots/2026-04-21-2100-section-a-v3-pre/` (dashboard + scripts pre-#92)

## How to snapshot — the standard recipe

In Python scripts (the in-script idiom — already used everywhere):

```python
import shutil
from datetime import datetime
from pathlib import Path

ts = datetime.now().strftime('%Y%m%d-%H%M%S')
snap = TARGET.with_name(TARGET.stem + f'.{TARGET.suffix.lstrip(".")}.bak-pre-{OPERATION}-{ts}')
shutil.copy2(TARGET, snap)
```

In bash (when running an external patcher whose own backup behavior is unknown):

```bash
TS=$(date +%Y%m%d-%H%M%S)
cp -p "$TARGET" "${TARGET}.bak-pre-${OPERATION}-${TS}"
```

In Cowork tool calls (when applying an Edit/Write directly):

1. First call `Bash` to copy the file to a `.bak-pre-{operation}-{ts}` sidecar.
2. Then run the Edit/Write.
3. After confirming the edit succeeded and validates, the sidecar can be left in place (cheap insurance).

## Validation gate after any mutation

After any mutated write:
- For HTML: confirm `</html>` is the last meaningful content; no `var PB` corruption; scripts balanced.
- For JSON: re-parse with `json.loads` to confirm structurally valid.
- For Python script: `python -c "import ast; ast.parse(open('X').read())"` to confirm parses.
- For dashboard specifically: run `validate-dashboard.py` and confirm exit 0.

If validation fails: roll back from the sidecar/snapshot. Do not attempt repair-in-place — the next mutation compounds the damage.

## Pre-existing scripts that already comply

The convention is built into all in-script writers:
- `build-memos.py` snapshots dashboard before bake
- `wire_cii_word_counts.py` snapshots each NVTK JSON before wire
- `rightsize_cii_bluf_summary.py` ditto
- `patch_momentum_table_renderer.py` snapshots dashboard before patch
- `author_cii4_momentum.py` snapshots each NVTK JSON before replace
- `strip_dash_rating_placeholders.py` snapshots before strip
- `patch_memo_refinements_v1.py` ditto

External-tool calls (Edit, Write directly to a file) are where this SOP needs explicit enforcement.

## Cleanup policy

- Sidecar `.bak-pre-*` files: leave in place for 7 days, then prunable. Cheap.
- Snapshot folders under `databases/snapshots/`: keep all milestone snapshots indefinitely. They're checkpoints.
- Any backup that's part of a `memory/session-handoffs/transcripts/...-FULL-BACKUP/` folder: NEVER delete.

## Rule of thumb

> **If you're about to overwrite something you didn't write in this same session, snapshot first.**

If you wrote it 30 seconds ago and you're about to overwrite it again with the next edit, that's normal flow — no snapshot needed. But anything that pre-existed your current operation is a candidate for rollback, and rollback requires a snapshot.

## Cross-references

- Edit-tool truncation risk: `auto-memory/feedback_edit_tool_truncation_bug.md`
- Dashboard PB corruption pattern: `auto-memory/feedback_dashboard_corruption_pattern.md`
- Structural backup protocol (full-conversation level, complementary): `auto-memory/feedback_structural_backup_protocol.md`
- This SOP imprinted into: SA SKILL.md (next update), CLAUDE.md global preferences (next update).
