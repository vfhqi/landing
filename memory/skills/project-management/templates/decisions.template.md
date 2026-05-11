# decisions.md — {PROJECT SLUG}

**Rules:**
- Append-only. Never delete or edit historical decisions. If superseded, log a new decision that supersedes it (and link back).
- Each decision gets an ID: `D-{SLUG-ABBREV}-N` (e.g. `D-PRJ-1`, `D-DSH-3`).
- Format: ID / Date / Decision / Why / How to apply / Superseded by (if any).

---

## D-{SLUG-ABBREV}-1 — {YYYY-MM-DD} — {Short title}

**Decision:** {What was decided, in one or two sentences.}

**Why:** {Motivation — often a constraint, a prior incident, a stakeholder ask.}

**How to apply:** {What changes in Watson's behaviour / the codebase / the workflow.}

**Superseded by:** {blank, or link to newer decision}

---
