# Thematics Research SOP
<!-- [W] Created 15-Apr-26. Referenced by RESEARCHER SKILL-V2.md (Query #23). -->

## Purpose

Defines how the RESEARCHER role researches and populates thematic overlays for portfolio construction. Thematics are macro/strategic trends that create systematic beneficiary/at-risk profiles across the investment universe. This SOP governs the ad hoc research workflow; the APM role then integrates the output into stock analysis and capital allocation decisions.

---

## When to Run

- **New thematic defined:** Richard identifies a new macro theme (e.g., Iran conflict, AI disruption, bear market positioning). RESEARCHER runs Query #23 immediately.
- **Quarterly refresh:** At the start of each quarter, RESEARCHER reviews all active thematics and runs refresh research on any where the landscape has materially changed.
- **Regime change:** Material shift in macro environment (e.g., war escalation, central bank pivot, sector rotation) triggers ad hoc refresh of affected thematics.
- **Richard requests it:** Any explicit instruction to research or update a thematic.

---

## Inputs

1. **Thematic name and definition** — from Richard or from `memory/context/active-thematics.md`
2. **Existing research** — prior thematic research in Notion Journal, Iran analysis (Mar 2026), sector notes
3. **Current pipeline** — `memory/projects/pipeline.md` for context on which stocks are in scope
4. **Investment strategy** — `memory/context/investment-strategy.md` for quality framework, setup profiles

---

## The 7 Deliverables Per Thematic

For each thematic, RESEARCHER produces:

| # | Deliverable | Description | Length |
|---|------------|-------------|--------|
| 1 | **Definition** | What the thematic IS — in 2-3 sentences. Transmission mechanism to corporate earnings. | 50-100 words |
| 2 | **Beneficiary Summary** | Who wins — in 1-2 sentences. The elevator pitch. | 30-60 words |
| 3 | **At-Risk Summary** | Who loses — in 1-2 sentences. The elevator pitch. | 30-60 words |
| 4 | **Beneficiary Attributes** | Detailed list of characteristics that make a company a beneficiary. Operational, financial, strategic attributes. Sector examples. | 300-600 words |
| 5 | **Beneficiary Probable Setups** | What stock-level patterns to look for. Thematic-specific setup descriptions. Where natural, map to FCS 6 setups. | 200-400 words |
| 6 | **At-Risk Attributes** | Detailed list of characteristics that make a company vulnerable. Operational, financial, strategic attributes. Sector examples. | 300-600 words |
| 7 | **At-Risk Probable Setups** | What stock-level patterns emerge for at-risk names. Thematic-specific. FCS mapping where natural. | 200-400 words |

**Total per thematic:** 1,200-2,200 words of structured output.

---

## Execution Flow

### Step 1: Template Preparation

1. Read `templates/23-thematic-research.md`
2. Fill placeholders: `{THEMATIC_NAME}`, `{THEMATIC_DEFINITION}`, `{BENEFICIARY_HINT}`, `{AT_RISK_HINT}`, `{GEOGRAPHIC_FOCUS}`
3. Richard's initial hints (beneficiary/at-risk summaries) go into the template as priors — the research validates, expands, and challenges them

### Step 2: Dual-Source Execution

**Claude [C] — Sonnet native:**
- Launch as parallel sub-agent with filled template
- WebSearch extensively for: macro analysis, sector impact studies, sell-side thematic reports, historical parallels, earnings sensitivity data
- Focus on EUROPEAN-LISTED companies and sectors
- Produce all 7 deliverables in a single structured memo

**AlphaSense [AS] — Haiku submission:**
- Extract [AS] prompt section from template
- Submit via Haiku AS Submission Agent (standard protocol per Research Execution SOP)
- AS searches: broker thematic research, expert calls on sector impacts, company-specific commentary on the thematic, earnings call mentions
- Wait 45-60 min → extract → process

### Step 3: Synthesis and Population

1. On [C] return: validate output (all 7 sections present, European focus, attribute lists are specific not generic)
2. On [AS] extraction: validate same criteria
3. **RESEARCHER synthesises** [C] and [AS] outputs into the final 7 deliverables — this is NOT a copy-paste job. The synthesis:
   - Takes the strongest attributes from each source
   - Resolves contradictions (flag if material)
   - Ensures attributes are ACTIONABLE (can be matched to a stock's characteristics)
   - Ensures setups are SPECIFIC (not generic "quality companies do well")
4. Write synthesised output directly into `memory/context/active-thematics.md` under the relevant thematic

### Step 4: Notion Posting

- Post a Journal entry with CHECKLIST/SOP designation
- Title: `[W] Thematics Research — {Thematic Name} — {Summary} [C+AS] @ DD-Mon-YY`
- Include: all 7 deliverables, source attribution, key judgements highlighted
- 30%+ highlighting (green = beneficiary signals, red = at-risk signals, yellow = contested/uncertain)
- Tag: Thematic Overlay, Portfolio Construction, Capital Allocation

### Step 5: APM Handoff

- Notify APM that thematic research is complete
- APM runs Mode 1 batch (portfolio impact matrix) or integrates into next FCS cycle (Mode 2)
- RESEARCHER does NOT score stocks against thematics — that's APM's job

---

## Quality Standards

1. **European focus.** All sector examples and attribute lists must be grounded in European-listed companies. US/global context is fine for framing but the actionable output targets the £5-50bn European universe.
2. **Attribute specificity.** "Companies with pricing power" is too generic. "Companies with contractual price escalators linked to CPI or input cost indices, renegotiated annually or more frequently" is specific enough to match against a stock.
3. **Setup specificity.** "Quality companies" is useless. "Regulated utility with 5Y+ tariff visibility, <3x net debt/EBITDA, and domestic-only revenue base" is actionable.
4. **Transmission mechanism.** Every attribute must have a clear path to EPS impact. "Oil-linked COGS" → "margin compression if oil rises 20%+" → "EPS downside risk." If the transmission is unclear, flag it.
5. **Challenge Richard's priors.** If the research contradicts Richard's initial hints (beneficiary/at-risk summaries), say so explicitly. Strong views, weakly held.
6. **Historical parallels.** Where possible, cite prior episodes (2008 oil spike, 2014 oil crash, COVID supply shock, 2022 energy crisis) and what worked/didn't.
7. **No hedging.** Every deliverable ends with a clear view. Uncertainty is expressed through confidence levels, not by avoiding conclusions.

---

## Interaction with Other SOPs

- **Research Execution SOP (V2):** Governs [C] and [AS] execution mechanics. This SOP governs thematic-specific content.
- **Notion Posting SOP:** Governs posting mechanics. Thematic research follows same posting rules.
- **APM SKILL §Thematics Overlay:** Governs how APM consumes and operationalises the output.
- **FCS SOPs:** Thematic alignment is considered during FCS Analysis (deliverable #11 Risk Assessment, Pillar III/VI).

---

## Key Files

| File | Purpose |
|------|---------|
| `memory/context/active-thematics.md` | Living codified file — thematic definitions + stock matrix |
| `templates/23-thematic-research.md` | Self-contained agent template for Query #23 |
| `memory/skills/researcher/SKILL-V2.md` | Master RESEARCHER skill (Query #23 in master table) |
| `memory/skills/assistant-portfolio-manager/SKILL.md` | APM skill (§Thematics Overlay) |
