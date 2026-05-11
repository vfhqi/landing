# Query 4: Earnings trends vs. peers (L2Yish)

> **CHAT-ITERATION DRAFT — v3 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/04-triaging-earnings-trends.md`. v3 adds four blocks per D-RSR-22: in-memo QC Audit panel, QC Commentary, SS breadth gate (5L Hard) + Expert breadth (5M Warn), AS prompt-side breadth instruction. All v2 content preserved verbatim — purely additive.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Do NOT include a "Company Description," "Business Overview," "Background," or any equivalent scene-setting section. The reader has already read the IG #1 Business Description memo for this stock and does not want it repeated. Start directly with the query-specific analysis. If the model insists on context, condense to 1-2 sentences inline at the top of section 1, no more. Section 2 onwards is query-specific only.

---

## MISSION

Benchmark {TICKER} ({COMPANY}) fundamentally against direct peers over the last 12-24 months. Identify relative momentum in revenue growth, margin trajectory, EPS delivery, and guidance changes. Assess whether company is gaining or losing market share within peer group. Determine if trends are company-specific or sector-wide. Output: comprehensive memo, target {WORD_TARGET} words, structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section.

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated, long-only equity investor (5-15 positions) focused on UK/European stocks, $5-50bn market cap. Holds for 12-24 months. Looks for businesses experiencing positive improvements in revenue growth rates, margins, EPS, guidance, strategy, growth ambition, sentiment. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**Triaging purpose:** Fast, disciplined filtering at LIGHT depth. Does this stock fit a recognisable setup profile? Is the fulcrum driver plausible? Any immediate disqualifiers? Pattern recognition + "strong views, weakly held" — sensible hypotheses that need testing with more evidence.

**For this query specifically:** The reader wants to understand {TICKER}'s competitive position through the lens of fundamental execution. Has the company beaten or missed peers on revenue growth, margin expansion, EPS trajectory? Are these trends accelerating or decelerating? Is the sector improving broadly, or is {TICKER} outperforming a declining peer group? This calibration is essential to determine if the company story is about operational excellence or just riding sector tailwinds.

**What downstream uses this output:** APM A&J reads this memo to populate Pillar P3 (Fundamental Investment Case — IC#1 Required Case Outputs) and Pillar P4 (Foundation Quality — BB#2 Required Foundation Quality, especially TC2 Advantaged business RA6 Strong financial outputs). The memo also surfaces on the RESEARCH STAGES dashboard tab. Format-aware structure (BLUF + signposted bullets + peer anchors + ❌/⚡ markers + coverage map) makes APM's analysis mechanical rather than reconstructive. Filler prose actively wastes APM's reading attention; substantive bullets compound it.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in the SECTIONS TO COVER block below must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*. A parent bullet ≤30 words plus 2-4 sub-bullets ≤25 words each carries 100-150 words of analytical content in a scannable form — same depth as a paragraph, vastly more useful for the reader.

If in doubt, write more substantive bullets rather than longer ones. A section with 12 substantive parent bullets (each with sub-bullets) is far more valuable than a section with 6 long bullets. Completeness and analytical rigour are more important than conciseness. Do not sacrifice depth for brevity.

**The test:** would Richard learn something from this memo that he couldn't get from a sell-side note? If the bullet just restates a sell-side consensus, it's filler. If it triangulates across sources, surfaces a base-rate anchor, or flags an outlier — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1 (only if the model insists on context).
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.** Splitting a 60w parent into a 30w parent + two 25w sub-bullets is mandatory, not optional.
- **One analytical dimension per bullet.** Bullets that mix timing + magnitude + significance get split into separate bullets, each with its own signpost prefix.
- **Signpost prefixes** (demi-bold + colon) on every parent bullet in body sections. Vocabulary specified per-section below — and licence to invent additional signposts where you spot analytical patterns the canonical list doesn't cover (see SIGNPOST DISCRETION clause below).
- **Peer / base-rate anchor** on every quantitative claim. Specific peer name OR sector median — never a number in isolation. Failure mode to avoid: "Bufab grew at 17% CAGR" (unanchored). Required form: "Bufab grew at 17% CAGR — 2.0x sector pace of 8.4%."
- **J-front verdict bullet** at the top of every section. Replaces grading. NOT a grade (RESEARCHER doesn't grade — that's APM territory). Instead: a verbal synthesis verdict, ≤30w, signpost-prefixed, peer-anchored. Example: "Net signal: revenue momentum above peer median but mix is degrading — 60% acquisition-led vs 18% sector norm."
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

Invented signposts are logged in the QC footer (`Invented signposts: "Cycle-to-cycle margin:", "Mix re-rating:"`) so vocabulary drift across memos can be reviewed and the canonical lists consolidated over time.

### Memo skeleton

```
1. METADATA HEADER (you populate)
   Ticker, company, query name, stage, source, generated date, target words.
   metadata.json: write at completion. Memo will not post without it.

2. KEY FINDINGS (BLUF)
   5-10 parent bullets. Each ≤30w. J→A→I order. Peer-anchored.
   The "skim layer": reader who reads nothing else gets the picture.

3. BODY SECTIONS §1-§9 (per SECTIONS TO COVER below)
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

### §1 — Executive Summary (peer ranking + sector context)

**Open with J-front verdict bullet:** "Verdict: {TICKER}'s position in peer group on fundamental momentum, in ≤30w."

**Canonical signpost vocabulary:** "Peer rank:", "Trend reversal:", "Trend acceleration:", "Sector tailwind:", "Sector headwind:", "Outperformer:", "Laggard:". Invent where pattern warrants (per SIGNPOST DISCRETION clause).

**Analytical sub-questions to address:**
- Stack-rank the peer group by fundamental momentum (revenue growth, EPS trajectory, margin evolution).
- Position {TICKER} within this ranking.
- Identify the 2-3 most significant trend reversals or accelerations in the peer group over L12M.
- Flag any sector-wide tailwinds or headwinds affecting all peers.

**Coverage:** 6-10 parent bullets + sub-bullets where data warrants. Cross-section verdict is implicit — DO NOT apply A-F or R/O/Y/G grade. APM grades.

**End with sceptical bullet:** "What might invalidate this peer ranking, and through what mechanism?"

---

### §2 — Revenue Growth & Organic Dynamics

**Open with J-front verdict bullet:** Net signal on {TICKER}'s revenue momentum vs peers — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "Reported growth:", "Organic growth:", "Mix:", "Geography:", "End-market:", "Pricing power:", "Volume:", "Market share:", "M&A contribution:", "FX impact:", "Forward guide:", "Sell-side revisions:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Revenue growth rates (reported AND organic) for {TICKER} vs each peer over L3M, L6M, L12M — weight recent most heavily.
- Breakdown of revenue by end-market, geography, or product line — compare trajectory to peers.
- Pricing power signals: price/volume decomposition, discount/premium trends relative to peers.
- Volume trends and market share implications — what evidence might point to share gains or losses?
- Sell-side revisions to revenue forecasts (current FY and next 2 FY) — which analysts revised up/down and magnitude.
- Forward revenue guidance from company vs sell-side consensus — credibility assessment.

**Coverage:** 10-15 parent bullets + sub-bullets. Each named analytical lens above gets at least one parent bullet.

**End with sceptical bullet:** "What would the bearish read on this revenue trajectory be? What might cause growth rates to be inflated by M&A, one-off items, or FX? Through what mechanism might organic growth be decelerating?"

---

### §3 — Margin Profile & Evolution

**Open with J-front verdict bullet:** Net signal on margin direction vs peers — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "Gross margin:", "EBIT margin:", "EBITDA margin:", "Direction:", "Decomposition:", "Price contribution:", "Volume contribution:", "Mix contribution:", "Input costs:", "Productivity:", "Operating leverage:", "Sell-side outlook:", "Cost programmes:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Gross margin, EBIT margin, EBITDA margin for {TICKER} vs peers over L3M, L6M, L12M.
- Margin trajectory: expanding, contracting, or flat? Relative to peers?
- Decomposition of margin moves: price, volume, mix, input cost inflation, productivity — what's driving?
- Operating leverage / scalability assessment — as revenue grows, do margins expand?
- Peer margin trends: is this company defending/expanding margins in a peer group that is compressing? Or following sector compression?
- Sell-side expectations for next 12-24M margin evolution — consensus view AND outliers.
- Cost structure commentary from management: restructuring, automation, supply chain efficiency programmes.

**Coverage:** 10-15 parent bullets + sub-bullets. Each decomposition lens gets explicit parent bullet treatment — don't bundle.

**End with sceptical bullet:** "What's the inversion case on margin direction? Through what mechanism might margin expansion be one-off (cost cuts vs sustainable revenue growth)? What hidden structural costs might be lurking?"

---

### §4 — EPS Trajectory & Delivery

**Open with J-front verdict bullet:** Net signal on EPS delivery vs peers — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "EPS growth:", "Reported vs adjusted:", "Sell-side revisions:", "Forward consensus:", "Beat/miss vs guide:", "Buyback contribution:", "Share count:", "Leverage:", "Capital allocation:", "Cash conversion:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- EPS growth rates for {TICKER} vs peers over L3M, L6M, L12M (both reported AND adjusted).
- Sell-side EPS estimate changes (current FY + next 2 FY) for {TICKER} vs peers — which analysts revised and by how much?
- Consensus EPS growth expectations: forward 12M, 24M, 36M.
- EPS delivery vs prior guidance: did company beat, meet, or miss? Magnitude?
- Buyback activity: what portion of EPS improvement might be organic vs share-count-reduction-driven?
- Leverage and capital allocation: how has debt evolved? Is cash flow generation sufficient for capital returns?

**Coverage:** 10-15 parent bullets + sub-bullets. Disaggregate organic vs M&A vs buyback contribution to EPS growth — this is mechanical accounting that the LLM should perform explicitly.

**End with sceptical bullet:** "What's the bearish read on EPS quality? Through what mechanism might EPS growth be reliant on margin expansion (vs revenue growth)? Might leverage be rising in ways that flatter near-term EPS? How sustainable might the buyback contribution be?"

---

### §5 — Guidance & Forecast Changes

**Open with J-front verdict bullet:** Net signal on guidance credibility — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "Initial guide:", "Mid-year revision:", "Final delivery:", "Beat ratio:", "Magnitude:", "Conservatism:", "Sandbagging signal:", "Overconfidence signal:", "Consensus alignment:", "Analyst revisions:", "Last 1M / 3M / 12M:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Management guidance for next 12-24 months (revenue, EBIT, EPS, cash flow) — conservatism assessment.
- Sell-side consensus view vs company guidance — any divergence?
- Magnitude of guidance changes over L1M, L3M, L12M — are management becoming more or less confident?
- Patterns in guidance beats/misses over L12M — consistent outperformance or moving target?
- Forward consensus changes by analyst over L1M, L3M, L12M — who revised up/down and magnitude.

**Coverage:** 8-12 parent bullets + sub-bullets. Build a guidance-credibility track record from the L8 reporting periods.

**End with sceptical bullet:** "What's the inversion case on guidance credibility? Through what mechanism might guidance be lowered to enable beats? What signs might indicate sandbagging vs overconfidence?"

---

### §6 — Comparative Peer Ranking

**Open with J-front verdict bullet:** {TICKER}'s overall standing in peer group on the four-dimensional momentum matrix — ≤30w.

**Canonical signpost vocabulary:** "Revenue momentum rank:", "Margin momentum rank:", "EPS momentum rank:", "Consensus revision rank:", "L3M rank shift:", "L6M rank shift:", "L12M rank shift:", "Outperformer:", "Underperformer:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Construct a ranking matrix: revenue growth momentum, margin momentum, EPS momentum, consensus revision momentum.
- Stack-rank all peers on each dimension.
- Identify {TICKER}'s position in each ranking — best-in-peer-group or lagging?
- Highlight any peers significantly outperforming or underperforming consensus expectations.
- Track ranking changes over L3M, L6M, L12M — is {TICKER} moving up or down the peer group?
- Identify any peer showing exceptional operational delivery or deterioration.

**Coverage:** Mandatory peer ranking table (5 closest peers + sector median row) followed by 8-12 commentary parent bullets. The table format is non-negotiable — APM uses it for cross-stock comparison.

**End with sceptical bullet:** "How stable might these rankings actually be? What might cause them to reverse on the next print, and through what mechanism?"

---

### §7 — Sector & Value Chain Context

**Open with J-front verdict bullet:** Is {TICKER}'s outperformance company-specific or sector-driven? — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "Sector revenue:", "Sector margin:", "Sector revisions:", "Supplier signals:", "Customer signals:", "Distributor signals:", "End-market growth:", "Competitive intensity:", "Cyclical:", "Structural:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Is the broader sector ({INDUSTRY}) showing improving or deteriorating fundamentals? Revenue growth rates, margin evolution, consensus revisions?
- Supply chain dynamics: are {TICKER}'s suppliers, distributors, customers showing corroborating trends?
- End-market health: are {TICKER}'s end-markets (vertical or geographic) growing or contracting? Relative to sector?
- Competitive intensity: is the sector consolidating or fragmenting? Price competition intensifying?
- Cyclical vs structural: are current trends dependent on macro/cycle, or driven by structural industry change?

**Coverage:** 8-12 parent bullets + sub-bullets. The cyclical-vs-structural disaggregation is the key analytical lens.

**End with sceptical bullet:** "What's the bearish cross-cutting read on sector context? Through what mechanism might {TICKER}'s outperformance depend on tailwinds that are fading? What structural decay might the peer group be hiding?"

---

### §8 — Quality of Earnings & Accounting

**Open with J-front verdict bullet:** Net signal on earnings quality vs peers — ≤30w, peer-anchored.

**Canonical signpost vocabulary:** "NWC days:", "Cash conversion:", "OCF vs EPS:", "One-offs:", "Adjustments:", "Non-GAAP gap:", "Inventory days:", "Receivables days:", "Aging:", "Peer norms:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Working capital trends: has NWC been a drag or benefit? Relative to peers?
- Cash conversion: is earnings translating to cash? Any divergence between GAAP and operating cash flow?
- One-off items, adjustments, non-GAAP measures: material to reported earnings? How do peers handle adjustments?
- Inventory and receivables trends: any aging concerns? Relative to peer norms?

**Coverage:** 6-10 parent bullets + sub-bullets. NWC days vs peer-median is the most load-bearing single number.

**End with sceptical bullet:** "What's the bearish read on earnings quality? Through what mechanism might non-GAAP adjustments be inflating true profitability? What might be deteriorating that hasn't yet shown in the headline?"

---

### §9 — Sceptical Synthesis (cross-cutting)

**Open with J-front verdict bullet:** What is the strongest bearish case for {TICKER} given everything above? — ≤30w.

**Canonical signpost vocabulary:** "Reverse-engineered bear:", "Single largest risk:", "Early warning:", "Breaking points:", "Peer-relative downside:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Reverse-engineer the bearish case: what would need to break for this company to underperform expectations?
- Identify the single largest risk to the thesis within the peer group context.
- What early warning signals might be forming in the earnings data (margins under pressure, growth decelerating, working capital deteriorating)?
- Through what mechanism might {TICKER} lose ground relative to peers?

**Coverage:** 8-12 parent bullets + sub-bullets. This is the dedicated cross-cutting sceptical synthesis. The per-section sceptical bullets above feed in here. DO NOT just restate them — synthesise them into a coherent bear case.

**End:** No sceptical bullet at end (the whole section is sceptical). Instead end with: "Confidence in thesis: HIGH / MEDIUM / LOW — verbal verdict only, ≤30w, NOT a grade." (This is RESEARCHER's confidence in the *positive thesis*, not a rating of the company. APM rates.)

---

## AGGREGATE BLOCKS (after §9)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly worse than peer median.

**Format:** `❌ Signpost: finding statement. Peer anchor. [Cross-ref: §X]`

**Example:** `❌ NWC days: 78 days vs peer median 52 — Bufab carries 50% more working capital than median peer. [Cross-ref: §8]`

RESEARCHER does NOT grade these. Surface, anchor, cross-reference. APM grades.

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design — if every memo flags 5+ outliers, the marker is meaningless.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `⚡ RARE: NWC release: SEK 480m released in Q3-24 — only Bufab in 12-peer group released NWC during destocking cycle. [Cross-ref: §8]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel into the memo at post time. RESEARCHER does NOT author the structured table — the validator computes every metric. RESEARCHER DOES author the Qualitative Commentary block immediately below.

The panel is plain-text-with-markdown. Visual styling (status pill colours, summary-bar layout, gate-table CSS) is owned by the SA - Ratings Dashboard project (D-RSR-21) and applied at render time downstream of this memo.

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS] / [C] / [C+AS]
**Stage:** Triaging
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

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say. This is the qualitative interpretation Richard reads alongside the structured table.

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
2. **Signposted with verdict-flavoured labels.** Canonical: "Net QC verdict:", "Warning context:", "Source breadth note:", "Counter-hypothesis check (AI-Dunning-Kruger):". Invent additional labels per SIGNPOST DISCRETION clause where pattern warrants.
3. **Specific not generic.** "Underline density borderline at 16 across 10 parents" not "underlines look fine."
4. **Cross-reference the body.** "Surfaced in §8 + Outliers block" — point to where the data lives.
5. **No A-F or R/O/Y/G grades** (per D-RSR-3, RESEARCHER does not grade — verbal verdict only).
6. **STRICTLY separate SS and expert call counts.** If the breadth note covers both, name them distinctly: "SS: 6 of 8 brokers cited; experts: 2 expert calls in addition."
7. **No empty restating.** "Memo passes all gates" with no further context = anti-pattern. Add interpretation.

---

## SOURCE-SPECIFIC DELTA — [AS] version

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

Before extracting any content, perform this pre-flight check:

1. **Query AS for SS pool size:** "How many sell-side analysts in the AlphaSense library currently cover {COMPANY} ({TICKER})? List the broker names." Record this as the AS pool size `Z` and the broker name list.

2. **Consult the FULL pool, not a subset.** Do NOT default to citing one or two preferred brokers. Read across every named broker in the AS pool where their research is relevant to earnings trends — revenue, margins, EPS, guidance, peer momentum. Where a broker has no relevant research for this query, note that explicitly (e.g. "UBS — no recent earnings-trends coverage found in last 12M") rather than silently dropping them.

3. **Name each broker cited.** When citing SS material, name the broker every time. Format: "[AS-Berenberg]" or "[AS-Citi]" prefix on the bullet, or inline "...per Berenberg's 12-Mar-26 note" framing.

4. **Strict separation from expert calls.** Expert calls are a distinct source type. Do NOT count expert calls toward SS breadth. If you cite an expert call, mark it as `[AS-Expert]` (with the expert's anonymised role/title), never as `[AS-Broker]`.

5. **Output the breadth metadata at memo-end.** Ensure the following fields are written into metadata.json by the parent RESEARCHER:
   - `ss_pool_size`: Z
   - `ss_brokers_cited`: list of distinct broker names
   - `expert_calls_cited`: list of distinct expert call references
   - `expert_call_count`: integer

**Why this matters:** Sell-side gives Watson access to information [C] / WebSearch cannot reach (proprietary research, broker estimates, analyst commentary). Memos that cite "SS consensus" while citing only 2 of 8 covering brokers materially distort Richard's read. The 5L gate enforces breadth structurally; this prompt instruction enforces it at source.

**Data sources for [AS] version:**
- AlphaSense expert calls (CMDs, results calls, sector roundtables)
- Sell-side research: all major analysts covering {TICKER} and peers
- Company filings: most recent 2-3 quarterly results and annual reports
- Consensus data: earnings estimate changes, revisions, rating changes over L12M

**[AS]-specific analytical lens:** sell-side revisions and analyst commentary are first-class data sources. Where [AS] expert call transcripts surface management commentary that diverges from the public guidance, flag explicitly with `⚡ RARE` if material.

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: `"{COMPANY} earnings trends {PEERS} comparative analysis revenue margin EPS"`.
- Secondary searches: sector context, value chain dynamics, macro tailwinds/headwinds.
- Screenshot verification: confirm Deep Research mode active, verify data sourcing.
- Read `notion-posting-sop.md` before posting output to Notion.
- Post to Notion Stock Notes with `[AS]` tag and date.

---

## SOURCE-SPECIFIC DELTA — [C] version

**Data sources for [C] version:**
- WebSearch: public company filings (latest 2-3 quarterly results + annual reports)
- Earnings releases and investor presentations
- News and market commentary on {TICKER} and peer group
- Industry reports and sector analysis

**[C]-specific analytical lens:** WebSearch surfaces public filings + news + investor presentations. [C] does NOT have access to AS expert calls or proprietary sell-side research. Where [C] cannot source a peer-anchor data point that [AS] would have, flag with `quality_flag: thin_peer_context` rather than guess.

**Execution:**
- Use WebSearch to access public filings, earnings releases, investor presentations.
- Focus on: latest quarterly results, forward guidance, peer benchmarking, sector trends.
- Cross-reference financial metrics across peer group from latest reported data.
- Integrate recent news and market commentary.
- Do NOT include footnotes/endnotes/links in final memo.
- Post to Notion Stock Notes with `[C]` tag and date.

---

## SUPPLEMENTARY QUANTITATIVE CONTEXT (24-Apr-26)

Before writing, check the **Master Dashboard** data files for {TICKER} to ground the analysis with the latest quantitative screening data:

- `master-dashboard/data/factset-ssem.json` — SS estimates revision % and momentum count. Use to calibrate §4 (EPS trajectory) and §5 (guidance vs consensus). Provides a quantitative anchor for the qualitative AlphaSense / Claude research.
- `master-dashboard/data/factset-valuation.json` — P/E current and 10Y percentile. Use to contextualise §9 (sceptical synthesis) — is the market pricing the trends you've identified?

**AlphaSense remains the overwhelming primary source** for the [AS] version of this query. The Master Dashboard data is supplementary context — a quantitative cross-check, not a substitute for the deep sell-side and transcript analysis.

---

## VALIDATION GATES (auto-applied at post time)

The validator runs at gate point before any Notion post. Output must pass:

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1-§9 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (§1-§8) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately (not overused) | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| **SS breadth ratio (5L) ≥40%** | hard floor | BLOCK or regenerate (legitimate_source_paucity bypass available if Z<3) |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged in QC table; no blocking |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS / web returns genuinely thin source material (e.g. small-cap with no broker coverage), word-count gate bypasses; structural gates (BLUF, signposts, peer context where applicable, sceptical bullet) still apply. Auto-flag, APM ratifies at Phase 4.5 hot wash.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

Before declaring complete, RESEARCHER verifies:

- [ ] Mission compass clear: have I benchmarked {TICKER} fundamentally vs peers, identifying relative momentum?
- [ ] Reader priorities applied: am I prioritising findings that bear on 18M-3Y EPS trajectory + 25% IRR potential?
- [ ] All 9 sections present, each with J-front verdict bullet and sceptical bullet.
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs (except optional 1-2 sentence inline scene-setter top of §1).
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used where applicable; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Master Dashboard cross-check done (factset-ssem.json + factset-valuation.json).
- [ ] metadata.json written.
- [ ] Sceptical synthesis in §9 actually synthesises — doesn't just restate per-section sceptical bullets.
- [ ] AS pool size Z queried and recorded in metadata.json (`ss_pool_size`).
- [ ] Distinct named SS brokers cited (Y); ratio Y/Z computed; `ss_breadth_gate` result recorded.
- [ ] Expert calls counted SEPARATELY (no conflation with SS); `expert_call_count` + `expert_calls_cited` recorded.
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored (3-4 bullets, signposted, ≤30w each, specific not generic).

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Earnings & Fundamental Trends [AS or C] @ DD-Mon-YY`
Tags: `#Triaging #Earnings #Trends`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only (per spec §16); never highlight whole bullets.

---

*End of Q4 ET — AFTER v3 draft (v2.1 pattern). Awaiting Richard's re-review.*
