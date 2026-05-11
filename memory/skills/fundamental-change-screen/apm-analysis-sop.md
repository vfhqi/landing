# APM — FCS Analysis SOP
<!-- [W] Created 13-Apr-26. V1. System Architect role, DEVELOPMENT mode. -->
<!-- V2 15-Apr-26: A-F scale replaces G/Y/O/R. Six Pillars framework. Database write step added. -->
<!-- Owner: APM-Analysis. Consumed by: APM-Judgement (next step), Richard (review). -->

## Purpose

This SOP governs how Watson produces the ANALYSIS component of the Fundamental Change Screen. Analysis is factual, evidence-based assessment of what a stock exhibits against the Target Investment Criteria. It is NOT judgement — it does not classify setups or form views. It answers: "What is the evidence?"

**Master reference:** `fundamental-change-screen/SKILL.md` (criteria definitions, attribute details, setup profiles)

---

## Pre-Requisites

### PRE-ANALYSIS GATE (Mandatory — execute before ANY analysis)

1. **Declare the stage.** Triaging or ESA. If unclear, ask Richard.
2. **Search Notion** for all existing RESEARCHER output on the stock (Stock Notes DB by ticker). List what exists with page titles and dates.
3. **Check the Master Dashboard** data files — read `master-dashboard/data/prices.json` (MA levels, 52W, RS) + `filter-results.json` (MM99 score, filter qualification stages) + `factset-ssem.json` (revision %, momentum count) for the stock. These provide formulaic inputs for Pillar I (Technical Momentum) and Pillar V (SS Earnings Momentum).
4. **Compare against stage requirements.** What RESEARCHER outputs are needed for this stage? What exists? What's missing?
5. **If gaps exist:** Escalate to Richard. Do not self-task the RESEARCHER. Do not proceed with analysis on missing foundations — flag which attributes will be under-supported.
6. **Read ALL available material.** Every Notion page, every source file, dashboard data. Light depth means shorter evidence per attribute, NOT less reading.

### Stage-Specific RESEARCHER Prerequisites

| Stage | Minimum RESEARCHER Inputs Required |
|-------|-----------------------------------|
| **Triaging** | IG outputs: BD [AS] + CF [C+AS merged] + TM [C]. Triaging outputs: Earnings Trends [C+AS merged] + Earnings Delivery [C+AS merged] + SS Commentary [AS] + KD Assessment [C+AS merged]. **Master Dashboard data** (`prices.json`, `filter-results.json`, `factset-ssem.json`). Total: 7 RESEARCHER pages (3 IG + 4 Triaging) + MD data. |
| **ESA** | All Triaging outputs + ESA queries #8-14 (merged where dual-source, per RESEARCHER SKILL-V2.md) + **Master Dashboard data** (all 4 data files) + any KQs |

**Note on merged pages (15-Apr-26):** Dual-source queries (#2, #4, #5, #7) now produce a single merged [C+AS] Notion page rather than separate [C] and [AS] pages. The merged page contains material from both sources with inline attribution. APM reads the merged page as a single input — source attribution is preserved throughout so APM can weight broker-sourced vs Claude-sourced evidence appropriately.

---

## Output Format

### TRIAGING ANALYSIS (1-3 pages, single Notion page)

**Notion page title:** `[W] {TICKER} ({Company Name}) — FCS Analysis (Triaging) [C] @ DD-Mon-YY`
**Properties:** Stock(s) relation linked. Case component = "APM Analysis". IAJA = Analysis. Depth = Triaging.

The analysis is structured by Pillar. Under each pillar, every applicable attribute gets a rating + evidence. The analytical priority drives the order: magnitude of change first (Inputs + Outputs), then probability (Foundations), then investability (Checks).

**Unclear-excluded rule:** If genuinely insufficient evidence exists to rate an attribute at the current stage depth, rate it as **"— unclear"** rather than defaulting to C. Unclear ratings are excluded from rollup weighting. A C means "assessed and acceptable." Unclear means "insufficient information to assess." Common unclear attributes at Triaging: IR helpfulness, insider activity, raise/lower skew counts, management quality (new appointment). These should resolve at ESA/DD.

**Single page convention (Triaging):** At Triaging, Analysis + Judgement are posted as ONE Notion page. The page follows the reading order: IC Summary (#4) → Pillar Analysis → ICDs → Risks → Key Questions → Judgement → Actions → Monitoring.

```
================================================================
STOCK: {TICKER} — {Company Name}
DATE: {DD-Mon-YY}
STAGE: TRIAGING (light depth)
================================================================

PRE-ANALYSIS GATE
  Existing Notion pages: [list all found, with dates]
  Dashboard data: [8-point score, status, key metrics]
  Required for Triaging: [list]
  Gaps identified: [list, or "None"]
  Gap action: [Escalated to Richard / Proceeding with caveats on: X, Y]

================================================================
PILLAR III: FUNDAMENTAL CHANGE — INPUTS (What is changing? How big?)
================================================================

CHANGE FORCES
  1.1 External change forces / tailwinds?    [A/B/C/D/F]
      [1-2 sentences: specific evidence of sector/market-level forces]
  1.2 Internal change forces?                [A/B/C/D/F]
      [1-2 sentences: specific evidence of corporate change]
      [If Corporate Change candidate: brief 6-layer mapping —
       which layers have visible evidence?]
  1.3 Absence of external headwinds?         [A/B/C/D/F]
      [1-2 sentences: what headwinds exist, how material]
  1.3b Well-invested base?                   [A/B/C/D/F]
      [1-2 sentences: operational/financial foundation]
  1.4 Thesis congruency with past/present?   [A/B/C/D/F]
      [1-2 sentences: does the change thesis follow logically?]
  1.5 Large CfC/mispricing?                  [A/B/C/D/F]
      [1-2 sentences: specific CfC identified, or growth mispricing]
      [If CfC candidate: which sub-type(s)? Evidence of CLEARING?
       Apply CfC scepticism rule — assume more persistent than it appears]
  1.6 Low trading multiple?                  [A/B/C/D/F]
      [1-2 sentences: current multiple, historical range, peer comparison]

MOMENTUM (from Dashboard 8-point scores at Triaging)
  M1 Technicals (RS, MAs, excess returns)    [A/B/C/D/F]
  M2 SS estimates, ratings, PTs, narrative   [A/B/C/D/F]
  M3 Peers — technicals, SS                 [A/B/C/D/F]
  M4 Company delivery                        [A/B/C/D/F]
  [1-2 sentences each sourced from dashboard data]

================================================================
PILLAR III: FUNDAMENTAL CHANGE — OUTPUTS (Does the case produce
what's needed? Most important family.)
================================================================

  4.1  Triple ratchet step-up (3Y, MT)?      [A/B/C/D/F]
       [Is earnings improvement multi-year and self-reinforcing?]
  4.2  12-20% EPS growth p.a.?               [A/B/C/D/F]
       [NB: for Demand-Driven, >20% is positive, not a concern]
  4.3  Margin/growth step-up?                [A/B/C/D/F]
       [Visible inflection in margins or revenue growth?]
  4.4  Fit with required setups?             [A/B/C/D/F]
       [Preliminary — which setup(s) plausibly fit?]
  4.5  Post CfC clearing / SP turn?          [A/B/C/D/F]
       [Is the CfC clearing AND has SP started to turn?]
  4.6  Less than 6M after turn?              [A/B/C/D/F]
       [Entry window timing]
  4.7  Helpful IR re. operating momentum?    [A/B/C/D/F]
       [Can we get intra-quarter colour?]
  4.8  Trackable key leading indicators?     [A/B/C/D/F]
       [Can FD/KDs be monitored fortnightly?]
  4.9  Modal case 18M EPS > guidance > SS?   [A/B/C/D/F]
       [DIRECTIONAL at Triaging — conservative guidance pattern?
        SS at low end? Beat-and-raise dynamics?]
  4.10 3:1 raise/lower skew NFY?             [A/B/C/D/F]
       [Estimate revision direction and breadth, directional]
  4.11 Multiple more co. than exog. driven?  [A/B/C/D/F]
       [Company fundamentals vs. sector sentiment?]
  4.12 More than 20% 3Y TSR?                 [A/B/C/D/F]
       [Rough TSR: current multiple → normalised exit × EPS growth]

================================================================
PILLAR IV: BUILDING BLOCKS — FOUNDATIONS (How probable is the change?)
================================================================

  3.1 Great operator?                        [A/B/C/D/F]
      [CEO/management quality. Animal CEO signal?]
  3.2 Advantaged business + widening SRCA?    [A/B/C/D/F]
      [Hard + soft competitive advantages. 1% company?]
  3.3 Favourable value chain dynamics?        [A/B/C/D/F]
      [Position, supplier/customer power, value capture]
  3.4 Supportive industry structure?          [A/B/C/D/F]
      [Oligopoly, BtE, rational behaviour]
  3.5 High secular growth potential?          [A/B/C/D/F]
      [Structural tailwinds, S-curve position]
  3.6 Stock market paradigm fit?              [A/B/C/D/F]
      [Alignment with current themes and risk regime]

  FOUNDATIONS VERDICT: [Summary — does the quality base make
  the change thesis probable or merely hypothetical?]

================================================================
PILLAR IV: BUILDING BLOCKS — CHECKS (Is it investable? Complexity filter.)
================================================================

  ** WATSON COMPLEXITY GATEKEEPER ROLE ACTIVE **

  2.1 ≤2 FDs and ≤4 KDs?                    [A/B/C/D/F]
  2.2 ≤10 geographies × business units?      [A/B/C/D/F]
  2.3 Zero VC headwinds to revenue?           [A/B/C/D/F]
  2.4 ≤2 CfCs or problems?                   [A/B/C/D/F]
  2.5 Conservative guidance confirmed?        [A/B/C/D/F]
  2.6 Clear strategy-to-EPS transmission?     [A/B/C/D/F]
  2.7 Clear VC/Co inputs-to-EPS transmission? [A/B/C/D/F]

  CHECKS VERDICT: [X of 7 pass. If ≥2 fail: explicit complexity
  concern and parking recommendation, regardless of other pillars.
  Neutral but challenging tone.]

================================================================
PILLAR IV: BUILDING BLOCKS — FITNESS-FOR-FIGHTING (light depth at Triaging)
================================================================

  5.1 Market cycle                           [A/B/C/D/F]
  5.2 AI disruption                          [A/B/C/D/F]
  5.3 Input cost inflation                   [A/B/C/D/F]
  5.4 No overlap with 10x invalidating ACHs  [A/B/C/D/F]

  [Families 8-12 NOT assessed at Triaging]

================================================================
SUMMARY RATINGS TABLE
================================================================

| Pillar | A | B | C | D | F | n/a |
|--------|---|---|---|---|---|-----|
| III: Fundamental Change — Inputs | | | | | | |
| III: Fundamental Change — Outputs | | | | | | |
| IV: Building Blocks — Foundations | | | | | | |
| IV: Building Blocks — Checks | | | | | | |
| IV: Building Blocks — FFF | | | | | | |
| **TOTAL** | | | | | | |
```

### Formatting and Posting Rules

- **30%+ sentence-level highlighting** (green_bg / yellow_bg / red_bg) per notion-posting-sop.md
- **Rating word highlighting:** GREEN/YELLOW/ORANGE/RED in their respective background colours
- **Bold:** All financial metrics, percentages, rating words, analyst names, company names
- **Pillar headers as H2.** Attribute families as H3. Individual attributes as bullet points.
- **Bullet structure — default is parent + sub-bullets.** Any bullet with a headline finding AND supporting evidence/context uses parent + sub-bullet format. Flat single bullets only for standalone facts. Hard cap: ~100 words per bullet (any level).
- **Chunking:** If >15K characters, chunk per notion-posting-sop.md protocol
- **Property verification:** Stock(s) relation, case component, IAJA, depth — all set correctly

---

## ESA ANALYSIS (3-5 pages, separate Notion page from ESA Judgement)

**Notion page title:** `[W] {TICKER} ({Company Name}) — FCS Analysis (ESA) [C] @ DD-Mon-YY`
**Properties:** Same as Triaging but Depth = ESA.

Same structure as Triaging with these key differences:

### Depth Increases at ESA

| Attribute Family | Triaging Depth | ESA Depth | What Changes |
|-----------------|---------------|-----------|-------------|
| 1. Business foundations | light | light | Same — but now assessed against Notion Journal SOPs systematically |
| 2. Case inputs | light | medium | Multi-source evidence. 6-layer framework for Corp Change fully mapped. CfC clearing evidence assessed with timeline. |
| 3. Setups | light | medium | Detailed checklist scoring for each candidate setup |
| 4. Past trend attributes | light | **robust** | Full GTH from dashboard + Technical Momentum SOP + Guidance/Earnings SOPs |
| 5. Transmission mechanism | n/a | medium | **NEW at ESA.** Trace strategy → actions → KFMs → FSOs → EPS. If unclear = false friend flag. |
| 6. Simplicity guardrails | light | **robust** | Full quantitative check. FD/KD counts verified. Perimeter mapped. |
| 7. Required case outputs | light | medium | **Financial model supports #9, #10, #12.** Actual numbers, not directional. |
| 8. Invalidating | n/a | light | **NEW at ESA.** 10 invalidating constraints checked. Red flag / yellow flag counts. |
| 9. Seek-to-avoid | n/a | medium | **NEW at ESA.** SHMLP risks, outcome skew, trough multiple, exogenous multiple. |
| 10. Small size | n/a | medium | **NEW at ESA.** Sentiment SHMLP risks. |
| 11. Nice-to-have | n/a | light | **NEW at ESA.** Positive optionality, self-righting MMO. |
| 12. Me-state | n/a | light | Richard only — APM flags observations but does NOT rate. |
| 13. FFF | light | light | Same depth, but informed by more research. |

### ESA-Specific Analysis Additions

**Transmission Mechanism (Family 5 — medium depth):**
```
TRANSMISSION MECHANISM ASSESSMENT
  Strategy → Actions → KFMs → FSOs → EPS

  Step 1: [Strategy/change thesis] → [Observable actions]
  Step 2: [Actions] → [Which KFMs should move?]
  Step 3: [KFMs] → [Which FSOs should improve?]
  Step 4: [FSOs] → [EPS impact, timing, magnitude]

  TRANSMISSION CLARITY: [Clear / Partial / Unclear]
  [If Unclear: this is a false friend signal. Flag prominently.]
```

**Constraint Families (8-12 — new at ESA):**
```
INVALIDATING CONSTRAINTS (light)
  5.I1 No slowing of core engine?            [A/B/C/D/F]
  5.I2 No mediocre CEOs / weird choices?      [A/B/C/D/F]
  5.I3 No big 'Hmmms'?                       [A/B/C/D/F]
  5.I4 No red flags (≥2 Rs)?                 [A/B/C/D/F]
  5.I5 No mediocrity (≥8 Ys)?               [A/B/C/D/F]
  5.I6 No recent earnings cuts?               [A/B/C/D/F]
  5.I7 No peers having problems?              [A/B/C/D/F]
  5.I8 No negative lesson overlap?            [A/B/C/D/F]
  5.I9 No false friend / unacceptable fit?    [A/B/C/D/F]

SEEK-TO-AVOID CONSTRAINTS (medium)
  5.A1 Fundamental SHMLP risks?               [A/B/C/D/F]
  5.A2 Wide outcome skew?                     [A/B/C/D/F]
  5.A3 Large downside to trough multiple?     [A/B/C/D/F]
  5.A4 Multiple more industry than company?   [A/B/C/D/F]

SMALL SIZE CONSTRAINTS (medium)
  5.S1 Sentiment-related SHMLP risks?         [A/B/C/D/F]

NICE-TO-HAVE (light)
  5.N1 Big positive optionality?              [A/B/C/D/F]
  5.N2 Rapid self-righting MMO?               [A/B/C/D/F]
```

### ESA Summary Ratings Table (expanded)

Includes all 13 families. Same format as Triaging table but with additional rows for the constraint families.

---

## Database Write Step (Mandatory after posting to Notion)

After posting Analysis to Notion, APM MUST also write ratings to the database system:

1. **Write attribute ratings** to `databases/detail/p3-fundamental-change.json` and/or `databases/detail/p4-building-blocks.json`
2. **Run rollup** via `databases/scripts/rollup.py` to compute pillar scores
3. **Rebuild dashboard** via `databases/scripts/build-dashboard.py`
4. **Verify** the Master IC Ratings DB (`databases/master/ic-ratings-current.json`) reflects the new ratings

This step ensures the dashboard and cross-stock comparison views are always current. The Notion page is the detailed written analysis; the database is the structured, comparable, filterable ratings.

### Rating Scale Reference

| Grade | Percentile | Meaning |
|-------|-----------|---------|
| **A** | 90-100% | Top decile. Rare/great. |
| **B** | 75-90% | Good. |
| **C** | 50-75% | Fine. |
| **D** | 35-50% | Weak. |
| **F** | Bottom ~33% | Fail. |

---

## Quality Standards

### Evidence Standards by Depth

| Depth | Evidence Requirement |
|-------|---------------------|
| **Light** | 1-2 sentences per attribute. Single-source acceptable. Directional assessment. |
| **Medium** | 2-4 sentences per attribute. Multi-source required (≥2 RESEARCHER outputs cited). Quantitative where available. |
| **Robust** | 4+ sentences per attribute. Full multi-source triangulation. Quantitative evidence mandatory. Financial model data where applicable. Specific RESEARCHER page citations. |

### Labelling Discipline

Every statement in the Analysis should be identifiable as ANALYSIS (factual assessment), not JUDGEMENT (view formation). If Watson catches itself forming a view ("this suggests the stock fits Setup X"), it should either move that to the Judgement note or explicitly flag it as a preliminary analytical observation requiring judgement-stage confirmation.

### Rating Scale

| Rating | Meaning | Colour |
|--------|---------|--------|
| **A** | Excellent. Top decile. Strong positive evidence. Meets criterion clearly. | `green_bg` |
| **B** | Good. Solid positive evidence. Meets criterion well. | `green_bg` |
| **C** | Fine. Partial or mixed evidence. Meets criterion adequately. | `yellow_bg` |
| **D** | Weak. Concerning. Evidence is negative or criterion substantially unmet. | `orange_bg` |
| **F** | Fail. Clear negative evidence. Disqualifying for this criterion. | `red_bg` |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V2 | 15-Apr-26 | Scale upgrade: [G/Y/O/R] → [A/B/C/D/F]. Six Pillars framework with updated pillar names. Database Write Step section added. Rating scale table updated to reflect new grading system. |
| V2.1 | 15-Apr-26 | Stage prerequisites updated for merged [C+AS] pages (RESEARCHER dual-source merge protocol). Triaging = 7 pages (3 IG + 4 Triaging). Note added on how APM reads merged pages. |
| V1 | 13-Apr-26 | Initial creation. Triaging + ESA formats defined. 4-Pillar structure. Complexity gatekeeper role. Change-first analytical priority. |
