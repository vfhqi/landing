# WATSON KAIZEN LESSONS — Project MANIFEST

**Status:** Active.
**Created:** 4-May-26 by Watson at Richard's instruction.
**Purpose:** A persistent, append-only record of Watson's quality / process / behavioural failures, root-cause analyses, and corrective measures. Per the kaizen principle: continuous improvement through honest examination of what went wrong and why.

This is the lily-pad project for "things Watson should learn from but that don't fit cleanly into a single feedback memory or single project's decisions log." When something goes wrong in a session that has cross-cutting implications for how Watson operates — process, role discipline, quality gates, behavioural priors, instruction-following — it gets captured here.

## Folder structure

- `MANIFEST.md` — this file.
- `state.md` — current open lessons + their corrective-action status.
- `lessons/` — one markdown file per lesson, dated. Long-form root-cause analyses with five-whys / three-gaps / corrective procedures. Index file at `lessons/INDEX.md`.
- `transcripts/` — verbatim conversation excerpts that triggered or shaped each lesson. So future-Watson can read what was actually said, not just the distillation.

## How to use

**When something goes wrong in a session that has cross-cutting behavioural implications:**
1. Write a new file in `lessons/<YYYY-MM-DD>-<short-slug>.md` using the template structure (problems list → three gaps → five whys → root cause → corrective procedures).
2. Save the relevant transcript excerpt verbatim in `transcripts/<YYYY-MM-DD>-<same-slug>.md`.
3. Add a one-line index entry in `lessons/INDEX.md`.
4. Cross-reference: file a one-liner pointer in `memory/MEMORY.md` so the lesson is in auto-memory and surfaces in future sessions.
5. Update `state.md` if the lesson generates open corrective actions.

**When starting a new session:**
- Skim `lessons/INDEX.md` for active patterns.
- Treat any lesson tagged `MISSION CRITICAL` as a behavioural constraint to verify against at every decision point this session.

## Cross-references

- `memory/corrections.md` — append-only log of corrections; each kaizen lesson should produce a one-line entry there too.
- `memory/MEMORY.md` — auto-memory index; mission-critical kaizen lessons should be pinned at the top.
- Wisdom Library — if a lesson generalises into a mental model, it can be promoted to `wisdom-library/`.
