# Investing System Architecture
<!-- [W] Reconstructed 27-Mar-26, enriched 27-Mar-26 with Forecastability Framework, Radar Process, knowledge optionality principle. Updated 15-Apr-26: Six Pillars IC framework, IC Ratings database system, ICD framework, 26 APM deliverables. -->

Richard views his approach as a **complex system**, not a linear process. The system has six interconnected domains, each feeding the others.

---

## The Six Domains

### 1. ETCs (Evergreen Target Conditions)
Three perpetual goals that never "complete" — they set the direction. Everything else serves them.

- **ETC 1 — Investing:** Have a portfolio and squad that makes outlier returns (5-10% outperformance per annum) on a rolling next-two-year basis by continually, fluidly and successfully adapting to any unfolding circumstances.
- **ETC 2 — Self/Performance:** Consistently execute the process at an elite level. Mark Douglas style. Conservative analysis, aggressive execution.
- **ETC 3 — Business/Viewforth:** Build and sustain a viable solo investment operation with appropriate infrastructure, tools, and professional standards.

### 2. Investment Strategy
The "what" — defines what to own, what to avoid, and the frameworks for deciding. Centred on the **Six Pillars of a Target Investment Case** (15-Apr-26, supersedes prior 4-pillar framework):

| Pillar | Name | Nature | Source |
|--------|------|--------|--------|
| I | Technical Momentum | Quantitative/Technical | Dashboard (formulaic) |
| II | Market Paradigm Fit | Thematic/Qualitative | APM judgement |
| III | Fundamental Change | Fundamental/Qualitative | APM analysis + judgement (Inputs + Outputs + Setup) |
| IV | Building Blocks — Robustness | Fundamental/Qualitative | APM analysis + judgement (Guardrails + Foundations + Constraints) |
| V | SS Earnings Momentum | Quantitative | Dashboard (formulaic, EPS 2x weighted) |
| VI | Valuation | Returns/Quantitative | Financial Analyst / APM |

**Rating scale:** A = top decile (rare, exceptional), B = good (75-90%), C = fair (50-75%), D = weak (35-50%), F = fail (bottom third).

**Rollup methodology:** Weighted worst-of — 60% bottom quartile of rated attributes, 40% overall weighted average. Conservative by design: a mix of B's and C's rounds toward C, not B. Family-specific weights for P4 (HEAVY: Guardrails/Foundations/Invalidating; MEDIUM: Seek-to-avoid/Size/Congruency/FFF; LIGHT: Nice-to-have). P5: EPS = 2x weight, rest = 1x.

**Investment Case Drivers (ICD) framework:** APM classifies all drivers per stock: Fulcrum Drivers (1-2, SP-defining), Key Drivers (up to 4), Secondary (minor), Tertiary (noise). Each FD has qualitative description + financial output mapping + 1-2 Leading Tracking Indicators. Transmission mechanism: INPUT (CEO/strategy) → INPUT (operational execution) → INPUT (qualitative change) → KFM → FSO → EPS → SP.

**26 APM deliverables per stock per stage:** Scaled by stage depth (Triaging light, ESA moderate, DD full). Four sections: B (Financials, produce first), A (IC Analysis), C (Summary, produce after A+B), D (Actions). Reading order: C → A → D → B.

**IC Ratings Database:** JSON source of truth with five layers — Decision (Master, ~20 fields), Detail (~107 fields across 6 pillars), Historical (snapshots), Information (RESEARCHER/Dashboard), Presentation (Notion + HTML dashboard). Rollup script computes master scores from detail. Dashboard shows colour-coded pillar ratings, monitoring plan, findings log.

Cross-reference: `investment-strategy.md`, `fundamental-change-screen/SKILL.md` (V7+), `databases/` folder

### 3. Market Environment ("Fit for Fighting")
Macro awareness that shapes portfolio construction and industry tilts. Not macro forecasting — environmental awareness that determines which setups to prioritise.

Current state (Mar 2026): Risk-off mode. Iran conflict driving industry-level analysis. Targeting: recurring non-cyclical revenues, domestic EU footprint, banks/insurance, cable companies, healthcare. Avoiding: European chems, consumer discretionary, beverages.

#### Resilience-Optionality 12-Dimension Framework (Aug 2023)
Deep assessment of portfolio position fragility. 12 dimensions of resilience + optionality; drives position sizing and monitoring intensity. Resilient positions can hold at larger sizes (15%) with lower stress. Fragile positions capped at 5% unless optionality is visible. Core insight: resilience ≠ safety (defensive stocks can be illiquid). Optionality (paths forward, expansion opportunities) ≠ growth (hard to forecast, binary risk).

#### End-Game Logic / Tarasoff Test (Jul 2023)
When a position breaks thesis or deteriorates materially, apply Josh Tarasoff's "end-game logic": What is the realistic probability of recovery to entry valuation within the holding period? If <30%, cut immediately. Don't hold deteriorating positions hoping for mean reversion. The market will likely get worse before better. Default action: exit, rebuild conviction, re-attack if case clears.

#### 18-4+ Time Horizon Discipline (Aug 2023)
Framework for managing multiple time horizons simultaneously:
- **18M thesis:** The core investment case. What drives 18M EPS?
- **4Y thesis:** The strategic direction and longer-term optionality.
- **"+":** The "why own it forever?" aspiration if thesis is exactly right.
Entry and exit decisions must respect all three horizons. If 18M thesis breaks but 4Y is intact, trim but don't fully exit. If 18M + 4Y both break, cut immediately.

#### SMP/FSO/KFM/OO Monitoring Framework (Nov 2023)
Four-dimension monitoring system for live positions:
- **SMP:** Share price momentum. Is the stock trading higher/lower on fundamentals or sentiment?
- **FSO:** Fundamental strength/opportunity. Are drivers still intact? Is case thesis advancing?
- **KFM:** Key fundamental milestones. Are quarterly/annual updates confirming thesis?
- **OO:** Operator outlook / competitive positioning. Is management executing? Is competitive position strengthening/weakening?

Monitor all four fortnightly. A deterioration in any dimension triggers 30-day shot clock unless the other three are clearly positive.

#### HQI Scorecard — High Quality Inflection (Core Sizing Framework)
Four-dimensional quality rating that drives position sizing:
1. **Resilience** — Business quality, moat sustainability, downside protection, margin of safety vs. intrinsic value
2. **Inflection/Optionality** — Growth optionality magnitude and probability; range of outcomes vs. consensus
3. **Potential Returns** — 3Y IRR potential, CAGR projections (targets 100-120%+ on probabilistic view)
4. **Conviction** — Confidence in assessment of above three (information breadth, circle of expertise, eyes-on work, bear case explored)

**HQI Categories** (drive position sizing):
- **Robust HQI:** High quality + proven inflection + very high conviction → 10-15% sizing
- **Resilient & Intense HQI:** Rounded profile + strong quality + growth optionality → 10-15% sizing
- **Ultra High Potential but Fragile (UHPYHQI):** High growth potential but execution/thesis risk → 0-5% (research/de-risking mode)
- **Resilient but Low Optionality HQI:** Strong defensive quality + limited growth → 8% sizing

#### Portfolio Management Framework — TCI (Target Condition Portfolio)
8-10 core positions on the "pitch" with specific concentration discipline:
- Top 3 names represent **40-50% of capital** (15-20% of AUM each)
- Handful at 5%, 8%, 10%, 12%
- Expect 2-3 position swaps per year (1-in-1-out discipline)
- Emphasis on core portfolio quality: high conviction, resilience-optionality scoring 8+/12 dimensions

#### Risk Matrix Framework (Forecastability × Impact × Resource Intensity)
Three dimensions to assess risk severity:
- **Forecastability (F):** Can we predict/see this coming? Sudden vs. drip-drip-drip? Epistemic (knowable) vs. aleatory (randomness)?
- **Impact (I):** How much damage if occurs? (25%+ vs. 5% on intrinsic value?) Timely (N6M) vs. far (5Y+)? Non-linear chain reactions? Thesis-invalidating?
- **Resource Intensity (R):** How much attention/expertise needed? Outside circle of excellence?

Aggregate by: range/number of risks, complexity, F/I/R mapping, team bias/weakness alignment.

#### Radar Process — Four-Step Environmental Monitoring
Top-down macro/environmental framework (not forecasting, situational awareness):
1. **Mapping:** Get high-altitude view of macro forces, risk environment, turning points vs. trends. Define time frames for persistence.
2. **Planning/Acting:** Identify which portfolio ideas flow forward, what triggers acceleration, leading indicators vs. contra-indicators.
3. **Here & Now:** Are we concentrated in best stocks? Sized correctly? Maximizing N2Y return targets vs. minimizing next-month loss?
4. **Insights to Monitor:** "All roads lead to The Fed and US stock market." Stock markets globally fungible. Market psychology often matters more than fundamentals in positioning.

### 4. Stock-Specific Research
The 4-stage pipeline from idea to investment (IG → ESA → DD → LIVE). Each stage has a Target Condition (TC) and SOP, with defined inputs, outputs, and decision gates.

**Forecastability Life Cycle Framework:** Implicit in many decisions — used for assessing predictability windows at each stage. Earlier stages offer wider forecastability; later stages narrow focus to near-term drivers. Key question at each gate: how far forward can we reliably forecast?

**Key Questions Framework as Foundational SOP (Jan 2023):** At every stage, the work produces a prioritised Key Questions list. KQs are the explicit gaps in conviction. By stage 2 (ESA), the top 3-5 KQs should define the research roadmap. By DD, all KQs must be answered or explicitly parked. KQs serve as the true guardrail against analytical rabbit holes — if it doesn't address a KQ, don't do the work.

Cross-reference: `investment-process.md`

### 5. Monitoring
Ongoing surveillance of live positions and watchlist names. Two modes:
- **Portfolio monitoring:** Track all drivers fortnightly, rate any deterioration RED, review monthly, move to disprove-or-invalidate if needed
- **Squad monitoring:** Lighter touch — developments checks, earnings reviews, information funnel processing

**Monitoring Plan Database (15-Apr-26):** Structured JSON database (`databases/monitoring/monitoring-plan.json`) where APM defines WHAT to monitor, WHY (higher intent/mission command), HOW, and FREQUENCY. RESEARCHER executes the monitoring. Findings logged to `databases/monitoring/findings-log.json` as time-series observations. APM reviews findings at next cycle. Default frequency: slower than instinct (Monthly unless specific reason for faster). Each monitoring item links to a driver tier (Fulcrum/Key/Secondary/Macro).

**Leakage Journal Concept (Sept 2023):** Systematic daily log of portfolio "leaks" — the way capital is haemorrhaging from the portfolio through (a) deteriorating positions held too long, (b) winners trimmed too early, (c) missed inflection points, (d) poor exits. Every month, analyse leakage patterns. Most leakage is systematic (endowment bias, FOFR, complexity avoidance). Coaching: focus on leakage reduction, not absolute return maximisation.

### 6. Workflow/Planning
The operating system layer — how work gets prioritised, sequenced, and executed day-to-day. Mission command principles applied to investment workflow.

**Radar Process:**
- **Step 1 — Mapping:** "Get your head out of the game" — high-altitude view of opportunity set, industry positioning, risk environment, watchlist development. No immediate action orientation.
- **Step 2 — Planning/Acting:** From the map, identify which ideas flow to the pipeline, what triggers acceleration, what warrants new research emphasis.

---

## How the Domains Connect

The system operates as a feedback loop, not a waterfall:

```
ETCs (direction) → Strategy (what to own) → Environment (industry tilts)
     ↓                    ↓                        ↓
  Process (pipeline) ← Monitoring (signals) ← Workflow (execution)
     ↑_________________________________________________↑
```

Key principles:
- **System execution > process compliance.** The system serves the strategy. The process serves the system. Everything is means to an end. "Doing investing" is not the priority — profiting in the environment is.
- **Thematic and style agnosticism.** The system watches all industries with no extreme preferences for sector, business model, or investment style (value vs growth). Preferences are fine; dogmatisms are not. This creates "knowledge optionality" — exposure to the full opportunity set, reducing blind spots. (Tao Jones concept: Structured Serendipity)

---

## Operating System Map

| Layer | Contains | Updates |
|-------|----------|---------|
| ETCs | 3 perpetual goals | Rarely — fundamental direction |
| Strategy | Setups, profiles, predictability tests | Quarterly review, evolving |
| Environment | Macro tilts, industry analysis, risk posture | Continuous — journal entries |
| Process | 6-stage funnel, SOPs, checklists | Refined after each major position |
| Monitoring | Driver tracking, threshold alerts | Daily/weekly cadence |
| Workflow | Task management, prioritisation, Watson protocols | Daily |

---

## Complex Systems Thinking Applied

See `mental-models.md` / `wisdom-library/` for full framework (principles, degradation indicators, self-management application). Key investing application: three degradation indicators (slower recovery rates, rising autocorrelation, rising variance) signal loss of resilience before collapse becomes visible.
