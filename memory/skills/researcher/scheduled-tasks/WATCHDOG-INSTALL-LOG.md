# WATCHDOG INSTALL LOG

**Installed:** 28-Apr-26 ~10:30 BST
**Installed by:** SA / RESEARCHER reform session

## STANDING SCHEDULED TASKS CREATED

| Task ID | Cron (Europe/London) | Next run | Purpose |
|---|---|---|---|
| `watson-overnight-watchdog-0330` | `30 3 * * *` | tonight 03:30 UK | Retry pass — diagnose missing outputs, retry inline, log retry |
| `watson-overnight-watchdog-0630` | `30 6 * * *` | tomorrow 06:30 UK | Final check — last AS extraction, loud flag if still incomplete, permanent failure log |

Both tasks were created via `mcp__scheduled-tasks__create_scheduled_task` and confirmed enabled in this session. Per the tool's response, dispatch jitter adds a few minutes — actual fire times are ~03:38 and ~06:36 respectively, which is fine for the design.

## INTEGRATION WITH EXISTING SCHEDULED TASKS

The reform does NOT replace the existing nightly machinery. It augments and disciplines it:

| Existing task | Role under new design |
|---|---|
| `watson-researcher-proposal` (16:00 daily) | Continues to generate the 4pm proposal. After Richard signs off in chat, BRIEF-INTAKE-SOP turns the sign-off into a brief-card. |
| `watson-researcher-executor` (23:05 daily) | Becomes **Task A** in the canonical two-task split. Reads the brief-card, runs [C] research, submits AS, writes Task A flag. Its prompt should be updated to reference CANONICAL-PROMPT.md Task A semantics (see "Follow-up changes" below). |
| `watson-morning-routine` (06:00 daily) | Reads `morning-briefing-flag.md`. Detects loud prefix and surfaces alerts at top of Richard's morning brief. |

A new standing task is needed for **Task B** (extract + post at ~01:00 after the executor's research wave). Recommendation: create `watson-researcher-task-b` at cron `0 1 * * *` (01:00 UK) — this gives the executor's 23:05 run plus AS submission ~90+ min before extraction begins. Not yet created in this session — flagged below.

## FOLLOW-UP CHANGES (NOT YET DONE THIS SESSION)

These need a follow-on session with Richard to align before changing:

1. **Update `watson-researcher-executor` prompt** to reference CANONICAL-PROMPT.md Task A semantics: read brief-card, no `request_cowork_directory`, write Task A completion flag, exit cleanly without waiting for AS.
2. **Create `watson-researcher-task-b`** standing scheduled task at cron `0 1 * * *` running CANONICAL-PROMPT.md Task B.
3. **Add Step 0 to `watson-morning-routine`** that reads `morning-briefing-flag.md` and surfaces loud-prefix alerts.

These three changes would close the loop completely. They are not blocking — the watchdog at 03:30 already provides retry + flag — but they would make the system a single coherent pipeline rather than a watchdog-bolted-onto-legacy.

## FIRST-NIGHT PRE-APPROVAL RECOMMENDATION

Per the scheduled-tasks tool's hint, Richard should click "Run now" once on each watchdog from the Scheduled sidebar to pre-approve any tools they need (file reads, `mcp__workspace__bash`, `notion-fetch`). After the first manual run, future automatic runs will not pause on permission prompts.
