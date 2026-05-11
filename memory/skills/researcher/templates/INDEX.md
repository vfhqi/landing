# ESA Research Templates — Index

## Overview
This directory contains 7 self-contained research templates for the RESEARCHER role at **Stage 3: Early-Stage Assessment (ESA)**. Each template is a standalone reference guide for executing a specific research query, designed to feed the APM's judgement process across two ESA passes.

## Template Structure (All Files)
Each template follows this format:
- **MISSION:** What the query produces (word count, deliverable)
- **CONTEXT — What the Reader Cares About:** Audience profile, ESA purpose, why this query matters, relevant mental models
- **PROMPT — [AS] Version:** Full AlphaSense research prompt (if applicable)
- **PROMPT — [C] Version:** Full Claude/WebSearch research prompt (if applicable)
- **EXECUTION:** Source-specific notes and quality gates

## Templates (Queries 8-14)

### Query 8: Business Model & Sector Primer — AS + C (dual-source)
**File:** `08-esa-bm-sector-primer.md`
**Word count:** 3,000+ per source version
**Sources:** AS (sell-side research, FactSet), C (WebSearch, public filings)
**Purpose:** Comprehensive industry structure primer and business model deep-dive
**Key outputs:** Industry overview, value chain mechanics, competitive landscape, barriers to entry, financial profiles, {COMPANY}'s positioning, key success factors, sceptical view

---

### Query 9: Earnings History L3Y — AS ONLY
**File:** `09-esa-earnings-history.md`
**Word count:** 3,000+ words
**Sources:** AS only (FactSet, Bloomberg, sell-side research, earnings calls)
**Purpose:** Multi-year earnings trajectory and consistency analysis
**Key outputs:** Quarterly/semi-annual earnings summary table (12-16 periods), trajectory inflections, quality assessment (recurring vs one-off, working capital, cash conversion), beat/miss patterns, seasonal trends, guidance credibility, forward plausibility

---

### Query 10: Short-Sellers & Bear Case — AS + C (dual-source)
**File:** `10-esa-short-sellers.md`
**Word count:** 3,000+ per source version
**Sources:** AS (sell-side bearish views, expert commentary), C (WebSearch, published reports, SEC filings, public commentary)
**Purpose:** Comprehensive survey of published short reports, bearish views, and critical analyses
**Key outputs:** Formal short reports (if any) + SI data, bearish sell-side views, accounting red flags, governance concerns, online bearish commentary, counter-arguments to bull case, historical patterns, bear evidence quality assessment, downside scenarios, skeptical rebuttals to bear case

---

### Query 11: Value-Chain Map — Claude ONLY
**File:** `11-esa-value-chain-map.md`
**Word count:** 3,000+ words
**Sources:** C only (WebSearch, public filings, industry reports, competitor presentations)
**Purpose:** Structured value-chain mapping from raw inputs to end customer
**Key outputs:** End-to-end value chain diagram/description, {COMPANY}'s position and integration level, adjacent stages (suppliers and customers), margin distribution across stages, power dynamics and pricing leverage, competitive map at {COMPANY}'s stage and adjacent stages, structural evolution/consolidation, {COMPANY}'s competitive advantages in chain position, vulnerabilities, strategic implications

---

### Query 12: Value-Chain Analysis — AS ONLY
**File:** `12-esa-value-chain-analysis.md`
**Word count:** 3,000+ words
**Sources:** AS (sell-side research, earnings calls, expert commentary, FactSet)
**Purpose:** Deep analysis of value-chain relationships and dynamics
**Key outputs:** Customer analysis (concentration, churn, satisfaction, switching costs, pricing leverage), supplier analysis (concentration, input cost trends, supply risk), competitor analysis (market share, competitive responses, pricing), distributor/channel analysis, cross-value-chain signals (what suppliers/customers/competitors are saying), structural changes in value chain, NWC trends, value-chain stress signals, margin sustainability assessment, sceptical view on assumptions

---

### Query 13: Guidance Tracking & Credibility — AS ONLY
**File:** `13-esa-guidance-tracking.md`
**Word count:** 3,000+ words
**Sources:** AS (FactSet consensus, Bloomberg, sell-side research, company guidance, earnings calls)
**Purpose:** Management guidance history, accuracy, credibility assessment
**Key outputs:** Current forward guidance statement, historical guidance accuracy tables (L4 periods with variance analysis), beat/miss patterns (sandbagging vs over-promising), estimate revision trends, key assumptions behind guidance (with sensitivity analysis), credibility assessment (Red/Orange/Yellow/Green), sell-side consensus on guidance, forward tracking metrics, scenario analysis (base/bull/bear), forward guidance update risk, sceptical challenge to guidance assumptions

---

### Query 14: Watson KD Assessment — ESA — AS + C (dual-source)
**File:** `14-esa-kd-assessment.md`
**Word count:** 4,000+ per source version
**Sources:** AS (sell-side research, earnings calls, expert commentary), C (WebSearch, filings, news archives)
**Purpose:** Targeted deep-dive on APM-identified Key Drivers (fulcrum and supporting) — UNIQUE SEQUENCING requirement
**Key outputs:** For EACH APM-identified driver: precise definition, bull case evidence, bear case evidence, forward trajectory plausibility, sell-side expectations, evidence gaps, Watson rating (Red/Orange/Yellow/Green), fulcrum-level assessment, cross-driver interactions, fulcrum-level synthesis, comparison to Triaging assessment, Watson back-brief for APM Pass 3 refinement

**CRITICAL UNIQUE FEATURE:** This query requires {APM_KD_SUMMARY} placeholder — parent RESEARCHER inserts the APM's Pass 1 key findings (identified drivers, suspected fulcrum drivers, evidence gaps, setup hypothesis, open questions). This creates a tight feedback loop between APM judgement (Pass 1) and RESEARCHER evidence (Pass 2).

---

## Sequencing in ESA Workflow

### Stage 3a: Triaging (8 queries — STAGE 2)
RESEARCHER executes 8 Triaging queries (not included in this template set). APM reads output, applies FCS framework.

### Stage 3b: ESA Pass 1 — FCS Analysis & Judgement (APM work)
APM reads Triaging output, runs FCS Analysis across 5 Pillars and 13 Categories, identifies preliminary key drivers and risks, flags evidence gaps, proposes setup classification, posts to Notion.

### Stage 3c: ESA Pass 2 — Deep-Dive Research (THIS TEMPLATE SET)
RESEARCHER executes Queries 8-14 (these 7 templates) in ~2-5 day window, posting each to Notion as completed. APM reads selectively, focusing on Query 14 (KDs) and any flagged evidence gaps.

**Execution order (recommended):**
1. Query 8 (BM/Sector Primer) — foundational
2. Query 9 (Earnings History) — foundational
3. Query 10 (Short-sellers) — foundational
4. Query 11 (Value-Chain Map) + Query 12 (Value-Chain Analysis) — can run in parallel
5. Query 13 (Guidance Tracking) — after fundamentals are clear
6. Query 14 (KD Assessment) — LAST, after APM has provided KD summary; requires {APM_KD_SUMMARY} input

### Stage 3d: ESA Pass 3 — Judgment Refinement (APM work)
APM reviews Query 14 output, refines FCS ratings, finalizes setup classification and key risks, posts final ESA summary and DD priorities.

---

## Quality Standards (All Templates)

**Word count gates:**
- Queries 8, 9, 10, 11, 12, 13: Minimum 3,000 words
- Query 14: Minimum 4,000 words
- Applies per source version (AS and C have separate minimums where dual-source)

**Quantification requirement:**
- Every assertion about financials, metrics, trends, or probabilities must include specific numbers or percentages
- "Revenue is growing" ❌ → "Revenue growing 12% CAGR over L3Y" ✓

**Highlighting (Notion posting):**
- 30%+ coverage of key evidence, judgements, risks, and uncertainties
- Use process_report.py to highlight all Notion postings

**Bullet discipline:**
- 12-18 bullets per major section (Query 14: 8-12 per driver)
- No bullet exceeds 150 words
- Bullets should be self-contained; avoid referencing prior bullets

**Table requirement:**
- Minimum 1-2 summary tables per query (varies by query; see EXECUTION section of each template)
- Tables must be clean, readable, quantified, and reference-able from text

**Scepticism requirement:**
- Every query must include explicit bear-case or sceptical view section
- Do not dismiss bear case; present it fairly with supporting evidence
- Rate drivers/assertions on Red/Orange/Yellow/Green scale with explanation

**No repetition:**
- Each section must add new information, not restate prior sections
- Avoid copy-pasting between templates (each is independent)

---

## Audience Context (Embedded in All Templates)

**Reader profile:**
Concentrated, long-only equity investor (5-15 positions), UK/Europe focus, $5-50bn market cap sweet spot, 12-24M hold period, singular focus on predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**ESA purpose (embedded in all):**
(1) Interrogate the change thesis — is the change significant enough to drive required financial outputs? Is management dynamic enough to execute? Are the required outputs (EPS trajectory, returns) compelling?
(2) Breadth coverage — ensure ALL aspects of the investment case are covered at light or medium depth. The setup title crystallises during ESA. ESA also establishes the key risks, key questions, and key confusions that DD will focus on.

---

## Notion Posting Convention

**Standard format for all ESA Query outputs:**
- **Title:** `[W] {TICKER} — Query Name [Source] @ DD-Mon-YY`
  - Example: `[W] DKSH — Business Model & Sector Primer [AS] @ 14-Apr-26`
- **Tags:** #ESA #{QueryTheme}
- **Structure:** Executive summary (500 words, top of page) + detailed sections + summary tables
- **Highlight:** 30%+ coverage using process_report.py
- **Link back:** Cross-link to Stock Notes page and any related Notion pages (e.g., Query 14 links to APM's Pass 1 FCS Analysis)

---

## Placeholder Conventions

**Standard placeholders (fill in via script or manual insertion):**
- `{TICKER}` — stock ticker (e.g., DKSH)
- `{COMPANY}` — full company name (e.g., Dksh Holding Ltd)
- `{INDUSTRY}` — industry category (e.g., business services & supplies)
- `{PEERS}` — comma-separated list of 3-5 key competitors (e.g., RELX, Experian, IHS Markit)
- `{ANGLES}` — 2-3 key investment angles identified in Triaging (e.g., margin expansion, customer wins, market share gains)
- `{KDs}` — key drivers identified (filled in by RESEARCHER based on Triaging and APM feedback)

**Unique placeholder (Query 14 only):**
- `{APM_KD_SUMMARY}` — structured summary of APM's Pass 1 key findings, inserted by parent RESEARCHER/APM before executing Query 14 research

---

## Handoff & Continuity

**From RESEARCHER to APM (Pass 2 to Pass 3):**
- RESEARCHER completes Queries 8-14, posts each to Notion
- Query 14 includes "Watson Back-Brief" section with explicit recommendations on: (a) fulcrum-level drivers, (b) setup classification confirmation/challenge, (c) key monitoring metrics, (d) DD priorities
- APM uses Query 14 back-brief to refine Pass 1 judgement and finalize FCS ratings

**From APM to DD Team (ESA to DD):**
- APM posts final ESA Summary with: (a) setup classification, (b) fulcrum-level drivers (2-3), (c) key risks and evidence gaps, (d) top 5 DD activities
- DD Team uses ESA Summary to scope detailed work, prioritize investigations, and define "success criteria" for each DD work-stream

---

## Version History
- **Created:** 14-Apr-26
- **Status:** Live
- **Applies to:** Stage 3 (ESA Pass 2) research execution
- **Maintenance:** Update as new feedback, calibration, or process refinements emerge. Keep track of changes in COWORK/memory/corrections.md.

---

## Related Files in System
- `memory/context/investing-system.md` — system architecture, 6-stage process, ETCs, operating system map
- `memory/skills/researcher/SKILL.md` — main researcher skill overview and SOP
- `memory/skills/assistant-portfolio-manager/SKILL.md` — APM FCS framework and ESA Pass 1 methodology
- `memory/corrections.md` — calibration log of researcher/APM feedback and process refinements
- `AI Prompts/kq-workflow/SKILL.md` — KQ (Key Question) research workflow (related but different methodology)
