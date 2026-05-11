# MANIFEST — {PROJECT SLUG}

**Status:** BOSSY — Watson obeys this manifest. It overrides ad-hoc loading choices for this project.
**Owner:** Richard (authoritative) + Watson (proposer, updater)
**Created:** {YYYY-MM-DD}
**Last reviewed:** {YYYY-MM-DD}
**Doctrine reconciled:** {YYYY-MM-DD} — CLAUDE.md / project-management SKILL.md version last checked against this MANIFEST. If >7 days old vs current CLAUDE.md, audit at next session.

---

## Purpose (one paragraph)

{Why this project exists. What does "done" look like. What problem does it solve.}

## Higher intent

{The deeper reason this matters. The meta-outcome this project serves. Preserved from Richard's words where possible.}

## Authority rules

- This manifest **extends** global rules (CLAUDE.md, feedback_*.md, other SKILLs) — it does NOT override them.
- If this project requires a local override, it must be logged in `decisions.md` with a project-scoped justification and a `D-{slug-abbrev}-N` ID.
- The default operating stance is global rules first, project rules second, ad-hoc never.

## Role bindings

- **Primary role:** {SA / APM / RES / EA / FA / HPC / COS}
- **Secondary roles (if any):** {list}
- **Meta-roles always watching:** SA + HPC (standing rule)

## Loads — Tier 1 (MANDATORY, silent at session start)

Watson fetches these every time without asking.

- [ ] `CLAUDE.md` (always)
- [ ] `.auto-memory/MEMORY.md` (always)
- [ ] `memory/corrections.md` (always)
- [ ] `PROJECTS/{slug}/MANIFEST.md` (this file)
- [ ] `PROJECTS/{slug}/state.md`
- [ ] `PROJECTS/{slug}/decisions.md`
- [ ] `PROJECTS/{slug}/open-questions.md`
- [ ] `PROJECTS/{slug}/handoffs/LATEST.md`
- [ ] {project-specific mandatory files, e.g. `memory/skills/X/SKILL.md`, `databases/Y.md`}

## Loads — Tier 2 (ASK Richard at session start)

Watson asks: *"Shall I also load {list}? Tilt comprehensive unless energy signals brevity."*

- [ ] {file 1 — reason}
- [ ] {file 2 — reason}
- [ ] ...

## Loads — Tier 3 (LAZY — fetch on demand only)

Known-relevant but heavy; pull only when the specific question arises.

- [ ] {file 1 — when}
- [ ] {file 2 — when}

## Invariants (NEVER violate without explicit Richard override)

List the one-strike rules for this project. Things that, if Watson does them, break the project.

1. {invariant 1}
2. {invariant 2}
3. ...

## Active open decisions (pointer)

Live list lives in `open-questions.md`. Summary here:
- {open decision 1 — status}
- {open decision 2 — status}

## Stakeholders

- **Richard (Owner / Final Authority)**
- **Watson ({role})** — execution, documentation, protocol adherence
- {other humans involved, if any}

## Success criteria

- {measurable outcome 1}
- {measurable outcome 2}
- {qualitative criterion}

## Known failure modes (red-team)

- {risk 1 — mitigation}
- {risk 2 — mitigation}

## Project-specific operating rules

- Save cadence: verbatim to `transcript.md` after each exchange + snapshot every 15 min (default) OR {project override}
- Handoff cadence: {default / custom}
- Escalation triggers: {what makes Watson pause and ask}

## Cross-references

- `memory/skills/project-management/SKILL.md` — the authoring protocol
- {other files that matter for this project}
