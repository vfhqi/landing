# Project Handoff — {PROJECT SLUG} — {YYYY-MM-DD}

## Optimal Restart Prompt — copy-paste into next session
```text
{Full self-contained restart prompt per memory/skills/session-handoff/restart-prompt-template.md.
Must include:
- Session role declaration (SA / APM / etc.)
- Project binding: "PROJECT: {slug}"
- WHERE WE LEFT OFF (3-5 sentences)
- ACTIVE OPEN QUESTIONS (3-5 with proposed defaults)
- TODAY'S WORK (≤4 lettered items)
- STANDING OPERATING RULES (load MANIFEST, read state.md, tilt comprehensive, inline Qs for SA/Opus)
- RECOVERY-MODE FALLBACK (if files unreachable: how to reconstruct)
- MISSION COMMAND axes for next session
Should be ~50-100 lines. NO placeholders in the final version.}
```

---

## Session Summary

{2-3 sentence overview of what happened this session.}

## Clarification Interrogation Record (Step 0 of HANDOFF SOP — MANDATORY)

**Universal principles candidates surfaced this session:**
- {Richard-quote or paraphrase} → codified where: {CLAUDE.md §X / auto-memory / project-scoped / rejected} — {1-line rationale}
- ...

**Cross-project leakage identified:**
- {doctrine that touched other projects} → propagation done to: {list of MANIFESTs edited} — {rationale}
- ...

**Mission Command / SOP evolution:**
- {any change to how the process itself runs based on today} → SSoT edit: {file + section}
- ...

**Preference drift / corrections integrated:**
- {correction} → codified at: {layer} — {1-line rationale}
- ...

**Parked ideas sweep:**
- {parked item} → promoted to {open-questions.md / decisions.md / archive / still parked with trigger: {trigger}}
- ...

**Empty-interrogation justification (only if all fields above empty):** {why}

## Live Tensions (unresolved, for next session)

- {"We were about to argue about X" / "I'm unsure whether Y is right" / "Richard pushed back on Z and I might re-suggest it"}
- ...

## Key Decisions (this session)

- {D-ID} — {short title} — {one-line description}

## Corrections Logged

{Count + brief description; linked to corrections.md if project-scoped, memory/corrections.md if global.}

## Memory Files Updated

- `state.md` — {what changed}
- `decisions.md` — {what appended}
- `open-questions.md` — {pruned N, added N; every entry has trigger}
- `log.md` — session entry appended
- `mission-command.md` — today + next session appended
- `transcript.md` — synchronous, complete
- `transcripts/{date}-structural-narrative.md` — summary generated
- `INDEX.md` / `INDEX.json` — last-touched updated
- MANIFEST audit: {Y/N — Tier 1 pointers resolve, doctrine-reconciled date updated}
- Sibling MANIFESTs edited (cross-project leakage): {list or "none"}

## Files Created / Edited (outside this project folder)

- {path} — {why}

## Snapshots

- Handoff snapshot: `snapshots/{YYYY-MM-DD-HHMM}/`
- Count this session: {N}

## Open Threads

- {thread 1 — what's dangling, state it left in}
- {thread 2 — ...}

## Meta-Role Observations

**Systems Architect:**
{Integration notes — what structural change was made, where it's been propagated, what still needs cross-file alignment.}

**High Performance Coach:**
{Behavioural observation — energy, pace, coherence of process, anything worth flagging for weekly review.}

## Quality Audit

- **What was delivered:** {list}
- **Governing SOP:** `memory/skills/project-management/SKILL.md` (+ project MANIFEST.md)
- **First-attempt pass rate:** {%}
- **Rework details:** {if any}
- **Correction logged?** {Y/N}

## Recovery recipe (if this handoff is all you have)

1. Mount COWORK silently.
2. Read this file's Optimal Restart Prompt (top of this document).
3. Read `PROJECTS/{slug}/MANIFEST.md` → load Tier 1.
4. Read `PROJECTS/{slug}/state.md`.
5. Ask Richard the Mission Command diagnostic.
6. Begin work.
