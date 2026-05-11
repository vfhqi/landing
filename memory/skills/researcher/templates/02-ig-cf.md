# Query 2: Fundamental Change Forces — AlphaSense + Claude

> **CHAT-ITERATION DRAFT — v2 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/02-ig-cf.md`. Standard v2 pattern (NO BB#2 overlay — Q2 is change-forces, not foundation-quality). v2 adds four blocks per D-RSR-22: in-memo QC Audit panel, QC Commentary, SS breadth gate (5L Hard) + Expert breadth (5M Warn), AS prompt-side breadth instruction. All v1 content preserved verbatim — purely additive.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Do NOT include a "Company Description," "Business Overview," "Background," or any equivalent scene-setting section. The reader has already read the IG #1 Business Description memo for this stock and does not want it repeated. Start directly with the change-forces analysis. If the model insists on context, condense to 1-2 sentences inline at the top of §1 ("Brief recap"), no more. Section 2 onwards is query-specific only.

---

## MISSION

Write a comprehensive change-forces memo for {COMPANY} ({TICKER}). This is an Ideas Generation (IG) stage output — the goal is to identify and assess ALL forces of change acting on the business, both internal (leadership, strategy, ambition, financial profile) and external (demand, competition, disruption, regulation, macro). The memo should illuminate whether meaningful change is occurring that could drive a re-rating or inflection.

Output: comprehensive memo, target {WORD_TARGET} words (default ~5,000-6,000w per source version under v2 pattern; legitimate-paucity bypass available). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored where possible. Every section opens with a J-front verdict bullet. Sceptical lens per section.

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated, long-only equity investor (5-15 positions) focused on UK/European stocks, $5-50bn market cap. Holds for 12-24 months. Singular focus: businesses experiencing positive improvements in revenue growth rates, margins, EPS, guidance, strategy, growth ambition, sentiment.

Key mental models applied to change forces:
- **Right-to-left thinking:** Start with the financial output (predictable 18M-3Y EPS), work backwards to what's driving it.
- **Transmission mechanism clarity:** Can you trace a clear path from the change to EPS impact? Zero clarity = false friend.
- **"Strong views, weakly held":** Form a view on each change force. Be willing to revise.
- **Scepticism bias:** Assume companies will misunderstand or downplay negative changes. Take a creative, probing view.
- **Demand pulse caution:** Most demand pulses totally reverse to trend. Assume 100% cyclical/temporary unless proven structural.

At IG stage, the reader wants to know: what's CHANGING at this company, how material is it, and is there a plausible path to a 25%+ IRR over 18-36 months?

**What downstream uses this output:** APM A&J reads this memo to populate Pillar P3 (IC#2 Required Case INPUTS — the change forces driving the case) and Pillar P3 (IC#3 Required Case SETUPS — does the change pattern match a recognisable setup archetype?). The memo also surfaces on the RESEARCH STAGES dashboard tab. Format-aware structure (BLUF + signposted bullets + peer anchors + ❌/⚡ markers) makes APM's IC#2/IC#3 grading mechanical rather than reconstructive.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in the SECTIONS TO COVER block below must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*. A parent bullet ≤30 words plus 2-4 sub-bullets ≤25 words each carries 100-150 words of analytical content in a scannable form — same depth as a paragraph, vastly more useful for the reader.

If in doubt, write more substantive bullets rather than longer ones. Completeness and analytical rigour are more important than conciseness. Do not sacrifice depth for brevity.

**The test:** would Richard learn something from this memo that he couldn't get from a sell-side note? Trust your judgement. Include anything that might be interesting to the reader. Where you identify uncommonly positive or negative information, include it.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1 (only if the model insists on context).
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.** Splitting a 60w parent into a 30w parent + two 25w sub-bullets is mandatory, not optional.
- **One analytical dimension per bullet.** Bullets that mix timing + magnitude + significance get split into separate bullets, each with its own signpost prefix.
- **Signpost prefixes** (demi-bold + colon) on every parent bullet in body sections. Vocabulary specified per-section below — and licence to invent additional signposts where you spot analytical patterns the canonical list doesn't cover (see SIGNPOST DISCRETION clause below).
- **Peer / base-rate anchor** on every quantitative claim where applicable. Specific peer name OR sector median — never a number in isolation.
- **J-front verdict bullet** at the top of every section. Replaces grading. NOT a grade (RESEARCHER doesn't grade — that's APM territory). Instead: a verbal synthesis verdict, ≤30w, signpost-prefixed, peer-anchored where quantitative.
- **Per-section sceptical bullet** at the bottom of every section. Inverts the section's findings. Frames open: what's the bearish counter-read, and through what mechanism could it materialise?
- **IAJA suffix tags** on every parent bullet: `[#J]` judgement / `[#A]` analysis / `[#I]` information.
- **❌ inversion marker** on findings clearly worse than peer median. RESEARCHER does NOT grade these — APM does.
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (top/bottom 5% of peer group on some dimension), (b) deliberately-weird signals (qualitative oddities the operator hasn't explained, cross-roads exposures the consensus is ignoring, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo. Archetype: a non-traditional CEO (e.g. WH Smith's CEO appointed from a different industry asking unconventional retail-format questions) is itself a ⚡ signal even before any quantitative anomaly surfaces.
- **Inline highlights** (green / yellow / red phrase-level spans) on the specific carrying phrase, NOT the whole bullet.

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Each section below lists a canonical signpost vocabulary. Use it where applicable — these are the labels Richard and APM read fluently across stocks, so cross-stock comparison stays mechanical. Where you spot an analytical pattern not covered by the canonical list, you have explicit licence to coin a new signpost label. Three guardrails on invented signposts:

1. **Canonical first.** If a listed signpost fits the bullet, use it — don't reinvent.
2. **Length cap: ≤4 words**, demi-bold + colon format. Long invented signposts break scannability.
3. **Single analytical dimension.** One lens per signpost. Compound signposts get split.

Invented signposts are logged in the QC footer (`Invented signposts: "Activist pressure ramp:", "Cycle inflection signal:"`).

### Memo skeleton

```
1. METADATA HEADER (you populate)
   Ticker, company, query name, stage, source, generated date, target words.
   metadata.json: write at completion. Memo will not post without it.

2. KEY FINDINGS (BLUF)
   5-10 parent bullets. Each ≤30w. J→A→I order. Peer-anchored where quantitative.
   The "skim layer": reader who reads nothing else gets the picture.

3. BODY SECTIONS §1-§13 (per SECTIONS TO COVER below)
   Each section opens with a J-front verdict bullet.
   Each section ends with a sceptical bullet (open-framed).
   Bullets between: signposted, peer-anchored, IAJA-tagged.

4. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
   0-5 bullets surfacing the strongest cross-cutting bearish counter-reads.
   Cross-references which section each came from.

5. AGGREGATE OUTLIERS (⚡)
   0-3 bullets. Genuinely unusual data points only.

6. QC FOOTER (auto-generated from metadata.json)
   Source attribution, word counts, peer-context density, signpost coverage,
   BLUF presence, J-front ordering check, invented signposts log,
   quality_flag if any.
```

---

## SECTIONS TO COVER

The thirteen body sections below are the natural arc of a change-forces memo — internal change first (§1-§5), then external change forces (§6-§12), then historical track record (§13). Each section preserves the prior version's analytical sub-questions verbatim under the format-aware envelope.

### §1 — Brief recap + Key components summary

**Open with J-front verdict bullet:** Net signal on the materiality of change at {COMPANY} — is something interesting happening? — ≤30w.

**Canonical signpost vocabulary:** "What it does:", "Revenue source:", "Geographies:", "Business lines:", "Revenue model:", "L3Y trajectory:", "N3Y trajectory:", "Leadership change:", "M&A:", "Margin change:", "Shareholder return:", "Demand change:", "Goal change:", "Disruption:", "Macro change:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Brief recap:** What it does, why, how — over L3Y and plausibly N3Y. Where revenue comes from. How many countries, business lines, revenue/business models. Maximum 1-2 sentences inline if model insists on context; otherwise condensed bullets.
- **Key components summary:** Simple list of any and all changes identified over L12-18M or plausibly N3Y related to: (1) CEO or senior leadership or IR roles; (2) M&A or corporate activity; (3) margins or financial profile; (4) shareholder returns; (5) demand/revenue and growth rates; (6) company goals/targets; (7) competitor/political/regulatory/other disruption; (8) other macro or industry changes.

**Coverage:** 8-12 parent bullets. The 8 component categories each get at least one parent bullet (or explicit "no change" note) — this is the BLUF-equivalent at section level.

**End with sceptical bullet:** "What might be changing that the company hasn't surfaced? Through what mechanism might apparent change be cosmetic rather than fundamental?"

---

### §2 — Change in leadership

**Open with J-front verdict bullet:** Net signal on leadership-team change at {COMPANY} — magnitude, direction, credibility — ≤30w.

**Canonical signpost vocabulary:** "CEO:", "CFO:", "IR:", "Board:", "2nd-level:", "eNPS:", "Culture:", "Turnover:", "Hiring posture:", "Departure:", "Successor profile:", "Tenure:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Internal leadership + personnel change — L12M and plausibly N36M:** CEO, CFO, IR, board, 2nd-level management, eNPS, culture, employee turnover.
- **Current state and how it's changing.**
- **Highlight all senior manager changes with accompanying logic.** Names, dates, prior role, successor, what catalysed the change, what the change signals.

**Coverage:** 8-12 parent bullets + sub-bullets. Each named manager gets its own parent bullet with successor profile sub-bullet.

**End with sceptical bullet:** "What's the bearish read on these leadership changes? Through what mechanism might recent appointments fail? What hidden departures might be unsurfaced? What governance signal might these changes carry?"

---

### §3 — Change in strategy/structure

**Open with J-front verdict bullet:** Net signal on strategic + structural change at {COMPANY} — magnitude, direction, internal coherence — ≤30w.

**Canonical signpost vocabulary:** "Strategic priority:", "Strategy shift:", "Org structure:", "Goal:", "Objective:", "Asset sale:", "Core/non-core:", "M&A:", "Partnership:", "JV:", "Activism:", "Investor framing:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Strategic priorities, strategy, organisational structure, goals, objectives — L12M and N36M:** Corporate strategy changes, financial goals, asset sales, organisational structure changes, core/non-core determinations, M&A, partnerships, JVs, activism.
- **How the company describes these changes to investors:** Tone shift, framing changes, narrative consistency or inconsistency.

**Coverage:** 10-15 parent bullets + sub-bullets. Each strategic shift gets its own parent bullet with timing sub-bullet + magnitude sub-bullet + investor-framing sub-bullet.

**End with sceptical bullet:** "What's the bearish read on the strategic shift? Through what mechanism might apparent strategic change be window-dressing? What internal incoherence might the new strategy mask? What execution risk might be under-priced?"

---

### §4 — Change in priorities/ambition

**Open with J-front verdict bullet:** Net signal on the company's ambition + intensity + standards — is the operator gear-shifting? — ≤30w.

**Canonical signpost vocabulary:** "Ambition:", "Intensity:", "Values:", "Standards:", "Productivity:", "Behaviour:", "CEO commentary:", "Tone shift:", "Earnings call signal:", "CMD signal:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Ambition, intensity, values, standards, productivity, behaviours — L12M and N36M.**
- **Pay particular attention to CEO verbal commentary from earnings calls and CMDs.** Direct quotes preferred. Tone shift identification.

**Coverage:** 8-12 parent bullets + sub-bullets. CEO direct quotes get their own parent bullets with date + venue sub-bullet.

**End with sceptical bullet:** "What might the apparent ambition shift be masking? Through what mechanism might rhetoric outpace reality? What signal of incongruence between ambition + capability might be lurking?"

---

### §5 — Financial profile change

**Open with J-front verdict bullet:** Net signal on financial-profile change at {COMPANY} — direction, magnitude vs peers, durability — ≤30w.

**Canonical signpost vocabulary:** "Revenue growth:", "Margin:", "Leverage:", "Cash conversion:", "FCF:", "Shareholder return:", "Opex investment:", "Capex investment:", "Intangibles investment:", "Investment finish date:", "Industry difficulty test:", "Improvement scope:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Changes in growth rates, margins, leverage, cash conversion, FCF, shareholder returns — L3Y and N3Y.**
- **Degree of investment in specific initiatives (opex/capex/intangibles)** and when increased investment will finish.
- **Vs key competitors:** explicit peer-anchor on each financial metric.
- **Performance during industry difficulty:** how did {COMPANY} perform vs peers during recent sector downturn?
- **Benchmark current and plausible N3Y profile** with competitor and sector references.
- **Highlight areas with scope for improvement.**

**Coverage:** 12-18 parent bullets + sub-bullets. Each financial metric gets explicit peer-median anchor.

**End with sceptical bullet:** "What's the bearish read on the financial-profile trajectory? Through what mechanism might margin expansion prove transient? What hidden capital intensity might be lurking? Through what mechanism might leverage rise faster than headline guidance?"

---

### §6 — Value chain — Demand

**Open with J-front verdict bullet:** Net signal on demand-side change forces shaping {COMPANY}'s revenue trajectory — ≤30w.

**Canonical signpost vocabulary:** "Customer behaviour:", "Sentiment:", "Volume:", "Pricing power:", "Discounting:", "Delays:", "Distributor change:", "Route to market:", "Demand pulse:", "Cycle stage:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Customer purchasing behaviour, sentiment, volumes, pricing power, discounting, delays.**
- **Changes to distributors / routes to market.**
- **Take a creative + probing view — assume companies will misunderstand or downplay demand slowdowns.**

**Coverage:** 8-12 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish demand-side read? Through what mechanism might apparent demand strength reverse? What demand pulse might be late-cycle vs structural?"

---

### §7 — Value chain — Competition

**Open with J-front verdict bullet:** Net signal on competitive intensity + structural change forces in {COMPANY}'s industry — ≤30w.

**Canonical signpost vocabulary:** "Industry structure:", "Market structure:", "Intensity:", "New competitor:", "Disruption:", "Substitute:", "Disintermediation:", "BtE:", "Barrier to exit:", "Competitor returns:", "Competitor margin:", "Competitor health:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Industry structure, market structure, competitive intensity, new competitors, disruption, substitutes, disintermediation, BtE, barriers to exit, competitor returns/margins/financial health — L3Y and N3Y.**
- **Take a creative + probing view.**

**Coverage:** 8-12 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish competitive read? Through what mechanism might apparent industry structural advantage erode? What new-entrant or substitute pattern might be under-priced?"

---

### §8 — Value chain — Disruption

**Open with J-front verdict bullet:** Net signal on disruption forces — technology, new entrants, other — shaping {COMPANY}'s competitive position — ≤30w.

**Canonical signpost vocabulary:** "Technology disruption:", "New entrant — innovative:", "New entrant — traditional:", "Disruption pace:", "Adoption curve:", "Incumbent response:", "Disruption cost:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Technology disruption, new entrants (innovative or traditional), any other disruption — L3Y and N3Y.**
- **Creative + probing view.**

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish disruption read? Through what mechanism might disruption compound faster than the conventional view assumes? What incumbent-response failure pattern might apply?"

---

### §9 — Value chain — Political and regulatory

**Open with J-front verdict bullet:** Net signal on political/regulatory change forces shaping {COMPANY}'s industry and geographies — ≤30w.

**Canonical signpost vocabulary:** "Regulatory shift:", "Political actor:", "Geography:", "Tariff:", "Subsidy:", "Tax change:", "Compliance cost:", "Labour regulation:", "Environmental regulation:", "Trade policy:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Actual or plausible political / regulatory influence on the company, its industry and geographies — L3Y and N3Y.**
- **Creative + probing view.**

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish political/regulatory read? Through what mechanism might regulatory shift damage {COMPANY}'s structural advantages? What political risk might be under-priced?"

---

### §10 — Value chain — Supply side

**Open with J-front verdict bullet:** Net signal on supplier-side change forces shaping {COMPANY}'s cost structure + supply security — ≤30w.

**Canonical signpost vocabulary:** "Supplier economics:", "Concentration:", "Relationship:", "Supplier health:", "Supplier returns:", "Supply risk:", "Vertical integration:", "Backward integration:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Supplier economics, relationships, concentration, risks — L3Y and N3Y.**
- **Including supplier returns on capital and financial health.**

**Coverage:** 5-8 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish supply-side read? Through what mechanism might supplier weakness become {COMPANY}'s problem? What concentration risk might be under-priced?"

---

### §11 — Revenue/demand cycle

**Open with J-front verdict bullet:** Net signal on revenue cyclicality + cycle stage — where in the cycle is {COMPANY}? — ≤30w.

**Canonical signpost vocabulary:** "Cyclicality:", "Predictability:", "Cycle stage:", "Cycle length:", "Through-cycle profile:", "Trough behaviour:", "Peak behaviour:", "Demand pulse:", "Inventory cycle:", "Capex cycle:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Revenue cyclicality and predictability — L3Y and N3Y.**
- **What stage of the demand cycle.**
- **Go beyond company commentary — use sell-side, peers, other data.**
- **Creative + probing view — assume companies downplay cyclicality.**

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish cycle-stage read? Through what mechanism might {COMPANY} be later-cycle than apparent? What demand pulse might totally reverse to trend?"

---

### §12 — Value chain — Macroeconomic

**Open with J-front verdict bullet:** Net signal on macro change forces influencing {COMPANY}'s revenue + margins — ≤30w.

**Canonical signpost vocabulary:** "Macro shift:", "Rates:", "FX:", "Inflation:", "Wage:", "Energy:", "Geopolitical:", "End-market macro:", "Customer macro:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **All broader macro changes potentially influencing revenue growth and margins — L18M and N3Y.**
- **Go beyond company commentary.**
- **Creative + probing view.**

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish macro read? Through what mechanism might apparent macro tailwinds reverse? What macro risk specific to {COMPANY}'s end-markets might be under-priced?"

---

### §13 — Historical track record of delivery

**Open with J-front verdict bullet:** Net signal on {COMPANY}'s delivery track record — credibility, internal vs external causation, peer-relative performance — ≤30w.

**Canonical signpost vocabulary:** "Delivery vs guide:", "Delivery vs SS:", "Beat ratio:", "Miss magnitude:", "Internal cause:", "External cause:", "Financial delivery:", "Strategic delivery:", "Operational delivery:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- **Delivery vs guidance and sell-side expectations over L3Y.**
- **Delineation between internal and external causes of delivery / miss.**
- **Financial, strategic, and operational delivery.**

**Coverage:** 8-12 parent bullets + sub-bullets. Track record table preferred (period × delivery vs guide × delivery vs consensus × cause classification).

**End with sceptical bullet:** "What's the bearish read on the delivery track record? Through what mechanism might apparent beats be guidance management? What miss pattern might cluster around catalyst events?"

---

## AGGREGATE BLOCKS (after §13)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly worse than peer median or sector base rate.

**Format:** `❌ Signpost: finding statement. Peer anchor. [Cross-ref: §X]`

**Example:** `❌ Margin trajectory: -180bps L3Y vs peer median +40bps — among bottom-quartile of sector. [Cross-ref: §5 Financial profile]`

RESEARCHER does NOT grade these. Surface, anchor, cross-reference. APM grades.

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `⚡ RARE: CEO turnover: 4 in 18 months — only 1 of 12 peers exceeded 2 in same period. [Cross-ref: §2 Leadership]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel into the memo at post time. RESEARCHER does NOT author the structured table — the validator computes every metric. RESEARCHER DOES author the Qualitative Commentary block immediately below.

The panel is plain-text-with-markdown. Visual styling is owned by the SA - Ratings Dashboard project (D-RSR-21).

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS] / [C] / [C+AS]
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

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text}

### Warnings (if any)
- {Gate}: {one-line description}
```

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say.

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired — why and whether they matter}
- **Source breadth note:** {≤30w on SS breadth + expert call breadth — STRICTLY separated}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view + counter-hypothesis + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing.}
```

### Authoring rules

1. **3-4 bullets, each ≤30 words.** Same parent-bullet discipline as body sections.
2. **Signposted with verdict-flavoured labels.** Canonical: "Net QC verdict:", "Warning context:", "Source breadth note:", "Counter-hypothesis check (AI-Dunning-Kruger):". Invent additional labels per SIGNPOST DISCRETION clause.
3. **Specific not generic.** "Underline density borderline at 16 across 10 parents" not "underlines look fine."
4. **Cross-reference the body.** "Surfaced in §6 Demand + Outliers block" — point to where the data lives.
5. **No A-F or R/O/Y/G grades** (per D-RSR-3).
6. **STRICTLY separate SS and expert call counts.** "SS: 6 of 8 brokers cited; experts: 2 expert calls in addition."
7. **No empty restating.** Add interpretation, not echo.

---

## SOURCE-SPECIFIC DELTA — [AS] version

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

Before extracting any content, perform this pre-flight check:

1. **Query AS for SS pool size:** "How many sell-side analysts in the AlphaSense library currently cover {COMPANY} ({TICKER})? List the broker names." Record this as the AS pool size `Z` and the broker name list.

2. **Consult the FULL pool, not a subset.** Do NOT default to citing one or two preferred brokers. Read across every named broker in the AS pool where their research is relevant to change forces — leadership, strategy, demand, competition, disruption, regulatory, macro, delivery. Where a broker has no relevant research for this query, note that explicitly (e.g. "UBS — no recent change-force coverage found in last 12M") rather than silently dropping them.

3. **Name each broker cited.** When citing SS material, name the broker every time. Format: "[AS-Berenberg]" or "[AS-Citi]" prefix on the bullet.

4. **Strict separation from expert calls.** Expert calls are a distinct source type. Mark expert calls as `[AS-Expert]` (with anonymised role/title), never as `[AS-Broker]`.

5. **Output the breadth metadata at memo-end.** Ensure metadata.json contains: `ss_pool_size` (Z), `ss_brokers_cited` (list), `expert_calls_cited` (list), `expert_call_count` (integer).

**Why this matters:** Sell-side gives Watson access to information [C] / WebSearch cannot reach. Memos that cite "SS consensus" while citing only 2 of 8 covering brokers materially distort Richard's read. The 5L gate enforces breadth structurally; this prompt instruction enforces it at source.

**Data sources for [AS] version:**
- All company investor presentations including CMDs — last 3 years.
- Quarterly, semi-annual, annual filings — last 3 years.
- Transcripts of all investor communications — last 3 years (emphasis on L12M).
- Sell-side research and expert calls — broad coverage, every analyst integrated, particular diligence on most recent 12 months.
- Blog posts, Medium, Substack from leading commentators. Upweight informal industry-participant commentary; underweight generalist news + academic articles.

**[AS]-specific analytical lens:** AS expert calls + SS research surface change forces that public filings hide (management evasiveness on demand pulses, competitor commentary on disruption forces, supplier-side cost commentary). SS analyst tone shift across L12M is first-class data for §4 (priorities/ambition) and §13 (delivery track record).

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: `"{COMPANY} {TICKER} change forces leadership strategy demand competition disruption regulatory macro {INDUSTRY} {PEERS}"`.
- Secondary searches: management commentary + tone analysis, sector roundtables, peer change-force comparisons.
- Screenshot verification: confirm Deep Research mode active, verify data sourcing.
- Read `notion-posting-sop.md` before posting output to Notion.
- Post to Notion Stock Notes with `[AS]` tag and date.

---

## SOURCE-SPECIFIC DELTA — [C] version

**Data sources for [C] version:**
- WebSearch — public company filings (annual reports, 10-K/10-Q equivalents, sustainability reports, press releases).
- Earnings releases + investor presentations + CMDs (where publicly accessible).
- News + market commentary on {COMPANY} and {PEERS}.
- Industry reports + commentator blogs (Substack, Medium, industry trade press).
- Upweight informal commentary from industry participants and investors; underweight generalist news media. Prefer creative, up-to-date, bold views over superficial commentary.

**[C]-specific analytical lens:** WebSearch surfaces public filings + news + investor presentations + industry commentary. [C] does NOT have access to AS expert calls or proprietary sell-side research. [C] compensates by: deeper company filings analysis, broader peer/competitor analysis, more industry/thematic research, more creative interpretation of public data. Where [C] cannot source a peer-anchor that [AS] would have, flag with `quality_flag: thin_peer_context`.

**Execution:**
- Use WebSearch extensively — multiple searches per section.
- Search terms: `"{COMPANY} CEO change strategy"`, `"{COMPANY} guidance L12M revision"`, `"{INDUSTRY} disruption {YEAR}"`, `"{COMPANY} {PEERS} margin comparison"`, `"{COMPANY} earnings call {LATEST_QUARTER}"`.
- Cross-reference multiple public sources to triangulate change-force assessments.
- Do NOT include footnotes/endnotes/links in final memo.
- Post to Notion Stock Notes with `[C]` tag and date.

---

## VALIDATION GATES (auto-applied at post time)

The validator runs at gate point before any Notion post. Output must pass:

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1-§13 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (§1-§13) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately (not overused) | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **SS breadth ratio (5L) ≥40%** | hard floor | BLOCK or regenerate (legitimate_source_paucity bypass available if Z<3) |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged in QC table; no blocking |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS / web returns genuinely thin source material, word-count gate bypasses; structural gates (BLUF, signposts, peer context where applicable, sceptical bullet) still apply. Auto-flag, APM ratifies at Phase 4.5 hot wash.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

Before declaring complete, RESEARCHER verifies:

- [ ] Mission compass clear: have I identified ALL change forces (internal + external) acting on {COMPANY}, with materiality assessment?
- [ ] Reader priorities applied: am I prioritising findings that bear on 18M-3Y EPS trajectory + 25% IRR potential?
- [ ] All 13 sections present, each with J-front verdict bullet and sceptical bullet.
- [ ] Mental models applied: right-to-left thinking, transmission mechanism clarity, demand pulse caution, scepticism bias.
- [ ] Every quantitative claim has a peer / base-rate anchor where applicable.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs (except optional 1-2 sentence inline scene-setter top of §1).
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used where applicable; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Track record table present (§13).
- [ ] metadata.json written.
- [ ] Sceptical bullets per section actually invert findings — not boilerplate "could be wrong."
- [ ] AS pool size Z queried and recorded in metadata.json (`ss_pool_size`).
- [ ] Distinct named SS brokers cited (Y); ratio Y/Z computed; `ss_breadth_gate` result recorded.
- [ ] Expert calls counted SEPARATELY (no conflation with SS); `expert_call_count` + `expert_calls_cited` recorded.
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored (3-4 bullets, signposted, ≤30w each, specific not generic).

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Fundamental Change Forces [AS or C] @ DD-Mon-YY`
Tags: `#IG #CF #ChangeForces`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only (per spec §16); never highlight whole bullets.

---

## EXECUTION

**Dual-source query.** Both versions run:
- [AS] version → submitted to AlphaSense Deep Research by Haiku agent.
- [C] version → executed natively by Sonnet sub-agent using WebSearch.

Parent RESEARCHER handles extraction, highlighting, formatting, and Notion posting for both outputs.

---

*End of Q2 IG CF — AFTER v2 draft (v2.1 pattern). Awaiting Richard's re-review.*
