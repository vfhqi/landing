# Optimal Restart Prompt — Universal Template

<!-- [W] Authored 22-Apr-26 as canonical SSoT for the restart-prompt artefact. Owned by the session-handoff SKILL. Update here, not in handoff notes. -->

## Purpose

Every handoff (manual end-of-session, 15:00 auto-handoff, and full-backup) MUST embed an **Optimal Restart Prompt** at the very top of the handoff note in a fenced ```text code block. This is the single artefact Richard copy-pastes into a new session to restart work with maximum continuity from the prior session — even if memory files are unreachable, even after long gaps, even if the next session is run on a different machine.

The restart prompt is **self-contained** (Richard chose "Full self-contained, ~50-100+ lines" on 22-Apr-26): it must work as a standalone briefing, not just as a pointer.

---

## Universal Skeleton (slots in `{{...}}`)

```text
Good {{morning|afternoon|evening}}. Watson, you are resuming {{PROJECT NAME}} from {{LAST SESSION DATE/TIME UK}}.

Role: {{PRIMARY ROLE}} ({{primary}}). {{SECONDARY ROLE}} as secondary/background.
Mode: {{DEVELOPMENT|EXECUTION}}.
Agenda mode rationale: {{1 sentence — why this mode}}.

=== ORIENTATION (read in this order before responding) ===
1. COWORK/.claude/CLAUDE.md (always — operating context)
2. COWORK/memory/session-handoffs/LATEST-FULL-BACKUP.md → follow pointer to latest backup folder
3. COWORK/memory/session-handoffs/transcripts/{{LATEST-BACKUP}}/STRUCTURAL-NARRATIVE.md
4. COWORK/memory/session-handoffs/latest.md (this handoff note)
5. COWORK/memory/projects/{{ACTIVE PROJECT}}/state.md (live project state)
6. COWORK/memory/projects/{{ACTIVE PROJECT}}/decisions.md (locked decisions — never re-ask)
7. {{ROLE-SPECIFIC SKILL FILE — e.g. memory/skills/assistant-portfolio-manager/SKILL.md}}
8. {{TASK-SPECIFIC SOP — e.g. memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md}}
9. .auto-memory/MEMORY.md (always — pointers to feedback rules)

=== WHERE WE LEFT OFF (verbatim — do not summarise without reading source files) ===
{{2-4 sentences: what was just shipped, what was in-flight when session ended, what state the live files are in}}

=== ACTIVE OPEN QUESTIONS (these block work — answer-or-park before authoring) ===
Q1. {{question + your proposed default + why}}
Q2. {{question + your proposed default + why}}
Q3. {{question + your proposed default + why}}
({{Optional Q4–Q5 if material}})

=== TODAY'S WORK, IN PRIORITY ORDER ===
A. {{Highest priority task — concrete deliverable, source files, dual-post target, validation step}}
B. {{Next priority — same shape}}
C. {{Next priority}}
D. {{Final: GitHub push + FULL-BACKUP + handoff}}

=== STANDING OPERATING RULES (always-on for this session) ===
- Pre-write snapshot before any non-trivial mutation (SA pre-write-backup-SOP).
- FULL-BACKUP every 30 min minimum and after every milestone (feedback_structural_backup_protocol).
- Dual-post live to Notion (Stock(s) relation MANDATORY) for any APM/RES output.
- If coverage is thin, brief the RESEARCHER — do NOT proceed with gaps (APM analysis-judgement-SOP).
- Live-case invalidations (D-INV-1) escalate immediately.
- Edit tool is BANNED on files >~800KB; use bash+Python (feedback_edit_tool_truncation_bug).
- {{Project-specific rule, if any}}

=== BACK-BRIEF REQUIRED BEFORE ANY AUTHORING ===
After completing the orientation reads, back-brief me in ONE paragraph covering:
(a) what was shipped last session,
(b) what is still owed to me,
(c) the three questions at the top of your stack for me to answer.

Do NOT start authoring or mutating files until I have answered the open questions above.

=== RECOVERY-MODE FALLBACK (use only if memory files are unreachable) ===
If COWORK fails to mount or any of the orientation files are missing/corrupt:
- Active project: {{PROJECT NAME}}
- Active stage: {{e.g. Triaging | ESA | DD-P1 | DD-RO | Invest}}
- Last shipped artefact: {{e.g. NVTK Triaging memo v3.1, dashboard build 1,911,916 bytes}}
- Last commit hash: {{e.g. 1ceb028 (stale — needs push)}}
- Live dashboard URL: {{GitHub Pages URL if applicable}}
- Re-mount COWORK at C:\Users\richb\Documents\COWORK and report status before doing anything else.
```

---

## Authoring rules (Watson follows these when drafting the prompt)

### R1 — Self-contained, not a pointer
Richard explicitly chose the **Full self-contained** depth on 22-Apr-26. The prompt must work even if the orientation reads fail. That's why the **WHERE WE LEFT OFF**, **ACTIVE OPEN QUESTIONS**, **TODAY'S WORK**, and **RECOVERY-MODE FALLBACK** sections are all populated with real content, not placeholders.

### R2 — Role/Mode declared at top
Per CLAUDE.md roles protocol. Always state both primary AND secondary role. Always declare mode explicitly with a one-sentence rationale (the rationale forces Watson to think about whether the mode is right rather than defaulting).

### R3 — Orientation reads in dependency order
1. CLAUDE.md → 2. LATEST-FULL-BACKUP → 3. STRUCTURAL-NARRATIVE → 4. latest handoff → 5. project state → 6. project decisions → 7. role SKILL → 8. task SOP → 9. .auto-memory/MEMORY.md. The order matters because each step assumes context from the previous.

### R4 — Open questions BEFORE work, not after
List 3-5 open questions with Watson's proposed defaults. This forces Richard to choose-or-park before content authoring begins, eliminating the "Watson got 80% through, then asked, then redid" failure mode.

### R5 — Priority order is explicit and small
A > B > C > D. No more than 4 lettered work items. Prevents tangent-chasing. The final item is ALWAYS GitHub push + FULL-BACKUP + handoff.

### R6 — Standing operating rules are listed inline
Don't assume Watson will recall them from auto-memory. List the live rules that apply to today's work explicitly. Always include: pre-write backup, FULL-BACKUP cadence, dual-post Notion, live-case invalidations, Edit tool ban on large files. Add project-specific rules as needed.

### R7 — Back-brief is mandatory
Per Richard's standing preference ("Richard likes explicit alignment checks"). The prompt MUST instruct Watson to back-brief before authoring.

### R8 — Recovery-mode fallback at bottom
The minimum viable state needed to resume if everything else fails. Project name, stage, last artefact, last commit, dashboard URL. Forces Watson to declare these explicitly when authoring the prompt — which itself surfaces gaps in our state-tracking.

### R9 — Verbatim, not summarised
The "Where we left off" section quotes the actual state of files (sizes, commit hashes, validator status), not a paraphrase. Paraphrases drift; numbers don't.

### R10 — One template, fill the slots
There is ONE universal template (Richard chose this on 22-Apr-26). Do not fork variants per role/project. The slots flex enough to cover SA builds, RES IG, APM cases, HPC coaching, EA admin.

---

## Where the prompt lives

| Location | Purpose | Update cadence |
|---|---|---|
| **Top of `memory/session-handoffs/latest.md`** in a fenced ```text block | Primary copy-paste target for the next live session | Overwritten every handoff |
| **Top of `STRUCTURAL-NARRATIVE.md`** inside each FULL-BACKUP folder | Frozen snapshot of restart prompt at backup time — survives even if `latest.md` is corrupted | Written once per backup, never edited |
| **Top of `memory/session-handoffs/{{topic}}-handoff-{{date}}.md`** for any topic-specific handoff | Same role for project/topic-specific resumption | Once per such handoff |

The legacy `memory/session-handoffs/TOMORROW-RESTART-PROMPT.md` file is **deprecated** — the prompt now lives at the top of `latest.md` itself. Do not create separate restart-prompt files going forward.

---

## Quality gate

Before considering a handoff complete, Watson confirms:

- [ ] Restart prompt is at the very top of `latest.md` (after title, before first H2)
- [ ] All `{{slots}}` are filled with real content (no placeholders left)
- [ ] Orientation reads list 9 items in correct order
- [ ] At least 3 open questions listed with proposed defaults
- [ ] Priority order has ≤4 lettered items
- [ ] Standing operating rules section present
- [ ] Back-brief instruction present
- [ ] Recovery-mode fallback section present and populated
- [ ] Same prompt embedded at top of STRUCTURAL-NARRATIVE.md in latest FULL-BACKUP folder

---

## Worked example

See `memory/session-handoffs/TOMORROW-RESTART-PROMPT.md` (21-Apr-26) for the prototype. Note: that file used a 7-step orientation list and embedded most of these elements but pre-dates the 22-Apr-26 codification. The template above is the canonical successor.
