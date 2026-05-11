---
name: Judgement → Analysis → Information ordering
tier: gold
category: general/decision-making
keywords: [communication, ordering, judgement-first, BLUF, layer-cake, signposting, bullet-construction]
cross_references: [iaja, mission-command, peer-and-base-rate-anchoring, top-decile-top-quartile-grading]
authors: [Richard]
created: 2026-05-01
last_updated: 2026-05-01
updated_by: SA
---

# Judgement → Analysis → Information ordering

## Definition

Every analytical output — at every level of the taxonomy — leads with **judgement**, followed by **analysis** that supports it, followed by **information** underneath. Reverse order = burying the lede; fail.

This applies recursively at every analytical tier: a single bullet, a CQ, an RA, an element, a group, a pillar, an investment case, a memo. The ordering is a fractal property — true at every scale.

## Why It Matters

Richard reads to disagree. He skims judgement first; if he agrees, he doesn't need to read further. If he disagrees, he drops down to analysis to see why; then drops further to information if the analysis depends on a fact he wants to verify. Three layers, optional drill-down.

The opposite ordering (information → analysis → judgement, the academic format) forces Richard to read everything to find out what Watson concluded. That's a 10× time tax on every output.

The ordering aligns with **progressive disclosure** (Nielsen Norman Group), **BLUF** (Bottom Line Up Front, military comms), and **layer-cake scanning** (NN/g eye-tracking research). Watson did not invent it — Watson is implementing a pattern that consistently wins across professional communication contexts.

## Application

**At bullet level:** Every parent bullet starts with the judgement (verdict/rating/short claim). Sub-bullets carry the supporting analysis. Information layer (citations, numbers, source quotes) sits underneath that.

**At CQ level:** The first bullet of a CQ's answer should be the judgement on that CQ. Subsequent bullets supply analysis. Anchor groups can be used to layer additional analysis when weight justifies depth.

**At RA level:** The RA summary block (when present) leads with bold judgement bullets; un-bold bullets carry the analysis layer. Rating chip on the RA is the most-distilled judgement of all.

**At element / group / pillar level:** Element summary, group summary, pillar summary — each leads with judgement bullets up top, analytical bullets below. The summary block IS the layer of judgement that lets Richard skip over the deeper structure if he agrees.

**At memo level:** A great memo lets Richard read 5% of the words and form 95% of the case-level view. That's only possible when judgement is structurally hoisted to the top of every analytical unit.

**Universal rule for ALL Watson communication:** Even in chat responses, status updates, EOD briefings, weekly reviews — lead with the verdict; supply the reasoning underneath.

## Examples from Track Record

- **Memo template V20 (1-May-26):** Every analytical tier (CQ, RA, element, group, pillar) has a summary block that leads with judgement bullets. Rating chips are the most-distilled judgement form; the chip is rendered BEFORE the supporting analysis.
- **EOD handoff format:** "At-a-glance" section at top is judgement-only; detailed sections beneath supply the analysis.
- **APM ratings:** A/B/C/D/F is the apex judgement; everything else in a memo is analysis or information that supports the rating.

## Anti-patterns

- **Front-loading caveats:** "Before we get to the conclusion, it's important to note that..." — this is the academic-paper pattern. Wrong here.
- **Burying the recommendation in a closing paragraph:** Classic management-consulting output. Wrong here.
- **Equal-weighting analysis vs judgement:** If Watson treats analysis and judgement as the same kind of bullet, Richard can't skim. The judgement bullet must be visually distinct (bold, top position, larger weight) — its hoisting must be apparent at a glance.

## Cross-References

`iaja` — IAJA loop runs Information → Analysis → Judgement → Action; J→A→I ordering is how the OUTPUT of that loop should be presented to a reader.
`mission-command` — back-briefing pattern; the back-brief itself should lead with the judgement on what Richard is asking, not a recap of his words.
`peer-and-base-rate-anchoring` — peer context is part of the analysis layer; it sits under the judgement, not above it.
`top-decile-top-quartile-grading` — the grade IS the judgement; the analysis explains why.

## Codified in

- `databases/memo-view-formatting-principles.md` v3.8 — memo template structurally enforces this at every tier via summary blocks + signposting + rating chips.
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 — SOP mirror.
- `memory/skills/communication-principles/SKILL.md` — cross-role principle.
- `memory/coaching/lessons-and-mistakes.md` — bright spot 1-May-26 references this ordering as part of why back-briefing succeeded.
