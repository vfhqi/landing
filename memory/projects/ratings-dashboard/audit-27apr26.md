# IC Ratings Dashboard — Comprehensive Audit Report
<!-- [W] 27-Apr-26 15:15 UK -->

## Summary

**Overall: PASS (with 2 bugs noted)**

Tested live on GitHub Pages (`https://vfhqi.github.io/dashboards/index.html`) via Chrome. All core functionality working. Zero JS errors. Two data-layer bugs identified (non-blocking).

## Environment

- URL: `https://vfhqi.github.io/dashboards/index.html?nocache=1777298400`
- Commit: `0f5880d` (cache-bust rebuild, 27-Apr-26 14:52 UK)
- File size: 5,203,516 bytes (local), 5,203,548 bytes (repo, +32 bytes cache-bust comment)
- Stocks in masterData: 3 (NVTK, HTRO, IGG)
- RESEARCH STAGES tickers: 55

## Test Results

### 1. RATINGS View — PASS
- 3 stock rows render correctly with all columns (Ticker, Company, Stage, MAP, LIST, MEMO, P1-P6, Setup, Fulcrum Driver, Rec, Next Action, Updated)
- Expand arrows (►/▼) work — show 6-pillar cards per stock
- Rating chips (A-F) colour-coded correctly
- PROGRESS recommendation badges render
- Warm cream theme consistent

### 2. MAP Button — PASS
- Opens full-screen overlay with Investment Case Change AFs
- AF #1 Required Case Outputs, AF #2 Required Case Inputs, AF #3 Setups
- Building Blocks sections (BB#1-BB#8) with sub-items and rating indicators
- Close button works

### 3. LIST Button — PASS
- Opens checklist comparison view
- 6 sections (I-VI) with sub-items and rating chips
- Multi-stock comparison columns ("+ SELECT CLICK TO CHOOSE")
- Close button works

### 4. MEMO Button — PASS
- Opens FCS Memo with stage toggle (Triaging/ESA/DD)
- Stage toggle switches content correctly:
  - DD: 37pp | 11,031 words, Section B = 3pp/971w
  - Triaging: 21pp | 5,684 words, Section B = 2pp/479w
- Sections confirmed rendering:
  - A: FINANCIALS (with word counts per stage)
  - B: Investment case - executive summary (BLUF, IAJA-tagged bullets)
  - C: REQUIRED ATTRIBUTES (graphical P1-P6 cards, SINGLE/MULTI-STAGE toggle, ratings table with hierarchical IDs)
- IAJA tagging: [J], [A], [I], [ACT] prefixes render correctly
- Underlined text, blockquotes, nested bullet lists all render

### 5. Toolbar Toggles — PASS
- JUDGEMENTS: toggles on/off independently
- ANALYSIS: toggles on/off, shows pillar group headers
- KEY: toggles on/off
- FUNDAMENTAL: toggles on/off, shows pillar group headers
- COLOUR: toggles rating legend (A/B/C/D/F/Not Rated with colour swatches)
- Multiple toggles can be active simultaneously
- Pillar group headers appear: TIMELINESS (P1-P2), CASE STRENGTH (P3-P4), MARKET RECOGNITION (P5), POTENTIAL RETURN (P6)

### 6. Sort & Filter (RATINGS) — PASS
- STAGE dropdown: All, IG, Triaging, ESA, DD, Live — filtering works
- STATUS dropdown: All, Active, Paused, Closed
- SORT BY dropdown: Stage, Ticker, P3 (Fundamental Change), Last Updated

### 7. RESEARCH STAGES Tab — PASS
- Toolbar button "RESEARCH STAGES" renders in correct position
- Cream theme matches RATINGS view (not dark navy)
- Fits on one screen without horizontal scrolling (table-layout: fixed, 10px font)
- Summary stat cards: Tickers (55), In Dashboard (55*), Queries Done (207), High Priority (19), Audit Pass (12/55)
- 5 sort buttons: Ticker, Queries, Words, Stage, Priority — all toggle asc/desc
- Filter input: tested "DCC" (1 result), "EK" (1 result EKTA), clear returns all 55
- Ticker click-through: exits coverage view → RATINGS (works for baked-in stocks)
- Column headers grouped by stage (IG, TRIAGING, ESA, DD, ANY, APM MEMOS)
- Colour-coded cells (green/olive/amber for word count thresholds)
- Notion posting dots (●) visible
- AUDIT column: PASS/FAIL per ticker
- NEXT ACTION column: truncated text with priority colouring

### 8. Console Errors — PASS
- Zero errors on page load
- Zero errors across all view switches (RATINGS → JUDGEMENTS → ANALYSIS → KEY → FUNDAMENTAL → COLOUR → RESEARCH STAGES → sorts → back)
- Zero warnings

## Bugs Found

### BUG-1: "IN DASHBOARD" stat shows 55 (should show 3)
- **Severity:** Low (cosmetic/informational)
- **Location:** RESEARCH STAGES summary card, second stat box
- **Expected:** Count of tickers that are baked into `masterData.stocks` (currently 3: NVTK, HTRO, IGG)
- **Actual:** Shows 55 (same as total ticker count)
- **Root cause:** `build-coverage-data.py` likely doesn't check `masterData` — it counts all tickers in the coverage JSON
- **Fix:** Either (a) have the JS count tickers that exist in `masterData.stocks`, or (b) have the build script flag which tickers are baked in

### BUG-2: Stock count mismatch — 3 stocks vs expected 8+
- **Severity:** Medium (data gap, not a code bug)
- **Location:** `masterData.stocks` in dashboard HTML
- **Expected:** 8 stocks (NVTK, HTRO, IGG, ENAV, EKTA, DCC, GET, PRY, DIE) per previous bake sessions
- **Actual:** Only 3 stocks (NVTK, HTRO, IGG) in current HTML
- **Root cause:** The coverage tab patcher (`patch-coverage-tab.py`) may have been run on a pre-bake version of the dashboard, or the baked stocks were lost during a file operation. Memo JSONs for all 8+ stocks exist in `databases/memos/`.
- **Fix:** Re-run the bake scripts (`bake-batch-v3-memos.py` etc.) to inject all memo JSONs back into the dashboard HTML, then re-run the coverage patcher.

## DCC-Specific Assessment

DCC cannot be fully tested in this audit because it is not baked into `masterData.stocks`. The RESEARCH STAGES tab shows DCC's coverage data (research queries, audit status, next action), and clicking DCC in the coverage table correctly exits to the RATINGS view — but DCC doesn't appear in the RATINGS table because it has no `masterData` entry.

To test DCC's MEMO view (stage toggle, sections A-F, ratings table), the DCC memo JSONs (`databases/memos/DCC/Triaging-v3.json`, `ESA-v3.json`) need to be baked into the dashboard.

## Recommendations

1. **Re-bake all stocks** — Run bake scripts to restore ENAV, EKTA, DCC, GET, PRY, DIE into `masterData`. This is the highest-priority fix.
2. **Fix "IN DASHBOARD" stat** — Update JS to count `masterData.stocks.length` instead of total coverage tickers.
3. **Push after re-bake** — Use `scripts/push-dashboard.sh` to deploy the full-stock dashboard to GH Pages.
