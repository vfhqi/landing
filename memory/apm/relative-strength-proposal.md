---
name: Relative Strength & Breadth Dashboard — Design Proposal
description: Architecture proposal for daily European industry/sector/geography relative strength and breadth monitoring
type: project
status: proposal
author: Watson [W]
date: 2026-03-30
---

# Relative Strength & Breadth Dashboard — Design Proposal

## 1. Purpose & Fit

This tool fills a specific gap in Richard's APM workflow: systematic, daily monitoring of where capital is rotating across European industries, sectors, and geographies. It answers three questions every morning:

1. **Where is relative strength improving?** (rotation targets — potential IG candidates)
2. **Where is relative strength deteriorating?** (rotation away — review existing positions)
3. **Is the move broad-based or narrow?** (breadth confirms or warns against the RS signal)

This is the quantitative backbone of the "Fit for Fighting" assessment. Currently, market/environment reads rely on Richard's qualitative judgement and journal entries. This dashboard adds a structured, repeatable data layer — something the APM role can check daily and flag when signals shift.

It also feeds directly into the risk-off/risk-on framework. Richard's current Iran-driven industry analysis (March 2026) is exactly the kind of environment where systematic RS + breadth tracking would surface rotation early.

---

## 2. Recommended Architecture: FactSet Excel Workbook

### Why Excel + FactSet (not Python, not standalone)

Richard already lives in Excel for financial models. The FactSet add-in provides real-time and historical data without needing API keys, Python environments, or scheduled scripts. A single workbook that auto-refreshes on open is the lowest-friction solution — it becomes part of the morning routine, not a separate system to maintain.

### Workbook Structure

| Sheet | Purpose | Data Source |
|-------|---------|-------------|
| **1. Universe** | Richard's ~1,616 tickers, linked from the master universe file | Existing file (link, not copy) |
| **2. Industry RS** | Mansfield RS + simple RS ratio for 14 Viewforth industries vs SXXP | FactSet formulas → STOXX 600 industry indices |
| **3. Sector RS** | Same methodology at sector level (17 sectors) | FactSet formulas → constituent aggregation |
| **4. Geography RS** | RS for 10 major European country indices vs SXXP | FactSet formulas → country index prices |
| **5. Industry Breadth** | % of constituents above 50d MA, per industry | FactSet price data per constituent |
| **6. Sector Breadth** | Same at sector level | FactSet price data per constituent |
| **7. Summary / Heatmap** | Single-page daily review — colour-coded RS + breadth grid | Formulas referencing sheets 2-6 |

### Sheet 1: Universe (Linked)

No duplication. Use an Excel reference to the master universe file (`Universe - 2026_03_30.xlsx`, Universe sheet). This keeps one source of truth. When the universe file updates, the workbook inherits changes.

Key columns needed downstream: Ticker, Industry (letter code), Sector (number code), Company, geography (parsed from ticker suffix).

### Sheet 2: Industry RS Dashboard

**Layout — one row per Viewforth industry:**

| Industry | STOXX Index Ticker | Mansfield RS | RS 1d Chg | RS 1w Chg | RS 1m Chg | RS 3m Chg | RS Trend | Signal |
|--------|-------------------|-------------|-----------|-----------|-----------|-----------|----------|--------|

**Columns explained:**

- **STOXX Index Ticker**: The STOXX 600 industry sub-index used as proxy (see mapping in Section 4)
- **Mansfield RS**: Primary signal. (Industry Price / SXXP Price) / 52w MA of (Industry Price / SXXP Price) - 1. Expressed as %. Positive = outperforming and accelerating vs own history
- **RS 1d/1w/1m/3m Chg**: Change in simple RS ratio (Industry / SXXP) over each period. Shows momentum of relative performance
- **RS Trend**: Categorical — "Improving", "Stable", "Deteriorating" based on direction of Mansfield RS over last 4 weeks
- **Signal**: Auto-generated flag combining RS + breadth (from Sheet 5). See Section 7 for logic

**FactSet formulas (template):**

```
// Current industry index price
=FG_PRICE("[INDUSTRY_TICKER]", "PRICE", 0, , , "D")

// SXXP price
=FG_PRICE("SXXP-EUR", "PRICE", 0, , , "D")

// Historical price for MA calculation (252 trading days ago)
=FG_PRICE("[INDUSTRY_TICKER]", "PRICE", -252, , , "D")

// Period return for RS change
=FG_PERF("[INDUSTRY_TICKER]", "1D")
=FG_PERF("[INDUSTRY_TICKER]", "1W")
=FG_PERF("[INDUSTRY_TICKER]", "1M")
=FG_PERF("[INDUSTRY_TICKER]", "3M")

// Same for SXXP benchmark
=FG_PERF("SXXP-EUR", "1D")
```

**Mansfield RS calculation (in Excel):**

```
RS_Ratio_Today = Industry_Price_Today / SXXP_Price_Today
RS_Ratio_52w_MA = AVERAGE(last 252 daily RS_Ratio values)
Mansfield_RS = (RS_Ratio_Today / RS_Ratio_52w_MA) - 1
```

For the 52-week MA, we need 252 daily RS ratio values. Two approaches:

- **Option A (simpler):** Use FactSet `FG_PRICE` to pull 252 days of history into a hidden helper range, compute the average. More formulas but transparent
- **Option B (cleaner):** Use FactSet's `=FDS()` function with a time-series request to get the trailing average directly. Fewer cells but more complex formula syntax

Recommendation: **Option A** for transparency. Helper columns can be hidden. Richard can audit the calculation.

### Sheet 3: Sector RS Dashboard

Same structure as Sheet 2, but for Richard's 17 sector classifications. The challenge here is that there are no direct STOXX indices for Richard's custom sectors (e.g., "M.10. Capital goods — Electricity storage/EV"). Two approaches:

- **Option A (recommended):** Calculate sector RS as the market-cap-weighted average RS of constituents in each sector. This uses Richard's actual universe, not a proxy index. More formulas but perfectly aligned with the portfolio universe
- **Option B:** Map to nearest STOXX 600 Sector sub-index where possible. Imperfect fit — Richard's taxonomy is deliberately non-GICS

For Option A, each sector row aggregates from the Universe sheet: pull price and market cap for each constituent via FactSet, compute weighted RS ratio, then Mansfield RS on that aggregate.

### Sheet 4: Geography RS Dashboard

**Layout — one row per country:**

| Country | Index Ticker | FactSet Ticker | Mansfield RS | RS 1d | RS 1w | RS 1m | RS 3m | Tickers in Universe |
|---------|-------------|---------------|-------------|-------|-------|-------|-------|---------------------|
| UK | FTSE 100 | FTSE-GB | | | | | | 237 |
| Germany | DAX 40 | DAX-DE | | | | | | 170 |
| Sweden | OMX Stockholm 30 | OMX-SE | | | | | | 162 |
| France | CAC 40 | PX1-FR | | | | | | 147 |
| Switzerland | SMI | SSMI-CH | | | | | | 124 |
| Italy | FTSE MIB | FTSEMIB-IT | | | | | | 89 |
| Spain | IBEX 35 | IBEX-ES | | | | | | 67 |
| Norway | OBX 25 | OBX-NO | | | | | | 60 |
| Netherlands | AEX | AEX-NL | | | | | | 49 |
| Denmark | OMX Copenhagen 25 | OMXC25-DK | | | | | | 40 |

All measured relative to SXXP using the same Mansfield RS methodology.

**Note:** FactSet ticker symbols above are indicative — exact tickers need confirming in FactSet's symbol lookup. The FactSet ticker format for indices varies (some use exchange suffix, some use dedicated codes like `SP50` for S&P 500). Richard will need to verify these in his FactSet terminal. Watson can draft the formulas once tickers are confirmed.

### Sheet 5: Industry Breadth

**Layout — one row per industry:**

| Industry | # Constituents | # > 50d MA | Breadth % | Breadth 1w Chg | Breadth 1m Chg | Breadth 3m Chg | Breadth Zone | Divergence? |
|--------|---------------|-----------|-----------|----------------|----------------|----------------|-------------|-------------|

**Calculation per constituent:**

```
// Current price
=FG_PRICE("[TICKER]", "PRICE", 0)

// 50-day MA — use FG_PRICE with moving average or calculate from 50 daily prices
=FG_PRICE("[TICKER]", "PRICE_AVG_50D", 0)

// Above 50d MA?
=IF(Current_Price > MA_50d, 1, 0)
```

**Aggregation per industry:**

```
Breadth_% = COUNTIF(industry_constituents_above_50d, 1) / COUNT(industry_constituents) * 100
```

**Breadth Zones:**

| Zone | Breadth % | Interpretation |
|------|-----------|---------------|
| Strong | >70% | Broad-based strength — industry rally has wide participation |
| Neutral | 40-70% | Mixed — some stocks participating, some not |
| Weak | <30% | Broad-based weakness — few stocks holding above trend |

**Divergence flag:** If industry RS is positive (outperforming) but breadth is falling, or industry RS is negative but breadth is rising, flag as "DIVERGENCE". These are early warning signals of rotation.

### Sheet 6: Sector Breadth

Identical methodology to Sheet 5, grouped by Richard's 17 sector codes instead of 14 industry codes. Smaller constituent counts per sector — flag where n < 10 as the breadth signal is less statistically meaningful.

### Sheet 7: Summary / Heatmap

**This is the sheet Watson reviews daily.** Single-page view, designed for 5-minute morning scan.

**Layout:**

Top section — **Industry Grid** (14 rows):

| Industry | Mansfield RS | RS Direction | Breadth % | Breadth Direction | Combined Signal |
|--------|-------------|-------------|-----------|------------------|----------------|

Each cell colour-coded:
- **Green** (dark/light): Strong positive / moderate positive
- **Red** (dark/light): Strong negative / moderate negative
- **Amber**: Neutral or divergent
- **Purple border**: Divergence flagged (RS and breadth disagreeing)

Bottom section — **Geography Grid** (10 rows):
Same format for country indices.

Right sidebar — **Alert Panel:**
- Top 3 industries by RS improvement this week
- Bottom 3 industries by RS deterioration this week
- Any divergence flags
- Breadth extremes (>80% or <20%)

**Conditional formatting rules:**

```
Mansfield RS > +5%  → Dark green
Mansfield RS +1% to +5%  → Light green
Mansfield RS -1% to +1%  → White/neutral
Mansfield RS -5% to -1%  → Light red
Mansfield RS < -5%  → Dark red

Breadth > 70%  → Green fill
Breadth 40-70% → No fill
Breadth < 30%  → Red fill
```

---

## 3. Relative Strength Methodology — Detail

### Primary: Mansfield Relative Strength

Stan Weinstein's method, adapted for industries. The key insight: it's not just whether a industry is outperforming, but whether that outperformance is accelerating or decelerating relative to its own history.

**Formula:**

```
RS_Ratio(t) = Price_Industry(t) / Price_SXXP(t)
MA_52w(t) = Average of RS_Ratio over trailing 252 trading days
Mansfield_RS(t) = ( RS_Ratio(t) / MA_52w(t) ) - 1
```

**Interpretation:**

| Mansfield RS | Meaning |
|-------------|---------|
| > 0 and rising | Industry outperforming and accelerating — strongest signal |
| > 0 and falling | Industry still outperforming but losing momentum — watch for rollover |
| < 0 and falling | Industry underperforming and deteriorating — weakest signal |
| < 0 and rising | Industry underperforming but improving — potential rotation target |

**Why Mansfield over simple RS ratio:**

Simple RS ratio tells you "is this industry beating the index?" Mansfield RS tells you "is this industry's relative performance better or worse than its own trailing norm?" The 52-week MA acts as a mean-reversion anchor. A industry can have a positive simple RS ratio but negative Mansfield RS if its outperformance is narrowing. This is the more actionable signal for rotation timing.

### Secondary: Simple RS Ratio Change

Simpler metric, useful as a sanity check and for short-term momentum:

```
RS_Ratio(t) = Price_Industry(t) / Price_SXXP(t)
RS_Change_1w = ( RS_Ratio(t) / RS_Ratio(t-5) ) - 1
RS_Change_1m = ( RS_Ratio(t) / RS_Ratio(t-21) ) - 1
RS_Change_3m = ( RS_Ratio(t) / RS_Ratio(t-63) ) - 1
```

This captures pure directional change without the smoothing of Mansfield. Useful for spotting sharp short-term rotations (e.g., sudden risk-off moves into defensives).

### Combined Signal Logic

| Mansfield RS | Breadth | Simple RS Trend | Signal |
|-------------|---------|----------------|--------|
| Positive & rising | >60% & rising | Positive | **STRONG BUY-SIDE ROTATION** — broad-based, accelerating |
| Positive & rising | <40% or falling | Positive | **NARROW LEADERSHIP** — outperformance driven by few names |
| Negative & rising | Rising | Turning positive | **EARLY ROTATION IN** — improving, watch for confirmation |
| Negative & falling | <30% & falling | Negative | **STRONG SELL-SIDE ROTATION** — broad-based weakness |
| Positive & falling | Falling | Turning negative | **ROTATION OUT BEGINNING** — early warning |

---

## 4. European Industry & Geographic Index Mapping

### Viewforth Industry → STOXX 600 Industry Index Mapping

This is the critical mapping. Richard's 14-industry taxonomy doesn't map 1:1 to STOXX 600 ICB industries. Proposed mapping (needs Richard's confirmation):

| Code | Viewforth Industry | Constituents | Proposed STOXX 600 Proxy | STOXX Ticker (indicative) | Fit Quality |
|------|-----------------|-------------|-------------------------|--------------------------|-------------|
| A | Consumer Staples | 80 | STOXX 600 Food & Beverage + Personal & Household Goods | SX3P + SXQP | Good |
| B | Healthcare | 111 | STOXX 600 Health Care | SXDP | Good |
| C | Infra, Telecoms, Utes, Defence | 146 | Blend: STOXX 600 Utilities + Telecoms + Industrials (part) | SX6P + SXKP + partial SX2P | Poor — composite |
| D | Financials | 247 | STOXX 600 Banks + Insurance + Financial Services | SX7P + SXIP + SXFP | Good (combine 3) |
| E | Consumer Discretionary | 157 | STOXX 600 Retail + Autos & Parts + Travel & Leisure | SXRP + SXAP + SXTP | Moderate |
| F | Transportation | 18 | STOXX 600 Industrial Transportation | SXRP (partial) | Moderate — small n |
| G | Technology | 97 | STOXX 600 Technology | SX8P | Good |
| H | Consumer Services | 1 | N/A — only 1 constituent | — | Skip |
| I | Professional/Business Services | 46 | STOXX 600 Industrial Goods & Services (partial) | SX2P (partial) | Poor — subset |
| J | Media | 12 | STOXX 600 Media | SXMP | Good — small n |
| K | Materials | 126 | STOXX 600 Basic Resources + Chemicals + Construction & Materials | SXPP + SX4P + SXOP | Good (combine 3) |
| L | Real Assets/Estate | 106 | STOXX 600 Real Estate | SX86P | Good |
| M | Industrials | 171 | STOXX 600 Industrial Goods & Services | SX2P | Good |
| N | Energy/Commodities/Metals | 94 | STOXX 600 Energy + Basic Resources (overlap with K) | SXEP + SXPP (partial) | Moderate |

**Key issues for Richard to resolve:**

1. **Industry C is a composite** — Infra/Telecoms/Utes/Defence spans 3+ STOXX industries. Options: (a) use a blended index, (b) break into sectors for RS purposes, (c) use constituent-level aggregation (Option A from Sheet 3)
2. **Industry H has 1 constituent** — exclude from industry-level RS analysis
3. **Overlap between K and N** — Basic Resources appears in both. Need clean delineation
4. **STOXX ticker symbols** — the tickers above are indicative based on common STOXX naming conventions. Richard needs to verify exact FactSet identifiers in his terminal. FactSet may use different identifiers (e.g., `STOXX600_HC` or `SXDP-EUR`)

### Geographic Index Tickers

| Country | Index | Common FactSet Ticker | Notes |
|---------|-------|-----------------------|-------|
| Pan-European | STOXX Europe 600 | SXXP | Benchmark for all RS calculations |
| UK | FTSE 100 | UKX or FTSE100-GB | 237 tickers in universe |
| Germany | DAX 40 | DAX-DE or GDAXI | 170 tickers |
| Sweden | OMX Stockholm 30 | OMX30-SE or OMXS30 | 162 tickers |
| France | CAC 40 | PX1-FR or FCHI | 147 tickers |
| Switzerland | SMI | SSMI-CH or SMI | 124 tickers |
| Italy | FTSE MIB | FTSEMIB-IT | 89 tickers |
| Spain | IBEX 35 | IBEX-ES or IBEX35 | 67 tickers |
| Norway | OBX 25 | OBX-NO | 60 tickers |
| Netherlands | AEX | AEX-NL | 49 tickers |
| Denmark | OMX Copenhagen 25 | OMXC25-DK | 40 tickers |

**Important:** All FactSet ticker symbols above need verification. FactSet uses its own identifier system, and the exact format depends on the FactSet Excel add-in version and configuration. The first build step (Section 6) is a ticker verification exercise.

---

## 5. Breadth Methodology — Detail

### Core Metric: % Above 50-Day Moving Average

For each industry and sector, calculate the proportion of constituent stocks trading above their 50-day simple moving average. This is the most widely used breadth measure and strikes the right balance between sensitivity (not too noisy at 50d) and responsiveness (not too lagged like 200d).

### Calculation

For each ticker `i` in industry `S`:

```
Above_50d(i) = 1 if Price(i) > SMA_50(i), else 0
Breadth(S) = SUM(Above_50d for all i in S) / COUNT(i in S) * 100
```

### Historical Tracking

To track breadth changes over 1w/1m/3m, we need to store or calculate historical breadth values. Two approaches:

- **Snapshot approach:** Each day, record today's breadth value in a running log (hidden sheet or column). Then 1w change = today's breadth minus 5 days ago, etc. Requires either a manual "save snapshot" step or a VBA macro on workbook open
- **Calculated approach:** Use FactSet to pull each constituent's price 5/21/63 days ago and its 50d MA at that point, then recalculate historical breadth from first principles. More formulas but no manual step

Recommendation: **Snapshot approach with VBA macro** that runs on workbook open. It appends today's breadth values to a hidden log sheet. The change columns then reference that log. This is simpler and avoids pulling thousands of historical data points.

### Breadth-Based Signals

| Signal | Condition | Interpretation |
|--------|-----------|---------------|
| Breadth Thrust | Breadth rises from <30% to >70% within 10 trading days | Rare, powerful — new uptrend in industry |
| Breadth Collapse | Breadth falls from >70% to <30% within 10 trading days | Rapid deterioration — defensive action |
| Improving Breadth | Breadth rising for 3+ consecutive weeks | Broadening participation — healthy |
| Deteriorating Breadth | Breadth falling for 3+ consecutive weeks | Narrowing participation — warning |
| Bullish Divergence | Industry price makes new low, breadth makes higher low | Potential bottoming — accumulation signal |
| Bearish Divergence | Industry price makes new high, breadth makes lower high | Potential topping — distribution signal |

### Constituent Count Thresholds

Breadth is less meaningful with small samples. Flag reliability:

| Constituents | Reliability | Note |
|-------------|------------|------|
| >30 | High | Statistically meaningful |
| 15-30 | Moderate | Directional but noisy |
| <15 | Low | Flag in dashboard — single-stock moves dominate |

From Richard's universe: Industries D (247), M (171), E (157), C (146), K (126), B (111), L (106), G (97) all have >30. Industry F (18), J (12), I (46), A (80), N (94) are mixed. Industry H (1) is excluded.

---

## 6. Daily Workflow — APM Morning Routine Addition

### Proposed Morning Sequence (addition to existing routine)

**Time: First 5-10 minutes of morning session**

1. **Open RS/Breadth workbook** → FactSet auto-refreshes data on open (if configured; otherwise Ctrl+Shift+R to refresh)
2. **Go to Sheet 7 (Summary/Heatmap)** → 30-second scan of the colour grid
3. **Check the Alert Panel** for:
   - Any new divergence flags (RS and breadth disagreeing)
   - Industries entering breadth extremes (<20% or >80%)
   - Top 3 / Bottom 3 RS movers this week
4. **Cross-reference with current positions and pipeline:**
   - Are any held positions in industries with deteriorating RS + falling breadth?
   - Are any pipeline names in industries showing early rotation signals?
5. **Watson posts "Fit for Fighting" update to Notion** — structured as:

```
## [W] Fit for Fighting — [Date]

### Market Regime
[Risk-on / Risk-off / Transitioning — based on breadth aggregate]

### Industry Rotation Signals
- **Strengthening:** [Industries with improving Mansfield RS + rising breadth]
- **Weakening:** [Industries with deteriorating Mansfield RS + falling breadth]
- **Watch — Divergence:** [Industries where RS and breadth disagree]

### Geographic Signals
- **Outperforming:** [Countries with positive Mansfield RS vs SXXP]
- **Underperforming:** [Countries with negative Mansfield RS vs SXXP]

### Portfolio Implications
- [Position-specific notes if any industry signals are relevant]
- [Pipeline implications — any IG candidates in rotating industries?]

### Data Snapshot
[Key numbers: SXXP level, VIX, aggregate breadth %, notable moves]
```

---

## 7. Implementation Plan

### Phase 1: Foundation (Day 1-2)

| Step | Task | Owner | Notes |
|------|------|-------|-------|
| 1.1 | **Verify FactSet index tickers** — look up exact FactSet identifiers for all STOXX 600 industry indices, country indices, and SXXP | Richard | Use FactSet symbol lookup. Watson can draft a ticker verification checklist |
| 1.2 | **Confirm industry mapping** — review the Viewforth → STOXX mapping in Section 4, resolve Industry C composite issue | Richard | Critical path — everything downstream depends on this |
| 1.3 | **Test FactSet formulas** — build a 3-row proof of concept (one industry, one country, one breadth calculation) | Richard + Watson | Watson drafts formulas, Richard tests in Excel with live FactSet connection |
| 1.4 | **Confirm FactSet refresh behaviour** — does the add-in auto-refresh on open? What's the refresh latency? | Richard | Affects whether VBA macro is needed |

### Phase 2: Build (Day 3-5)

| Step | Task | Owner | Notes |
|------|------|-------|-------|
| 2.1 | **Create workbook skeleton** — 7 sheets with headers, layout, conditional formatting rules | Watson | Watson can build the template offline; Richard adds FactSet formulas |
| 2.2 | **Sheet 2: Industry RS** — populate FactSet formulas for all 13 active industries (excl. H) | Richard | Using confirmed tickers from 1.1 |
| 2.3 | **Sheet 4: Geography RS** — populate for 10 country indices | Richard | Simpler — direct index-vs-SXXP |
| 2.4 | **Sheet 5: Industry Breadth** — build constituent-level price pulls + 50d MA for one industry, then replicate | Richard | Most formula-intensive sheet. Start with largest industry (D, 247 tickers) to stress-test |
| 2.5 | **Sheet 7: Summary/Heatmap** — wire up references to Sheets 2-6, apply conditional formatting | Watson + Richard | Watson builds the logic; Richard validates colours/thresholds |

### Phase 3: Sector & Polish (Day 6-8)

| Step | Task | Owner | Notes |
|------|------|-------|-------|
| 3.1 | **Sheet 3: Sector RS** — constituent-weighted aggregation for 17 sectors | Richard + Watson | Most complex sheet — depends on approach chosen (proxy index vs constituent-weighted) |
| 3.2 | **Sheet 6: Sector Breadth** — replicate Sheet 5 methodology at sector level | Richard | Straightforward once Sheet 5 works |
| 3.3 | **VBA macro for breadth snapshots** — auto-log daily breadth values on open | Watson | Watson writes the VBA; Richard tests |
| 3.4 | **Backtest / sanity check** — compare dashboard signals against known industry moves in last 3-6 months | Richard + Watson | Does the system flag the rotations Richard already observed? |

### Phase 4: Integration (Day 9-10)

| Step | Task | Owner | Notes |
|------|------|-------|-------|
| 4.1 | **Dry-run morning workflow** — run through the full daily routine for 3 consecutive days | Richard + Watson | Identify friction points, missing data, unclear signals |
| 4.2 | **Watson Notion template** — create "Fit for Fighting" template in Notion for daily posts | Watson | Automated or semi-automated via Notion API |
| 4.3 | **Integrate with APM skill** — update `memory/skills/assistant-portfolio-manager/SKILL.md` to reference this tool and the daily workflow | Watson | |
| 4.4 | **Document in tools-and-data.md** — add workbook to the tool map | Watson | |

---

## 8. What Watson Needs from Richard

Before building, the following decisions are required:

### Must-Have (blocks Phase 1)

1. **Industry mapping confirmation** — Does the Viewforth → STOXX mapping in Section 4 look right? Particularly:
   - How should Industry C (Infra/Telecoms/Utes/Defence) be handled? Split for RS purposes, or keep as composite?
   - Is the K/N overlap (Basic Resources) correctly allocated?

2. **FactSet index ticker verification** — Can you look up the exact FactSet identifiers for SXXP and 3-4 industry indices? Once we have the naming convention, Watson can infer the rest

3. **FactSet refresh behaviour** — Does your FactSet Excel add-in auto-refresh on workbook open, or require manual refresh?

### Nice-to-Have (can refine later)

4. **Industries to exclude or special-weight?** — Industry H (1 constituent) is excluded. Any others? Should any industry get extra attention in the heatmap (e.g., larger row)?

5. **Workbook location** — Save to `COWORK/Files/` alongside the universe file? Or a different location?

6. **Breadth threshold preferences** — The 70%/30% thresholds are standard. Would you prefer different levels based on your experience?

7. **Additional breadth measures** — % above 200d MA as a secondary? New 52-week highs vs lows? These can be added later but worth flagging now

8. **Sector RS approach** — Constituent-weighted aggregation (more accurate, more formulas) or nearest STOXX proxy (simpler, less precise)?

---

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| FactSet formula complexity causes slow refresh | Medium | Workbook takes >60s to open | Limit constituent-level pulls; use FactSet batch functions where available |
| Industry mapping imprecision distorts RS signals | Medium | False rotation signals | Use constituent-weighted RS (Option A) for Richard's custom industries rather than STOXX proxies |
| Breadth with small n (<15) generates noise | High (for F, J, H) | Unreliable signals for small industries | Flag small-n industries visually; weight summary signals toward large-n industries |
| FactSet data gaps (missing prices, delisted tickers) | Low | Calculation errors | Add IFERROR wrappers to all FactSet formulas; log errors in a hidden sheet |
| VBA macro compatibility across machines | Low | Breadth history tracking breaks | Keep VBA simple; document macro code in this proposal for rebuild |

---

## 10. Future Extensions (Post-MVP)

Not for v1, but worth noting for later iterations:

1. **Stock-level RS rankings within industries** — extend Mansfield RS to individual stocks, rank within industry. Would surface the strongest names in rotating industries
2. **RS momentum scoring** — composite score (0-100) combining Mansfield RS, breadth, and rate of change. Easier to sort and filter than multiple columns
3. **Automated Notion posting** — Watson reads the workbook output (exported to CSV or via FactSet API) and posts "Fit for Fighting" without manual input
4. **Weekly RS report** — longer-form analysis of industry rotation trends, posted to Notion every Friday as part of the weekly review
5. **Integration with IG pipeline** — industries showing improving RS + rising breadth automatically surface as IG hunting grounds, feeding the ideas generation process
6. **Correlation with portfolio P&L** — track whether industry RS signals would have improved entry/exit timing on past positions

---

*[W] Watson — Systems Architect mode — 30 March 2026*
*Proposal for Richard's review. Awaiting decisions on Section 8 before proceeding to Phase 1.*
