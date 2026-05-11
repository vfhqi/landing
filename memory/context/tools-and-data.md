# Tools and Data Map
<!-- [W] Reconstructed 27-Mar-26. Updated 15-Apr-26: IC Ratings database system added. -->

## Primary Tools

### Notion
**Role:** Central knowledge base and research repository
**Key databases:**
- **Stock Notes DB** — `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2` — All research memos, KQ outputs, Watson postings
- **Tasks DB** — Watson task execution source (watson-task-executor protocol)
- **Personal Journal** — Richard's reflections, SOPs, OKRs (source for investment-philosophy.md)
- **Watchlist / Squad** — Universe tracking and pipeline management

**Watson writes directly to Notion** for all internal work. Standard properties for Stock Notes:
- Note title with [W] prefix and source tag ([C] or [AS])
- Stock(s) relation (e.g., MTU → `https://www.notion.so/30b35e909b0b804ea82ace304e666733`)
- Case component tags ([KC], [KR], Inputs/change forces, etc.)
- Depth of note (Watson posting, Memo-ish, etc.)
- IAJA tags (Information, Analysis, Judgement)
- Date

### AlphaSense
**Role:** Proprietary document search — transcripts, broker research, news, filings
**Entry point:** `https://research.alpha-sense.com/gensearch` (Generative Search / Deep Research)
**Default mode:** Deep Research (10+ min, comprehensive). Auto mode only if explicitly requested.
**SOP:** Always run in parallel with Claude analysis. Post as separate [C] and [AS] pages to Notion.
**Known issues:** PerimeterX CAPTCHA blocking — Richard may need to complete manually. Content extraction via DOM JavaScript, not get_page_text. Mount caching bug when overwriting files.

### FactSet
**Role:** Financial data, screening, monitoring, consensus estimates
**Access:** Via Chrome (no direct API connector)
**Used for:** Quantitative data, consensus tracking, screening universe

### Excel + FactSet Plugin (RS & Breadth Engine)
**Role:** Financial models, universe database, sizing framework, portfolio dashboard, **market monitoring (RS & Breadth)**
**Files:** On Richard's local machine (OneDrive). RS & Breadth Engine template at `COWORK/outputs/RS-Breadth-Engine-Template.xlsx`.

**RS & Breadth Engine** (built 30-Mar-26):
- **Purpose:** Daily relative strength and breadth monitoring across Richard's full ~1,414-stock European universe. Feeds the "Fit for Fighting" market assessment domain.
- **Architecture:** 3 layers — (1) Excel + FactSet `=FDS()` formulas pull price data, (2) Python script processes CSV export into JSON, (3) Self-contained HTML dashboard for consumption.
- **Metrics:** RS Ratio (price ratio trend), Excess Return (bps ranking), Breadth (% above 20d/50d/200d MAs, % positive returns), RS Direction (rising/flat/falling).
- **Dimensions:** Notion-sourced taxonomy — 17 industries, 84 sectors (75 with active stocks), ~34 geographies. Equal-weighted. Timeframes: 1D, 1W, 1M, 3M.
- **Dashboard features:** Industry/sector/geography drill-down to constituent stocks, relative vs absolute mode toggle, sort by timeframe or name, breadth chart, distribution chart, 52-week price range indicators on stock views.
- **Data architecture (updated 01-Apr-26):**
  - **Notion = master** for universe membership + taxonomy (Industry, Sector). Source file: `stock_mapping_final.json` (1,400 tickers).
  - **FactSet = financial data** (returns, consensus estimates, ratings, TP) + display fields (company name, geography). Source: Excel export in `Files/Universe - YYYY_MM_DD.xlsx`.
  - **Pipeline:** `generate_dashboard.py` reads both → produces `rs-breadth-dashboard.html`.
  - **Weekly refresh:** `dashboard-weekly-refresh` scheduled task (Sundays 20:00 UK). Checks Notion for universe/taxonomy changes, regenerates dashboard.
- **Key files:**
  - `COWORK/generate_dashboard.py` — Pipeline script (Notion JSON + FactSet Excel → HTML)
  - `COWORK/rs-breadth-dashboard.html` — Live dashboard (FactSet data, ~1,392 stocks)
  - `COWORK/stock_mapping_final.json` — Notion-sourced ticker → (sector, industry) mapping
  - `COWORK/notion_mapping.json` — Notion page URL lookups (sectors, industries, geographies)
  - `COWORK/notion_reverse_lookup.json` — Reverse URL → name lookup for relation resolution
  - `COWORK/Files/Universe - 2026_04_01.xlsx` — Latest FactSet export (FS sheet: 78 cols of financial data)
  - `COWORK/outputs/Fundamental-Momentum-Spec.md` — Full specification
  - `COWORK/outputs/RS-Breadth-System-Spec.md` — Original system spec
- **Fundamental Momentum Panel** (added 30-Mar-26, live 01-Apr-26):
  - **Metrics:** Adj. EPS/Revenue/Adj. EBITDA revision % (computed from raw historical estimate snapshots in cols AW-BM), Target Price revision %, %Buy ratings (normalised to exclude No Rating/Restricted), % Buy Change (pp), Revision Breadth, Fundamental Direction.
  - **Timeframes:** 1M, 3M, 6M.
  - **Sortable estimates:** EPS, Revenue, EBITDA, Target Price, % Buy Change.
  - **Colour thresholds:** ±0.5/2/5% (different from technical panel's ±50/100/200 bps).
  - **Known issues:** Revision breadth (UP/DOWN counts) still returning 0 from FactSet — needs correct formula from FactSet support. Ratings normalised but raw delta used for change column.
- **Status:** LIVE with real FactSet data (01-Apr-26). Both panels operational. ~88% EPS coverage, ~90% TP coverage, ~92% ratings coverage.
- **APM integration (not a build skill — a reading/judgement skill):** Watson's APM role should consume the dashboard output to: (1) flag industries/sectors with deteriorating RS and breadth as risk signals, (2) suggest new ideas from industries/sectors showing improving momentum, (3) run a "momentum health check" on held positions — when RS direction is falling AND breadth is weak AND excess returns negative across 1W/1M/3M, proactively challenge Richard to re-justify the position. Richard self-identifies holding negative momentum names too long as a key behavioural weakness [D, 30-Mar-26]. The dashboard exists to combat this.

### Outlook
**Role:** Email + calendar
**Access:** Via Chrome only (no MCP connector). Watson should never send emails without approval.

### Gmail
**Role:** Secondary email. Connected via MCP but rarely used for investing work.

---

## Watson (Claude) Workflow

### Research Execution
Every research question runs through BOTH Claude AND AlphaSense:
1. Claude agent does web research + reasoning → produces [C] memo
2. AlphaSense Deep Research searches proprietary docs → produces [AS] output
3. Both posted to Notion as separate pages with sentiment highlighting

### Posting Conventions
- All Watson outputs tagged [W] in Notion
- Source suffix: [C] for Claude, [AS] for AlphaSense
- 30%+ sentiment highlighting on all posted content
- Green = bullish, Yellow = mixed, Red = bearish
- Large memos chunked for Notion API limits

### Prompt Library
Located in `COWORK/AI Prompts/`. Organised by process stage:
- `Watson - IG - *.docx` — Ideas generation prompts (BD, CF)
- `Watson - ESA - *.docx` — Early-stage assessment prompts
- `Watson - DD - *.docx` — Deep-dive prompts
- `Watson - ESA_DD - *.docx` — Cross-stage KQ prompts
- `Watson - Monitoring - *.docx` — Monitoring prompts

### IC Ratings Database System (15-Apr-26)
**Role:** Structured cross-stock database for Six Pillars IC ratings, monitoring plans, and findings. JSON source of truth with automated rollup and HTML dashboard.

**Architecture (5 layers):**
1. **Decision Layer** — `databases/master/ic-ratings-current.json`: One row per stock, ~20 fields. Pillar-level A-F scores, investment_case (setup, FDs, KDs, transmission clarity), actions (recommendation, next steps, parking reason).
2. **Detail Layer** — `databases/detail/p1-p6*.json`: Per-attribute A-F ratings within each pillar. P3 has ~23 attributes (Inputs, Outputs, Momentum). P4 has ~40 attributes across 8 families. ~107 fields total across 6 pillars.
3. **Historical Layer** — `databases/historical/snapshots.json`: Point-in-time snapshots of master ratings. Taken after each stage-gate decision.
4. **Information Layer** — RESEARCHER output (Notion), RS & Breadth Dashboard, Excel models.
5. **Presentation Layer** — Notion pages (synced from JSON) + standalone HTML dashboard (`databases/ic-ratings-dashboard-live.html`).

**Key scripts:**
- `databases/scripts/rollup.py` — Computes master pillar scores from detail ratings. Weighted worst-of: 60% bottom quartile, 40% overall weighted average. Family-specific weights for P4, EPS 2x for P5.
- `databases/scripts/build-dashboard.py` — Injects live JSON into HTML template. Produces standalone dashboard with three tabs: IC Ratings (filterable/sortable, colour-coded), Monitoring Plan, Findings Log.

**Monitoring subsystem:**
- `databases/monitoring/monitoring-plan.json` — APM defines items (SUBJECT, OBJECTIVE/LTI, HOW, WHY, FREQUENCY). RESEARCHER executes.
- `databases/monitoring/findings-log.json` — Time-series observations linked to monitoring items. APM reviews at next cycle.

**Workflow integration:** APM writes to database after every FCS Analysis + Judgement cycle. RESEARCHER reads monitoring plan for execution. Dashboard is the at-a-glance view for Richard. Notion sync (future) will push master data to Stocks DB.

### Data Flow
```
Prompts (COWORK/AI Prompts/) → Watson execution (Claude + AS) → Notion (Stock Notes DB)
                                                                      ↓
                                                              Richard reviews
                                                                      ↓
                                                         Pipeline decisions (progress/park)
                                                                      ↓
                                                    APM writes to IC Ratings DB (JSON)
                                                                      ↓
                                                    rollup.py → master scores computed
                                                                      ↓
                                              build-dashboard.py → HTML dashboard refreshed
```
