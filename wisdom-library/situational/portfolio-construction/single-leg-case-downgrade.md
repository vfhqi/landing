---
name: Single-Leg Case Downgrade Rule
tier: silver
category: situational/portfolio-construction
keywords: [investment-case, multi-setup, fulcrum-narrowing, conviction-downgrade, leg-collapse, optionality-loss, ekta]
cross_references: [stage-gating-bidirectionality, fulcrum-narrowing-pattern, judgement-importance-weighted-escalation]
authors: [Richard, Watson]
created: 2026-05-03
last_updated: 2026-05-03
updated_by: APM
---

# Single-Leg Case Downgrade Rule

## Definition

Per Richard's investing approach (4-pattern framework + investment-case Building Blocks), a case that started at Triaging as a **multi-leg setup** (e.g., Corporate Change + Product Cycle, or Earnings Upgrade Cycle + M&A-Driven EPSU) and **reduces to a single-leg setup at deeper analysis** is a candidate for **automatic conviction downgrade**, not a case-by-case judgement.

**The rule:** A one-setup case at C-conviction does not cross the entry bar UNLESS the one remaining setup is itself an A or B grade. This is a CASE-LEVEL rule independent of per-pillar ratings.

## Why It Matters

Bull cases often have load-bearing diversification across setups — the bull thesis works because EITHER leg succeeds; both succeeding is upside. When one leg compromises (Product Cycle leg threatened by competitive event; M&A leg compromised by Weterings-style cockroach), the standard reaction is to "shift weight to the remaining leg" or "treat the surviving leg as the new fulcrum."

This usually under-prices what was lost: the OPTIONALITY of the diversified case. A single-leg case requires that ONE leg to deliver on its own — much higher bar than a two-leg case where either leg can carry.

The rule forces explicit recognition: when a multi-leg case reduces to single-leg, conviction should drop a grade (not stay flat by re-weighting), unless the surviving leg is genuinely best-in-class.

## Application

At each stage gate (Triaging → ESA → DD), test whether the case structure has changed:

1. List the original setup legs (typically 2-3 at Triaging — Corporate Change EPSU/EPT + Product Cycle, etc.)
2. Test each leg at the deeper stage's evidence depth
3. If any leg is materially compromised (downgraded from B/A to C/D, or loses its independence): mark the case as **leg-collapsing**
4. Apply the downgrade:
   - 2-leg → 1-leg: downgrade conviction one grade (B → C, C → D)
   - 3-leg → 2-leg: downgrade half a grade (note carefully)
   - 3-leg → 1-leg: downgrade a full grade
5. Override only if the surviving leg is rated A or B (best-in-class evidence reinforced by multiple independent signals — per AJ SOP §Judgement doctrine)

## Examples from Track Record

- **EKTA (May-26):** Triaging two-setup case (Corporate Change EPSU/EPT + Product Cycle EPSU). ESA found Product Cycle leg compromised (Evo FY27/28 not FY26/27 + Varian Sept-26 + R&D cap unwinding). Cases reduced to single-leg (Corporate Change only). Per the rule: conviction stays C (cannot upgrade) but bias deteriorates; recommendation flipped from PROGRESS to PARK because Corporate Change leg is B-grade execution but C-grade outcome (cost cuts insufficient solo).
- **HTRO (May-26):** Started multi-leg at Triaging (DC scaling + BEAD + HE defence). ESA confirmed all 3 legs intact + 1 NEW concern (Weterings cockroach as cross-cutting M&A risk). Did NOT trigger the rule because no leg collapsed. Recommendation stayed PROGRESS-to-DD with cockroach watch.

The contrast (EKTA triggered the rule, HTRO did not) is the diagnostic case.

## Boundary Conditions

- "Leg collapse" is a binary judgement — partial degradation doesn't count. A leg goes from "credible source of alpha" to "no longer source of alpha" or remains intact.
- If a leg collapse is REPLACED by a new leg discovered at the deeper stage (e.g., a NEW Optionality emerges that wasn't visible at Triaging), no downgrade — net leg count unchanged.
- The rule applies stage-by-stage. Triaging→ESA leg collapse triggers ESA-stage downgrade; ESA→DD leg collapse triggers DD-stage downgrade; multiple stage-collapses compound.

## Cross-References

- `stage-gating-bidirectionality` (Bronze) — the parent rule that conviction can move down at deeper stages
- `fulcrum-narrowing-pattern` (Bronze) — the pattern that sets up leg collapses
- `judgement-importance-weighted-escalation` (referenced in AJ SOP v2.2 §Phase 3) — case-level rating belongs to Richard at Step 4
- AJ SOP v2.2 §Phase 3 Judgement-importance-weighted escalation
- richard-investing-approach.md §4 patterns + investment-case framework

## Change Log

- 2026-05-03 | APM | Created at Silver tier from EKTA ESA work. Clean rule with clear formulation; generalises across multi-setup cases. Co-authored with Richard's investing approach as conceptual source.
