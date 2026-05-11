# A&J SOP — Substance Methodology (10x weight)

**Version:** 1.0 — first standing version
**Authored:** 10-May-26 by Watson (APM role)
**Source:** distilled from HTRO V4-VERIFIED + V3 structural framework + V2 corrections
**Test stock validation:** HTRO (Hexatronic Group AB) — V1→V4 iteration documented in `PROJECTS/SA - Reports & Memos Repository/htro-test-stock/`

**Weight in three-SOP hierarchy:** 10x — this is the foundational SOP. Comms SOP (1x) and Presentation SOP (1/10x) sit on top. If the substance is wrong, no amount of presentation polish saves the case.

---

## §0 — PURPOSE + SCOPE

### What this SOP delivers

A standing methodology for producing investment-grade A&J on a single stock at any of the 6 stages (IG → Triaging → ESA → DD P1 → DD RO → Invest). The output is the SUBSTANCE — the analytical content, ratings, and integrated judgement. The Comms SOP determines HOW the substance is communicated at each stage; the Presentation SOP determines HOW it's formatted for Notion.

### What this SOP does NOT do

- Does NOT govern the per-stage memo construction (that's Comms SOP)
- Does NOT govern Notion formatting conventions (that's Presentation SOP)
- Does NOT replace stock-specific judgement — it provides the framework within which judgement operates
- Does NOT eliminate the need for Phase 0 hunts, RESEARCHER input, or Wisdom Library consultation

### Standing assumption

The user (Richard) is a solo public equities investor at Viewforth. Long-only, concentrated (5-15 positions), UK/Europe focus, GARP + event-driven/special situations. 25%+ IRR target for concentrated positions. The A&J SOP must produce output that supports concentrated long-only decisions, not portfolio overlay or trading.

---

## §1 — THE FRAMEWORK

### Three Pillars of any case

**Pillar I — Big Change Case (BCC):**
- The "engine" — what's changing about this stock that creates investment opportunity
- Three elements: E1 Predictability, E2 Asymmetry, E3 Transmission
- Plus optional E1.5 Optionality Value (added in V3, useful for stocks with embedded option value)

**Pillar II — Enabling Building Blocks (BB):**
- The "foundation" — the structural quality of the business
- Five Groups: BB#1 Operator, BB#2 Business Advantage + SRCA (QUADRUPLE WEIGHT), BB#3 Value Chain, BB#4 Industry Structure, BB#5 Secular Growth
- Pillar I + Pillar II together determine "is this a quality compounder or a turnaround?"

**Pillar III — Operational layer + monitoring:**
- The "in-flight checklist" — what to track once owned
- Three sub-blocks: D.I Monitoring metrics, D.II 10 Invalidation ACHs, D.III Risks + Tripwires + Hedges

### Master Ratings (MR1-MR6)

The Pillar work consolidates into 6 dimensions used in the Triaging / ESA / DD memos:
- MR1 — Earnings Growth Profile + Asymmetry
- MR2 — Business Quality + Moat
- MR3 — Management + Governance
- MR4 — Capital Allocation + Returns
- MR5 — Industry Position + Tailwinds
- MR6 — Stewardship + Alignment

Each rated A-F using bell-curve grading (target A, accept B, mediocrity-shun bar at C+/B-).

### 3-Check Declaration

Every case-level recommendation requires:
1. **Counter-Hypothesis check** — engaged with strongest counter to leading view, accepted or rejected with reasoning
2. **ACH ≥3** — at least 3 competing hypotheses surfaced, weighted, central case identified
3. **Multiple-Truths check** — ≥3 substantive multiple-truths identified (genuinely contradictory yet simultaneously valid)

### 10 Invalidation ACHs

Every case at DD-stage or post-investment requires explicit 10 single-strike sell triggers. These are pre-commitment selling discipline (Munger-style "invert always invert"). Each ACH has:
- Evidence chain (why this trigger matters)
- Tripwire mechanic (how to detect)
- Quantitative threshold (what counts as a trip)
- Action protocol (what to do on trip)

---

## §2 — THE PROCESS

### Phase 0 — Pre-flight gates (MANDATORY, ~30 min)

Per A&J SOP `analysis-judgement-SOP.md` Phase 0.0-0.3:

- **Phase 0.0** — Cohort manifest pre-load (does this ticker belong to an active cohort?)
- **Phase 0.1** — RESEARCHER coverage check (are required RR queries present?)
- **Phase 0.2** — Wisdom Library consult (load 5-10 matching mental models)
- **Phase 0.3** — Existing inputs hunt (NEW v2.5, MISSION CRITICAL):
  - Hunt 1: existing Excel financial model
  - Hunt 2: Master Dashboard pillar data (P1-P6 + ic-ratings)
  - Hunt 3: current share price (web-verified, not RR-text or training data)
  - Hunt 4: recent catalysts post-last-results
  - Hunt 5: verified peer multiples (web-sourced, not training-data approximations)

**The Phase 0.3 hunt prevents the V3 stale-SP error from recurring.** See `phase-0-checklist.md` for the full template.

### Phase 1 — Read + calibrate (10-20% of time)

- Read all RESEARCHER files for the ticker (per local-first lookup sequence)
- Read Master Dashboard data
- Read Richard's own Notion notes (case files, RNTS, journal entries)
- Calibrate: archetype tag, fact patterns, contradictions, key questions
- Track-record check (this stock + similar archetypes)

### Phase 2 — Pillar-by-pillar Analysis (50-60% of time)

**Effort allocation:** 70% of Phase 2 + 3 effort goes to Pillar II (Building Blocks). BB#2 quadruple-weight = roughly 40% of the entire Phase 2 effort goes on BB#2 alone.

**For each Pillar:**
- Decompose into elements/sub-elements
- Apply A-F bell-curve rating to each
- Document evidence chain for each rating
- Identify "look at the edges" findings (≥5 per case at DD depth)
- Engage counter-hypotheses for each rating

**For Pillar I (BCC):**
- E1 Predictability — bracket EPS at 12M, 24M, 36M horizons. Investment-grade ±15% / ±25% / ±35% thresholds.
- E2 Asymmetry — probability-weighted return calculation. Payoff ratio at central case. Tail-risk asymmetry.
- E3 Transmission — operational input → financial output → SP impact. Identify breakers. Multi-breaker = downgrade.
- E1.5 Optionality (optional) — separate from base-case. Re-rating mechanic, scarcity premium, M&A platform value.

**For Pillar II (BB):**
- BB#1 Operator Quality — CEO substance + archetype, CFO substance, senior team, board, comp alignment, track record
- BB#2 Business Advantage + SRCA (QUADRUPLE WEIGHT) — 8 sub-elements: differentiation, pricing power, customer stickiness, switching costs, network effects/scale, brand, IP, SRCA test
- BB#3 Value Chain — position in chain, customer concentration, supplier concentration, distribution, working capital
- BB#4 Industry Structure — Porter's Five Forces by segment, substitution threats
- BB#5 Secular Growth — segment-specific tailwinds, weighted by mix

**For Pillar III (Operational):**
- D.I — 5 quantitative tracking metrics with action protocols
- D.II — 10 Invalidation ACHs (single-strike sell triggers) with evidence chains
- D.III — 5 primary risks with quantification + tripwires + hedge consideration

### Phase 3 — Master Ratings + Integrated Judgement (10-15% of time)

- Consolidate Pillar work into MR1-MR6
- Reconcile with existing Master Dashboard ratings (Phase 0.3 Hunt 2 baseline)
- If revising existing ratings, justify with ≥3 evidence chains
- Compute composite Master Rating (equal-weighted simple average + qualitative judgement)

**Threshold for concentrated long position:**
- Composite ≥ B-/B = INVESTMENT GRADE for concentrated long
- Composite C+/B- = BORDERLINE — moderate position with explicit triggers
- Composite ≤ C = PARK or KILL

### Phase 4 — Integrated case-level judgement + 3-Check (10% of time)

- Park / Progress / Kill recommendation
- Confidence flag (Low / Medium / Medium-High / High)
- Position-sizing implication
- Entry-price discipline
- 3-Check Declaration formal

### Phase 5 — Stopping rule check (5% of time)

Per V3's 15-box stopping rule:
1. Every E1-E32 element has had real analysis applied + draft rating committed
2. Every Pillar (I, II, III) has integrated rating with reasoning
3. Every Group within each Pillar has integrated rating
4. Every Master Rating (MR1-MR6) has committed rating with reasoning
5. Case-level integrated judgement committed
6. 3-Check Declaration complete
7. ≥5 "look at the edges" findings logged
8. ≥1 substantive opposing-view section completed (deep bear case ≥3,000w + symmetric deep bull case ≥3,000w)
9. ≥1 historical parallel cited and reasoned through
10. Big Change Case + Enabling Building Blocks test explicitly answered
11. Comparable-company quantitative work (peer ratios)
12. Sum-of-parts valuation with segment-level multiples + scenario matrices
13. Mental-model lenses applied (≥5 investing-great frameworks)
14. 5-year vivid scenario narration (Bull/Base/Bear)
15. "What if I'm completely wrong?" pre-mortem

---

## §3 — KEY DOCTRINAL POINTS

### Quality > Speed

Always. The HTRO V3→V4 iteration showed that a 51,629-word "deep" memo built on stale inputs is structurally less useful than a 5,269-word focused memo built on verified inputs. **Verification depth > word count depth.**

### Phase 0.3 hunts are MANDATORY before Phase 1

The V3 stale-SP error was a Phase 0 process failure, not analytical reasoning failure. The fix is procedural: NEVER skip Phase 0.3 hunts on stock-specific A&J.

### BB#2 quadruple-weight is load-bearing

A C-rated BB#2 dominates Pillar II's integrated grade. If composite Master Rating is borderline, BB#2 is usually the binding constraint. Spend disproportionate effort here.

### Bell-curve grading

A = top 10% of universe
B = top 25%
C = middle 50%
D = bottom 25%
F = bottom 10%

Apply this discipline rigorously. "Everything is B+" is rating inflation that destroys decision-grade signal.

### The mediocrity-shun bar

DD-stage threshold for concentrated long position: composite Master Rating B-/C+ minimum. C/D composite cases should not be in concentrated 5-15 position book.

### Counter-hypothesis is structural

For every rating + judgement, the analyst must engage with the strongest counter to their view. Engaged + rejected with reasoning ≠ engaged + ignored. This discipline prevents confirmation bias from compounding through the case.

### Multiple-truths is structural

HTRO is BOTH a structurally inferior business model (sub-scale, no glass integration) AND has genuine pockets of competitive advantage (HE specialty, DC services). Both are simultaneously true. The case must hold both — collapsing them into a uniform judgement loses signal.

### Position-sizing is entry-price-sensitive

The HTRO V4 work showed that the entry-price discipline matters more than typical. At SEK 39.86, HTRO is a moderate position. At SEK 22-25, it would be a higher-conviction position. The asymmetry math is sensitive to entry; the SOP recommendation should reflect this.

### 10 ACHs are pre-commitment selling discipline

Don't wait until "the case is broken" to sell. Pre-commit to specific quantitative triggers at investment-decision time. When triggered, act per protocol — don't re-rationalise.

---

## §4 — VALIDATION + CALIBRATION

### How to know if the SOP worked

The SOP worked if:
1. The Park / Progress / Kill recommendation aligns with subsequent SP performance over 18-36 months (Pillar III monitoring confirms outcomes)
2. The 10 ACHs trigger BEFORE the case meaningfully breaks (early warning, not lagging)
3. The Master Ratings hold up to peer benchmarking (top-decile-rated stocks outperform; bottom-decile-rated stocks underperform)
4. The position-sizing recommendations match Richard's portfolio construction discipline

### Lessons from HTRO test (V1→V4)

**Lesson 1:** Phase 0.3 (existing inputs hunt) is non-negotiable. V3 missed it, V4 corrected. SOP now codifies as Phase 0.3.

**Lesson 2:** Word count is not the right metric for depth. V3 at 51k words was structurally rigorous but anchored on wrong inputs. V4 at 5k words was correct on verified data. Verification > volume.

**Lesson 3:** The Pillar I/II/III + BB#2 quadruple-weight + Master Ratings + 3-Check framework holds. Architecture validated.

**Lesson 4:** External validation matters. The Fjord Alpha analyst BUY at SEK 95 PT for 2031 was independent confirmation of V4's framing. Always seek 1-2 external triangulation points.

**Lesson 5:** Peer multiples drift fast. Training-data approximations (Prysmian 8.5x in V3) can be 50-100%+ off current verified figures (15.0x in V4). Web-verify peer multiples every time.

**Lesson 6:** Richard's existing model is one input among several. Not every sheet is HTRO-specific (some are template content). Apply judgement.

### Future SOP iterations

V1 (this document) is the first standing version. Subsequent versions should incorporate lessons from second-stock validation (Step 6 in the Workstream 1 plan, currently DEFERRED).

