# MM 8-Point Weekly Refresh — SOP

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 12-Apr-26. Standalone operational SOP for Minervini 8-point tag synchronisation to Notion STOCKS DB. -->
<!-- Cross-role visibility: APM (owns execution), HPC (consumes for regime monitoring), COS (scheduling/logistics), RESEARCHER (consumes for screening). -->

## Purpose

Maintain the **MM 8-Point** multi_select property on every page in the Notion STOCKS database, synchronised weekly with Minervini trend template scores computed from FactSet price data. This gives Richard — and every Watson role — a live technical overlay across the full ~1,000-stock European universe, directly filterable inside Notion.

**Why this matters to each role:**

| Role | How MM 8-Point is used |
|------|----------------------|
| **APM** | Entry decisions (Minervini 4-slug system requires trend template pass), position monitoring, watchlist prioritisation, regime shift detection across universe |
| **HPC** | Market breadth proxy — distribution of scores (how many 8/8 vs 0/8) signals bull/bear regime. Informs "fit for fighting" assessment and risk-off triggers |
| **COS (Executive Assistant)** | Scheduling the refresh, ensuring upstream Excel is exported, flagging staleness, maintaining the manifest |
| **RESEARCHER** | Screening and filtering — "show me all 7+ stocks in healthcare" or "which watchlist stocks just dropped below 4" requires current tags |

---

## Frequency & Scheduling

**Weekly. Run on weekends (Saturday or Sunday) after Richard has exported the latest FactSet Universe file.**

The refresh depends on fresh price data. Weekend execution captures Friday close. There is no value in running on the same data twice — the SOP includes a staleness check.

**Recommended scheduled slot:** Part of the weekend maintenance window. Can be triggered manually ("run the MM refresh") or automated via the scheduled task system. Execution takes ~5-10 minutes for a full universe push.

---

## The Full Chain

```
┌─────────────────────────────────────────────────────────────┐
│  1. RICHARD: Export FactSet → "Universe - YYYY_MM_DD.xlsx"  │
│     Location: COWORK/Files/                                 │
│     Contains: Prices, 200D/150D/50D/20D MAs, 52W hi/lo     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       v
┌─────────────────────────────────────────────────────────────┐
│  2. WATSON (or Richard): Run generate_dashboard.py          │
│     Location: COWORK/generate_dashboard.py                  │
│     Reads: Excel sheets "Universe" + "FS"                   │
│     Computes: 8 binary Minervini criteria per stock         │
│     Writes: COWORK/snapshots/minervini-history.json         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       v
┌─────────────────────────────────────────────────────────────┐
│  3. WATSON: Read JSON → Map to Notion page IDs → Push tags  │
│     Reads: snapshots/minervini-history.json (latest date)   │
│     Lookup: snapshots/master_manifest.json (ticker→page_id) │
│     Pushes: MM 8-Point multi_select on each STOCKS DB page  │
│     Method: 25 parallel Notion API calls per batch          │
│     Duration: ~5 minutes for ~977 stocks                    │
└─────────────────────────────────────────────────────────────┘
```

---

## The 8 Criteria (Minervini Trend Template)

The Minervini trend template evaluates whether a stock is in a confirmed Stage 2 uptrend. Each criterion is binary (pass/fail). Stocks scoring 8/8 are in the strongest technical position; 0/8 are in the weakest.

| # | Criterion | Tag Name | What It Means |
|---|-----------|----------|---------------|
| 1 | Price > 200-day MA | `1: P>200D` | Long-term trend is up |
| 2 | 200-day MA rising | `2: 200D rising` | Long-term trend accelerating |
| 3 | Price > 150-day MA | `3: P>150D` | Medium-term trend is up |
| 4 | 150-day MA > 200-day MA | `4: 150D>200D` | Medium-term trend stronger than long-term |
| 5 | 50-day MA > 150-day MA | `5: 50D>150D` | Short-term trend strongest |
| 6 | Price > 50-day MA | `6: P>50D` | Price above short-term trend |
| 7 | Price >30% above 52-week low | `7: >30% from low` | Meaningful recovery from lows |
| 8 | Price within 25% of 52-week high | `8: <25% from high` | Near highs, not extended collapse |

**Interpretation shortcuts for all roles:**
- **8/8** = Full Stage 2 uptrend. Strongest technical setup.
- **6-7/8** = Near-Stage 2. Usually missing one MA alignment or the 30%/25% distance checks.
- **4-5/8** = Transitional. Some MAs aligning but not confirmed.
- **1-3/8** = Weak. Likely Stage 3 (top) or Stage 4 (decline).
- **0/8** = No trend template criteria met. Deep Stage 4 or bottoming.

**For HPC/APM:** A portfolio where most positions are 6+ is technically healthy. If core positions start dropping below 4, that's a regime deterioration signal worth surfacing.

---

## Technical Specification

### Data Format: minervini-history.json

```json
{
  "2026-04-12": {
    "TICKER-CC": {
      "s": 5,           // score (0-8)
      "c": [true, false, true, false],  // category booleans: [LT, S2, ST, LD]
      "p": [1, 1, 1, 0, 1, 0, 1, 0]    // individual criteria pass/fail
    }
  }
}
```

The `p[]` array maps directly to tags: `p[0]` → criterion 1, `p[7]` → criterion 8. A value of 1 means pass (include that tag); 0 means fail (exclude).

### Tag Mapping (p[] → Notion multi_select)

```python
TAG_MAP = {
    0: "1: P>200D",
    1: "2: 200D rising",
    2: "3: P>150D",
    3: "4: 150D>200D",
    4: "5: 50D>150D",
    5: "6: P>50D",
    6: "7: >30% from low",
    7: "8: <25% from high"
}

def build_tags_json(p_array):
    tags = [TAG_MAP[i] for i, v in enumerate(p_array) if v == 1]
    return json.dumps(tags)  # e.g. '["1: P>200D", "3: P>150D"]' or '[]'
```

### Notion API Call Format

```
notion-update-page:
  page_id: <from master_manifest.json>
  command: "update_properties"
  properties: {"MM 8-Point": "<tags_json_string>"}
  content_updates: []
```

**Critical format rules:**
- `tags_json` MUST be a JSON array string: `"[\"1: P>200D\", \"6: P>50D\"]"`
- Empty tags MUST be `"[]"` — NOT `""` (empty string fails)
- Comma-separated, semicolon-separated, newline-separated formats all FAIL

### Key File Locations

| File | Persistent Location | Purpose |
|------|-------------------|---------|
| `generate_dashboard.py` | `COWORK/generate_dashboard.py` | Excel → JSON conversion. Computes all 8 criteria. |
| `minervini-history.json` | `COWORK/snapshots/minervini-history.json` | Rolling 14-day score history. Source of truth for tags. |
| `master_manifest.json` | `COWORK/snapshots/master_manifest.json` | Ticker → Notion page_id lookup. 1,264 entries. **Must be loaded/rebuilt each session.** |
| `build_push_list.py` | `COWORK/scripts/build_push_list.py` | Reference script for building push lists from manifest + JSON. |
| Universe Excel files | `COWORK/Files/Universe - YYYY_MM_DD.xlsx` | FactSet exports. Upstream raw data. |

### Notion Database Details

| Item | ID |
|------|----|
| STOCKS Database | `25435e909b0b80e4a7fcd6352fbf3187` |
| STOCKS Data Source | `collection://25435e90-9b0b-80ec-909d-000ba746fa2d` |
| Stock Notes (child DB — DO NOT push here) | `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2` |

---

## Execution Steps (Watson)

### Pre-flight

1. **Check upstream freshness.** Read `minervini-history.json`, get the latest date key. If older than 7 days from today → STOP, flag to Richard: "MM 8-Point refresh blocked — minervini-history.json latest date is [X], need fresh FactSet export."

2. **Load the manifest.** Read `COWORK/snapshots/master_manifest.json`. If not found, rebuild from Notion (query STOCKS DB, extract all tickers and page IDs). Structure: `{ticker: {page_id, stock_name, score, tags}}`.

3. **Sanity check score distribution.** Count stocks by score (0-8). If >80% score 0, something is wrong upstream (data issue, not a real market crash). Flag before pushing.

### Build & Push

4. **Build push list.** For each ticker in the latest snapshot date:
   - Look up `page_id` in manifest
   - If no page_id → skip, log as coverage gap
   - Convert `p[]` to tags_json string
   - Add to push list

5. **Push in parallel batches of 25.** Fire 25 `notion-update-page` calls simultaneously. Log each success/failure. Continue through full universe regardless of individual failures.

6. **Handle errors:**
   - "Property MM 8-Point not found" → page_id points to wrong page. Log ticker. Add to investigation queue. **Do not retry.**
   - Rate limit / timeout → retry once after 5 seconds, then skip and log.
   - Other errors → log and skip.

### Post-push

7. **Spot check.** Fetch 5 random stocks from Notion (mix of 0-tag, partial, 8/8) and verify tags match the JSON. If any mismatch → flag immediately.

8. **Report.** Log: total attempted, successful, failed, skipped (no page_id), score distribution. Post to session handoff.

---

## Known Issues & Error Patterns

### Manifest Page ID Mismatches

**Pattern:** "Property MM 8-Point not found" error on a stock that definitely exists in the STOCKS DB.

**Root cause:** The manifest builder sometimes picks up a Stock Notes sub-page (child database `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2`) instead of the main STOCKS page. Both databases contain pages with the stock's ticker in the title, but only the STOCKS database has the MM 8-Point property.

**Fix:** Fetch the failing page_id. Check its `ancestor-path`. If parent is "Stock notes" not "Stocks", search Notion for the ticker to find the correct STOCKS DB page. Update the manifest.

**Resolved cases (12-Apr-26):**

| Ticker | Wrong page_id (Stock Notes) | Correct page_id (STOCKS) |
|--------|---------------------------|-------------------------|
| BYLOT-GR | `26835e909b0b8022aa4fe1cf6659fc29` | `26835e909b0b8044b7f8fa1431655195` |
| HFG-GB | `25d35e909b0b8002a1f3fa707c611962` | `25e35e909b0b80f09731c9a15a581e25` |
| HTWS-GB | `29835e909b0b80d993d8d2a8afe5662a` | `29835e909b0b80e8b237d5c01229661d` |

### Coverage Gaps

**529 tickers** in the Minervini universe have empty page IDs in the manifest (as of 12-Apr-26). By country: GB(88), CH(56), DE(53), NO(42), ES(37), FR(33), NL(32), SE(29), DK(25), FI(21), BE(20), AT(18), PL(15), plus smaller counts. Many are large-caps that almost certainly exist in the STOCKS DB (ASML, SAP, Novo Nordisk, Shell, HSBA, Adyen, etc.) — the manifest builder simply didn't find them. Full list: `COWORK/snapshots/coverage-gaps-2026-04-12.md`. Backfilling requires querying the STOCKS DB for each ticker and updating the manifest. This is a priority maintenance task — reduces coverage from ~45% to potentially 90%+ of the Minervini universe.

---

## Monitoring & Quality Checks

| Check | Frequency | Action if failed |
|-------|-----------|-----------------|
| Upstream freshness (JSON date < 7 days old) | Every run | Block push, flag to Richard |
| Score distribution sanity (>80% score 0) | Every run | Block push, flag data issue |
| Post-push spot check (5 random stocks) | Every run | Investigate mismatches immediately |
| Manifest age (>30 days since rebuild) | Monthly | Rebuild from Notion to catch new stocks |
| Coverage gap audit | Quarterly | Query STOCKS DB for unmatched tickers, backfill manifest |
| Full audit (sample 15+ across score ranges) | Quarterly | Cross-reference Notion tags vs JSON |

---

## Cross-Role Usage Guide

### For APM (Primary Owner)

You execute the weekly refresh and consume the tags for:
- **Entry screening:** Filter STOCKS DB by MM 8-Point contains "1: P>200D" AND "2: 200D rising" etc. to find Stage 2 candidates.
- **Position monitoring:** Track whether held positions maintain their MM score week-over-week. A drop from 7→4 in a core position is an early warning.
- **Universe regime:** The aggregate score distribution tells you whether the European market is broadening (more 7-8s) or narrowing (fewer). This feeds the "fit for fighting" assessment.

### For HPC (High Performance Coach)

The MM 8-Point data feeds two HPC concerns:
- **Market regime & psychology.** When the universe median score drops from 6 to 3, Richard may be fighting the tape. HPC should surface this: "The universe median MM score has dropped from X to Y over the past 3 weeks — are you adjusting risk accordingly?"
- **Position psychology.** If a held position drops from 8/8 to 2/8, that's objective technical deterioration. HPC can use this to pre-empt Minervini emotional cycle stages (Denial → Frustration → Hope): "TICKER has lost 6 of 8 trend template criteria. Your own rules say this is a mechanical exit signal. Are we in denial?"

### For COS (Chief of Staff / Executive Assistant)

Your responsibilities:
- **Scheduling.** Ensure the weekly refresh is in the calendar/task system. Remind Richard to export FactSet on Friday/Saturday if not done.
- **Staleness monitoring.** If Watson reports "JSON stale" during a session, that means the refresh didn't run. Escalate.
- **Manifest maintenance.** If Richard adds stocks to the Notion STOCKS DB, the manifest needs updating. Flag for the next refresh session.

### For RESEARCHER

The MM 8-Point tags let you filter the STOCKS DB during screening work:
- "Show me all healthcare stocks with MM score 7+" → Filter by Sector = Healthcare AND MM 8-Point contains criteria 1-7.
- "Which of my watchlist stocks are technically strongest?" → Sort/filter by tag count.
- Note: The tags are a snapshot (updated weekly). For intra-week precision, check the JSON directly.

---

## History & Context

| Date | Event |
|------|-------|
| 05-Apr-26 | First Minervini scoring run. generate_dashboard.py created. |
| 06-Apr-26 | minervini-history.json established with rolling 14-day history. |
| 08-Apr-26 | MM 8-Point property added to Notion STOCKS DB. |
| 09-12 Apr-26 | Batch tagging across multiple sessions. 161 → 448 → 917 stocks tagged. |
| 12-Apr-26 | Full batch 4 complete (469 stocks). 3 page ID errors identified and fixed. Audit passed (10/10 spot checks). SOP formalised. master_manifest.json persisted to COWORK. |

**Total tagged as of 12-Apr-26:** 917 stocks (of ~977 in Minervini universe, ~1,264 in full manifest).

---

## Appendix: Quick-Reference Cheat Sheet

**To trigger a refresh:**
> "Run the MM 8-Point weekly refresh"

**Watson should:**
1. Read `COWORK/snapshots/minervini-history.json` — check latest date
2. Read `COWORK/snapshots/master_manifest.json` — load ticker→page_id map
3. Build push list from latest date's scores
4. Push 25 at a time to Notion
5. Spot-check 5 stocks
6. Report results

**If JSON is stale:**
> Richard needs to export FactSet Universe file and run `generate_dashboard.py`

**If a page_id fails:**
> Fetch the page, check ancestor-path. If it's a Stock Notes page, search Notion for the correct STOCKS page. Update manifest.

**If manifest is missing:**
> Rebuild by querying Notion STOCKS DB (view by view, ~100 per query) to extract all ticker→page_id pairs. Save to `COWORK/snapshots/master_manifest.json`.
