---
name: Earnings Upgrade Cycle — Consensus-Gap Quantification Rule
tier: bronze
category: situational/simple-patterns
keywords: [earnings-upgrade-cycle, consensus-gap, sell-side-revisions, gap-closing, prysmian, monitoring-discipline]
cross_references: [right-to-left-thinking, peer-and-base-rate-anchoring]
authors: [Watson]
created: 2026-05-03
last_updated: 2026-05-03
updated_by: APM
---

# Earnings Upgrade Cycle — Consensus-Gap Quantification Rule

## Definition

In a clean Earnings Upgrade Cycle case (one of Richard's 4 setup patterns), the key quantitative discipline at ESA is to **explicitly quantify the gap** between management guidance and consensus estimates. The gap should be expressed as a percentage on the most-relevant medium-term metric (e.g., FY28 EBITDA). Without quantification, the case is qualitative and un-trackable. WITH quantification, you have a concrete monitoring metric AND an explicit entry/exit trigger.

## Why It Matters

Earnings Upgrade Cycle cases die from "we knew the gap existed but couldn't size it." The qualitative version of the case ("consensus is too low") sounds compelling but doesn't translate into operational discipline:
- No explicit monitoring metric
- No clear catalyst trigger
- No way to track the thesis playing out vs failing

The QUANTIFIED version of the case ("consensus is 8-12% below management guidance on FY28 EBITDA, expected to close upward by H2 2026") is operationally tractable:
- Track quarterly consensus revisions toward management guidance (visible via FactSet SSEM)
- Explicit trigger: if gap closes >50%, thesis is playing out (size up); if gap widens >20%, thesis is breaking (sizedown or exit)
- Specific catalyst dates: each quarterly print is a discrete data point on gap trajectory

## Application

When evaluating an Earnings Upgrade Cycle case at ESA:

1. Identify management's stated medium-term guidance (typically CMD or annual report — quantitative)
2. Pull current consensus estimates for the SAME metric, SAME year
3. Compute the gap as percentage
4. Test gap-closing direction probability:
   - Gap likely closes UP (consensus revises to management): if FY-1 actuals tracking ≥ guidance, no major one-off concerns
   - Gap likely closes DOWN (management walks back to consensus): if FY-1 actuals lagging guidance, capacity overhang, or confidence-event risks
   - Gap holds: if the case is cyclical and uncertain
5. Document the quantification in the memo (P5 SS Momentum analysis + IC#1 Outputs framing)
6. Add the quarterly gap as a TI (Trackable Indicator) in E.II.1 monitoring plan
7. Set explicit triggers for size-up / size-down based on gap trajectory

For PRY: 8-12% gap on FY28 EBITDA quantified at ESA. Direction probability: 60% close-up, 25% holds, 15% close-down. Monitoring: FY28 EBITDA consensus tracked quarterly via FactSet SSEM.

## Examples from Track Record

- **PRY (May-26):** ESA quantified consensus-vs-management gap at 8-12% on FY28 EBITDA. Bull thesis: gap closes upward as backlog converts to revenue. Trigger thresholds set for monitoring. PRY ESA GNG CHECKS Q2 explicitly probes this question.
- **Counter-pattern (training reference):** Cases where management guidance is qualitative ("positive growth") with no quantitative number — gap quantification impossible. APM should flag this as a guidance-credibility issue (BB#3 downgrade) rather than treating it as a clean Earnings Upgrade Cycle.

## Boundary Conditions

- Requires management to provide quantitative medium-term guidance (some companies deliberately avoid; CMD-cycle companies usually do)
- Consensus estimates need at least 5+ analyst coverage for the gap to be statistically meaningful (single-analyst targets are noisy)
- Gap quantification is most useful at 12-24 month horizons; short-horizon gaps (next quarter) have too much noise
- COMET (May-26) had thin SS coverage — gap quantification was un-actionable due to coverage gap, not absence of management guidance. The pattern requires BOTH sides (management + sell-side) to be quantitative

## Cross-References

- `right-to-left-thinking` (Gold) — the gap closure flows EBIT → EPS → multiple via specific transmission
- `peer-and-base-rate-anchoring` (Gold) — peer base-rates inform gap-closing direction probability
- AJ SOP v2.2 §Phase 2 P5 SS Earnings Momentum content scaffold + Phase 3 D.II.1 monitoring trigger discipline

## Change Log

- 2026-05-03 | APM | Created at Bronze tier from PRY ESA work. Should generalise across most Earnings Upgrade Cycle cases. Promote to Silver with 1-2 more cases (CARLB at DD may qualify).
