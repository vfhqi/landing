---
name: Outlier Flagging — The "Hmmmmm" Marker (🚩 RARE)
tier: gold
category: general/decision-making
keywords: [outlier, rare, unusual, edge-case, signal, communication, evidence, variant-perception, tape-reading, marker-as-discovery]
cross_references: [peer-and-base-rate-anchoring, top-decile-top-quartile-grading, invert-and-call-out-bottom-quartile, animal-ceo, false-friends, management-cant-explain, incentives-drive-behaviour, ss-buy-rating-vs-revisions-divergence, sandbagging-precision-management-archetype]
authors: [Richard, Munger, Mauboussin]
created: 2026-04-30
last_updated: 2026-05-04
updated_by: APM
---

# Outlier Flagging — The "Hmmmmm" Marker (🚩 RARE)

## Definition
Anything **rare, unusual, uncommon, an edge case, or an outlier** in the areas the investment case cares about gets an explicit `🚩 RARE:` marker. This is the most insightful and actionable information class — the data points that make Richard go "Hmmmmm — why is that?"

## Why It Matters
Most data points are average. They fit the base rate. They confirm the obvious. They are not actionable.

The high-signal data points are the **deviations**: things that don't fit, things that surprise, edges where companies have done something most companies don't do. These are where genuine variant perception lives. A single unusual fact often reveals more than a hundred average ones.

The Leo Quinn example (WH Smith CEO, no bonus, 100% stock comp through 2027) is the model: one unusual data point that signals high CEO confidence — more revealing than an entire annual report's standard reporting. The base rate for FTSE350 CEOs on equity-only comp is <2%. Quinn put himself in that 2%. That's the signal.

## Application
Every memo must include at least one explicit scan for outlier data points. Markers: prepend `🚩 RARE:` to the verdict word. Optionally pair with the percentile grade — a 99th-percentile finding is both `[A]` AND `🚩 RARE:`.

Categories to scan for:

- **Compensation oddities:** CEO no-bonus / all-stock comp; founder paid £1; locked-in equity grants; clawback provisions; pay below sector median for senior roles
- **Capital allocation oddities:** insider buying spikes; no-debt operators in leveraged industries; special dividends; share buybacks at trough valuations; large transformative acquisitions in size-conservative companies
- **Disclosure oddities:** unusually candid management language; removal of forward guidance with explanation; sudden reporting changes; segment reorganisations that surface previously hidden detail
- **Operational oddities:** retention rates >95%; NPS in top decile; customer concentration unusually low or high; unusual gross margin trajectory
- **Governance oddities:** board with industry operators not just NEDs; founder-led with succession plan; family ownership with skin-in-the-game; unusual chair-CEO splits
- **Behavioural / cultural oddities:** unusual hiring patterns; internal promotion ratios; attrition rates; CEO public appearances or absences; unusual customer/employee testimonials

**Anything that surprises Watson during research** — if Watson notices and thinks "that's odd," it goes in.

The QC footer reports a RARE-marker count per memo; **zero RARE markers in a memo with substantive primary research = quality flag** (the scan didn't happen, or the analyst missed the unusual — both worth knowing).

This is operationalised as **Communication Principle #4** in `memory/skills/communication-principles/SKILL.md`.

### Marker-as-discovery pattern (NEW 4-May-26)

The 🚩 RARE convention is sometimes treated purely as a **communication marker** — a way to flag known unusual findings for the reader. But applied with discipline during memo-authoring, the marker becomes a **discovery mechanism**: the act of explicitly scanning "what is genuinely unusual here?" surfaces patterns the analyst hadn't pre-thought.

This is structurally similar to the inversion-Jacobi practice (asking "where would I die?" surfaces failure modes the analyst wouldn't have thought to enumerate). The 🚩 RARE prompt forces the analyst to look at the data with a different question — not "what does this confirm?" but "what here would surprise a sector specialist?"

**Empirical evidence (May 2026):** the GYM-GB "100% buy + persistent negative L1M revisions" pattern was DISCOVERED while applying the 🚩 RARE marker — not pre-thought, not flagged in any of the 77,342 words of GYM research, but visible the moment the analyst asked "what here is empirically rare?" The pattern subsequently became its own Wisdom Library entry (`ss-buy-rating-vs-revisions-divergence`). The marker drove the discovery.

**Operational rule:** when authoring memos, treat the 🚩 RARE scan as an active analytical exercise, not a passive labelling exercise. Spend 5-10 minutes per memo explicitly asking "what is empirically rare here that I haven't yet noticed?" The discoveries justify the time.

## Examples from Track Record
- **WH Smith (Apr-26 — the namesake):** 🚩 **Leo Quinn elected zero salary, 100% stock comp through 2027.** FTSE350 base rate <2%. Direct signal of personal conviction in NTM execution. Linked publicly to stated EPS doubling target. Single most actionable data point in the entire SMWH file.
- **HTRO (track record):** 🚩 **Customer retention 99.2% over 7 years.** Industrial services sector median 87%; only 1 of 32 European peers above 97%. Material moat indicator unexplained by stated competitive position. Triggered the value-chain deep dive.
- **Diploma (track record):** 🚩 **Disciplined acquirer with 35-year track record of 70+ deals, zero major write-downs.** Sector base rate ~30% of acquisitions written down within 5 years. Not just "good capital allocation" — outlier capital allocation. Carried the conviction.
- **AENA (track record):** 🚩 **Concession with mandated 0% real toll growth through 2027.** Most concession assets have CPI-linked or inflation+ pricing. The 0% creates a near-term headwind that mathematically resolves at the next regulatory reset — a genuine variant view available in plain disclosure.
- **NEX (Apr-26 cables):** 🚩 **Order book covers 5+ years of revenue at current capacity.** Industrial peers typically have 12-18 months. The 5-year visibility is the central thesis variable.

## Counter-Examples (When NOT to Flag)
- A "normal" data point that confirms the base rate — even if positive — is not a 🚩. "Operating margin in line with sector at 12%" is a [C] grade, not a 🚩.
- A finding that is unusual but irrelevant to the investment case is not a 🚩. "CEO has unusual hobby of competitive sailing" is colour, not signal.
- A finding that is unusual but already known and discounted by the market is a weaker 🚩 — note it, but flag the discounting.

## Cross-References
`peer-and-base-rate-anchoring` (the data infrastructure that makes "rare" identifiable); `top-decile-top-quartile-grading` (often paired with [A]); `invert-and-call-out-bottom-quartile` (often paired with ❌ for negative outliers); `animal-ceo` (CEOs whose outlier behaviour signals quality); `false-friends` (the inverse — when an outlier looks like signal but isn't); `incentives-drive-behaviour` (the underlying logic for why compensation oddities matter); `ss-buy-rating-vs-revisions-divergence` (specific RARE pattern — narrative + modelling divergence); `sandbagging-precision-management-archetype` (specific RARE archetype — exact-target delivery)

## Change Log
2026-04-30 | SA | Created at Gold tier — direct from Richard's Communication Principles 30-Apr-26 lock. Operationalised in `memory/skills/communication-principles/SKILL.md` Principle #4. Quinn / WH Smith is the namesake example.
2026-05-04 | APM | Augmented with "Marker-as-discovery pattern" sub-section from GYM-TRIO Triaging+ESA hotwash. The 🚩 RARE marker drove the discovery of the SS Buy/revisions divergence pattern — empirical confirmation that the marker functions as an active analytical exercise, not passive labelling. Added cross-refs to `ss-buy-rating-vs-revisions-divergence` and `sandbagging-precision-management-archetype`.
