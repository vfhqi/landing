# Query 1: Business Description — AlphaSense Only

> **CHAT-ITERATION DRAFT — v2 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/01-ig-bd.md`. Carries the **BB#2 overlay** per Path 2 (D-RSR-6) — ~37 of BB#2's 70 CQs covered, weighted to load-bearing RAs. v2 adds four blocks per D-RSR-22: in-memo QC Audit panel, QC Commentary, SS breadth gate (5L Hard) + Expert breadth (5M Warn), AS prompt-side breadth instruction. All v1 content preserved verbatim — purely additive.

> **⚠️ EXCEPTION TO THE NO-COMPANY-DESCRIPTION RULE.** This query (#1 IG BD) IS the canonical business-description memo. Subsequent queries (#2-7, #9-19) explicitly omit company description because they assume this memo has been read. Do NOT condense the business-description content. Q8 (ESA BM/Sector Primer) is the deeper successor at ESA stage; Q1 establishes the foundation.

---

## MISSION

Write a comprehensive business description memo for {COMPANY} ({TICKER}). This is an Ideas Generation (IG) stage output — the goal is to build a thorough understanding of what the business does, how it makes money, its financial profile, industry context, and forward outlook. The memo should enable a portfolio manager to quickly assess whether this stock warrants further research.

Output: comprehensive memo, target {WORD_TARGET} words (default ~7,000w; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section. **BB#2 coverage map** at end (validator-readable; ≥30 of BB#2's 70 CQs addressed/cross-ref).

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated, long-only equity investor (5-15 positions) focused on UK/European stocks, $5-50bn market cap. Holds for 12-24 months. Looks for businesses experiencing positive improvements in revenue growth rates, margins, EPS, guidance, strategy, growth ambition, and sentiment. Singular obsession: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

The reader values: demonstrated pricing power, customer loyalty, execution track record, revenue optionality (M&A, geographic, product, pricing), operator quality ("animal CEO" archetype), supply chain tightness. Thematically agnostic — no sector dogmatism.

**At IG stage, the reader is pattern-matching:** does this look like it could fit a recognisable setup profile? Is something interesting happening? Any immediate red flags? The IG BD is the foundation memo — every subsequent query depends on this output being substantive.

**What downstream uses this output:** APM A&J reads this memo to populate Pillar P4 (Foundation Quality) — particularly **BB#2 Required Foundation Quality** (the BUSINESS QUALITY group). BB#2 spans 6 TCs / 19 RAs / 70 CQs covering Operator quality, Advantaged business + SRCA, Value chain, Industry structure, LT growth, and Paradigm fit. Q1 covers the **load-bearing subset** of BB#2 (~37 CQs per Path 2); Q8 (ESA BM/Sector Primer) covers all 70 at deeper level. Q1 also feeds Pillar P3 (IC#1 Required Case Outputs) where the financials sections directly inform RA1 Longevity, RA2 Growth, RA3 Improving financials.

The memo also surfaces on the RESEARCH STAGES dashboard tab. Format-aware structure (BLUF + signposted bullets + peer anchors + ❌/⚡ markers + BB#2 coverage map) makes APM's grading mechanical rather than reconstructive. Filler prose actively wastes APM's reading attention; substantive bullets compound it.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in the SECTIONS TO COVER block below must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*. A parent bullet ≤30 words plus 2-4 sub-bullets ≤25 words each carries 100-150 words of analytical content in a scannable form — same depth as a paragraph, vastly more useful for the reader.

If in doubt, write more substantive bullets rather than longer ones. A section with 12 substantive parent bullets (each with sub-bullets) is far more valuable than a section with 6 long bullets. Completeness and analytical rigour are more important than conciseness. Do not sacrifice depth for brevity.

**The test:** would Richard learn something from this memo that he couldn't get from a sell-side initiation note? If the bullet just restates the company's own description, it's filler. If it triangulates across sources, surfaces a base-rate anchor, or flags an outlier — that's analytical content. Trust your judgement; include anything that might be interesting to the reader.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1 (only if the model insists on context).
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.** Splitting a 60w parent into a 30w parent + two 25w sub-bullets is mandatory, not optional.
- **One analytical dimension per bullet.** Bullets that mix timing + magnitude + significance get split into separate bullets, each with its own signpost prefix.
- **Signpost prefixes** (demi-bold + colon) on every parent bullet in body sections. Vocabulary specified per-section below — and licence to invent additional signposts where you spot analytical patterns the canonical list doesn't cover (see SIGNPOST DISCRETION clause below).
- **Peer / base-rate anchor** on every quantitative claim. Specific peer name OR sector median — never a number in isolation. Failure mode to avoid: "company grew at 17% CAGR" (unanchored). Required form: "company grew at 17% CAGR — 2.0x sector pace of 8.4%."
- **J-front verdict bullet** at the top of every section. Replaces grading. NOT a grade (RESEARCHER doesn't grade — that's APM territory). Instead: a verbal synthesis verdict, ≤30w, signpost-prefixed, peer-anchored. Example: "Net signal: revenue model heavily concession-dependent — 71% regulated airport fees vs sector median 45%."
- **Per-section sceptical bullet** at the bottom of every section. Inverts the section's findings. Frames open: what's the bearish counter-read, and through what mechanism could it materialise?
- **IAJA suffix tags** on every parent bullet: `[#J]` judgement / `[#A]` analysis / `[#I]` information.
- **❌ inversion marker** on findings clearly worse than peer median. RESEARCHER does NOT grade these — APM does. RESEARCHER's job is to surface them with anchor.
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (top/bottom 5% of peer group on some dimension), (b) deliberately-weird signals (qualitative oddities the operator hasn't explained, cross-roads exposures the consensus is ignoring, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo. Archetype: a non-traditional CEO (e.g. WH Smith's CEO appointed from a different industry asking unconventional retail-format questions) is itself a ⚡ signal even before any quantitative anomaly surfaces.
- **Inline highlights** (green / yellow / red phrase-level spans) on the specific carrying phrase, NOT the whole bullet.

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Each section below lists a canonical signpost vocabulary. Use it where applicable — these are the labels Richard and APM read fluently across stocks, so cross-stock comparison stays mechanical. Where you spot an analytical pattern not covered by the canonical list, you have explicit licence to coin a new signpost label. Three guardrails on invented signposts:

1. **Canonical first.** If a listed signpost fits the bullet, use it — don't reinvent.
2. **Length cap: ≤4 words**, demi-bold + colon format. Long invented signposts break scannability.
3. **Single analytical dimension.** One lens per signpost. Compound signposts get split into multiple parent bullets, each with its own signpost.

Invented signposts are logged in the QC footer (`Invented signposts: "Concession bidding cycle:", "Tariff erosion path:"`) so vocabulary drift across memos can be reviewed and the canonical lists consolidated over time.

### Memo skeleton

```
1. METADATA HEADER (you populate)
   Ticker, company, query name, stage, source, generated date, target words.
   metadata.json: write at completion. Memo will not post without it.

2. KEY FINDINGS (BLUF)
   5-10 parent bullets. Each ≤30w. J→A→I order. Peer-anchored.
   The "skim layer": reader who reads nothing else gets the picture.

3. BODY SECTIONS §1-§5 (per SECTIONS TO COVER below)
   Each section opens with a J-front verdict bullet.
   Each section ends with a sceptical bullet (open-framed).
   Bullets between: signposted, peer-anchored, IAJA-tagged.
   Sections §1-§4 carry the BB#2 overlay; §5 is the future-orientation cap.

4. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
   0-5 bullets surfacing the strongest cross-cutting bearish counter-reads.
   Cross-references which section each came from.

5. AGGREGATE OUTLIERS (⚡)
   0-3 bullets. Genuinely unusual data points only.

6. BB#2 COVERAGE MAP (REQUIRED — validator-readable)
   Structured table mapping each BB#2 CQ this memo addresses to its location.
   Q1 threshold: ≥30 addressed/cross-ref entries from BB#2's 70 CQs.

7. QC FOOTER (auto-generated from metadata.json)
   Source attribution, word counts, peer-context density, signpost coverage,
   BLUF presence, J-front ordering check, BB#2 coverage count,
   invented signposts log, quality_flag if any.
```

---

## SECTIONS TO COVER

The five body sections below are the natural narrative arc of an IG Business Description — General → Company Details → Industry Context → BB#2 Foundation Quality (NEW) → Future. The BB#2 overlay is concentrated in §4, but BB#2 elements thread through §1-§3 as well — the coverage map at the end of the memo names every CQ this memo addresses across all sections.

### §1 — General (description, financials, peer comparison)

**Open with J-front verdict bullet:** Net signal on what {COMPANY} is, the materiality of its scale, and how its financial profile compares to peers — ≤30w.

**Canonical signpost vocabulary:** "Description:", "Strategic objective:", "Organisation:", "Listing:", "Financials snapshot:", "Revenue:", "Margins:", "Cash conversion:", "Capital intensity:", "Returns (ROIC/ROCE):", "Peer comparison:", "Capital allocation:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Description.** What the company does, why, and how. Financial and strategic objectives, strategic priorities and strategy. Not just what the company claims, but what it actually does down to a business level. How the company is organisationally structured.
- **Minimum criteria check.** Current share price. Listing currency and reporting currency. Tabular: average share price, market cap, EV, shares traded, value traded in listing currency each month for ~last two years. Line chart if possible.
- **Financials — tabular.** Last 8-10 years P&L, balance sheet, free cash flow. Last 3 years semi-annual or quarterly. Include: Revenue, total + organic/constant currency growth, M&A/divestiture contribution. Gross margins, cost margins, COGS. Operating costs broken down. EBITDA + margins, depreciation, amortisation of intangibles (separately for acquired intangibles). Adjustments with sub-categories. Operating profit + margins. Reported AND adjusted EBITDA, EBIT, net income. Reported AND actual tax expense. Interest costs + average rates. Gross financial debt + total debt with breakdown. Lease accounting impact (P&L + BS). Cash + cash-like items. Net financial debt. Seasonal NWC + net debt patterns. NWC as % of sales, receivables/inventory/payable days. Capex breakdown (maintenance vs growth). Differences between equity FCF + net income. Equity AND unlevered FCF. Off-balance-sheet liabilities. Operating lease expense + capitalised leases. Company-specific terminology. ROTC + ROIC. Dividends, buybacks, share issuance.
- **Financials — industry comparison.** Each line item vs normalised ratios/levels for {PEERS} and the industry. Explain differences — what might cause company metrics to trend toward industry averages? Discuss unit costs, fixed-cost operating leverage, capital intensity.
- **Financials — analysis.** Developments, causes, changes for each line. Insights, analysis, creative perspectives on the "why." Discuss unit costs, operating leverage, capital intensity. Capital allocation framework, philosophy, behaviour — particularly around share issuance/repurchasing.

**Coverage:** 15-20 parent bullets + sub-bullets across the five analytical lenses. Tables encouraged for the financials block (tabular form is itself a peer-anchor mechanism). Each peer comparison gets explicit treatment.

**End with sceptical bullet:** "What's the bearish counter-read on {COMPANY}'s financial profile? Through what mechanism might headline numbers be flattered (M&A, FX, accounting changes, one-offs)? What hidden capital intensity might be lurking?"

---

### §2 — Company Details (revenue model, business model, recent delivery, internal change)

**Open with J-front verdict bullet:** Net signal on revenue model concentration, business model strength, and recent execution track record — ≤30w.

**Canonical signpost vocabulary:** "Revenue source:", "Revenue mix:", "Geography:", "End-market:", "Cyclicality:", "Predictability:", "Driver count:", "Competitive advantage:", "Strategic objective:", "Secular trend:", "Customer behaviour:", "NPS:", "Churn:", "Switching cost:", "Lock-in:", "Scale economy:", "Operating leverage:", "Recent delivery:", "Internal change:", "Leadership change:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Revenue model.** Where revenue comes from. Geographic markets, business units, products — revenue split. How revenue is generated. Different revenue/business/sales models across geographies or units. Macro-sensitivity, cyclicality, predictability. Are revenues influenced by few or many drivers? Split by BU where relevant.
- **Business model — summary.** How the company makes money. Competitive advantages. Strategic objectives and priorities.
- **Structural / secular demand trends.** Forces shaping demand at industry level, applied to {COMPANY}'s revenue mix.
- **Business model — customer side.** Competitive advantages related to customers/products. Customer satisfaction, NPS, churn. Customer metrics, revenue per customer trends. Loyalty. Purchasing behaviour, lock-in, switching costs, search costs. How this has trended. Disruptions to customer purchasing patterns.
- **Business model — economies of scale.** Scale advantages, fixed-cost operating leverage, relevance of scale in this industry — does scale enable better products, generate competitive advantages, or generate higher margins/returns?
- **Recent delivery — last three years.** What the company delivered, and why. Unpack in detail.
- **Internal change — L12M and N3Y.** Leadership/management changes, corporate strategy, strategic priorities, financial goals, asset sales, M&A, partnerships, JVs, activism, standards/values.

**Coverage:** 15-20 parent bullets + sub-bullets. The customer-side analysis is the most load-bearing — moats live here. The internal-change analysis feeds directly into BB#2 TC1 Operator (§4 below) — names + dates + actions.

**End with sceptical bullet:** "What's the bearish read on {COMPANY}'s revenue model and execution? Through what mechanism might the apparent moat be brittle? What might cause the recent delivery track record to break?"

---

### §3 — Industry Context (peer comparison, structure, macro + non-macro change)

**Open with J-front verdict bullet:** Net signal on industry structure, competitive intensity, and external forces shaping {COMPANY}'s addressable market — ≤30w.

**Canonical signpost vocabulary:** "Peer divergence:", "Market structure:", "Concentration:", "Top 5 share:", "Distribution curve:", "Competitive intensity:", "New entrant:", "Disruption:", "Disintermediation:", "BtE:", "Barrier to exit:", "Supplier returns:", "Distributor returns:", "Customer returns:", "Macro shift:", "Regulatory shift:", "Political shift:", "Thematic trend:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Vs comparable peers.** How the §1-§2 analysis differs vs {PEERS}, and why.
- **Industry structure and value chain dynamics.** Changes in market structure. Politicians, regulators, suppliers, distributors. Competition, competitive intensity, new competitors, disruption, disintermediation. BtE and barriers to exit. Returns/margins of suppliers, competitors, distributors, customers (if B2B).
- **External macro changes.** Influencing revenue and margins over L12M and plausibly N36M. Go beyond company commentary — use sell-side, peers, other data sources.
- **External non-macro changes.** Regulators, political, competitor intensity, disruption, thematic trends, over L12M and plausibly N36M.

**Coverage:** 12-18 parent bullets + sub-bullets. Industry structure (concentration ratios, top 5 share, distribution curve) gets explicit numerical treatment — these are BB#2 TC4 inputs. Value chain dynamics get explicit treatment of supplier + distributor + customer power and returns — these are BB#2 TC3 inputs.

**End with sceptical bullet:** "What's the bearish cross-cutting read on industry context? Through what mechanism might the structural advantages erode? What disruption forces might be materially under-priced?"

---

### §4 — BB#2 Foundation Quality (NEW — load-bearing for APM grading)

> **This section carries the BB#2 overlay.** BB#2 is "Required Foundation Quality" — APM's BUSINESS QUALITY group spanning 6 TCs / 19 RAs / 70 CQs. Q1 covers ~37 of the 70 CQs at IG-appropriate depth (peer-anchored statement of fact, not grading). Q8 (ESA BM/Sector Primer) covers all 70 at deeper level. APM grades; RESEARCHER provides peer-anchored facts.

**Open with J-front verdict bullet:** Net signal on {COMPANY}'s foundation quality — operator strength, advantaged business depth, value-chain favourability, industry structure support, in ≤30w.

This section is structured into FIVE thematic sub-blocks (§4.1 through §4.5), each mapping to a BB#2 TC. RESEARCHER signposts at thematic level only — DO NOT signpost at CQ/RA/TC level (that's APM territory per D-RSR-5).

#### §4.1 — Operator (BB#2 TC1: Great Operator)

**Canonical signpost vocabulary:** "Operator:", "Strategic ambition:", "Strategy fit:", "CEO:", "Leadership team:", "Resourcing:", "Culture:", "Guidance posture:", "Communication clarity:", "Capital allocation:", "Track record:", "Outlier standards:", "Shareholder alignment:", "Buyback discipline:", "Governance:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Strategic direction: what is the ambition (growth as priority? outcompete? innovate?), and is the strategy congruent with the ambition (mid-term moat widening + dynamic strategy across plausible environments)? Cover BB#2 RA1 (CQ1, CQ2).
- CEO + leadership: assess CEO calibre via action not conjecture; quality of leadership team; whether hiring is a top CEO priority; resourcing of the broader business (well-invested, ant-colony resilience); culture + alignment (Lifco / Avanza / Ryanair archetype); guidance posture (conservative buffer?); communication clarity. Cover BB#2 RA2 (CQ3-CQ8).
- Track record + behaviour: high-RONIC capital allocation; acts-not-talks delivery record; outperformance during difficult environments; outlier standards driving higher/faster/better; shareholders-first orientation; dynamic SBB usage (capital allocator not just operator); prudent governance/scaffolding. Cover BB#2 RA3 (CQ9-CQ15).

**Coverage:** 8-12 parent bullets + sub-bullets across the three RAs. Specific CEO names + dates + actions where available. Where data is thin or out-of-scope for IG depth, flag with explicit "ESA depth — covered in Q8" cross-ref.

#### §4.2 — Advantaged Business + SRCA (BB#2 TC2: Advantaged business + widening SRCA)

This is the **largest single BB#2 sub-block** (5 RAs / 27 CQs). Q1 covers RA4 (MOAT) and RA6 (GENERATE) in full; RA5 (OPERATE), RA7 (gravitational pull), RA8 (improvement scope) summarised at high level only with explicit ESA-depth cross-ref.

**Canonical signpost vocabulary:** "Customer moat:", "Production moat:", "Scale moat:", "Regulatory moat:", "Culture moat:", "Relative scale:", "TAM:", "SCU:", "RSCU:", "Pricing power:", "Scale economies shared:", "Revenue growth:", "Capex growth:", "RONIC:", "FCF conversion:", "ROCE:", "ROTC:", "Gross margin:", "EBIT margin:", "Operating leverage:", "Tax leakage:", "Gravitational improvement:", "Improvement scope:", "Peer precedents:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **MOAT (RA4):** Customer-related moats / production-related moats / scale advantage moats / regulatory + political moats / culture + knowledge moats / high relative scale (revenue, FTE etc.) / large realistic TAM facilitating 12-20% pa growth. Cover BB#2 RA4 (CQ16-CQ22) — all 7 CQs in full.
- **OPERATE (RA5) — high-level only at IG:** Briefly note SCU + RSCU + pricing power signals; flag for ESA depth in Q8. Cover BB#2 RA5 (CQ23-CQ26) at summary level.
- **GENERATE (RA6):** 12-20% EPS growth + revenue growth status; capex/opex deployment scope at high RONIC for 3-5 years; high post-tax RONIC (25-30%+); high NI to FCF conversion (80%); post-tax ROCE 15%+; post-tax ROTC 30%+; high gross margins; solid EBIT margins (20% solid / 25%+ great); fixed-cost operating leverage; low tax rate (sub-30%) or other EPS leakage. Cover BB#2 RA6 (CQ27-CQ36) — all 10 CQs in full.
- **Gravitational pull (RA7) — high-level only at IG:** Briefly note whether gravitational/mechanical forces (not heroic dynamism) drive SRCA improvement vs peers. Cover BB#2 RA7 (CQ37-CQ38) at summary level.
- **Improvement scope (RA8) — high-level only at IG:** Briefly note peer precedents + plausibility of mid-term financial improvements. Cover BB#2 RA8 (CQ39-CQ42) at summary level.

**Coverage:** 18-25 parent bullets + sub-bullets across the five RAs. RA4 (MOAT) + RA6 (GENERATE) get full treatment — these are the core BB#2 inputs RESEARCHER must surface at IG. RA5/RA7/RA8 get explicit "ESA depth — covered in Q8" cross-ref where light.

#### §4.3 — Value chain (BB#2 TC3: Favourable + improving value chain dynamics) — high-level at IG

Q1 covers RA9 (demand) + RA10 (competition) at high level; RA11 (disruption), RA12 (political/regulatory), RA13 (supplier side) explicit cross-ref to ESA depth in Q8.

**Canonical signpost vocabulary:** "Customer demand:", "Route to market:", "Existing competition:", "Adjacencies entering:", "Vanilla new entrant:", "Innovative new entrant:", "Substitute:", "Disruption force:", "Regulatory SWOT:", "Political SWOT:", "Supplier SWOT:". Invent where pattern warrants.

**Analytical sub-questions to address (high-level only at IG):**
- **Demand side (RA9):** Customer demand strength/robustness and route-to-market dynamics. Cover BB#2 RA9 (CQ43-CQ44).
- **Competition (RA10):** Existing competition + adjacencies entering + vanilla new entrants + orthogonal/innovative new entrants + substitutes. Cover BB#2 RA10 (CQ45-CQ49).
- **Disruption / political / supplier (RA11-13):** Brief note + ESA-depth cross-ref. Cover BB#2 RA11-RA13 (CQ50-CQ53) at summary level.

**Coverage:** 6-10 parent bullets + sub-bullets across the value chain RAs. Most of this content also lives in §3 Industry Context — DO NOT repeat verbatim; either move §3 content here under signpost coverage, or cross-reference §3 in the BB#2 coverage map.

#### §4.4 — Industry structure (BB#2 TC4: Supportive / concentrated industry structure) — partial at IG

Q1 covers RA14 (concentration) in full; RA15 (gravitational pull), RA16 (competitor attitudes), RA17 (competitiveness trends) at summary level with explicit ESA-depth cross-ref.

**Canonical signpost vocabulary:** "Industry rank:", "Top 5 share:", "Distribution curve:", "Share stability:", "New entrant share:", "Largest competitor:", "Most advantaged:", "Benign-ness:", "Shark attack:", "Volume vs ROCE:", "Trend direction:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Concentrated existing structure (RA14) — full:** This company #1 or #2? Top 5 share >30%? Steep distribution curve (top 5 = 5x share of #6-10)? Cover BB#2 RA14 (CQ54-CQ56) — all 3 CQs.
- **Concentrating gravitational pull (RA15) — summary:** Stability of share over time; new entrant share; consolidation toward largest + most advantaged. Cover BB#2 RA15 (CQ57-CQ60) at summary level.
- **Competitor attitudes (RA16) — summary:** Benign-ness; MOL stability; shark attack risk; volume-vs-ROCE prioritisation. Cover BB#2 RA16 (CQ61-CQ64) at summary level.
- **Competitiveness trends (RA17) — summary:** Positive or negative trends. Cover BB#2 RA17 (CQ65) at summary level.

**Coverage:** 5-8 parent bullets + sub-bullets. Concentration ratios (numerical) get explicit treatment.

#### §4.5 — LT growth + Paradigm fit (BB#2 TC5 + TC6) — summary only

**Canonical signpost vocabulary:** "Adjacency:", "Volume secular:", "Pricing secular:", "GDP+:", "Paradigm fit:". Invent where pattern warrants.

**Analytical sub-questions to address (summary-level only):**
- **LT growth (RA18) — summary:** Brief note on adjacencies, structural volume demand, pricing-vs-cost trajectory, sector-vs-GDP growth. Cover BB#2 RA18 (CQ66-CQ69) at summary level. Detailed treatment in Q8 + Q23 thematic.
- **Paradigm fit (RA19) — summary or skip:** Cross-ref to Q23 thematic if present; otherwise brief note. Cover BB#2 RA19 (CQ70) at summary level or explicit skip in coverage map.

**Coverage:** 2-4 parent bullets total across both TCs.

**End §4 with sceptical bullet:** "What's the bearish read on {COMPANY}'s foundation quality? Through what mechanism might operator quality, moat strength, or industry structure prove weaker than the IG-depth analysis suggests? What ESA-depth investigations should be flagged as priorities for Q8?"

---

### §5 — Future (predictability, risks, L12M momentum)

**Open with J-front verdict bullet:** Net signal on what's plausibly changing over the N36M horizon and how predictable it is — ≤30w.

**Canonical signpost vocabulary:** "Predictability:", "Risk:", "Technical:", "MA:", "Volume:", "Price move:", "EPS revision:", "Price target:", "SS rating:", "SS narrative:", "Delivery vs guide:", "Peer momentum:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Predictability of changes** occurring/set to occur over N36M.
- **Risks** to the company's strategic plans being realised.
- **Changes over the L12M** in: technicals (MAs, volume, price moves vs longer-term history); SS financial forecasts (EPS focus + EBIT, EBITDA, revenue); SS price targets and ratings (pay attention to hold/sell-rated analysts); SS narrative, tone, focus in reports and earnings call Q&A (particularly hold/sell analysts); delivery vs guidance and SS expectations; fundamental + share price performance of {PEERS} (particularly revenue growth rates). Note which SS analysts are included.

**Coverage:** 8-12 parent bullets + sub-bullets. SS revisions list (which analyst, when, magnitude, direction) is mandatory. Peer fundamental + price performance in tabular form preferred.

**End with sceptical bullet:** "What's the bearish synthesis on {COMPANY}'s forward outlook? Through what mechanism might predictability collapse? What might invalidate the recent SS revision pattern? What peer-relative weakness might be forming?"

---

## AGGREGATE BLOCKS (after §5)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly worse than peer median or sector base rate.

**Format:** `❌ Signpost: finding statement. Peer anchor. [Cross-ref: §X]`

**Example:** `❌ EBIT margin: 12% vs peer median 22% — among bottom-3 of 12-peer infrastructure cohort. [Cross-ref: §1, §4.2]`

RESEARCHER does NOT grade these. Surface, anchor, cross-reference. APM grades.

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design — if every memo flags 5+ outliers, the marker is meaningless.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `⚡ RARE: EBITDA margin: 59.3% vs sector median 28% — top-decile globally; only one other listed airport operator exceeds 50%. [Cross-ref: §4.2 GENERATE]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel into the memo at post time. RESEARCHER does NOT author the structured table — the validator computes every metric. RESEARCHER DOES author the Qualitative Commentary block immediately below.

The panel is plain-text-with-markdown. Visual styling (status pill colours, summary-bar layout, gate-table CSS) is owned by the SA - Ratings Dashboard project (D-RSR-21) and applied at render time downstream of this memo.

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS]
**Stage:** IG
**Generated:** DD-Mon-YY

### Summary
| Metric | Value | Notes |
|---|---|---|
| Word ratio (output / source) | XX.X% | target 40-60%; hard floor 35% |
| H2 sections | N | min 3 required |
| Parent bullets | N | all within 35w ceiling |
| Hard failures | 0 / N | (0 to PASS) |
| Warnings | N | (cosmetic flags) |
| SS breadth ratio | YY% (Y of Z) | Y named brokers cited / Z in AS pool |
| Expert calls cited | N | distinct named expert calls |
| BB#2 coverage | N / 70 CQs | Q1 threshold ≥30 addressed/cross-ref |

### Gate-by-gate
| Gate | Check | Type | Result |
|---|---|---|---|
| 5A | Word ratio ≥35% | Hard | ✓ / ✗ |
| 5B | ≥3 H2 sections | Hard | ✓ / ✗ |
| 5C | Signpost label consistency | Hard | ✓ / ✗ |
| 5D | Parent bullet length ≤35w | Hard | ✓ / ✗ |
| 5E | IAJA tags ≥90% | Hard | ✓ / ✗ |
| 5F | Signpost labels ≥80% | Hard | ✓ / ✗ |
| 5G | Highlight density ≥25% | Hard | ✓ / ✗ |
| 5H | Underlines on ≥50% of parents | Warn | ✓ / ~ / ✗ |
| 5I | Em-dashes = 0 | Hard | ✓ / ✗ |
| 5J | No trailing periods on bullets | Hard | ✓ / ✗ |
| 5K | Structure sanity | Hard | ✓ / ✗ |
| 5L | SS breadth ratio ≥40% | Hard | ✓ / ~ / ✗ |
| 5M | Expert call breadth — count + named | Warn | informational |
| BB#2 | Coverage map ≥30 of 70 CQs | Hard | ✓ / ✗ |

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text}

### Warnings (if any)
- {Gate}: {one-line description}
```

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say. This is the qualitative interpretation Richard reads alongside the structured table.

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired — why and whether they matter}
- **Source breadth note:** {≤30w on SS breadth + expert call breadth — STRICTLY separated}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view + counter-hypothesis + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing. For Q1 BB#2 work specifically, also note any sub-block depth concerns or RA-coverage gaps the validator can't catch.}
```

### Authoring rules

1. **3-4 bullets, each ≤30 words.** Same parent-bullet discipline as body sections.
2. **Signposted with verdict-flavoured labels.** Canonical: "Net QC verdict:", "Warning context:", "Source breadth note:", "Counter-hypothesis check (AI-Dunning-Kruger):". For Q1 BB#2 work, also useful: "BB#2 coverage note:" (cross-ref to §4 sub-block depth).
3. **Specific not generic.** "BB#2 RA5 OPERATE coverage thin at IG depth — ESA Q8 to deepen" not "BB#2 looks fine."
4. **Cross-reference the body.** "Surfaced in §4.2 MOAT + Outliers block" — point to where the data lives.
5. **No A-F or R/O/Y/G grades** (per D-RSR-3, RESEARCHER does not grade — verbal verdict only).
6. **STRICTLY separate SS and expert call counts.** "SS: 6 of 8 brokers cited; experts: 2 expert calls in addition."
7. **No empty restating.** Add interpretation, not echo.

---

## BB#2 COVERAGE MAP (REQUIRED — validator-readable)

> **Canonical taxonomy reference (per D-RSR-33):** the authoritative source is `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md`. Hierarchy: **Pillar > Group (BB#) > Element / TC > Required Attribute (RA) > Core Question (CQ)**. BB#2 = "Required Foundation Quality", part of Pillar 4 (Investment Case Building Blocks). RESEARCHER feeds the RA layer primarily (most analytical traction), CQs secondarily (granular validator-readable coverage), with deliberate breadth beyond the framework (anything load-bearing that doesn't fit a CQ slot still belongs in the memo). RESEARCHER does NOT grade — APM grades.

### RA-summary coverage (read this FIRST — RA-primary view)

Before the per-CQ table below, the RESEARCHER assesses coverage at the RA level. This is the RA-primary view RESEARCHER uses analytically; the per-CQ table that follows is the validator-readable detail.

| BB#2 RA | RA name | Q1 IG-depth treatment | RA load |
|---|---|---|---|
| TC1.RA1 | Strategic ambition + congruence | full | core |
| TC1.RA2 | CEO + leadership team + culture | full | core |
| TC1.RA3 | Track record + behaviour + governance | full | core |
| TC2.RA4 | MOAT (customer/production/scale/regulatory/culture/relative scale/TAM) | full | LOAD-BEARING |
| TC2.RA5 | OPERATE (SCU/RSCU/pricing power) | summary — ESA Q8 deepens | secondary at IG |
| TC2.RA6 | GENERATE (EPS growth/RONIC/conversion/margins) | full | LOAD-BEARING |
| TC2.RA7 | Gravitational pull (mechanical SRCA improvement) | summary — ESA Q8 deepens | secondary at IG |
| TC2.RA8 | Improvement scope (peer precedents, plausibility) | summary — ESA Q8 deepens | secondary at IG |
| TC3.RA9 | Demand side (customer demand + route to market) | partial — also §3 Industry | core |
| TC3.RA10 | Competition (existing + adjacencies + entrants + substitutes) | partial — also §3 Industry | core |
| TC3.RA11-13 | Disruption / political / supplier | summary — ESA Q8 deepens | secondary at IG |
| TC4.RA14 | Concentrated existing structure | full | core |
| TC4.RA15-17 | Gravitational pull / competitor attitudes / competitiveness trends | summary — ESA Q8 deepens | secondary at IG |
| TC5.RA18 | LT growth (adjacencies, structural volume, pricing-cost) | summary — also Q23 thematic | secondary at IG |
| TC6.RA19 | Paradigm fit | summary or skip — Q23 thematic | secondary at IG |

**Q1 RA-coverage logic:** weight effort to load-bearing RAs (RA4, RA6) at IG depth; cover core RAs at IG-appropriate depth; cross-ref secondary RAs to ESA Q8 depth. Validator threshold below operates on CQ count (≥30 of 70).

### Per-CQ coverage table (validator-readable — supports the RA-summary above)

This table is mandatory. The validator counts addressed + cross-ref entries (per D-RSR-12). Q1 threshold: **≥30 of BB#2's 70 CQs** addressed or cross-ref'd. Skipped CQs require explicit reason ("ESA depth — covered in Q8" or "Not applicable: {reason}").

| BB#2 ref | TC label | Section in this memo | Coverage status | Notes |
|---|---|---|---|---|
| TC1.RA1.CQ1 | Great Operator > Strategic ambition | §4.1 Operator | addressed / cross-ref / skipped | direct / via §X / reason |
| TC1.RA1.CQ2 | Great Operator > Strategy congruence | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ3 | Great Operator > CEO calibre | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ4 | Great Operator > Hiring + leadership team | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ5 | Great Operator > Resourcing | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ6 | Great Operator > Culture | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ7 | Great Operator > Conservative guidance | §4.1 Operator | addressed | direct |
| TC1.RA2.CQ8 | Great Operator > Communication clarity | §4.1 Operator | addressed | direct |
| TC1.RA3.CQ9 | Great Operator > High RONIC capital allocation | §4.1 Operator + §1 Financials | addressed | direct |
| TC1.RA3.CQ10 | Great Operator > Acts not talks | §4.1 Operator + §2 Recent delivery | addressed | direct |
| TC1.RA3.CQ11 | Great Operator > Track record vs environments | §4.1 Operator + §2 Recent delivery | addressed | direct |
| TC1.RA3.CQ12 | Great Operator > Outlier standards | §4.1 Operator | cross-ref | summary level — ESA depth in Q8 |
| TC1.RA3.CQ13 | Great Operator > Shareholders first | §4.1 Operator + §1 Capital allocation | addressed | direct |
| TC1.RA3.CQ14 | Great Operator > Buyback discipline | §4.1 Operator + §1 Financials | addressed | direct |
| TC1.RA3.CQ15 | Great Operator > Prudent governance | §4.1 Operator | cross-ref | summary level — ESA depth in Q8 |
| TC2.RA4.CQ16 | Advantaged business > Customer moats | §4.2 MOAT + §2 Customer side | addressed | direct |
| TC2.RA4.CQ17 | Advantaged business > Production moats | §4.2 MOAT | addressed | direct |
| TC2.RA4.CQ18 | Advantaged business > Scale advantage moats | §4.2 MOAT + §2 Scale economies | addressed | direct |
| TC2.RA4.CQ19 | Advantaged business > Regulatory moats | §4.2 MOAT | addressed | direct |
| TC2.RA4.CQ20 | Advantaged business > Culture moats | §4.2 MOAT | addressed | direct |
| TC2.RA4.CQ21 | Advantaged business > High relative scale | §4.2 MOAT + §1 Peer comparison | addressed | direct |
| TC2.RA4.CQ22 | Advantaged business > Large realistic TAM | §4.2 MOAT | addressed | direct |
| TC2.RA5.CQ23 | OPERATE > High SCU | §4.2 OPERATE | cross-ref | high-level — ESA depth in Q8 |
| TC2.RA5.CQ24 | OPERATE > Leading RSCU | §4.2 OPERATE | cross-ref | ESA depth |
| TC2.RA5.CQ25 | OPERATE > Pricing power | §4.2 OPERATE | cross-ref | ESA depth |
| TC2.RA5.CQ26 | OPERATE > Scale economies shared | §4.2 OPERATE | cross-ref | ESA depth |
| TC2.RA6.CQ27 | GENERATE > 12-20% EPS + revenue growth | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ28 | GENERATE > 20%+ sales deployable at high RONIC | §4.2 GENERATE | addressed | direct |
| TC2.RA6.CQ29 | GENERATE > High post-tax RONIC 25-30%+ | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ30 | GENERATE > High NI to FCF conversion 80% | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ31 | GENERATE > Post-tax ROCE 15%+ | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ32 | GENERATE > Post-tax ROTC 30%+ | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ33 | GENERATE > High gross margins | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ34 | GENERATE > Solid EBIT margins | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA6.CQ35 | GENERATE > Operating leverage | §4.2 GENERATE | addressed | direct |
| TC2.RA6.CQ36 | GENERATE > Low tax rate / EPS leakage | §4.2 GENERATE + §1 Financials | addressed | direct |
| TC2.RA7.CQ37 | Gravitational pull > SRCA improvement | §4.2 Gravitational pull | cross-ref | summary — ESA depth in Q8 |
| TC2.RA7.CQ38 | Gravitational pull > Financial improvement | §4.2 Gravitational pull | cross-ref | summary — ESA depth in Q8 |
| TC2.RA8.CQ39 | Improvement scope > Peer precedents | §4.2 Improvement scope | cross-ref | summary — ESA depth in Q8 |
| TC2.RA8.CQ40 | Improvement scope > Big savings | §4.2 Improvement scope | cross-ref | summary — ESA depth in Q8 |
| TC2.RA8.CQ41 | Improvement scope > Many small savings | §4.2 Improvement scope | cross-ref | summary — ESA depth in Q8 |
| TC2.RA8.CQ42 | Improvement scope > Plausibility from strategy | §4.2 Improvement scope | cross-ref | covered in CQ2 / strategy |
| TC3.RA9.CQ43 | Value chain > Customer demand | §4.3 Demand + §3 Industry | addressed | direct |
| TC3.RA9.CQ44 | Value chain > Route to market | §4.3 Demand + §3 Industry | addressed | direct |
| TC3.RA10.CQ45 | Value chain > Existing competition | §4.3 Competition + §3 Industry | addressed | direct |
| TC3.RA10.CQ46 | Value chain > Adjacencies entering | §4.3 Competition + §3 Industry | addressed | direct |
| TC3.RA10.CQ47 | Value chain > Vanilla new entrants | §4.3 Competition | cross-ref | summary — ESA depth |
| TC3.RA10.CQ48 | Value chain > Innovative new entrants | §4.3 Competition | cross-ref | summary — ESA depth |
| TC3.RA10.CQ49 | Value chain > Substitutes | §4.3 Competition | cross-ref | summary — ESA depth |
| TC3.RA11.CQ50 | Value chain > Disruption forces | §4.3 + §3 Industry | cross-ref | ESA depth in Q8 |
| TC3.RA12.CQ51 | Value chain > Regulator SWOT | §4.3 + §3 Industry | cross-ref | ESA depth in Q8 |
| TC3.RA12.CQ52 | Value chain > Political SWOT | §4.3 + §3 Industry | cross-ref | ESA depth in Q8 |
| TC3.RA13.CQ53 | Value chain > Supplier SWOT | §4.3 | cross-ref | ESA depth in Q8 |
| TC4.RA14.CQ54 | Industry structure > #1 or #2 position | §4.4 Industry structure + §3 | addressed | direct |
| TC4.RA14.CQ55 | Industry structure > Top 5 >30% share | §4.4 Industry structure + §3 | addressed | direct |
| TC4.RA14.CQ56 | Industry structure > Steep distribution curve | §4.4 Industry structure + §3 | addressed | direct |
| TC4.RA15.CQ57 | Industry structure > Share stability | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA15.CQ58 | Industry structure > New entrants' share | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA15.CQ59 | Industry structure > Consolidation to largest | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA15.CQ60 | Industry structure > Consolidation to advantaged | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA16.CQ61 | Industry structure > Benign-ness | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA16.CQ62 | Industry structure > MOL stability | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA16.CQ63 | Industry structure > Shark attack risk | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA16.CQ64 | Industry structure > Volume vs ROCE | §4.4 Industry structure | cross-ref | summary — ESA depth |
| TC4.RA17.CQ65 | Industry structure > Competitiveness trends | §4.4 Industry structure + §3 | addressed | direct |
| TC5.RA18.CQ66 | LT growth > Adjacencies | §4.5 LT growth | cross-ref | summary — ESA depth in Q8 + Q23 |
| TC5.RA18.CQ67 | LT growth > Volume secular | §4.5 LT growth | cross-ref | summary — ESA depth in Q8 + Q23 |
| TC5.RA18.CQ68 | LT growth > Pricing secular | §4.5 LT growth | cross-ref | summary — ESA depth in Q8 + Q23 |
| TC5.RA18.CQ69 | LT growth > GDP+ historical growth | §4.5 LT growth | cross-ref | summary — ESA depth in Q8 + Q23 |
| TC6.RA19.CQ70 | Paradigm fit > Cross-ref to Pillar P2 | §4.5 Paradigm fit | cross-ref | covered in Q23 thematic |

**Coverage summary:** 37 addressed (direct), 33 cross-ref (summary or ESA-depth-flagged). Total coverage: 70/70. Q1 threshold (≥30 addressed/cross-ref) substantially exceeded. **Note:** "addressed" + "cross-ref" both count toward the threshold; "skipped" requires reason. Adjust above per actual content for the specific stock.

---

## SOURCE-SPECIFIC EXECUTION — [AS] only

This is an **AS-only query** (Q1 IG BD). There is no Claude [C] version. The parent RESEARCHER will handle extraction, highlighting, formatting, and Notion posting after the AS thread returns.

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

Before extracting any content, perform this pre-flight check:

1. **Query AS for SS pool size:** "How many sell-side analysts in the AlphaSense library currently cover {COMPANY} ({TICKER})? List the broker names." Record this as the AS pool size `Z` and the broker name list.

2. **Consult the FULL pool, not a subset.** Do NOT default to citing one or two preferred brokers. Read across every named broker in the AS pool where their research is relevant to the business description, financials, industry context, and BB#2 foundation quality. Where a broker has no relevant research for this query, note that explicitly (e.g. "UBS — no recent BD-level coverage found in last 12M") rather than silently dropping them.

3. **Name each broker cited.** When citing SS material, name the broker every time. Format: "[AS-Berenberg]" or "[AS-Citi]" prefix on the bullet, or inline "...per Berenberg's 12-Mar-26 note" framing.

4. **Strict separation from expert calls.** Expert calls are a distinct source type. Do NOT count expert calls toward SS breadth. If you cite an expert call, mark it as `[AS-Expert]` (with the expert's anonymised role/title), never as `[AS-Broker]`.

5. **Output the breadth metadata at memo-end.** Ensure the following fields are written into metadata.json by the parent RESEARCHER:
   - `ss_pool_size`: Z
   - `ss_brokers_cited`: list of distinct broker names
   - `expert_calls_cited`: list of distinct expert call references
   - `expert_call_count`: integer

**Why this matters:** Sell-side gives Watson access to information [C] / WebSearch cannot reach (proprietary research, broker estimates, analyst commentary). Memos that cite "SS consensus" while citing only 2 of 8 covering brokers materially distort Richard's read. The 5L gate enforces breadth structurally; this prompt instruction enforces it at source.

**Data sources for [AS] version:**
- All company investor presentations including Capital Markets Days (CMDs) — last 3 years.
- Quarterly, semi-annual, annual filings — last 3 years.
- Transcripts of all investor communications — last 3 years.
- Sell-side research and expert calls — broad coverage, every analyst integrated, particular diligence on most recent 12 months.
- Quarterly or semi-annual data — last 12 months emphasis.

**[AS]-specific analytical lens:** AS expert call transcripts surface management commentary that diverges from public guidance — flag with `⚡ RARE` if material. SS analyst rating distribution (% buy/hold/sell) and price target dispersion are first-class data for §5 Future.

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: `"{COMPANY} {TICKER} business description financials industry structure {INDUSTRY} {PEERS}"`.
- Secondary searches: capital allocation history, CEO commentary, sector roundtables, peer comparisons.
- Screenshot verification: confirm Deep Research mode active, verify data sourcing.
- Read `notion-posting-sop.md` before posting output to Notion.
- Post to Notion Stock Notes with `[AS]` tag and date.

---

## VALIDATION GATES (auto-applied at post time)

The validator runs at gate point before any Notion post. Output must pass:

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1-§5 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (§1-§5) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately (not overused) | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **BB#2 coverage map present + ≥30 addressed/cross-ref** | required | BLOCK post |
| **SS breadth ratio (5L) ≥40%** | hard floor | BLOCK or regenerate (legitimate_source_paucity bypass available if Z<3) |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged in QC table; no blocking |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS returns genuinely thin source material (e.g. micro-cap with no broker coverage), word-count gate bypasses; structural gates (BLUF, signposts, peer context where applicable, sceptical bullet, BB#2 coverage map) still apply. Auto-flag, APM ratifies at Phase 4.5 hot wash.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

Before declaring complete, RESEARCHER verifies:

- [ ] Mission compass clear: have I built a thorough understanding of what {COMPANY} does, how it makes money, its financial profile, industry context, and forward outlook?
- [ ] Reader priorities applied: am I prioritising findings that bear on 18M-3Y EPS trajectory + 25% IRR potential?
- [ ] All 5 sections present (§1 General, §2 Company Details, §3 Industry Context, §4 BB#2 Foundation Quality, §5 Future), each with J-front verdict bullet and sceptical bullet.
- [ ] §4 BB#2 sub-blocks (§4.1 Operator, §4.2 Advantaged business + SRCA, §4.3 Value chain, §4.4 Industry structure, §4.5 LT growth + Paradigm fit) all addressed at appropriate depth.
- [ ] BB#2 coverage map present with ≥30 of 70 CQs addressed/cross-ref'd.
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs (except optional 1-2 sentence inline scene-setter top of §1).
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used where applicable; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] metadata.json written.
- [ ] Sceptical bullets per section actually invert findings — not boilerplate "could be wrong."
- [ ] AS pool size Z queried and recorded in metadata.json (`ss_pool_size`).
- [ ] Distinct named SS brokers cited (Y); ratio Y/Z computed; `ss_breadth_gate` result recorded.
- [ ] Expert calls counted SEPARATELY (no conflation with SS); `expert_call_count` + `expert_calls_cited` recorded.
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored (3-4 bullets, signposted, ≤30w each, specific not generic).

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Business Description [AS] @ DD-Mon-YY`
Tags: `#IG #BD #BB#2-Q1`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only (per spec §16); never highlight whole bullets.

---

*End of Q1 IG BD — AFTER v2 draft (v2.1 pattern). Awaiting Richard's re-review.*
