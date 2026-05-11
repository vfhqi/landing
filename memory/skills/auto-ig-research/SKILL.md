# Auto IG Research SOP — 8/8 Minervini Trigger

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 13-Apr-26. SA/DEVELOPMENT. Automated IG research for stocks meeting 8/8 Minervini criteria. -->
<!-- Updated 24-Apr-26: Primary data source changed from snapshots/minervini-history.json to Master Dashboard filter-results.json MM99 filter. -->

> **DATA SOURCE UPDATE (24-Apr-26):** This SOP's upstream data source is now `master-dashboard/data/filter-results.json` → MM99 filter → `score` field. The legacy `snapshots/minervini-history.json` is deprecated. References below to `minervini-history.json` should be read as `filter-results.json` until the scanner script (`auto_ig_scanner.py`) is updated to read the new format. The scanner script itself needs updating to parse the Master Dashboard JSON schema.

## Purpose

Automatically detect stocks that newly qualify as 8/8 on the Minervini trend template and run the full IG RESEARCHER workflow (BD + CF, dual-source) without Richard's approval. This ensures no technically qualified stock falls through the cracks between dashboard refreshes.

**This SOP does NOT promote stocks through the pipeline.** It produces IG research outputs only. Richard decides whether to progress, triage, or park.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│  UPSTREAM: Dashboard Refresh (Saturday + mid-week if export)     │
│  generate_dashboard.py → minervini-history.json                  │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌──────────────────────────────────────────────────────────────────┐
│  SCANNER: auto_ig_scanner.py                                     │
│  Reads: minervini-history.json (latest 2 dates)                  │
│  Reads: auto-ig-tracking.json (persistent state)                 │
│  Reads: master_manifest.json (ticker → Notion page_id)           │
│  Queries: Notion Stock Notes DB (backlog check)                  │
│                                                                  │
│  Outputs:                                                        │
│  1. Delta list: stocks that moved from <8 → 8/8                  │
│  2. Backlog list: 8/8 stocks without IG research in Notion       │
│  3. Combined + deduplicated + capped at 5 (recency-prioritised)  │
│  4. Updates auto-ig-tracking.json with "queued" status           │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌──────────────────────────────────────────────────────────────────┐
│  EXECUTION: RESEARCHER IG Workflow (per stock, up to 5/night)    │
│                                                                  │
│  Phase 1 — Claude [C] (parallel, immediate):                     │
│    • BD [C] — native sub-agent, web search, ~7,000 words         │
│    • CF [C] — native sub-agent, web search, ~7,000 words         │
│    • Post both to Notion with 30%+ highlighting                  │
│                                                                  │
│  Phase 2 — AlphaSense [AS] (Chrome, 10-concurrent limit):        │
│    • Attempt BD [AS] + CF [AS] via Chrome Deep Research           │
│    • If Chrome unavailable → queue for next live session          │
│    • If Chrome available → submit all (5 stocks × 2 = 10 reports │
│      fits in a single wave), wait 45–60min, extract via PDF      │
│      download (see as-claude-research-sop-v2.md), post           │
│    • Concurrent limit is 10 (confirmed 15-Apr-26) — nightly      │
│      5-stock cap = 10 AS reports = single wave, no batching      │
│                                                                  │
│  Phase 3 — Update tracking:                                      │
│    • Mark stock as "completed" in auto-ig-tracking.json           │
│    • Log pages posted (page IDs, titles)                         │
│    • Log any failures (AS Chrome unavailable, extraction errors)  │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌──────────────────────────────────────────────────────────────────┐
│  REPORTING: Handoff + Morning Summary                            │
│  • auto-ig-overnight-report.md written to memory/reports/        │
│  • watson-morning-questions reads report → tells Richard          │
│  • session-handoff-auto includes auto-IG results                 │
└──────────────────────────────────────────────────────────────────┘
```

---

## Trigger Logic (Two Sources, Combined)

### Source 1: Delta Detection

Compare the two most recent dates in minervini-history.json. Any stock where:
- Current score = 8
- Previous score < 8

These are "newly qualified" — highest priority.

### Source 2: Backlog Sweep

From all current 8/8 stocks, identify any that do NOT have IG research already posted to Notion. Check by searching Stock Notes DB for pages matching `[W] {TICKER} - Business Description [C]`. If no BD [C] page exists, the stock is backlog.

### Combining & Prioritising

1. **Merge** delta + backlog lists, deduplicate
2. **Filter out** stocks already in auto-ig-tracking.json with status "completed" or "queued"
3. **Filter out** stocks without a page_id in master_manifest.json (can't link to Notion)
4. **Prioritise by recency:** Delta stocks first (they just crossed 8/8), then backlog stocks sorted by how recently they achieved 8/8 (check historical scores)
5. **Cap at 5 per night**
6. **Queue remainder** for next night (they'll be picked up by the backlog sweep)

### Recency Rule

Per calibration (13-Apr-26): prioritise recent 8/8 passes (weeks). Stocks that have been 8/8 for 12+ months are lower priority — trend exhaustion/reversal risk. The scanner uses minervini-history.json lookback to estimate qualification duration.

---

## Data Freshness: Saturday + Mid-Week

### Saturday (Primary Refresh)

The existing `mm-8-point-weekly-refresh` task (Saturday 09:00 UK) runs generate_dashboard.py after Richard's FactSet export. The auto-IG scanner runs that night (Saturday 23:30 UK) against the fresh JSON.

### Mid-Week Check (Wednesday)

A second scheduled task (Wednesday 22:00 UK) checks for fresh FactSet exports:

1. List files in `COWORK/Files/NOT BACKED UP/RB downloads/` matching `Universe - YYYY_MM_DD*.xlsx`
2. Find the most recent file by filename date
3. Compare against the latest date in minervini-history.json
4. **If the Excel date is newer** than the JSON date → run `generate_dashboard.py` with the new file → then run the scanner
5. **If no newer file** → skip, log "no fresh export found"

This catches mid-week exports Richard occasionally does without requiring a manual trigger.

---

## Nightly Cap: 5 Stocks

If the scanner identifies >5 candidates:
- Process the top 5 (recency-prioritised)
- Remaining stocks stay in the backlog — they'll be picked up the next night
- At 5 stocks × 4 pages = 20 Notion pages per night
- [C] research: 10 parallel agents, ~15 minutes total
- [AS] research: 10 submissions in ~4 waves of 3, ~3 hours total

If the backlog is large (e.g., 267 current 8/8s on first run), the nightly cap means it clears over time. Delta stocks always jump the queue.

---

## Execution Detail

### Pre-Flight (Every Run)

1. Read `COWORK/master-dashboard/data/filter-results.json` — check `_meta.generated` date, verify <48h old. Use MM99 filter `score` field per stock (replaces deprecated `snapshots/minervini-history.json`)
2. Read `COWORK/snapshots/master_manifest.json` — load ticker→page_id map
3. Read `COWORK/snapshots/auto-ig-tracking.json` — load processing state
4. Run `auto_ig_scanner.py` — get tonight's candidate list (max 5)
5. If candidate list is empty → log "no new candidates", exit
6. If JSON is stale (>7 days old) → log "JSON stale, skipping", exit

### Phase 1: Claude [C] Research (Parallel, Immediate)

For each candidate stock (up to 5):

1. **Read existing Stock Notes** — search Notion for the ticker, read any existing pages (RESEARCHER prerequisite)
2. **Adapt prompts** — fill in ticker/company from manifest, apply [C] adaptation (remove sell-side/expert references)
3. **Launch BD [C] + CF [C] as parallel native sub-agents** — each uses WebSearch extensively, writes ~7,000 words
4. **Validate output** — word count gates (BD ≥ 3,000w, CF ≥ 4,000w), correct ticker, all sections present
5. **Process through pipeline** — `python3 scripts/process_report.py {TICKER} {BD|CF} {filepath}` → highlight (30%+) → chunk
6. **Post to Notion** — Stock Notes DB, full properties, full length, chunked if >15K chars
7. **Verify posting** — spot-check 1-2 pages per run

All 5 stocks × 2 prompts = 10 sub-agents launch simultaneously. Results arrive in ~5-15 minutes.

### Phase 2: AlphaSense [AS] Research (Chrome, Best-Effort)

1. **Check Chrome availability** — attempt to navigate to `research.alpha-sense.com/gensearch`
2. **If Chrome unavailable:**
   - Log "[AS] Chrome not available — [C] pages posted, [AS] queued for next live session"
   - Update tracking: mark AS status as "queued_for_live"
   - Exit Phase 2
3. **If Chrome available:**
   - Plan waves: 5 stocks × 2 prompts = 10 submissions → 4 waves of 3 (3, 3, 3, 1)
   - **Wave 1:** Submit 3 prompts to Deep Research (BD/CF for first 2 stocks, BD for 3rd)
     - Verify Deep Research mode (JS check + screenshot)
     - Log URLs to `memory/research-queue.md`
   - **Wait 45 minutes** — use this time to verify [C] postings
   - **Extract Wave 1** — DOM extraction or clipboard intercept per AS Research SOP
   - **Submit Wave 2** (3 more prompts)
   - Repeat until all 10 submitted + extracted
   - **Process and post** each [AS] output through the standard pipeline
4. **Update tracking** — mark AS status as "completed" with page IDs

### Phase 3: Reporting

After all execution completes:

1. **Update auto-ig-tracking.json** — mark each stock with status, page IDs, timestamps
2. **Write overnight report** to `memory/reports/auto-ig-overnight-YYYY-MM-DD.md`:

```markdown
# Auto IG Overnight Report — DD Mon YYYY

## Scanner Results
- JSON date: YYYY-MM-DD
- Delta stocks (new 8/8): X
- Backlog stocks (missing IG): Y
- Candidates after dedup + cap: Z (of N total)

## Execution Summary
| Ticker | BD [C] | CF [C] | BD [AS] | CF [AS] | Status |
|--------|--------|--------|---------|---------|--------|
| ABC-GB | Posted (page_id) | Posted (page_id) | Posted (page_id) | Queued | Partial |

## Pages Posted
- Total new Notion pages: X
- All highlighted 30%+: Yes/No
- Verification spot-check: Pass/Fail

## Failures / Queued
- [AS] Chrome unavailable: list tickers
- Extraction errors: list tickers
- Queued for next night (over cap): list tickers

## Next Run
- Remaining backlog: X stocks
- Estimated nights to clear: Y
```

3. **This report is consumed by:**
   - `watson-morning-questions` (07:00 UK) — incorporates overnight results into morning briefing
   - `session-handoff-auto` (15:00 UK) — includes in handoff summary
   - Richard's manual session — Watson reports what was done overnight

---

## Tracking State: auto-ig-tracking.json

Persistent file at `COWORK/snapshots/auto-ig-tracking.json`. Structure:

```json
{
  "last_scan_date": "2026-04-13",
  "last_json_date": "2026-04-12",
  "processed": {
    "AHT-GB": {
      "first_detected": "2026-04-13",
      "qualification_date": "2026-04-12",
      "source": "delta",
      "prev_score": 7,
      "c_status": "completed",
      "c_pages": {
        "bd": "page_id_here",
        "cf": "page_id_here"
      },
      "as_status": "completed",
      "as_pages": {
        "bd": "page_id_here",
        "cf": "page_id_here"
      },
      "completed_date": "2026-04-13"
    },
    "BAS-DE": {
      "first_detected": "2026-04-13",
      "qualification_date": "2026-04-12",
      "source": "backlog",
      "prev_score": 7,
      "c_status": "completed",
      "c_pages": {},
      "as_status": "queued_for_live",
      "as_pages": {},
      "completed_date": null
    }
  },
  "queue": ["TICKER-CC", "..."],
  "stats": {
    "total_scanned": 267,
    "total_processed": 5,
    "total_queued": 18,
    "total_completed": 3
  }
}
```

**Status values:**
- `c_status` / `as_status`: "pending" | "in_progress" | "completed" | "failed" | "queued_for_live"
- A stock is fully "completed" only when BOTH c_status AND as_status are "completed"
- "queued_for_live" means [AS] research is waiting for a live session with Chrome

**Deduplication rule:** Once a stock appears in `processed` with c_status = "completed", it is never re-scanned — even if it drops below 8/8 and returns. The IG research is done. Richard decides the next step.

---

## Scheduled Tasks

### 1. auto-ig-overnight (Daily, 23:30 UK)

**Schedule:** Every day at 23:30 UK (22:30 UTC winter, 22:30 BST → 21:30 UTC summer)
**Cron:** `30 23 * * *` (UK local)

**Prompt summary:**
1. Read this SKILL.md + RESEARCHER SKILL.md + AS/Claude Research SOP + Notion Posting SOP
2. Read minervini-history.json, master_manifest.json, auto-ig-tracking.json
3. Run scanner: detect delta + backlog, prioritise, cap at 5
4. Execute IG workflow for each candidate (Phase 1 + Phase 2)
5. Write overnight report
6. Update tracking state

### 2. auto-ig-midweek-refresh (Wednesday, 22:00 UK)

**Schedule:** Wednesday at 22:00 UK
**Cron:** `0 22 * * 3`

**Prompt summary:**
1. Check `COWORK/Files/` for FactSet exports newer than latest minervini-history.json date
2. If found → run `python3 generate_dashboard.py "{newest_file}"` → regenerate JSON
3. Then trigger the same scanner + execution as the overnight task
4. If no newer file → log "no mid-week export", exit

---

## Integration Points

### Morning Summary (watson-morning-questions, 07:00 UK)

The morning task reads `memory/reports/auto-ig-overnight-*.md` (latest file). If a report exists from last night:
- Tell Richard how many stocks were processed
- List the tickers and what was posted
- Flag any [AS] submissions queued for live session
- Flag any failures

### Session Handoff (session-handoff-auto, 15:00 UK)

The handoff includes:
- Auto-IG results from last night's run
- Any [AS] submissions that need live-session extraction
- Backlog status (how many remain)

### Live Session Pickup

When Richard starts a live session and Chrome is available, Watson checks auto-ig-tracking.json for any stocks with `as_status: "queued_for_live"`. Watson proactively submits those [AS] queries and reports when done. This is not a separate scheduled task — it's part of the session-start protocol.

---

## Prompt Templates

The auto-IG system uses the same prompt templates as manual IG:

| Prompt | Template File |
|--------|--------------|
| Business Description (BD) | `AI Prompts/Watson - IG - Business description - REV V03_RB.docx` |
| Change Forces (CF) | `AI Prompts/Watson - IG - Change forces - REFV04_RB.docx` |

Watson adapts these per the AS/Claude Research SOP Step 1 (remove sell-side/expert references for [C], keep for [AS]).

---

## Quality Standards

All outputs follow existing RESEARCHER quality standards:

- **Word count:** BD ≥ 3,000 words, CF ≥ 4,000 words
- **Highlighting:** 30%+ coverage, sentence-level precision (not paragraph-level)
- **Formatting:** 8-15 H2s, 15-25 H3s, heavy bold, tables where appropriate
- **Full length:** Complete output posted, never summarised
- **Pre-flight gate:** Run Step 2.5 checklist from Notion Posting SOP
- **Verification:** Spot-check 1-2 pages per run

---

## Constraints & Failure Modes

| Constraint | Mitigation |
|-----------|-----------|
| AS 10-concurrent Deep Research limit (confirmed 15-Apr-26) | 5-stock nightly cap = 10 AS reports = single wave, no batching needed |
| AS requires Chrome browser | Best-effort overnight; queue for live session if unavailable |
| JSON staleness (>7 days old) | Block execution, log warning. Saturday refresh should prevent this. |
| Manifest coverage gaps (529 tickers) | Skip stocks without page_ids. Backfill project will improve this over time. |
| Large backlog on first run | 5/night cap. Delta stocks jump queue. Clears over ~50+ nights for full backlog. |
| Sub-agent output quality | Word count gates, ticker verification, section checks per RESEARCHER SOP |

---

## First-Run Consideration

On the first run, the backlog sweep will identify up to ~267 current 8/8 stocks that may not have IG research. Many of these are large-caps that Richard may have already researched manually (outside Watson). The tracking file starts empty, so the first few nights will produce the most output.

**Richard should review the first overnight report** and may want to bulk-mark certain tickers as "completed" in tracking (e.g., current portfolio positions, stocks already triaged manually). Watson can do this on request.

---

## Key Files

| File | Location | Purpose |
|------|----------|---------|
| This SOP | `memory/skills/auto-ig-research/SKILL.md` | Master reference |
| Scanner script | `scripts/auto_ig_scanner.py` | Detects candidates |
| Tracking state | `snapshots/auto-ig-tracking.json` | Persistent processing state |
| Overnight reports | `memory/reports/auto-ig-overnight-YYYY-MM-DD.md` | Nightly execution logs |
| RESEARCHER SKILL.md | `memory/skills/researcher/SKILL.md` | IG pipeline logic |
| AS/Claude Research SOP | `memory/skills/researcher/as-claude-research-sop.md` | Execution mechanics |
| Notion Posting SOP | `memory/skills/researcher/notion-posting-sop.md` | Posting mechanics |
| **Master Dashboard filter results** | **`master-dashboard/data/filter-results.json`** | **Primary source — MM99 filter scores (replaces `snapshots/minervini-history.json`)** |
| Master manifest | `snapshots/master_manifest.json` | Ticker → page_id |

---

## Changelog

| Date | Change |
|------|--------|
| 13-Apr-26 | Initial creation. SA/DEVELOPMENT mode. |
