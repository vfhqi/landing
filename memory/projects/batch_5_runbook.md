# Batch 5 Execution Runbook
**Prepared:** 31 Mar 2026 08:00 UK
**Status:** READY FOR EXECUTION
**Tickers:** 191

---

## Quick Start

1. **Load the batch:** `taxonomy_agent_batch_5.json` (191 tickers with pre-computed URLs)
2. **For each ticker:**
   - Search Notion Stocks DB for the ticker (semantic search)
   - If found: Fetch page → verify Ticker property → update Sector + Industry
   - If not found: Log as skipped, move to next
3. **Report:** updated count, skipped count, failed count

**Expected time:** 20-30 minutes serial, 10-15 minutes with 6 parallel agents

---

## Step-by-Step Execution

### 1. Load Batch Data
```python
import json
with open('/sessions/gifted-modest-carson/mnt/COWORK/taxonomy_agent_batch_5.json', 'r') as f:
    batch_5 = json.load(f)

# batch_5 now contains 191 tickers
# Each entry: {
#   "TEQ-SE": {
#     "sector_url": "https://www.notion.so/33335e909b0b8110a19ac2f419d70b55",
#     "industry_url": "https://www.notion.so/28e35e909b0b812597e0f9a212f8cc2d"
#   },
#   ...
# }
```

### 2. For Each Ticker, Execute Search

Use the `notion-search` tool:
- Query: `[TICKER]`
- Data source: `collection://25435e90-9b0b-80ec-909d-000ba746fa2d` (Stocks DB)
- Page size: 3
- Max highlight length: 0

Example:
```
notion-search (TEQ-SE, page_size=3, max_highlight_length=0)
→ Returns 1-3 pages with company names matching "TEQ" or "SE" or similar
```

### 3. Verify Match

Search results will return pages by company name, not ticker. You MUST verify:

```python
# Pseudocode
search_result = notion_search("TEQ-SE")  # Returns company pages
for page in search_result:
    page_content = notion_fetch(page['id'])
    ticker_field = page_content['properties']['Ticker']

    if ticker_field == "TEQ-SE":
        # MATCH FOUND - proceed to update
        page_id = page['id']
        break
else:
    # NO MATCH - log as skipped
    log_skipped("TEQ-SE")
    continue
```

### 4. Update Page

Use `notion-update-page` with:

```json
{
  "command": "update_properties",
  "page_id": "[PAGE_ID_FROM_SEARCH]",
  "properties": {
    "Sector": "[\"https://www.notion.so/33335e909b0b8110a19ac2f419d70b55\"]",
    "Industry": "[\"https://www.notion.so/28e35e909b0b812597e0f9a212f8cc2d\"]"
  },
  "content_updates": []
}
```

**CRITICAL:** Properties are JSON array strings. Format must be: `["URL1", "URL2"]` inside double quotes.

### 5. Log Result

After each update:
```python
if update_succeeded:
    updated_tickers.append("TEQ-SE")
elif search_returned_no_results:
    skipped_tickers.append("TEQ-SE")
elif update_failed:
    failed_tickers.append("TEQ-SE")
```

### 6. Report Final Count

After all 191 tickers processed:
```
Total: 191
Updated: [X]
Skipped: [Y]  (search returned no match)
Failed: [Z]   (update operation failed)
```

---

## Example: Processing "TEQ-SE"

```
INPUT:
  Ticker: TEQ-SE
  Sector URL: https://www.notion.so/33335e909b0b8110a19ac2f419d70b55
  Industry URL: https://www.notion.so/28e35e909b0b812597e0f9a212f8cc2d

STEP 1: Search
  notion-search(query="TEQ-SE", data_source="collection://25435e90-9b0b-80ec-909d-000ba746fa2d", page_size=3)
  → Returns page with title "Techem" (likely match)

STEP 2: Verify (Fetch)
  notion-fetch(page_id="33335e909b0b...")
  → Check properties["Ticker"] == "TEQ-SE" ✓ MATCH

STEP 3: Update
  notion-update-page(
    command="update_properties",
    page_id="33335e909b0b...",
    properties={
      "Sector": "[\"https://www.notion.so/33335e909b0b8110a19ac2f419d70b55\"]",
      "Industry": "[\"https://www.notion.so/28e35e909b0b812597e0f9a212f8cc2d\"]"
    }
  )
  → Success ✓

STEP 4: Log
  updated_tickers.append("TEQ-SE")

OUTPUT:
  Result: UPDATED
  Sector: Industrial products – Diversified manufacturing
  Industry: Industrials
```

---

## Parallel Execution (6 Agents)

If using 6 parallel agents, split batch:

| Agent | Tickers | Command |
|-------|---------|---------|
| Agent 0 | TEQ-SE to CMBNOR-DE (first 32) | Process sub-batch 0 |
| Agent 1 | CMBAM-SE to DKDNORM-DK (next 32) | Process sub-batch 1 |
| Agent 2 | DKD-NL to ECOR-ES (next 32) | Process sub-batch 2 |
| Agent 3 | ECOR-FI to ESIT.MI (next 32) | Process sub-batch 3 |
| Agent 4 | ESM-ES to GMGH-SE (next 32) | Process sub-batch 4 |
| Agent 5 | GMGH-SQ to ZZZZZ (last 31) | Process sub-batch 5 |

Each agent:
1. Loads its sub-batch tickers
2. For each: search → fetch → verify → update → log
3. Reports final count when done
4. Saves results to `batch_5_agent_[N]_results.json`

---

## Handling Failures

### Search Returns No Results
- Log as "skipped"
- Move to next ticker
- (Optional: Retry with shorter query, e.g., "TEQ" instead of "TEQ-SE")

### Search Returns Multiple Results, No Exact Match
- Log as "skipped"
- Document which pages were reviewed (for manual follow-up)
- Move to next ticker

### Update Fails
- Log as "failed"
- Record error message
- DO NOT retry immediately (may be permission/structure issue)
- Move to next ticker

### Timeout on Search
- Log as "timeout"
- Skip ticker
- Don't retry (may be API overload)

---

## Files & References

| File | Purpose |
|------|---------|
| taxonomy_agent_batch_5.json | The batch data (191 tickers + URLs) |
| notion_mapping.json | Sector/industry name → URL lookup (reference) |
| stock_mapping_final.json | Full 1,400-ticker mapping (reference) |
| batch_5_execution_report.md | Detailed batch analysis |
| BATCH_5_EXECUTION_SUMMARY.md | Executive summary & context |
| sector-taxonomy-update-progress.md | Master progress tracker (update after execution) |

---

## Expected Success Rate

Based on previous batches (0-3):
- **Batch 0:** 44 of 234 (18%) — low hit rate, possible search inefficiency
- **Batch 1:** 118+ of 234 (50%+) — better, possible API improvements
- **Batch 2:** 7 of 234 (3%) — very low, likely different search strategy needed
- **Batch 3:** 38 of 234 (16%) — low, consistent with batches 0, 2

**Batch 5 expectations:** 30-50% success rate (55-100 tickers updated) with standard semantic search

**Optimization note:** If using fetch verification, success rate may be higher (70-80%) due to more robust matching.

---

## Resumption Instructions

If execution pauses midway:

1. Check results file: `batch_5_agent_[N]_results.json` or similar
2. Identify last ticker processed
3. In batch file, remove tickers already done
4. Save as `batch_5_remaining.json`
5. Resume from next ticker
6. Merge results: `updated_so_far + new_batch_results = final_total`

---

## Final Integration

After all tickers processed:

1. Save results to `batch_5_final_results.json`:
   ```json
   {
     "batch_number": 5,
     "total_tickers": 191,
     "updated": [list],
     "skipped": [list],
     "failed": [list],
     "updated_count": X,
     "skipped_count": Y,
     "failed_count": Z
   }
   ```

2. Update progress tracker:
   ```
   memory/projects/sector-taxonomy-update-progress.md
   → Add row: | 5 | 191 | X | Y | Z |
   ```

3. Archive this runbook:
   ```
   memory/projects/batch_5_execution_summary.md (rename from COWORK root)
   ```

---

## Support & Escalation

If >20% of tickers fail or timeout:
- Check Notion API status
- Try different search strategy (e.g., company name instead of ticker)
- Consider batch 4+5 combined second pass with modified search approach

---

*Runbook for Watson Taxonomy Update Batch 5 Execution*
*Created: 31 Mar 2026, 08:00 UK*
