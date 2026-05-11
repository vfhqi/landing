# SA SOP — TOTAL SYSTEM MAP

<!-- [W] Created 21-Apr-26 by Systems Architect. Living doc. Review fortnightly with Richard. -->

## Purpose

The TOTAL SYSTEM MAP is a visual taxonomy of everything that has been structurally "recorded" in Richard's investing operating system (COWORK + .claude + external surface). It is a navigation aid, not an audit: it helps Richard see what exists, what labels are in play, and how concepts link — so he can direct Watson optimally and avoid the "why didn't you load that" problem.

**Higher intent:** Improve SA execution and the Richard↔Watson collaboration interface.

**Cadence:** Fortnightly review with Richard. SA owns build and refresh. CoS owns calendar enforcement of the fortnightly review and flags drift between reviews.

---

## Why the map exists (the problem it solves)

Richard has reported two recurring friction points:
1. He is sometimes unclear what has been structurally recorded by Watson (i.e. is this in a SKILL.md, a context file, auto-memory, or nowhere?).
2. Watson sometimes fails to load things that should be loaded by default. A shared map of the taxonomy helps both sides converge on what should load when.

The map is the reference document that closes this loop.

---

## Design rules (baked in from 21-Apr-26 briefing)

- **Primary lens = DOMAIN, not role.** Richard's instruction was explicit: "show how YOU see it, as the goal is for me to understand YOUR understanding of the system." Watson carries the system mentally as 7-8 domains. Role tags ride on leaves as overlays. Do not flip to role-first without re-confirming with Richard.
- **Depth = 4 levels.** Including sections within SKILL.md files and individual templates within researcher/.
- **Output = single collapsible HTML tree (colour-coded, filterable) + .md source of record.** HTML is the navigation surface; .md is the durable text version for diffs and future SA review.
- **Stale/orphan files: include but grey-tag as [STALE] / [ORPHAN].** The map has cleanup-signal value beyond pure taxonomy. Do not exclude silently.
- **Scope = COWORK filesystem + .claude/CLAUDE.md + auto-memory + scheduled protocols + external surface (Notion, AS, FactSet, GH Pages, Netlify, Outlook, Gmail, Claude in Chrome).**
- **Location:** `memory/maps/total-system-map.html` and `memory/maps/total-system-map.md`. New folder. Room to grow (data-flow map, role-map, etc.).
- **Colour palette:** Richard's standard — Purple = judgements / key questions, Blue = observations / context, Green = actions / follow-ups. STALE/ORPHAN = grey.

---

## The 7 domains (Watson's mental model)

1. **KERNEL** — what loads every session (`.claude/CLAUDE.md`, auto-memory `MEMORY.md`, corrections.md, latest handoff)
2. **CONTEXT** — who Richard is and how he invests (`memory/context/*.md`)
3. **SKILLS & ROLES** — how Watson does the work. Three sub-branches:
   - 3a. Role skills (SA, APM, RES, EA, HPC, IA, CoS)
   - 3b. Workflow skills (IG, session-handoff, notion-posting, MM 8-point, auto-ig, etc.)
   - 3c. Skill canon (CLAUDE.md-level skills: consolidate-memory, setup-cowork, skill-creator, schedule, cycler)
4. **RESEARCH MACHINE** — production line: AI Prompts, Files/, research-output, prompt templates
5. **DATABASES & DASHBOARDS** — the cockpit: IC Ratings, RS-Breadth/Minervini, Pullback Monitor, Position Manager, memos, scripts
6. **COACHING** — the performance layer: podcast-library, coaching-log, bright-spots, HPC references
7. **PROTOCOLS & PIPELINE** — what runs and what's in-flight:
   - 7a. Scheduled protocols (5 jobs + daily-podcast)
   - 7b. Pipeline (stock-level, per `pipeline.md`)
   - 7c. Projects (meta-level)
   - 7d. Active thematics
8. **EXTERNAL SURFACE** — Notion DBs, AlphaSense, FactSet, Excel, Outlook, Gmail, GH Pages, Netlify, Claude in Chrome

The 7 domains could arguably compress to 6 (merge 6 into 3b) or expand to 8 (split 7a out as its own "time-based executors" domain). Defer to Richard during review.

---

## Fortnightly review cadence

Review is owned by SA, enforcement is owned by CoS.

At each review:
1. Diff the map against live filesystem — any new SKILL.md, context file, or dashboard gets added.
2. Re-assess STALE/ORPHAN tags — has anything been cleaned up, or should new items be greyed?
3. Check role-tag accuracy — have role responsibilities shifted?
4. Check external surface — any new MCP connector, new Notion DB, new dashboard host?
5. 15-minute walk-through with Richard. Purpose: does the map still match how he wants to navigate? Any domain feeling wrong, crowded, or missing?
6. Update this SOP if design rules have changed.
7. Log the review in CoS delivery scorecard.

**Next review due:** ~05-May-26 (two weeks from build date). CoS to add to calendar enforcement.

---

## Build workflow

1. Re-walk COWORK (light touch) and .claude/.
2. Update the `.md` source of record first — it is the durable artefact.
3. Regenerate HTML from the .md (or edit HTML directly if structural change is small).
4. Verify: open HTML, spot-check 10 random leaf nodes against filesystem, check all collapse/filter behaviour.
5. Commit handoff note describing what changed since last review.

---

## Anti-patterns to avoid

- Do not duplicate content under every role a skill serves — use role tags on leaves instead.
- Do not silently exclude stale files — grey them out. The cleanup signal is part of the value.
- Do not go deeper than 4 levels in the visual — it becomes an audit, not a map. Link to source files for depth.
- Do not reorder the 7 domains without discussion — the order reflects load-priority (kernel first, external surface last).
- Do not build this map without also updating CLAUDE.md Key Files table to reference it.

---

## Open questions for Richard (to resolve at first review)

1. Are scheduled protocols better as their own top-level domain (current: nested under 7a)?
2. Coaching as a domain (6) vs HPC skill (3a) — the current split has "library/output" under 6 and "how-to" under 3a. Does this feel right or should they collapse?
3. Should the map include a parallel "load-order" view (what Watson should load first for each role) as a secondary visualisation?

---

## Files this SOP governs

- `memory/maps/total-system-map.html` (the deliverable)
- `memory/maps/total-system-map.md` (the source of record)
- `memory/skills/systems-architect/total-system-map-SOP.md` (this file)
- `memory/projects/total-system-map.md` (project tracking, CoS-owned)
