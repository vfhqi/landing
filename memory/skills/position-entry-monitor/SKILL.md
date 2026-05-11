# Position Entry Monitor — SOP

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 15-Apr-26. Renamed from Pullback Monitor 16-Apr-26. Primary owner: APM role. -->

## Purpose

The Position Entry Monitor is the APM's tool for timing capital deployment into stocks Richard has already decided to buy. It watches a manually curated watchlist and scores each stock daily against 10 diagnostic signals for healthy pullback retests of moving averages, and 5 EWS (Early Warning System) binary signals for Probing Bet entry.

**This is NOT a screening tool** (that's the RS & Breadth Dashboard). This is an execution timing tool — it answers "when to buy," not "what to buy."

**Two entry types supported:**
- **18M MM Slugs** — full 8/8 Minervini criteria; composite score 6+ is the primary signal
- **Probing Bets** — pre-8/8 entry; use EWS filter (3+ ticks = setup forming, 5 ticks = ready). SL on 20D or 50D depending on which MA is rising.

**Secondary role (16-Apr-26):** The monitor is also the primary data source for Query #3 (Technical Momentum) in the RESEARCHER role. When Watson runs IG on any stock, it checks the monitor first. For covered stocks, monitor data replaces FactSet charts and `extract_tm_data.py`. Chart screenshots from `position-entry-monitor.html` are embedded directly in Notion. See RESEARCHER SKILL-V2.md §IG Execution and template `03-ig-tm.md` for full protocol.

---

## Architecture

```
pullback-watchlist.json (Richard adds/removes tickers; Watson adds automatically when running IG Query #3 for uncovered stocks)
    ↓
yfinance (daily OHLCV, 6M lookback, ~125 trading days)
    ↓
generate_pullback_data.py
  ├─ Computes 7 SMAs (5/10/20/50/100/150/200D)
  ├─ Detects swing highs (10-day rolling window)
  ├─ Scores 10 diagnostic signals (composite max 7.0)
  ├─ Computes 5-signal EWS (SP>5D, 5D↑, 10D↑, 20D↑, 50D↑) + tick count
  ├─ Generates chart data (OHLCV + all 7 MAs + volume)
  ├─ Reads IC Ratings DB for Pillar III (Signal 7)
  └─ Outputs pullback-data.json → injects var PB into position-entry-monitor.html
        ↓
position-entry-monitor.html (standalone dashboard)
  ├─ EWS filter bar: show stocks with ≥1/2/3/4/5 ticks
  ├─ Summary table: composite score, signal heatmap, EWS columns, tick count
  ├─ Per-stock detail: EWS breakdown, signal scores, MA distances, charts, IC Ratings, Fund Momentum
  └─ Red flag badges: DIST / RETRACE / STAGE_BREAK
```

---

## Files

| File | Purpose |
|------|---------|
| `pullback-watchlist.json` | Watchlist. Richard adds/removes stocks; Watson adds automatically when running IG Query #3 for uncovered stocks. |
| `generate_pullback_data.py` | Pipeline script. yfinance → signals → EWS → JSON/HTML. |
| `pullback-data.json` | Output data file (standalone mode). |
| `position-entry-monitor.html` | Standalone dashboard HTML. |
| `databases/master/ic-ratings-current.json` | Pillar III ratings for Signal 7. |
| `stock_mapping_final.json` | Industry/Sector taxonomy for RS benchmarks. |

---

## Refresh Protocol

### When to refresh
- Daily (morning routine) — run with live yfinance data
- When Richard adds a stock to the watchlist
- Before any entry decision

### Steps

1. **Run the pipeline locally on Windows:**
   ```bash
   cd C:\Users\richb\Documents\COWORK && python generate_pullback_data.py
   ```
   
   Options:
   - `--sample` — use sample data (testing, no internet required)
   - `--json-only` — output JSON file only, don't inject into dashboard
   - `--factset FILE` — cross-check against FactSet Excel export

   **IMPORTANT:** The pipeline must be run locally on Richard's Windows machine. The Cowork sandbox cannot reach Yahoo Finance (proxy restriction). Watson reads pre-generated `pullback-data.json` — it cannot regenerate it from within the sandbox.

2. **Review output:** Console shows per-stock summary with scores, depth, days, and red flags.

3. **Open dashboard:** Open `position-entry-monitor.html` in browser. Click any stock row to expand detail panel.

### Adding a stock to the watchlist

Richard can edit `pullback-watchlist.json` directly. Watson adds stocks automatically when running IG Query #3 for a stock not yet on the watchlist — Watson adds the entry then prompts Richard to run `python generate_pullback_data.py`. Required fields:
```json
{
  "ticker": "HTRO-SE",
  "yfinance_ticker": "HTRO.ST",
  "company_name": "Hoist Technology Group",
  "date_added": "2026-04-15",
  "notes": "Stage 2 confirmed. Waiting for first pullback to 50D.",
  "target_ma": "50D",
  "industry": "Technology",
  "sector": "IT Services"
}
```

Exchange suffixes: `.ST`=Stockholm, `.L`=London, `.AS`=Amsterdam, `.DE`=Frankfurt, `.CO`=Copenhagen, `.SW`=Swiss, `.PA`=Paris, `.MC`=Madrid, `.HE`=Helsinki, `.OL`=Oslo.

---

## EWS — Early Warning System (5 binary signals)

EWS indicates when a Probing Bet setup is forming. It does NOT replace the composite signal score for 18M MM Slug entries.

| # | Signal | What it measures | True if |
|---|--------|-----------------|---------|
| 1 | **SP > 5D MA** | Price above very short-term trend | Close > 5D SMA |
| 2 | **5D MA rising** | Short-term momentum turning up | 5D SMA today > 5D SMA yesterday |
| 3 | **10D MA rising** | Medium short-term momentum | 10D SMA today > 10D SMA yesterday |
| 4 | **20D MA rising** | 20D trend direction | 20D SMA today > 20D SMA yesterday |
| 5 | **50D MA rising** | Intermediate trend direction | 50D SMA today > 50D SMA yesterday |

**Tick count interpretation:**

| Ticks | Meaning | Action |
|-------|---------|--------|
| 5/5 | Setup fully formed | Consider Probing Bet (SL on 20D or 50D as applicable) |
| 4/5 | Setup nearly formed | Watch closely — likely entry in 1-2 days |
| 3/5 | Setup forming | On radar — monitor daily |
| 0-2 | Too early | Not actionable yet |

**Probing Bet entry criteria:**
- SP > 20D MA AND 20D rising → SL on 20D MA
- OR SP > 50D MA AND 50D rising → SL on 50D MA
- Use EWS filter (≥4 ticks) to surface candidates

---

## Signal Framework (10 components, composite max 7.0)

### Core Signals (weight 1.0 each)

| # | Signal | What it measures | Pass | Amber | Fail |
|---|--------|-----------------|------|-------|------|
| 1 | **Depth contained** | % from swing high | <15% | 15-25% | >25% |
| 2 | **150D MA holds** | Price above rising 150D | Above + rising | Within 2% | Below or declining |
| 4 | **VCP intact** | Current PB shallower than prior | Shallower by 2pp+ | Similar (±2pp) | Deeper |
| 5 | **RS holding** | vs Market + Industry + Sector | Positive vs all 3 | Positive vs 2/3 | Negative vs 2+ |
| 6 | **Recovery speed** | Days since pullback started | <30 days | 30-60 days | >60 days |
| 7 | **Fundamental context** | Pillar III from IC Ratings DB | A or B | C | D or F |

### Volume-Price Quality Signals (weight 0.5 each)

| # | Signal | What it measures | Pass | Amber | Fail |
|---|--------|-----------------|------|-------|------|
| 3a | **Down-day volume** | Down-day vol vs 50D avg | <70% of avg | 70-100% | >100% (distribution) |
| 3b | **Up/down ratio** | Up days vs down days in PB | >0.8 | 0.5-0.8 | <0.5 |
| 3c | **Candle quality** | Close position on up days | >60% (strong) | 40-60% | <40% (weak closes) |

### Penalty-Only Signals (weight 0.5, no bonus for pass)

| # | Signal | What it measures | Neutral | Amber | Fail |
|---|--------|-----------------|---------|-------|------|
| 3d | **Distribution days** | Consecutive down + rising vol | 0 | 1-2 | 3+ (RED FLAG) |
| 3e | **Rapid retracement** | Advance wiped in N/5 days | Absent | — | Present (RED FLAG) |

### Composite Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 6.0-7.0 | **STRONG** (green) | Retest forming — consider deploying capital (18M MM Slug) |
| 4.0-5.9 | **WATCHING** (amber) | Setup developing, monitor daily |
| 0-3.9 | **WEAK** (red) | Not yet / deteriorating — do not deploy |

---

## Red Flags

Four standalone red-flag badges in the summary table. ANY red flag = investigate before deploying:

- **DIST: N** — N consecutive down-days on above-average or increasing volume (N ≥ 3)
- **RETRACE** — Rapid retracement detected (advance wiped in N/5 days)
- **200D BREAK** — Price below 200D MA (potential Stage 2 → Stage 3)
- **VIOLATIONS** — 3+ of Minervini's 8 violation signals triggered simultaneously → immediate exit review

---

## MA Alert Tiers

| Tier | MAs | Meaning |
|------|-----|---------|
| **PRIMARY** (green) | 50D, 150D | Minervini sweet spots for entry. Price within 2% of these MAs. |
| **SECONDARY** (blue) | 20D, 100D | Lighter signals. Often noise. |
| **WARNING** (red) | 200D | Potential stage break. Not a buy signal. |

---

## Pullback Detection

**Swing high algorithm:** Identifies the most recent local price peak — the highest close in a rolling 10-day window that is also higher than the 5 days either side. The pullback period runs from that peak to today.

A stock is "in pullback" when it is >2% below its swing high.

---

## FactSet Weekly Calibration

When Richard provides a fresh FactSet Excel export, run:
```bash
python generate_pullback_data.py --factset "Files/Universe - YYYY_MM_DD.xlsx"
```

The script compares yfinance closes vs FactSet closes and flags divergences >1%.

---

## Integration Points

- **IC Ratings DB** (`databases/master/ic-ratings-current.json`): Signal 7 reads Pillar III rating
- **RS & Breadth Dashboard**: Industry/Sector taxonomy from `stock_mapping_final.json` for Signal 5 benchmarks
- **Monitoring Plan** (`databases/monitoring/monitoring-plan.json`): Red flags from Position Entry Monitor should feed into monitoring plan reviews

---

## Relationship to Other APM Tools

| Tool | Purpose | Handoff |
|------|---------|---------|
| RS & Breadth Dashboard | Screening — WHICH stocks are in Stage 2 | Stocks scoring 8/8 → candidate for watchlist |
| Position Entry Monitor | Timing — WHEN to deploy capital | Strong score (6+) → 18M MM Slug; 4+ EWS ticks → Probing Bet |
| Position Management (future) | Capital — HOW MUCH to deploy | After entry decision → tranche management |
| IC Ratings Dashboard | Fundamental — IS the case intact? | Pillar III feeds Signal 7 |

---

## Future Enhancements (Post-V1)

- [ ] Integration as tab in RS & Breadth Dashboard (currently standalone)
- [ ] Industry/Sector RS benchmarks computed from RS Dashboard data (currently Market-only)
- [ ] Automated scheduling (daily cron via Watson task executor — blocked by proxy; must run locally)
- [ ] Historical signal snapshots (rolling 14-day like Minervini Changes tab)
- [ ] Notification system (Notion post when stock hits 6+/7 or 5 EWS ticks)
- [ ] FactSet auto-calibration (compare and flag divergences automatically)
