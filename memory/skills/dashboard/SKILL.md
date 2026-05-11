# RS & Breadth Dashboard — SOP

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 07-Apr-26. Primary owner: APM role. -->

## Purpose

The RS & Breadth Dashboard is the APM role's primary tool for systematic momentum monitoring across the Viewforth universe (~1,400 European equities). It provides technical, fundamental, and Minervini screen data in a single self-contained HTML file, refreshed from FactSet Excel exports.

This SOP covers: architecture, data flow, refresh protocol, panel descriptions, maintenance rules, and known issues.

---

## Architecture

```
FactSet Excel (Files/Universe - YYYY_MM_DD.xlsx)
  ├── TIMESAVED sheet → source data timestamp (cell A1)
  ├── Universe sheet → company names + geography (display fields)
  └── FS sheet → returns, consensus, MAs, volume, ratings, TP
        ↓
Notion mapping (stock_mapping_final.json)
  └── Universe membership + taxonomy (Industry → Sector)
        ↓
generate_dashboard.py
  ├── Loads Notion universe (gates membership, provides taxonomy)
  ├── Reads FactSet Excel (financial data + display fields)
  ├── Deduplicates + removes no-price stocks
  ├── Computes derived fields (excess returns, RS/fund direction, MA flags)
  ├── Builds aggregations (industry, sector, geo)
  ├── Computes Minervini 8-point scores (Python, mirrors JS logic)
  ├── Updates rolling snapshot (snapshots/minervini-history.json, 14 days)
  ├── Computes entry/exit diffs for Changes tab
  └── Bakes everything into rs-breadth-dashboard.html as var D = {...}
        ↓
rs-breadth-dashboard.html
  └── Self-contained: all data, JS, CSS in one file. Opens in any browser.
```

**Key principle:** The HTML file is a snapshot. It contains no live data feeds. To update it, re-run the pipeline with a fresh Excel export.

---

## Files

| File | Purpose |
|------|---------|
| `rs-breadth-dashboard.html` | The dashboard. Self-contained HTML. |
| `generate_dashboard.py` | Pipeline script. Reads Excel + Notion → HTML. |
| `stock_mapping_final.json` | Notion universe export. Defines membership + Industry/Sector taxonomy. |
| `audit_dashboard_coverage.py` | Coverage audit: compares Notion mapping vs FactSet Excel. Run before pipeline. |
| `tmp_industries_lookup.json` | Industry page URL → name lookup (16 entries, for Notion sync). |
| `Files/Universe - YYYY_MM_DD.xlsx` | FactSet data export. Richard saves new versions as needed. |
| `snapshots/minervini-history.json` | Rolling 14-day Minervini score history. One entry per day per stock. |

---

## Refresh Protocol

### When to refresh
- Richard says "refresh dashboard", "update dashboard", or similar
- After Richard confirms a new FactSet Excel export is saved and closed
- As part of daily morning routine (if fresh data is available)

### Steps

1. **Run the pipeline:**
   ```bash
   cd /sessions/*/mnt/COWORK && python generate_dashboard.py
   ```
   Auto-detects latest `Files/Universe - YYYY_MM_DD.xlsx`. To specify a file:
   ```bash
   python generate_dashboard.py "Files/Universe - YYYY_MM_DD - V2.xlsx"
   ```

2. **Verify output:** Check console for stock count, coverage stats, snapshot confirmation. Report to Richard: which file used, source timestamp, refresh timestamp, stock count, any gaps.

3. **Present the file:** Share `rs-breadth-dashboard.html` so Richard can open it.

### Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `BadZipFile: File is not a zip file` | Excel file is open/locked on Richard's machine | Ask Richard to save and close the file. Or use a V2 copy. |
| Missing `ma_200d_5m` / `ma_200d_6m` | New columns not in the Excel export | Verify columns CQ (95) and CR (96) contain data in the FS sheet |
| Stock count lower than expected | Notion mapping doesn't include the ticker | Check `stock_mapping_final.json` for missing tickers |

---

## Panel Descriptions

**Panel order (left to right):** Minervini | Score Changes | Category Changes | Technical | SS Earnings Momentum | Combined | Stock (hidden, opens on ticker click)

**Tab label history:** "Fundamental" was renamed to "SS Earnings Momentum" on 20-Apr-26 to clarify that the panel surfaces sell-side consensus revisions (the leading indicator of sell-side earnings momentum), not standalone fundamental analysis. "VF Fundamentals" was renamed to "VF Tagging" on the same day. Internal panel state names (`fundamental`, `vfFundamentals`) were intentionally NOT renamed — label-only change to minimise blast radius.

### 1. Technical (Relative Strength & Breadth)
- **Metrics:** Excess returns (1D/1W/1M/3M vs equal-weight universe mean), MA breadth (% above 20D/50D/200D), positivity breadth, RS direction (rising/flat/falling)
- **Views:** Industry, Sector, Geography — all drill down to constituent stocks
- **Modes:** Relative (vs benchmark) or Absolute returns
- **Sorting:** By timeframe return or alphabetical
- **Stock detail:** Click any ticker for single-stock view with returns, MA position, volume

### 2. SS Earnings Momentum (Consensus Estimate Revisions)
- **Layout:** Industry/Sector group summary at top, then ALL STOCKS section below
- **ALL STOCKS columns:** Ticker, Company, Sector, Price (contextual dp: <10→2dp, 10-100→1dp, >100→0dp), L1M revisions (EPS/EBITDA/Sales/PT/%Buy), L3M revisions, L6M revisions, Validation Checks (5 criteria)
- **Toggles in ALL STOCKS filter bar:**
  - FY1/FY2 toggle (default FY2) — switches revision columns between FY1 and FY2 data
  - Checks TF toggle (1M/3M/6M, default 3M) — changes Validation Check timeframe
  - 5 Validation Check filter buttons (EPS/EBITDA/Rev/TP/Δ%Buy) — filter to stocks passing selected checks
- **Validation Checks:** EPS upgrade (>0), EBITDA upgrade (>0), Revenue upgrade (>0), TP upgrade (>0), %Buy increase (>0). Timeframe controlled by Checks TF toggle.
- **Stock detail:** Revisions table + ratings & breadth grid

### 3. Minervini 8 Points (Advancing Screen)
- **8 criteria in 4 categories:**
  - Long-term Trend (LT): Price > 200D, 200D trending up (1-6M)
  - Stage 2 ID (S2): Price > 150D, 150D > 200D
  - ST Momentum (ST): 50D > 150D, Price > 50D
  - Leadership (LD): Price > 30% above 52W low, Price within 25% of 52W high
- **Summary tables:** Industry and Sector, showing % meeting each threshold (8/8, 7+, 6+, 5+) and category pass rates (LT, S2, ST, LD). Sortable by any threshold. Clickable to filter All Stocks.
- **All Stocks table:** Full list with inline filters (score threshold + category toggles LT/MT/ST/LD). Default filters: all 4 categories ON, sorted by Industry → Sector → Company.
- **4 Cumulative Criteria Sections** (below All Stocks): LT Only, LT+MT, LT+MT+ST, All 4 — each as a separate card section with coloured top border, showing stocks meeting that cumulative filter set
- **KPIs:** Universe count, Pass 8/8, Score 7+, 6+, 5+
- **Stock detail:** 3-column layout (Technical / Fundamental / Minervini) with 52W range bar and MA markers

### 4. Changes (Daily Entry/Exit Tracking)
- **Shows:** Which stocks entered or exited each threshold (8/8, 7+, 6+, 5+) compared to each prior day in the rolling 14-day window
- **Layout:** Threshold toggle at top. Per-day cards with side-by-side entry (green) and exit (red) tables. Net change indicator.
- **Data source:** `snapshots/minervini-history.json` — Python computes diffs at pipeline time and bakes them into the HTML.
- **Requires:** At least 2 daily refreshes to show any changes. First refresh = baseline only.
- **Stock detail:** Tickers are clickable to drill into single-stock view.

### 5. Combined (Technical + Fundamental + Minervini)
- **Layout:** ALL STOCKS first, then Industries, then Sectors below
- **ALL STOCKS columns:** Ticker/Company (toggle), Industry, Sector, Score, Price, Price Levels (6 cols: 52Hi/52Lo/50D/150D/200D/20D), Minervini criteria (4 Cat or 8 Sub toggle), Fundamental revisions (EPS/Rev/EBITDA 1M/3M/6M + TP 1M), Validation Checks (5 cols)
- **Sortable columns:** Ticker/Company, Industry, Sector, Score — click header to toggle asc/desc with arrow indicators
- **Filter bar toggles:**
  - Ticker/Company name toggle
  - Category filters (LT/MT/ST/LD) — colour-coded multi-select
  - Criteria mode (4 Cat / 8 Sub)
  - Prices mode (Abs / % from current)
  - Checks filter (EPS/EBITDA/Rev/TP/Δ%Buy) — filter to stocks passing selected checks
  - Checks TF (1M/3M/6M, default 3M) — controls Validation Check timeframe (shared with Fundamental page via `fundValTF`)
- **Industry/Sector click-to-filter:** Click a name in summary tables to filter All Stocks
- **Industries/Sectors tables:** Below All Stocks, with their own Criteria and Prices toggles

### 6. Score Changes (new name: was "Changes")
- Same as described in panel 4 above

---

## FactSet Excel Column Mapping (FS Sheet)

| Cols | Index | Data |
|------|-------|------|
| A | 1 | Ticker |
| B-F | 2-6 | Returns: 1D, 1W, 1M, (skip), 3M |
| H | 8 | Price |
| I-J | 9-10 | 52W Low, 52W High |
| K | 11 | Market Cap |
| AD | 30 | Geography |
| AW-BA | 49-53 | EPS snapshots: now, -1M, -3M, -6M, -12M |
| BC-BG | 55-59 | EBITDA snapshots: now, -1M, -3M, -6M, -12M |
| BI-BM | 61-65 | Sales snapshots: now, -1M, -3M, -6M, -12M |
| BP-BS | 68-71 | Target price: current, -1M, -3M, -6M |
| BT-BX | 72-76 | Ratings: %Buy, %Hold, %Sell, Buy 1M ago, Buy 3M ago |
| BY-BZ | 77-78 | Revision breadth: EPS up 1M, EPS down 1M |
| CB-CE | 80-83 | Moving averages: 20D, 50D, 150D, 200D |
| CG-CJ | 85-88 | Volume: 1D, avg 5D, avg 20D, avg 50D |
| CM-CP | 91-94 | 200D MA historical: 1M, 2M, 3M, 4M ago |
| CQ-CR | 95-96 | 200D MA historical: 5M, 6M ago |

FY2 consensus data uses the same structure but offset columns (defined in `generate_dashboard.py`).

---

## Minervini Scoring — Dual Implementation

**IMPORTANT:** The Minervini 8-point scoring logic exists in two places:
- **JavaScript** (`minCriteria` in `rs-breadth-dashboard.html`) — runs live in the browser for the Minervini tab, stock detail view, and KPIs
- **Python** (`compute_minervini_score` in `generate_dashboard.py`) — runs at pipeline time for snapshot history and Changes tab diffs

These must stay in sync. If criteria or thresholds change, both must be updated. The criteria are:

| # | Criterion | Pass condition | Category |
|---|-----------|----------------|----------|
| 1 | Price vs 200D MA | > 0% | Long-term Trend |
| 2 | 200D MA trend | Rising for >= 1 month | Long-term Trend |
| 3 | Price vs 150D MA | > 0% | Stage 2 ID |
| 4 | 150D vs 200D MA | > 0% | Stage 2 ID |
| 5 | 50D vs 150D MA | > 0% | ST Momentum |
| 6 | Price vs 50D MA | > 0% | ST Momentum |
| 7 | Price vs 52W Low | > 30% | Leadership |
| 8 | Price vs 52W High | >= -25% | Leadership |

Category pass = both criteria in that category pass. Used for LT/S2/ST/LD summary columns and filter buttons.

---

## Snapshot & Change Tracking

- `snapshots/minervini-history.json` stores `{date: {ticker: score}}` for each day the pipeline runs
- Trimmed to 14 days automatically
- Diffs computed: for each prior day, entries = stocks meeting threshold today but not then; exits = stocks meeting then but not today
- Change data baked into `var D.minervini_changes` with full ticker/company/sector/score for display
- Changes tab shows all prior days with entry/exit tables and net change

---

## Maintenance Rules

1. **Never overwrite the HTML manually.** Always re-run the pipeline. The pipeline preserves all JS/CSS logic and only replaces the `var D = {...}` data block.
2. **Snapshot file is append-only** (within the 14-day window). Don't manually edit `minervini-history.json`.
3. **Notion mapping is the source of truth for universe membership and taxonomy.** If a stock is missing, check `stock_mapping_final.json` first.
4. **Excel must be closed before running.** `openpyxl` can't read locked files. Use a V2 copy if the original is locked.
5. **If scoring logic changes, update both Python and JS.** See "Dual Implementation" section above.
6. **Always run coverage audit before pipeline.** `python audit_dashboard_coverage.py` checks Notion mapping vs FactSet Excel alignment. If gaps found, Richard adds missing tickers to FactSet before proceeding.
7. **Universe changes require Notion sync first.** When stocks are added/removed/reclassified in Notion, Watson runs the incremental Notion sync (Step 0 of refresh skill) to update `stock_mapping_final.json` before the pipeline.

Full refresh protocol: `memory/skills/refresh-dashboard/SKILL.md`

---

## APM Integration

This dashboard is the APM role's primary momentum monitoring tool. It directly supports:

- **Daily RS Check** (Minervini Daily Protocol, 10 min) — open dashboard, scan held positions, scan watchlist, check breadth, make one decision
- **Momentum Health Check** (weekly standing duty) — combine Technical + Fundamental signals on held positions; RED FLAG if RS falling AND fundamental downgrading AND negative excess returns
- **Exit Discipline Enforcement** — deteriorating Minervini scores and RS direction are evidence for 30-day shot clock activation
- **Pipeline Scanning** — use Minervini tab to identify Stage 1→2 transitions on watchlist names; use Changes tab to spot newly qualifying stocks
- **Industry/Sector Rotation** — Technical panel breadth data shows which industries have positive momentum; informs risk-on/risk-off positioning

Full APM protocols: `memory/skills/assistant-portfolio-manager/SKILL.md`

### Cross-Role Integration [D] (07-Apr-26)

The dashboard is not just an APM monitoring tool — it is a **major input to Ideas Generation and Workflow Planning**. This links it to:
- **Chief of Staff role** — uses dashboard signals to prioritise which pipeline stocks get research attention next (workflow planning)
- **Researcher role** — dashboard IG scans (Minervini entries, improving breadth, fundamental upgrades) feed directly into the IG stage of the 6-stage process
- **APM role** — momentum monitoring, exit discipline, held position health checks

The dashboard therefore sits at the intersection of three roles and informs what Richard works on, not just what he monitors.
