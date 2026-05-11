# Ratings Dashboard — Project Home
<!-- [W] Created 21-Apr-26. Owner: SYSTEMS ARCHITECT role. Active build. -->

## What this project is

The **Ratings Dashboard** is Richard's main investing dashboard — single HTML file with multiple tabs. The MEMO tab renders per-stock case-file memos (BLUF, prose, callouts, ratings tables) from JSON source files baked at build-time.

## Active workstream — Stage Toggle Build

Add a **Triaging / ESA / DD** stage toggle to the MEMO tab so each stock can render at the appropriate stage of disclosure. NVTK is the lead stock — getting all three stages populated (with Lorem-Ipsum where live content doesn't exist yet) so we can sign off on visual fidelity to the MEMOview spec.

## Current status (as of 21-Apr-26 morning)

See `state.md` for the live picture. **Always read `state.md` first.**

## Files in this folder

| File | Purpose |
|------|---------|
| `README.md` | This file — what the project is |
| `state.md` | **Live state — read first, update every step** |
| `decisions.md` | Locked decisions (do not re-ask Richard) |
| `spec.md` | MEMOview budgets, section architecture, conventions |
| `open-questions.md` | Genuinely unresolved questions |
| `sources.md` | Canonical paths to Excel, JSONs, build script, dashboard, mockup |
| `log.md` | Chronological activity log |
| `snapshots/` | Backups taken before each save |

## Operating rules for this project

1. **Read `state.md` before doing anything.** If a new session starts and you find this folder, your first read is `state.md`.
2. **Never ask Richard a question that's answered in `decisions.md` or `spec.md`.** If a decision exists, follow it. If you genuinely don't know, check `open-questions.md` first.
3. **Update `state.md` after every meaningful action** (file written, build run, decision taken). Treat it like a working journal, not a handoff doc.
4. **Snapshot before you touch the live dashboard.** Copy current `dashboard.html` and any touched JSONs into `snapshots/{YYYY-MM-DD-HHMM}/` before saving the new version.
5. **No GitHub push during this build.** Local only. Richard will push when ready.
6. **Visual fidelity > formal validation.** If validators fight you, prioritise the rendered length and look matching MEMOview spec.
