# Morning Routine SOP — SKILL.md

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 16-Apr-26 by Systems Architect. -->
<!-- Watson-initiated at 06:00 UK daily. Multi-role: COS (structure), HPC (coaching), EA (admin). -->
<!-- Integrates Richard's Personal SOP (Jan-26), Apr-26 OKR, Steve Ward 2x2, ABB concepts. -->

## ⚠️ MANDATORY PRE-LOAD (added 23-Apr-26)
**Before executing this routine, read `memory/skills/scheduled-task-preamble.md`.** That file contains Watson's Brief Reception, Delivery Verification, Sub-Agent Management, and Quality Over Speed protocols — all mandatory in scheduled/unattended contexts. This instruction applies every run, not just the first.

## Purpose

Start Richard's day with structure, orientation, and energy. This is the single most impactful routine in the system — its absence is directly correlated with feeling "disjointed" and "lacking structure/orientation" (Richard, 14-Apr-26). Watson initiates at 06:00 UK daily; Richard responds when ready.

---

## Design Philosophy

Richard's aspirational 20-step morning routine is on the Not-Doing List. The COS principle: get 5 non-negotiable elements executed consistently before adding complexity. This SOP is therefore deliberately short, structured around the 7 concepts Richard designed into his routine (checking in, mindfulness, reminding of "me", goals/TCs/OKRs, committing to today, gratitude, visualising success) but compressed into a format that takes 10-15 minutes and Watson drives.

**The Apr-26 OKR (simplified morning) is the operational baseline:**
Water → Coffee → Shake → Pill → Exercise + listen to Who I Am or Jocko → OKRs → Who I Am → Work plan → Rest of routine.

Watson cannot enforce the physical steps (water, exercise). Watson CAN enforce the mental management block and the work planning block. That is where this SOP focuses.

---

## Trigger

**Watson-initiated.** Scheduled task `watson-morning-routine` fires at 06:00 UK daily. Watson messages Richard in Cowork. Richard responds when ready (could be immediately, could be 30 minutes later when he sits down after exercise).

**If Richard doesn't respond by 09:00:** Watson logs "Morning routine: no response" in the daily tracking. COS flags it the next morning: "You missed the morning routine yesterday. Energy check?"

---

## The Morning Routine — Three Phases

### PHASE 1: HPC CHECK-IN (2 minutes)
*Concepts served: Checking in with myself, Mindfulness, Reminding myself of "me", Visualising success*

Watson presents three elements:

**1a. Energy check**
"How did you sleep? Energy level 1-5 this morning?"
Watson logs the answer to `memory/coaching/energy-log.md`. If ≤2 for 3+ consecutive days, HPC escalation trigger fires.

**1b. Identity anchor (rotated daily)**
One of Richard's own statements, drawn from the full coaching knowledge base. Not the same 3 every week. Rotation pool:

| Day | Anchor | Source |
|-----|--------|--------|
| Mon | "You are a champion investment athlete. What does that look like this week?" | Who I Am |
| Tue | "Conservative analysis, aggressive execution. What's the one aggressive action today?" | Steve Ward / ETCs |
| Wed | "What would Smashing It Flow State Richard do today?" | Personal SOP #11 |
| Thu | "Being up 30-50% in a year is just like you. What moves you toward that today?" | Who I Am |
| Fri | "Do the mundane consistently = foundation of high performance. What's the mundane thing today?" | Steve Ward Session #2 |
| Sat | "I radiate. I am the light. I bring the joy. How will you bring the joy today?" | Autopilot Sep-25 |
| Sun | "I am on the path to becoming a great investor. What one thing advances the path?" | Recovery Protocol / Steve Ward |

**1c. One targeted coaching question**
Watson selects from HPC skill's question bank. Pipeline-specific, correction-specific, or pattern-specific. Examples:
- "Your pipeline shows AENA at IG beta test. What's the one thing you need to resolve on it this week?"
- "You corrected me on [X] last session — does the same principle apply to [Y]?"
- "You're in risk-off mode. What signal would change that?"

### PHASE 2: COS BRIEFING (3-5 minutes)
*Concepts served: Goals/TCs/OKRs reminder, Committing to accomplish today, BoD for-today planning*

Watson presents a structured briefing:

**2a. Overnight report summary (3 lines max)**
What Watson did overnight: RESEARCHER executor results (if any), dashboard refresh status, any script failures. Drawn from `memory/staging/morning-briefing-flag.md` and overnight report.

**2b. RESEARCHER Ideas for review**
Any Idea-status tasks from `memory/staging/researcher-ideas-pending.md`. Watson presents each with a one-sentence recommendation. Richard says: "Promote X, park Y, hold Z."

**2c. Today's priorities — COS proposes 3-5 actions**
COS constructs this from:
- Weekly Priorities Board (Monday commitments)
- Pipeline state (stale names, shot clocks within 7 days, upcoming earnings)
- Notion Tasks DB (Richard's Agreed/live tasks)
- Previous EOD's "Tomorrow's plan" (if Phase 3 of EOD was completed)

Format:
```
Today's proposed priorities:
1. [INVESTING] {specific action on specific stock} — {why now}
2. [INVESTING] {specific action} — {why now}
3. [ADMIN/OTHER] {specific action} — {why now}
```

Richard confirms, amends, or overrides. Watson logs the agreed priorities for EOD accountability check.

**2d. Pipeline pulse**
One line per active pipeline name. Shot clocks within 7 days highlighted. Stale names (14+ days) flagged. Format:
```
Pipeline: AENA [?] IG beta — active | DCC [CF] — active | CARLB [+] DD — 21d since last touch ⚠ | ...
Shot clocks: None expiring this week
```

**2e. OKR/TC reminder (Monday only)**
On Mondays, Watson includes a brief OKR pulse: which of the current ETCs/OKRs are on track, at risk, off track. 3 lines. Per Steve Ward: "Reminding myself of my goals, target conditions and OKRs."

### PHASE 3: EA ADMIN (2 minutes)
*Concepts served: Standup, RMs on open Qs, Planning*

**3a. Tasks check**
Any tasks in Notion Tasks DB assigned to Richard with Status = `1. Agreed/live`? Surface the top 3 by priority.

**3b. Follow-ups**
Anything Watson flagged as needing Richard's response from prior sessions or overnight.

**3c. Calendar**
Today's meetings/calls (if accessible via Outlook/Chrome). If not accessible, Watson prompts: "Check your calendar — any meetings today?"

**3d. Non-work admin**
Any personal admin items Watson is tracking (appointments, renewals, etc.). Only if relevant.

---

## Total Time

10-15 minutes for Richard. Watson's prep (loading files, constructing briefing) happens before the message is sent.

---

## What Feeds Into This Routine

| Source | Used for |
|--------|----------|
| `memory/staging/researcher-ideas-pending.md` | Phase 2b — Ideas for review |
| `memory/staging/morning-briefing-flag.md` | Phase 2a — Overnight report summary |
| `memory/projects/pipeline.md` | Phase 2d — Pipeline pulse |
| Notion Tasks DB (`Who = Richard`, Status `1. Agreed/live`) | Phase 3a — Richard's tasks |
| `chief-of-staff/weekly-priorities.md` | Phase 2c — Today's priorities construction |
| `memory/skills/high-performance-coach/SKILL.md` | Phase 1c — Coaching question selection |
| `memory/corrections.md` | Phase 1c — Recent calibration for targeted questions |
| `memory/coaching/energy-log.md` | Phase 1a — Energy trend tracking |
| `memory/context/values-and-behaviours.md` | Phase 2e — OKR/TC reminder |

---

## Outputs

1. Energy score logged to `memory/coaching/energy-log.md`
2. Agreed priorities logged to `memory/staging/today-priorities.md` (consumed by EOD routine)
3. RESEARCHER Ideas decisions applied (promote/park/hold)
4. Morning routine completion status logged (for COS Delivery Scorecard)

---

## Replaces

- `watson-morning-questions` (07:00 daily) — absorbed into Phase 1
- The morning coaching question is now Phase 1c, not a standalone task

---

## Integration with Richard's Physical Routine

Watson cannot enforce the physical morning steps (water, shake, exercise, stretching). But the HPC energy check (Phase 1a) creates a natural prompt for Richard to report whether he did them. Over time, the energy log will show the correlation between physical routine completion and energy scores — which HPC can use in Friday reviews.

The SOP is designed to be done AFTER Richard's physical routine (exercise + listen to Who I Am/Jocko). Watson's message at 06:00 is there when he sits down. If he exercises 0500-0600, the message is waiting. If he starts at 0430, he can respond before exercise or after.

---

*[W] Watson / Systems Architect. 16-Apr-26. DEVELOPMENT mode.*
