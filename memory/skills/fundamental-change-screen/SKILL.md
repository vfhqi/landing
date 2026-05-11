# Fundamental Change Screen — SOP

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 12-Apr-26, V5 12-Apr-26, V6 13-Apr-26. System Architect role, DEVELOPMENT mode. -->
<!-- V7 15-Apr-26: Six Pillars supersedes 4-pillar framework. A-F scale replaces G/Y/O/R. 26-deliverable APM structure. Database integration. -->
<!-- Owner: RESEARCHER (information) + APM-Analysis (attributes) + APM-Judgement (setups) + Richard (decisions) -->

## Purpose

This SOP governs the **Fundamental Change Screen** — the qualitative analytical framework Watson uses to classify whether a European equity is exhibiting genuine fundamental change that could drive an Earnings Power Step-Up (EPSU) or Earnings Power Transformation (EPT).

The screen exists because Richard's alpha comes from one source: **identifying stocks where 18M-3Y EPS will be materially higher than the market currently expects**. The market makes specific, identifiable errors in how it processes fundamental change. Each of the 6 setup profiles below exploits a different type of market error. The screen's job is to identify the error type, assess the evidence, and classify the stock accordingly.

This is NOT a technical screen and NOT a mechanical filter. It is a structured qualitative assessment framework — a disciplined way of asking "what is changing at this company and why is the market wrong about it?"

**Framework version:** Six Pillars of a Target Investment Case (V7, 15-Apr-26). This version supersedes the 4-pillar framework. The existing 4 pillars (Foundations, Inputs, Checks, Outputs) are retained as Pillars III and IV. Three new pillars are added: I (Technical Momentum), II (Market Paradigm Fit), V (SS Earnings Momentum), VI (Valuation).

---

## Referenced SOPs

| SOP | File | Covers |
|-----|------|--------|
| **APM Analysis SOP** | `apm-analysis-sop.md` | How to produce the Analysis component: PRE-ANALYSIS GATE, Triaging format (1-3pp), ESA format (3-5pp), evidence standards, rating scale, posting rules |
| **APM Judgement SOP** | `apm-judgement-sop.md` | How to produce the Judgement component: setup classification, false friend detection, ACH sketch, IAJ+2DSA, meta questions check. Triaging (combined with Analysis), ESA (separate Notion page) |
| **Notion Posting SOP** | `researcher/notion-posting-sop.md` | Highlighting, formatting, chunking, property verification |
| **RESEARCHER SKILL** | `researcher/SKILL-V2.md` (V2.13) | Research pipeline, 22 v2.1 query templates + Q23 thematic (legacy), per-query source assignment, merged [C+AS] page protocol, stage-specific RESEARCHER outputs |

---

## Architecture: Target Investment Criteria vs. Process

**This distinction is fundamental.** The FCS operates across two independent dimensions:

### TARGET INVESTMENT CRITERIA (the "WHAT")
What makes a strong investment case. Organised as:
- **4 PILLARS:** Foundations, Inputs, Checks, Outputs
- **13 ATTRIBUTE FAMILIES** (grouped under the 4 pillars)
- **Individual ATTRIBUTES** (under each family)
- **6 SETUPS** (the patterns being matched against)
- **6 META QUESTIONS + 11 SPECIFIC QUESTIONS** (the judgements to form — see Meta Questions section)
- **20+ CASE COMPONENTS** (the deliverables to produce per stage — tracked separately)

### THE SIX PILLARS (master framework, supersedes 4-pillar structure)

| Pillar | Name | Nature | Rating Scale | Source |
|--------|------|--------|-------------|--------|
| **I** | Technical Momentum | Quantitative/Technical | A-F | **Master Dashboard** (formulaic: MM99 score, filter qualification stages, RS excess returns from `filter-results.json`; MA data from `prices.json`) + RESEARCHER Query #3 qualitative analysis. APM synthesises both. |
| **II** | Market Paradigm Fit | Thematic/Qualitative | A-F | APM judgement |
| **III** | Fundamental Change | Fundamental/Qualitative | A-F | APM analysis + judgement (Inputs + Outputs + Setup) |
| **IV** | Building Blocks — Robustness | Fundamental/Qualitative | A-F | APM analysis + judgement (Guardrails + Foundations + Constraints) |
| **V** | SS Earnings Momentum | Quantitative | A-F | **Master Dashboard** `factset-ssem.json` (formulaic: revision %, momentum count, EPS 2x weighted) + RESEARCHER earnings analysis. AlphaSense is primary qualitative source. |
| **VI** | Valuation | Returns/Quantitative | A-F | Financial Analyst / APM. **Master Dashboard** `factset-valuation.json` (P/E, percentiles) as supplementary input. |

**Mapping from old 4-pillar to new Six Pillars:**
- Old Pillar I (Foundations) → Now part of new Pillar IV (Building Blocks, "Foundation Quality" family)
- Old Pillar II (Inputs) → Now Pillar III (Fundamental Change)
- Old Pillar III (Checks) → Now part of new Pillar IV (Building Blocks, "Simplicity Guardrails" family + constraint families)
- Old Pillar IV (Outputs) → Now part of Pillar III (Fundamental Change, "Required Case Output Attributes")
- NEW: Pillar I (Technical Momentum) — was always checked via Dashboard/Minervini but not a formal FCS pillar. Now sourced from **Master Dashboard** (`filter-results.json` MM99 filter + `prices.json` MA data)
- NEW: Pillar V (SS Earnings Momentum) — was embedded in GTH/momentum attributes, now a standalone pillar. Quantitative data from **Master Dashboard** `factset-ssem.json`
- NEW: Pillar VI (Valuation) — was attribute 4.12/1.6, now a standalone pillar

### RATING SCALE (A-F, replaces G/Y/O/R)

| Grade | Percentile | Meaning |
|-------|-----------|---------|
| **A** | 90-100% | Top decile. Rare/great. Reserved for genuinely exceptional attributes. |
| **B** | 75-90% | Good. Strong positive signal. |
| **C** | 50-75% | Fine. Acceptable, no concern. |
| **D** | 35-50% | Weak. Concern, needs monitoring or resolution. |
| **F** | Bottom ~33% | Fail. Material negative. May be invalidating depending on attribute. |

**Roll-up logic per pillar:** Detail attribute ratings roll up to pillar scores using weighted worst-of methodology. Negatives weight more heavily than positives. Family-specific weights apply (see database architecture).

**Unclear-excluded rule (15-Apr-26):** If the evidence for an attribute is genuinely insufficient at the current stage depth, rate it as **"—" (unclear)** rather than defaulting to C. Unclear ratings are **excluded from rollup weighting** entirely — they do not drag pillar scores. The distinction: a C means "we assessed this and it's acceptable, not great." Unclear means "we literally do not have enough information to rate this." Common at Triaging: IR helpfulness (no interaction), insider activity (no data), management quality (new appointment too early). As the stock progresses to ESA/DD, unclear attributes should resolve to a letter grade.

### DATABASE INTEGRATION

All ratings are stored in the IC Ratings database system (`databases/` on COWORK drive):
- **Master DB** (`databases/master/ic-ratings-current.json`): One row per stock, six pillar scores, summary fields
- **Detail DBs** (`databases/detail/p3-fundamental-change.json`, `p4-building-blocks.json`, etc.): Per-attribute ratings
- **Historical snapshots** (`databases/historical/snapshots.json`): Point-in-time copies at stage transitions
- **Monitoring Plan** (`databases/monitoring/monitoring-plan.json`): TI monitoring items for RESEARCHER
- **Dashboard** (`databases/ic-ratings-dashboard-live.html`): Standalone HTML presentation layer

**APM write protocol:** After completing Analysis + Judgement, APM writes attribute ratings to detail DBs → runs rollup script → updates master DB → rebuilds dashboard. See `databases/scripts/rollup.py` and `databases/scripts/build-dashboard.py`.

### RESEARCH PROCESS (the "HOW")
How to analyse the criteria, at progressively deeper levels:
- **IG → Triaging → ESA → DD → Live**
- Each stage defines the DEPTH at which each attribute family is assessed (light / medium / robust)
- Each stage has specific RESEARCHER prerequisites and CASE COMPONENT deliverables

### ANALYTICAL PRIORITY — CHANGE FIRST, QUALITY AS PROBABILITY GATE
The primary objective is assessing the **magnitude of fundamental change** in INPUTS and OUTPUTS. Is something big changing? How big? FOUNDATIONS (quality) then serves as the **probability gate** — it tells you how likely the change is to actually manifest versus being derailed by weak management, no moat, competitive pressure, or demand softness. Quality is the bankability check on the change thesis, not the starting point.

**Flow:** "How much is changing?" (Inputs + Outputs) → "How likely is it to actually happen?" (Foundations as probability filter) → "Is the case investable and simple enough?" (Checks as complexity filter)

### THE 6 META QUESTIONS (Judgement Framework)
After APM has completed Analysis and Judgement on attributes and setups, these meta questions serve as the final qualitative catch-all. The aim is to have positive, robust answers for all six — or the case is invalidated (the most common outcome):

1. **Winning pattern fit?** — Does it fit a strong target setup? Any false friend/unacceptable fit?
2. **Bankable beat-and-raise + growth + EPSU + 3Y triple ratchet?** — Are the modal case outputs compelling?
3. **Bankability externally?** — Headwinds? Compelling tailwinds? Favourable value chain?
4. **Bankability internally?** — Business quality compelling? Internal change compelling?
5. **Timely?** — CfC clearing? Past trends supportive?
6. **Sufficient TSR?** — Low multiple in fair range? Compelling return?

These are nebulous, qualitative questions held at the back of the mind throughout the process. They don't replace the attribute analysis — they sit above it as a meta-level sense-check.

---

## Conceptual Foundation

### Two Types of Fundamental Change

Fundamental change manifests in two fundamentally different ways:

**1. Pushing of a Force** — something NEW is being added or intensified:
- A demand explosion arrives at the sector level (Demand-Driven EPSU/EPT)
- A new CEO, strategy, or corporate transformation creates internal push (Corporate Change EPSU/EPT)
- These are ADDITIVE change forces — the market error is failing to model the new force

**2. Removal of a Concern** — something NEGATIVE is abating or clearing:
- A Cause for Concern (CfC) is clearing in a high-quality compounder (CfC Clearing in HQC)
- A cyclical trough is forming and operating conditions are stabilising (Trough-on-Trough)
- An extreme CfC is clearing in a viable but medium-quality business (Huge CfC Clearing)
- These are SUBTRACTIVE change forces — the market error is continuing to price a concern that is resolving

This "pushing vs. removal" distinction shapes everything: the data sources, the assessment criteria, and the conviction framework. Pushing-of-a-force setups require evidence of the NEW thing (demand data, CEO actions, strategy changes). Removal-of-a-concern setups require evidence of CLEARING — that the negative is abating — plus a quality floor (the business must deserve to re-rate once the concern clears).

**CfC + CLEARING:** For Setups 4, 5, and 6, the emphasis is on CLEARING. A Cause for Concern alone is not a setup — it's just a problem. The setup only exists when there is credible evidence that the CfC is clearing or will clear within a defined timeframe. "CfC clearing" is the operative phrase, not just "CfC."

**CfC SCEPTICISM RULE:** Do NOT dismiss CfCs as "transient." Issues the market is worried about often drag longer, go further, and get weirder than expected ("worser, odder, longer, further"). The correct approach: identify a handful of specific issues the market is worried by, assume they are MORE persistent than they appear, and require hard evidence of clearing before downgrading severity. "Transient-looking" issues are precisely the ones that catch investors out. Default to scepticism.

### Naming Convention

**Always refer to setups by their word-based titles, not numbers.** The numeric labels (1-6) are internal shorthand only — all output, Notion posts, and analysis should use the full names:

| Short | Full Title |
|-------|-----------|
| — | **Stable Serial Acquirer** (DEFERRED) |
| — | **Demand-Driven EPSU/EPT** |
| — | **Corporate Change EPSU/EPT** |
| — | **CfC Clearing in HQC** |
| — | **Trough-on-Trough** |
| — | **Huge CfC Clearing (Medium Quality)** |

### The Market Errors Being Exploited

| Setup | Type | Market Error | What the Market Gets Wrong |
|-------|------|-------------|---------------------------|
| Demand-Driven EPSU/EPT | Pushing | **Analytical — future ≠ past** | Extrapolates historical demand levels. Fails to model structural demand explosion. Underestimates operating leverage. |
| Corporate Change EPSU/EPT | Pushing | **Analytical — future ≠ past** | Anchors to old strategy/structure/management. Fails to model corporate transformation. Underestimates pace of INPUT changes translating to OUTPUT changes. |
| CfC Clearing in HQC | Removal | **Emotional/myopia** | Overweights a temporary CfC. Prices a permanent quality discount into a business whose underlying quality is intact. Misses clearing evidence. |
| Trough-on-Trough | Removal | **Emotional/myopia** | At cyclical trough, extrapolates further decline. Fails to recognise operating stabilisation and estimate conservatism. |
| Huge CfC Clearing | Removal | **Emotional/myopia** | Extreme fear prices in worst case for a viable business. Misses clearing event that creates powerful mean-reversion. |

### Relationship to Richard's 4 Patterns

Richard's best investments combine 2-3 of four recurring patterns. The setups are the mechanism through which these patterns manifest:

| Pattern | How It Maps to Setups |
|---------|----------------------|
| **Animal CEO** (Slootman archetype) | Corporate Change EPSU/EPT (layer 1 RESOURCES change) is the strongest single signal. Also feeds CfC Clearing in HQC sub-type 1 (no-CEO CfC clearing when a strong appointment is made). An Animal CEO presence upgrades conviction for ANY setup. |
| **Massive corporate change plan** | Corporate Change EPSU/EPT directly. Most attractive variant: company emerging from a large investment phase — multi-year margin/EPS depression from doing the right thing, then revenue accelerates + margins expand as one-off costs fall away + operating leverage materialises. |
| **Huge demand explosion** | Demand-Driven EPSU/EPT criterion 1. Must be genuinely structural or multi-year. High growth is AMAZING in Demand-Driven — the key is catching the inflection from low/medium to HIGH growth. Goldilocks 20-30% growth applies to other setups, NOT this one. |
| **Very large SP decline** | CfC Clearing in HQC, Trough-on-Trough, and Huge CfC Clearing all feature bottom-quartile multiples. The SP decline is raw material; setup classification determines whether the decline represents opportunity (CfC clearing, cyclical trough) or trap (false friend, structural deterioration). |

### The Three Profiles (from Pillar 2)

- **Predictable CfC clearing:** Bankable earnings + clearing catalyst + reasonable multiple → CfC Clearing in HQC and Huge CfC Clearing
- **EPT (Earnings Power Transformation):** Demand surge driving earnings transformation → Demand-Driven EPSU/EPT
- **EPSU (Earnings Power Step-Up):** Internal change/push driving earnings step-up → Corporate Change EPSU/EPT, and the cyclical variant Trough-on-Trough

---

## Entry Trigger: Which Stocks Enter the FCS?

**Trigger: 8/8+ on the Master Dashboard MM99 filter score (from `filter-results.json`).**

A stock enters the FCS queue when it scores 8 or above on the Master Dashboard's MM99 technical screening filter (11-test, 5 groups: Long-term, Mid-term, Short-term, 52W Leadership, Relative Strength). This is a necessary condition — no stock enters the FCS without it. Data source: `master-dashboard/data/filter-results.json` → `mm99.score` field per stock.

**Recency rule:** Prioritise stocks that have RECENTLY passed 8/8 (weeks, not months). Stocks that passed 12+ months ago are at elevated risk of trend exhaustion or reversal. The FCS is designed to catch inflections early, not to validate extended moves.

**Gate decision:** Richard decides which 8/8 stocks enter the FCS queue. Watson does not auto-promote stocks from IG to Triaging based on the score alone. Watson surfaces 8/8 passes to Richard; Richard decides whether to advance.

**Future:** Rules for automatic promotion may be formalised. For now, Richard's discretion is the gate.

---

## Stage-Gating: Depth of Analysis per Process Stage

**The FCS is executed at different depths depending on where the stock is in Richard's 6-stage process.** The current analysis depth is TRIAGING-level. ESA and DD require progressively more. Watson MUST know which stage is being executed — if unclear, ASK before starting.

### Depth Requirements by Stage

The 13 Case Attribute categories require different levels of analytical depth at each stage. "Light" = quick assessment from available information. "Medium" = structured analysis using multiple sources. "Robust" = comprehensive analysis using full research SOPs and primary sources.

| # | Case Attribute Category | Triaging | ESA | DD |
|---|------------------------|----------|-----|-----|
| 1 | Business foundations | light | light | robust |
| 2 | Case inputs | light | medium | robust |
| 3 | Setups — acceptable, unacceptable, false friend | light | medium | robust |
| 4 | Past trend attributes | light | robust | robust |
| 5 | Transmission mechanism | n/a | medium | robust |
| 6 | Required simplicity input attributes (guardrails) | light | robust | robust |
| 7 | Required case output attributes | light | medium | robust |
| 8 | Invalidating attributes | n/a | light | robust |
| 9 | Strenuously seek-to-avoid attributes | n/a | medium | robust |
| 10 | Small-size constraining attributes | n/a | medium | robust |
| 11 | Nice-to-have attributes | n/a | light | robust |
| 12 | Me-state attributes | n/a | light | robust |
| 13 | Fitness-for-fighting attributes | light | light | robust |

**Reference file:** `Files/Attributes_Depth_per_stage.xlsx`

### Practical Implications

**TRIAGING (current FCS default):** Categories 1-4, 6-7, 13 assessed at LIGHT depth. Categories 5, 8-12 are n/a — do not assess. Sources: Claude research, dashboard data, public filings. Adequate for setup classification and pass/fail gating.

**ESA:** All 13 categories assessed. Many at MEDIUM or ROBUST depth. This requires the RESEARCHER role to have completed the full 4-page research package (BD + CF × Claude + AlphaSense). Categories 4 and 6 jump to ROBUST — these need detailed financial history and guardrail verification that LIGHT assessment cannot provide.

**DD:** ALL categories at ROBUST depth. Full research stack required. RESEARCHER role must provide guidance/earnings research SOPs, primary source verification, management contact analysis. This is the final gate before investment.

### Resource Requirements by Stage

| Stage | Minimum RESEARCHER Input | Additional APM Resources |
|-------|-------------------------|------------------------|
| Triaging | IG outputs (BD + CF × [C] + [AS]) + Most Recent Earnings Review [C] + [AS] + GTA + GTH + Peer GTH + Sell Side (SS) Analysis + Business Model & Sector Primer + Guidance + **Master Dashboard data** (`prices.json`, `filter-results.json`, `factset-ssem.json`) | None — ad hoc analysis sufficient |
| ESA | All Triaging + History of Earnings Delivery + Tracking vs Guidance + Value Chain Analysis + Value Chain Map + Pre-mortem + CEO/CFO Questions + Technical Momentum research (all dual-source) | Financial model (basic), peer comparison |
| DD | Everything from ESA + Case Summarisation + Management/Governance Checks + CEO Research + Insider Comments + FX Exposure + any KQs (all dual-source) | Full financial model, scenario analysis, ACH |

**CRITICAL:** Before starting analysis at ANY stage, Watson must check Notion and the Dashboard for existing RESEARCHER output. If gaps exist, brief the RESEARCHER on what's needed (see PRE-ANALYSIS GATE in the Three-Role Process section below). Do not attempt ESA or DD depth on TRIAGING-level information.

**RESEARCHER SEQUENCING AT TRIAGING:** The Most Recent Earnings Review [C] and [AS] is NOT automatically produced as part of IG. Richard must brief the RESEARCHER to run it. When APM hits the PRE-ANALYSIS GATE and finds Most Recent Earnings Review missing, the correct action is to escalate to Richard — not to self-task the RESEARCHER. Richard decides when and whether to commission that work.

**APM INFORMATION INGESTION RULE:** APM-Analysis ALWAYS reads ALL available Notion pages AND source files for the stock — not a subset. The aim is maximum information ingestion to give the broadest possible analytical base for conducting Analysis, forming Judgement, and proposing Actions + 2 downstream actions (IAJ + 2DSA). At Triaging depth the assessment is LIGHT, but the reading is COMPREHENSIVE. Light depth means shorter evidence statements and fewer sources cited per attribute, not less reading.

---

## The Three-Role Process: INFORMATION → ANALYSIS → JUDGEMENT

The Fundamental Change Screen is executed across three Watson roles in sequence. Each role has a distinct responsibility and output. **Skipping or conflating these steps degrades quality.**

### Role 1: RESEARCHER — Information Gathering

**Purpose:** Provide the raw information base that Analysis and Judgement work from.
**Master reference:** `memory/skills/researcher/SKILL.md` + prompt templates in `AI Prompts/`

#### RESEARCHER Output Requirements by Stage

The RESEARCHER must produce specific outputs BEFORE APM Analysis can begin at each stage. Watson must check what exists and brief the RESEARCHER on gaps.

| Stage | Required RESEARCHER Outputs | Prompt Templates |
|-------|---------------------------|-----------------|
| **IG** | BD [C], BD [AS], CF [C], CF [AS] — **4 Notion pages per stock** | `Watson - IG - Business description - REV V03_RB.docx`, `Watson - IG - Change forces - REFV04_RB.docx` |
| **Triaging** | IG outputs (above) + Most Recent Earnings Review [C], [AS] + GTA Unknown KDs [C], [AS] + GTH Analysis [C], [AS] + Peer GTH [C], [AS] + Sell Side (SS) Analysis [C], [AS] + Business Model & Sector Primer [C], [AS] + Guidance [C], [AS] + **Master Dashboard data** (`prices.json`, `filter-results.json`, `factset-ssem.json`) | `Watson - Triaging - *.docx` prompts + BM&Sector Primer + Guidance (moved from ESA 13-Apr-26) |
| **ESA** | All Triaging outputs + History of Earnings Delivery [C], [AS] + Tracking vs Guidance [C], [AS] + Value Chain Analysis [C], [AS] + Value Chain Map [C], [AS] + Pre-mortem [C], [AS] + CEO/CFO Questions + Technical Momentum research | `Watson - ESA - *.docx` prompts (7+ types, dual-source each) |
| **DD** | All ESA outputs + Case Summarisation + Management & Governance Checks + Researching a CEO + Insider Comments + FX Exposure + any KQs briefed | `Watson - DD - *.docx` prompts (5+ types, dual-source) |

**The CF output is the primary input for setup classification.** Its 14 sections map directly to setup criteria (see Appendix A). The BD output feeds the quality assessment that gates Foundations and CfC Clearing in HQC.

#### PRE-ANALYSIS GATE — MANDATORY

**Before starting ANY attribute analysis or APM judgement, Watson MUST:**

1. **Search Notion** for all existing RESEARCHER output on the stock (search Stock Notes DB by ticker). List what exists.
2. **Check the Master Dashboard** data files (`master-dashboard/data/prices.json` + `filter-results.json`) for current MM99 scores, filter qualification stages, MA data, and RS excess returns.
3. **Compare existing output against the stage requirements table above.** Identify gaps.
4. **If gaps exist → ESCALATION PROTOCOL** (see below).
5. **Only proceed with analysis once the information base is sufficient for the declared stage.**

This is non-negotiable. Watson does not start attribute analysis on incomplete information. The quality of the analysis is bounded by the quality of the information base.

#### RESEARCHER GAP ESCALATION PROTOCOL

When Watson identifies missing RESEARCHER outputs:

**Option A — Brief and wait:** Flag the gaps to Richard, recommend briefing the RESEARCHER to run the missing SOPs. Hold analysis until output is posted.

**Option B — Brief and start:** Flag the gaps, brief the RESEARCHER, begin analysis on available information with explicit caveats on which attributes are under-supported. Re-assess affected attributes once RESEARCHER gaps are filled.

**The briefing must be specific:**
- Which stock
- Which SOP/prompt is needed (exact template name)
- Which stage this serves
- Which attributes in the FCS are blocked or under-supported without it
- Priority relative to other pipeline work

**Example gap brief:**
> "NKT ESA: Missing Guidance Analysis [C] and [AS]. Template: `Watson - ESA - Guidance - REFV05_RB.docx`. Without this, attributes 1.M4 (company delivery), 4.1 (triple ratchet), 4.9 (modal case > guidance > SS), and 4.10 (EPS raise/lower skew) cannot be assessed beyond TRIAGING depth. Recommend RESEARCHER runs this before APM proceeds to ESA-level analysis."

### Role 2: APM — Investment Case Analysis (Attributes)

**Full SOP:** `fundamental-change-screen/apm-analysis-sop.md`

**Purpose:** Assess the stock against every applicable attribute. This is ANALYSIS — factual assessment of what the stock exhibits, rated objectively.
**Input:** ALL available Notion pages + source files + **Master Dashboard data** (`prices.json`, `filter-results.json`, `factset-ssem.json`, `factset-valuation.json`) + company disclosures. APM reads EVERYTHING — light depth means shorter evidence per attribute, not less reading.
**Output:** Structured attribute assessment posted to Notion Stock Notes + entered into the Fundamental Change Analysis database.

The APM rates every applicable attribute across the 4 Pillars (excluding me-state) at the depth appropriate to the declared stage. Each attribute receives a G/Y/O/R rating with evidence.

**What Analysis IS:** "This company has a great operator — evidence: X, Y, Z." "There are strong internal change forces at layers 1-3." "The transmission mechanism from strategy to EPS is unclear." These are factual assessments grounded in evidence.
**What Analysis is NOT:** "This stock fits Setup 3." That's Judgement. Watson should be explicit about when it is analysing vs. when it is forming a judgement.

### Role 3: APM — Investment Case Judgement (Setup Classification + IAJ+2DSA)

**Full SOP:** `fundamental-change-screen/apm-judgement-sop.md`

**Purpose:** Map the attribute ratings to setup profiles. Determine which setup(s) the stock fits, how strongly, and at what maturity stage. Form a view. Propose actions.
**Input:** The attribute assessment from Analysis.
**Output:** Setup classification with checklist verdict, score, maturity stage, false friend check, recommended action, and **2+ downstream actions** (IAJ+2DSA). Posted to Notion Stock Notes + entered into database.

**Analysis and Judgement are linked but distinct skills.** If in doubt about whether a statement is analysis or judgement, Watson should label it explicitly. Analysis = evidence-based factual assessment. Judgement = forming a view by synthesising multiple analyses into a conclusion.

**What Judgement IS:** "Given these attribute ratings, the pattern matches Demand-Driven EPSU/EPT at full-output maturity." "This is a false friend — transmission mechanism from strategy to EPS is absent."
**What Judgement is NOT:** "Richard should buy this stock." That's Richard's decision.

**IAJ+2DSA:** Every Judgement output must include at least 2 concrete downstream actions. These might be: progress to next stage, park with specific reassessment criteria, run specific KQ research, build financial model for specific attributes, commission RESEARCHER for specific gap. Future: COS (Chief of Staff) role may drive these actions.

---

## The 4 Analytical Pillars and 13 Attribute Families (Pillars III and IV detail)

The TARGET INVESTMENT CRITERIA are organised in **4 PILLARS**, containing **13 ATTRIBUTE FAMILIES** with individual attributes beneath each. The pillar numbering in the ESA checklist (3, 1, 2, 4) reflects the original tab layout; the conceptual order is: Foundations → Inputs → Checks → Outputs. Pillar 5 (Fitness-for-Fighting) sits as a constraint layer across all pillars.

**Note:** These 4 analytical pillars map into the Six Pillars framework as Pillars III (Fundamental Change) and IV (Building Blocks). The attribute detail below is unchanged — only the framing and rating scale are updated.

**Analytical priority:** Assess magnitude of CHANGE (Inputs + Outputs) first. Then test PROBABILITY of that change manifesting (Foundations). Then test INVESTABILITY (Checks). See "Analytical Priority" in Architecture section.

### PILLAR I: BUSINESS — FOUNDATIONS (6 attributes)

The **probability gate**. Foundations tell you how likely the change thesis is to actually happen. A company with a great operator, widening moat, favourable value chain, and concentrated industry structure has a high probability of translating change forces into financial outputs. A company without these has a hypothesis, not a case.

| # | Attribute | Theme | What You're Assessing |
|---|-----------|-------|----------------------|
| 3.1 | Great operator? | Strong company (internal) | CEO/management quality, execution track record, commercial ambition, culture. Animal CEO = A. |
| 3.2 | Advantaged business + widening SRCA? | Strong company (internal) | Hard + soft competitive advantages. Pricing power, switching costs, network effects, moats. 1% company characteristics. |
| 3.3 | Favourable value chain dynamics? | Favourable value chain (external) | Position in value chain. Supplier/customer power balance. Value capture vs. value creation. |
| 3.4 | Supportive / concentrated industry structure? | Favourable value chain (external) | Oligopoly, barriers to entry, rational competitive behaviour, limited new entrants. |
| 3.5 | High secular / long-term growth potential? | Growth | Structural tailwinds (5%+ minimum). Multi-year demand drivers. S-curve positioning. |
| 3.6 | Fit with stock market paradigm / regime / thematics? | Stock market fit | Alignment with current market themes, risk regime, sector rotation. |

**FOUNDATIONS SOPs — CRITICAL REFERENCE:**

Section 3 attributes MUST be assessed using Richard's Notion Journal SOPs. These are the canonical check-do lists that define what "great operator", "advantaged business", etc. actually mean in Richard's system. Watson must read and internalise these SOPs before assessing Foundations at ANY stage.

| Attribute | Notion Journal SOP | Page ID |
|-----------|-------------------|---------|
| 3.1 Great operator? | **Investing SOP: 'Check-do' lists for 'great operator/allocator'** | `2d235e90-9b0b-80be-a5b1-f4edbe29aa50` |
| 3.2 Advantaged business + SRCA? | **Investing SOP: 'Check-do' list for "Advantaged business + widening moats"** | `2c635e90-9b0b-80ac-ae6b-f1b6e6bc6c4a` |
| 3.3 Value chain dynamics? | **Investing SOP: 10x 'supportive value chain dynamics' check-do list** | `2d235e90-9b0b-808c-97c4-fc1c5cec9e53` |
| 3.4 Industry structure? | **Investing SOP: 'Check-do' list for 'supportive industry structure'** | `2d235e90-9b0b-801c-83a7-ec4a5e844feb` |
| (Meta-reference) | **Investing SOP: Check-pick refer-to list for assessing business/industry quality** | `2e635e90-9b0b-8084-ba7a-fb9572bdc238` |

**Loading protocol:** Before any FCS execution, fetch and read the relevant SOPs from Notion. For TRIAGING, a light pass against these frameworks is sufficient. For ESA/DD, the assessment must systematically address the SOP checkpoints and cite specific evidence against each.

### PILLAR II: CASE — INPUTS (Change Forces + Momentum + Setup Classification)

**Change forces (the core of the screen):**

| # | Attribute | Theme | What You're Assessing |
|---|-----------|-------|----------------------|
| 1.1 | External change forces / tailwinds? | Sufficient change forces (PUSHING) | Demand shifts, regulatory changes, policy support, technological disruption benefiting the company. |
| 1.2 | Internal change forces? | Sufficient change forces (PUSHING) | CEO change, strategy shift, restructuring, M&A, operational improvement. Assessed via the 6-layer framework for Setup 3. |
| 1.3 | Absence of external headwinds? | Sufficient base | No material headwinds undermining the thesis. Or headwinds identified and manageable. |
| 1.3b | Well-invested base? | Sufficient base | Company has the operational/financial foundation to execute on the change thesis. |
| 1.4 | Thesis congruency with past/present? | Sufficient base | Does the change thesis flow logically from observable evidence? Does it make sense given the company's history? |
| 1.5 | Large CfC/mispricing? | Mispricing | Is there a CfC creating a discount (REMOVAL setups)? Or a growth mispricing (PUSHING setups)? |
| 1.6 | Low trading multiple? | Mispricing | Is valuation attractive on forward normalised earnings? |

**Momentum / GTH attributes (past trend constraints):**

| # | Attribute | Theme | What You're Assessing |
|---|-----------|-------|----------------------|
| 1.M1 | Technicals — relative, absolute (MAs, etc.) | Price momentum | Minervini score, MA relationships, RS direction, excess returns. |
| 1.M2 | SS — estimates, ratings, PTs, narrative | Fundamental momentum | Estimate revision direction, rating changes, target price moves, narrative shift. |
| 1.M3 | Peers — technicals, SS | Peer momentum | Are peers confirming or diverging from the stock's momentum pattern? |
| 1.M4 | Company — delivery | Delivery momentum | Is the company meeting/beating expectations? Guidance trajectory? |

**GTH Sourcing by Stage:**

| Stage | Peer technicals (M1, M3) | Company delivery (M4) |
|-------|--------------------------|----------------------|
| **Triaging** | Base on **Master Dashboard MM99 scores, filter qualification stages, and RS excess returns from `filter-results.json`** only. No additional research required. | Acceptable at LIGHT depth from public filings and recent results. |
| **ESA / DD** | Master Dashboard data AND run the **RESEARCHER Query #3 (Technical Momentum) SOP** for qualitative depth (stage analysis, base formation, volume patterns, pullback health). | Base on **Guidance and Earnings Research SOPs** + Master Dashboard `factset-ssem.json` as supplementary context. If RESEARCHER queries have not been run and posted, escalate to RESEARCHER role first. |

**Setup classification:** Output of Judgement step (see Setup sections below).

### PILLAR III: CASE — CHECKS (Simplicity Guardrails + Transmission Mechanism)

These are gatekeepers — they test whether the case is INVESTABLE, not whether it's attractive.

**COMPLEXITY GATEKEEPER — WATSON'S ACTIVE ROLE:** Richard has a tendency to let too many cases through on Checks. Watson's responsibility in APM is to be the disciplined enforcer here. When a stock has 3+ CfCs, a sprawling perimeter, unclear transmission mechanism, or too many drivers — Watson should flag this as a hard problem in a neutral but challenging tone, and recommend parking or downgrading conviction. Do not accommodate complexity with generous Y-ratings. If ≥2 of the 7 guardrails fail, Watson should actively recommend parking or requiring significant additional evidence before progressing, regardless of how strong the other pillars look. Richard decides, but Watson's job is to surface the complexity risk prominently.

| # | Attribute | Theme | What You're Assessing |
|---|-----------|-------|----------------------|
| 2.1 | 2 or less fulcrum drivers and 4 or less key drivers? | Narrowly focused bet | Is the case simple enough to track and invalidate? |
| 2.2 | 10 or less geographies × business units? | Narrow perimeter | Is the business simple enough to understand thoroughly? |
| 2.3 | Zero value chain headwinds to revenue? | No headwinds | Are there material value chain obstacles to revenue growth? |
| 2.4 | 2 or less CfCs or problems? | Narrow range of issues | Pret sandwich risk check — too many CfCs = fatal regardless of individual severity. |
| 2.5 | Company confirms conservative guidance? | Conservative IR | Is guidance set at a level that creates conditions for beats? |
| 2.6 | Clear strategy-to-EPS transmission mechanism? | Clear investment case | Can you trace strategy → actions → financial outputs → EPS? **If not = false friend.** |
| 2.7 | Clear VC/Co inputs-to-EPS transmission mechanism? | Trackable case drivers | Can you trace value chain/company inputs → leading indicators → EPS quarter by quarter? |

### PILLAR IV: CASE — OUTPUTS (Financial Profile + Navigatability)

**THE MOST IMPORTANT ATTRIBUTE FAMILY.** The Required Case Output Attributes (12 attributes below) are the attributes that most directly drive the stock price. They are the financial translation of the change thesis into investable reality. These should be assessed at EVERY stage from Triaging onwards — they are not deferred to ESA.

**Financial output attributes:**

| # | Attribute | Theme | What You're Assessing |
|---|-----------|-------|----------------------|
| 4.1 | Three-year, mid-term, triple ratchet step-up? | Longevity of case | Is the earnings improvement multi-year and self-reinforcing? |
| 4.2 | 12-20% EPS growth p.a.? | Growth rate | Is growth in the sweet spot for other setups? (Note: for Setup 2, high growth above 20% is POSITIVE — see Setup 2 section.) |
| 4.3 | Margin/growth step-up? | Financial improvement | Is there visible margin expansion or revenue acceleration? |
| 4.4 | Fit with required setups? | Setup fit | Does the case match an acceptable setup profile? |
| 4.5 | Post CfC clearing / SP turn? | Timeliness | Is the CfC clearing and/or SP turning? |
| 4.6 | Less than 6M after turn? | Timeliness | Is entry within the 0-6M window of the turn? |
| 4.7 | Helpful IR re. operating momentum? | Navigatability | Will investor relations provide useful intra-quarter data? |
| 4.8 | Trackable key leading indicators? | Navigatability | Can key drivers be monitored fortnightly? |
| 4.9 | Modal case 18M EPS > guidance > SS? | Earnings upgrades | Is the modal case above both guidance and SS consensus? |
| 4.10 | 3:1 SS/G EPS raise/lower skew NFY? | Earnings upgrades | Is the estimate revision skew strongly positive? |
| 4.11 | Multiple more company than exogenously driven? | Limited drawdown risk | Is the valuation supported by company fundamentals, not sector/macro? |
| 4.12 | More than 20% 3Y TSR? | Returns | Does the case deliver sufficient total shareholder return? |

**Stage-specific notes on Output Attributes:**
- **4.9 (Modal case > guidance > SS):** Requires a financial model to answer with conviction. At Triaging, assess directionally — if the company is known for conservative guidance and IR actively anchors SS estimates low to create room for beat-and-raise (e.g. Helios Towers pattern), and if available analysis shows SS estimates sit at the low end of guidance, a directional judgement is possible. At ESA/DD, requires the actual Excel model.
- **4.10 (3:1 raise/lower skew):** Requires DD-level judgement for high conviction. At Triaging/ESA, assess from available SS data — estimate revision direction, breadth of upgrades/downgrades, and whether the pattern is consistent with beat-and-raise dynamics.
- **4.12 (>20% 3Y TSR):** At Triaging, a rough TSR estimate from current multiple, consensus EPS trajectory, and normalised exit multiple. At ESA, modelled in Excel.

**Me-state attributes (Richard only — APM does NOT rate these):**

| # | Attribute | What Richard Assesses |
|---|-----------|----------------------|
| 4.MS1 | Believe in 'IT, NT and MT' | Conviction across all timeframes |
| 4.MS2 | Very understandable + clear + predictable | Fingertip feel |
| 4.MS3 | Excited | Emotional engagement with the case |
| 4.MS4 | Feel comfortable | Sense of control |
| 4.MS5 | "Sit three steps ahead"-able | Anticipation of market moves |
| 4.MS6 | Faster OODA loop speed than the SP | Information processing advantage |
| 4.MS7 | Erosion spottable early | Deterioration detection confidence |
| 4.MS8 | ACH-able | Can compete hypothesis profiles |
| 4.MS9 | Crisply trackable KDs (Enav) | vs. fuzzily trackable KDs (HBX) |
| 4.MS10 | Updateable [new info] | Can incorporate new information |
| 4.MS11 | Hold-all-in-head-able | Cognitive manageability |
| 4.MS12 | Granularly extrapolatable from qualitative to EPS | vs. noisy/blackbox extrapolation |
| 4.MS13 | Easily defined and clear invalidation thresholds | vs. vague invalidation |

### PILLAR IV (continued): CONSTRAINT FAMILIES — ESA onwards

**The following attribute families sit under Pillar IV but are NOT assessed at Triaging.** They come in at ESA (light or medium depth) and DD (robust). The Required Case Output Attributes above ARE assessed at Triaging. This split is deliberate: at Triaging, you focus on whether the case OUTPUTS are compelling. At ESA, you additionally check whether they survive the constraint filters.

### FITNESS-FOR-FIGHTING CONSTRAINTS (Family 13)

**Environmental constraints:**

| # | Attribute | What You're Assessing |
|---|-----------|----------------------|
| 5.1 | Market cycle — downturn | Does current macro regime support or undermine the case? |
| 5.2 | AI disruption | Is the business exposed to AI disruption risk? |
| 5.3 | Input cost inflation (geopolitical) | Is the business exposed to input cost spikes? |
| 5.4 | No overlap with 10x general invalidating ACHs | Does the case survive the general invalidation checklist? |

**Invalidating constraints (any "yes" = serious concern):**

| # | Attribute | What You're Assessing |
|---|-----------|----------------------|
| 5.I1 | No slowing of core engine vs. company's DNA | Is the core business momentum intact? |
| 5.I2 | No mediocre CEOs or weird, silly simple choices? | Management quality check |
| 5.I3 | No big 'Hmmms'? | Gut-level discomfort check |
| 5.I4 | No to red flags/achilles heel = 2+ "F"s? | Red flag count |
| 5.I5 | No to mediocrity = 8+ "D"s? | Weak flag count (too many weak = mediocre) |
| 5.I6 | No recent earnings cuts (unless CfC part of case)? | Earnings trajectory |
| 5.I7 | No peers having problems? | Sector health |
| 5.I8 | No overlap with negative lessons and setups? | Track record pattern check |
| 5.I9 | No fit with unacceptable / false friend setups? | Setup disqualification |

**Strenuously seek-to-avoid constraints:**

| # | Attribute | What You're Assessing |
|---|-----------|----------------------|
| 5.A1 | Fundamental SHMLP risks? | Avoiding invalidation at trough SP |
| 5.A2 | Wide skew in outcomes (low case predictability)? | Case predictability |
| 5.A3 | Large downside to trough multiple? | Mark-to-market risk |
| 5.A4 | Multiple more influenced by industry than company? | Valuation independence |

---

## Stable Serial Acquirer (Mis-Modelled High Quality EPS Upgrader)

**STATUS: DEFERRED.** To be designed and added in a future session. Placeholder only.

**Market error:** Modelling error — consensus fails to properly model the compounding effect of serial M&A in a VMS/platform acquirer with disciplined capital allocation.

---

## Demand-Driven EPSU or EPT

### The Thesis

A structural or sustained cyclical demand explosion is underway at the sector or market level. The company is positioned — through competitive dominance, scalable business model, and operating leverage — to translate that demand into a non-linear earnings step-up or transformation that the market is not modelling.

### Market Error Exploited

**Analytical error: future ≠ past.** The sell-side models historical demand run-rates and applies modest growth assumptions. They fail to model the S-curve inflection in demand. The buy-side anchors to historical multiples appropriate for the old growth profile. Both miss the operating leverage: fixed cost base means revenue growth flows disproportionately to EBIT and EPS.

### Growth Rate Calibration — SPECIFIC TO SETUP 2

**High growth is AMAZING in Setup 2.** Unlike other setups where Goldilocks growth of 20-30% is the sweet spot, Setup 2 actively seeks the moment when growth INFLECTS from low/medium to HIGH. Catching this inflection — from 5-10% historical growth to 30%+ or even 50%+ — is the entire point of the setup. The demand explosion IS the high growth.

The critical discipline is not avoiding high growth but avoiding OVER-EXTRAPOLATION: most demand pulses totally reverse to trend. The edge is capturing the high-growth phase while it lasts, sizing appropriately, and not projecting it into perpetuity. Assume the demand explosion is 100% cyclical/temporary until proven structural. The burden of proof is on the bull case.

**Goldilocks 20-30% growth applies to other setups (3, 4, 5, 6)** where the case is about normalised earnings improvement, not demand-driven transformation.

### The 5 Criteria

| # | Criterion | What You're Looking For | Red Flags |
|---|-----------|------------------------|-----------|
| **1** | **Market-wide demand explosion?** | A sector/market-level demand surge — NOT company-specific outperformance. Must be structural (multi-year secular shift) or a cyclical upswing with 2+ years of visibility. Evidence: industry data showing significant growth acceleration, order book expansion across the sector, capex announcements by customers, government policy/stimulus driving adoption. | Company-specific one-off wins. Covid-style temporary demand spikes. Demand driven purely by channel stuffing or pull-forward. |
| **2** | **Dominant competitive position?** | Top 1-3 market share position in the segment benefiting from demand. Evidence the company captures DISPROPORTIONATE demand vs. competitors. Ideally: 1% company characteristics (hard + soft SRCA). Pricing power demonstrated in the market. | Fragmented market with no clear leader. Company growing but losing relative share. Market share achieved through price concessions. |
| **3** | **One-to-many scalability (Avanza not Theon)?** | Revenue growth requires MINIMAL incremental resource. Platform economics: each new customer/transaction generates revenue with near-zero marginal cost. Software, marketplaces, subscription models, regulatory monopolies, toll-road/infrastructure concessions. | Project-based model where revenue = headcount × utilisation (Theon archetype). Revenue growth requiring proportional capex, inventory build, or hiring. |
| **4** | **Oligopoly (structure AND behaviour)?** | Industry structure concentrated AND competitive behaviour rational. Stable or rising ASPs, limited new entrants, high barriers to entry. Monopoly or near-monopoly structures score highest. | Many competitors (>10 material players). History of price wars. Low barriers to entry. Commodity-like product. |
| **5** | **Fixed cost leverage (margin expansion)?** | High proportion of fixed costs means revenue growth → disproportionate margin expansion. Evidence: historical proof of margin expansion in prior upturn, or underutilised capacity ready to absorb demand. | Predominantly variable cost structure. Cost inflation eating margins. Company investing in growth that ADDS costs before revenue materialises. |

### Decision Logic

**Checklist mode (pass/fail):**
- **Mandatory:** Criterion 1 must be A or B. Without a genuine demand explosion, there is no Setup 2 thesis.
- **Threshold:** ≥ 3 of 5 criteria must be A or B.
- **Pass =** A or B on #1 AND ≥ 3 of 5 total A or B.

**Scored mode (0-15):**
- Each criterion rated: A = 5, B = 4, C = 3, D = 2, F = 1, Blank = 0.
- **Strong (≥ 12):** Highly likely demand-driven EPSU/EPT. Prioritise.
- **Possible (9-11):** Credible but incomplete evidence. Needs more data.
- **Fail (< 9):** Demand thesis does not hold. Park or reclassify.

### Worked Example: Getlink (GET-FR) — Setup 2 Assessment

[Note: In worked examples below, historical ratings use the old G/Y/O/R scale. New analysis uses A-F. Mapping: G→B, Y→C, O→D, R→F, with A reserved for top-decile exceptional cases.]

**Context:** Getlink operates the Channel Tunnel (monopoly concession to 2086). High-speed cross-Channel rail passengers expected to grow from 12M to 22M over the next decade as new operators (Virgin, Trenitalia, Evolyn, Gemini) enter the market. EU rail liberalisation and carbon policy create structural tailwinds.

| # | Criterion | Rating | Evidence |
|---|-----------|--------|----------|
| 1 | Market-wide demand explosion? | **G** | Sector-level: 4 new operators submitted ORR applications. Passenger growth 12M→22M structural (new routes to Germany, Switzerland, Bordeaux). EU rail liberalisation + carbon modal shift. Not company-specific. |
| 2 | Dominant competitive position? | **G** | Natural monopoly — no competing fixed link between UK and continent. Benefits from ALL operators' growth via access charges. |
| 3 | One-to-many (Avanza not Theon)? | **G** | Classic toll-road economics. Tunnel is built. Each additional train = access charges at near-zero marginal cost. Pure platform leverage. |
| 4 | Oligopoly (structure, behaviour)? | **G** | Better than oligopoly: natural monopoly. No fixed-link competitors. Substitute competition (ferries, flights) structurally disadvantaged. |
| 5 | Fixed cost leverage (margin up)? | **G** | Tunnel maintenance largely fixed. Eurotunnel EBITDA margin ~56% and expanding. Incremental trains flow through at very high incremental margin. |

**Checklist: PASS** (G on #1, 5 of 5 G). **Score: 15/15 — Strong.**

The demand thesis is structural, the competitive position is a monopoly, and the economics are pure platform leverage. The Getlink case is an unusually clean Setup 2. The key uncertainty is TIMING — when do new operators actually start running trains and contributing to Getlink's revenue? (2027-2028 most likely.)

---

## Corporate Change-Driven EPSU or EPT

### The Thesis

A material change in corporate leadership, strategy, structure, or ambition is driving an earnings step-up or transformation. The market anchors to the company's historical earnings profile and fails to model the impact of the change programme.

### Market Error Exploited

**Analytical error: future ≠ past.** The sell-side models historical margin structures and growth rates. When change INPUTS are visible (new CEO, new strategy) but change OUTPUTS have not yet appeared in the financials, the market's backward-looking models systematically underestimate the pace and magnitude of improvement.

### The 6-Layer Input/Output Framework

Setup 3 assessment requires understanding the distinction between INPUTS and OUTPUTS of corporate change. This is critical: inputs are leading indicators that predict output changes. A stock can be classified as Setup 3 at different maturity stages depending on how far down the 6 layers the change has propagated.

**INPUT LAYERS (leading, qualitative, screenable by RESEARCHER):**

| Layer | Category | What It Contains | Examples |
|-------|----------|-----------------|----------|
| **1. RESOURCES** | People/assets that make choices | CEO change, CFO change, board refresh, key hires, management team overhaul. These are the "actors" who drive change. | New CEO appointed. New CFO from cost-cutting background. Board refreshed with industry experts. |
| **2. STRATEGIC CHOICES** | Direction, goals, perimeter decisions | Strategy change, new targets, guidance level, market perimeter, priorities, ambition level. These are the DECISIONS the resources make. | New €1bn EBITDA target set at CMD. Strategy pivoted from product to platform. Guidance raised. Exited 3 non-core markets. |
| **3. STRATEGIC ACTIONS** | Execution of those choices | Product launches, market exits, restructuring, M&A execution, cost programmes, capex allocation, hiring/firing. These are the THINGS DONE based on the choices. | Launched new product line. Completed bolt-on acquisition. Downsized workforce by 15%. Initiated $500M buyback. |

**OUTPUT LAYERS (lagging, financial, require analysis):**

| Layer | Category | What It Contains | Examples |
|-------|----------|-----------------|----------|
| **4. KFM (Key Financial Metrics)** | Company-specific operational KPIs | ARPU, NRR, ARR, order book, utilisation, win rates, churn rates, cost-per-unit, headcount per unit — the metrics that prove inputs are translating. | ARPU up 8% YoY. Order book at record levels. Customer churn rate falling. Cost-per-unit down 12%. |
| **5. FSO (Financial Statement Outputs)** | Standard financial statement items | Revenue growth, margins, EPS growth, ROIC, cash conversion, working capital efficiency — the P&L/B-S/CF evidence visible in reported accounts. | Revenue growth accelerated from 5% to 15%. EBIT margin expanded 200bps. FCF conversion improved to 90%. |
| **6. SS ESTIMATES** | Sell-side consensus changes | Revision direction and magnitude for EPS, EBITDA, revenue. Target price changes. Rating upgrades. The market's catch-up to the change story. | FY2 EPS revised up 8% in L3M. 3 analysts upgraded to Buy. Average PT raised 15%. |

### How to Read the 6 Layers

The layers form a **transmission chain**: Resources (layer 1) → make Strategic Choices (layer 2) → execute Strategic Actions (layer 3) → which change KFMs (layer 4) → which flow into FSOs (layer 5) → which the sell-side eventually models (layer 6).

**The key insight:** Inputs are NOT always clearly "telegraphed" into outputs. A company might appoint a CEO with a cost-cutting record (layer 1 input) without yet announcing cost cuts (layer 3 action) or showing margin improvement (layer 5 output). But the PROBABILITY of cost cuts → higher margins → higher EPS is high. The market, anchored to current financials, fails to model this forward chain. That's the analytical error Setup 3 exploits.

**Setup maturity = how far down the 6 layers the change has propagated:**

| Maturity Stage | Layers Visible | Example | Conviction Level |
|----------------|---------------|---------|-----------------|
| **Input-only** | Layers 1-2 (maybe early 3) | SMWH: New CEO with superb operational track record. No new guidance yet. No output evidence. | Lower — thesis is probabilistic. Size small (UHPYHQI 0-5%). |
| **Input + Early Output** | Layers 1-4 | New CEO has set targets (layer 2), initiated restructuring (layer 3), KFMs starting to improve (layer 4). FSOs not yet visible. | Medium — transmission chain working. Size building. |
| **Full Output** | All 6 layers | Inputs visible, KFMs improving, financial statements showing margin/EPS improvement, SS upgrading estimates. | High — full conviction. Size to core position. |

**Ideally, a strong Setup 3 case has BOTH inputs AND outputs clearly communicated** by the company, sell-side, or primary research. But the screen must also identify stocks at the Input-only stage — these are EARLIER in the lifecycle, higher uncertainty but potentially higher reward (catching the opportunity before the market).

### Input Assessment Criteria

| # | Input Criterion | Layer | What You're Looking For | Red Flags |
|---|----------------|-------|------------------------|-----------|
| **I1** | **CEO change?** | 1-RESOURCES | New CEO appointed. Strongest single signal of corporate change. First 12-18 months = highest probability period for earnings power transformation. Animal CEO (Slootman archetype) = maximum conviction. | Internal promotion signalling continuity. Crisis-forced change without succession plan. No relevant industry experience. Caretaker/transition figure. |
| **I2** | **Other leadership/actor changes?** | 1-RESOURCES | New CFO, COO, board members, division heads. New CFO often signals financial discipline change. Activist investor involvement can catalyse change. | Revolving door (dysfunction). Crisis-driven changes. Cost-cutter CFO without growth vision. |
| **I3** | **Strategy/strategic priorities change?** | 2-CHOICES | Material shift in direction, markets, products. New end-markets targeted. Geographic expansion. Digital transformation. Strategy articulated clearly AND backed by resource allocation. | "PowerPoint transformation" — strategy announced but no resources allocated. Frequent pivots. New strategy cannibalises existing business without clear net benefit. |
| **I4** | **Financial guidance increase?** | 2-CHOICES | Raised guidance, MT targets, financial ambitions. New CMD with higher targets. Upgraded margin/growth guidance. Puts management credibility on the line. | Trivial increase (1-2% EPS). Driven by one-off tailwind. History of raising then cutting. "Aspirational" without milestones. |
| **I5** | **Standards improvement?** | 2-CHOICES / 3-ACTIONS | Execution standards improving. Operational KPIs trending up. Governance upgrades. Cost discipline. Quality metrics strengthening. | Cosmetic changes. KPI improvement from one-off. Standards up but no financial translation within 2-3 quarters. |
| **I6** | **Perimeter/composition reduction?** | 3-ACTIONS | Divesting non-core assets. Simplifying portfolio. Exiting low-ROIC businesses. Improving revenue quality and margin mix. | Divesting to survive. Selling crown jewels. Removing diversification in a cyclical business. |
| **I7** | **Strategically-sensible M&A step-up?** | 3-ACTIONS | M&A accelerating AND strategically coherent. Fills capability gaps, expands addressable market, consolidates fragments. Disciplined integration with post-deal ROIC meeting targets. | Empire-building. Pace outstrips integration capacity. Excessive multiples. M&A papering over organic weakness. |
| **I8** | **B/S utilisation increase?** | 3-ACTIONS | Balance sheet used more aggressively. Leverage for strategic M&A. Working capital efficiency improvements. Asset monetisation. | Dangerous leverage levels. Supplier stretch disguised as WC improvement. Asset stripping. |
| **I9** | **Shareholder returns increase?** | 3-ACTIONS | Buyback initiation/step-up. Special dividend. Progressive dividend policy. Higher payout ratio. Signals management views stock as undervalued. | Buyback funded by debt. Buyback at stretched valuation. Unsustainable dividend increase. |

### Output Assessment Criteria

| # | Output Criterion | Layer | What You're Looking For | Red Flags |
|---|-----------------|-------|------------------------|-----------|
| **O1** | **KFM improvement visible?** | 4-KFM | Company-specific operational KPIs trending in right direction. ARPU, NRR, order book, utilisation, cost metrics, win rates — the leading evidence that inputs are translating. | KFMs flat or deteriorating despite input changes (inputs not working). KFM improvement from one-off or seasonal. |
| **O2** | **Revenue growth step-up?** | 5-FSO | Revenue growth rate accelerating vs. prior periods. New products/markets contributing visibly. Organic growth improving (not just M&A). | Revenue growth but margin-dilutive (buying growth). FX-driven. Channel stuffing. |
| **O3** | **Margin/EPS step-up?** | 5-FSO | EBIT/EBITDA margins expanding. EPS growth rate accelerating. Operating leverage materialising. One-off costs rolling off. | Margin improvement from cost cuts only (no revenue growth = unsustainable). Margin expansion at expense of investment (starving the business). |
| **O4** | **FCF / balance sheet improvement?** | 5-FSO | Free cash flow improving. Working capital efficiency. Debt reduction. Cash generation supporting the change thesis. | FCF decline despite reported EPS growth (earnings quality issue). Working capital deterioration. |
| **O5** | **SS estimate revisions upward?** | 6-SS | Consensus EPS/EBITDA/revenue revised upward. Target prices raised. Ratings upgraded. The market catching up. | SS upgrading but stock price not responding (already priced?). Only 1-2 analysts upgrading (not broad-based). |

### Decision Logic

**Checklist mode (pass/fail) — INPUT side:**
- **Minimum:** ≥ 3 of 9 input criteria rated G.
- **Automatic pass (override):** CEO change (I1) G + guidance increase (I4) G. New leader raising ambitions = highest conviction variant.

**Checklist mode — OUTPUT side:**
- **Input-only stage:** 0 output G acceptable — stock is classified as Setup 3 (early stage), sized as UHPYHQI (0-5%).
- **Input + Early Output:** ≥ 1 of 5 output criteria G. Conviction building.
- **Full Output:** ≥ 3 of 5 output criteria G. Full conviction, core sizing.

**Scored mode (0-42):**
- 9 input criteria × G=3/Y=2/U=1/Blank=0 = max 27
- 5 output criteria × G=3/Y=2/U=1/Blank=0 = max 15
- Total maximum: 42
- **Strong (≥ 28):** Multi-dimensional corporate transformation with financial evidence. High priority.
- **Possible (18-27):** Partial change story. May be early stage (strong inputs, weak outputs) or broad but shallow.
- **Fail (< 18):** Insufficient evidence of corporate change.

### Worked Example: Getlink (GET-FR) — Setup 3 Assessment

| # | Input Criterion | Rating | Evidence |
|---|----------------|--------|----------|
| I1 | CEO change? | **U** | No. Leriche appointed 2020 (6 years ago). |
| I2 | Other leadership changes? | **U** | No material changes. Stable team. |
| I3 | Strategy change? | **Y** | Feb-26 CMD: proactive operator recruitment, new routes targeted, AI/data strategy. Acceleration of existing strategy, not a pivot. |
| I4 | Guidance increase? | **Y** | €1bn EBITDA by 2030 target is ambitious vs. €859M in 2025. But 2026 guidance €820-860M is flat. MT ambition up, NT cautious. |
| I5 | Standards improvement? | **Y** | AI/data operational optimisation. Improved Eurotunnel availability. Gradual, not transformational. |
| I6 | Perimeter reduction? | **U** | No. Actually diversifying (Eleclink, Europorte, Customs Services). |
| I7 | M&A step-up? | **U** | No M&A activity. Organic strategy. |
| I8 | B/S utilisation? | **Y** | Net debt reduced €184M. Cash €1.5bn. Deleveraging, not leveraging up. |
| I9 | Shareholder returns? | **G** | New progressive dividend: €0.80 (from €0.58) with +€0.05/yr to €1.00 by 2030. Material step-up. |

| # | Output Criterion | Rating | Evidence |
|---|-----------------|--------|----------|
| O1 | KFM improvement? | **Y** | Eurostar record 20M passengers. Shuttle traffic solid. Eleclink 94% availability. New operators not yet in traffic data. |
| O2 | Revenue growth? | **U** | Group revenue -1% (Eleclink drag). Eurotunnel +4%. Modest. |
| O3 | Margin/EPS step-up? | **Y** | EBITDA +4% above guidance. Eurotunnel EBITDA margin ~56%. Improving but not inflecting. |
| O4 | FCF/balance sheet? | **Y** | FCF €374M. Net debt down €184M. Solid but not transformational. |
| O5 | SS estimates up? | **U** | Mixed consensus: 8 buy, 6 hold, 2 sell. Avg PT €18 below current ~€20. SS not catching up. |

**Checklist: FAIL** — Only 1 input G (I9). Need 3, or I1+I4 auto-pass. Neither met.
**Score: 19/42** — Possible range (barely), but driven by Y-ratings not G-ratings. Inputs: G=3 + 4×Y(=8) + 4×U(=4) = 15. Outputs: 0×G + 3×Y(=6) + 2×U(=2) = 8. Total = 23. [Correction from trial run: more accurate scoring with the expanded criteria.]

**Verdict: Does not qualify as standalone Setup 3.** Corporate change elements are real but insufficient — they are supporting factors to the Setup 2 demand thesis, not a corporate transformation in their own right.

---

## CfC Clearing in High Quality Compounder (HQC)

### The Thesis

A high-quality compounding business is trading at a discount because of a specific, identifiable Cause for Concern. The CfC is clearing or will clear within 6-12 months. The market's emotional/myopic overweighting of the CfC has created a buying opportunity in a business whose underlying quality is intact.

**CfC + CLEARING is the operative concept.** A CfC alone is just a problem. The setup only exists when there is credible evidence of CLEARING.

### Quality Gate (PREREQUISITE)

**Before assessing any CfC, the business must pass the quality gate.** Setup 4 ONLY works in high-quality compounders. In medium-quality businesses, the same CfC dynamics are classified under Setup 6 (with much stricter requirements).

Quality gate evidence: BD quality average ≥ B, demonstrable hard + soft SRCA, historical compounding through prior downturns, top 1-3 competitive position.

If the quality gate fails → reclassify to Setup 6 if CfC is large enough, or park.

### The 8 CfC Sub-Types

| # | CfC Sub-Type | What It Looks Like | What "CLEARING" Means | Typical Timeline |
|---|--------------|-------------------|----------------------|-----------------|
| **1** | **Internal — No CEO** | CEO departed. Uncertainty about direction. | Credible successor appointed (ideally Animal CEO). Market begins pricing new vision. | 3-9 months |
| **2** | **Internal — Strategy vacuum** | No clear strategic direction. Previous strategy exhausted. | New strategy articulated, backed by resources, showing early proof points. | 6-12 months |
| **3** | **Internal — Investment phase** | NT financials depressed by deliberate investment (capex, R&D, expansion). Margins compressed. Company doing the RIGHT THING but market punishing NT financials. | Investment phase completing. New products gaining traction, new markets generating revenue, capex peaking, one-off costs rolling off. MT financials inflecting upward. | 12-24 months |
| **4** | **Internal — Guidance for MT?** | MT guidance unclear/withdrawn. Market discounting for uncertainty. | Guidance set/reinstated/raised. CMD with MT financial targets. The ACT of providing guidance reduces uncertainty premium. | 3-6 months |
| **5** | **Internal — Company mis-execution** | Product failures, operational stumbles, project delays. Creates guidance delivery risk AND cockroach/weirder risk. | Demonstrable execution improvement over 2+ consecutive quarters. No further surprises. Root cause identified and addressed. **Highest risk sub-type — clearing takes longest and false clearings most common.** | 6-12+ months |
| **6** | **External — Market demand ↓** | Sector-level demand weakness. Not company-specific. | Demand stabilisation: leading indicators turning, destocking complete, comparable companies reporting stabilisation. Stabilisation IS clearing — don't need recovery. | 6-18 months |
| **7** | **External — Competition ↓** | ATM pricing pressure from competitors. SRCA risk. | Competitive behaviour calming: pricing stabilising, irrational competitors retrenching/exiting, industry consolidating. | 6-12 months |
| **8** | **External — Disruption to EGP** | Long-term disruption risk to earnings growth profile and investment-base-case bankability. Most existential CfC category. | Disruption thesis disproved with evidence OR company demonstrating successful pivot/adaptation. Requires STRUCTURAL conviction, not just "disruption won't happen." | 12-36 months |

### Decision Logic

**Checklist mode:**
- Quality gate: MUST pass.
- ≥ 1 identifiable CfC from the 8 sub-types.
- Credible evidence the CfC is CLEARING or will clear within 6-12 months.
- **Pass =** Quality gate + ≥ 1 CfC + clearing evidence.

**Scored mode (per CfC sub-type, 0-6):**
- CfC severity (how depressed): Bottom quartile = 3, second quartile = 2, above median = 1
- Clearing evidence: Clear = 3, Emerging = 2, Speculative = 1, None = 0
- **Strong (≥ 5):** Deep discount + strong clearing. **Possible (3-4):** Moderate. **Fail (< 3).**

### Key Pitfalls

- **"Pret sandwich risk"** — >2 simultaneous CfCs = escalate caution materially (Sdiptech lesson)
- **Sub-type 5 cockroach risk** — management lies to themselves before lying to market. Wait for 2+ quarters of demonstrable improvement.
- **Sub-type 8 requires structural conviction** — "disruption won't happen" is NOT a clearing thesis
- **Quality gate is NON-NEGOTIABLE** — medium quality + CfC clearing = Setup 6, not Setup 4 (Nexi lesson)

---

## Trough-on-Trough Turn in Quality Cyclical

### The Thesis

A quality cyclical business has experienced a prolonged downturn (18M+). Operating conditions are stabilising: demand troughing, competitive behaviour calming, costs restructured, estimates rebased, guidance kitchen-sinked. The market, anchored to the downturn narrative, is failing to model the coming recovery.

### The 9 Criteria

| # | Criterion | What You're Looking For | Gate? |
|---|-----------|------------------------|-------|
| **1** | **Bottom quartile trading multiple (2YF normalised margins)?** | Stock at bottom 25% of its own 10-year P/E range on normalised margins. | **MANDATORY** |
| **2** | **End market demand decreased for 18M+?** | Sustained demand decline — long enough to reset expectations. | |
| **3** | **Competitive behaviour calmed?** | Competitors stopped price-cutting for volume. Rational behaviour returning. | |
| **4** | **New contract pricing levels now stable?** | Forward-looking pricing stabilised. Leading indicator. | |
| **5** | **Company has executed right-sizing for L6M+?** | Cost restructuring underway ≥ 6 months. Benefits flowing. | |
| **6** | **Competitors/substitutes retrenched for L6M+?** | Industry-wide capacity reduction. Supply discipline returning. | |
| **7** | **SS estimates cut deeply/fully across all analysts?** | Consensus comprehensively rebased to conservative levels. Creates conditions for positive surprise. | **MANDATORY** |
| **8** | **Company guidance rebased lower, ideally KSed?** | Guidance kitchen-sinked. Future beats probable. | **MANDATORY** |
| **9** | **"You know" and "puking/sadness" check — DK farfalle?** | Gut-level capitulation. Emotional texture of exhausted despair in SS commentary, buy-side positioning, media, and Richard's instinct. **If not present, trough may not be in.** Cannot be faked or analytically constructed. | **MANDATORY** |

### Decision Logic

**Checklist:** Mandatory gates #1, 7, 8, 9 ALL must pass + ≥ 3 of remaining 5 (#2-6). Minimum 7 of 9.
**Scored (0-27):** G=3, Y=2, U=1. Strong ≥ 21, Possible 15-20, Fail < 15. Gates #1, 8, 9 must each score ≥ 2 regardless of total.

### Key Pitfalls

- **"Worser, odder, longer, further"** — things get worse than expected, in stranger ways, for longer, and go further
- **Never try to solve deteriorations analytically** — too complex, fast negative OODA loop. Wait for the PATTERN.
- **DK farfalle is not optional** — emotional capitulation IS the bottom signal

---

## Huge CfC with Clearing Event (Medium Quality)

### The Thesis

A very large CfC has driven extreme SP decline in a company that is NOT best-in-class but IS viable. The clearing event creates powerful mean-reversion. Lower quality floor = stricter requirements.

### How It Differs from Setup 4

| Dimension | Setup 4 (HQC) | Setup 6 (Medium Quality) |
|-----------|---------------|--------------------------|
| Business quality | High (A/B rated) | Medium (C/B rated) |
| CfC severity | Moderate to large | Very large — disrupted operations |
| Margin for error | Higher | Lower — must be right on clearing |
| Return profile | Quality re-rating + compounding | Mean-reversion (limited beyond normalised) |
| Criteria strictness | Quality gate + ≥1 CfC clearing | ALL 5 criteria must pass |
| Holding period | Long (compounding) | Short (6-12M tactical) |

### The 5 Criteria

| # | Criterion | What You're Looking For |
|---|-----------|------------------------|
| **1** | Bottom quartile trading multiple (2YF normalised margins)? | Extreme discount required — medium quality needs bigger margin of safety. |
| **2** | SS estimates cut deeply/fully? | Comprehensive rebasing across ALL analysts. |
| **3** | Company guidance rebased lower, ideally KSed? | Kitchen-sinked. Future beats probable. |
| **4** | Disruptive impact on operations/revenue in LTM? | CfC has ACTUALLY disrupted business. Must assess: is disruption abating? Cockroach/weirder risk addressed? |
| **5** | "You know" and "puking/sadness" check — DK farfalle? | Gut-level capitulation. Must be MORE extreme than Setup 5 given lower quality floor. |

### Decision Logic

**Checklist: ALL 5 must pass.** Strictest setup — lowest quality floor = minimal margin for error.
**Scored (0-15):** G=3, Y=2, U=1. Strong ≥ 12, Possible 9-11, Fail < 9. Gate: #5 must score ≥ 2.

### Key Pitfalls

- **Cockroach risk highest here** — medium quality + severe CfC = high probability of undisclosed problems
- **Value traps look like Setup 6** — Nexi lesson: deep value (5x) but BCG Cash Cow strategy, no genuine EPSU post-clearing
- **Shortest holding period** — 6-12M tactical position, not core holding. Size max 5-8%.

---

## Setup Interaction and Multi-Setup Classifications

Setups are not mutually exclusive. Common combinations:

| Combination | Example | Signal |
|-------------|---------|--------|
| Demand-Driven + Corporate Change | Demand explosion + new CEO capturing it | Very strong |
| Corporate Change + CfC Clearing | Corporate transformation in a quality compounder | Strong — change programme IS the clearing event |
| CfC Clearing + Trough-on-Trough | Quality cyclical at trough with specific CfC on top | Strong — cyclical and company-specific clearing converge |
| Setup 3 + Setup 5 | Corporate restructuring in a cyclical trough | Very strong — internal and external aligned |

Getlink exemplifies a strong Setup 2 with minor Setup 3 supporting elements — the demand explosion thesis is the primary driver, corporate change (CMD, dividend policy) amplifies it but doesn't standalone.

### False Friend Detection

A stock matching a setup pattern but with structural flaws is a **false friend**:

- Zero clarity of transmission mechanism from company actions to 18M-3Y EPS → false friend
- No "soul" — company doesn't believe in anything (Adevinta lesson)
- Egotism in management communication (S4 Capital lesson)
- Deep value with defensive/stagnant strategy (Nexi lesson — BCG Cash Cow)
- "Pret sandwich risk" — individually inoffensive concerns collectively fatal (Sdiptech lesson)
- HBX archetype — no clarity of tracking inputs to EPS

---

## Formatting Rules

### Rating Word Highlighting (Notion + local files)

When writing rating words, ALWAYS highlight them in their corresponding colour:

- <span color="green_bg">**GREEN**</span> — use `<span color="green_bg">GREEN</span>` in Notion
- <span color="yellow_bg">**YELLOW**</span> — use `<span color="yellow_bg">YELLOW</span>` in Notion
- <span color="orange_bg">**ORANGE**</span> — use `<span color="orange_bg">ORANGE</span>` in Notion (note: Notion uses `orange_bg`)
- <span color="red_bg">**RED**</span> — use `<span color="red_bg">RED</span>` in Notion

This applies everywhere a rating word appears: attribute ratings, summary counts, setup verdicts, cross-stock comparisons. The colour makes scanning ratings instant.

### Notion Posting Standards

All FCS Notion posts MUST follow the RESEARCHER role's `notion-posting-sop.md` formatting standards. Key requirements:

- **Sentiment highlighting:** 30%+ of text highlighted (green_bg / yellow_bg / red_bg). Sentence-level, not paragraph-level.
- **Header density:** 8-15 H2 headers, 15-25 H3 headers per full memo.
- **Bold density:** All financial metrics, ratings, percentages, analyst names, key terms bolded.
- **Bullet points:** Each 1-3 sentences / up to ~100 words. Nested for sub-points. Split if longer.
- **Pre-flight checklist:** Run the SOP's quality gate before posting (header count, highlight coverage, bold density, content completeness).
- **Full reference:** `memory/skills/researcher/notion-posting-sop.md`

---

## Output Format

**The detailed output templates for Analysis and Judgement are defined in the two SOPs:**
- **Analysis format:** `apm-analysis-sop.md` — Triaging (1-3pp, combined) and ESA (3-5pp, separate page)
- **Judgement format:** `apm-judgement-sop.md` — Triaging (combined with Analysis) and ESA (separate page)

**Key structural points:**
- At **Triaging:** Analysis + Judgement in a single Notion page. Sections clearly demarcated.
- At **ESA:** Two separate Notion pages. Judgement page includes context recap for standalone reading.
- **Analytical priority order:** Inputs (change magnitude) → Outputs (financial translation) → Foundations (probability) → Checks (investability)
- **Rating scale:** G (GREEN) / Y (YELLOW) / O (ORANGE) / R (RED)
- All standard Notion posting rules apply (30%+ highlighting, rating word colours, header density, bold density)

---

## Evaluation: Checklist vs. Scored

Run both modes in parallel for 8-12 weeks. Track divergences (stocks where checklist says FAIL but scored says POSSIBLE), Richard's verdict on each divergence, and downstream outcomes. After 8 weeks, adopt one mode, a hybrid, or continue both.

---

## Appendix A: CF Prompt Section → Setup Criteria Mapping

| CF Prompt Section | Primary Setup(s) Fed | Specific Criteria |
|-------------------|---------------------|-------------------|
| Change in leadership | Setup 3 | Input I1 (CEO), I2 (other leadership) |
| | Setup 4 | Sub-types 1 (no CEO), 2 (strategy vacuum) |
| Change in strategy/structure | Setup 3 | Input I3 (strategy), I6 (perimeter), I7 (M&A) |
| Change in priorities/ambition | Setup 3 | Input I3 (strategy), I5 (standards) |
| Change in growth/investment | Setup 3 | Input I7 (M&A), I8 (B/S) |
| | Setup 4 | Sub-type 3 (investment phase) |
| Change in margins/financials | Setup 3 | Output O3 (margin step-up), Input I4 (guidance) |
| | Setup 5 | Criterion 5 (right-sizing) |
| Change in shareholder returns | Setup 3 | Input I9 (shareholder returns) |
| Change in demand | Setup 2 | Criteria 1 (demand), 3 (scalability) |
| | Setup 4 | Sub-type 6 (market demand ↓) |
| | Setup 5 | Criterion 2 (end market demand) |
| Value chain — Competition | Setup 2 | Criteria 2 (position), 4 (oligopoly) |
| | Setup 4 | Sub-type 7 (competition ↓) |
| | Setup 5 | Criteria 3 (behaviour), 4 (pricing), 6 (retrenchment) |
| Value chain — Disruption | Setup 4 | Sub-type 8 (disruption to EGP) |
| Value chain — Political/regulatory | Setup 4 | Sub-type 8 (regulatory variant) |
| | Setup 6 | Criterion 4 (disruptive impact) |
| Value chain — Supply side | Setup 2 | Criteria 4 (oligopoly), 5 (cost leverage) |
| | Setup 5 | Criterion 6 (competitor retrenchment) |
| Revenue/demand cycle | Setup 2 | Criterion 1 (demand) |
| | Setup 5 | Criteria 2 (demand duration), 4 (pricing) |
| Value chain — Macroeconomic | Setup 5 | Criteria 1 (valuation), 2 (demand) |
| | Setup 6 | Criterion 1 (valuation) |
| Historical track record | Setup 4 | Quality gate evidence |

## Appendix B: Parking Reasons Taxonomy

**Long list (revisit in 3-6 months):**
NT/MT headwinds · Unclear mid-term investment case · Unexciting mid-term investment case · IT reseller · Slightly challenged business/weak mid-term · Unproven model ATM and complex MT conviction · Excessive customer/revenue concentration · Other reason

**Very long list (revisit only on material change):**
Serial acquirer VMS (deferred Setup 1) · AI disruption risk — pricing model (consulting) · AI disruption risk — core activity · AI disruption risk — aggregator/matcher · AI disruption risk — curator · AI disruption risk — searcher · AI disruption risk — beneficiary of high search costs · Structural regulatory risks · Structural political risks · Other reason

---

## Key Files

| File | Purpose |
|------|---------|
| This file | Master SOP for Fundamental Change Screen |
| `Files/Book5.xlsx` | ESA checklist — full attribute framework (long form + visual map) |
| `Files/Setups_SubSetups_12Apr26.xlsx` | Setup criteria and stock-level ratings |
| `memory/skills/assistant-portfolio-manager/SKILL.md` | APM operational manual |
| `memory/skills/researcher/SKILL.md` | Research pipeline logic (BD + CF prompts) |
| `memory/context/investment-strategy.md` | 4 Pillars, HQI framework, setup profiles |
| `memory/context/richard-investing-approach.md` | Philosophy, 4 patterns, playbook |
| `AI Prompts/Watson - IG - Change forces - REFV04_RB.docx` | CF prompt template |
| `AI Prompts/Watson - IG - Business description - REV V03_RB.docx` | BD prompt template |
| `memory/coaching/stock-archetypes.md` | 19 archetypes for pattern recognition |
| `memory/coaching/track-record-by-stock.md` | Historical parallels |

---

## Version History

| Date | Change |
|------|--------|
| 12-Apr-26 | V1: Initial creation. 5 active setups (Setup 1 deferred). Both checklist and scored modes. |
| 12-Apr-26 | V2: Removed Minervini 8-point and Mechanical EPS Upgrader (separate tools). Focused on fundamental change. Expanded criteria detail. |
| 12-Apr-26 | V3: Major restructure. Added pushing/removal framing. Corrected Setup 2 growth calibration. Overhauled Setup 3 with 6-layer input/output framework (Resources → Strategic Choices → Strategic Actions → KFM → FSO → SS). Added 3-role process (RESEARCHER → APM Analysis → APM Judgement). Integrated full ESA attribute framework from Book5.xlsx (Sections 3, 1, 2, 4, 5). Added Getlink worked examples for Setup 2 and Setup 3. Added stock assessment output template. |
| 12-Apr-26 | V4: Structural feedback integration. (1) Stage-gating: 13 attribute categories mapped to light/medium/robust depth across Triaging/ESA/DD from Attributes_Depth_per_stage.xlsx. Watson must know which stage before starting. (2) GTH sourcing by stage: Triaging = dashboard 8-point scores only; ESA/DD = dashboard + AS/Claude Technical Momentum research SOP + Guidance/Earnings research SOPs. (3) CfC scepticism rule: never dismiss as "transient" — default to scepticism, require hard clearing evidence. (4) Foundations SOPs: linked 5 Notion Journal SOPs (Great Operator, SRCA, value chain, industry structure, meta-quality) as canonical references. (5) Formatting: rating word colour highlighting (GREEN/YELLOW/ORANGE/RED), full Researcher notion-posting-sop.md compliance. (6) Word-based setup naming convention enforced. |
| 12-Apr-26 | V5: RESEARCHER prerequisites overhaul. (1) Full RESEARCHER output requirements table by stage (IG/Triaging/ESA/DD) with exact prompt template references. (2) PRE-ANALYSIS GATE: mandatory Notion search + dashboard check before any attribute analysis. (3) RESEARCHER GAP ESCALATION PROTOCOL: two options (brief-and-wait or brief-and-start) with specific briefing template. (4) Output template updated to include stage declaration and prerequisite check section. (5) Resource requirements table updated with specific SOP names per stage. |
| 15-Apr-26 | V7: Six Pillars framework supersedes 4-pillar structure. (1) Introduced Six Pillars (I: Technical Momentum, II: Market Paradigm Fit, III: Fundamental Change, IV: Building Blocks, V: SS Earnings Momentum, VI: Valuation). (2) Rating scale A-F replaces G/Y/O/R. (3) Database integration architecture: master + detail DBs, historical snapshots, monitoring plan, HTML dashboard. (4) 26 APM Deliverables framework added with production/reading order, investment case drivers hierarchy, and six reference frameworks. |

---

## The 26 APM Deliverables (per stock, per stage)

The APM produces 26 numbered deliverables for each stock at each stage of the research process. These replace the previous combined "FCS Analysis + Judgement" format.

### Reading Order (how Richard consumes the output)

| Order | # | Deliverable | Triaging | ESA | DD |
|-------|---|-------------|----------|-----|-----|
| C | 4 | IC written summary | 1 page | 2 pages | 3 pages |
| A | 1 | Ratings — all pillars, TCs, As, Qs [tabular] | Completed | Completed | Completed |
| A | 2 | Written judgements — all pillars, TCs, As, Qs | 2 pages | 4 pages | 6 pages |
| A | 3 | Written analysis — all pillars, TCs, As, Qs | 4 pages | 8 pages | 10 pages |
| B | 5 | Guidance | 0.5 page | 2 pages | 3 pages |
| B | 6 | Financial estimates — SS | 0.5 page | 2 pages | 3 pages |
| B | 7 | Financial forecasts — modal case (RB/FA) | RB | RB | RB |
| B | 8 | TSR DuPont (RB/FA) | RB | RB | RB |
| A | 9 | Basic checks (ADV, market cap, listing age) | 0.5 page | 0.5 page | 0.5 page |
| A | 10 | Investment Case Drivers — qualitative + financial | 1 page (hypothesising) | 2 pages | 3 pages |
| A | 11 | 10 general/standard invalidation ACH scenarios | n.a. | 1 page (hypothesising) | 1-2 pages |
| A | 12 | Key confusions (KCs) and key unknowns (KUs) | 1 page | 2 pages | 0.5 page |
| A | 13 | Key concerns/risks (KRs) | 1 page | 2 pages | 2 pages |
| A | 14 | Key hygiene factors/assumptions (KHF/As) | n.a. | 0.5 page | 1 page |
| A | 15 | Key positive optionality (KPOs) | 0.5 page | 0.5 page | 0.5 page |
| A | 16 | Key questions (KQs) before capital deployed | 1 page | 2 pages | 1 page |
| A | 17 | Key actions for next stage (KAs) | 1 page | 1 page | 1 page |
| A | 18 | Invalidation thresholds ("if X, exit") | 0.5 page | 2 pages | 3 pages |
| A | 19 | Negative expected developments | 0.5 page | 1 page | 1 page |
| A | 20 | Monitoring plan for TIs/ICDs/peers (for RESEARCHER) | n.a. | 1 page (hypothesising) | 1-2 pages |
| D | 21 | Recommendation to prioritise vs other opportunities | — | — | — |
| D | 22 | Next-stage KQs/KAs if progressed | — | — | — |
| D | 23 | Parking reasons ("gaps" analysis) if parked | — | — | — |
| D | 24 | Re-assessment criteria for re-activation | — | — | — |
| D | 25 | Monitoring plan for re-assessment criteria | — | — | — |
| — | 26 | Appendices [optional] | Any supplementary | Any supplementary | Any supplementary |

### Production Order (how APM produces the output)

B (Financials: #5, #6, #7, #8) → A (IC Analysis: #1, #2, #3, #9-#20) → C (Summary: #4) → D (Actions: #21-#25)

**Note:** Deliverables #7 and #8 are marked "RB" — these are produced by Richard / the Financial Analyst role (not yet briefed). APM uses available SS estimates and directional analysis until FA produces the modal case model.

### Investment Case Drivers (#10) — ICD Framework

The ICD deliverable is the connective tissue between ratings, monitoring, and workflow planning.

**Driver hierarchy:**
- **Fulcrum Drivers (FDs):** 1-2 things that DEFINE the thesis for the share price. If these go wrong, the case is dead. Commercial judgement about what drives the SP, not general business importance.
- **Key Drivers (KDs):** Up to 4 material factors. Pretty important but not thesis-defining.
- **Secondary Drivers (SDs):** Minor, but documented. May be upstream sub-drivers of FDs. Captured to avoid re-analysis.
- **Tertiary Drivers (TDs):** Noise. Captured explicitly as "we looked at this, it doesn't matter" to prevent future re-work.

**Each driver has:**
- Qualitative description (what's happening)
- Financial output mapping (transmission to KFMs → FSOs → EPS)
- 1-2 Leading Tracking Indicators (TIs) per FD — observable, monitorable data

**The APM's judgement on WHERE in the transmission chain the SP-moving fulcrum sits is one of the most important analytical outputs.** This is stock-specific and often sector-specific. For some stocks the SP reacts to input-level strategic deliverables (e.g. regulatory approval). For others it only reacts to financial outputs (SS upgrades, guidance beats).

Deliverable #20 (Monitoring Plan) translates the ICD output into actionable RESEARCHER instructions via the Monitoring Plan database.

### Six Frameworks — Mandatory Reference (PLACEHOLDER)

The APM should reference six investing frameworks when producing deliverables. Full codification pending — integrate at current understanding level where HELPFUL:

1. **10x Invalidation Criteria** — codified in Pillar IV, family 8 (Invalidating Attributes)
2. **Reductionist Quality Framework** — the 6 Foundations attributes + Notion Journal SOPs
3. **Holistic Quality Framework** — PLACEHOLDER (Scale Economies Shared / emergent business model properties)
4. **Mispricings Framework** — PLACEHOLDER (feeds Pillar III attributes 1.5, 1.6 and setup market error taxonomy)
5. **Inflection/Change + Inputs/Outputs** — fully codified in this SOP (6-layer framework, transmission mechanism)
6. **Patterns/Chain Patterns** — individual attribute patterns combine into chain patterns (setups). The 6 setups ARE chain patterns.
