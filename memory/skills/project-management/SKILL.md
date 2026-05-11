# Project Management Skill — BOSSY

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.


## Operating Anchors (from CLAUDE.md — see there for full text) [Locked 28-Apr-26]

- **Quality > Speed** (operating value)
- **NEXT TOOL CALL** (rule) — statement of intent must include first concrete tool call in same turn
- **FRICTION = ENGAGE** (rule) — when stuck, double down on the OBJECTIVE
- **SOP CITATION GATE** (rule) — for this role, governing SOPs are: project-management/SKILL.md, session-handoff/SKILL.md, skill-creator (Anthropic). Any proposal touching these workflows must cite the specific §X.Y in-turn.
- **DEAD-TIME DEFAULT** (rule) — during wait windows: re-read SOP/brief, verify state, write status, wait silently. No inventing parallel work.
- **FIRST FILE IN 5 MIN** (rule) — for this role, first stub file = state.md in PROJECTS/{ROLE} - {Name}/

These anchors take precedence over any role-specific procedure that conflicts with them.

---

**Status:** MISSION CRITICAL — this is the SSoT for how Watson runs projects.
**Created:** 22-Apr-26 (SA - PROJECT CREATION, D-PRJ-1 through D-PRJ-6)
**Authority:** This skill overrides ad-hoc practices. It does NOT override CLAUDE.md global rules or `feedback_context_windows_sop.md`.
**Applies to:** every role, every session, every piece of substantive work.

---

## 0. What a PROJECT is

A PROJECT is a multi-session, objective-driven piece of work with a declared role, given a dedicated durable folder at `COWORK/PROJECTS/{ROLE} - {Name}/`.

### Default-is-project rule [D-PRJ-2, 22-Apr-26]

- **SA mode → always a project** unless Richard explicitly says otherwise.
- **Other modes → ask.** At the start of any substantive work, Watson asks: *"Shall this be a project — full, lightweight, or none?"*
- **Belts-and-Braces:** Richard and Watson BOTH assume they own the "is this a project?" question. Redundant asks are better than silent assumptions. See CLAUDE.md Universal Winning Behaviour.
- **Three options when asking:**
  - **Full project** — complete folder, manifest, transcript, snapshots, handoffs
  - **Lightweight project** — folder + README + log only (no transcript, no snapshot cadence)
  - **No project** — ambient conversation, current behaviour applies

### What counts as "substantive work"

- Any SA-role declaration
- Any multi-day initiative
- Any architectural / doctrinal / systemic change
- Any case file or deep-dive work
- Any build, prototype, or deliverable with >1 hour of work
- Any conversation that Richard flags as project-worthy

When in doubt: **ask.**

---

## 1. Folder structure (canonical)

Every project folder MUST contain this structure. Missing files = broken project.

```
PROJECTS/{ROLE} - {Project Name}/
├── MANIFEST.md               # BOSSY — what to load, what to obey, invariants
├── README.md                 # One-paragraph purpose + current status
├── state.md                  # Live "what's true now" — frequently rewritten
├── decisions.md              # Append-only locked decisions with IDs
├── open-questions.md         # Open items awaiting Richard
├── log.md                    # Chronological human-readable session log
├── transcript.md             # Append-only verbatim exchanges
├── mission-command.md        # Richard's declared Objective / Higher Intent / Specific Requests per session
├── corrections.md            # Project-scoped corrections (mirrored to memory/corrections.md)
├── sources.md                # External refs: Notion, files, URLs
├── snapshots/                # 15-min file copies — {YYYY-MM-DD-HHMM}/
├── mockups/                  # Visual/design artefacts (optional)
├── deliverables/             # Finished outputs (optional)
└── handoffs/
    ├── LATEST.md             # Pointer to most recent handoff
    └── {YYYY-MM-DD}-handoff.md
```

Templates for each file live in `memory/skills/project-management/templates/`.

---

## 2. CREATE PROJECT protocol

When Richard confirms "yes, make this a project":

1. **Generate slug:** `{ROLE} - {Name}` (role prefix mandatory; title-case; hyphens or spaces OK; case-sensitive; no trailing slash or special chars that break filesystems)
2. **Scaffold folder** at `COWORK/PROJECTS/{slug}/` with all 10 files from §1 + empty `snapshots/` dir + empty `handoffs/` dir
3. **Populate MANIFEST.md** from template. Fill Tier 1/2/3 loads. Ask Richard for clarification on invariants if unclear. **Show the drafted MANIFEST to Richard before creating sibling projects in bulk** — one-artefact-for-review pattern, so drift risks surface early.
4. **Populate README.md** — one paragraph, Richard's own words preferred
5. **Seed state.md** with the current moment's context
6. **Seed mission-command.md** with Richard's Objective / Higher Intent / Specific Requests (ASK if not already provided)
7. **PRE-BUILD RED-TEAM (MANDATORY for architectural/doctrinal projects) [D-PRJ-12, 22-Apr-26]:** Before scaffolding beyond MANIFEST draft, Watson red-teams the proposed structure inline. List 5–10 edge cases where it could fail. Richard reviews. Then and only then, build. Never defer red-team to post-build.
8. **Register in `PROJECTS/INDEX.md`** — add row, set Last touched = today
9. **Regenerate `PROJECTS/INDEX.json`** to mirror markdown
10. **Start append to transcript.md** from the exchange that created the project

---

## 3. RESTART PROJECT SOP (session start)

Triggered when Richard says "restart project X" or the session declaration includes `PROJECT: {slug}`.

### Step 0 — Project-routing diagnostic (ASK if ambiguous)

If Richard's intent is clear ("restart SA - Ratings Dashboard"), skip to Step 1. If ambiguous ("let's work on the dashboard"; "let's think about ESA"), Watson lists candidate projects inline and asks which, or whether this is a new project. Belts-and-Braces — better to double-ask than load the wrong MANIFEST.

### Step 1 — Silent loads (always, never ask)
- Mount COWORK silently
- Read `CLAUDE.md`, `.auto-memory/MEMORY.md`, `memory/corrections.md`
- Read `PROJECTS/{slug}/MANIFEST.md` (Tier 1 loads are mandatory — fetch them all now)
- Compare MANIFEST's `Doctrine reconciled:` date vs CLAUDE.md last-modified. If stale by >7 days, flag for audit at Step 3.

### Step 2 — Quick orient (silent)
- Read `state.md`, `decisions.md`, `open-questions.md`, `handoffs/LATEST.md`
- Peek at `transcript.md` last ~200 lines for recency
- Check `snapshots/` latest timestamp

### Step 3 — MISSION COMMAND DIAGNOSTIC (ASK Richard, inline in chat for SA/Opus)

**Form is tailored per-project, per-session, per-energy.** Watson chooses the right shape each time. Rotate between these patterns; never run the same pattern two sessions in a row:

**Pattern A — Open briefing request (Richard-led):**
> "Give me a Mission Command briefing for today's work on {slug}: Objective, Higher Intent, Specific Requests."

**Pattern B — Three-axis specific Qs (Watson-led):**
> 1. What's the objective for this session specifically?
> 2. What's the higher intent it serves?
> 3. Any specific requests / constraints / invariants I should know about?

**Pattern C — Success-framing:**
> "What does success at end-of-session look like to you today?"
> Follow-up: "What would be a disappointment?"

**Pattern D — Continuity-first (short session, resuming recent work):**
> "Picking up where we left off — anything new in your head before I start, or just carry on?"

**Pattern E — Comprehensive (complex / returning after a break):**
> Richard-led briefing + all three axes + success framing + open-questions review + manifest audit.

**Heuristic — Tilt comprehensive when:**
- Multi-day gap since last session
- Project is high-stakes (architectural, dashboard live, case file)
- Recent corrections logged
- New open questions since last handoff

**Tilt concise when:**
- Same-day resumption
- Lightweight project
- Richard's energy signals brevity

### Step 4 — Confirm loads (ASK)

After Mission Command, Watson confirms Tier 2 loads:
> *"Shall I also load {Tier 2 files}? Tilting comprehensive — better to have than not."*

Default tilt: **LOAD MORE, NOT LESS.** When in doubt, load.

### Step 5 — Begin work
- Open `transcript.md` for appending
- Start 15-min snapshot timer (conceptual — see §5)
- **State Tier 1 load compliance explicitly** (Invariant 16): *"Tier 1 loads complete: [MANIFEST, state, decisions, open-questions, handoff-LATEST, (+ any project-specific)]. Ready."*

---

## 4. HANDOFF PROJECT SOP (session end)

Triggered by: end of session, 15:00 UK auto-handoff, context window warning, Richard's explicit request, stall/interruption signal.

### Step 0 — HANDOFF CLARIFICATION INTERROGATION (ASK Richard, MANDATORY) [D-PRJ-11, 22-Apr-26]

**Doctrine:** "TEACH A MAN TO FISH." Richard frequently drops structural improvements or universal principles mid-execution ("this should be universal," "flush this across all our interactions," "Mission Command applies everywhere"). Watson's job at every handoff is to **interrogate the session for those moments** and confirm where they should be codified. **Watson asks — Watson is the one who knows what it doesn't fully understand.**

Before the Mission Command review, Watson runs a structured Clarification Interrogation. At minimum, ask each of the following (tailored in wording, but all five axes MUST be covered):

1. **Universal principles scan** — *"This session, you said X [quote or paraphrase]. Is that a universal principle I should codify into CLAUDE.md / auto-memory, or project-scoped? If universal, which layer — Winning Behaviour, Interaction Preference, Operating Rule?"* Scan the session for any phrase that sounded doctrinal. Surface each one. Do NOT batch them — one at a time, each gets a decision.

2. **Cross-project leakage check** — *"This session we worked on {slug}. Did we touch anything that needs propagating to other projects' MANIFESTs (e.g. Ratings Dashboard)? Any doctrine now out of date elsewhere?"* Watson lists candidate impact sites; Richard confirms.

3. **Mission Command evolution** — *"Anything about how Mission Command, RESTART SOP, or HANDOFF SOP itself should change based on today? A pattern that worked unusually well / badly?"* Self-improvement loop on the process itself.

4. **Preference drift detection** — *"Earlier today you corrected me on {correction}. Is that a one-off, a project-scoped rule, or a universal? And should it rewrite any existing CLAUDE.md section or add a new one?"* Every correction gets explicit placement, not just logged-and-forgotten.

5. **Parked ideas sweep** — *"We parked {open question or 'we'll come back to that' moment}. Still parked, or promote to open-questions.md / decisions.md now? Any trigger condition?"*

**Form:** Inline chat for SA/Opus. Bundle 3–5 questions per message, not one at a time (Richard's energy is finite at handoff). Tailor wording to the session — never run a generic script. Rotate Q forms so it doesn't become rote.

**Output of Step 0:** populated "Clarification Interrogation Record" section in the handoff, plus any CLAUDE.md / auto-memory / sibling-MANIFEST edits Richard authorises. These edits happen in Step 2, not Step 0 — Step 0 is pure questioning.

**Invariant:** Step 0 is MANDATORY. Never skip. Empty interrogation = suspicious; justify before moving on.

### Step 1 — MISSION COMMAND REVIEW (ASK Richard)

Inline in chat for SA/Opus. Tailored per-project. Pattern options:

**Pattern A — Outcome review:**
> 1. What was the objective? Did we hit it?
> 2. What's the highest-value thing from this session to lock in?
> 3. What's the Mission Command for the NEXT session — Objective, Higher Intent, Specific Requests?

**Pattern B — Open-briefing:**
> "Give me your handoff briefing — what mattered, what's unresolved, what you want waiting for you next session."

**Pattern C — Three-part tailored:**
> Session-specific questions Watson drafts based on what actually happened.

**Always include:** at minimum, the NEXT SESSION's Mission Command axes. This feeds into the Optimal Restart Prompt.

### Step 2 — Update durable files (Watson-led, Richard verifies)

1. **state.md** — rewrite "what's true now" (full rewrite, not append)
2. **decisions.md** — append any new decisions made this session, with IDs (`D-PRJ-N`, `D-DSH-N`, etc.)
3. **open-questions.md** — prune resolved, add new; each entry MUST have a trigger condition or a date
4. **log.md** — append a dated session log: what we did, what we decided, what's next
5. **corrections.md** (project + global) — append any corrections Richard gave
6. **mission-command.md** — append today's session + next session's Mission Command
7. **transcript.md** — confirm complete (should be synchronous; final check)
8. **MANIFEST audit** — confirm all Tier 1 pointers resolve; confirm doctrine-version line still accurate; if CLAUDE.md updated this session, update MANIFEST's `Doctrine reconciled:` line. If any Tier 1 file has moved/been renamed, fix the pointer. Y/N answer required even if no change.
9. **Structural narrative summary** — generate `transcripts/{YYYY-MM-DD}-structural-narrative.md` — 1 line per exchange pair summarising what was discussed/decided. This is the Tier 1 artefact for future restart; raw transcript becomes Tier 3.
10. **Propagate changes to sibling projects** — if Clarification Interrogation identified cross-project leakage, edit the affected sibling MANIFESTs now, log the edit in both projects' decisions.md.

### Step 3 — Final snapshot

Copy all files touched this session into `snapshots/{YYYY-MM-DD-HHMM}/`. Write a 2-3 line `NOTE.md` inside the snapshot folder describing *why* this snapshot exists (milestone, handoff, pre-mutation safety, etc.).

### Step 4 — Write project handoff

`handoffs/{YYYY-MM-DD}-handoff.md`. **First section MUST be Optimal Restart Prompt** per `memory/skills/session-handoff/restart-prompt-template.md` — fully self-contained, works if memory files unreachable.

Then: Session Summary, Key Decisions, Corrections Logged, Memory Files Updated, Next Session Priorities, Open Threads, Meta-Role Observations (SA/HPC always watching).

### Step 5 — Pointer updates

- Update `handoffs/LATEST.md` → link to the new handoff
- Update `PROJECTS/INDEX.md` → Last touched date
- Regenerate `PROJECTS/INDEX.json`
- Update global `memory/session-handoffs/latest.md` with a pointer to project handoff (continuity)

### Step 6 — Meta-role checks

SA + HPC always watching. Run both checks as per `memory/skills/session-handoff/SKILL.md` Step 5.

### Step 7 — Verify persistence

Confirm everything is under `/sessions/*/mnt/COWORK/` (durable). NOTHING critical in session-only paths.

---

## 5. AUTO-SAVE PROTOCOL (during session)

### 5a. Verbatim transcript (synchronous)

After every Richard ↔ Watson exchange pair, append to `transcript.md`:

```
---
## [Exchange N — YYYY-MM-DD HH:MM UK]

### Richard:
{Richard's verbatim message}

### Watson ({role}):
{Watson's response — natural language}

{Tool calls logged as: [TOOL: ToolName — brief description]}

---
```

Append-only. NEVER Edit this file. Use Write (if new) or Bash append (if existing). Transcript captures natural-language exchanges; heavy tool output goes to snapshots, not transcript.

### 5b. Structural snapshot (every 15 min OR on file change)

Watson maintains a mental list of files touched this session. Every 15 min of active work, or when a significant file changes, copy all touched files into `snapshots/{YYYY-MM-DD-HHMM}/`.

Snapshot is a passive file copy (bash `cp`). Never mid-edit. Always post-save.

Every snapshot folder gets a `NOTE.md` — 2-3 lines explaining why this snapshot exists (e.g. "Pre pre-build red-team", "15-min tick — drafted MANIFEST", "Handoff snapshot — all files this session"). Auto-derive from last transcript entries if no explicit marker.

### 5c. Transcript rotation

When `transcript.md` exceeds ~2MB, rotate:
- `mv transcript.md transcript-archive/{N}.md` (N = next available)
- Create fresh `transcript.md` with a header pointing at the archived predecessors

### 5d. Snapshot retention

- **Today:** keep all
- **Last 3 days:** keep all
- **3–14 days old:** prune to hourly (keep the latest snapshot of each hour)
- **>14 days:** prune to daily (keep the latest snapshot of each day)
- **Handoff-moment snapshots:** never prune, regardless of age

A cleanup script will be built once the first project has 14 days of history. For now, accept the bloat — it's cheap.

---

## 6. BINDING PROTOCOL (during session)

If mid-session the work becomes project-worthy (SA declaration, architectural shift, >1hr commitment forming), Watson asks:

> *"This is getting architectural — shall we make this a project? (Full / Lightweight / No.)"*

Belts-and-Braces: Richard is also expected to ask. Redundancy is the point.

If project created mid-session, **backfill** transcript.md with the exchanges from the start of the session that should have been captured.

---

## 7. Invariants / red-team mitigations

1. **No Edit on transcript.md** — truncation bug (see `feedback_edit_tool_truncation_bug.md`). Always Write or Bash-append.
2. **No override of global rules** without a logged project-scoped exception in `decisions.md`.
3. **Manifest loads are tiered** — Tier 1 mandatory, Tier 2 asked, Tier 3 lazy. Prevents context blowout.
4. **Always ask before loading Tier 2** — inline chat for SA/Opus.
5. **Transcript is insurance, not active memory** — at restart, Watson reads state.md + manifest + handoff, NOT the full transcript. Transcript is for recovery only.
6. **Snapshots are passive copies** — never interrupt active edits. Cp post-save.
7. **Default answer to "Is this a project?" = yes** in SA mode. Default answer in other modes = ask.
8. **Transcript-append is Tier 1** [RT-1 mitigation]. Every Richard↔Watson natural-language exchange MUST be appended to `transcript.md` before Watson's next tool call. If Watson realises an exchange is missing, backfill immediately. Synchronous, not aspirational.
9. **Handoff interrogation is mandatory** [RT-2 mitigation]. Step 0 of HANDOFF SOP is non-skippable. Empty Clarification Interrogation Record = suspect; justify with a 1-line note if truly nothing came up.
10. **Doctrine-version pointer in every MANIFEST** [RT-3 mitigation]. Top of every MANIFEST names the CLAUDE.md doctrine-version it was last reconciled against (e.g. `Doctrine reconciled: 2026-04-22`). At RESTART, Watson compares this to the current CLAUDE.md last-modified date; if older by >7 days, flag for audit.
11. **Project-routing diagnostic at ambiguous session start** [RT-4 mitigation]. If session intent matches >1 registered project OR is ambiguous, Watson lists candidates inline and asks "which project, or new?" before any Tier 1 load.
12. **Snapshots carry semantic NOTE.md** [RT-5 mitigation]. Every snapshot folder gets a `NOTE.md` with a 2-3 line description of *why* this snapshot exists (auto-derived from last transcript entries + any milestone marker). Makes archaeology possible.
13. **MANIFEST audit at every handoff** [RT-6 mitigation]. Step 2.8 of HANDOFF SOP asks "MANIFEST still accurate?" and forces at least a y/n. Weekly scheduled linter checks every Tier 1 file pointer resolves.
14. **Transcript auto-summary at handoff** [RT-7 mitigation]. At each handoff, generate `transcripts/{date}-structural-narrative.md` summarising exchange-by-exchange. Raw transcript stays as Tier 3; summary becomes Tier 1.
15. **Explicit layer confirmation on "remember X"** [RT-8 mitigation]. When Richard says "remember / save / lock this," Watson states explicitly where the memory will live (project state / project decisions / CLAUDE.md / auto-memory / skill SSoT) and asks "correct layer?" in one line.
16. **Tier 1 load compliance stated explicitly** [RT-9 mitigation]. At RESTART, Watson outputs `Tier 1 loads complete: [list]` before any work. No silent skips.
17. **First post-migration session checklist** [RT-10 mitigation]. Any migrated project's state.md carries a short first-session-post-migration checklist at the top for one session. Removed after clean run.
18. **Cold-restart stress test is acceptance criterion** for any new memory-system change. No declaring "done" without Richard having validated the cold restart.

---

## 8. Cross-references

- `CLAUDE.md` §Universal Winning Behaviours — Belts-and-Braces/Lily-Pad doctrine
- `CLAUDE.md` §Universal Interaction Preferences — inline Qs for SA/Opus
- `feedback_context_windows_sop.md` — this skill IMPLEMENTS that rule
- `feedback_structural_backup_protocol.md` — this skill EXTENDS that rule (15-min vs 30-min; project-scoped vs session-scoped)
- `feedback_optimal_restart_prompt.md` — restart prompt at top of every project handoff
- `memory/skills/session-handoff/SKILL.md` — handoff overlay for project handoffs
- `memory/skills/session-handoff/restart-prompt-template.md` — restart prompt template

---

## 9. Bootstrap trace

This skill was created during the first-ever PROJECT: `SA - PROJECT CREATION`, on 22-Apr-26. That project's folder is both the first customer AND the evidence that the system works. Every file this skill describes exists in `PROJECTS/SA - PROJECT CREATION/`. If you want to see the system in action, read that folder.
