# Block 1 Defect List — 28-Apr-26 morning
<!-- [W] Captured from Richard's local-file Chrome review with 12 screenshots. Source: Block 1 of "complete the dashboard today" plan. -->

## Source images
1. Image 1 — RATINGS view full table with 9 stocks, P1-P6 columns (visual baseline showing wrong pillar ratings for various stocks)
2. Image 2 — LIST view modal: HTRO comparison, ticker-selector dropdown overlapping rows
3. Image 3 — LIST view modal: HTRO comparison vs IGG/GET/DCC/EKTA — ratings/colours wrong for several stocks
4. Image 4 — MAP view modal: HTRO Summary Map V19 — all attribute ratings showing dashes (no ratings rendered)
5. Image 5 — RATINGS view: NEXT ACTION column text truncated with "..."
6. Image 6 — RATINGS view: UPDATED column title + 2026-04-15 format + line break splitting date across two lines
7. Image 7 — RATINGS view: HTRO row expanded — "Tree data not yet populated for this stock" instead of pillar cards / momentum table
8. Image 8 — NVTK row expanded showing the SS Earnings Momentum table layout (used as reference for restyle)
9. Image 9 — HTRO row expanded showing zeroed/blank SS Earnings Momentum data (0.0% across all rows, 0/15 score)
10. Image 10 — RATINGS view: SETUP column showing 6 different setup names ("Demand-Driven EPSU", "Corporate Change EPSU/EPT", "Earnings-Recovery EPSU/EPT", "CfC Margin Expansion", "Earnings Upgrade Cycle", "Corporate Change (HQI)")
11. Image 11 — RESEARCH STAGES tab showing 4 highlighted single-column ✓ markers per stage (one per IG/Triaging/ESA/DD audit-pass column)
12. Image 12 — RESEARCH STAGES tab showing the 3 APM columns (TRI/ESA/DD) + 1 AUDIT column highlighted

## Defect list (Richard's verbatim, numbered for tracking)

| # | Area | Defect | Reference |
|---|------|--------|-----------|
| D1 | RATINGS | P1-P6 visuals wrong for various stocks | Image 1 |
| D2 | LIST view | Ticker-selector dropdown needs scrolling | Image 2 |
| D3 | LIST view | Ratings (colours, ratings) not displaying correctly for various stocks | Image 3 |
| D4 | MAP view | Ratings not displaying for all stocks | Image 4 |
| D5 | RATINGS | NEXT ACTION column text truncated | Image 5 |
| D6 | RATINGS | UPDATED column → rename to LAST UPDATE; format DD-MMM-YY (e.g. 04-Apr-26); single line, no break | Image 6 |
| D7 | RATINGS | Column renames: SETUP → PRIMARY SETUP; STAGE → RESEARCH STAGE; REC → RECOMMENDATION | n/a |
| D8 | RATINGS | Clicking HTRO and all stocks except NVTK breaks the expanded view; text and ratings missing | Image 7 |
| D9 | RATINGS / SS Earnings Momentum panel | (a) Add median L1M/L3M/L6M for the stock's SECTOR, INDUSTRY, and MARKET. (b) Restyle: column widths, graphic design UX best practices, dashboard guidelines. Change ROW TOTAL → ROW SCORE. (c) Watson to suggest additional metrics — discuss first. | Image 8 |
| D10 | RATINGS / SS Earnings Momentum panel | Data looks incorrect for all stocks except NVTK | Image 9 |
| D11 | RATINGS | SETUP column: subtle but clear colour differentiation per setup type | Image 10 |
| D12 | RATINGS | Add 8 narrow columns on right side under master "RESEARCH STAGES" header. 4 cols (IG/Tri/ESA/DD audit-pass ticks) + 4 cols (3 APM memo cols TRI/ESA/DD + 1 AUDIT result). Cells clickable → navigate to RESEARCH STAGES tab with the stock in view. | Images 11, 12 |

## Status

- Block 1 defects: **12 captured, all open** as at 28-Apr-26 morning.
- Block 2 (10-ticker bake): **PAUSED** until Block 1 defects fixed and Richard signs off on visual changes.
- Pre-fix snapshot will be taken before any code mutation. Path: `databases/snapshots/2026-04-28-{HHMM}-pre-block1-fixes/`.
