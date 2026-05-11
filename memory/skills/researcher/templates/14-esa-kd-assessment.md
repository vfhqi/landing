# Query 14: Watson KD Assessment — ESA — AS + C (dual-source)

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/14-esa-kd-assessment.md`. Standard v2.1 pattern. NO BB#2 overlay (Q14 is driver-deep-dive at ESA depth). 5L SS breadth gate applies. Dual-source [AS]+[C]. **DORMANT-APM-INPUT MODE per D-RSR-31 (locked 06-May-26 PM):** the APM memo structure does NOT yet have a discrete simplified-KDs + key-concerns/issues block for Q14 to consume. Watson INFERS the driver list from prior Triaging research (Q4-Q7) + general thesis context. The `apm_kd_summary_inferred: true` bypass is the DEFAULT mode (not exception). When APM memo gets the discrete KD-input block built (TODO future), re-amend per D-RSR-31 part 1.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Reader has read Q1 IG BD. Start directly with the KD-deep-dive analysis.

---

## MISSION

**Targeted deep-dive assessment** of Key Drivers (KDs) identified by the APM role in ESA Pass 1 for {TICKER} ({COMPANY}). Provide the APM with evidence-rich material to refine or stress-test judgement on which drivers are truly fulcrum-level and how they're tracking.

Output: comprehensive memo, target {WORD_TARGET} words (default ~6,000-7,500w under v2.1 density doctrine — deeper than Q7 because per-driver depth at ESA is higher than Triaging; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. **Per-driver structure: each APM-flagged driver gets its own dedicated section with bull case + bear case + forward trajectory + plausibility verdict.** Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section.

---

## CONTEXT — What the Reader Cares About

**Audience:** Richard Black, concentrated long-only equity investor (5-15 positions), UK/European focus, $5-50bn market cap. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**ESA Purpose & Sequencing:** Q14 runs in **ESA Pass 2 — AFTER the APM role has completed FCS Analysis & Judgement and posted it to Notion.** The workflow:

1. **Triaging (Stage 2):** Rapid-fire assessment. RESEARCHER posts 8 Triaging queries. APM reads, applies FCS framework, identifies preliminary KDs and risks.
2. **ESA Pass 1:** APM runs FCS Analysis & Judgement (ratings across 5 Pillars and 13 Categories), identifies most critical KDs and evidence gaps, defines preliminary setup classification, flags open questions.
3. **ESA Pass 2 (Q14):** RESEARCHER runs targeted deep-dive on specific KDs the APM flagged, providing evidence-rich material that supports or challenges APM's preliminary judgement.
4. **ESA Pass 3:** APM reviews Q14 evidence, refines judgement, finalises setup classification + FCS ratings.

**This is NOT a general KD assessment like Triaging Q7.** Q14 is a **TARGETED deep-dive on the specific drivers the APM flagged** — informed by `{APM_KD_SUMMARY}`.

**Key Driver definition** (Richard's system): A KD is a financial or operational variable that, if it moves in your assumed direction with the assumed magnitude over your assumed timeframe, validates the investment thesis and drives required IRR. Example: "Unit economics improve 200bps from volume leverage" or "Customer win rate improves from 30% to 45%."

**Fulcrum-level drivers** are the 2-3 KDs where the case is MOST sensitive: if they go right, thesis works at required IRR; if they go wrong, thesis breaks. Q14's job is to test whether APM's fulcrum hypothesis holds up under deep-dive evidence.

**What downstream uses this output:** APM Pass 3 reads this memo to refine FCS ratings and finalise setup classification. APM uses Q14's per-driver verdicts to confirm or revise which drivers are fulcrum-level. Memo also surfaces on the RESEARCH STAGES dashboard tab. Q14 is the ESA-depth analogue of Q7 (Triaging KD assessment).

**Mental models:** Targeted deep-dive, fulcrum-level identification, evidence-weight bias, bear-case stress-testing, forward trajectory probability assessment.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in SECTIONS TO COVER must be addressed substantively per driver. The bulleted format constrains the *shape* of output, not its *depth*.

**Per-driver depth (ESA-level):** Each APM-flagged driver gets dedicated treatment with bull case + bear case + forward trajectory + sell-side expectations + evidence gaps + plausibility verdict. Don't skimp on the per-driver detail — this memo is the centre of gravity for ESA-stage KD judgement.

If in doubt, write more substantive bullets rather than longer ones. Tilt sceptical: assume APM-Pass-1 hypothesis is biased toward optimism; Q14's job is to stress-test.

**The test:** would the APM learn something about each driver from this memo that they couldn't get from re-reading Q4-Q7 + Q9-Q13? If the bullet just restates Triaging-level commentary, it's filler. If it triangulates historical precedent + competitive benchmark + management track record + sell-side dispersion + sensitivity analysis to surface a non-obvious plausibility judgement — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1.
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.**
- **One analytical dimension per bullet.**
- **Signpost prefixes** (demi-bold + colon) on every parent bullet. SIGNPOST DISCRETION clause applies.
- **Peer / base-rate anchor** on every quantitative claim.
- **J-front verdict bullet** at top of every section. NOT a grade.
- **Per-driver plausibility verdict** at end of each driver section — verbal high plausibility / medium plausibility / low plausibility (NOT a grade — D-RSR-3 enforced).
- **Per-section sceptical bullet** at bottom of every section. Open-framed.
- **IAJA suffix tags:** `[#J]` / `[#A]` / `[#I]`.
- **❌ inversion marker** on driver weaknesses.
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (e.g. unique driver dependency, unusual evidence gap; concentration of risk in a single driver in top/bottom 5% of cohort), (b) deliberately-weird signals (drivers the operator hasn't named, drivers with unexplainably thin evidence, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo.
- **Inline highlights** (green/yellow/red phrase-level spans).

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Three guardrails: (1) canonical first, (2) ≤4 words demi-bold + colon, (3) single analytical dimension.

### Memo skeleton

```
1. METADATA HEADER (incl. {APM_KD_SUMMARY} reference)
2. KEY FINDINGS (BLUF) — 5-10 parent bullets
3. §1 Executive Summary — APM Pass 1 reference + Q14 verdict overview
4. §2-§N Per-Driver Sections (one per APM-flagged driver, typically 5-8 drivers)
5. §N+1 Cross-Driver Interactions
6. §N+2 Fulcrum-Level Synthesis + Setup Classification Refinement
7. §N+3 Watson Back-Brief for APM Pass 3 (LOAD-BEARING)
8. §N+4 Sceptical Synthesis (cross-cutting bear case)
9. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
10. AGGREGATE OUTLIERS (⚡)
11. QC AUDIT PANEL (validator-filled)
12. QC COMMENTARY (RESEARCHER-authored)
13. QC FOOTER
```

---

## SECTIONS TO COVER

### §1 — Executive Summary (Watson driver inference + verdict overview)

**Open with J-front verdict bullet:** Net signal on Watson's inferred driver landscape — load-bearing fulcrum candidates + setup archetype hypothesis — ≤30w.

**Canonical signpost vocabulary:** "Inferred driver count:", "Inferred fulcrum candidate:", "Setup hypothesis:", "Driver-by-driver — verdict:", "Plausibility distribution:", "Setup classification — Watson view:", "HQI:", "BFF:", "Earnings Turnaround:", "Operational Inflection:", "Capital Allocation:", "Open questions for APM Pass 3:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Watson's inferred driver list (5-8 drivers): names + suspected fulcrum-level + evidence-gap context. Drawn from prior Triaging Q4-Q7 + general thesis context (Q1, Q2) + any ESA priors already shipped (Q8, Q9, Q10, Q13).
- For each inferred driver, summarise Q14's verdict: high plausibility / medium plausibility / low plausibility (verbal, NOT graded — see §2-§N per-driver sections for detail).
- Setup classification — Watson's view: which setup archetype best fits the driver landscape? (HQI / BFF / Earnings Turnaround / Operational Inflection / Capital Allocation / Other.)
- Open questions remaining for APM Pass 3: which driver-level evidence gaps remain? Which judgements does Watson recommend APM scrutinise most?

**Coverage:** 8-12 parent bullets + sub-bullets. Mandatory: driver-verdict summary table (driver × Watson verdict × plausibility × fulcrum-candidate-status).

**End with sceptical bullet:** "What might invalidate Watson's inferred driver list? Through what mechanism might APM Pass 3 reach a materially different driver set than Watson inferred?"

**Note — Dormant-APM-input mode (D-RSR-31):** Q14 currently runs WITHOUT APM Pass 1 input — `{APM_KD_SUMMARY}` is unpopulated, `apm_kd_summary_inferred: true` bypass active. Watson infers drivers from prior research instead. When the APM memo gets a discrete simplified-KDs + key-concerns/issues block built, this section will be re-amended to consume APM input directly per D-RSR-31 part 1.

---

### §2-§N — Per-Driver Sections (one section per APM-flagged driver, typically 5-8 drivers)

For each APM-flagged driver, provide a **dedicated section** with the structure below. Section heading: "§N — Key Driver: {Driver Name}".

**Open with J-front verdict bullet:** Net signal on this driver's plausibility + how it differs from APM Pass 1 hypothesis — ≤30w.

**Canonical signpost vocabulary (per driver):** "Driver definition:", "Magnitude required:", "Baseline:", "Target state:", "Required trajectory:", "Bull — historical:", "Bull — recent:", "Bull — mgmt:", "Bull — competitive:", "Bull — SS:", "Bull — industry:", "Bull — initiatives:", "Bear — historical drag:", "Bear — recent deterioration:", "Bear — execution:", "Bear — competitive pressure:", "Bear — macro:", "Bear — structural:", "Bear — SS skeptic:", "Quarterly trajectory:", "Acceleration needed:", "Probability — verbal:", "Key dependency:", "Downside scenario:", "Consensus alignment:", "Estimate revision:", "Evidence gap:". Invent where pattern warrants.

**Analytical sub-questions to address per driver:**

**Define the driver precisely:**
- Statement of the driver: "Gross margin expands from 42% to 47% over N24M".
- Why material to the case? (Contribution to required IRR.)
- Baseline / current state: where is this metric today?
- Target state: what's the level required in 18-24 months for the case to work?
- Required trajectory: what's the quarterly/annual progression needed?

**Bull case (current evidence supporting driver):**
- Historical precedent: similar improvements achieved before? Quantify.
- Recent trends: metric already moving right? (Last 2-4 quarters.)
- Management commentary: confidence, initiatives, timelines.
- Competitive comparisons: vs {PEERS} — upside potential?
- Sell-side consensus: are analysts assuming improvement?
- Industry tailwinds: trends supporting improvement?
- Company initiatives: specific actions being taken?

**Bear case (current evidence challenging driver):**
- Historical drag: similar improvements that fell short? What went wrong?
- Recent deterioration: metric flat or deteriorating?
- Management execution risk: track record of delivering similar initiatives?
- Competitive pressure: competitors working against {COMPANY}?
- Macro headwinds: industry / macro conditions against improvement?
- Structural constraints: factors preventing improvement? (Capital intensity, concentration, etc.)
- Sell-side skepticism: any analysts skeptical?

**Forward trajectory — 18-24M plausibility:**
- Implied quarterly/annual improvement rate to reach target.
- Current trajectory: recent trend rate of change.
- Acceleration needed vs recent trend.
- Risk / probability — verbal high plausibility / medium plausibility / low plausibility (NOT a grade).
- Key dependencies: what must happen?
- Downside scenario: if improvement stalls/reverses, EPS impact?

**Sell-side & management expectations:**
- SS consensus assumption on this driver — improvement assumed over N24M.
- Compare to APM's assumed driver: is consensus more or less bullish than case assumption?
- Management guidance alignment.
- Estimate revisions L12M.
- Consensus dispersion.

**Evidence gaps:**
- APM-flagged gaps (from `{APM_KD_SUMMARY}`).
- Q14-identified gaps: what additional evidence would strengthen / weaken confidence?
- Specific items APM should investigate further at Pass 3.

**Coverage per driver:** 18-25 parent bullets + sub-bullets per driver. Each driver section ends with verbal plausibility verdict.

**End each driver section with:** "Plausibility verdict: high plausibility / medium plausibility / low plausibility — verbal verdict, ≤30w, NOT a grade. Fulcrum-level vs APM Pass 1: VALIDATES / REVISES / CHALLENGES."

---

### §N+1 — Cross-Driver Interactions + ACH (Heuer's Analysis of Competing Hypotheses)

**Open with J-front verdict bullet:** Net signal on driver dependencies + correlation across the driver set, AND the ACH-survivor hypothesis (the cross-driver hypothesis with FEWEST hard inconsistencies) — ≤30w.

**Canonical signpost vocabulary:** "Driver A → Driver B:", "Independent drivers:", "Correlated drivers:", "Sequential dependency:", "Parallel dependency:", "Joint probability:", "Compound risk:", "Conditional driver:", "ACH hypothesis:", "ACH survivor:", "Disconfirming evidence:", "Diagnostic evidence:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Cross-driver dependencies: do drivers depend on each other? If driver A fails, does driver B also fail?
- Correlation across drivers: are they independent (5-8 independent positive bets) or correlated (one event hits multiple)?
- Joint probability assessment: if each driver is X% likely independently, what's the joint probability of all delivering?
- Sequential vs parallel dependencies.
- Conditional drivers: any drivers that only matter IF another driver delivers?

**ACH structure (NEW per D-RSR-33 — load-bearing for Q14):**

Apply Heuer's Analysis of Competing Hypotheses across the driver set. Required artefacts:

1. **Enumerate ≥3 competing cross-driver hypotheses** (mutually exclusive, collectively exhaustive). Examples for a 5-driver thesis: (a) "All 5 deliver — bull case fully realises"; (b) "Top 2 drivers deliver, bottom 3 underwhelm — partial-bull thin-margin case"; (c) "Top 1 + bottom 1 deliver, middle 3 underwhelm — flat-to-modest case"; (d) "Correlated failure — 1 fails, 2-3 cascade — bear case"; (e) "Setup classification was wrong — drivers reflect a different archetype".

2. **For each hypothesis, identify ≥1 piece of disconfirming evidence** that would invalidate it. The ACH winner is the hypothesis with the FEWEST hard inconsistencies — NOT the one with the most supporting evidence. (Per `analysis-of-competing-hypotheses-heuer` Wisdom Library Gold entry.)

3. **Identify diagnostic evidence** — the items that discriminate hardest between hypotheses. Flag what additional data-gathering would most efficiently kill one or more hypotheses. This becomes the priority list for any DD-stage follow-up.

4. **State the ACH survivor explicitly** — the hypothesis that has fewest disconfirming items as of this memo. This is the leading hypothesis. "Strong views, weakly held" — the survivor is updateable as new evidence arrives.

5. **Cross-cut with means/motive/opportunity for any operator-driven driver.** If a driver depends on management action (capital allocation, capex pacing, ROIC discipline), apply M/M/O — does the operator have means + motive + opportunity to deliver?

**Coverage:** 10-14 parent bullets + sub-bullets (was 8-12 — raised to accommodate ACH structure).

**End with sceptical bullet:** "What's the bearish read on driver interactions? Through what mechanism might driver correlations prove higher than apparent? Which competing hypothesis has the LEAST disconfirming evidence — and is that hypothesis the leading view, or is it being filtered out by anchoring on a more comfortable narrative?"

---

### §N+2 — Fulcrum-Level Synthesis + Setup Classification Refinement

**Open with J-front verdict bullet:** Net signal on which 2-3 drivers are TRUE fulcrum + whether APM's setup hypothesis holds — ≤30w.

**Canonical signpost vocabulary:** "True fulcrum — driver:", "Non-fulcrum — driver:", "APM hypothesis — confirmed:", "APM hypothesis — revised:", "Setup classification — confirmed:", "Setup classification — revised:", "Setup archetype match:", "HQI:", "BFF:", "Earnings Turnaround:", "Operational Inflection:", "Capital Allocation:", "Other archetype:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Which 2-3 drivers are TRULY fulcrum-level (vs APM's Pass 1 hypothesis)?
- Setup classification: does evidence confirm APM's setup hypothesis (HQI / BFF / Earnings Turnaround / etc.)?
- If revising APM's hypothesis: what's the revised setup archetype?
- Which non-fulcrum drivers are still important but not load-bearing?

**Coverage:** 8-12 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on the fulcrum identification? Through what mechanism might the chosen fulcrum drivers prove non-fulcrum (i.e. case still works without them)? Through what mechanism might a non-fulcrum driver actually be fulcrum?"

---

### §N+3 — Watson Back-Brief for APM Pass 3 (LOAD-BEARING)

**Open with J-front verdict bullet:** Net signal on what APM should focus on in Pass 3 + key open items — ≤30w.

**Canonical signpost vocabulary:** "APM action — refine:", "APM action — revise:", "APM action — confirm:", "Open question — driver:", "Open question — assumption:", "Open question — fulcrum:", "Setup classification — final:", "FCS rating implication:", "Risk to monitor:", "Key data point — N3M:", "Key data point — N6M:". Invent where pattern warrants.

**Analytical sub-questions to address (LOAD-BEARING — this is what APM Pass 3 acts on):**
- Watson's back-brief to APM: which Pass-1 judgements should APM refine / revise / confirm in Pass 3?
- Open questions remaining for APM Pass 3: per-driver evidence gaps, setup-classification uncertainties, fulcrum-identification ambiguity.
- FCS rating implications: which Pillars / Categories should APM revisit based on Q14 evidence?
- Risks to monitor going forward: specific data points to track at N3M / N6M / N12M.
- Key triggers for case invalidation: what specific events would cause the case to break?

**Coverage:** 12-18 parent bullets + sub-bullets. This section is the load-bearing artefact APM Pass 3 reads.

**End with sceptical bullet:** "What might Watson have missed in this back-brief? Through what mechanism might APM Pass 3 reach a materially different judgement than Q14's evidence suggests?"

---

### §N+4 — Sceptical Synthesis (cross-cutting)

**Open with J-front verdict bullet:** Cross-cutting bear synthesis — what is the strongest bear case for the APM-flagged driver landscape given everything above? — ≤30w.

**Canonical signpost vocabulary:** "Reverse-engineered bear:", "Single largest case-level risk:", "Stacked driver downside:", "Cumulative miss probability:", "Setup classification — at risk:", "FCS rating — at risk:", "Invalidation trigger:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Reverse-engineer the bear case across all APM-flagged drivers.
- Single largest case-level risk: which scenario most damages the case?
- Stacked downside: if 2-3 drivers miss simultaneously, what's the damage?
- Setup classification at risk: under what evidence would the setup archetype need revision?
- FCS rating at risk: under what evidence would APM's preliminary FCS ratings need downgrades?
- Invalidation triggers: which specific events would prove the case wrong?

**Coverage:** 10-15 parent bullets + sub-bullets.

**End:** No sceptical bullet (whole section is synthesis). Instead end with: "Confidence in case-level thesis post-Q14: high plausibility / medium plausibility / low plausibility — verbal verdict only, ≤30w, NOT a grade."

---

## AGGREGATE BLOCKS

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets.

**Format:** `❌ Signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X driver]`

**Example:** `❌ Driver #3 (margin recovery) — peer median 6 quarters to recovery; {COMPANY} now in quarter 11 of attempted recovery. [Cross-ref: §4]`

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X driver]`

**Example:** `⚡ RARE: Driver #1 (TAM expansion) — implied addressable market 4× sector base rate over N24M; only 2 of 50 European peers face comparable TAM dynamic. [Cross-ref: §2]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel.

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS] / [C] / [C+AS]
**Stage:** ESA Pass 2
**Generated:** DD-Mon-YY
**APM_KD_SUMMARY received:** YES / NO

### Summary
| Metric | Value | Notes |
|---|---|---|
| Word ratio (output / source) | XX.X% | target 40-60%; hard floor 35% |
| H2 sections | N | min 3 required |
| Parent bullets | N | all within 35w ceiling |
| Hard failures | 0 / N | (0 to PASS) |
| Warnings | N | (cosmetic flags) |
| SS breadth ratio | YY% (Y of Z) | Y named brokers cited / Z in AS pool |
| Expert calls cited | N | distinct named expert calls |
| Drivers covered | N | mandatory: matches APM_KD_SUMMARY count (typically 5-8) |

### Gate-by-gate
| Gate | Check | Type | Result |
|---|---|---|---|
| 5A | Word ratio ≥35% | Hard | ✓ / ✗ |
| 5B | ≥3 H2 sections | Hard | ✓ / ✗ |
| 5C | Signpost label consistency | Hard | ✓ / ✗ |
| 5D | Parent bullet length ≤35w | Hard | ✓ / ✗ |
| 5E | IAJA tags ≥90% | Hard | ✓ / ✗ |
| 5F | Signpost labels ≥80% | Hard | ✓ / ✗ |
| 5G | Highlight density ≥25% | Hard | ✓ / ✗ |
| 5H | Underlines on ≥50% of parents | Warn | ✓ / ~ / ✗ |
| 5I | Em-dashes = 0 | Hard | ✓ / ✗ |
| 5J | No trailing periods on bullets | Hard | ✓ / ✗ |
| 5K | Structure sanity | Hard | ✓ / ✗ |
| 5L | SS breadth ratio ≥40% | Hard | ✓ / ~ / ✗ |
| 5M | Expert call breadth — count + named | Warn | informational |
| Q14-APM | APM_KD_SUMMARY present in metadata + driver count matches | Hard | ✓ / ✗ |
| Q14-DC | Per-driver section per APM-flagged driver (typically 5-8) | Hard | ✓ / ✗ |
| Q14-PV | Per-driver verbal plausibility verdict (high plausibility / medium plausibility / low plausibility, NOT graded) | Hard | ✓ / ✗ |
| Q14-BB | Watson Back-Brief section (§N+3) present | Hard | ✓ / ✗ |

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text}
- `apm_kd_summary_inferred: true` — reason: {free text} — if APM_KD_SUMMARY missing and Q14 inferred drivers from prior research

### Warnings (if any)
- {Gate}: {one-line description}
```

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say.

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired}
- **Source breadth note:** {≤30w on SS breadth + expert call breadth — STRICTLY separated}
- **APM Pass-1 alignment:** {≤30w on whether Q14 evidence broadly supports / revises / challenges APM Pass 1 hypothesis}
- **Counter-hypothesis check (AI-Dunning-Kruger / ACH spine):** {≤50w stating: leading driver-set view + ≥3 competing cross-driver hypotheses (per §10 ACH structure) + identification of the hypothesis with FEWEST hard inconsistencies. For Q14 specifically, the cross-driver ACH IS structurally load-bearing. If you can't enumerate ≥3 competing hypotheses with disconfirming evidence each, the memo isn't done.}
```

### Authoring rules

1. **4-5 bullets, each ≤30 words (Counter-hypothesis check ≤50w for Q14 due to cross-driver ACH structural spine).**
2. **Signposted with verdict-flavoured labels.** Q14-specific: "APM Pass-1 alignment" replaces generic "Edge case flag" — Q14's central insight is whether evidence confirms or revises APM's preliminary judgement. **Counter-hypothesis check (with ACH framing) is universally mandatory** (D-RSR-33).
3. **Specific not generic.**
4. **Cross-reference the body.**
5. **No A-F or R/O/Y/G grades.**
6. **STRICTLY separate SS and expert call counts.**
7. **No empty restating.**

---

## SOURCE-SPECIFIC DELTA — [AS] version

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

Before extracting any content, perform this pre-flight check:

1. **Query AS for SS pool size:** "How many sell-side analysts in the AlphaSense library currently cover {COMPANY} ({TICKER})? List the broker names." Record this as the AS pool size `Z` and the broker name list.

2. **Consult the FULL pool, not a subset.** Do NOT default to citing one or two preferred brokers. For Q14, breadth across SS pool is critical — different analysts will have different views on each driver. Where a broker has no relevant driver-level coverage, note that explicitly.

3. **Name each broker cited.** Format: "[AS-Berenberg]" or "[AS-Citi]" prefix.

4. **Strict separation from expert calls.** Mark expert calls as `[AS-Expert]`. Q14 expert-call usage often valuable — sector experts on driver-specific topics.

5. **Output the breadth metadata at memo-end.** metadata.json contains: `ss_pool_size` (Z), `ss_brokers_cited` (list), `expert_calls_cited` (list), `expert_call_count` (integer).

**Why this matters:** Q14's per-driver evidence assessment requires per-driver SS commentary. Citing only 2 of 8 brokers misses 75% of the per-driver analytical landscape APM needs to refine Pass 1 judgement.

**Data sources for [AS] version:**
- AlphaSense expert calls: industry experts on driver-specific topics, former insiders.
- Sell-side research: per-driver analyst commentary, sensitivity analyses, estimate revisions tied to specific drivers.
- Company filings: management commentary on each driver from earnings calls + investor presentations.
- Consensus data: per-driver consensus assumptions where extractable.
- **APM Pass 1 output:** read APM's FCS Analysis & Judgement memo from Notion as primary input context.

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: per-driver searches based on `{APM_KD_SUMMARY}`.
- Read APM Pass 1 output for {TICKER} as primary input context.
- Read prior Triaging memos (Q4-Q7) for {TICKER} as supporting context.
- Read `notion-posting-sop.md` before posting.
- Post to Notion Stock Notes with `[AS]` tag and date.

---

## SOURCE-SPECIFIC DELTA — [C] version

**Data sources for [C] version:**
- WebSearch — per-driver public sources (filings, presentations, press releases, news, industry reports).
- Public competitor information — peer driver-level performance.
- Industry consultant reports — driver-specific industry views.
- **APM Pass 1 output:** read APM's FCS Analysis & Judgement memo from Notion as primary input context.

**[C]-specific analytical lens:** WebSearch reaches public driver-level material. [C] does NOT have AS expert calls or proprietary sell-side. Compensates via deeper public-source synthesis. Where [C] cannot source per-driver SS dispersion that [AS] would have, flag with `quality_flag: thin_peer_context`.

**Execution:**
- Use WebSearch extensively per driver.
- Search terms per driver: `"{COMPANY} {DRIVER_NAME} delivery"`, `"{INDUSTRY} {DRIVER_NAME} peer benchmark"`, `"{COMPANY} {DRIVER_NAME} guidance"`.
- Read APM Pass 1 output as primary context.
- Read prior Triaging Q4-Q7 memos as supporting context.
- Do NOT include footnotes/endnotes/links in final memo.
- Post to Notion Stock Notes with `[C]` tag and date.

---

## VALIDATION GATES (auto-applied at post time)

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1 + per-driver + §N+1, §N+2, §N+3, §N+4 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (each section incl. each per-driver section) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **Q14-APM — APM_KD_SUMMARY present + driver count matches** | hard | BLOCK post (or `apm_kd_summary_inferred: true` bypass with reason) |
| **Q14-DC — Per-driver section per APM-flagged driver** | hard | BLOCK post |
| **Q14-PV — Per-driver verbal plausibility verdict (high plausibility / medium plausibility / low plausibility)** | hard | BLOCK post |
| **Q14-BB — Watson Back-Brief section present** | hard | BLOCK post |
| **SS breadth ratio (5L) ≥40%** | hard floor | BLOCK or regenerate |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS/web returns thin source material per driver, word-count gate bypasses; structural gates still apply. `apm_kd_summary_inferred: true` — when APM Pass 1 output unavailable, Watson infers driver list from prior research; document reason.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

- [ ] Mission compass clear: have I conducted targeted deep-dive on each APM-flagged driver?
- [ ] Reader priorities applied: 18M-3Y EPS trajectory + 25% IRR potential.
- [ ] APM_KD_SUMMARY received and reflected: driver list + suspected fulcrum + evidence gaps + setup hypothesis + open questions.
- [ ] Per-driver structure: each APM-flagged driver gets dedicated section (typically 5-8 sections).
- [ ] Each per-driver section ends with verbal plausibility verdict (high plausibility / medium plausibility / low plausibility — NOT a grade) + fulcrum-status (VALIDATES/REVISES/CHALLENGES APM).
- [ ] §N+1 Cross-driver interactions, §N+2 Fulcrum synthesis, §N+3 Watson Back-Brief for APM Pass 3, §N+4 Sceptical synthesis ALL present.
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs.
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to driver sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Mandatory driver-verdict summary table (§1).
- [ ] AS pool size Z queried + recorded.
- [ ] Distinct named SS brokers cited (Y); ratio Y/Z computed; gate result recorded.
- [ ] Expert calls counted SEPARATELY (no conflation with SS).
- [ ] Prior Triaging Q4-Q7 memos read as supporting context.
- [ ] APM Pass 1 output read as primary input context.
- [ ] metadata.json written.
- [ ] In-memo QC Audit panel rendered (validator-filled).
- [ ] Qualitative QC Commentary block authored — Q14-specific "APM Pass-1 alignment" note.
- [ ] Sceptical synthesis in §N+4 actually synthesises — doesn't restate per-driver bears.

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Watson KD Assessment — ESA [AS or C] @ DD-Mon-YY`
Tags: `#ESA #KeyDrivers #FulcrumIdentification #ESAPass2`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only.

---

## EXECUTION

**Dual-source query.** Both versions run:
- [AS] version → submitted to AlphaSense Deep Research by Haiku agent.
- [C] version → executed natively by Sonnet sub-agent using WebSearch.

**Required input from APM Pass 1:** `{APM_KD_SUMMARY}` placeholder MUST be populated by parent RESEARCHER with structured summary of APM's Pass 1 findings. If unavailable, use `apm_kd_summary_inferred: true` bypass with reason.

Parent RESEARCHER handles extraction, highlighting, formatting, and Notion posting for both outputs.

---

*End of Q14 ESA KD Assessment — AFTER v1 draft (v2.1 pattern, 5L applies, dual-source, per-driver structure with Q14-APM/Q14-DC/Q14-PV/Q14-BB gates). Awaiting Richard's review with Q13 in BATCH 3.*
