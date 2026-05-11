# CONTEXT WINDOWS + SOP

**Status:** MISSION CRITICAL — applies to every role, every session, every conversation.
**Created:** 20-Apr-26 (evening, after MEMO-view session context loss incident).
**Origin:** Richard's direct instruction after repeated context-compaction loss broke project continuity.

---

## AIM

Watson must **never lose knowledge in a temporary context window / session memory**. Many projects persist over multiple days (MEMO view build, FCS SOP V5, thematics, MM batch, dashboard architecture, etc.). Losing continuity is not a minor inconvenience — it is a project-level failure.

## REQUESTS (standing rules)

1. **Do not write to context-window memory unless explicitly asked.** Always check which memory layer to write to. If in doubt, write to a durable file.
2. **Default to durable memory files** that persist across sessions. Any such file can be restarted weekly if it grows stale, but nothing critical should live only in session memory.
3. **Save continually / regularly.** Maximum gap: **5 minutes** between saves during active work. If a decision is made, a structure is agreed, a correction is received, a file is edited, a judgement is rendered — persist it immediately to a durable file.
4. **Every role, by default.** RESEARCHER, EA, FA, APM, HPC, SA — same rule. No role is exempt. No "this is just quick work" exceptions.
5. **Embed visibly.** This rule must be obvious/high-up in CLAUDE.md and linked from MEMORY.md so every fresh session hits it early.

## WHAT COUNTS AS "DURABLE"

- Anything under `C:\Users\richb\Documents\COWORK\` (the mounted COWORK folder). Persists on Richard's local disk across sessions.
- Specifically: `memory/`, `databases/`, `Files/`, `AI Prompts/`, etc.
- **NOT durable:** session scratch (`/sessions/*/mnt/outputs/` outside COWORK), conversation context, summaries, in-context TODO lists, tool output history, auto-memory space under `local-agent-mode-sessions/...` (app-internal, not in session mount).

## WHAT COUNTS AS "CONTEXT-WINDOW ONLY"

- Messages in the current conversation.
- Output of tool calls that isn't also saved to a file.
- Compacted summaries of prior conversation turns.
- TaskList entries (useful for current session only — do not rely on for project state).

## PRACTICAL APPLICATION

**Every 5 minutes of active work**, ask: *"Is anything I've learned, decided, corrected, or built in the last 5 min living only in this context window?"* If yes → persist now.

**Save triggers** (non-exhaustive):
- Richard gives a correction or preference → append to `memory/corrections.md` and/or write new `feedback_*.md` memory.
- New project understanding, scope, or structure → write to `memory/projects/{project}.md`.
- Style decision, taxonomy, naming convention → write to `memory/context/*.md` or the relevant SKILL.
- Transcript of long session → extract to `memory/transcripts/{date}-{project}.md` as durable reference (see 20-Apr-26 memo-view transcript for precedent).
- File edit → the diff is on disk; OK. But **why** the edit was made should be captured in a commit message or project note if non-obvious.
- Open decision waiting on Richard → log to `memory/projects/{project}.md` under "Open decisions".

**Session handoff protocol** (existing, reinforced):
- `memory/session-handoffs/latest.md` overwritten each handoff.
- Pre-compaction: if context is about to compact, write a handoff note first.

## WHY THIS MATTERS (incident log)

- **27-Mar-26:** Memory files were written to session-relative paths and lost when the session ended. Rule: all memory files live under `C:\Users\richb\Documents\COWORK\`.
- **20-Apr-26 evening:** Post-compaction summary of MEMO view session inferred Section A = "Summary & IAJA Conclusion." Wrong. Actual Section A = FINANCIALS (per `databases/memo-schema.md`). Claude was operating on a condensed inference rather than reading the authoritative durable file. Richard halted: *"This is stupid. stupid. stupid. Stupid. We spent so long briefing this in earlier."* The fix was to read the full conversation transcript (saved durably as `memory/transcripts/20-Apr-26-memo-view-morning.md`) AND the schema file — both durable. Lesson: **compaction drops detail; durable files retain it. Always prefer the durable file.**

## RELATIONSHIP TO OTHER MEMORY LAYERS

| Layer | Purpose | Durability | Use for |
|-------|---------|------------|---------|
| Conversation context | Current session reasoning | Ephemeral | Active thinking only |
| TaskList | Current session task tracking | Ephemeral | In-session coordination |
| Auto-memory (app-internal) | Cross-session personal index | Persists (different mechanism) | Quick hooks — but NOT primary storage for project work |
| **COWORK memory/** | **Project + operating knowledge** | **Persists on local disk** | **Primary. Everything critical goes here.** |
| Git commits (vfhqi/dashboards etc.) | Code changes + context | Persists | Code + concise "why" |

**Rule of thumb:** If Watson is unsure where to save, the answer is **COWORK memory/**.

---

## COMPACTION SURVIVAL — PROTOCOL RELOAD (added 23-Apr-26)

**Problem:** When context compaction occurs, Watson's operating protocols get summarised. Summaries drop details — which is exactly the failure mode these protocols exist to prevent.

**Rule:** After any context compaction event, Watson must:
1. Check whether the Operating Values, UWBs, and Operating Method are still fully in context (not just summarised)
2. If summarised or absent → re-read CLAUDE.md (Operating Values + UWBs) and `memory/context/working-preferences.md` §Watson Operating Rules
3. The auto-memory pointer at MEMORY.md line 1 serves as the tripwire — if Watson sees the pointer but can't recall the full protocol detail, reload

**This makes compaction survivable rather than catastrophic.** The protocol details are on disk; Watson just needs to re-read them.

---
*This rule overrides conflicting guidance elsewhere. When in doubt, save to COWORK.*
