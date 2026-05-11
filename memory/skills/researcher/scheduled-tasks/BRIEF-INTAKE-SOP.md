# BRIEF INTAKE SOP — RESEARCHER OVERNIGHT

**Status:** Live | **Created:** 28-Apr-26 | **Owner:** RESEARCHER role
**Role this file plays:** When Richard briefs Watson during the day for overnight RESEARCHER execution, this SOP is the wrapper that turns conversation into a verified scheduled task. **The session cannot end until the commit ritual completes.**

---

## WHEN TO INVOKE

Trigger on any of these patterns from Richard:
- "Run [tickers] tonight / overnight"
- "Do [stages] on [tickers] for the morning"
- "Set up [research] to run while I sleep"
- A future-time start ("at 04:15", "from 23:00")
- Approval of a `researcher-proposal-{date}.md` file

If unsure whether the brief is for tonight or just for discussion, **ASK Richard explicitly**: *"Confirm: do you want this scheduled for overnight execution, or are we discussing for a future session?"*

---

## THE COMMIT RITUAL — FIVE STEPS, INVIOLATE

The session cannot close until all five complete. If any fails, surface to Richard in the same session.

### Step 1 — Parse brief into structured fields

Extract from Richard's natural language:
- **TICKERS** — list of stock codes (validate format e.g. `MTRS-SE`, `KNIN-CH`)
- **STAGES_PER_TICKER** — IG, Triaging, ESA, DD per ticker
- **SOURCES** — `dual` (default if AS browser available), `c-only`, `as-only`
- **SPECIAL ANGLES** — any KQs, focus areas, or angles Richard flagged

Where ambiguous, ask **before** writing the brief-card. Do not guess.

### Step 2 — Write the brief-card (v2.0, 30-Apr-26)

Save to `memory/staging/researcher-brief-{NIGHT-OF-EXECUTION-YYYY-MM-DD}.md`. Schema below. The brief-card is the **authoritative artefact** — it is what Task A and Task B read at fire time. The chat conversation is NOT the source of truth; the brief-card is.

**CRITICAL DATING CONVENTION (locked 28-Apr-26):** The brief-card is dated by the **night the research executes**, NOT the day it was written. If Richard briefs in at 17:00 on 28-Apr for tasks that fire after midnight (so on 29-Apr), the brief-card is `researcher-brief-2026-04-29.md`. Why: the watchdogs at 03:38 / 06:36 BST run on the date of execution and read the brief-card matching *today's* date. If the brief-card is dated by authoring day, the watchdog will not find it and will incorrectly write `status="no-overnight-research"`. Origin: 28-Apr-26 VOD test caught this; corrected before tasks fired.

#### Mandatory append protocol (revised v2.0, 30-Apr-26)

If a brief-card already exists for the night-of-execution, **read-modify-write append**, never `Write` with new content as the only payload. The session of 28/29-Apr-26 lost Block 1 content (BGN) when Block 3 (ESA) was written over the top — that failure mode is structurally prevented here.

**Sequence (apply every time):**

```
2a. CHECK existence:
    - Use Read tool on `memory/staging/researcher-brief-{NIGHT-OF-EXECUTION}.md`
    - If file exists → capture full content
    - If file does not exist → proceed to 2c (new file path)

2b. APPEND (existing file):
    - Read the manifest header at top
    - Append new ticker block(s) to existing body
    - Update manifest header: increment blocks_count, append to blocks array, update last_appended timestamp, update total_expected_pages
    - Write back the FULL content (manifest + all prior blocks + new blocks)
    - NEVER call Write with only the new content as payload

2c. CREATE (new file):
    - Compose manifest header (blocks=[NEW_BLOCK], blocks_count=1, last_appended=NOW, total_expected_pages=N)
    - Compose body with single ticker block
    - Write the file

2d. VERIFY (after every write, append OR create):
    - Re-read the file
    - Check (i) all prior ticker blocks present (block titles + counts match manifest), (ii) new ticker blocks added, (iii) no duplicate sections (count `## BRIEF BLOCK` headers; must match manifest blocks_count)
    - If verification fails → restore from backup (memory/backups/) and retry append
    - If verification still fails after one retry → escalate to Richard before session close
```

#### Banned: suffixed brief-card variants

Do NOT create files like `researcher-brief-esa-{date}.md`, `researcher-brief-bgn-{date}.md`. **One brief-card per night-of-execution, period.** Suffixed siblings fragment the watchdog's single-source-of-truth assumption and break completion checking. The 29-Apr `researcher-brief-esa-2026-04-29.md` was a workaround that became a failure mode — do not repeat.

If a brief-card is corrupted and cannot be recovered by append:
1. Restore from `memory/backups/{date}-pre-write/` (pre-write snapshot, see SA pre-write-backup-SOP)
2. Re-apply append per 2a-2d
3. Do NOT create a sibling file as a "safer" option — that breaks the watchdog

#### Manifest header schema (mandatory at top of every brief-card, v2.0)

```yaml
---
brief_card_version: 2.0
night_of_execution: 2026-04-30
manifest:
  blocks: [BGN, VOD-GB, ESA-EKTA-HTRO-HTWS]
  blocks_count: 3
  last_appended: 2026-04-29T21:31:00+01:00
  last_appended_by: RESEARCHER session (live, Richard at desk)
  total_expected_pages: 22
  total_expected_as_threads: 18
sign_off: Richard confirmed in chat 2026-04-29
---
```

The watchdog reads the manifest first to validate consistency before processing.

### Step 3 — Fill the canonical template

Read `memory/skills/researcher/scheduled-tasks/CANONICAL-PROMPT.md`. Substitute every `{{variable}}` from the brief-card. Produce two prompt strings (Task A + Task B), or one prompt string for the single-task variant.

**Do not hand-roll**. If the template doesn't fit the brief, the brief-card is wrong — go back to Step 1 and clarify with Richard.

### Step 4 — Create the scheduled task(s) and verify

For each task, before calling `mcp__scheduled-tasks__create_scheduled_task`:

- **Verify `fireAt` is in the future** by running `TZ='Europe/London' date` in bash. The target time must be at least **5 minutes** ahead of `now`. (This absorbs former SKILL-V2 Rule #29 into a code check.)
- **Verify the prompt** is non-empty, contains the right brief-card path, and references `CANONICAL-PROMPT.md` semantics.
- **Verify the trigger time spacing** for two-task split: Task B's `fireAt` must be ≥75 min after Task A's `fireAt`.

Then create the task(s). Capture the returned task ID(s).

### Step 5 — Read back to Richard, get confirmation

Last line of the session must be the read-back. Format:

```
SCHEDULED-TASK COMMIT — TONIGHT'S RESEARCHER BRIEF

Brief-card: memory/staging/researcher-brief-{NIGHT-OF-EXECUTION-YYYY-MM-DD}.md
Tickers: <list>
Stages: <summary>

Task A (research + submit): id=<task-a-id>, fireAt=<TZ-confirmed timestamp>
Task B (extract + post):    id=<task-b-id>, fireAt=<TZ-confirmed timestamp>

Watchdog 03:30 retry + 06:30 final-check are standing scheduled tasks; they will check expected outputs against Notion page IDs and retry/flag automatically.

Confirm to commit, or correct.
```

If Richard does not respond before he closes the session, **the tasks are still committed** (he asked for autonomous execution). The read-back is for his benefit, not a permission gate.

If Richard corrects ("actually drop KNIN") — update the brief-card and the scheduled-task prompt(s), then re-read-back.

---

## BRIEF-CARD SCHEMA

```markdown
# RESEARCHER BRIEF-CARD — {YYYY-MM-DD}
**Created:** {YYYY-MM-DD HH:MM TZ}
**Sourced from:** {chat conversation | researcher-proposal-{date}.md | session handoff}
**Sign-off:** {Richard confirmed at HH:MM | implicit (autonomous run)}

## SCHEDULED TASKS
- Task A id: {task-a-id} | fireAt: {ISO timestamp UK}
- Task B id: {task-b-id} | fireAt: {ISO timestamp UK}
- Watchdog: standing tasks 03:30 + 06:30 (see WATCHDOG-SOP.md)

## TICKERS

### {TICKER-1} ({Company name})
- Stages: {IG | Triaging | ESA | DD}
- Sources: {dual | c-only | as-only}
- **Per-query plan** (explicit, derived from SKILL-V2 23-Query Master Table):
  ```
  {QUERY-NUM}: {QUERY-NAME} — source={C|AS|AS+C} — as_required={true|false} — expected_notion_pages={1|2}
  e.g.
  Q1: Business Description — source=AS — as_required=true — expected_notion_pages=1
  Q2: Change Forces — source=AS+C — as_required=true — expected_notion_pages=1 (merged)
  Q3: Technical Momentum — source=C — as_required=false — expected_notion_pages=1
  ```
  Read the Master Table; do not invent sources. The `as_required` flag is what Task B's AS-FIRST GATE reads.
- Special angles: {free text — KQs, focus areas, what to weight}
- Expected Notion pages on completion: {integer — sum of expected_notion_pages above}
- Notes: {free text — any context Richard flagged}

### {TICKER-2} (...)
...

## EXPECTED OUTPUTS — TOTAL
- Notion pages: {sum}
- Files folder: COWORK/Files/{TICKER}/{STAGE}/...
- Completion flag: memory/staging/overnight-status-{YYYY-MM-DD}.json

## DEPENDENCIES / KNOWN GAPS
- {e.g. "KNIN AS browser not pre-warmed — Task B may find threads STILL-RUNNING"}
- {e.g. "MTRS — no prior Notion pages; clean start"}
```

---

## WORKED EXAMPLE — WHAT YESTERDAY *SHOULD* HAVE LOOKED LIKE

Richard typed (in chat, evening of 27-Apr): *"Run IG + Triaging on MTRS, IG only on KNIN, Triaging on COMET overnight."*

**Step 1 (parse).** TICKERS=`[MTRS-SE, KNIN-CH, COTN-CH]`. STAGES=`{MTRS-SE: [IG, Triaging], KNIN-CH: [IG], COTN-CH: [Triaging]}`. SOURCES=`dual` for all. No special angles flagged.

**Step 2 (brief-card).** Watson writes `memory/staging/researcher-brief-2026-04-28.md` with the three ticker blocks above plus expected page counts (MTRS: 7, KNIN: 3, COTN: 4 → 14 total). *(Note: brief-card is named by night-of-execution. In this example Richard briefed evening of 27-Apr for tasks firing post-midnight on 28-Apr → file is `2026-04-28`. See "Critical Dating Convention" in Step 2 above.)*

**Step 3 (template fill).** Two prompts produced — Task A and Task B — each parameterised with the brief-card path.

**Step 4 (create + verify).** `TZ='Europe/London' date` returns `Mon Apr 27 21:30:00 BST 2026`. Task A `fireAt` = `2026-04-28T01:00:00+01:00` (3.5 h ahead — pass). Task B `fireAt` = `2026-04-28T02:30:00+01:00` (90 min after Task A — pass). Both created. IDs captured.

**Step 5 (read-back).** Watson posts the read-back block. Richard sees task IDs and times. Closes laptop.

**At 01:00.** Task A fires. Reads brief-card. Runs the [C] research, submits AS, saves files, writes flag. Exits.

**At 02:30.** Task B fires. Reads brief-card + completion flag. Extracts AS, merges, highlights, posts 14 Notion pages, records page IDs in metadata.json, writes flag.

**At 03:30.** Watchdog runs. Reads brief-card + flag. Expected 14 pages, found 14 page IDs in metadata.json. Status complete. Logs "all green" to morning-briefing-flag.md.

**At 06:30.** Watchdog re-checks. Still complete. Morning routine reads `morning-briefing-flag.md`, sees overnight-status=complete, mentions it in Richard's morning brief.

That is the "fully fully completed by morning" outcome.

---

## FAILURE MODES THIS SOP PREVENTS

| Yesterday's failure | What this SOP would have done |
|---|---|
| MTRS — verbal agreement, no scheduled task | Step 4 forces task creation; Step 5 forces read-back; cannot end session without a task ID |
| gym-trio — `request_cowork_directory` in prompt | Step 3 fills `CANONICAL-PROMPT.md` which contains no such call (and forbids it) |
| COMET — scheduling collision absorbed by morning routine | Step 4 enforces ≥75 min Task A → Task B spacing; watchdog at 03:30 catches collision and retries |
| Approval-tonight file empty, nothing ran | This SOP retires that pattern — brief-card *is* the approval, scheduled task *is* the commitment |

---

## INPUT VARIANTS WATSON ACCEPTS

**Form 1 — natural language (preferred).**
*"Run IG on KNIN, full IG + Triaging on MTRS, Triaging only on COMET. Dual-source where possible."*
→ Watson parses, asks any clarifying Q (max 2), proceeds.

**Form 2 — structured one-liner per ticker.**
```
- MTRS-SE: IG + Triaging, dual
- KNIN-CH: IG, dual
- COTN-CH: Triaging, dual
```
→ Watson parses directly, no clarifying Q needed.

**Form 3 — sign-off on a researcher-proposal-{date}.md.**
*"Approve items 2, 3 and 6 from tonight's proposal."*
→ Watson reads the proposal file, picks the items, parses, proceeds.

---

## COUPLING TO OTHER FILES

- `CANONICAL-PROMPT.md` — the prompt template Step 3 fills.
- `WATCHDOG-SOP.md` — the standing 03:30 + 06:30 retry/check tasks.
- `memory/skills/researcher/SKILL-V2.md` — read by the scheduled task at fire time (loaded by `scheduled-task-preamble.md` chain).
- `memory/skills/scheduled-task-preamble.md` — universal unattended-mode disciplines.
- `memory/staging/researcher-brief-{NIGHT-OF-EXECUTION-YYYY-MM-DD}.md` — the brief-card produced by this SOP.
- `memory/staging/overnight-status-{YYYY-MM-DD}.json` — the completion flag the watchdog reads.

---

## CHANGELOG

- **28-Apr-26** v1.0 — Created. Replaces the old `researcher-proposal → researcher-approved-tonight → ad-hoc scheduled task` chain. Brief-card *is* the approval; scheduled task *is* the commitment; read-back is the close-the-loop.
