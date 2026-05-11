---
name: Daily Briefing & Review
description: CoS-owned skill for morning briefing and end-of-day review. Produces a daily summary file (.md + Notion page) at both ends of the working day.
role: Chief of Staff
type: skill
created: 2026-03-30
---

# Daily Briefing & Review Skill

## Purpose

Two structured touchpoints per working day: a **morning briefing** (when Richard first interacts) and an **end-of-day review** (at session close or handoff). Each produces a daily summary file saved locally and posted to Notion. The CoS owns this skill; HPC and Buddhist Mentor contribute specific sections.

This is not optional. If Richard starts a session and Watson has not delivered the morning briefing, Watson delivers it before any other work. If a session ends without an EOD review, Watson flags it.

---

## Morning Briefing

### Trigger
First interaction of the day with Richard. Watson detects this by checking:
1. Is there a daily summary file for today's date? If not → morning briefing.
2. Has Watson already delivered a morning briefing in this session? If not → morning briefing.

### Structure

```
# Daily Briefing — [Day] [DD Mon YYYY]

## Yesterday's Summary
[2-3 sentences: what was accomplished, what wasn't, any decisions made]

## Overnight Flags [D] (16-Apr-26)
[Issues, concerns, or questions raised in last night's Watson Overnight Report. Pulled from Watson Log DB entry. Format: each flag on one line — what the concern is + suggested action. If no flags: "Overnight run clean — no flags." If no overnight report found: "No overnight report found — check Watson Log DB."]

## Today's Priorities (CoS)
1. [Priority 1 — with completion criteria]
2. [Priority 2 — with completion criteria]
3. [Priority 3 — with completion criteria]
[Source: Weekly Priorities Board, overdue items, pipeline triggers]

## Overdue / Carried Forward
- [Item — originally due X, now Y days overdue]
[If nothing overdue: "Clean slate."]

## Market / Pipeline Flags
- [Any time-sensitive pipeline items: earnings dates, catalyst windows]
- [RS & Breadth flags if dashboard data available: industries/positions showing momentum shifts]
- [Market context relevant to current positions or watchlist]

## HPC Check-In
[1 targeted question about energy, wellbeing, or process — calibrated to recent patterns]
[E.g., "How did you sleep? You've been building hard for 3 days."]

## Mode & Role
Running as: [DEVELOPMENT/EXECUTION]
Primary role: [based on priorities]
[Watson infers and states. Richard corrects if wrong.]
```

### Pre-Briefing: Overnight Report + Scheduled Task Health Check [D] (31-Mar-26; updated 16-Apr-26)
Before generating the briefing, Watson:
1. Fetches the **Watson Log DB** (`collection://4bc35e90-9b0b-820a-a5c1-873d4c355477`) and retrieves the most recent overnight report (Subject contains "Watson Overnight Report" + today's or yesterday's date)
2. Extracts any **issues, concerns, or flags** raised in that report — these become the **Overnight Flags** section of the morning briefing
3. Uses `list_scheduled_tasks` to check all active scheduled tasks: flag any that should have fired overnight but did not complete, or that have been running >2 hours with <10 turns (**STALLED**)
4. If a task failed or stalled, add it to Today's Priorities as item #1 with a recommendation (retry, take over manually, or investigate)

This was added after the sector-taxonomy-stock-update task stalled overnight on 30-Mar-26. Overnight Flags section added 16-Apr-26 per Richard's direction.

### Data Sources (read before generating)
| Source | What to extract |
|--------|----------------|
| session-handoffs/latest.md | Yesterday's summary, open threads, next priorities |
| chief-of-staff/weekly-priorities.md | This week's contract, completion status |
| coaching-log.md | Recent HPC observations for calibrating check-in question |
| corrections.md | Any recent calibration points to act on |
| projects/pipeline.md | Time-sensitive items, stage changes |
| RS & Breadth dashboard (when live) | Momentum flags on held positions |
| Notion Tasks DB | Overdue "Agreed/live" items |
| Scheduled tasks list | Overnight task health — stalled, failed, or completed |
| Watson Log DB (overnight report entry) | Issues, concerns, flags from last night's watson-task-executor run |

### Delivery
1. Generate the briefing content
2. Present to Richard in chat (full text)
3. Save to `memory/daily-summaries/YYYY-MM-DD.md`
4. Post to Notion as `[W] Daily Briefing — DD Mon YYYY` (under daily log or journal parent)

---

## End-of-Day Review

### Trigger
Any of:
- Richard says "handoff", "EOD", "end of day", "wrap up", or similar
- Session handoff protocol is invoked
- Watson judges the working day is ending (last interaction before evening)
- Auto-trigger at 15:00 UK weekdays (session-handoff-auto)

### Structure

```
## End-of-Day Review — [Day] [DD Mon YYYY]

### What We Did
[Numbered list of activities/outputs, grouped by role if multiple roles active]
1. [Activity] — [why it matters / what it feeds into]
2. [Activity] — [why it matters]
...

### Key Decisions
- [Decision 1 — context and rationale]
- [Decision 2]
[If no decisions: "No major decisions today — execution day."]

### Deliverables
| File / Output | Location | Status |
|---------------|----------|--------|
| [file name] | [COWORK path or Notion] | [Complete/WIP] |

### Priority Scorecard
| Priority | Status | Notes |
|----------|--------|-------|
| [Priority 1 from morning] | Done / Partial / Not started | [brief note] |
| [Priority 2] | | |
| [Priority 3] | | |

### Done Well (Selk)
[1 specific thing Richard executed well today — evidence-based, not generic]

### Get Better (Selk)
[1 specific thing to improve tomorrow — actionable, not vague]

### Corrections Logged
[Count + brief description, or "None today"]

### Memory Files Updated
[List of files changed during the session]

### Tomorrow's Likely Priorities
[Watson's best guess at tomorrow's top 3, based on pipeline state and what was/wasn't completed today]

### Open Threads
[Anything unresolved that needs attention]
```

### Delivery
1. Generate the review content
2. Present to Richard in chat (full text)
3. **Append** EOD section to existing `memory/daily-summaries/YYYY-MM-DD.md` (morning briefing should already be there)
4. Update the Notion page `[W] Daily Briefing — DD Mon YYYY` with EOD section appended
5. Also write to `memory/session-handoffs/latest.md` (this IS the handoff note — the daily review replaces the ad-hoc handoff)

---

## File Management

### Daily Summary Files
- Location: `memory/daily-summaries/YYYY-MM-DD.md`
- One file per day. Morning briefing creates it; EOD review appends to it.
- Rolling — keep all files. They form a searchable daily log.
- **CRITICAL:** Write to COWORK mount only. Never session-relative paths.

### Notion Pages
- Title format: `[W] Daily Briefing — DD Mon YYYY`
- One page per day. Morning creates; EOD updates.
- Parent: TBD — Richard to specify which Notion database/page these live under. Default: Watson Operating Manual or Personal Journal.

### Relationship to Session Handoff
This skill **supersedes** the ad-hoc session handoff note for days Watson is active. The daily summary file IS the handoff note. The `session-handoffs/latest.md` file is still updated (for backward compatibility and session-start reading), but it's generated from the daily summary, not written separately.

Multi-session days: If Richard has multiple sessions in one day, each session's start checks for the existing daily summary and picks up from where it left off. The EOD review covers the full day, not just the last session.

---

## Integration with Other Roles

| Role | Morning contribution | EOD contribution |
|------|---------------------|-----------------|
| **CoS** | Priorities, overdue items, mode/role suggestion | Priority scorecard, done well/get better, tomorrow's priorities |
| **HPC** | Energy/wellbeing check-in question | Behavioural observations from the day (if any) |
| **Buddhist Mentor** | Optional: brief equanimity anchor if stress signals present | Optional: reflection prompt if attachment/aversion patterns observed |
| **APM** | RS & Breadth flags, position momentum alerts | Position-level observations |
| **SA** | System gaps or improvements identified | Memory files updated, skill changes |

---

## Quality Standards

- **Morning briefing: under 200 words in chat.** Crisp. Actionable. Not a report — a launch pad. The full detail goes in the file; the chat delivery is the executive summary.
- **EOD review: under 400 words in chat.** Comprehensive but scannable. Richard should be able to read it in 90 seconds.
- **Priorities always have completion criteria.** Not "work on MTU" but "MTU: extract 3 AS reports, highlight, post to Notion."
- **Done well / get better: specific and evidence-based.** Not "good discipline today" but "ran the full triaging checklist on FLTR without shortcuts."
- **No hedging, no filler.** Direct CoS voice throughout.

---

## Scheduled Task Integration

This skill should be registered as part of:
- **watson-morning-questions** (07:00 UK daily): Morning briefing is the first thing delivered, incorporating the HPC morning questions.
- **session-handoff-auto** (15:00 UK weekdays): EOD review is the handoff. They're the same thing.

If Watson is not in a live session at these times, the scheduled task generates the file and posts to Notion. Richard sees it when he next opens Notion or starts a session.
