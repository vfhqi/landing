---
name: Stage-Gating Works in Both Directions
tier: bronze
category: situational/portfolio-construction
keywords: [stage-progression, esa, dd, conviction-revision, depth-of-analysis, recommendation-flip, research-process]
cross_references: [judgement-analysis-information-ordering, peer-and-base-rate-anchoring]
authors: [Watson]
created: 2026-05-03
last_updated: 2026-05-03
updated_by: APM
---

# Stage-Gating Works in Both Directions

## Definition

Each gate transition in the 6-stage research process (IG → Triaging → ESA → DD → Capital) can shift conviction in EITHER direction — not just upward. The depth-of-analysis added at each stage is a genuine recalibration tool, not a one-way validation ladder. A stage-progressing memo can downgrade conviction (PROGRESS → PARK) just as readily as it can upgrade it.

## Why It Matters

The intuitive failure mode is treating stage progression as monotonic — "I decided to triage it, so I'll progress it; I decided to ESA it, so I'll DD it." That collapses the gate into a sunk-cost ratchet. The discipline of treating each gate as a fresh judgement (with new information from the deeper analysis) is what protects against carrying broken cases forward.

Empirical evidence: 03-May-26 batch run on 4 stocks yielded 4 different ESA-stage outcomes — recommendation moved DOWN (EKTA: PROGRESS→PARK), UP-with-flag (HTRO: PROGRESS-to-DD with NEW cockroach), CONFIRMED (PRY: PROGRESS-to-DD), or surfaced a RESEARCHER GAP (COTN-CH: PROGRESS-to-ESA-gated). 3 of 4 were materially recalibrated by the depth added at ESA stage — only PRY's Triaging-stage view survived ESA scrutiny intact.

## Application

When authoring an ESA / DD memo, do NOT anchor on the prior stage's recommendation. Read the new RESEARCHER inputs FIRST, form judgements from those, THEN compare to the prior memo's framing. If the stages disagree, the deeper stage usually wins (more information). The Triaging→ESA recommendation FLIP is a feature, not a bug.

Specifically: at ESA stage, the new queries (08-BM, 10-Short, 11-VCMap, 12-VCAnalysis) are designed to surface structural risks that flat Triaging coverage cannot see — Varian-Sept-26 platform threats, R&D capitalisation accounting unwinds, value-chain bundle moats, etc. Expect them to change the answer in ~30-50% of stocks.

## Examples from Track Record

- **EKTA (May-26):** Triaging recommended PROGRESS to ESA on triple-margin-lever thesis. ESA found Varian Sept-26 next-gen platform threat + R&D capitalisation unwinding (-150bp) + backlog cascade risk → recommendation FLIPPED to PARK.
- **HTRO (May-26):** Triaging PROGRESS-to-ESA on DC scaling + asset-light services. ESA confirmed DC fulcrum but surfaced Weterings capital-destruction flag (M&A integration cockroach) → PROGRESS-to-DD with explicit cockroach watch.
- **PRY (May-26):** Triaging all-B distribution. ESA confirmed oligopoly + €17bn backlog visibility + quantified consensus gap → PROGRESS-to-DD with no recommendation change (the rare case where Triaging view survived intact).
- **COTN-CH (May-26):** Triaging surfaced AEIS structural-vs-cyclical share question. ESA-stage RESEARCHER queue was MISSING (7 queries unrun) — the gate revealed a coverage gap, not a conviction shift.

## Cross-References

- AJ SOP v2.2 §Phase 0 (pre-flight RESEARCHER coverage check) — gate-readiness check
- AJ SOP v2.2 §Judgement-importance-weighted escalation — case-level decisions belong to Richard at Step 4
- STAGE PROGRESSION SOP §Step 4 weekly review meeting
- `judgement-analysis-information-ordering` (Gold) — informs how the recommendation flip is communicated

## Change Log

- 2026-05-03 | APM | Created at Bronze tier from 03-May-26 batch run on 4 stocks (EKTA / HTRO / PRY / COTN-CH).
