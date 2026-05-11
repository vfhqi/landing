# WATSON KAIZEN LESSONS — State

**Last updated:** 2026-05-04 by Watson

## Open lessons + corrective-action status

| Date | Lesson | Status | Corrective procedure |
|---|---|---|---|
| 2026-05-04 | Quality-gate must run at the decision point, not as a slogan | OPEN — corrective procedure proposed; needs Richard sign-off + behavioural verification next session | See `lessons/2026-05-04-quality-gate-failures.md` |
| 2026-05-04 | Session-end quality verdict: ATROCIOUS (Richard's explicit verdict) — sustained 8+ ship iterations within a single session despite mid-session corrective recording | OPEN — same corrective procedure as gate-failure lesson; pattern proven recurring within a single session | Same kaizen lesson + handoff `PROJECTS/SA - Dashboard Memo Read Layer/handoffs/handoff-2026-05-04-1148-quality-failure.md` |

## Pattern register

A growing register of behavioural patterns that have caused quality failures. Each is something to actively check against in future sessions.

1. **Knowing-vs-running gap.** Acknowledging a rule is not the same as applying it at the decision point. Rules need to fire as procedural gates, not as values to honour. (Source: 2026-05-04 lesson.)
2. **Capability-assumption-without-check.** Assuming a tool isn't available because the obvious form isn't (e.g. "no chromium binary in /usr/bin") instead of checking the MCP tool list. (Source: 2026-05-04 lesson — Claude in Chrome was available the entire time.)
3. **Spec-surrogate substitution.** Working against my mental sketch of the spec rather than the actual spec file on disk. (Source: 2026-05-04 lesson — built v1 against an interpretation of mockup v3 instead of mockup v3 itself.)
4. **Static-check theatre.** Running grep + AST + size checks and calling it "audit", when the bug class (cascade specificity, layout, hover, interactive) cannot be caught by static checks. (Source: 2026-05-04 lesson.)
5. **Self-imposed tempo.** Generating speed pressure on myself when no external deadline exists, then trading off audit thoroughness against that imagined pressure. (Source: 2026-05-04 lesson.)
6. **Ship-and-find-out.** Treating "shipped to preview URL" as the audit gate when the actual gate is "rendered in browser and walked end-to-end". (Source: 2026-05-04 lesson.)
7. **Recurrence within a single session.** Even after articulating root cause + saving the kaizen lesson mid-session, the same patterns recurred in the very next iterations. Mechanism: the lesson sits in context but is not running as a procedural gate. Acknowledgment of the rule is not application of the rule. (Source: 2026-05-04 PM — atrocious-quality verdict at session end.)
