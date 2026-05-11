---
name: Outlier-to-Cohort RS Fade
tier: bronze
category: situational/simple-patterns
keywords: [technical-analysis, relative-strength, sector-strength, mean-reversion, rs-rank, idiosyncratic-isolation, cohort-effect]
cross_references: [outlier-flagging-rare-data, peer-and-base-rate-anchoring]
authors: [Minervini, Watson]
created: 2026-05-03
last_updated: 2026-05-03
updated_by: APM
---

# Outlier-to-Cohort RS Fade

## Definition

When a single stock's Relative Strength rank materially diverges from its sector cohort's median RS rank (e.g., stock at RS 78 in a cohort at RS 50), the gap typically closes via the COHORT pulling the stock down rather than the stock pulling the cohort up. Estimated base-rate split: 70% cohort wins, 30% stock wins.

This is a technical-analysis variant of the broader `outlier-flagging-rare-data` pattern: a rare data point demands explanation, and "this stock is genuinely better" is usually the WEAKER explanation than "this stock will mean-revert."

## Why It Matters

A high RS rank is one of the strongest single bull signals in technical analysis (Minervini 8-point system requires RS rank ≥70). But high RS in ISOLATION — without sector confirmation — is a different signal than high RS WITH cohort support. The former is fragile (institutional money rotating through, not in); the latter is durable (institutional money rotating in, sector-wide).

The Minervini 8-point system as commonly applied does not distinguish these two cases. A stock can pass 8/8 Minervini and still be a high-risk technical setup if the sector cohort is rolling over — because the stock's outperformance becomes a fade target rather than a leadership signal.

## Application

When evaluating P1 Technical Strength (C.II.1 of any memo):

1. Compute the stock's RS rank (universe + sector)
2. Compute the SECTOR COHORT median RS rank
3. If stock RS exceeds cohort median by >20 percentile points, flag as **outlier-to-cohort**
4. Test the explanation:
   - "Stock is genuinely best-in-class within a so-so sector" → durable; verify with fundamentals
   - "Stock is the last man standing in a sector that's rolling over" → fade signal; technicals will mean-revert to cohort
5. Add a downgrade trigger to the technical setup: **"sector cohort breaks 200D first" = early warning for stock**

Practical rule: an outlier-to-cohort technical setup is rated 1 grade lower than the same setup with cohort support. An 8/8 Minervini in an outlier-to-cohort context = B not A; in a sector-supported context = A or B depending on other factors.

## Examples from Track Record

- **EKTA (May-26):** RS rank 78 in med-tech equipment cohort with RS rank ~50. Cohort: Varian RS 62, Accuray RS 35, Mevion RS 28. Stock was sectorally-isolated outlier. Combined with base-3 + extended +28% from 200D, technical setup downgraded from default A toward B with explicit downgrade trigger ("sector cohort breaks 200D first").
- **COTN-CH (May-26):** RS rank 81 in semi-cap equipment cohort with RS rank ~70. Cohort SUPPORTIVE (cycle inflection visible across cohort — ASML, AMAT, LRCX, AEIS all trending up). Different from EKTA's isolated outperformance. Technical setup rated B held — sector context didn't downgrade.

The contrast between EKTA (isolated outlier → downgrade) and COTN-CH (sector-supported → no downgrade) is the diagnostic case for this pattern.

## Boundary Conditions

- Time horizon: applies to 3-12 month technical setups; less informative for very-short-term (< 1 month) or very-long-term (> 2 year) horizons
- Cohort definition matters: use the smallest meaningful sector grouping (e.g., "med-tech equipment" not "healthcare"). Too-broad cohort dilutes the signal
- Industry transition periods (e.g., new theme emerging, new technology displacing old) can create legitimate sector-dispersion where the outlier is the leader, not the laggard. Test by checking if the cohort is bifurcating (some up, some down) vs uniformly weak

## Cross-References

- `outlier-flagging-rare-data` (Gold) — the parent pattern this is a technical-analysis variant of
- `peer-and-base-rate-anchoring` (Gold) — cohort base-rate anchors the outlier-test
- Minervini 8-point system — base technical framework that this pattern adds nuance to
- AJ SOP v2.2 §Phase 2 §C.II.1 content scaffold (e) — sector-strength check is mandatory in P1 analysis

## Change Log

- 2026-05-03 | APM | Created at Bronze tier from 03-May-26 EKTA vs COTN-CH technical comparison. Awaiting more cases to consider Silver promotion.
