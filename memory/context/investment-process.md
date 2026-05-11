# Investment Process — 4-Stage Research Funnel
<!-- [W] Reconstructed 27-Mar-26. Updated 01-Apr-26: corrected to 4 stages per Richard's briefing. Updated 15-Apr-26: Six Pillars IC framework, 26 APM deliverables, ICD framework, database integration. -->

## Overview

Four stages, each reflecting Richard's KNOWLEDGE level of a stock. Each stage has a Target Condition (TC) and SOP. At every stage: define work plan, do work, analyse, judge (progress or park), generate 2 downstream actions. No open loops.

```
IG → ESA → DD → LIVE
```

## Two Orthogonal Dimensions (Stocks DB)

Stocks are classified on TWO independent axes:

### KNOWLEDGE Level (= research stage, reflects depth of understanding)
Maps to Stocks DB field "KNOWLEDGE level":
- 1. Pre-IG
- 2. RB generated
- 3. Triaged
- 4. ESA
- 5. Deep dive

### INTEREST Level (= watchlist placement, reflects conviction/proximity to action)
Maps to Stocks DB field "INTEREST level":
- 1. Live (in portfolio)
- 2. Very short list
- 3. Short list
- 4. Long-list
- 5. Very long-list
- 6. Uncategorised ATM

### How Stocks Move Through the System
1. Stocks progress through the 4 stages of the research process (IG → ESA → DD → LIVE)
2. At any stage gate, they are either progressed to the next stage or PARKED onto a watchlist
3. If a stock is PARKED, it gets: (a) a specific INTEREST level / watchlist placement, (b) REASONS FOR PARKING, and (c) REASSESSMENT CRITERIA that define what would reactivate it
4. If a stock completes DD and is invested in, it moves to LIVE (INTEREST level = "1. Live")

### Additional Stocks DB Fields
- **TIMELINESS level**: High urgency (N0-3M), Middling (N3-6M), Low/unclear (N6M+)
- **Parking reason**: CEO quality, Near-term risks, No clear case

---

## Stage 1: IG (Ideas Generation)

**Purpose:** Surface new names for the squad. The aim is **filtering OUT** ideas that are not remotely acceptable. Breadth over depth.

**KNOWLEDGE levels covered:** Pre-IG → RB generated

**Process:**
1. Run Business Description (BD) prompt through both Claude [C] AND AlphaSense [AS]
2. Run Change Forces (CF) prompt through both Claude [C] AND AlphaSense [AS]
3. Post 4 FULL-LENGTH outputs to Notion Stock Notes DB with [C] and [AS] tags
4. Apply 30%+ sentiment highlighting to all outputs
5. No IAJA synthesis at IG stage (07-Apr-26 instruction)
6. Richard reads, forms initial view, decides: progress to Triaging or park

**Prompt templates:** `AI Prompts/Watson - IG - Business description - REV V03_RB.docx` and `AI Prompts/Watson - IG - Change forces - REFV04_RB.docx`

**Skill reference:** `memory/skills/researcher/SKILL.md` (master file; archived IG skill at `memory/skills/ig-ideas-generation/SKILL.md`)

**Universe:** ~1,300 European stocks. Sweet spot: $5-50bn market cap.

---

## Stage 1b: Triaging

**Purpose:** Determine whether the idea is a **good fit** — at a LIGHT level, based on **pattern recognition** and **"strong views, weakly held"** (sensible hypotheses that need testing with more evidence). Not deep analysis — fast, disciplined filtering.

**KNOWLEDGE level:** Triaged

**Key work products:**
- Most Recent Earnings Review (Richard must commission — not auto-produced)
- GTA Unknown Key Drivers analysis
- GTH Analysis + Peer GTH Analysis
- Sell Side (SS) Analysis — **SS = Sell Side, NOT Short Seller**
- IR Contact prep (returned in chat, NOT posted to Notion)
- Business Model & Sector Primer (moved from ESA, 13-Apr-26)
- Guidance analysis (moved from ESA, 13-Apr-26)

**Prompt templates:** Multiple Triaging-stage prompts in `AI Prompts/Watson - Triaging - *.docx` plus two ESA-labelled templates (BM&Sector Primer, Guidance) now used at Triaging.

**Output:** Triaging-level FCS assessment. Setup profile classification. Decision: progress to ESA or park onto a watchlist with reasons and reassessment criteria.

---

## Stage 2: ESA (Early-Stage Assessment)

**Purpose:** Dual purpose: (1) interrogate the change thesis — is the change significant enough, is management dynamic enough, are the required outputs compelling; (2) breadth coverage — ensure ALL aspects of the investment case are covered at light or medium depth. ESA establishes the **key risks, key questions, and key confusions** that DD will focus on.

**KNOWLEDGE level:** ESA

**Key work products:**
- History of Earnings Delivery (multi-year trajectory — distinct from Triaging's Most Recent Earnings Review)
- Tracking vs Guidance analysis (forecast accuracy)
- Value chain analysis / map
- Pre-mortem (always REFV02_RB)
- CEO/CFO question set
- Key Questions identified and researched
- Short Seller All 10 TEST (WIP — ask Richard before running)

**Prompt templates:** Multiple ESA-stage prompts in `AI Prompts/Watson - ESA - *.docx`

**Output:** ESA memo with preliminary investment case, key risks, key confusions, and fulcrum driver thesis. The setup title crystallises at ESA. Decision: progress to DD or park onto a watchlist with reasons and reassessment criteria.

---

## Stage 3: DD (Deep-Dive)

**Purpose:** Resolve the key questions. Test the fulcrum driver thesis. Fill gaps, stress test, prepare for investment committee (self). Round out the case. Encompasses both the initial deep-dive and the rounding-out phase.

**KNOWLEDGE level:** Deep dive

**Key work products:**
- KQ research memos (Claude + AlphaSense dual-source)
- KQ analysis memos (framework-driven judgement)
- FX exposure analysis
- Management deep-dive (CEO research, insider comments, governance checks)
- Pre-mortem
- Remaining KQs resolved
- Case file complete
- Position sizing framework applied
- Monitoring plan defined

**Prompt templates:** Multiple DD-stage prompts in `AI Prompts/Watson - DD - *.docx` and `AI Prompts/Watson - ESA_DD - *.docx`

**Output:** Complete investment case with all key questions answered, risks mapped, and monitoring plan. Decision: invest (move to LIVE) or park onto a watchlist with reasons and reassessment criteria.

---

## Stage 4: LIVE

**Purpose:** Live position in the portfolio. Shift to monitoring mode.

**INTEREST level:** "1. Live"

**Key activities:**
- Execute entry (timing, sizing)
- Set up monitoring cadence (driver tracking, earnings reviews)
- Apply paranoid tilt
- Track against 18-month lifecycle
- Regular monitoring of Tracking Indicators (TIs) and drivers
- Communication from Watson on status and any changes

---

## Stage-Gate Logic

At every stage gate:
1. **IAJA loop:** Information gathered → Analysis performed → Judgement formed → Action taken
2. **2 downstream actions minimum** — every judgement must generate at least 2 next steps
3. **Park protocol:** If parking, log the reason and the trigger that would re-activate
4. **No open loops:** Every thread must be resolved or explicitly parked with a future trigger

## Six Pillars IC Framework Integration (15-Apr-26)

The Six Pillars framework defines the TARGET INVESTMENT CASE that the research process is building toward at every stage. The 4-stage funnel (IG → ESA → DD → LIVE) remains the process; the Six Pillars define what a complete investment case looks like.

**At each stage, the APM produces a subset of 26 deliverables** scaled by depth:
- **IG:** Light — #4 (IC Summary sketch), #9 (initial Six Pillar ratings, mostly "—"), #10 (ICD hypothesising), #14 (Key Questions), #21-25 (Actions)
- **Triaging:** Light-to-moderate — adds #1-3 (IC Analysis), #5-6 (EGP, KFMs), #11 (Risk Assessment), #20 (Monitoring Instructions)
- **ESA:** Moderate — all 26 deliverables at medium depth. This is where the IC crystallises.
- **DD:** Full depth — all 26 deliverables comprehensively. All KQs answered. Monitoring plan fully defined.

**Database write step** is mandatory after every APM Analysis + Judgement cycle. APM writes detail ratings to pillar JSONs, updates master, runs rollup script, rebuilds dashboard. This creates a living, versioned record of how the IC evolved through stages.

**ICD framework (deliverable #10)** classifies all drivers: Fulcrum (1-2, SP-defining) → Key (up to 4) → Secondary → Tertiary (noise). Each Fulcrum Driver gets 1-2 Leading Tracking Indicators that feed the Monitoring Plan.

Cross-reference: `fundamental-change-screen/SKILL.md` (V7+), `assistant-portfolio-manager/SKILL.md`, `assistant-portfolio-manager/analysis-judgement-SOP.md` (governs memo authoring at Triaging/ESA/DD — updated 28-Apr-26 with authoring order, 70/30 time split, Notion note lookup, Opus mandate), `databases/` folder

---

## Memo Cover Sheet Standard (Jan 2023)

Every formal investment case analysis (ESA onwards) includes a standard cover sheet:
- **Stock ticker, company name, date, Watson version number**
- **Investment thesis (1-2 sentences):** What is the core case?
- **Key fulcrum driver:** What is the single most important driver?
- **Risk/reward profile:** Upside case, base case, downside case with multiples
- **3 key questions:** What would change the investment case?
- **Time horizon:** 18M, 4Y, "+infinity"?
- **Conviction rating (1-10):** Based on 8-element framework
- **Position sizing recommendation:** Based on conviction + resilience assessment
- **Monitoring plan:** What is tracked fortnightly? What would trigger exit?

This standardises the case and prevents analysis without conclusion.

## Team Decision Architecture (Sept 2023)

While Richard is sole decision-maker, when involving advisors/peers (Ed, James, Pedro):
- **Pre-decision:** Seek challenge on key assumptions (ACH format preferred)
- **During decision:** Listen to their evidence/concerns; form your own view
- **Post-decision:** Communicate your logic clearly; welcome pushback

Core principle: "Form your own judgment on every stock. Never abrogate to analyst." Richard has excellent track record of trusting own judgment even when disputed (Greggs example: Pedro concerned, Richard trusted analysis, stock up 25% YTD).

## Research Process Discipline Changes (2022-23)

1. **No analytical deep-dives as substitutes for exit decisions.** When a stock triggers deterioration signals, the 30-day shot clock runs. Using that time to "understand the company better" is avoidance. Default is zero; can be reopened with fresh conviction only.

2. **Complexity trap avoidance.** If you need >3 Excel tabs to understand the investment case, it's too complex. HQI cases are simple: what is the inflection? What drives 18M EPS? What's the fulcrum driver?

3. **Memo discipline.** Every ESA and DD must produce a formal memo (cover sheet + case). Rough notes don't count. Memo discipline forces clarity.

## Conviction Assessment: 8-Dimension Scoring

See `investment-strategy.md` → "Conviction Assessment — Eight Elements" for the full 8-element framework.

## Daily Execution Scoring

See `high-performance.md` → "Daily Execution Scoring" for the full 5-point daily scoring system.

## IAJA Synthesis — Automatic Stage Capstone (SOP)

**After completing any stage's research prompts, Watson automatically produces an IAJA Synthesis page.** This is non-optional and applies to every stage (IG, ESA, DD). It is the capstone of every stage's execution.

**What it does:**
- Synthesises findings from ALL source outputs produced during that stage into a single consolidated view
- Applies the IAJA framework: Information gathered → Analysis → Judgement → 2+ downstream actions
- Forms Watson's preliminary view on the stock at this stage — not just restating what the outputs said, but drawing out analytical implications and forming a judgement
- Proposes at least 2 concrete downstream actions (e.g., "progress to ESA," "park because X," "investigate KQ on Y," "run peer GTH," "schedule monitoring for Z")

**Format:**
- Single page per stage, however long it needs to be (use chunking protocol if >15K chars)
- Naming: `[W] {TICKER} ({Company Name}) - {STAGE} IAJA Synthesis [W] @ DD-Mon-YY — {one-sentence judgement}`
  - Example: `[W] OEM (OEM International) - IG IAJA Synthesis [W] @ 30-Mar-26 — Quality serial acquirer with solid Nordic niche but limited near-term catalysts; suggest park on short list pending Q1 earnings`
  - Source tag is [W] (Watson's synthesis), NOT [C] or [AS]
- Properties: IAJA = Information + Analysis + Judgement (all three)
- 30%+ sentiment highlighting
- Posted to Stock Notes DB (`collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2`)

**Scope by stage:**
- **IG:** Synthesises BD [C], BD [AS], CF [C], CF [AS] (4 source outputs)
- **ESA:** Synthesises all ESA-stage outputs (up to ~16 source outputs — sector primer, value chain, earnings history, guidance, premortem, etc.)
- **DD:** Synthesises all DD-stage outputs (KQ memos, management deep-dive, FX exposure, etc. — variable number)

## Parking Protocol

Parked names get:
- [-] prefix in Notion
- Placed on a specific watchlist (INTEREST level: Very short list through Uncategorised ATM)
- **Parking reason** logged (Stocks DB field — e.g., CEO quality, Near-term risks, No clear case)
- **Reassessment criteria** defined — specific, observable triggers that would reactivate the name (e.g., "revisit if share price falls below X" or "revisit post Q2 earnings")
- Removed from active research workflow but retained in squad for monitoring
- Watson monitors reassessment criteria on parked watchlist names and communicates status changes to Richard

---

## Initiating Investment Checklist (17-Step Gate Before Entry)

**Gene Pool & Standards Gate:**
1. Does new stock raise average quality of portfolio (>50th percentile)?
2. Cross-check against historical investing lessons — any errors being repeated?
3. Comfortable putting trade order to go straight to 8% (gut + head alignment)?

**Portfolio Construction Gate:**
4. If at 10 stocks max, which stock simultaneously exits? (1-in-1-out discipline)
5. Comfortable cannot reverse position in F3M? F6M? (conviction test)
6. Within maximum new positions/year (4-6 max)?

**Analytical Rigor Gate:**
7. Have you personally built a model?
8. Have you personally written a long memo (not analyst's)?
9. Risk memos from analyst + James (stress test views)?
10. Pre-mortemed the idea properly with team (noodled all issues)?
11. Re-read every memo, re-checked model, re-reviewed all primary research?
12. Are all your key questions genuinely answered? Honestly?

**Consensus & Calibration Gate:**
13. Head-gut concordance: What does gut say? Matches head analysis?
14. Have you resisted premature toe-holds before research is complete?
15. Have you run metacognition checklist (15+ strategic business model considerations)?

**Final Discipline Gate:**
16. Minimum one week percolation time after all final checks before investing (forced pause)
17. Chris (team member) must run checklist; minimum 30-minute review meeting before new investment

---

## Position Monitoring Checklist — Live Position Discipline

**Thesis Simplicity (Guardrail):**
- Never want theses getting more complex. Want them getting simpler.
- If thesis has added layers since entry, thesis is deteriorating.

**Alignment Check (Weekly/Fortnightly):**
- All indicators pointing same direction? (Best cases: data directionally aligned, reduces forecast dependency)
- Are most important indicators changing? (They often evolve; update tracking set quarterly)

**Tracking Indicators Setup:**
1. What are the 4-6 core tracking indicators for this position?
2. Are they SMART (specific, measurable, achievable, relevant, time-bound)?
3. Are they MECE (mutually exclusive, collectively exhaustive)?
4. Based on Superforecasting principles (observable, not analytical)?

**Active Monitoring (Monthly):**
1. How are leading fundamental tracking indicators changing?
2. How are leading market sentiment indicators changing?
3. Are all indicators pointing same direction? (If yes: deep holistic trust; if no: investigate divergence)
4. Hard Bloomberg data review monthly (earnings, guidance trends, covenant status)

**Tools & Execution:**
- Optionality plot updated quarterly
- 3-monthly pre-mortem review (would we still buy at current price?)
- Dashboard + Bloomberg terminal daily access
- 30-day deterioration shot clock (if 2+ indicators RED, default is reduce unless clear counter-evidence)

---

## Exit Proposal Memo SOP (When Considering Reduction/Exit)

**Step 1: All Reasons to Exit**
- Unstructured jumble initially: list all concerns comprehensively
- Performance vs. key drivers; performance vs. expected hypothesis
- Investigation: How might I be wrong? Is "Gentle Bull" manifesting but I'm distracted by transient issues?

**Step 2: Metacognition Checklist Validation**
- Run all metacognition checks (15+ business model / competitive / strategic considerations)
- Logic: "Slow is smooth. Smooth is fast" — invest thinking time upfront to avoid reactive mistakes

**Step 3: Proposed Position Monitoring Plan**
- Specific tracking indicators to follow going forward
- Probability of "Gentle Bull" manifesting — what would increase it?
- Be very specific (Who, what, when, how, why); aim to allocate minimal time going forward
- Define: Hard outcome triggers that would justify re-entry if exited

**Step 4: Move to Monitoring List?**
- If not exiting but reducing/moving to bench: why? Reassessment criteria?

**Step 5: Sign-Off Protocol**
- Both Richard and lead analyst sign off (like a contract)
- Both include detailed comments on rationale and disagreements
- Document any dissent clearly — disagreement is valuable input

---

## Metacognition Checklist — Strategic Business Analysis Framework

**Scope:** 15+ categories of business model, competitive, and strategic considerations that challenge every thesis.

**Core Categories:**

**1. Business Model & Competitive Strategy**
- Incumbent dilemma (are they defending against disruption or not?)
- Latent pricing power (can they raise prices without losing volume?)
- Latent growth/margin opportunities (greenfield expansion?)
- Fulcrum products (is the case dependent on one product/customer?)
- Moat strength (trust moat vs. structural moat; durability under attack?)
- Incentive alignment (management paid for right behaviors?)
- Culture/execution (culture eats strategy for breakfast; is culture top-tier?)

**2. Market Position & Dynamics**
- Red Queen/Darwin's Finches (hyper-competitive or defensible?)
- Market share change metrics (HHI; consolidation vs. fragmentation; speed of winners?)
- Relative winner when going gets tough (defensive quality in downturns?)
- Land of blind (weak competitors = easy wins, but is there a formidable entrant?)
- Competitive strategy (Sun Tzu: superior position vs. direct confrontation?)

**3. Value Chain & Scale Economics**
- Value chain analysis (where are profit pools? Is company in best position?)
- Scale economies (does bigger = better or just bigger?)
- Physical networks (fibre, railways, platforms — embedding creates moats?)
- Two-sided marketplace networks (buyers/sellers feedback loop?)
- Market cap vs. TAM (can genuinely 5x from here?)

**4. Growth & Reinvestment Runway**
- Reinvestment runway length & depth (how many years of compounding left?)
- Organic vs. M&A growth (can they grow organically or dependent on M&A?)
- Customer pick-and-choose vs. bundling (are they losing negotiating power?)
- High operating leverage implications (good when up, brutal when down?)

**5. Downside & Fragility Scenarios**
- Thin margins = tough businesses (are they running to stand still?)
- Customer concentration risk (top 3 customers >40%? High risk.)
- Regulation/patents as moat (fragile if policy changes?)
- High leverage + cyclical = double disaster (debt serviceability stress?)
- Strategic pivot vs. flip-flop flailing (are they adapting smartly or reactive?)

**6. Less Obvious Risks**
- Long periods of slow growth = red flag (is compounding exhausted?)
- Running to stand still (strong revenue, weak earnings growth?)
- Economic chokepoints (are there bottlenecks in supply chain they don't control?)
- Systemic risk (interconnected failures beyond their control?)
- "Hail Mary" strategies (is management out of ideas and making crazy bets?)
