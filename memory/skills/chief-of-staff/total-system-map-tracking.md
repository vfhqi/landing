# CoS Tracking — TOTAL SYSTEM MAP

<!-- [W] Created 21-Apr-26 by CoS-under-SA-umbrella. Enforcement tracker for fortnightly review. -->

## What this tracks

The TOTAL SYSTEM MAP is a living visual taxonomy of Richard's full operating system. SA owns the build. CoS owns the cadence: making sure the fortnightly review actually happens, flagging drift in between, and escalating if the map is allowed to go stale.

SOP: `memory/skills/systems-architect/total-system-map-SOP.md`
Project file: `memory/projects/total-system-map.md`

---

## Cadence commitment

- **Frequency:** Fortnightly (every 14 days)
- **Duration:** ~15 minutes with Richard, plus ~30 min of SA prep before the call
- **Owner (build):** Systems Architect
- **Owner (cadence):** Chief of Staff
- **First review:** Build/kickoff 21-Apr-26 (rough tree agreed in-line; HTML build pending Richard reply)
- **Next review target:** ~05-May-26
- **Recurring slot:** TBD — suggest Monday morning as part of Weekly Priorities Board (CoS cadence block)

---

## CoS enforcement actions

### Between reviews
- If any new SKILL.md is created by SA, CoS flags: "does the system map need updating?"
- If a new scheduled protocol is added, CoS flags for map update
- If a new Notion DB or external connector is added, CoS flags for external-surface branch update
- If Richard mentions he was surprised something was/wasn't recorded, CoS logs it as a map-refresh trigger

### At review
- Confirm the review happened (log to delivery scorecard)
- Capture any structural decisions made (new domain, renamed branch, tag updates)
- Ensure SA updates the SOP if design rules changed
- Update this tracker's "Last review" field

### If review is missed
- Day +1: gentle prompt to Richard and SA
- Day +3: escalate — "The map has drifted {N} days past review cadence. Propose {date}."
- Day +7: log as a delivery-scorecard miss

---

## Status log

| Date | Event | Outcome |
|------|-------|---------|
| 21-Apr-26 | Project kickoff (SA session, Opus, DEVELOPMENT mode) | Back-brief done. 7 domains agreed. Rough tree sketched inline. HTML build pending Richard's reply. |
| TBD | HTML + .md delivered | Pending |
| ~05-May-26 | First fortnightly review | Scheduled |

---

## Why this matters (so CoS doesn't let it drift)

Richard's two stated pain points (21-Apr-26 briefing):
1. Confusion about what has been "recorded" structurally.
2. Watson not loading things by default that should be loaded.

The map is the mechanism that closes both loops. If the map goes stale, both problems return. CoS's job is to make that not happen.
