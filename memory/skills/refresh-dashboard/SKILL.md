# Refresh Dashboard Skill

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.


## Purpose
Re-generate the RS & Breadth Dashboard (`rs-breadth-dashboard.html`) with fresh data. Includes universe sync (Notion → mapping file), FactSet coverage audit, and pipeline execution.

**Full dashboard SOP:** `memory/skills/dashboard/SKILL.md` — covers architecture, all 6 panels, column mapping, snapshot system, maintenance rules.

## When to use
- Richard says "refresh dashboard", "update dashboard", "re-run the dashboard"
- After Richard confirms he has saved a new FactSet Excel export
- As part of daily morning routine (if fresh data available)
- After adding new stocks to the Notion Stocks DB

---

## Full Refresh Protocol (4 steps)

### Step 0. Notion Universe Sync (if stocks/taxonomy may have changed)

**When to run:** Always run if Richard has added, removed, or reclassified stocks in Notion since the last refresh. Skip if it's a pure data refresh (same universe, new prices).

**Procedure — Incremental Sync:**
Watson queries the Notion Stocks DB for recently created or modified entries and updates `stock_mapping_final.json`.

1. **Check for new stocks** — Query Notion Stocks DB (`collection://25435e90-9b0b-80ec-909d-000ba746fa2d`) using the "Simple" view. The view returns ~100 stocks per query (sorted alphabetically). Compare returned tickers against `stock_mapping_final.json`.

2. **For any new/changed tickers**, resolve their Industry and Sector relation URLs:
   - Industry lookup: `tmp_industries_lookup.json` (16 entries, page URL → name)
   - If Industry URL not in lookup, fetch the page via Notion to get the name
   - Sector: fetch the Sector page via Notion to get the name (no complete lookup exists)

3. **Update `stock_mapping_final.json`:**
   - Add new entries: `"TICKER": {"new_sector": "Sector Name", "new_industry": "Industry Name"}`
   - Update changed entries (if Industry or Sector relation changed)
   - Do NOT remove entries (stocks removed from Notion may still need to be in the mapping for historical dashboard comparisons)

4. **If Richard says "full universe sync needed"** — run multiple view queries with different filters to cover all ~1,400 stocks. This is rare; incremental is the default.

**Key reference data:**
- Stocks DB: `collection://25435e90-9b0b-80ec-909d-000ba746fa2d`
- Industries DB: `collection://28e35e90-9b0b-8187-852b-000b0b967f4f` (16 entries)
- Sectors DB: `collection://26635e90-9b0b-8013-a82d-000b4d6ba06d` (~137 entries)
- Industries lookup file: `tmp_industries_lookup.json`

### Step 1. Coverage Audit

Run the coverage audit to check whether the Notion mapping and FactSet Excel are aligned:

```bash
cd /sessions/*/mnt/COWORK && python audit_dashboard_coverage.py
```

**What it checks:**
- Tickers in Notion mapping but missing from FactSet Excel (ACTION: Richard adds to FactSet)
- Tickers in FactSet but not in Notion mapping (INFO: excluded from dashboard)
- Data quality: tickers with missing Industry or Sector assignments

**If gaps found:**
1. Report the missing tickers to Richard, grouped by Industry
2. Richard adds them to the FactSet screen
3. Richard refreshes the FactSet data, saves, and closes the Excel file
4. Watson re-runs the audit to confirm coverage is clean
5. Proceed to Step 2

**If no gaps:** Proceed directly to Step 2.

### Step 2. Run the Pipeline

```bash
cd /sessions/*/mnt/COWORK && python generate_dashboard.py
```

No arguments needed — auto-detects latest `Files/NOT BACKED UP/RB downloads/Universe - YYYY_MM_DD.xlsx`.

If Richard specifies a particular file:
```bash
cd /sessions/*/mnt/COWORK && python generate_dashboard.py "Files/NOT BACKED UP/RB downloads/Universe - YYYY_MM_DD.xlsx"
```

If the original is locked (BadZipFile error), check for a V2/V3 copy:
```bash
ls "Files/NOT BACKED UP/RB downloads/Universe - YYYY_MM_DD"*.xlsx
```

### Step 3. Verify + Present

**Verify output:**
- Check console for: stock count, coverage stats, snapshot saved confirmation
- Confirm both timestamps populated (source data saved + dashboard refreshed)
- Check snapshot line: should show N days in history (accumulates with daily runs)

**Present the file:**
Share `rs-breadth-dashboard.html` so Richard can open it.

**Report to Richard (brief):**
- Which Excel file was used
- Source data timestamp (from TIMESAVED!A1)
- Dashboard refresh timestamp (now)
- Stock count and any data gaps
- Snapshot status (N days of history)
- Coverage audit result (matched count, any gaps)

---

## Quick Refresh (data only, no universe change)

When Richard just wants fresh prices/estimates and the universe hasn't changed:

```bash
cd /sessions/*/mnt/COWORK && python audit_dashboard_coverage.py && python generate_dashboard.py
```

Skip Step 0 entirely. The audit confirms alignment, pipeline runs immediately.

---

## What the Pipeline Does
1. Loads Notion universe (membership + taxonomy) from `stock_mapping_final.json`
2. Reads FactSet Excel (prices, returns, MAs, consensus, ratings, volume)
3. Deduplicates + removes no-price stocks
4. Computes derived fields (excess returns, RS/fund direction, MA flags)
5. Builds aggregations (industry, sector, geo)
6. Computes Minervini scores + updates rolling 14-day snapshot
7. Computes entry/exit diffs for Changes tab
8. Bakes everything into HTML as `var D = {...}`

---

## Files

| File | Purpose |
|------|---------|
| `stock_mapping_final.json` | Notion universe: ticker → {industry, sector}. Source of truth for membership + taxonomy. |
| `audit_dashboard_coverage.py` | Coverage audit: compares Notion mapping vs FactSet Excel. |
| `generate_dashboard.py` | Pipeline: reads mapping + Excel → produces HTML dashboard. |
| `rs-breadth-dashboard.html` | The dashboard output. Self-contained HTML. |
| `tmp_industries_lookup.json` | Industry page URL → name lookup (for Notion sync). |
| `Files/Universe - YYYY_MM_DD.xlsx` | FactSet data export. Richard saves new versions. |
| `snapshots/minervini-history.json` | Rolling 14-day Minervini score history. |
| `coverage_audit_report.json` | Latest audit results (JSON). |

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `BadZipFile` | Excel file open/locked | Ask Richard to close it, or use V2 copy |
| Low stock count | Notion mapping missing tickers | Run Step 0 (Notion sync) then re-audit |
| No change data | First run (no prior snapshot) | Normal — changes appear from 2nd refresh |
| Coverage gaps | New stocks in Notion, not yet in FactSet | Report to Richard, he adds + refreshes |
| Stale taxonomy | Industry/Sector changed in Notion | Run Step 0 to update mapping |
