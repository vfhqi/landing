---
name: Peer & Base Rate Anchoring
tier: gold
category: general/decision-making
keywords: [peer-comparison, base-rate, anchoring, context, percentile, communication, evidence, data-derived, narrative-derived]
cross_references: [base-rates-vs-case-rates, top-decile-top-quartile-grading, invert-and-call-out-bottom-quartile, outlier-flagging-rare-data, regression-to-mean, quantitative-data-anchor-first, ss-buy-rating-vs-revisions-divergence]
authors: [Mauboussin, Kahneman, Richard]
created: 2026-04-30
last_updated: 2026-05-04
updated_by: APM
---

# Peer & Base Rate Anchoring

## Definition
Every quantitative claim must be presented in the context of a relevant comparison set: peer companies, sector medians, industry distributions, or the full universe. A number without context is unjudgeable; a number with peer context becomes signal.

## Why It Matters
Investing is comparative. There are no absolute measures of "good." 22% gross margins is excellent for industrial services, mediocre for software, irrelevant for banks. Forcing the comparison every time builds the orientation muscle and prevents the analytical trap of judging a number against an internal anchor (e.g. "last year's number") instead of an external one (e.g. "the sector").

## Application
For every metric, fact, or quantitative claim:
- State the value
- State the comparison: sector median (most relevant), industry distribution, or universe percentile
- Three preference layers — sector → industry → universe
- If the comparison is genuinely unknown, say so and flag for follow-up
- Sources: FactSet sector medians, broker comp tables, Master Dashboard percentiles, INDEX.json data

This is operationalised as **Communication Principle #1** in `memory/skills/communication-principles/SKILL.md`. Inline format: *"22% gross margin (sector median 12%, top decile 22%)."*

### Operational pattern: data-derived vs narrative-derived peer context (NEW 4-May-26)

**Data-derived peer context** (strong) — pulled directly from quantitative sources: FactSet SSEM revisions, factset-valuation.json percentiles, Master Dashboard sector medians, INDEX.json percentile bands. Numbers are what they are; comparison is mechanical.

**Narrative-derived peer context** (weak) — inferred from research narrative ("BFIT is the largest..."; "GYM operates at lower margin than..."): readable but not benchmarked. The risk: narrative tone can quietly substitute for measurement. "Top quartile" gets used because the research voice felt confident, not because the percentile was checked.

**Rule:** when authoring memo-grade peer context, anchor to data-derived sources. When the data-derived source is missing or corrupted (e.g., factset-valuation.json missing trio names May-26), explicitly flag the gap; do not substitute narrative-derived context silently. Cross-ref `quantitative-data-anchor-first` (the anti-pattern that emerges when narrative anchors precede data load).

**Worked example:** GYM-TRIO comp-table v1 (May 2026) used narrative-derived peer context ("GYM has cleanest balance sheet"; "SATS faces saturation"). FactSet SSEM data — when loaded — showed the directional picture was wrong on momentum (SATS = LEADER 13/15; GYM = LAGGARD 1/15). Forced v1→v2 reframing. Lesson: data-derived peer context is structurally different from narrative-derived; treat them as separate sources of evidence with different reliability weights.

## Examples from Track Record
- **WH Smith (Apr-26):** Travel division 6.5% revenue CAGR through Covid recovery. Standalone fact = ambiguous. Vs UK travel retail peer set 2-3% = top quartile. Vs European travel retail 4-5% = above median. The peer comparison turned an ambiguous metric into a clear positive signal for the Quinn turnaround thesis.
- **DCC (Mar-26):** ROCE 12.5%. Standalone = unimpressive. Vs distribution peer median 8.5% = above median but not exceptional. Vs disciplined-acquirer peer set (Diploma, Halma) 22-28% = bottom quartile. The peer choice changed the verdict.
- **General lesson:** Same metric, three different verdicts depending on which base rate you anchor against. State the choice explicitly.

## Cross-References
`base-rates-vs-case-rates` (the broader statistical principle); `top-decile-top-quartile-grading` (the grading system this enables); `regression-to-mean` (why base rates work); `quantitative-data-anchor-first` (the anti-pattern that emerges when peer context is narrative-anchored before data load); `ss-buy-rating-vs-revisions-divergence` (specific application — peer context is what makes SS revision patterns interpretable)

## Change Log
2026-04-30 | SA | Created at Gold tier — direct from Richard's Communication Principles 30-Apr-26 lock. Operationalised in `memory/skills/communication-principles/SKILL.md` Principle #1.
2026-05-04 | APM | Augmented with "Operational pattern: data-derived vs narrative-derived peer context" sub-section from GYM-TRIO Triaging+ESA hotwash. Added cross-refs to `quantitative-data-anchor-first` and `ss-buy-rating-vs-revisions-divergence`. Added keywords data-derived / narrative-derived.
