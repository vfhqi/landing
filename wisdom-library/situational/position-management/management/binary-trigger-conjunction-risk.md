---
name: Binary Trigger Conjunction Risk — Correlated Invalidations
tier: bronze
category: situational/position-management/management
keywords: [invalidation, binary-trigger, conjunction-probability, correlated-risks, scenario-analysis, ach, ekta, prysmian]
cross_references: [single-leg-case-downgrade, cockroaches-never-alone, peer-and-base-rate-anchoring]
authors: [Watson]
created: 2026-05-03
last_updated: 2026-05-03
updated_by: APM
---

# Binary Trigger Conjunction Risk — Correlated Invalidations

## Definition

Many investment cases have multiple invalidation triggers that, individually, have manageable probability (15-30% each). The case-killing scenario is usually the **CONJUNCTION** of two triggers firing in the same quarter or earnings cycle. The conjunction probability is LOWER than either single-trigger probability but materially HIGHER than independence-implied product would suggest, because conjunction triggers are often correlated (both reflect a common macro / structural condition).

## Why It Matters

Standard scenario analysis ignores correlation between triggers. A case might have:
- Trigger A: 25% prob (e.g., backlog write-down)
- Trigger B: 25% prob (e.g., competitive event invalidating product cycle)

Independence-implied conjunction = 25% × 25% = 6.25%. But if both triggers reflect "macro stress on the company's core market" (common driver), the actual conjunction is closer to 12-15% — roughly 2× the independence assumption.

The case-killer scenario isn't usually a single-trigger event; it's the conjunction. APM judgement should explicitly identify the most-likely conjunction AND name the correlation that elevates its probability vs independence-product.

## Application

When constructing the D.II.1 ten-ACH stack at ESA / DD:

1. List the top 3-5 invalidation triggers AND their individual probabilities
2. For each pair: ask "do these triggers share a common driver?" (macro stress, sector cycle, competitive intensity, regulatory shift)
3. If correlated: estimate conjunction probability as ~1.5× to 2.5× the independence product
4. Identify the top-1 conjunction (highest joint probability AND most case-destructive)
5. Add as an explicit ACH watchpoint in D.II.1
6. Monitoring discipline: track BOTH triggers in parallel — early warning on either elevates conjunction probability

The output is an explicit "case-killer" scenario named in the memo, not just a list of independent triggers. APM should be able to articulate "if X AND Y both happen in 2H 2026, the case dies — X probability ~25%, Y probability ~30%, conjunction ~15% given both correlate to weak European industrial demand."

## Examples from Track Record

- **EKTA (May-26):** ACH#11 (third backlog write-down, ~25% prob) + ACH#12 (Varian Sept-26 superior platform, ~60-70% prob). Both correlate to "European mid-cap medtech under pressure" macro environment. Conjunction probability estimated ~10-15% (vs 15-18% independence-product) — the case-killer scenario explicitly named.
- **PRY (May-26):** Encore integration miss + capacity oversupply 2027 (NKT/Hellenic). Both correlate to "European industrial cycle weakness." Conjunction ~20-25% per ESA GNG CHECKS Q8.
- **HTRO (May-26):** DC growth deceleration + Weterings-second-cockroach. Different correlation driver (hyperscaler capex + serial-acquirer discipline are largely independent) so conjunction closer to independence-product ~6-10%.

## Boundary Conditions

- Correlation estimation is judgemental — explicit acknowledgement, not false precision. APM should give a range (e.g., "1.5× to 2.5× independence")
- Some conjunctions are negatively correlated (one trigger firing reduces probability of the other) — these are case-protective, not case-killer
- Triggers tied to discrete events (regulatory ruling, competitor product launch with known date) have lower variance than triggers tied to continuous metrics (margin compression) — different sizing of conjunction probability
- The pattern applies most strongly to cases with concentrated risk drivers; diffuse-risk cases (highly diversified businesses, conglomerates) rarely have meaningful trigger conjunctions

## Cross-References

- `single-leg-case-downgrade` (Silver) — when the conjunction destroys both legs
- `cockroaches-never-alone` — the operational analog (multiple cockroaches share root causes)
- `peer-and-base-rate-anchoring` (Gold) — base-rates for correlated-trigger conjunctions in similar archetypes
- AJ SOP v2.2 §Phase 3 D.II.1 ten ACH stack + invalidation framework

## Change Log

- 2026-05-03 | APM | Created at Bronze tier from EKTA + PRY ESA ACH analyses. Promote to Silver with formalised conjunction-probability estimation framework (currently judgemental).
