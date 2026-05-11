# Bulk Notion Operations — Skill

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.


## Purpose
SOP for updating large numbers of Notion pages in a consistent pattern (e.g., reassigning properties across hundreds of stock pages). Applicable to any role that needs to make systematic changes across the Stocks DB, Sectors DB, or any other large Notion database.

**Accessible to:** RESEARCHER, CHIEF OF STAFF, APM, SYSTEMS ARCHITECT

---

## When to Use
- Reassigning stocks to new sectors/industries/geographies
- Bulk-updating any relation, select, or text property across many pages
- Any operation touching >20 Notion pages with a repeatable pattern

---

## Architecture: Pre-compute → Batch → Parallel Agents

### Phase 1: Pre-compute the update payload
Build a JSON mapping file BEFORE any Notion calls. Structure:
```json
{
  "TICKER_OR_KEY": {
    "property_1_url": "https://www.notion.so/PAGE_ID",
    "property_2_url": "https://www.notion.so/PAGE_ID"
  }
}
```
- Save to COWORK (persistent) so work survives session breaks
- Include a separate URL mapping file if properties are relations (name → Notion page URL)
- Validate: check all keys have valid URLs, count totals, flag missing mappings

### Phase 2: Split into batches
- Split the mapping into 6 batch files (~200-250 items each)
- Save batch files to COWORK
- Create a progress tracker markdown file in `memory/projects/`

### Phase 3: Launch parallel agents
Launch 6 agents simultaneously, one per batch. Each agent:

1. Reads its batch file
2. For each item:
   a. **Search** the target DB: `notion-search` with `data_source_url`, `page_size: 3`, `max_highlight_length: 0`
   b. **Extract page ID** from search result URL (last 32 chars, no dashes)
   c. **Update** via `notion-update-page`: `command: "update_properties"`, properties as JSON array strings
3. Reports completion count

### Phase 4: Track and resume
- After each round, tally completions per batch
- Update the progress tracker
- Launch new rounds for remaining items
- Repeat until done

---

## Critical Efficiency Rules (Hard-Won)

1. **Agents must EXECUTE, not PLAN.** Agents that spend context on "preparing manifests" or "creating execution plans" complete 5-10x fewer updates. The agent prompt must be extremely directive: "search, update, move on."

2. **Minimise search response size.** Always use `page_size: 3` and `max_highlight_length: 0` on all Notion searches. Large responses waste agent context.

3. **Do NOT fetch before updating.** The search result URL is sufficient to extract the page ID. Fetching the full page before updating doubles the API calls for zero benefit.

4. **Skip failures immediately.** If a search returns no results, move to the next item. Don't retry, don't debug. Log it and continue.

5. **Relation properties are JSON array strings.** Format: `'["https://www.notion.so/PAGE_ID"]'` — note the outer single quotes and inner double quotes with square brackets.

6. **Save everything to COWORK.** Batch files, mapping files, progress tracker — all must be in the COWORK mount so they survive session breaks.

7. **One batch per agent.** Don't split work within an agent. Each agent owns one batch file completely.

---

## Agent Prompt Template

```
You are updating [ENTITY] pages in a Notion database. Your job is to update each page's [PROPERTY] relation properties.

1. Read the file `[BATCH_FILE_PATH]` — JSON mapping of keys to target URLs
2. For EACH key:
   a. Search Notion (data_source_url: "[COLLECTION_URL]") for the key. Use page_size: 3, max_highlight_length: 0.
   b. Find the matching page from search results
   c. Update via notion-update-page: command "update_properties", properties: {"[PROP]": "[\"URL\"]"}, content_updates: []
3. Skip items with no search results. Do NOT plan or prepare — just search and update.
4. Report total completed at the end.

[LIST ANY ALREADY-COMPLETED ITEMS TO SKIP]
```

---

## Progress Tracker Template

Save to `memory/projects/[operation-name]-progress.md`:
```markdown
# [Operation Name] — Progress Tracker
**Created:** [date]
**Last updated:** [date]

## Status: [IN PROGRESS / COMPLETE]

### Batch Progress
| Batch | Total | Done | Remaining |
|-------|-------|------|-----------|
| 0 | 234 | 89 | 145 |
| ... | ... | ... | ... |

### Key Files
| File | Purpose |
|------|---------|
| [mapping].json | Item → target property mapping |
| [urls].json | Property names → Notion page URLs |
| update_batch_X.json | Pre-computed batch payloads |

### Resumption Instructions
[Step-by-step for next session to pick up where this left off]
```

---

## Known Limitations
- **Notion search is semantic, not exact.** Ticker searches may return partial matches. Agents should verify the Ticker field matches exactly before updating.
- **Agent throughput varies.** Expect 40-120 updates per agent per round depending on search hit rate and response sizes.
- **No true pagination on DB views.** The `notion-query-database-view` tool returns ~100 results with no offset parameter. For full DB exports, use repeated searches instead.
- **Duplicate pages exist.** The Stocks DB has legacy pages without tickers. Agents should only update pages that have the target identifier field set.

---

## Example: Sector Taxonomy Reassignment (30-Mar-26)
- **Operation:** Reassign 1,400 stocks to new 84-sector / 16-industry taxonomy
- **Files:** stock_mapping_final.json, notion_mapping.json, update_batch_0-5.json
- **Progress:** memory/projects/sector-taxonomy-update-progress.md
- **Result:** ~550 done in 2 rounds of 6 agents (~4 hours), ~850 scheduled overnight
- **Key learning:** Agents prompted with "just search and update" outperformed those given detailed instructions by 5-10x
