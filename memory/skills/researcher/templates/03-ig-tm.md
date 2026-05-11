# Query 3: Technical Momentum — Claude Only

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/03-ig-tm.md`. Standard v2.1 pattern (NO BB#2 overlay — Q3 is technical not foundation-quality). Five Q3-specific amendments locked 06-May-26: word target raised to 4,000w (+33% from 3,000w prior; revised 06-May-26 PM from initial 3,500w to 4,000w per Richard's calibration), source-data-files-not-charts, multi-dim RS with named peer table, sceptical lens robust, BLUF retained. Plus Q3-specific Gate 5N: Master Dashboard data inputs verified accurate + complete.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Do NOT include a "Company Description," "Business Overview," or any equivalent scene-setting section. Reader has read Q1 IG BD. Start directly with TM analysis.

---

## MISSION

Write a comprehensive technical momentum memo for {COMPANY} ({TICKER}). This is an Ideas Generation (IG) stage output — assess the stock's technical position using Minervini's Stage Analysis framework, moving average structure, volume patterns, and relative strength across multiple dimensions (vs sector, vs industry, vs market, vs named peer companies).

Output: comprehensive memo, target {WORD_TARGET} words (default 4,000w; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim grounded in Master Dashboard data files (NOT web-search approximations, NOT chart-image reads). Every section opens with a J-front verdict bullet. Sceptical lens per section.

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated long-only equity investor (5-15 positions), UK/European focus, $5-50bn market cap. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**TM is increasingly important to the reader's decision-making** (signed off 06-May-26 — word target raised 40% to reflect this weight). Richard uses Minervini's Stage Analysis as a technical overlay on fundamental research. An 8/8 Minervini score is the trigger for IG research. The reader wants to understand:
- What stage is the stock in?
- How healthy is the advance?
- What does the MA structure say about institutional accumulation?
- What is the relative strength dispersion vs sector + industry + market + named peers?
- Are there pullback patterns that inform entry timing?

**Triaging purpose:** Fast, disciplined filtering at LIGHT depth. Does this stock fit a recognisable technical setup profile? Is the technical picture confirming or contradicting the fundamental thesis?

**Key vocabulary** (use these terms, not alternatives):
- "risk budget" (not "thermal capacity")
- "fulcrum driver" (not "key catalyst")
- "setup" (not "trade idea")
- "park" (not "pass")

**What downstream uses this output:** APM A&J reads this memo to populate **Pillar 1 (Technical Momentum)** in the IC framework. The memo's MM99 score + filter qualification + RS dispersion + base structure feed APM's Pillar 1 grading directly. Memo also surfaces on the RESEARCH STAGES dashboard tab.

---

## REQUIRED INPUTS — MASTER DASHBOARD-FIRST PROTOCOL

**Source-data-files NOT charts (locked 06-May-26).** Watson reads the underlying numeric source data, NOT the rendered chart images. Reasons: (a) source data has more precision than chart-image reads; (b) eliminates risk of chart-misread; (c) Watson's [C] sub-agent is text-native. Richard reviews charts visually in a separate window via the Master Dashboard — that is the human review surface.

### Step 1: Check Master Dashboard data files

1. Read `COWORK/master-dashboard/data/prices.json` — search for the ticker. Provides price, 7 MAs (5D/10D/20D/50D/100D/150D/200D), previous-day values, 52W H/L, ADV, market cap.
2. Read `COWORK/master-dashboard/data/filter-results.json` — search for the ticker. Provides MM99 score (11-test, 5 groups), all filter pass/fail results, qualification stages, RS excess returns vs sector/industry/market, EWS signals.
3. Read `COWORK/master-dashboard/data/factset-ssem.json` — for SS revisions context (Q3 informational use).
4. Read `COWORK/master-dashboard/data/factset-valuation.json` — for valuation context (Q3 informational use).

**If FOUND in Master Dashboard:** Use MD data as the **quantitative backbone** for MA structure, MM99 score, filter status, and RS. See **Master Dashboard Data Extraction** below.

**Supplement with pullback monitor (temporary):** If `COWORK/pullback-data.json` contains the ticker, extract 10-signal composite, base count/history, violation tracking, red flags, MA alerts. These fields are not yet computed by the Master Dashboard's UTR tab. See **Pullback Monitor Supplementary Data** below.

**Data freshness:** Check `_meta.generated` timestamp on prices.json + filter-results.json. If older than 48 hours, note this in memo header ("Data as of {date}") — do NOT block writing.

**If NOT FOUND in Master Dashboard:** Add the stock to `COWORK/master-dashboard/data/universe.json`:
```json
{
  "ticker": "{TICKER}",
  "yf_ticker": "{YFINANCE_FORMAT}",
  "company_name": "{COMPANY}",
  "sector": "{SECTOR}",
  "industry": "{INDUSTRY}"
}
```
(yfinance format: .ST=Stockholm, .L=London, .AS=Amsterdam, .DE=Frankfurt, .CO=Copenhagen, .SW=Swiss, .PA=Paris, .MC=Madrid.)

Inform Richard: "Added {TICKER} to Master Dashboard universe. Please run `python generate_master_data.py --full-universe`. I will proceed with the TM memo once the data is available." While waiting, proceed with other IG queries (#1, #2) that don't require TM data.

### Master Dashboard Data Extraction

| Data needed | Source file | JSON path |
|---|---|---|
| Current price | prices.json | `price` |
| Previous-day price | prices.json | `price_prev` |
| All 7 MA levels | prices.json | `mas.5D`, `mas.10D`, `mas.20D`, `mas.50D`, `mas.100D`, `mas.150D`, `mas.200D` |
| Previous-day MA levels | prices.json | `mas.5D_prev`, `mas.10D_prev`, etc. |
| 52W high / low | prices.json | `high_52w`, `low_52w` |
| ADV (1M, 3M) | prices.json | `adv_1m`, `adv_3m` |
| Market cap | prices.json | `market_cap` |
| MM99 score (11-test) | filter-results.json | `mm99.score`, `mm99.max_score` |
| MM99 group pass/fail | filter-results.json | `mm99.group_a` through `mm99.group_e` (each has `pass` + per-test detail) |
| RS excess returns (sector/industry/market) | filter-results.json | `mm99.group_e.rs_sector`, `mm99.group_e.rs_industry`, `mm99.group_e.rs_market` |
| Basing Plateau status | filter-results.json | `basing_plateau.group_a/b/c.pass` + weeks_meeting |
| Probing Bet qualification | filter-results.json | `probing_bet.group_a/b/c/d/e` |
| Uptrend Retest signals | filter-results.json | `uptrend_retest.composite_score`, `uptrend_retest.signals`, `uptrend_retest.ews` |
| VCP status | filter-results.json | `vcp` |
| SSEM revision data | factset-ssem.json | Per-ticker revision %, momentum count |
| Valuation (P/E, percentile) | factset-valuation.json | Per-ticker P/E, 10Y percentile |

### Pullback Monitor Supplementary Data (if available)

| Data needed | JSON path | Notes |
|---|---|---|
| 10-signal composite score + status | `scores.composite`, `scores.composite_status` | Weighted score (max 7.0) with signal-level detail |
| Individual signal scores (s1–s7, 3a–3e) | `scores.signals` | Volume quality, candle quality, distribution days, recovery speed |
| Base count + base history | `scores.base_count`, `scores.base_details` | Dates, depth, breakout for each base |
| Violation count + details | `scores.violation_count`, `scores.violation_details` | 8 Minervini violation types |
| Red flags | `scores.red_flags` | 200D break, death cross, distribution, retracement |
| MA alerts (which MAs being tested) | `scores.ma_alerts` | Within 2% of any MA |
| Pullback depth % + days | `scores.drawdown_pct`, `scores.pullback_days`, `scores.in_pullback` | Current pullback state |
| Swing high date + price | `scores.swing_high` | Local peak detection |

If pullback-data.json unavailable: proceed with MD data only. Note in memo: "Pullback signal depth unavailable — assessment based on Master Dashboard screening data."

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in SECTIONS TO COVER must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*. A parent bullet ≤30 words plus 2-4 sub-bullets ≤25 words each carries 100-150 words of analytical content in scannable form.

If in doubt, write more substantive bullets. Completeness and analytical rigour > conciseness. Do not sacrifice depth for brevity.

**The test:** would Richard learn something from this memo that he couldn't get from glancing at the Master Dashboard chart? If the bullet just restates a chart observation, it's filler. If it triangulates MM99 + RS + base + volume + peer dispersion to surface a non-obvious signal — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1 (only if model insists).
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.**
- **One analytical dimension per bullet.** Split compound bullets.
- **Signpost prefixes** (demi-bold + colon) on every parent bullet. Vocabulary specified per-section. SIGNPOST DISCRETION clause applies.
- **Peer / base-rate anchor** on every quantitative claim. For TM, peer anchors include: sector RS percentile, industry RS percentile, market RS percentile, AND named-peer RS comparison. Never a number in isolation.
- **J-front verdict bullet** at top of every section. Verbal verdict, ≤30w, peer-anchored. NOT a grade (RESEARCHER doesn't grade — APM grades Pillar 1).
- **Per-section sceptical bullet** at bottom of every section. Open-framed: what's the false-signal counter-read, and through what mechanism could it materialise?
- **IAJA suffix tags** on every parent bullet: `[#J]` / `[#A]` / `[#I]`.
- **❌ inversion marker** on technically weak findings (e.g. RS bottom-quartile, MA stack inverted).
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (top/bottom 5% on some dimension — e.g. MM99 11/11, RS percentile >95), (b) deliberately-weird technical signals (atypical pattern formations, unusual volume signatures, cross-roads exposures the consensus is ignoring, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo.
- **Inline highlights** (green/yellow/red phrase-level) on the specific carrying phrase.
- **Master Dashboard data is THE backbone.** Do NOT web-search for MA levels, MM99 scores, RS percentiles — they are in the JSONs.

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Three guardrails: (1) canonical first, (2) ≤4 words demi-bold + colon, (3) single analytical dimension. Invented signposts logged in QC footer.

### Memo skeleton

```
1. METADATA HEADER (you populate)
   Ticker, company, query name, stage, source ([C]), generated date, target words, MD data timestamp.
   metadata.json: write at completion. Memo will not post without it.

2. KEY FINDINGS (BLUF)
   5-10 parent bullets. Each ≤30w. J→A→I order. Peer-anchored.
   Skim layer.

3. BODY SECTIONS §1-§7 (per SECTIONS TO COVER below)
   Each section opens with J-front verdict.
   Each section ends with sceptical bullet.

4. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
   0-5 bullets surfacing strongest cross-cutting bearish technical reads.

5. AGGREGATE OUTLIERS (⚡)
   0-3 bullets. Genuinely unusual data points only.

6. QC AUDIT PANEL (validator-filled at post time)
   Includes Q3-specific Gate 5N (Master Dashboard data integrity).

7. QC COMMENTARY (RESEARCHER-authored)
   3-4 free-flowing bullets summarising what the structured numbers say.

8. QC FOOTER (auto-generated from metadata.json)
```

---

## SECTIONS TO COVER

### §1 — Stage Identification + History

**Open with J-front verdict bullet:** Net signal on {TICKER}'s current stage + recent stage trajectory — ≤30w.

**Canonical signpost vocabulary:** "Current stage:", "Stage 1→2 transition:", "Stage 2→3 transition:", "Stage 2 advance:", "Stage 4 decline:", "MA crossover:", "Volume signal:", "Stage history:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Identify and narrate the full stage history (5Y horizon).
- When did each stage transition occur? (Stage 1→2, 2→3, 3→4, 4→1)
- How long did each stage last?
- What was the percentage advance in each Stage 2 run?
- Where is the stock NOW in the stage cycle?
- Reference specific MA crossovers and price/volume patterns that marked transitions.

**Coverage:** 8-12 parent bullets + sub-bullets. Stage transitions get explicit dates + MA references.

**End with sceptical bullet:** "What might be misread in this stage classification? Through what mechanism might a Stage 2 advance prove to be a Stage 4 dead-cat bounce in disguise?"

---

### §2 — Current Technical Setup + MM99 Breakdown

**Open with J-front verdict bullet:** Net signal on current setup health — ≤30w, MM99-anchored.

**Canonical signpost vocabulary:** "Price vs 200D:", "Price vs 50D:", "Price vs 5D:", "MA stack:", "MM99 score:", "MM99 Group A:", "MM99 Group B:", "MM99 Group C:", "MM99 Group D:", "MM99 Group E:", "Filter qualification:", "Volume confirmation:", "Accumulation signal:", "Distribution signal:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Current price relative to all 7 MAs (exact levels from prices.json).
- MA ordering and spacing — is the stack healthy (price > 5D > 10D > 20D > 50D > 100D > 150D > 200D)?
- MM99 score (11-test, 5 groups) — each group and each test individually. Show pass/fail for every test.
- Filter qualification status: which filters pass? At what stage (Early/Late/Capital)?
- Volume analysis: is volume confirming the move? Accumulation vs distribution patterns (use pullback monitor signals 3a-3e if available).

**Coverage:** 12-18 parent bullets + sub-bullets. **Mandatory: full MM99 11-test breakdown** with each test's pass/fail and value. **Mandatory: MA stack table** (each of 7 MAs with current value + previous-day value + price-vs-MA distance %).

**End with sceptical bullet:** "What's the bearish read on the current setup? Through what mechanism might MM99 9/11 be misleading (e.g. one or two tests carrying inflated weight)? What weak link in the MA stack is most fragile?"

---

### §3 — Multi-dimensional Relative Strength (LOAD-BEARING per Richard 06-May-26)

**Open with J-front verdict bullet:** {TICKER}'s overall RS standing across the four dimensions — ≤30w.

**Canonical signpost vocabulary:** "RS vs sector:", "RS vs industry:", "RS vs market:", "RS percentile:", "Sector outperformance:", "Industry outperformance:", "Market outperformance:", "Peer rank:", "Named peer comparison:", "RS dispersion:", "RS divergence:", "RS trend:". Invent where pattern warrants.

**Analytical sub-questions to address (LOAD-BEARING — Richard wants depth here):**
- **RS vs sector:** Excess return vs sector benchmark (1M, 3M, 6M, 12M). Sector RS percentile. Trend direction. Use `mm99.group_e.rs_sector` from filter-results.json.
- **RS vs industry:** Excess return vs industry benchmark (1M, 3M, 6M, 12M). Industry RS percentile. Trend direction. Use `mm99.group_e.rs_industry`.
- **RS vs market:** Excess return vs broad market (1M, 3M, 6M, 12M). Market RS percentile. Trend direction. Use `mm99.group_e.rs_market`.
- **RS vs named individual peers:** Stack-rank {TICKER} against each named peer in {PEERS} on RS percentile, MA position relative to peer's MAs, base structure. **Mandatory peer-RS table** (5 closest named peers + sector median row).
- **RS dispersion across dimensions:** Where does {TICKER} stand in each dimension? Is the RS picture coherent (top quartile in all four) or divergent (top in market but bottom in sector)?
- **RS trend over time:** Are the RS percentiles improving or deteriorating across L3M, L6M, L12M?
- **Divergences:** Any divergences between fundamental momentum and technical RS? Between price RS and earnings RS (SSEM)?

**Coverage:** 12-18 parent bullets + sub-bullets. **Mandatory peer-RS table** is non-negotiable — APM uses it for cross-stock comparison.

**End with sceptical bullet:** "What's the bearish read on the RS picture? Through what mechanism might high RS prove late-cycle exhaustion rather than leadership confirmation? What sector or peer dispersion signal might be under-weighted?"

---

### §4 — Base Formation Analysis

**Open with J-front verdict bullet:** Net signal on base structure — type, depth, duration, volume pattern, breakout integrity — ≤30w.

**Canonical signpost vocabulary:** "Base type:", "Cup-and-handle:", "Flat base:", "High-tight flag:", "VCP:", "Base depth:", "Base duration:", "Pivot point:", "Breakout level:", "Volume dry-up:", "Volume expansion:", "Base count:". Invent where pattern warrants.

**Analytical sub-questions to address (using base history from pullback-data.json if available, else MD data + 3Y price action):**
- Identify the base pattern (cup-and-handle, flat base, high-tight flag, VCP, etc.).
- Base depth (% decline from left-side high to low).
- Base duration (weeks/months).
- Volume pattern during base: dry-up on declines, expansion on advances?
- Pivot point / breakout level identification.
- Base count: which base is this in the current advance? (1st-stage / 2nd-stage / 3rd-stage / 4th-stage = late-cycle).

**Coverage:** 8-12 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on the base? Through what mechanism might apparent breakout be a false breakout (low volume, late-stage, climax pattern)? What base-count fatigue signal might be lurking?"

---

### §5 — Moving Average Analysis

**Open with J-front verdict bullet:** Net signal on MA slopes, spacing, and historical pullback patterns — ≤30w.

**Canonical signpost vocabulary:** "50D slope:", "200D slope:", "Golden cross:", "Death cross:", "Price-vs-50D:", "Price-vs-200D:", "Extension:", "Historical pullback range:", "MA support test:", "MA violation:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- 50D MA slope and trajectory (current value vs 30D ago).
- 200D MA slope and trajectory.
- 50/200 relationship — golden cross timing if applicable.
- Price distance from 50D and 200D (% above/below) — is it extended?
- Historical pattern: how far does this stock typically run above its 50D before pulling back?

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on MA structure? Through what mechanism might 50D slope be flatlining despite price strength? What MA violation pattern would invalidate the technical thesis?"

---

### §6 — Volume Analysis

**Open with J-front verdict bullet:** Net signal on volume — accumulation vs distribution, climax patterns, institutional behaviour — ≤30w.

**Canonical signpost vocabulary:** "ADV (30D):", "ADV trend:", "Up-volume:", "Down-volume:", "Volume ratio:", "Climax pattern:", "Exhaustion gap:", "Blow-off top:", "Distribution day count:", "Accumulation day count:", "Institutional rating:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- ADV (30D) vs 6M and 12M averages.
- Up-volume vs down-volume ratio over recent weeks.
- Volume climax patterns (exhaustion gaps, blow-off tops)?
- Institutional accumulation/distribution rating.
- Distribution day count (institutional selling pressure indicator).

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish volume read? Through what mechanism might apparent accumulation prove to be window-dressing? What distribution signal might be forming that hasn't yet broken price?"

---

### §7 — Pullback Tests (Stage 2 stocks only) + Sceptical Synthesis

**Open with J-front verdict bullet:** Cumulative trend health from pullback-test sequence — ≤30w. (For non-Stage-2 stocks: brief note + skip pullback table.)

**Canonical signpost vocabulary:** "Pullback test:", "MA tested (20D):", "MA tested (50D):", "MA tested (100D):", "Pullback depth:", "Pullback duration:", "Volume on pullback:", "MA hold:", "MA violation:", "Cumulative trend health:", "Stage 2 maturity:". Invent where pattern warrants.

**Analytical sub-questions to address (if Stage 2):**
- Catalogue every pullback test in the current advance.
- Which MA was tested (20D, 50D, 100D)?
- Depth of pullback (%).
- Duration (days/weeks).
- Volume pattern during pullback (declining = healthy).
- Did the MA hold or was it violated?
- Pullback health verdict for each test.
- Cumulative trend health assessment.

For early Stage 2 stocks (0-2 tests): describe what to watch for.

**Coverage:** 8-12 parent bullets + sub-bullets. **Mandatory pullback-test table** if 3+ tests have occurred (date, MA tested, depth, duration, volume pattern, hold/violation, verdict).

**End with cross-cutting sceptical synthesis bullet:** "What is the strongest bearish technical case for {TICKER} given everything above? — ≤30w. Reverse-engineer: what would invalidate the technical thesis? Single largest risk to the technical setup?"

---

## AGGREGATE BLOCKS (after §7)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly weak relative to peer / base-rate.

**Format:** `❌ Signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `❌ RS vs sector: -3.2% trailing 6M — bottom-quartile of 12-peer industrials cohort. [Cross-ref: §3]`

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `⚡ RARE: MM99 score 11/11 + RS top-decile across all four dimensions — only 6 of 1,300 European universe meeting both. [Cross-ref: §2 + §3]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel into the memo at post time. Q3-specific gate 5N added (Master Dashboard data integrity).

The panel is plain-text-with-markdown. Visual styling owned by SA - Ratings Dashboard project (D-RSR-21).

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [C]
**Stage:** IG
**Generated:** DD-Mon-YY
**MD data timestamp:** {prices.json _meta.generated}

### Summary
| Metric | Value | Notes |
|---|---|---|
| Word ratio (output / source) | XX.X% | target 40-60%; hard floor 35% |
| H2 sections | N | min 3 required |
| Parent bullets | N | all within 35w ceiling |
| Hard failures | 0 / N | (0 to PASS) |
| Warnings | N | (cosmetic flags) |
| MD data integrity | PASS / FAIL | Gate 5N — see below |

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
| **5N** | **Master Dashboard data inputs verified accurate + complete (Q3-specific)** | **Hard** | **✓ / ✗** |

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text} — e.g. stock newly added to MD universe; data <48h old.

### Warnings (if any)
- {Gate}: {one-line description}
```

### Gate 5N — Master Dashboard data integrity (Q3-specific)

5N is unique to Q3 (and any future TM-related queries). Validates ALL of:

- `prices.json` loaded and contains {TICKER} entry.
- `_meta.generated` timestamp present and within 7 days of memo generation date (warn if 2-7 days; fail if >7 days).
- All 7 MAs (5D, 10D, 20D, 50D, 100D, 150D, 200D) present and numeric (no nulls, no zero-values).
- Latest price, 52W H/L, ADV present and numeric.
- `filter-results.json` loaded and contains {TICKER} entry.
- MM99 score present (`mm99.score`) and numeric.
- All 5 MM99 groups present (`group_a` through `group_e`) with `pass` field set.
- RS excess returns (`rs_sector`, `rs_industry`, `rs_market`) present and numeric.
- No obvious data anomalies (e.g. >50% single-day price move suggests stale/bad data — flag for review).

If any check fails: 5N FAIL. Memo is BLOCKED from posting. Watson must re-run Master Dashboard data generation (`python generate_master_data.py --full-universe`) before retrying.

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say.

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired — why and whether they matter}
- **MD data note:** {≤30w on Master Dashboard data freshness / completeness — Q3-specific cross-ref to Gate 5N}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view + counter-hypothesis + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing.}
```

### Authoring rules

1. **3-4 bullets, each ≤30 words.** Same parent-bullet discipline as body sections.
2. **Signposted with verdict-flavoured labels.** Canonical: "Net QC verdict:", "Warning context:", "MD data note:" (Q3-specific replaces "Source breadth note:" since Q3 is [C]-only with no SS), "Counter-hypothesis check (AI-Dunning-Kruger):". Invent additional labels per SIGNPOST DISCRETION.
3. **Specific not generic.** "MM99 8/11 — Group D (volume) failing on s3a only" not "MM99 looks fine."
4. **Cross-reference the body.** "Surfaced in §3 RS divergence + Outliers block."
5. **No A-F or R/O/Y/G grades** (per D-RSR-3, RESEARCHER does not grade).
6. **MD data note is mandatory for Q3** — surface freshness, completeness, and any anomalies the source data showed.
7. **No empty restating.** Add interpretation, not echo.

---

## VALIDATION GATES (auto-applied at post time)

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1-§7 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (§1-§7) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately (not overused) | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **Mandatory peer-RS table (§3)** | required | BLOCK post |
| **Mandatory MA stack table (§2)** | required | BLOCK post |
| **Mandatory full MM99 11-test breakdown (§2)** | required | BLOCK post |
| **Gate 5N — Master Dashboard data integrity** | required | BLOCK post |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when MD data genuinely thin (e.g. stock newly added to universe, data <48h since first generation), word-count gate bypasses; structural gates including 5N still apply.

**Note on 5L / 5M:** SS breadth gate (5L) and Expert breadth (5M) DO NOT apply to Q3 per D-RSR-20 — Q3 is mostly numeric and [C]-only. Skipped from validation.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

- [ ] Mission compass clear: have I assessed {TICKER}'s technical position via Stage Analysis + MA structure + MM99 + multi-dim RS + base + volume + pullback tests?
- [ ] Reader priorities applied: TM is increasingly important to Richard's decisions; have I provided depth proportionate to that weight (~3,500w target)?
- [ ] All 7 sections present, each with J-front verdict bullet and sceptical bullet.
- [ ] Master Dashboard data files read FIRST (NOT chart images, NOT web-search approximations).
- [ ] Multi-dimensional RS analysis (vs sector + industry + market + named peers) addressed in depth (§3).
- [ ] Mandatory tables: peer-RS table (§3), MA stack table (§2), full MM99 11-test breakdown (§2).
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs (except optional 1-2 sentence inline scene-setter top of §1).
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Master Dashboard data timestamp noted in memo header.
- [ ] Gate 5N data integrity check passed (MD data freshness + completeness verified).
- [ ] metadata.json written.
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored (3-4 bullets, signposted, ≤30w each, specific not generic, MD data note mandatory).
- [ ] Sceptical bullets per section actually invert findings — not boilerplate "could be wrong."

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Technical Momentum [C] @ DD-Mon-YY`
Tags: `#IG #TM #TechnicalMomentum #Pillar1`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only (per spec §16); never highlight whole bullets.

**Note on chart embedding:** Per Richard 06-May-26, charts are NOT embedded in the memo — Richard reviews charts in a separate window via the Master Dashboard. The memo references chart-equivalent observations from source data (e.g. "price crossed above 50DMA on 23-Apr with volume 1.4x ADV"). No chart images required in Notion posting.

---

## EXECUTION

**Claude [C] only.** No AlphaSense version (AS has minimal technical/chart data).

**Primary flow:** Sonnet sub-agent receives this template + extracted Master Dashboard data (`prices.json` + `filter-results.json` + `factset-ssem.json` + `factset-valuation.json` fields for {TICKER}) as input context. If `pullback-data.json` also contains the ticker, include the supplementary signal-level data.

**Fallback flow (stock not in Master Dashboard):** Stock added to `universe.json`. RESEARCHER waits for Richard to run `python generate_master_data.py --full-universe`, then proceeds with primary flow.

**Ground quantitative claims in Master Dashboard data.** Do NOT web-search for MA levels, price data, MM99 scores, or RS metrics — these are in the dashboard JSON files. Gate 5N enforces this.

Parent RESEARCHER handles highlighting, formatting, and Notion posting.

---

*End of Q3 IG TM — AFTER v1 draft (v2.1 pattern + Q3-specific Gate 5N). Awaiting Richard's review with rest of BATCH 1 (Q5, Q6, Q7).*
