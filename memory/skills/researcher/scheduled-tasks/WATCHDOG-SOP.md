# OVERNIGHT COMPLETION WATCHDOG — SOP

**Status:** Live | **Created:** 28-Apr-26 | **Owner:** RESEARCHER role
**Role this file plays:** A standing pair of scheduled tasks (03:30 + 06:30 UK) that read the night's brief-card, check expected outputs vs Notion page IDs, **automatically retry on partial completion**, and surface unrecoverable failures into the morning routine. Richard's insurance against silent overnight failures.

---

## ARCHITECTURE

Two standing scheduled tasks. Both run every night regardless of whether a brief-card exists.

| Task | fireAt UK | Job |
|---|---|---|
| `watson-overnight-watchdog-0330` | 03:30 daily | Read brief-card → check outputs → retry on partial → log result |
| `watson-overnight-watchdog-0630` | 06:30 daily | Final check → if still incomplete, surface loud flag to morning routine |

Both watchdogs read the SAME brief-card (`memory/staging/researcher-brief-{YYYY-MM-DD}.md`) and the SAME completion flag (`memory/staging/overnight-status-{YYYY-MM-DD}.json`).

---

## 03:30 WATCHDOG — RETRY PASS

**Why 03:30:** Task A fires ~01:00, submits AS. Task B fires ~02:15, extracts and posts. By 03:30, both tasks have had time to complete. AS extractions that took longer than expected may still be running, but most should be done. If incomplete, there's still time before morning to retry.

### Prompt body

```text
WATSON — OVERNIGHT WATCHDOG (03:30 RETRY PASS)
Role: RESEARCHER. Mode: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT (do NOT call request_cowork_directory)
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/scheduled-tasks/CANONICAL-PROMPT.md (for Definition of Done)
  - Resolve TODAY = current YYYY-MM-DD in Europe/London
  - Brief-card path = memory/staging/researcher-brief-{TODAY}.md
  - Completion flag path = memory/staging/overnight-status-{TODAY}.json

STEP 1 — EARLY EXIT IF NO WORK
  - If brief-card does not exist → write morning-briefing-flag.md status="no-overnight-research" → exit.
  - If completion flag exists with status=complete AND notion_pages_posted >= expected_pages →
      write morning-briefing-flag.md status="overnight-complete" with page IDs → exit.

STEP 2 — DIAGNOSE WHAT'S MISSING
  Read brief-card. For each ticker × stage, derive expected outputs (Notion pages).
  Read COWORK/Files/{TICKER}/{STAGE}/*/metadata.json for actual page IDs.
  Build a missing-outputs list:
    - TASK_A_NOT_RUN: brief-card exists but no [C] raw files on disk
    - TASK_B_NOT_RUN: [C] files exist but no [AS] extraction and no Notion page IDs
    - AS_STILL_RUNNING: as-thread.json status=STILL-RUNNING for some queries
    - POST_INCOMPLETE: some queries posted, some missing

STEP 3 — RETRY DECISION TREE
  IF TASK_A_NOT_RUN:
    Re-run Task A logic inline (read CANONICAL-PROMPT.md Task A template, fill from brief-card, execute).
    Then immediately re-run Task B logic inline.
    Tag every output with metadata flag "retry_03_30=true".
  ELIF TASK_B_NOT_RUN OR POST_INCOMPLETE:
    Re-run Task B logic inline for the missing queries only.
    Tag with "retry_03_30=true".
  ELIF AS_STILL_RUNNING:
    Open each STILL-RUNNING thread in Chrome.
    If now complete: extract + merge + post.
    If still running: log to flag, leave for 06:30 watchdog.

STEP 4 — UPDATE COMPLETION FLAG
  Append a "watchdog_03_30" block to memory/staging/overnight-status-{TODAY}.json:
    {
      "watchdog_03_30": {
        "fired_at": "<ISO ts>",
        "diagnosed": <list of missing-outputs>,
        "actions_taken": <list of retries>,
        "notion_pages_posted_after_retry": <count>,
        "still_outstanding": <list>
      }
    }

STEP 5 — POST-MORTEM ENTRY (if any retry happened)
  If actions_taken is non-empty:
    Append an entry to memory/coaching/lessons-and-mistakes.md under "Watson/System Lessons" section.
    Format: "### {DD-Mon-YY} — Overnight Watchdog 03:30 Retry — {brief 1-line summary}"
    Body: what was missing, why (best inference from logs), retry outcome.
    This is automatic — no Richard input needed.

STEP 6 — INTERIM FLAG TO MORNING ROUTINE
  Write/update memory/staging/morning-briefing-flag.md:
    {
      "overnight_status": "complete" | "complete-after-retry" | "partial" | "still-running",
      "expected_pages": <int>,
      "actual_pages": <int>,
      "page_ids": [<list>],
      "outstanding": [<list>],
      "watchdog_03_30_log": "<one-line summary>"
    }

DEFINITION OF DONE FOR 03:30 WATCHDOG:
  - Brief-card read (or absence confirmed)
  - Diagnosis written to flag
  - Retries attempted where applicable
  - Morning briefing flag updated
```

---

## 06:30 WATCHDOG — FINAL CHECK

**Why 06:30:** Even with the 03:30 retry, some failures may persist (e.g. AS service down, Notion API throttling). The 06:30 watchdog is the **last quality check before Richard wakes up**. If anything is still missing, it surfaces *loudly* into the morning briefing so Richard cannot miss it.

### Prompt body

```text
WATSON — OVERNIGHT WATCHDOG (06:30 FINAL CHECK)
Role: RESEARCHER. Mode: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT (do NOT call request_cowork_directory)
  - Read: memory/skills/scheduled-task-preamble.md
  - Resolve TODAY = current YYYY-MM-DD in Europe/London
  - Brief-card path = memory/staging/researcher-brief-{TODAY}.md
  - Completion flag = memory/staging/overnight-status-{TODAY}.json

STEP 1 — EARLY EXIT IF NO WORK
  - If brief-card does not exist → write morning-briefing-flag.md status="no-overnight-research" → exit.

STEP 2 — FINAL DIAGNOSIS
  Re-read brief-card and metadata.json files.
  Compute final_actual_pages vs expected_pages.
  Compute final_outstanding list.

STEP 3 — ONE LAST AS-EXTRACTION ATTEMPT (if needed)
  If any as-thread.json status=STILL-RUNNING:
    Try once more to extract. If complete, post + record page ID.
    If still running, mark FINAL-INCOMPLETE.

STEP 4 — WRITE THE LOUD FLAG
  Update memory/staging/morning-briefing-flag.md with the FINAL state.
  If status != "complete" or "complete-after-retry":
    Set a LOUD prefix at the top of the flag file:
      "🚨 OVERNIGHT RESEARCH INCOMPLETE — REQUIRES RICHARD ATTENTION"
      Followed by: tickers affected, what's missing, what was tried, what still needs to happen in a live session.
  This file is read by watson-morning-routine — the loud prefix triggers a top-of-routine alert.

STEP 5 — PERMANENT FAILURE LOG
  If status=FINAL-INCOMPLETE:
    Append a permanent entry to memory/coaching/lessons-and-mistakes.md:
      "### {DD-Mon-YY} — Overnight Research Failed Despite Watchdog Retries"
      Body: what was supposed to run, what ran, what was missing after both 03:30 retry and 06:30 check, hypothesised cause, what Richard needs to do manually.
    This becomes a structural record so the failure is never silent.

DEFINITION OF DONE FOR 06:30 WATCHDOG:
  - Final flag written (loud if incomplete, quiet if complete)
  - Permanent log entry written if applicable
  - Morning routine has everything it needs to alert Richard
```

---

## INTERACTION WITH MORNING ROUTINE

`watson-morning-routine` (07:00 UK daily) must include this block at the top of its execution:

```text
STEP 0 — Read memory/staging/morning-briefing-flag.md
  If status starts with "🚨":
    Open the morning brief with the alert before anything else.
    State: tickers affected, what's missing, what was tried.
    Ask Richard: "Resolve now in live session, or queue for later?"
  Else:
    Acknowledge overnight result quietly: "Overnight research: <N> pages posted across <tickers>."
```

(This block is added to the morning routine SKILL when the watchdog tasks go live.)

---

## CREATING THE STANDING SCHEDULED TASKS

These are created **once** as recurring tasks. Use `mcp__scheduled-tasks__create_scheduled_task` with `cron` recurrence.

| Task name | cron (Europe/London) | Prompt body |
|---|---|---|
| `watson-overnight-watchdog-0330` | `30 3 * * *` | Body of "03:30 WATCHDOG" section above |
| `watson-overnight-watchdog-0630` | `30 6 * * *` | Body of "06:30 WATCHDOG" section above |

**Creation procedure:** When this SOP is first put into production, Richard runs (in a live session): *"Create the watchdog scheduled tasks per WATCHDOG-SOP.md."* Watson then calls `mcp__scheduled-tasks__create_scheduled_task` twice with the prompts above, verifies both task IDs returned, and writes the IDs into a `WATCHDOG-INSTALL-LOG.md` next to this file.

If the cron syntax is not supported and only `fireAt` is, create them as *recurring* tasks if the API supports it; if it does not, create as one-off tasks rolled forward each evening by the watchdog itself (each watchdog re-creates tomorrow's at the end of its run).

---

## SAFETY: WATCHDOG IDLENESS

If no brief-card exists for the day, the watchdogs exit immediately at Step 1 with status `no-overnight-research`. They do not run research speculatively, they do not invent work. They are passive insurance.

This means: the watchdogs are safe to run every night even on nights when no overnight RESEARCHER work is briefed. Cost is negligible (a few file reads + an exit).

---

## CHANGELOG

- **28-Apr-26** v1.0 — Created. Pair of standing scheduled tasks at 03:30 + 06:30 UK. 03:30 retries on partial; 06:30 final-checks and surfaces loudly to morning routine. Replaces the previous "rely on Watson reading rules" pattern with structural enforcement.
