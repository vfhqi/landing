# RESEARCHER TEMPLATE SUITE — Queries 15-22

**Created:** 14-Apr-26

This document indexes the 8 new research templates for DEEP DIVE (DD) and KEY QUESTION (KQ) queries. These templates standardise research workflows across a broad range of analytical tasks.

---

## TEMPLATE INDEX

### **Query 15: Insider/Expert Comments — AS ONLY**
**File:** `15-dd-insider-comments.md`

Extract and synthesise proprietary insights from insider commentary, expert network transcripts, management call analysis, and insider transaction patterns. Identify what insiders and industry experts are saying that isn't in headline numbers.

**Sections:**
- Management commentary analysis (tone shifts, hesitations, topic avoidance)
- Expert network insights (former employees, competitors, customers)
- Insider transactions (L12M buying/selling patterns)
- Conference/investor day commentary
- Customer/supplier/competitor perspectives
- Key quotes and unusual commentary
- Narrative vs reality check

**Min words:** 3,000  
**Source:** AlphaSense ONLY  
**Stage:** DD (resolve ESA questions)  
**Output:** 12-18 bullets per section, 30%+ highlighting

---

### **Query 16: Management and Governance Checks — Claude ONLY**
**File:** `16-dd-mgmt-governance.md`

Assess management quality, governance structure, board composition, compensation alignment, and governance red flags. Evaluate operator quality using "animal CEO" archetype framework.

**Sections:**
- CEO assessment (background, track record, leadership style, compensation)
- CFO assessment (financial discipline, transparency, guidance accuracy)
- Senior leadership team (depth, tenure, recent changes)
- Board composition and independence
- Compensation structure and alignment
- Governance structure and red flags
- Culture indicators (Glassdoor, LinkedIn, eNPS)
- Governance rating

**Min words:** 3,000  
**Source:** Claude ONLY (public sources, no sell-side)  
**Stage:** DD (assess manager quality)  
**Output:** 12-18 bullets per section, 30%+ highlighting

---

### **Query 17: FX Exposure — Claude ONLY**
**File:** `17-dd-fx-exposure.md`

Comprehensive FX risk analysis including revenue/cost currency mismatch, translation vs transaction exposure, hedging policies, and quantified sensitivity analysis.

**Sections:**
- Revenue by currency (geographic breakdown, mix trends)
- Cost by currency (natural hedges, mismatches)
- Translation exposure (reported earnings impact L3Y)
- Transaction exposure (economic impact)
- Hedging policy assessment
- Quantified sensitivity analysis (tables)
- Peer FX exposure comparison
- Macro FX outlook (N12-24M)
- FX as tailwind/headwind for thesis

**Min words:** 3,000  
**Source:** Claude ONLY (public filings, no proprietary)  
**Stage:** DD (quantify hidden earnings drivers)  
**Output:** 12-15 bullets + sensitivity tables, 30%+ highlighting  
**Note:** Originated from ChatGPT prompt (REFV01CGPT). Functional but flagged for future rewrite.

---

### **Query 18: CEO Research — AS ONLY**
**File:** `18-dd-ceo-research.md`

Deep research into the CEO specifically: background, track record at company and prior roles, leadership approach, investor perception, key-person risk. Rate CEO against "animal CEO" framework.

**Sections:**
- Career history and biography
- Track record at {COMPANY} (revenue, margin, strategic shifts, M&A, capital allocation)
- Track record at prior companies (pattern recognition)
- Leadership style and approach
- Sell-side and investor perception
- Compensation and alignment
- Key-person risk assessment
- CEO quality rating

**Min words:** 3,000  
**Source:** AlphaSense ONLY  
**Stage:** DD (assess execution capability)  
**Output:** 12-18 bullets per section, 30%+ highlighting

---

### **Query 19: Pre-mortem — AS + C (dual-source)**
**File:** `19-dd-premortem.md`

Ultimate stress test: assume the investment has failed at 18 months and work backward. Generate 10 distinct failure narratives, synthesise with meta-analysis. Apply ACH framework (YES, NO, FALSE FRIEND profiles).

**Sections (Part A — Failure Narratives):**
- 10 scenarios across: revenue risks, margin risks, execution risks, competitive risks, false-friend risks
- For each: narrative, early warning signals, plausibility rating, monitoring checklist, interaction effects

**Sections (Part B — Meta-Analysis):**
- Scenario clustering and interactions
- Probability-weighted failure assessment
- False friend detection (earnings beats that hide deterioration)
- Transmission mechanism test (thesis driver stress test)
- Historical parallels from track record
- Recommended monitoring checklist
- Overall thesis robustness and confidence rating

**Min words:** 4,000 per version  
**Source:** AS + C (dual-source; post separate memos)  
**Stage:** DD (confirm or disconfirm thesis)  
**Output:** 15-20 bullets per scenario + meta-analysis, 30%+ highlighting  
**Key feature:** FALSE FRIEND scenarios are most important (thesis appears to confirm but is deteriorating)

---

### **Query 20: CEO/CFO Meeting Prep — AS + C (DD stage)**
**File:** `20-dd-ceo-cfo-meeting-prep.md`

Preparation for a management meeting: financial-centric questions that walk the P&L, test the thesis, probe uncertainties. ≥15 questions across ≥6 themes. Each question is specific, testable, designed to REVEAL non-public information. ≥2 non-obvious questions (Concept A — WH Smith CEO archetype). ≥1 power-of-incentives probe. Cross-refs Q19 ACH matrix.

**Key distinction:** DD-stage template (per D-RSR-32 — relocated from ad-hoc into DD group). Dual-source [AS]+[C] default.

**Sections:**
- Executive summary (key findings)
- [Natural topic breakdowns based on question]
- Data gaps and research opportunities
- Second and third-order implications

**Min words:** 3,000  
**Source:** Ask Richard: [AS] only, [C] only, or both  
**Stage:** Any (IG, Triaging, ESA, DD)  
**Output:** Sections with 10-15 bullets, confidence ratings per section, 30%+ highlighting  
**Example KQs:**
- "Is the addressable market growing faster than consensus assumes?"
- "Are we in structural pricing pressure or cyclical?"

---

### **Query 21: KQ — Research (breadth-first) — AS + C [default dual]**
**File:** `21-kq-research.md`

Broad research into a specific key question: landscape mapping by dimension, data, sources, evidence. Explain everything known about a research-type KQ. Classify by confidence, identify data gaps, surface second/third-order implications via M/M/O test.

**Key distinction:** Research type = "what is the landscape?" vs Analysis type (Query 22) = "what is your judgment?" Dual-source [AS]+[C] DEFAULT per MEMORY.

**Sections:**
- Executive summary (conclusion first)
- Competing hypotheses (2-3 stated clearly)
- Evidence matrix (supports/contradicts each hypothesis)
- Evidence assessment (strength, confidence, alternatives)
- Key assumptions test
- Disconfirmation test (what would disprove this?)
- Probability assessment
- Transmission mechanism (for leading hypothesis)
- Strongest counterargument and response
- Final recommendation and confidence rating

**Min words:** 3,000  
**Source:** Ask Richard: [AS] only, [C] only, or both  
**Stage:** Any (IG, Triaging, ESA, DD)  
**Output:** Evidence matrix + probability assessment, 30%+ highlighting  
**Example KQs:**
- "Is the margin expansion sustainable or unsustainable?"
- "Will the CEO's new strategy work or fail?"
- "Is this a 'best friend' or a 'false friend'?"

---

### **Query 22: KQ — Analysis (ACH-disciplined) — AS + C [default dual]**
**File:** `22-kq-analysis.md`

Framework-driven analysis of a specific key question: ACH matrix structural spine (D-RSR-33), ≥3 competing hypotheses, M/M/O per hypothesis, multiple-truths-coexist synthesis section. Verbal verdict ("high/medium/low plausibility"). Per Concept B 3-check declaration.

**Key distinction:** Analysis type = "which competing hypothesis is most likely?" vs Research type (Query 21) = "what is the landscape?" Dual-source [AS]+[C] DEFAULT per MEMORY.

**Themes:**
1. Revenue drivers and visibility (backlog, pipeline, customer concentration, pricing trends, market share)
2. Margin trajectory and levers (gross margin, operating margin, mix, timing)
3. Capital allocation and FCF (capex discipline, M&A strategy, dividend/buyback, debt targets)
4. Competitive position and market dynamics (competition, advantage, switching costs, pricing power)
5. Key risks and execution challenges (supply chain, labour, regulatory, technology, concentration)
6. Thesis-specific questions (test core thesis assumptions)

**Min words:** 2,000  
**Source:** Ask Richard: [AS] only, [C] only, or both  
**Stage:** Any (typically ESA or DD when direct management access available)  
**Output:** 15-25 questions with context notes (what reveals, good vs bad answer, follow-up probe), 30%+ highlighting  
**Post-meeting:** Update Notion with actual responses, surprises, follow-ups needed

---

## EXECUTION WORKFLOW

### For any DD or KQ research task:

1. **Identify query type** (Q15-22)
2. **Determine source(s)** if not specified: ask Richard
3. **Populate placeholders** in prompt:
   - {TICKER}, {COMPANY}, {INDUSTRY}, {PEERS}
   - {THESIS_SUMMARY}, {KEY_QUESTIONS}, {KQ_TITLE}, {KQ_CONTEXT}, {KQ_OBJECTIVE}
   - {STAGE}, {STAGE_CONTEXT}
4. **Execute research** using specified source(s)
5. **Structure output** using template's OUTPUT STRUCTURE
6. **Highlight** 30%+ of memo in Notion (prioritise executive summaries, key findings, assessments)
7. **Post to Notion** with title convention: `[W] {TICKER} — {Query #} — {Brief Title} @ DD-Mon-YY`

### Highlighting Priorities (all templates):
- Executive summaries and key findings
- Risk assessments and red flags
- Quantified analysis (tables, probabilities, sensitivities)
- Judgement statements (ratings, confidence assessments)
- Monitoring recommendations

---

## SOURCE REFERENCE MAP

| Query | AS | C | Both | Notes |
|-------|-----|-----|------|-------|
| 15 | YES | — | — | Insider data proprietary |
| 16 | — | YES | — | Public governance data |
| 17 | — | YES | — | Filing-based FX analysis |
| 18 | YES | — | — | Sell-side CEO commentary |
| 19 | YES | YES | YES | Separate memos, reader synthesises |
| 20 | YES | YES | Ask | Research question, either/both |
| 21 | YES | YES | Ask | Analysis question, either/both |
| 22 | YES | YES | Ask | Meeting prep, either/both |

---

## INTEGRATION WITH EXISTING TEMPLATES

These 8 templates (Q15-22) join the existing 14 templates (Q1-14) in the researcher suite:

- **Q1-3:** IG stage (Business Description, Change Forces, Thesis Mapping)
- **Q4-7:** Triaging stage (Earnings Trends, Earnings Delivery, SS Commentary, KD Assessment)
- **Q8-14:** ESA stage (Business Model, Earnings History, Short Sellers, Value Chain Map/Analysis, Guidance Tracking, KD Assessment)
- **Q15-18:** DD stage (Insider Comments, Mgmt/Governance, FX Exposure, CEO Research)
- **Q19:** DD stress test (Pre-mortem)
- **Q20-21:** Cross-stage (KQ Research, KQ Analysis)
- **Q22:** Cross-stage (Management meeting prep)

All 22 templates follow the same structure: MISSION, CONTEXT, PROMPT ([AS] and/or [C] versions), EXECUTION.

---

## KEY DESIGN PRINCIPLES

1. **Consistency across templates:** Same structure, same audience context, same output requirements
2. **Audience first:** Every template centres on "concentrated long-only investor, 12-24M hold, 25%+ IRR target"
3. **Dual-source capability:** Most templates support both [AS] and [C] versions; reader selects source per task
4. **Specificity:** Prompts include detailed research areas, execution protocols, output structure
5. **Highlighting as standard:** All outputs require 30%+ highlighting in Notion (enforces synthesis)
6. **No open loops:** Every template produces actionable, structured output ready for decision-making

---

## NEXT STEPS

- File all 8 templates in `/memory/skills/researcher/templates/`
- Update master researcher skill README to index all 22 queries
- In CLAUDE.md, update researcher skill reference: "22 query templates covering IG through DD, cross-stage KQ analysis, and management meeting prep"
- When executing queries, reference this document for context/execution notes

