# Minervini Inverted Screen — Operational SOP
<!-- [W] Created 15-Apr-26 from Minervini-Complete_Conversation_Summary_for_Cowork-15-Apr.md -->
<!-- Cross-reference: APM SKILL.md §Technical Overlays for Idea Sourcing -->

## Purpose

Reduce the ~1,300-stock European equity universe to a manageable shortlist by **eliminating** stocks that are structurally incapable of delivering 50%+ upside within a 2-year holding period. Designed for a fundamental investor with a 4–6 week research-to-deployment timeline.

**Key insight:** Rather than screening FOR Minervini's criteria (which admits stocks that have already moved substantially), screen OUT the structurally broken. What remains is the research universe for a fundamental investor seeking 50%+ upside.

**Frequency:** Weekly, every Monday morning.
**Owner:** Watson (APM or Researcher role).
**Output:** Scored shortlist. Names scoring 15+ flagged for IG pipeline.
**Source document:** `COWORK/Files/MarkMinervini-Complete_Conversation_Summary_for_Cowork-15-Apr.md`

---

## Architecture: Two-Stage Process

**Stage 1 — Quantitative Disqualification Screen (automated, weekly):**
Seven hard binary filters. Any single failure = remove from universe. Eliminates ~60–70% mechanically.

**Stage 2 — Scored Assessment (manual, on Stage 1 survivors):**
20-point checklist across technical positioning (0–10) and fundamental momentum (0–10). Names scoring above threshold enter research pipeline.

---

## Stage 1: Seven Hard Disqualification Filters

Apply to full universe. Binary pass/fail per stock. Fail any one = disqualified.

| # | Filter | Disqualification Threshold | What It Eliminates |
|---|--------|---------------------------|-------------------|
| 1 | Price vs. 200-day SMA | Price > 40% BELOW 200-day SMA | Deep Stage 4 declines, months from any 200-day crossover |
| 2 | 200-day SMA trend | Declining 4+ consecutive months AND/OR velocity >2–3% monthly decline | Persistent structural downtrends |
| 3 | Price vs. 52-week high | Price > 60% BELOW 52-week high | Catastrophic declines, massive overhead supply |
| 4 | 50-day vs. 200-day SMA | 50-day > 25% BELOW 200-day SMA | Active accelerating decline, bearish stack widening |
| 5 | Sell-side estimate revisions | ZERO positive revisions in 90 days | No fundamental momentum whatsoever |
| 6 | Average daily turnover | < €500k | Uninvestable liquidity |
| 7 | Market cap | < €200m | Micro-cap governance and liquidity risk |

### Filter 2 — Two Complementary Measures for 200-Day SMA Direction

Use both — they catch different failure modes:

**Velocity filter (2–3% monthly SMA decline):**
Catches fast, violent declines early. A stock falling ~10%/month for 2+ consecutive months produces approximately a 2% monthly SMA decline — early enough to be useful, serious enough to avoid eliminating routine pullbacks. The COVID V-recovery produced a maximum ~1.65% monthly SMA decline — a 2% threshold would NOT have eliminated those names from the universe.

**Duration filter (4+ months declining):**
Catches slow, persistent grinds that the velocity filter misses. A stock eroding steadily by 3–4% per month for 4+ months indicates an entrenched structural downtrend, even if no single month triggers the velocity filter.

**Practical implementation:** Either condition independently triggers disqualification.

### Why These Thresholds Are Wider Than Minervini's Full Criteria

Minervini's 8-point trend template is designed to qualify stocks already in Stage 2. These disqualification filters are designed to eliminate stocks that have no realistic path to Stage 2 within a 12–18 month research and deployment window. The gap between these filters and Minervini's full criteria is the "fishing zone" — names that fail the positive criteria but are not yet irretrievably broken.

---

## The Inversion Table — Minervini Criteria Mapped to Disqualification Profiles

| # | Minervini Criterion (pass = qualify) | Inverted Profile (fail = disqualify) | What It Catches |
|---|---|---|---|
| 1 | Price above 200-day SMA | Price > 40% below 200-day SMA | Deep Stage 4, months from 200-day crossover |
| 2 | 200-day SMA trending up 1+ months | 200-day declining 4+ consecutive months | Entrenched structural downtrend |
| 3 | Price above 150-day SMA | Price > 30% below 150-day SMA | Intermediate-term trend broken badly |
| 4 | 150-day SMA above 200-day SMA | 150-day > 10% below 200-day SMA | Full bearish intermediate structure, death cross widening |
| 5 | 50-day above 150-day SMA | 50-day > 25% below 200-day SMA | Active short-term collapse, bearish stack widening |
| 6 | Price above 50-day SMA | Price > 20% below 50-day SMA | Freefall below nearest support |
| 7 | Price ≥ 25% above 52-week low | Price within 10% of 52-week low | No evidence of institutional accumulation |
| 8 | Price within 25% of 52-week high | Price > 60% below 52-week high | Massive overhead supply |

**The gap between columns is intentional.** A stock might fail Minervini's positive criteria (not yet in Stage 2) while also NOT meeting the disqualification thresholds. That gap is where fundamental investors fish — early enough that the bulk of the move is ahead, late enough that structural recovery is credible.

---

## Stage 2: Scored Assessment (20-Point System)

Run on all Stage 1 survivors. Score each stock across two dimensions. Total = Technical Positioning (0–10) + Fundamental Momentum (0–10).

### Technical Positioning Score (0–10)

| Sub-criterion | Max Points | Scoring Rules |
|--------------|-----------|--------------|
| 200-day SMA direction | 3 | 0 = declining; 1 = flat; 2 = rising 1–3 months; 3 = rising 4+ months |
| Price relative to 200-day SMA | 2 | 0 = below; 1 = within 5% above; 2 = >5% above |
| Moving average stacking | 3 | 0 = bearish/tangled; 1 = partial bullish (1 crossover); 2 = 50D above 150D, both near/approaching 200D; 3 = full bullish stack confirmed (50 > 150 > 200, all rising) |
| 52-week positioning | 2 | 0 = >40% below 52-week high; 1 = 20–40% below high; 2 = within 20% of high |

**Total technical score: 0–10**

### Fundamental Momentum Score (0–10)

| Sub-criterion | Max Points | Scoring Rules |
|--------------|-----------|--------------|
| EPS estimate revisions (90 days) | 3 | 0 = revised down or zero upward; 1 = ≥1 upward revision but net flat/negative; 2 = net positive revisions; 3 = FY1 EPS revised up 5%+ in 90 days |
| Revenue estimate revisions (90 days) | 2 | 0 = flat or declining; 1 = revised up; 2 = revised up 3%+ in 90 days |
| Consensus rating trajectory | 2 | 0 = % buy ratings declining; 1 = stable; 2 = % buy ratings increasing |
| Consensus price target trajectory | 2 | 0 = declining or flat; 1 = increasing modestly (<10%); 2 = increasing 10%+ in 90 days |
| Most recent earnings surprise | 1 | 0 = miss; 1 = beat |

**Total fundamental score: 0–10**

---

## Prioritisation Tiers

| Combined Score | Classification | APM / Research Action |
|----------------|---------------|----------------------|
| 15–20 | **Prime candidates** | Enter IG research pipeline immediately. Flag to Richard same day. |
| 10–14 | **Watch and deepen** | Monitor weekly. Begin preliminary Business Description research. |
| 5–9 | **Too early** | Check back monthly. Log in watchlist with current score. |
| 0–4 | **Uninvestable currently** | Ignore until scoring improves. |

**Within tiers, rank by technical score first** (stocks closer to technical qualification = closer to deployment timeline). Rank by fundamental score second.

**Most actionable signal:** A rising score week-over-week — a name transitioning in real time from one tier to the next. A stock that moves from 10→14 to 15+ in a single week warrants immediate IG attention.

---

## Stage 1→2 Transition — The Sweet Spot for a Fundamental Investor

The Stage 1→2 transition sequence occurs in a predictable order. A fundamental investor's 4–6 week research window aligns with steps 2–4:

| Step | Signal | Research status |
|------|--------|-----------------|
| 1 | Price spends more time above 200-day than below | Begin monitoring; too early for full IG |
| **2** | **200-day SMA stops declining and flattens** | **← EARLIEST STRUCTURAL SIGNAL. Start IG research here.** |
| **3** | **50-day SMA crosses above 200-day** | **← Sweet spot. Begin ESA. Stock in late Stage 1 / early Stage 2.** |
| **4** | **150-day SMA crosses above 200-day** | **← Confirming. DD work appropriate.** |
| 5 | Full bullish stack forms (50 > 150 > 200, all rising, price above all) | Capital deployment window. |
| 6 | 52-week positioning criteria resolve (≥25% above low, within 25% of high) | Minervini's full 8-point template satisfied. |

**Early enough** that the bulk of the move is ahead. **Late enough** that the trend is credibly turning.

### Compressed Stage 1 Transitions

Powerful catalysts (transformational earnings beats, major contract wins, regulatory approvals) can absorb remaining supply in weeks rather than months. Stage 1 occurs but is compressed. Response:

1. Begin fundamental research immediately on the catalyst event
2. Do NOT chase the V-shaped move
3. Wait for structural confirmation — first base within the new advance, VCP, or constructive pullback to 20-day SMA
4. The catalyst provided energy; the subsequent base provides the entry

**Also watch for:** Stocks that were never in true Stage 4 — they were in a deep Stage 2 correction driven by market-wide selling, not stock-specific deterioration. When market stabilises, moving averages re-stack quickly because they never fully inverted. These can look like "skipped Stage 1" situations but are actually a continuation of a prior Stage 2.

---

## Weekly Execution Protocol

### Monday Morning Workflow

| Step | Action | Tool/Source |
|------|--------|-------------|
| 1 | Run 7 hard filters on full universe | **Master Dashboard** `filter-results.json` (MM99 filter provides Groups A-E data) + `prices.json` (MA levels, 52W, price data) + `factset-ssem.json` (estimate revisions for Filter 5) |
| 2 | Generate Stage 1 survivor list | All stocks passing all 7 filters |
| 3 | Score each survivor (Stage 2) | Manual scoring per 20-point system, using MD data for technical sub-criteria and `factset-ssem.json` for fundamental sub-criteria |
| 4 | Compare scores to prior week | Flag all week-over-week increases of 3+ points |
| 5 | Identify newly scoring 15+ names | Add to IG pipeline immediately |
| 6 | Identify pipeline names that dropped 3+ points | Flag for Richard — thesis timing may have extended |
| 7 | Update watchlist with current scores | Log in tracking system |
| 8 | Flag any held portfolio position with deteriorating Inverted Screen score | Cross-reference with APM portfolio review |

### What to Track Week-over-Week

- **Rising scores (any tier transition):** Most actionable signal — name improving in real time
- **Falling scores in pipeline names:** May indicate research timeline needs to extend; flag to Richard
- **Newly entering Stage 1 survivors:** Net new names surviving Stage 1 filters this week vs. last
- **Portfolio positions appearing in Stage 1 failures:** A live holding now failing one of the 7 hard filters is a technical deterioration alert — escalate to APM immediately

---

## Integration with Other Watson Tools

| Tool | Integration |
|------|-------------|
| **Master Dashboard MM99 filter** | The MM99 tab (11-test, 5 groups) shows positive Stage 2 qualifiers; the Inverted Screen shows negative disqualifications. They are complementary — MM99 catches stocks that have fully arrived, the Inverted Screen catches stocks approaching. Check overlap for names that have graduated from Inverted Screen watchlist to MM99 qualification. Data source: `master-dashboard/data/filter-results.json` → `mm99` object per stock. |
| **Master Dashboard filter tabs** | Use the BP (Basing Plateau) and PB (Probing Bet) tabs to identify Stage 1→2 transition candidates — stocks with Basing Plateau qualification (Medium/Tight) that are starting to show Probing Bet Early/Late qualification are prime Inverted Screen graduates. |
| **IG workflow** | Names scoring 15+ feed directly into the IG workflow — run Business Description and Change Forces prompts via both Claude [C] and AlphaSense [AS]. |
| **RESEARCHER V2** | Inverted Screen output informs which stocks to run through the RESEARCHER query framework (22 v2.1 templates + Q23 thematic). Prioritise Stage 1→2 transition stocks (steps 2–4 above) for full RESEARCHER treatment. |
| **Pipeline.md** | Newly identified 15+ scorers should appear in pipeline.md under IG stage with Inverted Screen score noted. |
| **Master Dashboard MM99 tab** | Cross-reference Inverted Screen survivors against Master Dashboard's MM99 filter (`filter-results.json`). Names improving toward 8/8+ = double signal. |

---

## Key Analytical Notes

### All Moving Averages Are Simple (SMAs), Not Exponential (EMAs)

Minervini's published criteria, Stage Analysis template, trend template, and teaching all specify SMAs. The 150-day SMA is specifically chosen for Weinstein compatibility (30-week × 5 days = 150). Some practitioners substitute EMAs at 10- and 21-day timeframes (creating confusion), but Minervini's own system uses SMAs throughout. The disqualification filters and scoring criteria above all refer to SMAs.

### The 200-Day SMA is the Spine of the Entire System

Its slope determines stage classification. Its direction determines trend. Its relationship to price and other averages determines template qualification. Every other moving average is secondary to the 200-day's structural role. A flattening 200-day after a prolonged decline is the earliest structural signal worth acting on.

### RSI is NOT Part of the Screening Framework

Minervini references a 14-period daily RSI as a secondary confirming tool only. IBD relative strength ranking (90+, ideally 95+) is a separate filter outside the trend template — this measures relative price performance vs. the market, not the RSI oscillator. Neither is part of the Inverted Screen disqualification or scoring framework.

---

## File References

| File | Purpose |
|------|---------|
| `COWORK/Files/MarkMinervini-Complete_Conversation_Summary_for_Cowork-15-Apr.md` | Source document — full Minervini methodology summary |
| `COWORK/Files/Minervini_Sell_Discipline.md` | ~10,000-word sell discipline framework |
| `COWORK/Files/Inverted_Minervini_Screen_Framework.md` | Original framework document from the conversation |
| `COWORK/Files/Stage_2_to_Stage_3_Transition.md` | ~4,000-word Stage 2→3 transition detail |
| `memory/skills/assistant-portfolio-manager/SKILL.md §Technical Overlays` | APM-level summary of this SOP |
| `memory/coaching/risk-management-lessons.md §3a` | Technical exit validation rules |
