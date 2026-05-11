# CANONICAL SCHEDULED-TASK PROMPT — RESEARCHER OVERNIGHT

**Status:** Live | **Created:** 28-Apr-26 | **Owner:** RESEARCHER role
**Role this file plays:** the ONLY allowed shape for an overnight RESEARCHER scheduled-task prompt. All overnight RESEARCHER tasks are produced by filling in the variables below. Hand-rolling overnight prompts is no longer permitted.

---

## WHY THIS TEMPLATE LOOKS LIKE THIS

Three same-day failures on 28-Apr-26 produced this template. Every structural choice below maps to one of them. Read this section once before editing the template.

| Failure (28-Apr-26) | Root cause | Structural fix in this template |
|---|---|---|
| **gym-trio** — 33 AS submissions never attempted | Prompt called `request_cowork_directory` as pre-flight; UI dialog stalled the unattended session at step 1 | Template never calls `request_cowork_directory`. COWORK is accessed directly via `/sessions/*/mnt/COWORK/` (bash) or `C:\Users\richb\Documents\COWORK\` (file tools). |
| **COMET** — three tasks absorbed into morning routine; context exhausted before AS extraction | Multiple research tasks fired within the same window, all consumed by `watson-morning-routine` at 06:03 | Template enforces the **two-task split** (Task A research+submit at ~01:00; Task B extract+post at ~02:15) with ≥75 min separation. Task B never depends on Task A's session staying alive. |
| **MTRS** — research never ran at all | Verbal agreement to "start at 04:15" with no scheduled task created | The brief-intake SOP (`BRIEF-INTAKE-SOP.md`) makes commit ritual mandatory. This template is the *prompt body* — the intake SOP is the wrapper that creates and verifies the scheduled task. |

The **24-Apr-26 "Do It Right" quality reform** (ONE value: pride in correctness; THREE rules: test it / save it / match the brief; STRUCTURAL ENFORCEMENT) is the philosophical parent of this template. Procedural rules are absorbed into structure. Watson does not "remember" Rule #28/#29/#30 — it fills in this template, which already encodes them.

---

## TEMPLATE VARIABLES

A brief-card produced by the brief-intake SOP must populate these variables. Variables in `{{double-braces}}` are substituted at template-fill time.

| Variable | Type | Example |
|---|---|---|
| `{{BRIEF_CARD_PATH}}` | path | `memory/staging/researcher-brief-{NIGHT-OF-EXECUTION}.md` (dated by the night tasks fire, NOT the day briefed) |
| `{{TICKERS}}` | list | `MTRS-SE, KNIN-CH` |
| `{{STAGES_PER_TICKER}}` | dict | `{MTRS-SE: [IG, Triaging], KNIN-CH: [IG]}` |
| `{{SOURCES}}` | enum | `dual`, `c-only`, `as-only` |
| `{{TASK_LETTER}}` | enum | `A` (research+submit) or `B` (extract+post) |
| `{{TASK_A_FIRE_AT}}` | ISO timestamp UK | `2026-04-29T01:00:00+01:00` |
| `{{TASK_B_FIRE_AT}}` | ISO timestamp UK | `2026-04-29T02:15:00+01:00` |
| `{{EXPECTED_NOTION_PAGES}}` | integer | `7` (per ticker, per stage scope) |
| `{{COMPLETION_FLAG_PATH}}` | path | `memory/staging/overnight-status-2026-04-29.json` |

---

## TEMPLATE — TASK A (RESEARCH + SUBMIT)

This is the prompt body that gets passed to `mcp__scheduled-tasks__create_scheduled_task` for Task A.

```text
WATSON — RESEARCHER OVERNIGHT TASK A (RESEARCH + SUBMIT)
Brief-card: {{BRIEF_CARD_PATH}}
Tickers: {{TICKERS}}
Stages per ticker: {{STAGES_PER_TICKER}}
Sources: {{SOURCES}}
Fire time: {{TASK_A_FIRE_AT}}
Expected Notion pages on completion of Task B: {{EXPECTED_NOTION_PAGES}}

ROLE: RESEARCHER. MODE: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT (do NOT call request_cowork_directory; COWORK is mounted)
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/SKILL-V2.md (Critical Rules section + 23-Query Master Table)
  - Read: {{BRIEF_CARD_PATH}} — this is your authoritative brief
  - If brief-card cannot be read: STOP. Write {{COMPLETION_FLAG_PATH}} with status=failed, reason=brief-card-missing. Exit.

STEP 1 — RESEARCH ([C] AGENTS, NATIVE)
  For each ticker × stage in the brief-card:
    Identify [C] queries from the 23-Query Master Table.
    Dispatch as parallel Sonnet sub-agents using templates from memory/skills/researcher/templates/.
    On return: validate per Rule #10 (two-tier word-count gate).
    Save raw outputs to COWORK/Files/{TICKER}/{STAGE}/{QUERY-NUM}-{QUERY-NAME}/raw-C.md.
    Write metadata.json stub (source=C, word_count, timestamp_returned).

STEP 2 — SUBMIT ([AS] AGENTS, BROWSER)
  For each ticker × stage with [AS] queries in scope:
    Prepare prompts (Sonnet) per templates from memory/skills/researcher/templates/.
    Submit via Haiku browser agent to research.alpha-sense.com/gensearch in Deep Research mode.
    Verify mode selection (screenshot + JS aria-pressed=true).
    Log AS thread URLs to COWORK/Files/{TICKER}/{STAGE}/{QUERY-NUM}-{QUERY-NAME}/as-thread.json with status=PENDING.
    DO NOT wait for AS to complete. Task B will extract.

STEP 3 — TASK A COMPLETION FLAG
  Write {{COMPLETION_FLAG_PATH}} with:
    {
      "task": "A",
      "fired_at": "{{TASK_A_FIRE_AT}}",
      "completed_at": "<actual ISO timestamp>",
      "tickers": {{TICKERS}},
      "c_outputs_saved": <count>,
      "as_threads_submitted": <count>,
      "status": "complete" | "partial" | "failed",
      "next_task": "B at {{TASK_B_FIRE_AT}}"
    }

STEP 4 — POST-RUN REPORT
  Append a section to memory/conversations/researcher-overnight-{{YYYY-MM-DD}}.md:
    - What was attempted (tickers × stages × queries)
    - Evidence: file paths, word counts, AS thread URLs
    - Any items skipped/failed and why
    - Hand-off line: "Task B at {{TASK_B_FIRE_AT}} will extract AS + merge + post."

DEFINITION OF DONE FOR TASK A:
  - All [C] raw files saved to COWORK/Files/{TICKER}/{STAGE}/{QUERY-NUM}-*/raw-C.md
  - All [AS] thread URLs logged with status=PENDING
  - Completion flag written
  - Post-run report written
  Raw files alone are NOT done — flag and report are mandatory.

DO NOT:
  - Call mcp__cowork__request_cowork_directory
  - Wait for AS extraction (Task B's job)
  - Post anything to Notion (Task B's job)
  - Schedule any further tasks (the watchdog handles retries)
```

---

## TEMPLATE — TASK B (EXTRACT + POST)

```text
WATSON — RESEARCHER OVERNIGHT TASK B (EXTRACT + POST)
Brief-card: {{BRIEF_CARD_PATH}}
Tickers: {{TICKERS}}
Stages per ticker: {{STAGES_PER_TICKER}}
Sources: {{SOURCES}}
Fire time: {{TASK_B_FIRE_AT}}
Expected Notion pages: {{EXPECTED_NOTION_PAGES}}

ROLE: RESEARCHER. MODE: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT (do NOT call request_cowork_directory)
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/notion-posting-sop.md
  - Read: memory/skills/notion-posting-standard/SKILL.md (full)
  - Fetch Stock Notes DB schema: notion-fetch collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2
  - Read {{COMPLETION_FLAG_PATH}}.
    - If Task A status != "complete" or "partial": STOP. Append to flag: status=B-skipped, reason=A-incomplete. Exit.
  - Read {{BRIEF_CARD_PATH}}.

STEP 1 — EXTRACT [AS] OUTPUTS
  For each ticker × stage × AS query with status=PENDING:
    Open AS thread URL in Chrome.
    Verify thread completed (sidebar label shows "Deep Research", output present).
    If still running: mark as_thread.json status=STILL-RUNNING and skip this query (watchdog retry).
    If complete: download PDF, extract via pdfplumber, save to .../raw-AS.md.
    Validate per Rule #10 (two-tier word-count gate).
    Update as-thread.json status=EXTRACTED.

STEP 2 — MERGE (DUAL-SOURCE QUERIES)
  For each query that is dual-source per the Master Table:
    Apply pre-merge validation gate (Rule #14).
    If pass: merge per backbone defaults (Rule #15) into merged.md.
    If fail: post [C]-only; save [AS] as local reference.

STEP 3 — POST TO NOTION (AS-FIRST GATE APPLIES)
  For each query in scope, FIRST determine its source from the Master Table (SKILL-V2 23-Query Master Table):
    - SOURCE = "C" only             → eligible to post (single-source [C])
    - SOURCE = "AS" only            → eligible to post ONLY if raw-AS.md exists, validated, status=EXTRACTED
    - SOURCE = "AS + C" (dual)      → eligible to post ONLY if ALL of:
        (a) raw-AS.md exists for this query
        (b) Rule #10 (two-tier word-count) and Rule #14 (pre-merge validation) have been applied
        (c) merged.md has been written, OR Rule #14 explicitly failed with logged reason → [C]-only fallback
      If [AS] is still STILL-RUNNING or NOT-YET-EXTRACTED for a dual-source query: DO NOT POST. Mark query as POSTING-DEFERRED in metadata.json, leave for the 03:30 / 06:30 watchdog.
      Posting a dual-source query as [C]-only because "AS is slow" or "might not come back" is forbidden. Wait, or defer.
  For each query that passes the gate:
    Apply 30%+ sentiment highlighting.
    Post per notion-posting-standard/SKILL.md.
    MANDATORY properties: Stock(s) relation set; title format per Rule #21.
    On post success: write Notion page_id to metadata.json.
  Log every POSTING-DEFERRED query in the Task B completion flag's "skipped_or_failed" list with reason="AS-not-yet-in".

STEP 4 — VERIFY POSTING
  Spot-check at least one page per ticker.
  Confirm: properties set, content full-length, highlighting applied, IAJA tagged at ESA/DD.

STEP 5 — TASK B COMPLETION FLAG
  Update {{COMPLETION_FLAG_PATH}}:
    {
      "task": "B",
      "fired_at": "{{TASK_B_FIRE_AT}}",
      "completed_at": "<actual ISO timestamp>",
      "notion_pages_posted": <count>,
      "expected_pages": {{EXPECTED_NOTION_PAGES}},
      "status": "complete" | "partial" | "failed",
      "page_ids": [<list>],
      "skipped_or_failed": [<list with reasons>]
    }

STEP 6 — POST-RUN REPORT
  Append final section to memory/conversations/researcher-overnight-{{YYYY-MM-DD}}.md.
  Include all Notion page IDs as evidence of completion.

DEFINITION OF DONE FOR TASK B:
  - All [AS] outputs extracted (or marked STILL-RUNNING for watchdog)
  - All in-scope outputs posted to Notion with page IDs recorded
  - Stock(s) relation set on every page
  - Completion flag updated with status, page IDs, and any failures
  - Post-run report written
  Files on disk alone are NOT done. Notion page IDs are the definitive completion signal.

DO NOT:
  - Call mcp__cowork__request_cowork_directory
  - Re-run [C] research (Task A's job)
  - Make investment verdicts (RESEARCHER produces Information; APM does Analysis + Judgement — Rule #19)
```

---

## SINGLE-TASK VARIANT (FOR [C]-ONLY BRIEFS)

The single-task variant is ONLY for briefs where `{{SOURCES}} = "c-only"` AND every query in scope is `C`-only per the Master Table. If any query in scope is dual-source (`AS + C`), use the two-task split instead — the AS-first gate (Inviolate Rule #5) makes the single-task variant unsafe for dual-source work.

If `{{SOURCES}} = "c-only"` there is no AS extraction phase. In this case the brief-card produces ONE task instead of two. Use the Task A template above with these modifications:

- STEP 2 (SUBMIT [AS]) is omitted entirely.
- STEP 3 (TASK A COMPLETION FLAG) becomes the final flag — set `next_task` to `null` and add a `proceed_to_post` block:

```text
STEP 3 (REPLACED) — POST + VERIFY
  Apply 30%+ highlighting → post to Notion → record page IDs in metadata.json → spot-check verify.
  Write completion flag with status, page IDs, and any failures.
  See Task B Steps 3-6 for the posting block; follow those exactly.
```

Single-task variant fires at ~01:00 UK and completes in one session window. Use this for small [C]-only briefs (e.g. JDG IG [C]-only, or thematic-research updates).

---

## INVIOLATE RULES (THE ONLY ONES THIS TEMPLATE CARRIES)

These rules survive in this template because they cannot be made structural — they govern Watson's *judgement*, not the prompt's mechanics.

1. **Definition of "complete"** = Notion page IDs recorded in metadata.json. Raw files on disk alone = incomplete. Flag and report are mandatory.
2. **Two-tier word-count gate** (SKILL-V2 Rule #10) is applied on every sub-agent return. <50% min = do not post; 50–75% min + section coverage <80% = do not post; otherwise post.
3. **Stock(s) relation is mandatory** on every Notion post. Without it, the page is invisible in stock-filtered views.
4. **No `request_cowork_directory` call, ever**, in any scheduled task. COWORK is mounted; access it directly.
5. **AS-FIRST POSTING GATE — dual-source queries cannot post until AS is in (added 28-Apr-26).** For any query whose Master Table source is `AS + C` (i.e. dual-source): do NOT post the Notion page until (a) [AS] output has been extracted to `raw-AS.md`, (b) word-count + ticker validation passed (Rule #10 + #14), (c) the merge has been written to `merged.md`. Posting a `[C]`-only memo for a dual-source query is **only permitted** if the pre-merge validation gate (Rule #14) has explicitly failed and the failure has been logged with reason. Posting prematurely because AS "looks slow" or "might not come back" is forbidden — the query waits, or escalates to the next watchdog window. Single-source queries (`C` only or `AS` only per Master Table) are unaffected by this gate. [D]
6. **CLOSE CHROME at end of Phase 1 (added 30-Apr-26 v2.0).** The Phase 1 (live session) workflow ends with Chrome closed. NEVER keep Chrome alive across the wait window. Phase 2 cold-reopens fresh windows. This is the structural fix for Chrome tab discard / Memory Saver / blank-pane / renderer-hang failures. SKILL-V2 Rule #30.
7. **AUTO-RESUBMIT BROKEN AS THREADS in Phase 2 (added 30-Apr-26 v2.0).** Per SKILL-V2 Rule #31: if Phase 2 extraction fails after 2-3 retries over 15 min AND original submission >120 min ago → resubmit fresh in new Chrome window. Resubmissions are free. Do NOT defer broken threads indefinitely. Full decision tree in `as-claude-research-sop-v2.md` Rule #31 section.
8. **QC FOOTER MANDATORY (added 30-Apr-26 v2.0).** Per SKILL-V2 Rule #32: every Notion memo posted must include the QC headline pill at top + audit footer block at bottom, both auto-generated from metadata.json. Spec in `notion-posting-sop.md` §Step 4.5.

---

## FOUR-PHASE EXECUTION MODEL (v2.0, 30-Apr-26)

The TASK A / TASK B split above is the legacy two-task variant. The **canonical model is now four phases** per SKILL-V2 Rule #30. Both variants remain valid:

| Variant | When to use |
|---|---|
| **Two-task (A/B)** | Simple briefs, smaller token budget, where extraction is reliable and AS health is good |
| **Four-phase** | Default for dual-source overnight briefs. Maximum reliability, minimum context per phase. |

### Four-phase mapping

| Phase | Old name | Fire time | Chrome state |
|---|---|---|---|
| Phase 1 | (was Task A "research + submit") | Live session, immediately on brief sign-off | Open during; **CLOSED at end** |
| Phase 2 | (was Task B step 1 "extract") | Scheduled 02:00 UK or ≥3h post-submission | **Cold reopen per thread**; closed at end |
| Phase 3 | (was Task B step 2 "merge") | Scheduled ~02:30 UK | Not used |
| Phase 4 | (was Task B step 3-6 "post") | Scheduled ~03:00 UK | Not used |

### Phase 2 task prompt (canonical)

```text
WATSON — RESEARCHER OVERNIGHT PHASE 2 (EXTRACT — COLD REOPEN)
Brief-card: {{BRIEF_CARD_PATH}}
Fire time: {{PHASE_2_FIRE_AT}} (default 02:00 UK)
Reads: as-thread.json files in COWORK/Files/{TICKER}/{STAGE}/{QUERY-NUM}-*/
Writes: raw-AS.md per thread + updated as-thread.json with status=EXTRACTED

ROLE: RESEARCHER. MODE: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/as-claude-research-sop-v2.md (§Step 6 + Rule #31)
  - Read: {{BRIEF_CARD_PATH}}
  - Validate manifest header (blocks_count matches body sections)

STEP 1 — COLD-REOPEN EXTRACTION (per thread)
  For each thread URL in as-thread.json with status=SUBMITTED:
    1. Open fresh Chrome window (or fresh tab in fresh browser session)
    2. resize_window(1920, 1080)
    3. Navigate to thread URL
    4. Wait 60 seconds
    5. Check for PDF Download button
    6. If absent: wait 60s more, recheck (up to 3 min total)
    7. If still absent after 3 min → APPLY RULE #31 AUTO-RESUBMIT DECISION TREE
    8. If present: download PDF, extract via pdfplumber, save raw-AS.md, validate per Rule #10
    9. Update as-thread.json: status=EXTRACTED, extracted_at=<ISO ts>
    10. Close tab/window before opening next URL

STEP 2 — RULE #31 AUTO-RESUBMIT (when triggered)
  If extraction failed AFTER 15 min retry window AND original submission >120 min ago:
    1. Re-read prompt_text from as-thread.json
    2. Open fresh Chrome window, submit per Phase 1 protocol
    3. Run §Step 3a five-check verification on new thread
    4. Update as-thread.json: old thread status=BROKEN_RESUBMITTED, new thread status=SUBMITTED
    5. Defer extraction of new thread to next Phase 2 cycle (≥45 min later)
    6. Set metadata.json auto_resubmit_triggered=true (surfaces in QC footer)
  
  If a SECOND auto-resubmit cycle also fails 120 min later:
    STOP. Surface 🚨 AS_REPEATED_FAILURE to morning-briefing-flag.md.

STEP 3 — COMPLETION FLAG
  Write/append to {{COMPLETION_FLAG_PATH}}:
    {
      "phase": 2,
      "fired_at": "{{PHASE_2_FIRE_AT}}",
      "completed_at": "<actual ISO ts>",
      "extracted_count": <int>,
      "auto_resubmitted_count": <int>,
      "still_running_count": <int>,
      "next_phase": "Phase 3 at {{PHASE_3_FIRE_AT}}"
    }

DEFINITION OF DONE FOR PHASE 2:
  - All threads either EXTRACTED, BROKEN_RESUBMITTED, or STILL_RUNNING (logged with reason)
  - Chrome closed
  - Completion flag written
```

### Phase 3 task prompt (canonical)

```text
WATSON — RESEARCHER OVERNIGHT PHASE 3 (MERGE)
Brief-card: {{BRIEF_CARD_PATH}}
Fire time: {{PHASE_3_FIRE_AT}} (default 02:30 UK)
Reads: raw-C.md + raw-AS.md pairs from COWORK/Files/
Writes: merged.md + qc-audit.md per dual-source query

ROLE: RESEARCHER. MODE: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/SKILL-V2.md (§Rules #14, #15, #17, #18, #32)
  - Read: {{BRIEF_CARD_PATH}}
  - Read prior Phase 2 completion flag — confirm at least some threads EXTRACTED

STEP 1 — APPLY MERGE PROTOCOL (per dual-source query)
  For each query in scope where Master Table source = AS+C AND raw-AS.md status=EXTRACTED:
    Apply pre-merge validation gate (Rule #14)
    If pass: merge per backbone defaults (Rule #15) into merged.md
    If fail: post [C]-only; save [AS] as local reference (log Rule #14 failure)
  For queries where raw-AS.md is BROKEN_RESUBMITTED or STILL_RUNNING: defer to next Phase 3 cycle.

STEP 2 — GENERATE QC AUDIT FOOTER (per query)
  Run scripts/generate_qc_footer.py {ticker} {stage} {query-num}
  Output: qc-audit.md in query folder + footer block ready for Phase 4 to append to merged.md
  Headline pill block written separately for Phase 4 to prepend.

STEP 3 — COMPLETION FLAG
  Append phase 3 block to {{COMPLETION_FLAG_PATH}}.
  
DEFINITION OF DONE FOR PHASE 3:
  - All eligible queries merged or [C]-only fallback logged
  - qc-audit.md written for every query
  - Completion flag updated
```

### Phase 4 task prompt (canonical)

```text
WATSON — RESEARCHER OVERNIGHT PHASE 4 (PUBLISH)
Brief-card: {{BRIEF_CARD_PATH}}
Fire time: {{PHASE_4_FIRE_AT}} (default 03:00 UK)
Reads: merged.md (or notion-formatted.md) + qc-audit.md per query
Writes: Notion pages + dashboard manifest links + final completion flag

ROLE: RESEARCHER. MODE: SCHEDULED / UNATTENDED.

STEP 0 — PRE-FLIGHT
  - Read: memory/skills/scheduled-task-preamble.md
  - Read: memory/skills/researcher/notion-posting-sop.md (esp. §Step 4.5 QC footer)
  - Read: memory/skills/notion-posting-standard/SKILL.md (full)
  - Fetch Stock Notes DB schema: notion-fetch collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2

STEP 1 — POST TO NOTION (per query)
  For each query with merged.md or notion-formatted.md ready:
    Prepend QC headline pill (from qc-audit.md)
    Append QC audit footer block (from qc-audit.md)
    Apply 30%+ sentiment highlighting if not already done
    Post per notion-posting-standard/SKILL.md
    MANDATORY properties: Stock(s) relation set; title format per SKILL-V2 Rule #21
    On post success: write Notion page_id to metadata.json

STEP 2 — DASHBOARD LINK (when dashboard build is live — Q2 follow-up)
  Update RESEARCH STAGES tab manifest with Notion page_id link per query.

STEP 3 — VERIFY POSTING
  Spot-check at least one page per ticker.

STEP 4 — FINAL COMPLETION FLAG
  Append phase 4 block to {{COMPLETION_FLAG_PATH}} with notion_pages_posted, page_ids, skipped_or_failed.

DEFINITION OF DONE FOR PHASE 4:
  - All eligible queries posted with QC pill + footer
  - All page IDs recorded
  - Completion flag finalised with status=complete
```

---

## CHANGELOG

- **28-Apr-26** v1.0 — Created. Absorbs former SKILL-V2 Rules #28, #29, #30 into structure. Two-task split is the default for any dual-source brief. References scheduled-task-preamble.md for the universal unattended-mode disciplines.
- **30-Apr-26** v2.0 — FOUR-PHASE MODEL added. Inviolate Rules #6, #7, #8 added (close Chrome at end of Phase 1; auto-resubmit per Rule #31; QC footer mandatory). Two-task variant retained for simple briefs. Locked per Richard's instruction.
