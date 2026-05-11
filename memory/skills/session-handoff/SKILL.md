# Session Handoff Skill — V2

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] V2 rewrite 23-Apr-26. Purpose: close the workstream, capture everything, save where it belongs. -->
<!-- Supersedes V1 (reconstructed 27-Mar-26). Change log: removed 4b/4c/4d production tasks, added Step 0 project routing, removed "Next Session Priorities", SA role skips meta-role questions, latest.md becomes thin pointer. -->

## Purpose

Close this workstream. Capture everything — decisions, corrections, discussions, file changes. Save it where it belongs so any future session can find it. **This is an archival act, not a planning act.**

---

## When to Execute

- End of every working session (manual trigger or scheduled)
- Before any PC restart or shutdown
- When context window is running low

---

## Protocol

### Step 0: Identify Save Location

**Before writing anything**, determine where the handoff note and corrections belong.

**Check:** Does this workstream belong to a project in `COWORK/PROJECTS/`?

| Condition | Handoff note location | Corrections location | Transcript location |
|---|---|---|---|
| **Project exists** in `COWORK/PROJECTS/{Project Name}/` | `PROJECTS/{Project Name}/handoffs/handoff-YYYY-MM-DD-HHMM.md` | `PROJECTS/{Project Name}/corrections.md` | Append to `PROJECTS/{Project Name}/transcript.md` |
| **No project** (standalone/ad-hoc session) | `memory/session-handoffs/handoff-YYYY-MM-DD-HHMM.md` | `memory/corrections.md` | `memory/conversations/YYYY-MM-DD.md` |

In **both** cases, update `memory/session-handoffs/latest.md` as a thin pointer:

```
# Latest Handoff — DD Mon YYYY HH:MM

- **Workstream:** {project name or 'standalone'}
- **Role:** {primary role}
- **Handoff note:** {full path to handoff file}
- **Project folder:** {full path to project folder, or 'N/A'}
```

This ensures there is always a single "what happened last" breadcrumb at a predictable location, but the substance lives in the right place.

**Naming convention [D] (12-Apr-26):** All projects and tasks use `ROLE - Description In 3-6 Words`. Role acronyms: RES, EA, FA, APM, HPC, SA. Multi-role: list all.

### Step 1: Session Review

Summarise the session:
- **Decisions made** — what was agreed, changed, or established
- **Corrections given** — any mistakes Watson made that Richard corrected (high-signal)
- **Pipeline changes** — any stocks progressed, parked, or newly flagged
- **Work completed** — what was delivered or shipped
- **Work incomplete** — anything started but not finished (state it left in)

### Step 2: Log Corrections

Append any corrections to the appropriate corrections file (determined in Step 0). Format:
```
### YYYY-MM-DD — [Category]
**Correction:** What was wrong
**Correct approach:** What should happen instead
**Impact:** How this changes Watson's future behaviour
```

### Step 3: Update Memory Files

Review all memory files for staleness or new information:
- Update CLAUDE.md pipeline table if any stocks moved stages
- Update context files if new information about Richard's system/approach emerged
- Update skill files if any SOPs were refined
- If project exists: update `PROJECTS/{Project Name}/state.md` with current state
- If project exists: update `PROJECTS/{Project Name}/decisions.md` with any new locked decisions
- Never overwrite — create new versions or append

### Step 4: Write Handoff Note

**[D] (22-Apr-26)** Every handoff note MUST begin with an **Optimal Restart Prompt** in a fenced ```text block at the top of the file (immediately after the H1 title, before the first H2). Authoring rules and the universal template live in `memory/skills/session-handoff/restart-prompt-template.md` — that file is the SSoT.

The restart prompt must be **fully self-contained** (Richard's 22-Apr-26 choice): it works as a standalone briefing even if memory files are unreachable. Populate every slot with real content — no placeholders. Run the quality gate at the bottom of `restart-prompt-template.md` before considering the handoff complete.

**Handoff note template:**

```markdown
# Session Handoff — DD Mon YYYY HH:MM
## {Project Name or 'Standalone'} | {ROLE} | {DEVELOPMENT|EXECUTION}

## Optimal Restart Prompt — copy-paste into next session
```text
{{full restart prompt per restart-prompt-template.md}}
```

## Session Summary
[2-3 sentence overview of what happened]

## Key Decisions
[Bullet list of what was agreed, changed, established]

## Corrections Logged
[Count and brief description, or "None"]

## Memory Files Updated
[List of files changed and what changed]

## Open Threads
[Anything unresolved or incomplete — state what's dangling, not what to do about it]

## Quality Audit
- **What was delivered:** [files/pages/outputs produced]
- **Governing SOP:** [which SOP governed quality]
- **First-attempt pass rate:** [yes/no]
- **Rework details:** [what failed, what was fixed — or "None"]
- **Correction logged?** [yes/no/N/A]

## Meta-Role Observations
[SA/HPC integration notes or Q&A — see Step 5]
```

### Step 5: Meta-Role Checks

**Conditional on the session's primary role:**

**If primary role was SA:**
Watson does NOT ask meta-role questions. Richard is the architect in SA sessions — Watson doesn't coach the architect on architecture. Instead, Watson silently:
1. Identifies all structural changes made during the session
2. Confirms they have been integrated across ALL relevant files (CLAUDE.md, working-preferences.md, relevant SKILL.md files, auto-memory)
3. Logs the integration checklist in the handoff note under "Meta-Role Observations"

**If primary role was anything else (RES, APM, EA, FA, HPC, CoS):**
Run both meta-role checks:

**Systems Architect Check — ask Richard 1-2 of these:**
- Did anything in this session reveal a gap in Watson's skills, memory, or SOPs?
- Should any new skill be created, or existing skill refined?
- Did a correction occur that implies a structural change to how Watson operates?
- Are there patterns across recent sessions that suggest a system improvement?

**High Performance Coach Check — ask Richard 1-2 of these:**
- Did anything in this session reveal a behavioural pattern worth noting?
- Was process execution consistent with stated standards?
- Are there coaching observations to log for the weekly review?
- Any decisions made under stress, fatigue, or time pressure worth reflecting on?

Integrate Richard's answers into the relevant memory/skill files immediately. Log in handoff note under "Meta-Role Observations."

### Step 5.5: Hot Wash + Wisdom Library Proposal (NEW v2.3 — 03-May-26; Step 5.5.0 added 04-May-26 v2.4-cohort)

**Purpose.** Close the Wisdom Library bookend opened at the start of work (RESEARCHER SKILL-V2.13 Rule #37 = pre-query consult; AJ SOP v2.4 §Phase 0.2 = APM pre-analysis consult). At session end, surface what the session TAUGHT the library — without this step, the library only grows when Richard prompts.

**Step 5.5.0 — Cohort presence check (NEW 04-May-26, lock-step with cohort SKILL §5)**

Before running the per-session hot wash + WL survey, check whether this session worked on any tickers belonging to an active cohort:

1. **Scan `memory/staging/cohort-*-*.md`** for active manifests touched this session.
2. **For each active cohort touched:**
   - Determine whether the LAST per-stock memo in any sub-cohort was authored this session
   - If YES, **AJ SOP v2.4.1 §Phase 4.6 (Cohort hot wash) MUST have been run** before this Step 5.5 fires
   - If Phase 4.6 was run, link to the cohort hot wash artefact (`databases/memos/_cohort/{cohort-name}/hot wash.md`) in the handoff note
   - If Phase 4.6 was NOT run when it should have been, **STOP** — author Phase 4.6 now (cohort hot wash + Cohort GNG CHECKS + WL outcomes) before continuing Step 5.5
3. **For each cohort that is still IN-FLIGHT** (sub-cohort not yet completed in this session), note in the handoff: cohort name, member tickers, sub-cohort completion status, expected hot wash trigger date.

**Why Step 5.5.0 not Step 5.5 §1:** the cohort layer operates ABOVE the session layer. A cohort's hot wash may need to fire before the session can close, and that hot wash itself produces WL candidates that should appear in the session's WL survey. Step 5.5.0 routes the cohort artefacts into the session record before per-session content is finalised.

**Why Step 5.5.0 not at session start:** session start has no notion of "session work" yet — the cohort presence check needs the session's work to be complete to determine if any sub-cohort closed during this session. The cohort hot wash trigger is "last memo in sub-cohort ships," which is a session-end determination.

**De-duplication rule:** if Phase 4.6 already ran during this session and produced WL outcomes, those outcomes are listed in the handoff note WITHOUT re-surveying the same content at Step 5.5 §2. Step 5.5 §2 surveys ONLY content NOT already covered by Phase 4.6 (typically: cross-cohort patterns, process / SA insights, Watson-behavioural patterns).

**Quality gate G17 enforcement:** if a cohort's hot wash is overdue (LAST memo shipped in this session but Phase 4.6 not run), Step 5.5 BLOCKS until Phase 4.6 is complete. Recovery: author Phase 4.6 inline, then resume Step 5.5.

**Cross-ref:** `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0 §5 (cohort hot wash SOP); `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.4 §Phase 4.6 + G17 (the gate Step 5.5.0 enforces); `memory/skills/researcher/SKILL-V2.md` V2.13 Rule #38 (cohort manifest pre-consult — front-end of cohort layer).

**1. Hot Wash — 3-question structure**

Run these three questions on the session as a whole:

- **What happened?** (factual — what was authored, what tools used, what calls made; no analysis)
- **What worked / what didn't?** (honest, blameless — what fired correctly per SOP; where friction surfaced; where Watson made errors and how recovered)
- **What do we change next time?** (actionable, owner-tagged — SOP refinement candidates; tooling improvements; process bindings; UWB candidates)

Capture in handoff note under a new sub-section "Hot Wash" (between Quality Audit and Meta-Role Observations).

**2. Wisdom Library Survey**

Based on the session, identify candidate insights for the library. Categorise per `wisdom-library/SKILL.md` §1:

- **Sector / industry insights** → `situational/industries/`
- **Business-model insights** → `situational/business-models/`
- **Investment-case insights** → `situational/portfolio-construction/` or `situational/position-management/{entry,exit,management}/`
- **Setup pattern insights** → `situational/simple-patterns/`
- **Process / decision-making insights** → `general/decision-making/`

For each candidate: name + one-sentence definition + source case from this session + cross-references.

**3. Tier each candidate** per Wisdom Library SKILL §1:

- **Bronze** — one observation, "watch for promotion"
- **Silver** — multiple confirmations, structurally established
- **Gold** — universally applicable, multiple cases, deep cross-reference network

**4. Author + file (if Richard agrees)**

For each candidate Richard agrees to file:

1. Pre-write JSON validation: `python3 -c "import json; json.load(open('wisdom-library/INDEX.json'))"`
2. Write `.md` per Wisdom Library SKILL §2 format (frontmatter + Definition + Why It Matters + Application + Examples + Cross-References + Change Log)
3. Heredoc + atomic mv + byte-verify per `feedback_silent_file_truncation.md` SOP
4. Update INDEX.json with new entry (single transaction; backup INDEX.json first)
5. Cite the new entry in the handoff note's Memory Files Updated section

**5. Capture deferred candidates**

If a candidate surfaces but is deferred (Richard hasn't approved, evidence is too thin, cross-check needed):

- Append to `wisdom-library/_meta/candidate-queue.md` (append-only)
- Format: name, source-session, tier proposed, evidence (1-3 sentences), why deferred, sourcing path to file (e.g., "1 more case observed")

**6. Cross-role implementations**

This Step 5.5 is the cross-role parent of role-specific bookend implementations:

- **APM:** runs WL survey at AJ SOP v2.3 §Phase 4.5 (after every memo authored, regardless of session boundary)
- **RESEARCHER:** runs WL pre-query consult at SKILL-V2.11 Rule #37 (front-end of bookend)
- **HPC / EA / FA / SA / COS:** runs WL survey at this Step 5.5 (session-handoff time)

The bookend pattern: every analytical engagement OPENS with "what does the library know about cases like this?" and CLOSES with "what did this case teach us that the library doesn't yet know?"

**7. Cite in handoff note**

The handoff note "Memory Files Updated" section MUST list any new Wisdom Library entries OR explicitly say "no new entries this session — N candidates filed to wisdom-library/_meta/candidate-queue.md" OR "no candidates this session."

**Quality gate:** session-handoff SKILL execution is INCOMPLETE without Step 5.5 documented. The handoff note's Hot Wash + WL outcomes are required artefacts.

**Why Step 5.5 not after Step 6:** the Wisdom Library entries should be REFERENCED in the handoff note (Step 6 finalises the note). Putting WL filing after Step 6 would orphan the entries from the handoff record. Step 5.5 between Meta-Role Checks (Step 5) and Save+Verify (Step 6) ensures the bookend artefacts are captured before the handoff archives the session.

**Cross-ref:**
- `wisdom-library/SKILL.md` (consultation conventions + entry format)
- `wisdom-library/_meta/candidate-queue.md` (deferred-candidate staging)
- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.3 §Phase 4.5 (APM-specific implementation)
- `memory/skills/researcher/SKILL-V2.md` v2.11 Rule #37 (RESEARCHER front-end of bookend)
- Wisdom Library entry `memory-needs-workflow-binding` (Bronze, 03-May-26) — the meta-pattern this Step 5.5 implements

### Step 6: Save and Verify

1. **Post conversation log** to Watson Conversations Notion DB (`collection://af72d577-fc57-4e6f-9059-a646f65c3a1c`).
   - Title: `[W] Watson Conversation — DD Mon YYYY`
   - Properties: Date, Session Number, Primary Role, Mode, Key Topics, Stocks Discussed, Session Type
   - Content: Verbatim record, timestamped, role-tagged
2. **Save conversation to disk** — `memory/conversations/YYYY-MM-DD.md` (always) + project transcript (if project exists, per Step 0)
3. **Update `memory/session-handoffs/latest.md`** — thin pointer per Step 0 format
4. **If project exists:** verify project `state.md` reflects current reality
5. **Verify persistence** — confirm ALL files are on the COWORK mount (`/sessions/*/mnt/COWORK/`), NOT session-relative paths. Files outside COWORK are destroyed when the session ends.

---

## File Persistence Rule

**ALL memory files must be written to the COWORK mount.** This is the single most important operational rule for file management.

- COWORK path: `/sessions/*/mnt/COWORK/` → persists on Richard's local disk at `C:\Users\richb\Documents\COWORK`
- Session path: `/sessions/*/` (outside mnt/COWORK) → ephemeral, destroyed on session end
- `.claude/` path: Read-only for skills, writable for CLAUDE.md → persists across sessions but limited

If the COWORK directory is not mounted, use `request_cowork_directory` to mount `C:\Users\richb\Documents\COWORK` before writing any files.

---

## Session START Protocol (Memory Health Check) [D] (27-Mar-26)

At every session start, before any work:

1. **Mount COWORK:** Verify `/sessions/*/mnt/COWORK/` is accessible. If not, mount via `request_cowork_directory` with path `C:\Users\richb\Documents\COWORK`.
2. **Read key files:** corrections.md, session-handoffs/latest.md, CLAUDE.md. These provide continuity.
3. **Read role-relevant files:** Based on declared primary role, read the preparation files listed in that role's charter.
4. **Flag staleness:** If any "Live" file from CLAUDE.md's inventory is missing or has a last-modified date older than 7 days, flag it to Richard.
5. **Declare mode and role:** If Richard hasn't declared, infer from context and state it. Richard corrects if wrong.

---

## Real-Time Conversation Logging [D] (27-Mar-26)

During sessions, Watson captures the conversation in real-time to `memory/conversations/YYYY-MM-DD-HH-[short-description].md`. This supplements memory files with the full context of discussions.

- Log Richard's messages verbatim where possible (especially instructions, preferences, insights, corrections)
- Log Watson's key responses and reasoning
- Timestamp entries
- Tag with role prefixes: [SA], [HPC], [RES], [IA], [EA], [APM]
- This log is the primary insurance against context loss between sessions

---

## What Is NOT Part of Handoff

The following are standalone protocols with their own schedules. They were previously bundled into the handoff SOP (V1 Steps 4b, 4c, 4d) but do not belong here. Handoff is archival — these are production tasks.

| Task | Where it lives now | Trigger |
|---|---|---|
| **Bright Spots logging** | Standalone — append to `memory/bright-spots.md` when a win occurs | During session (real-time) or at weekly review |
| **Daily Podcast generation** | `skills/daily-podcast/SKILL.md` | Standalone scheduled task or EOD routine |
| **Auto-IG Overnight Report** | `watson-researcher-executor` (23:05) + morning routine surfacing | Scheduled + morning briefing |

---

## Change Log

| Date | Change | Reason |
|---|---|---|
| 27-Mar-26 | V1 created (reconstructed) | Initial SOP |
| 12-Apr-26 | Step 0 naming convention added | Project/task naming discipline |
| 22-Apr-26 | Restart prompt template codified (R1-R10) | Standardise restart artefact |
| **23-Apr-26** | **V2 rewrite.** Removed 4b/4c/4d. Added Step 0 project routing. Removed "Next Session Priorities". SA role skips meta-role questions. `latest.md` becomes thin pointer. | Richard's instruction: handoff = close the workstream + capture everything. Not a launchpad for next actions. Production tasks don't belong in an archival protocol. |
| **03-May-26** | **Step 5.5 added — Hot Wash + Wisdom Library Proposal.** Cross-role bookend with AJ SOP v2.3 §Phase 4.5 (APM) and RESEARCHER SKILL-V2.11 Rule #37 (RESEARCHER pre-query consult). Hot wash 3-question structure + WL survey + tier + author/file or defer to candidate-queue. | Richard's instruction: enforce bookend pattern — start = WL consult, end = WL survey. Per Wisdom Library entry `memory-needs-workflow-binding` (Bronze) — memory entries don't enforce behaviour without workflow binding; Step 5.5 IS the workflow binding for "propose WL entries at session end." |
| **04-May-26** | **Step 5.5.0 added — Cohort presence check (cohort layer extension).** Sits at start of Step 5.5. Cross-role lock-step with AJ SOP v2.4.1 §Phase 0.0 + §Phase 4.6 + G17 (APM cohort layer), RESEARCHER SKILL-V2.13 Rule #38 (cohort manifest pre-consult), and master cohort SOP `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.1. Step 5.5.0 enforces G17: when a sub-cohort's last memo ships in this session, Phase 4.6 (cohort hot wash) MUST have run before Step 5.5 closes. De-duplication rule: cohort hot wash WL outcomes are listed in handoff WITHOUT re-surveying at Step 5.5 §2. | Cohort layer wraps the per-stock + per-session bookend. Without Step 5.5.0, cohort hot washes would be orphaned from the session record. |
