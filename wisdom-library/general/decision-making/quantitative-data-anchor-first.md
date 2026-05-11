---
name: Quantitative-Data-Anchor-First (Anti-Pattern)
tier: gold
category: general/decision-making
keywords: [anchoring, narrative-bias, comp-table, skeleton-bias, framework-bias, data-discipline, sequencing, process]
cross_references: [peer-and-base-rate-anchoring, base-rates-vs-case-rates, strong-views-weakly-held, bayesian-updating, p-equals-p-minus-i, memory-needs-workflow-binding]
authors: [Watson, Richard]
created: 2026-05-04
last_updated: 2026-05-04
updated_by: APM
---

# Quantitative-Data-Anchor-First (Anti-Pattern)

## Definition

When building any comparative framework — comp table, peer-rank, scoring model, stack-rank — load the **quantitative inputs FIRST**, before committing structure to writing. Building a "skeleton then populating from data later" is an anti-pattern: the skeleton becomes the anchor, and once a narrative is written it requires active work to overturn even when contradictory data lands.

The rule: **structure follows data, not the other way around.**

## Why It Matters

Anchoring is one of the most well-documented cognitive biases in decision research (Kahneman, Tversky). In comparative analysis, anchoring is most insidious when it operates through structural choices — which dimension is in column 1, which name is at the top of a stack-rank, what gets a "borderline" framing — because these choices feel mechanical when in fact they encode strong implicit judgements.

Once committed to writing, the structural anchor is sticky. Subsequent contradictory data must overcome the friction of "we already said X" rather than start from neutral. The fix becomes available only through deliberate effort: explicit "challenge the skeleton" checkpoints, documented rebuilds, and a willingness to throw away the v1 framing.

The asymmetric risk: a skeleton that mis-anchors a stack-rank can directionally bias **portfolio sizing decisions** that follow from the rank. A 3-name comp table that puts the wrong stock at #1 may produce a sizing differential that compounds the error.

## Application

For any comparative analytical work:

- **Phase 0.5 — Data pre-flight (NEW v2.2 doctrine).** Before drafting any framework, identify all relevant quantitative sources and verify they are loadable: FactSet (SSEM, valuation), Master Dashboard (prices, filter results), per-stock financials, peer reference data. Fix corrupted files first; document gaps before they become discoveries mid-flight.

- **Load data BEFORE structure.** Read the actual numbers. Compute the actual percentiles. Pull the actual revisions, multiples, growth rates, leverage ratios. Only then start drafting comparative structure.

- **Treat "skeleton" outputs as hypotheses, not structures.** When proposing to draft a quick comp-table or stack-rank pre-data, write explicitly: "this is a hypothesis to be revised on data load." Build challenge checkpoints.

- **Embed explicit revision triggers.** After data lands, run a "challenge the skeleton" pass: does the data support the structure? Which cells changed direction? Which framing assumptions are now wrong?

- **Document v1→v2 reframings as calibration events.** When the data forces a reframing, capture the lesson. Was the qualitative anchor materially wrong? What was the source of the bias? Calibration log entry, not silent fix.

## Examples from Track Record

- **GYM-TRIO comp-table (May 2026 — the namesake):** v1 stack-ranked GYM > BFIT > SATS purely on qualitative read of the BM-Primer. SATS marked "borderline-park" on a "saturation thesis" anchor. FactSet SSEM data — loaded mid-flight in BFIT memo Phase 1 — showed SATS as the trio's momentum LEADER (13/15) and GYM as the LAGGARD (1/15). Forced full v1→v2 reframing with SATS upgraded to PROGRESS-CLEAN. The skeleton had set a wrong anchor that required active work to overturn. Cost: ~30 minutes of rebuild + the bias-management overhead across three subsequent memos.

- **Risk-pattern recognition:** the "build skeleton then populate" speed-vs-quality tradeoff is the same pattern as `memory-needs-workflow-binding` (memory entries don't enforce behaviour without workflow binding). Knowing the rule isn't enough; the workflow has to mechanically force the data load before structure.

## Counter-Examples (When Skeleton-First IS Defensible)

- **Pure exploratory work where no quantitative data exists yet.** First-pass scoping of a new sector or business model — pre-IG stage. Here the skeleton IS the data structure being defined. Different category of work.

- **When the skeleton is explicitly a question, not a conclusion.** "Here are the dimensions we should measure these names on" is a legitimate skeleton output if the cells are deliberately empty pending data. The anti-pattern is when cells get populated with qualitative read while waiting for quantitative data.

- **Time-pressured first-look briefings.** A client-pressure 30-min back-of-envelope where you flag "this is impressionistic" up front and never let it become canonical.

## Cross-References

`peer-and-base-rate-anchoring` (Communication Principle #1 — the data infrastructure that prevents this anti-pattern); `base-rates-vs-case-rates` (the underlying statistical principle); `strong-views-weakly-held` (the cognitive posture that makes revision possible); `bayesian-updating` (the formal correction process); `p-equals-p-minus-i` (Performance = Potential minus Interference; structural anchors are interference); `memory-needs-workflow-binding` (the parallel process pattern — knowing the rule ≠ running the rule)

## Change Log
2026-05-04 | APM | Created at Gold tier — direct from GYM-TRIO Triaging+ESA hotwash 03/04-May-26. Anti-pattern surfaced when comp-table v1 ranking proven directionally wrong by FactSet SSEM data loaded mid-flight. Material reframing v1→v2 absorbed but bias-management overhead real. Universal across investing analysis; should be a Phase 0.5 SOP discipline.
