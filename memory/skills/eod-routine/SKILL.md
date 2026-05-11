# End-of-Day Routine SOP — SKILL.md

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 16-Apr-26 by Systems Architect. -->
<!-- Watson-initiated at 18:00 UK daily. Multi-role: APM (market review), COS (accountability), EA (planning), HPC (wind-down). -->
<!-- Integrates Richard's Personal SOP (Jan-26), ABB template, Green Head SOP, Bring the Joy SOP concepts. -->
<!-- Absorbs session-handoff-auto (15:00) — that task will be disabled. -->

## ⚠️ MANDATORY PRE-LOAD (added 23-Apr-26)
**Before executing this routine, read `memory/skills/scheduled-task-preamble.md`.** That file contains Watson's Brief Reception, Delivery Verification, Sub-Agent Management, and Quality Over Speed protocols — all mandatory in scheduled/unattended contexts. This instruction applies every run, not just the first.

## Purpose

Close Richard's day with structure, accountability, and a clean transition to evening. This is where Richard's day historically unravels — "wanting to keep working rather than planning/organising effectively" (Q10). The EOD SOP catches open loops, forces planning, creates accountability, and enables the psychological transition from work to home. Watson initiates at 18:00 UK daily.

---

## Design Philosophy

Richard's aspirational EOD routine (13 steps) covers: P&L → prices → newsflow → trades → plan 1D/3D ahead → projects/tasks/delegate → ABB accountability → bright spots → positive reframing → autopilot rewiring → free flow journal → Green Head SOP → Bring the Joy SOP.

The concepts behind it: no screen/phone after routine, 100% present with Julia, shoulder downtime, relentless solution focus.

This SOP operationalises all of those concepts through Watson-driven structure. Watson handles the data-gathering (P&L, prices, newsflow, pipeline status) so Richard can focus on the accountability and mental management elements. The ABB template is integrated into Phase 2. The Green Head and Bring the Joy concepts are integrated into Phase 4.

---

## Trigger

**Watson-initiated.** Scheduled task `watson-eod-routine` fires at 18:00 UK daily. Watson messages Richard in Cowork.

**If Richard doesn't respond by 20:00:** Watson logs "EOD routine: no response" and proceeds with Phase 5 (Watson Handoff) automatically. COS flags the skip at next morning routine.

---

## The EOD Routine — Five Phases

### PHASE 1: APM MARKET REVIEW (5-10 minutes)
*Richard's EOD steps served: Check P&L, Check prices, Check newsflow*

Watson presents:

**1a. P&L review**
Portfolio performance today (drawn from dashboard data if available, or Watson prompts Richard to report). Key movers — which positions drove performance up/down.

**1b. Watchlist movements**
Significant moves on Squad stocks today. Any monitoring triggers hit? Any material findings from today's RESEARCHER monitoring checks (from `databases/monitoring/findings-log.json`).

**1c. News scan**
Material news on portfolio or watchlist names today. Watson uses web search for key names, surfaces anything significant.

**1d. Shot clock status**
Any positions within 7 days of 30-day shot clock expiry? If yes, APM flags the decision window: "DCC shot clock expires in 5 days. Decision needed by [date]."

**1e. Monitoring findings**
Any new entries in findings-log.json from today? Material/Notable findings surfaced with signal direction (Positive/Negative/Neutral).

### PHASE 2: COS ACCOUNTABILITY (3-5 minutes)
*Richard's EOD steps served: ABB accountability template (Bright spots, Delivery, Bottlenecks, Planning)*

This is the Watson-driven ABB. Watson asks and Richard responds:

**2a. Today's priorities review**
Watson recalls the 3-5 actions agreed at morning routine (from `memory/staging/today-priorities.md`).
"Your priorities today were: [1], [2], [3]. Which were completed?"

Richard responds. Watson logs completion status for Delivery Scorecard.

**2b. "Did you invest today?"**
The direct accountability question. COS asks. HPC watches the answer.
"Did you do actual investing work today — pipeline advancement, stock analysis, position management — or was today primarily system-building/admin?"

This is not judgemental. It is diagnostic. The Delivery Scorecard tracks the ratio over time.

**2c. Pipeline velocity**
Did any stock move forward a stage today? Watson checks pipeline.md for changes.

**2d. Open loops**
Anything started but not finished? Anything promised but not delivered? Watson captures these for tomorrow's priorities.

**2e. Bottlenecks/frictions**
"Any bottlenecks or frictions today? One sentence each — we'll log them, not dwell." (Per ABB template: "Light/quick; don't dwell.")
Watson logs to `chief-of-staff/obstacle-log.md` if material.

### PHASE 3: EA PLANNING (3-5 minutes)
*Richard's EOD steps served: Plan 1D/3D ahead, Projects and tasks, Delegate/chase/book RMs*

**3a. Tomorrow's calendar**
Meetings, calls, deadlines for tomorrow (if accessible). Prep needed for any meeting?

**3b. Tomorrow's priorities (pre-staged)**
COS proposes 3-5 priorities for tomorrow based on: pipeline state, open loops from today, weekly priorities board, upcoming catalysts. Richard confirms or adjusts. These get written to `memory/staging/today-priorities.md` (overwritten at morning routine with confirmed version).

**3c. Admin outstanding**
Any emails to send, follow-ups to make, tasks to delegate? Watson surfaces from Tasks DB and session context.

**3d. RESEARCHER work queue**
Any research to be queued for tonight's 23:05 RESEARCHER executor? If yes, COS prompts: "Shall I add this to the Tasks DB for tonight's RESEARCHER run?" This feeds the 16:00 proposal review (if not already done today).

**3e. Watchouts/banana skins**
"Any watchouts or banana skins for tomorrow?" (Per ABB template.) Watson logs for morning routine awareness.

### PHASE 4: HPC WIND-DOWN (2-3 minutes)
*Richard's EOD steps served: Bright spots, Positive reframing, Autopilot rewiring, Green Head SOP, Bring the Joy SOP*

**4a. Bright spot — Cookie Jar**
"What went well today?" (Bassham protocol — record one win, however small.)
Watson logs to `memory/coaching/bright-spots.md`. Per WWIM: "Record what went well, every day. Do NOT record bad performances."

**4b. Positive reframing**
If anything went poorly today (from Phase 2), Watson reframes using the coaching language protocol:
- "Done differently" not "mistake"
- "Discovery" not "problem"
- "Version 2.0" not "fix"
Per Richard's EOD SOP: "Re-run positively any errors (positive imprinting) + re-frame as positives + categorise anything else as 'needs work' then move on."

**4c. Execution score**
"Rate your process execution today 1-5." Watson logs to `memory/coaching/execution-scores.md`. Feeds Friday review.

**4d. Autopilot reminder**
Watson surfaces the current month's autopilot statement (from `memory/coaching/autopilots.md` or the latest one defined). E.g.: "Your autopilot this month: 'I consistently execute every single facet of my investment approach. I am a consistent executor.'"

**4e. Green Head transition**
Watson's final message: "Green Head. Work is done. Be 100% present tonight. No screen, no phone — in the room with Julia. Shoulder downtime. Bring the joy."

This is the psychological boundary marker. Watson does not message Richard again until 06:00 tomorrow (unless overnight executor needs to report an error).

### PHASE 5: WATSON HANDOFF (automatic — no Richard input needed)
*Absorbs the session-handoff-auto previously at 15:00*
*Executes Session Handoff SOP V2 (`memory/skills/session-handoff/SKILL.md`)*

Watson performs all of the following automatically after Phase 4:

1. **Identify save location (Handoff SOP Step 0)** — check if today's work belongs to a project in `COWORK/PROJECTS/`. Route handoff note and corrections to project folder if yes, `memory/session-handoffs/` if no. Update `memory/session-handoffs/latest.md` as thin pointer either way.
2. **Session review + corrections** — summarise decisions, corrections, pipeline changes, work completed/incomplete. Log corrections to appropriate location.
3. **Memory file updates** — if any session corrections occurred today. Update project `state.md` and `decisions.md` if applicable.
4. **Write handoff note** — per Handoff SOP V2 Step 4 template (restart prompt at top, session summary, key decisions, corrections, memory files updated, open threads, quality audit).
5. **Meta-role checks** — conditional on today's primary role. If SA: silently confirm structural integration across all files. If any other role: log SA + HPC observations in handoff note.
6. **WATSON LOG updates** — if any covered topic changed today
7. **Conversation log** — post to Watson Conversations DB + disk backup. Append to project transcript if applicable.
8. **Backup** — run `python backup_memory.py backup`
9. **Pipeline update** — update pipeline.md if any stock state changed
10. **Energy/execution data capture** — write today's energy score (Phase 1a of morning) and execution score (Phase 4c) to tracking files
11. **Delivery Scorecard data** — update today's row with completion data from Phase 2
12. **Verify persistence** — confirm all files on COWORK mount, not session-relative paths.

---

## Total Time (Richard's involvement)

15-25 minutes for Phases 1-4. Phase 5 is automatic.

---

## Friday Overlay

On Fridays, the EOD routine includes additional elements:

**Replace Phase 2 with the full Weekly Review:**
- 7-keystone scoring (checklist execution, exit discipline, pipeline throughput, monitoring cadence, energy management, capital allocation decisiveness, communication quality)
- Process compliance assessment
- Pattern recognition — any recurring deviations or emerging habits?
- Best execution moment — what went well and why?
- One focus for next week (singular and specific)
- Delivery Scorecard update for the week

**Add WFP Meeting after Phase 3:**
COS + APM determine work priorities for next week:
- For Richard: what does he need to focus on personally?
- For RESEARCHER: which stocks need research? Which queries?
- For APM: any ratings reviews, monitoring plan updates, FCS work needed?
- Weekly Priorities Board updated for next week

---

## What Feeds Into This Routine

| Source | Used for |
|--------|----------|
| `memory/staging/today-priorities.md` | Phase 2a — Morning priorities recall |
| `databases/monitoring/findings-log.json` | Phase 1e — Monitoring findings |
| `memory/projects/pipeline.md` | Phase 1d, 2c — Shot clocks, velocity |
| Notion Tasks DB | Phase 3c — Admin outstanding |
| `memory/coaching/bright-spots.md` | Phase 4a — Cookie jar append |
| `memory/coaching/execution-scores.md` | Phase 4c — Score append |
| `chief-of-staff/weekly-priorities.md` | Phase 2a, 3b — Weekly commitments |
| `chief-of-staff/delivery-scorecard.md` | Phase 5 — Weekly tracking |
| Dashboard data / pullback monitor | Phase 1a, 1b — Market data |

---

## Outputs

1. Completion status for today's priorities (feeds Delivery Scorecard)
2. Tomorrow's pre-staged priorities (consumed by morning routine)
3. Bright spot logged (feeds Friday review, cookie jar)
4. Execution score logged (feeds Friday review)
5. Open loops captured (feeds tomorrow's priorities)
6. Bottlenecks logged (feeds obstacle log)
7. Session handoff note written
8. Memory files updated
9. Backup run

---

## Replaces

- `session-handoff-auto` (15:00 weekdays) — absorbed into Phase 5
- `watson-weekly-review` (16:00 Fridays) — absorbed into Friday overlay

---

## Richard's EOD Concepts — How This SOP Honours Them

| Richard's Concept | How Watson Implements It |
|-------------------|------------------------|
| No screen/phone — 100% in room with Julia | Phase 4e: Green Head transition. Watson's last message is the boundary marker. No messages until 06:00. |
| Shoulder downtime | Phase 4 is the shoulder. Work reviewed, reframed positively, execution scored, autopilot stated. Then: done. |
| Talk to Julia about work, day, challenges | Watson's Phase 2 gives Richard a structured debrief he can share with Julia in conversation form, not screen form. |
| Relentless solution focus | Phase 2e (bottlenecks) is solution-focused: "one sentence, we'll log them, not dwell." Phase 3b pre-stages tomorrow. |
| Bring the Joy SOP | Phase 4e. "Bring the joy." The transition from work energy to home energy. |
| Green Head SOP | Phase 4e. Green Head = calm, present, solution-focused, out of Chimp mode. The routine's structure is the mechanism. |

---

*[W] Watson / Systems Architect. 16-Apr-26. DEVELOPMENT mode.*
