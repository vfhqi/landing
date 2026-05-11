# ⛔ STOP — DO NOT USE THIS FILE ⛔
<!-- [W] STOP banner added 23-Apr-26 after Watson read this file by mistake in a live BGN ESA session. -->

**THIS IS THE DEPRECATED V1 RESEARCHER SKILL. THE LIVE FILE IS `SKILL-V2.md`.**

**If you are reading this, stop immediately and read `SKILL-V2.md` instead. This file contains the OLD 6-template ESA list and the OLD IG/Triaging structure. Using it will cause incorrect research plans.**

---

# RESEARCHER Role Skill — V1 (ARCHIVED — DO NOT USE)
<!-- [W] Created 28-Mar-26. Restructured 02-Apr-26: absorbed IG + KQ pipeline logic, references new AS/Claude Research SOP + Notion Posting SOP. -->

> **⚠️ DEPRECATED (14-Apr-26): This is the V1 RESEARCHER SKILL. The active version is `SKILL-V2.md` (23-query framework, Master Dashboard integration, per-query source assignment). Use V2 for all current work. This file is retained for reference only. Key differences: V1 references pullback-watchlist.json, generate_pullback_data.py, and position-entry-monitor.html — all of which are now deprecated in favour of the Master Dashboard (24-Apr-26). See SKILL-V2.md §Master Dashboard Integration.**

## Purpose

Watson acts as Richard's primary research engine — generating ideas, running structured research workflows, extracting insights from multiple sources, and posting formatted outputs to Notion. This is the master file for the RESEARCHER role. It defines the research pipeline logic (what prompts, how many outputs, what synthesis). The *how* of browser execution and Notion posting lives in the two referenced SOPs.

---

## When to Activate

- Ideas Generation (IG) stage workflows
- Key Question (KQ) research
- Early-Stage Assessment (ESA) workflows
- Deep-Dive (DD) workflows
- Earnings preparation and post-earnings analysis
- Industry/thematic research
- Monitoring (TIs, Drivers, Reassessment Criteria)
- Info Flow SOPs

---

## Referenced SOPs

| SOP | File | Covers |
|---|---|---|
| **Research Execution SOP** | `as-claude-research-sop.md` | Claude [C]: native execution via web search + writing. AlphaSense [AS]: browser submission, fire-and-forget, URL bookmarking, extraction. Prompt adaptation. Batch planning. |
| **Notion Posting SOP** | `notion-posting-sop.md` | Sentiment highlighting → format → post to Stock Notes DB → verify. Full-length rule. Chunking for large memos. |
| **Briefing Note SOP** | `briefing-note-sop.md` | Automatic capture of ESA/DD research briefings as tagged Stock Notes pages. Synthesised memo format. Triggers on any ESA/DD briefing — no permission asked. |

**All research types below use these SOPs.** This file defines only pipeline-specific logic: which prompts, how many outputs, what synthesis.

---

## Critical Rules (Cross-Research-Type)

1. **Dual-source mandatory:** Every research question runs through BOTH Claude AND AlphaSense. Post as separate [C] and [AS] pages. Never blend. [D]
2. **Full-length posting:** Never summarise. The Notion page IS the memo. [D]
3. **30%+ highlighting:** Mandatory on all postings. [D]
4. **IAJA synthesis:** SKIPPED at IG stage. Only mandatory at ESA and DD stages. Uses [W] tag. [D] (Updated 07-Apr-26: Richard instructed "Don't do the IAJA" for IG.)
5. **Premortem variant:** Always use REFV02_RB. REFV01_RB and REFV01_Cowboy are permanently discarded. [D] (01-Apr-26)
6. **Prompt adaptation:** Remove sell-side/expert interview references for Claude [C] prompts. Keep them for AlphaSense [AS]. This is the ONLY systematic difference. [D] (02-Apr-26)
7. **Native [C] execution:** Claude [C] research is done natively by Watson using web search — NOT via browser submission to claude.ai. This eliminates 45-min waits and concurrency limits. [D] (02-Apr-26)
8. **Diligence checks mandatory:** All sub-agent outputs must be validated on return. All AlphaSense submissions must be screenshot-verified. See `memory/skills/diligence-checks/SKILL.md` for full framework. [D] (09-Apr-26)
9. **Output validation gates:** On every sub-agent return, verify: (a) word count ≥ minimum (BD: 3,000w, CF: 4,000w, KQ: 3,000w), (b) correct company/ticker in output, (c) all expected sections present. If word count <50% of minimum, do not post — escalate to Richard. [D] (09-Apr-26)
10. **Briefing note — automatic at ESA/DD:** When Richard briefs Watson on ESA or DD research, Watson automatically saves a synthesised briefing memo to Stock Notes. No permission asked. Tagged as "Watson back-brief" depth, IAJA = Analysis + Judgement + Action needed - Research. Title format: `[W] {TICKER} - {Stage} - Briefing Note - {summary} ({Company Name}) [W] @ DD-Mon-YY`. Full SOP: `briefing-note-sop.md`. [D] (13-Apr-26)
11. **Wisdom Library consult — automatic before research (mandatory):** Before starting any research task, read `wisdom-library/INDEX.json`, filter by keywords matching stock characteristics (industry, sector, setup type, stage, known issues). Load top 5-10 matching model files (cap at 10). Use models to frame/direct research as orientation. Do NOT inform Richard — just apply. If genuinely confused about relevance, ask. Bias toward including more models. [D] (24-Apr-26)
12. **Wisdom Library update — automatic after research (mandatory):** After completing research and posting to Notion, scan output for novel patterns, lessons, or framework insights. If genuinely new: create Bronze model file + update INDEX. If existing model confirmed: update its Examples section + Change Log. Tag: `updated_by: RESEARCHER | DD-Mon-YY | from {TICKER} {STAGE} research`. Do NOT propose — just do. [D] (24-Apr-26)
13. **Notion cross-referencing — Wisdom Library models:** In every Notion posting, include inline model references where relevant (e.g., "This pattern is consistent with the **Cockroaches Never Alone** model [Gold]") AND a summary section at end: `**Mental Models Applied:** Model1 (Tier), Model2 (Tier), ...`. [D] (24-Apr-26)

---

## IDEAS GENERATION (Stage 1)

### Prompts

Three prompts per stock:
1. **Business Description (BD)** — Template: `AI Prompts/Watson - IG - Business description - REV V03_RB.docx`
2. **Change Forces (CF)** — Template: `AI Prompts/Watson - IG - Change forces - REFV04_RB.docx`
3. **Technical Momentum (TM)** — Template: `AI Prompts/Watson - IG - Technical momentum - REFV01_RB.md` [D] (13-Apr-26)

### Prompt Adaptation

**BD + CF:** Fill in: stock/company name and ticker, industry context, any specific angles Richard has flagged. Then apply Claude/AS adaptation per AS/Claude Research SOP Step 1.

**TM:** Fill in: stock/company name and ticker, industry/sector. TM is **[C] only** — no AlphaSense version (AS has minimal technical/chart data). **Position Entry Monitor-first protocol (16-Apr-26):** Watson checks `pullback-watchlist.json` for the ticker. If found, reads `pullback-data.json` and uses monitor data as the quantitative backbone — no FactSet script or manual chart images required. Chart screenshots captured from `position-entry-monitor.html` at 6M/1Y/3Y/5Y via Claude in Chrome. If not found, Watson adds to watchlist and prompts Richard to run `python generate_pullback_data.py`. Full protocol in template `03-ig-tm.md`. **This file is archived — see SKILL-V2.md for current SOP.** [D]

**Prompt complexity ceiling (02-Apr-26):** Keep Research mode prompts to 6 sections max. For the CF template (14 sections), condense into 6 macro-sections or split into 2 separate prompts. TM has 7 sections (Section 7 = Pullback Tests, added 13-Apr-26 — ceiling exception granted as Section 7 is conditional and may be brief for early-stage stocks).

### Outputs: 5 Notion Pages per Stock (IG stage — no IAJA)

<!-- Updated 13-Apr-26: Titles include Stage, 3-10 word summary, and (Company Name) before source tag. Normal hyphens. -->
<!-- Updated 16-Apr-26: Company name REMOVED. Summary expanded to 5-15 word substantive descriptor. See SKILL-V2.md and notion-posting-standard/SKILL.md §8 for current spec. -->

| # | Title | Source |
|---|---|---|
| 1 | `[W] {TICKER} - IG - Business Description - {5-15 word summary} [C] @ DD-Mon-YY` | Claude |
| 2 | `[W] {TICKER} - IG - Business Description - {5-15 word summary} [AS] @ DD-Mon-YY` | AlphaSense |
| 3 | `[W] {TICKER} - IG - Change Forces - {5-15 word summary} [C] @ DD-Mon-YY` | Claude |
| 4 | `[W] {TICKER} - IG - Change Forces - {5-15 word summary} [AS] @ DD-Mon-YY` | AlphaSense |
| 5 | `[W] {TICKER} - IG - Technical Momentum - {5-15 word summary} [C] @ DD-Mon-YY` | Claude (FactSet-enriched) |

**Note (07-Apr-26):** IAJA synthesis skipped at IG stage per Richard's instruction. IAJA only applies from ESA stage onwards.

### Execution Flow

1. Adapt BD + CF prompts for both sources (4 prompts total)
2. For TM: check `pullback-watchlist.json`. If found, extract from `pullback-data.json`. If not found, add to watchlist and prompt Richard to run `python generate_pullback_data.py`. See template `03-ig-tm.md` for full protocol. **Do NOT request FactSet charts from Richard.**
3. Launch [C] BD + CF + TM as parallel native agents (immediate execution, no browser). TM agent receives extracted monitor data. Chart screenshots captured via Claude in Chrome from position-entry-monitor.html.
5. Submit [AS] BD + CF to AlphaSense via Chrome (fire-and-forget, URL bookmarking)
6. [C] agents complete in minutes → highlight and post [C] outputs (BD, CF, TM) to Notion. TM posting includes chart image embedded at top.
7. After 45+ min, retrieve and extract [AS] outputs → highlight and post to Notion
8. Run posting verification spot-check per Notion Posting SOP Step 4

### TM-Specific Execution Notes [D] (13-Apr-26)

- **Position Entry Monitor is mandatory input (16-Apr-26).** Do NOT request FactSet charts from Richard or run `extract_tm_data.py` unless already available. Check `pullback-watchlist.json` → extract from `pullback-data.json` → capture chart screenshots from `position-entry-monitor.html`. Full protocol in template `03-ig-tm.md`. [D]
- **Chart reading adds value for:** (a) full historical stage transitions — 5Y chart, (b) base formation and MA convergence/divergence — 3Y chart, (c) setup emergence and MA crossover sequence — 1Y chart, (d) detailed breakout structure, pullback tests, candlestick patterns, daily volume — 6M chart, (e) cross-checking data extraction values against the more current chart right-edge labels — any chart.
- **Chart-data discrepancy handling:** The chart right-edge labels may be more current than the weekly FactSet Excel export. If values differ, note both and use the chart values as the more current reference. Flag the Excel date in the memo header.
- **Dashboard cross-reference.** For the Momentum & Relative Strength section, Watson should also reference the stock's sector and industry momentum from the RS & Breadth Dashboard.
- **If FactSet Excel is stale (>7 days old):** Flag to Richard that the data may be outdated and note the Excel file date in the memo header.
- **Score history from minervini-history.json** is automatically included in the extraction output. Use it to show the trajectory of the 8-point score over recent weeks.
- **Notion embedding:** All 4 chart images are posted to the Notion TM page as image blocks at the top of the memo (after the header, before the Overall Summary). This gives Richard the visual reference alongside the narrative.
- **Section 7 (Pullback Tests):** Only applies when stock is in Stage 2. Catalogues every pullback test in the current Stage 2 advance: which MA tested, depth %, duration, volume pattern, hold/violation, health verdict. Cumulative trend health assessment. For early Stage 2 stocks (0-2 tests), section is brief but describes what to watch for. [D] (13-Apr-26)
- **Vocabulary standard:** Use Richard's terminology throughout: "risk budget" (not "thermal capacity"), "fulcrum driver" (not "key catalyst"), "setup" (not "trade idea"), "park" (not "pass"). See CLAUDE.md glossary. [D] (13-Apr-26)

### Batch Execution (Cycling Multiple Stocks)

[C] prompts: Launch all simultaneously as parallel agents. No concurrency limit.
[AS] prompts: Plan waves respecting 3-concurrent limit. Submit wave 1 → wait 45 min → extract wave 1 + submit wave 2 → repeat.
TM prompts: Run extraction script once per stock (fast), then launch all TM [C] agents in parallel alongside BD/CF agents.

Optimal pattern: While [AS] Wave 1 runs, Watson completes all [C] research (BD + CF + TM) + posting.

### Automated IG (8/8 Minervini Trigger)

**IG research is now automatically triggered for stocks meeting 8/8 Minervini criteria.** The auto-IG system runs nightly (23:30 UK) + mid-week (Wednesday 22:00 UK if fresh FactSet export exists). It uses the same execution flow above but is fully autonomous — no permission required.

**Full SOP:** `memory/skills/auto-ig-research/SKILL.md`
**Scanner script:** `scripts/auto_ig_scanner.py`
**Tracking state:** `snapshots/auto-ig-tracking.json`

Cap: 5 stocks per night. Delta stocks (new <8→8/8) prioritised over backlog. [AS] attempted via Chrome overnight; queued for live session if Chrome unavailable. Richard gates all downstream decisions (triaging, ESA promotion).

---

## KEY QUESTIONS (KQ Research)

**KQs can arise at ANY stage (IG, Triaging, ESA, DD)** but most commonly from ESA onwards. When Richard asks Watson to run the AS/Claude Research SOP for any stock at any stage, Watson always asks: **"Are there any specific KQs you want investigated alongside the standard reports?"** [D] (13-Apr-26)

### Two KQ Types

1. **Researching KQ (REF V05)** — Broad research into a topic. Landscape, data, sources.
   Template: `AI Prompts/kq-workflow/references/kq-researching-template.md`

2. **Analysing KQ (REF V02)** — Framework-driven analysis. Judgement-heavy.
   Template: `AI Prompts/kq-workflow/references/kq-analysing-template.md`

**Default:** Researching. Watson infers from context and proceeds. Only use Analysing when clearly a judgement/framework question.

### Prompt Adaptation

Fill in: stock/topic in title, context paragraph (researcher identity + industry), objective (~3,000 words), higher intent, specific requirements. Guide/Formatting/Audience sections are standard — use as-is. Then apply Claude/AS adaptation.

### Outputs: 2 Notion Pages per KQ

<!-- Updated 13-Apr-26: Stage + summary + (Company Name) before source tag. Normal hyphens. -->

| # | Title (stage known) | Title (thematic/multi-stock) | Source |
|---|---|---|---|
| 1 | `[W] {TICKER} - {Stage} - {KQ Title} KQ - {summary} ({Company Name}) [C] @ DD-Mon-YY` | `[W] {TOPIC} - {KQ Title} KQ - {summary} [C] @ DD-Mon-YY` | Claude |
| 2 | `[W] {TICKER} - {Stage} - {KQ Title} KQ - {summary} ({Company Name}) [AS] @ DD-Mon-YY` | `[W] {TOPIC} - {KQ Title} KQ - {summary} [AS] @ DD-Mon-YY` | AlphaSense |

**Naming:** For single-stock KQs at a known process stage, use the full format including stage. For thematic or multi-stock KQs, `{TOPIC}` = theme name (uppercase) — stage omitted if not clearly associated with one stage.

### Execution Flow

1. Adapt KQ prompt for both sources (2 prompts)
2. Launch [C] KQ as native agent (immediate execution)
3. Submit [AS] KQ to AlphaSense via Chrome (fire-and-forget)
4. [C] agent completes in minutes → highlight and post to Notion
5. After 45+ min, retrieve [AS] → highlight and post to Notion

---

## TRIAGING (Stage 2)
<!-- Updated 13-Apr-26: Added BM&Sector Primer and Guidance (moved from ESA). Clarified SS = Sell Side. Relabelled Earnings Review. -->

### Purpose at Triaging

Triaging determines whether an IG idea is a **good fit** — but at a LIGHT level, based on **pattern recognition** and **"strong views, weakly held"** (sensible hypotheses that need testing with more evidence). The aim is NOT deep analysis but fast, disciplined filtering: does this stock fit a recognisable setup profile? Is the fulcrum driver plausible? Any immediate disqualifiers?

FCS categories assessed at Triaging (LIGHT depth): 1 (Business foundations), 2 (Case inputs), 3 (Setups), 4 (Past trend attributes), 6 (Required simplicity guardrails), 7 (Required case outputs), 13 (Fitness-for-fighting). Categories 5, 8-12 are n/a at this stage.

### Triaging Prompt Templates (in `AI Prompts/`)

| Template | File | Focus |
|---|---|---|
| **Most Recent Earnings Review** | `Watson - Triaging - Earnings review - REFV06_RB.docx` | Latest quarterly results — what just happened. NOT auto-produced at IG; Richard must commission. |
| **GTA — Unknown Key Drivers** | `Watson - Triaging - GTA - Unknown KDs - REF03_RB.docx` | "Greater Than Average" — identifies what's driving above-average performance |
| **GTH Analysis** | `Watson - Triaging - GTH Analysis - REFV04_RB.docx` | "Growth Through Holdings" — M&A-driven growth assessment |
| **Peer GTH Analysis** | `Watson - Triaging - Peer GTH Analysis - REFV02_RB.docx` | Peer comparison of GTH patterns |
| **Sell Side (SS) Analysis** | `Watson - Triaging - SS Analysis - REFV01_RB.docx` | Sell-side analyst views, consensus, rating distribution. **SS = Sell Side, NOT Short Seller.** |
| **IR Contact** | `Watson - Triaging - IR contact - REFV01_RB.docx` | Investor Relations prep / question framing. **Returned in chat — NOT posted to Notion.** |
| **Business Model & Sector Primer** | `Watson - ESA - Business model and sector primer - REFV01_RB.docx` | Industry structure, competitive dynamics baseline. Moved from ESA to Triaging (13-Apr-26). |
| **Guidance** | `Watson - ESA - Guidance - REFV05_RB.docx` | Management guidance, targets, credibility of forward outlook. Moved from ESA to Triaging (13-Apr-26). |

### Outputs

Every research query produces a separate Notion page in Stock Notes DB (dual-source: [C] + [AS]). **Exception:** IR Contact is returned in conversation only, not posted to Notion.

### Execution Flow

1. Read ALL existing Stock Notes pages for the ticker
2. Adapt selected Triaging templates for both [C] and [AS] sources (per AS/Claude Research SOP Step 1)
3. Launch [C] research as parallel native agents
4. Submit [AS] prompts to AlphaSense Deep Research
5. Post all outputs to Notion with 30%+ highlighting (per Notion Posting SOP) — except IR Contact
6. Run posting verification

---

## ESA (Early-Stage Assessment — Stage 3)
<!-- Updated 13-Apr-26: Moved BM&Sector Primer and Guidance to Triaging. Broadened purpose beyond change-only. Relabelled Earnings History. Clarified Short Seller All 10 TEST = non-auto. -->

### Purpose at ESA

ESA has a dual purpose:

1. **Change thesis interrogation:** Is the change significant enough to drive the required financial outputs? Is management dynamic enough to execute? Are the required outputs (EPS trajectory, returns) compelling?
2. **Breadth coverage:** Ensure ALL aspects of the investment case have been covered at light or medium depth. ESA is not just about the change — it's about establishing a comprehensive baseline so that DD can focus on the specific KQs and risks that emerge.

The setup title crystallises during ESA — it emerges from the research, not pre-defined. ESA also establishes the **key risks, key questions, and key confusions** that DD will focus on resolving.

FCS categories assessed at ESA: ALL 13. Many at MEDIUM or ROBUST depth. Categories 4 (Past trend) and 6 (Simplicity guardrails) jump to ROBUST.

### ESA Prompt Templates (in `AI Prompts/`)

| Template | File | Focus |
|---|---|---|
| **History of Earnings Delivery** | `Watson - ESA - Earnings history - REFV01_RB.docx` | Multi-year earnings trajectory and consistency — distinct from Triaging's Most Recent Earnings Review |
| **Tracking vs Guidance** | `Watson - ESA - Tracking vs guidance - REFV01_RB.docx` | Actual delivery vs stated targets — forecast accuracy |
| **Value Chain Analysis** | `Watson - ESA - Value chain analysis - REFV01_RB.docx` | Value chain positioning, margins, power dynamics |
| **Value Chain Map** | `Watson - ESA - Value chain map - REFV01_RB.docx` | Visual/structural value chain mapping |
| **Pre-mortem** | `Watson - ESA - Premortem - REFV02_RB.docx` | Stress-test the thesis. **Always REFV02_RB** (REFV01_RB and REFV01_Cowboy permanently discarded) |
| **CEO/CFO Questions** | `Watson - ESA - CEO_CFO Questions - REFV02_RB.docx` | Preparation for management meetings |
| **Short Seller All 10 TEST** | `Watson - ESA - Short Seller All 10 TEST - REFV02_RB.docx` | Bear case stress-test (10 dimensions). **TEST = WIP, do not auto-run. Ask Richard if it should be run.** |
| **KQ Researching** | `Watson - ESA_DD - Researching a KQ - REFV05_RB.docx` | Broad research into a specific question |
| **KQ Analysing** | `Watson - ESA_DD - Analysing a KQ - REFV02_RB.docx` | Framework-driven analysis of a specific question |
| **KQ Cost/Margins** | `Watson - ESA_DD - Researching KQ - Cost_margins - REFV01_RB.docx` | Specific cost/margin deep-dive |

### Outputs: New Notion Page per Query

Every research query produces a separate Notion page in Stock Notes DB. Each [C] and [AS] output = its own page. Purpose: feed Richard + APM role for their ANALYSIS and JUDGEMENT. IAJA synthesis mandatory at end of ESA stage (uses [W] tag).

### Execution Flow

0. **Post Briefing Note** — Watson automatically captures and posts the ESA/DD briefing to Stock Notes per `briefing-note-sop.md`. This happens BEFORE any research execution.
1. **Read ALL existing Stock Notes pages for the ticker** — always, before any research begins
2. Read Claude system notes / prior Watson work on the stock
3. Adapt selected ESA templates for both [C] and [AS] sources (per AS/Claude Research SOP Step 1)
4. Launch [C] research as parallel native agents
5. Submit [AS] prompts to AlphaSense Deep Research (set up company profile first if needed)
6. Post all outputs to Notion with 30%+ highlighting (per Notion Posting SOP)
7. Run posting verification
8. IAJA synthesis at end of stage

### Template Selection

Watson selects which ESA templates to run based on:
- Richard's brief (specific focus areas, KQs)
- What's already available in Notion from IG and Triaging stages
- The central change thesis — prioritise templates that test the significance and credibility of the change
- Breadth check — ensure all aspects of the case are covered at appropriate depth per the 13 Case Attribute categories
- Richard may specify a subset; if not, Watson proposes a template plan for sign-off
- **TEST prompts** (e.g., Short Seller All 10 TEST) are NOT auto-run; Watson asks Richard if they should be included

### AlphaSense Setup

If the stock does not have an existing AlphaSense company profile or saved search, Watson creates one as part of ESA setup. This is RESEARCHER's responsibility.

---

## DD (Deep-Dive — Stage 4)
<!-- Updated 13-Apr-26: Clarified TEST prompts, relabelled, added FX note. -->

### Purpose at DD

Resolve the key questions identified at ESA. Stress-test the fulcrum driver thesis. Fill gaps, complete the case. ALL 13 FCS categories at ROBUST depth.

### DD Prompt Templates (in `AI Prompts/`)

| Template | File | Focus |
|---|---|---|
| **FX Exposure** | `Watson - DD - FX exposure - REFV01CGPT.docx` | Currency risk analysis. **Note: CGPT-origin prompt, flagged for future rewrite.** |
| **Insider Comments** | `Watson - DD - Insider Comments - REFV01_RB.docx` | Management commentary deep-dive |
| **Management & Governance Checks** | `Watson - DD - Management and governance checks - REFV01_RB.docx` | Operator quality, governance structure |
| **Researching a CEO** | `Watson - DD - Researching a CEO - REFV01_RB.docx` | CEO background, track record, quality |
| **Case Summarisation (TEST)** | `Watson - DD - TEST Case Summarisation - REFV01_RB.docx` | Investment case synthesis. **TEST = WIP, do not auto-run. Ask Richard.** |
| **FDJ Notes Test (TEST)** | `Watson - DD - TEST FDJ notes test - REFV01_RB.docx` | Experimental. **TEST = WIP, do not auto-run. Ask Richard.** |
| **KQ Researching** | `Watson - ESA_DD - Researching a KQ - REFV05_RB.docx` | Broad research KQ (shared with ESA) |
| **KQ Analysing** | `Watson - ESA_DD - Analysing a KQ - REFV02_RB.docx` | Framework-driven analytical KQ (shared with ESA) |
| **KQ Cost/Margins** | `Watson - ESA_DD - Researching KQ - Cost_margins - REFV01_RB.docx` | Specialised cost/margin KQ (shared with ESA) |

### Outputs

Multiple dual-source Notion pages. IAJA Synthesis mandatory at end of stage. Full case file produced.

## MONITORING

Regular monitoring of LIVE positions (TIs, Drivers) and watchlist names (Reassessment Criteria). Uses same SOPs. Watson proactively communicates status changes. APM role intersects here. (SOPs TBD.)

## INFO FLOW

Regular packages of new information on defined topics. Uses same SOPs. (SOPs TBD.)

## EARNINGS

- **Pre-earnings:** Consensus estimates, key drivers, bull/bear scenarios
- **Post-earnings:** Key data points, assess vs expectations, flag thesis implications. Immediate reaction note + detailed analysis within 24h.

---

## Research Quality Standards

### From Richard's Journals and Corrections

1. **Always have a conclusion.** No analysis without judgement. No "it depends." Strong views, weakly held. [D]
2. **Show full reasoning chain.** Don't skip steps. Richard wants to see how Watson arrived at the conclusion. [D]
3. **Right-to-left thinking.** Start with the financial output (predictable 18M-3Y EPS), work backwards. Don't get lost in business description without connecting to financials.
4. **ACH approach.** Don't solve for "yes." Build profiles of "no," "false friend," and "yes." Systematically test evidence against each.
5. **Flag confidence level and key assumptions.** When uncertain: best guess + flag assumptions. Only stop if stakes are high. [D]
6. **"Hell Yeah or No" filter.** Don't over-research mediocre ideas. If it doesn't pass initial excitement test, park it.
7. **Goldilocks growth check.** 20-30% is sweet spot. 10% = inflection unlikely. 50-70% = too hard to forecast.
8. **False friend detection.** Zero clarity of transmission mechanism from company actions to EPS = false friend. Flag immediately.

### Research Pitfalls to Avoid (from Lessons)

- **Trees not wood:** Getting lost in detail without maintaining strategic view (XVIVO lesson)
- **Solving deteriorations analytically:** If a stock is deteriorating, the answer is exit review, not more research
- **Lazy extrapolation of cyclical highs:** Most demand pulses totally reverse to trend. Assume 100% cyclical/temporary unless proven structural (Avanza, Covid stocks)
- **Vague financial analysis:** IR calls and investment cases must be financial-centric, not narrative-driven (Avanza lesson)
- **Narrow frame distraction:** Maintain the forest view

---

## What Richard Values in Research

- **Predictability obsession:** Can Watson track and forecast the EPS trajectory? Singular focus.
- **Evidence of quality dimensions:** Not theoretical moats — demonstrated pricing power, customer loyalty, execution.
- **Revenue optionality mapping:** M&A, geographic, product, pricing optionality. Multiple sources = de-risked.
- **Operator quality assessment:** "Animal CEO" (Slootman archetype). Holistic/congruent culture. Attacking, not defensive.
- **Supply chain physics:** Companies supplying into physically tight supply chains (Diploma-type).
- **Thematic agnosticism:** Watch all industries. No dogmatisms. "Knowledge optionality."
- **Management meeting prep: