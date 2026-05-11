# Pullback Monitor — Pipeline Error Report
**Date:** 2026-04-16  
**Run time:** ~06:17 BST  
**Triggered by:** watson-task-executor (scheduled overnight run)

---

## Summary

**Result: FAILED — 0 / 137 stocks processed**

The pipeline ran to completion but produced zero data due to a **network proxy block** in the Cowork sandbox environment. The sandbox cannot make outbound HTTPS CONNECT tunnel requests to Yahoo Finance (api.finance.yahoo.com). All tickers returned `curl: (56) CONNECT tunnel failed, response 403`.

---

## Root Cause

- **Error:** `Failed to perform, curl: (56) CONNECT tunnel failed, response 403`
- **Cause:** Cowork sandbox has allowlisted network access only. Yahoo Finance (yfinance) requires outbound HTTPS tunnelling which is blocked by the environment's proxy.
- **Not a script bug:** The script logic is sound. The issue is environmental.
- **Not a ticker 404:** All failures are proxy-level blocks, not missing tickers.

---

## What Was Produced

- `pullback-data.json` was updated at 06:17 BST but contains 0 stocks:
  - File size: 331 bytes (skeleton/metadata only)
  - `"stock_count": 0`, `"stocks": []`
- HTML injection ran but embedded 0 stocks into `pullback-monitor.html` and `rs-breadth-dashboard.html`

---

## Recommended Fix

The `generate_pullback_data.py` script must be **run locally on Richard's machine** (Windows), not inside the Cowork sandbox. Options:

1. **Run script locally via Windows Task Scheduler** — Schedule `python generate_pullback_data.py` at 06:00 BST daily from `C:\Users\richb\Documents\COWORK\`. Cowork can then read the pre-generated `pullback-data.json`.
2. **Manual run** — Richard opens PowerShell, `cd C:\Users\richb\Documents\COWORK`, runs `python generate_pullback_data.py`.
3. **Watson reads pre-generated file** — If Richard runs the script locally, Watson can analyse and report on the JSON output in the next session.

---

## Action Required

→ Richard to run `generate_pullback_data.py` locally on his Windows machine.  
→ Watson cannot execute yfinance from within the Cowork sandbox due to proxy restrictions.

---

---

## Second Attempt — 2026-04-16 23:40 BST (pullback-monitor-nightly)

Same result. Scheduled task triggered at 23:40 BST. All 979 fetch attempts failed with identical `curl: (56) CONNECT tunnel failed, response 403` error. 0 stocks scored. `pullback-data.json` overwritten with empty skeleton (331 bytes). HTML dashboards injected with 0 stocks.

**This is a persistent infrastructure issue — the scheduled task cannot run this pipeline from within the Cowork sandbox.**

*Report updated by Watson (automated scheduled task)*

---

## Third Attempt — 2026-04-17 23:40 BST (pullback-monitor-nightly)

Same result. Scheduled task triggered at 23:40 BST. All 977 fetch attempts failed with identical `curl: (56) CONNECT tunnel failed, response 403` error. 0 stocks scored. `pullback-data.json` overwritten with empty skeleton (331 bytes). HTML dashboards injected with 0 stocks.

**This is a persistent infrastructure issue — the scheduled task cannot run this pipeline from within the Cowork sandbox.**

The only resolution is to run `generate_pullback_data.py` directly on Richard's Windows machine. Consider setting up Windows Task Scheduler locally as a permanent fix.

*Report updated by Watson (automated scheduled task)*

---

## Fourth Attempt — 2026-04-18 23:41 BST (pullback-monitor-nightly)

Same result. Scheduled task triggered at 23:41 BST. All 979 fetch attempts failed with identical `curl: (56) CONNECT tunnel failed, response 403` error. 0 stocks scored. `pullback-data.json` overwritten with empty skeleton (331 bytes). HTML dashboards injected with 0 stocks. Watchlist now shows **976 stocks** (up from 137 originally documented in the task).

**This is a persistent infrastructure issue — four consecutive failures. The scheduled task cannot run this pipeline from within the Cowork sandbox.**

The only resolution is to run `generate_pullback_data.py` directly on Richard's Windows machine. Recommend deactivating or pausing this scheduled task until Windows Task Scheduler is set up locally.

*Report updated by Watson (automated scheduled task)*
