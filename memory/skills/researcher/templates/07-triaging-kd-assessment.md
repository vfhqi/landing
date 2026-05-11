# Query 7: Watson's Assessment of Key Drivers — Triaging Stage

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/07-triaging-kd-assessment.md`. Standard v2.1 pattern. NO BB#2 overlay (Q7 is driver-focused, synthesises Q4-Q6 into 5-8 KDs). 5L SS breadth gate + 5M expert gate apply.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Reader has read Q1 IG BD. Start directly with KD synthesis.

---

## MISSION

Identify and evaluate **5-8 most important share price drivers** for {TICKER} ({COMPANY}) over next 24 months. Assess plausibility of delivery against management guidance and sell-side expectations. Integrate L12M reporting performance, guidance changes, and macro context. **This is Watson's FIRST-PASS hypothesis on key drivers** — standalone analysis based on prior Triaging research output (Queries 4-6: Peer Comparative Analysis, Earnings Delivery, Sell-Side Commentary).

Output: comprehensive memo, target {WORD_TARGET} words (default ~5,500-6,500w under v2.1 density doctrine; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section. **Per-driver structure: each of the 5-8 drivers gets its own dedicated section.**

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated long-only equity investor (5-15 positions), UK/European focus, $5-50bn market cap. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**Triaging purpose:** Fast, disciplined filtering at LIGHT depth. Does this stock fit a recognisable setup profile? Is the fulcrum driver plausible? Pattern recognition + "strong views, weakly held."

**For this query specifically:** The reader wants Watson's consolidated hypothesis on the key fulcrum drivers. What 5-8 factors will determine {TICKER}'s share price over the next 24 months? How likely are they to be delivered? Is the thesis based on durable fundamentals or dependent on multiple things going right? **This calibrates risk/reward: does the opportunity justify further due diligence (progress to ESA) or should it park?**

**What downstream uses this output:** APM A&J reads this memo as the key input to **fulcrum-driver identification** at Triaging stage. APM uses Watson's KD list to construct the case-level thesis (which drivers are load-bearing, which are nice-to-have). Memo also surfaces on the RESEARCH STAGES dashboard tab. Q14 (ESA KD Assessment) deepens this work after APM Pass 1 input.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in SECTIONS TO COVER must be addressed substantively per driver. The bulleted format constrains the *shape* of output, not its *depth*.

**Per-driver depth:** Each of the 5-8 drivers gets dedicated treatment (definition, company guidance, SS consensus, recent performance, macro context, plausibility, bear case). Don't skimp on the per-driver detail — APM grades fulcrum-status off this analysis.

**Methodology** (applied per-driver):
- Identify each key driver independently — do not assume one drives another.
- For each driver: assess company guidance, sell-side consensus, recent performance, and peer context.
- Evaluate plausibility: is the driver achievable? What are the key assumptions? What could cause it to miss?
- Quantify where possible: EPS impact, revenue impact, multiple expansion.
- Integrate macro/end-market context: are tailwinds fading or accelerating?
- Tilt sceptical: assume management and sell-side are biased toward optimism.
- Fact-check all figures against prior research output (Q4-Q6).

**The test:** would Richard learn something about the driver landscape from this memo that he couldn't get from a sell-side note? If the bullet just restates a sell-side estimate, it's filler. If it triangulates company guidance + SS consensus + recent delivery + peer benchmark + macro context to surface a non-obvious plausibility judgement — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1.
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.**
- **One analytical dimension per bullet.**
- **Signpost prefixes** (demi-bold + colon) on every parent bullet. SIGNPOST DISCRETION clause applies.
- **Peer / base-rate anchor** on every quantitative claim.
- **J-front verdict bullet** at top of every section. NOT a grade.
- **Per-section sceptical bullet** at bottom of every section. Open-framed.
- **Per-driver plausibility verdict** (NOT a grade) — each driver section ends with verbal plausibility verdict ("high plausibility / medium plausibility / low plausibility plausibility based on {key assumption}", ≤30w). No A-F. No R/O/Y/G.
- **IAJA suffix tags:** `[#J]` / `[#A]` / `[#I]`.
- **❌ inversion marker** on weak findings.
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (a driver where the magnitude or evidence-strength is top/bottom 5% vs sector cohort), (b) deliberately-weird signals (drivers the operator hasn't named, drivers whose evidence quality is unexplainably thin, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo.
- **Inline highlights** (green/yellow/red phrase-level spans).

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Three guardrails: (1) canonical first, (2) ≤4 words demi-bold + colon, (3) single analytical dimension.

### Memo skeleton

```
1. METADATA HEADER
2. KEY FINDINGS (BLUF) — 5-10 parent bullets
3. §1 Executive Summary (driver list + ranking + cross-cutting verdict)
4. §2-§9 Per-Driver Sections (5-8 driver-specific sections)
5. §10 Driver Synthesis + Sceptical Synthesis (cross-cutting)
6. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
7. AGGREGATE OUTLIERS (⚡)
8. QC AUDIT PANEL (validator-filled)
9. QC COMMENTARY (RESEARCHER-authored)
10. QC FOOTER
```

---

## SECTIONS TO COVER

### §1 — Executive Summary (driver list + impact ranking)

**Open with J-front verdict bullet:** Net signal on {TICKER}'s driver landscape — high-conviction single-fulcrum setup or multi-variable thesis — ≤30w.

**Canonical signpost vocabulary:** "Driver count:", "Driver list:", "Top driver:", "Impact ranking:", "Single fulcrum:", "Multi-variable:", "Plausibility distribution:", "Single largest risk:", "Consensus alignment:", "L12M trajectory:", "Conviction setup:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- List the 5-8 key drivers, stack-ranked by estimated impact on 24M share price return.
- For each driver: binary assessment = "high plausibility" or "execution risk."
- Summary of key assumptions: what must happen for thesis to work?
- Single largest risk: which driver, if it fails, would most damage the investment case?
- Consensus view on drivers: are sell-side expectations aligned with company guidance?
- Changes in driver expectations over L12M: accelerating or decelerating?
- Overall thesis assessment: is this a "high conviction" setup with 1-2 key drivers, or "multi-variable" requiring many things to go right?

**Coverage:** 8-12 parent bullets + sub-bullets. Mandatory: driver-ranking table (driver × est. impact × plausibility verdict × confidence).

**End with sceptical bullet:** "What might invalidate this driver list? Through what mechanism might a driver omitted from the top 5-8 actually be the dominant fulcrum?"

---

### §2-§9 — Per-Driver Sections (5-8 dedicated sections)

For each of the 5-8 identified drivers, provide a **dedicated section** with the structure below. Section heading: "§N — Key Driver #N: {Driver Name}".

**Open with J-front verdict bullet:** Net signal on this driver's plausibility + impact magnitude — ≤30w.

**Canonical signpost vocabulary (per driver):** "Driver definition:", "Mechanism to EPS:", "Mechanism to SP:", "Company guide:", "Management commentary:", "Track record:", "Conservatism vs optimism:", "SS consensus:", "Bullish analyst:", "Sceptical analyst:", "Estimated EPS impact:", "Estimated revenue impact:", "Recent delivery:", "L3Y baseline:", "Peer benchmark:", "Macro tailwind:", "Macro headwind:", "Visibility:", "Plausibility — H / M / L:", "Bear case:", "Miss scenario:", "Miss magnitude:". Invent where pattern warrants.

**Analytical sub-questions to address (per driver):**

**Definition:**
- What is this driver? How does it drive EPS and share price? Mechanism clarity.

**Company guidance & management view:**
- Explicit or implicit guidance on this driver: what does management say will happen?
- Assumptions embedded in guidance: revenue growth, margin improvement, cost savings, market share.
- Credibility of management view: track record on this type of commitment historically.
- Conservatism vs optimism of guidance: sandbagging or moving targets?

**Sell-side consensus & estimates:**
- What is sell-side consensus on this driver? EPS impact, revenue impact, timing.
- Consensus changes over L1M, L3M, L12M: upgraded or downgraded?
- Which analysts most bullish vs most skeptical on this driver? (Named brokers per D-RSR-19.)
- Estimated financial impact: $ revenue, $ EBIT, % EPS uplift from successful delivery.

**Recent performance & baseline context:**
- How has {COMPANY} performed on this driver historically (last 3 years data)?
- Peer group performance on same driver: is {COMPANY} leading, matching, or lagging?
- Trend in this driver over L3M, L6M, L12M: accelerating, stable, or decelerating?
- Early warning signals: any signs of weakness or strength in recent reporting?

**Macro & end-market context:**
- How dependent is this driver on macro/sector tailwinds? Structural or cyclical?
- End-market health: are conditions supporting or constraining this driver?
- Competitive dynamics: are competitors pursuing same driver? Share of opportunity?
- Visibility & certainty: is this driver largely in management's control or dependent on external factors?

**Plausibility assessment:**
- Verbal plausibility verdict: HIGH (>80%), MEDIUM (50-80%), or LOW (<50%). NOT a grade.
- Key assumptions underpinning plausibility verdict: what must be true?
- What would need to change for delivery to be at risk?
- Magnitude of impact if delivered: % EPS uplift, multiple expansion implication.

**Sceptical / bearish interpretation (per driver):**
- What is the bear case on this driver? Why might it fail?
- Most likely miss scenario: what would cause underperformance vs guidance/consensus?
- Magnitude of impact if this driver misses: % EPS downside, multiple compression.
- Any red flags or warning signals visible in recent data?

**Coverage per driver:** 12-18 parent bullets + sub-bullets per driver. Each driver section gets its own per-driver sceptical bullet at the end.

**End each driver section with:** "Plausibility verdict: high plausibility / medium plausibility / low plausibility — verbal verdict, ≤30w, NOT a grade."

---

### §10 — Driver Synthesis + Sceptical Synthesis (cross-cutting)

**Open with J-front verdict bullet:** Cross-cutting bearish synthesis — what is the strongest bearish case for {TICKER} given all 5-8 drivers? — ≤30w.

**Canonical signpost vocabulary:** "Driver dependency:", "Single-driver risk:", "Multi-driver risk:", "Correlation across drivers:", "Reverse-engineered bear:", "Single largest case-level risk:", "Cumulative plausibility:", "Stacked downside:", "Setup archetype:", "Fulcrum candidate:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Cross-driver dependencies: do drivers depend on each other? If driver #2 fails, does driver #3 also fail?
- Correlation across drivers: are they independent (5-8 independent positive bets) or correlated (one negative event hits multiple)?
- Cumulative plausibility: if each driver is 70% likely independently, what's the joint probability of all delivering? (compound probability framing)
- Setup archetype: does this driver landscape pattern-match a recognisable setup (e.g., "margin recovery + buyback compounder" / "TAM expansion + market share gainer")?
- Reverse-engineer the bear case from analyst commentary + per-driver bear cases.
- Single largest case-level risk: across all drivers, which scenario most damages the case?
- Stacked downside: if 2-3 drivers miss simultaneously, what's the damage?

**Coverage:** 10-15 parent bullets + sub-bullets. This is the dedicated cross-cutting sceptical synthesis.

**End:** No sceptical bullet (whole section is sceptical). Instead end with: "Confidence in case-level thesis: high plausibility / medium plausibility / low plausibility — verbal verdict only, ≤30w, NOT a grade."

---

## AGGREGATE BLOCKS (after §10)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly worse than peer median or driver-specific weakness.

**Format:** `❌ Signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X driver]`

**Example:** `❌ Driver #3 (margin recovery) — peer median 6 quarters to recovery; {TICKER} now in quarter 9 of attempted recovery. [Cross-ref: §4]`

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X driver]`

**Example:** `⚡ RARE: Driver #1 (TAM expansion) — 4× implied addressable market within sector; only 2 of 50 European stocks share comparable TAM dynamic. [Cross-ref: §2]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel. Plain-text-with-markdown. Visual styling owned by SA - Ratings Dashboard project (D-RSR-21).

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS] / [C] / [C+AS]
**Stage:** Triaging
**Generated:** DD-Mon-YY

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
| Driver count | N (5-8 target) | mandatory: 5 minimum, 8 maximum |

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
| Q7-DC | Driver count 5-8 inclusive | Hard | ✓ / ✗ |

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text}

### Warnings (if any)
- {Gate}: {one-line description}
```

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 4-5 free-flowing bullets summarising what the structured numbers say. **Counter-hypothesis check is mandatory** per D-RSR-33 — without it, the memo is not complete.

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired — why and whether they matter}
- **Source breadth note:** {≤30w on SS breadth + expert call breadth — STRICTLY separated}
- **Driver-set composition:** {≤30w on driver count + plausibility distribution + setup archetype}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view + counter-hypothesis + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing.}
```

### Authoring rules

1. **4-5 bullets, each ≤30 words (Counter-hypothesis check ≤40w).**
2. **Signposted with verdict-flavoured labels.** Q7-specific: "Driver-set composition:" replaces generic "Edge case flag:" because the driver-set composition is the load-bearing Q7-specific judgement. **Counter-hypothesis check is universally mandatory** (D-RSR-33).
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

2. **Consult the FULL pool, not a subset.** Do NOT default to citing one or two preferred brokers. Read across every named broker in the AS pool where their research is relevant to key drivers — driver identification, sensitivity, structural vs cyclical, monitoring. Where a broker has no relevant research, note that explicitly.

3. **Name each broker cited.** Format: "[AS-Berenberg]" or "[AS-Citi]" prefix on the bullet, or inline framing.

4. **Strict separation from expert calls.** Mark expert calls as `[AS-Expert]` (with anonymised role/title), never as `[AS-Broker]`.

5. **Output the breadth metadata at memo-end.** Ensure metadata.json contains: `ss_pool_size` (Z), `ss_brokers_cited` (list), `expert_calls_cited` (list), `expert_call_count` (integer).

**Why this matters:** SS gives Watson access to driver assessments, sensitivity analyses, and quantified EPS/revenue impacts that public filings don't surface. Memos that cite "consensus says driver X delivers $Y EPS" while citing only 2 of 8 covering brokers materially distort Richard's read. The 5L gate enforces breadth structurally.

**Data sources for [AS] version:**
- AlphaSense expert calls: most recent earnings call, prior quarter CMDs, sector roundtables.
- Sell-side research: all major analysts covering {TICKER} — driver-specific notes, sensitivity analyses.
- Company filings: most recent results release, investor presentation, prior 3 quarterly/annual filings.
- Consensus data: analyst estimates, rating changes, price target changes L12M.
- **Prior Triaging research output (Q4-Q6):** Read these memos as input — Watson's KD assessment synthesises them.

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: `"{COMPANY} key drivers fulcrum {INDUSTRY} EPS sensitivity guidance"`.
- Secondary searches: per-driver SS commentary, peer benchmark on same drivers, macro context.
- Read prior Q4-Q6 memos for {TICKER} as context input.
- Read `notion-posting-sop.md` before posting to Notion.
- Post to Notion Stock Notes with `[AS]` tag and date.

---

## SOURCE-SPECIFIC DELTA — [C] version

**Data sources for [C] version:**
- WebSearch: company filings, investor presentations, public earnings releases.
- Industry reports + analyst coverage summaries from public sources.
- News + market commentary on driver delivery.
- **Prior Triaging research output (Q4-Q6):** Read these as input.

**[C]-specific analytical lens:** WebSearch surfaces public material. [C] does NOT have access to AS expert calls or proprietary sell-side. Compensate via deeper company filings analysis + broader peer research + creative interpretation of public data. Where [C] cannot source a driver-specific peer-anchor that [AS] would have, flag with `quality_flag: thin_peer_context`.

**Execution:**
- Use WebSearch extensively per driver.
- Search terms per driver: `"{COMPANY} {DRIVER_NAME} guidance"`, `"{COMPANY} {DRIVER_NAME} delivery L12M"`, `"{INDUSTRY} {DRIVER_NAME} peer comparison"`.
- Read prior Q4-Q6 memos for {TICKER} as context input.
- Do NOT include footnotes/endnotes/links in final memo.
- Post to Notion Stock Notes with `[C]` tag and date.

---

## SUPPLEMENTARY QUANTITATIVE CONTEXT (24-Apr-26)

Before writing, check the **Master Dashboard** data files for {TICKER}:
- `master-dashboard/data/factset-ssem.json` — SS estimates revision pattern. Use to calibrate per-driver consensus strength.
- `master-dashboard/data/factset-valuation.json` — P/E percentile. Use to contextualise whether market has priced in driver delivery.

**AlphaSense remains the overwhelming primary source** for the [AS] version. Master Dashboard data is supplementary.

---

## VALIDATION GATES (auto-applied at post time)

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1 + per-driver sections + §10 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (each driver section + §1) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **Driver count between 5 and 8 (Q7-DC gate)** | hard | BLOCK post |
| **Per-driver plausibility verdict (high plausibility / medium plausibility / low plausibility)** | required (verbal, NOT graded) | BLOCK post if missing |
| **Mandatory driver-ranking table (§1)** | required | BLOCK post |
| **SS breadth ratio (5L) ≥40%** | hard floor | BLOCK or regenerate |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS / web returns genuinely thin source material, word-count gate bypasses; structural gates still apply.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

- [ ] Mission compass clear: have I identified 5-8 key drivers and assessed plausibility per driver?
- [ ] Reader priorities applied: 18M-3Y EPS trajectory + 25% IRR potential.
- [ ] §1 Executive Summary present with driver-ranking table.
- [ ] 5-8 per-driver sections present (one section per driver).
- [ ] Each per-driver section ends with verbal plausibility verdict (high plausibility / medium plausibility / low plausibility — NOT a grade).
- [ ] §10 cross-cutting sceptical synthesis present.
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs.
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to driver sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Mandatory driver-ranking table (§1) present.
- [ ] Master Dashboard cross-check done.
- [ ] Prior Q4-Q6 memos read as input context.
- [ ] metadata.json written.
- [ ] Sceptical synthesis in §10 actually synthesises — doesn't restate per-driver bears.
- [ ] AS pool size Z queried and recorded in metadata.json (`ss_pool_size`).
- [ ] Distinct named SS brokers cited (Y); ratio Y/Z computed; `ss_breadth_gate` result recorded.
- [ ] Expert calls counted SEPARATELY (no conflation with SS).
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored — Q7-specific "Driver-set composition" note.

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Watson Key Drivers Assessment [AS or C] @ DD-Mon-YY`
Tags: `#Triaging #KeyDrivers #FulcrumIdentification`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only.

---

## EXECUTION

**Dual-source query.** Both versions run:
- [AS] version → submitted to AlphaSense Deep Research by Haiku agent.
- [C] version → executed natively by Sonnet sub-agent using WebSearch.

Parent RESEARCHER handles extraction, highlighting, formatting, and Notion posting.

---

*End of Q7 Triaging KD Assessment — AFTER v1 draft (v2.1 pattern, per-driver structure, Q7-DC driver-count gate). Awaiting Richard's review with rest of BATCH 1.*
