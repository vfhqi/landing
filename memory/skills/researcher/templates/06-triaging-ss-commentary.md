# Query 6: Sell-Side Commentary Summary

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/06-triaging-ss-commentary.md`. Standard v2.1 pattern. NO BB#2 overlay (Q6 is SS-survey-focused). **5L SS breadth gate is LOAD-BEARING for Q6** — the entire query is about SS coverage breadth and depth, so the 5L gate is the central QC check.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Reader has read Q1 IG BD. Start directly with the SS analyst survey.

---

## MISSION

Comprehensive survey of all sell-side analyst views covering {TICKER} ({COMPANY}). Map rating distribution, price targets, forecast changes, and narrative themes. Identify consensus view and outliers. Track analyst migration over L12M.

Output: comprehensive memo, target {WORD_TARGET} words (default ~5,000-6,000w under v2.1 density doctrine; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section. **5L gate is the central QC check — Q6 cannot ship if SS breadth ratio < 40%.**

---

## CONTEXT — What the Reader Cares About

The reader is Richard Black, a concentrated long-only equity investor (5-15 positions), UK/European focus, $5-50bn market cap. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**Triaging purpose:** Fast, disciplined filtering at LIGHT depth. Does this stock fit a recognisable setup profile? Is the fulcrum driver plausible? Pattern recognition + "strong views, weakly held."

**For this query specifically:** The reader wants to understand what sell-side analysts collectively think about {COMPANY}'s prospects. Are they bullish, sceptical, or split? Have analysts been revising estimates up or down? Are there any credible contrarian views? This calibrates the investment opportunity: is the market consensus underestimating or overestimating the company? **Sceptical analysis is key — most analysts are buy-rated by default; hold/sell ratings are the signal.**

**What downstream uses this output:** APM A&J reads this memo to populate Pillar P5 (Sell-Side Earnings Momentum) AND to triangulate against APM's own thesis. SS dispersion + outlier analysis is the load-bearing input — does APM's view align with consensus or stand against it? Memo also surfaces on the RESEARCH STAGES dashboard tab.

**Why 5L is load-bearing:** Q6 IS the SS-survey query. If the memo cites only 2 of 8 covering brokers, it's not a survey — it's a sample. The 5L gate enforces breadth. AS has a documented tendency to over-weight one or two preferred brokers; this query MUST consult the full pool.

---

## DEPTH AND COMPLETENESS — MANDATORY

Aim for comprehensive coverage. Every analytical sub-question named in SECTIONS TO COVER must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*.

**Be very granular:** cover every active analyst covering the stock. The §10 Specific Analyst Perspective section is per-analyst by design. If 8 analysts cover {TICKER}, the §10 section has 8 analyst profiles — not "the top 3."

If in doubt, write more substantive bullets rather than longer ones. Tilt conservative/sceptical: most analysts are buy-biased by default; treat holds/sells as signal. Fact-check all figures.

**The test:** would Richard learn something about the analyst landscape from this memo that he couldn't get from a Bloomberg consensus screen? If the bullet just restates the average price target, it's filler. If it triangulates ratings + revisions + narrative themes + outlier credibility — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

### Doctrine summary
- **Bulleted output throughout.** No prose paragraphs anywhere except: 1-2 sentence inline scene-setter at top of §1.
- **Parent bullets ≤30 words. Sub-bullets ≤25 words. Max 2 levels of nesting.**
- **One analytical dimension per bullet.**
- **Signpost prefixes** (demi-bold + colon) on every parent bullet. SIGNPOST DISCRETION clause applies.
- **Peer / base-rate anchor** on every quantitative claim. Specific peer name OR sector median — never a number in isolation.
- **Named broker every time.** Every SS reference names the broker (e.g. "[AS-Berenberg]" prefix or inline framing). NEVER aggregate as "consensus says X" without naming the brokers behind the claim.
- **J-front verdict bullet** at top of every section. NOT a grade.
- **Per-section sceptical bullet** at bottom of every section. Open-framed.
- **IAJA suffix tags:** `[#J]` / `[#A]` / `[#I]`.
- **❌ inversion marker** on findings clearly worse than peer median.
- **⚡ RARE marker** on genuine outliers — encompasses (a) statistical outliers (top/bottom 5% on some dimension — e.g. analyst is the only sceptic in a 12-broker BUY stack), (b) deliberately-weird signals (qualitative oddities the analyst hasn't explained, conviction language that diverges from the rating, "things that make me go hmmmm"). Sparse-by-design — ≤3 per memo.
- **Inline highlights** (green/yellow/red phrase-level spans).

### SIGNPOST DISCRETION (use canonical first, invent where pattern warrants)

Three guardrails: (1) canonical first, (2) ≤4 words demi-bold + colon, (3) single analytical dimension.

### Memo skeleton

```
1. METADATA HEADER
2. KEY FINDINGS (BLUF) — 5-10 parent bullets
3. BODY SECTIONS §1-§11
4. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
5. AGGREGATE OUTLIERS (⚡)
6. QC AUDIT PANEL (validator-filled — 5L LOAD-BEARING)
7. QC COMMENTARY (RESEARCHER-authored)
8. QC FOOTER
```

---

## SECTIONS TO COVER

### §1 — Executive summary (consensus snapshot + outliers)

**Open with J-front verdict bullet:** Net signal on {TICKER}'s sell-side coverage — bullish consensus, sceptical consensus, or split — ≤30w.

**Canonical signpost vocabulary:** "Active analysts:", "Pool size (Z):", "Buy / Hold / Sell:", "Consensus PT:", "Implied return:", "Consensus EPS:", "Consensus revenue:", "Consensus narrative:", "L12M revision pattern:", "Mood shift:", "Outlier — bullish:", "Outlier — sceptical:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Total number of active analysts covering {TICKER} — distribution by rating (Buy / Hold / Sell / Neutral). MUST match `ss_pool_size` (Z) in metadata.json.
- Consensus price target vs current share price — implied return, timeframe.
- Consensus EPS estimates: current FY, next FY, FY+2 — direction vs prior consensus.
- Consensus revenue growth expectations: forward 12-24 months.
- Key consensus narrative: what is the market story about this company?
- Major estimate revisions over L1M, L3M, L12M — direction and magnitude.
- Analyst mood: more bullish, more sceptical, or unchanged over L12M?
- Notable outliers: most bullish and most sceptical analysts — credibility assessment.
- Red flags from sell-side: top concerns mentioned across analyst notes.
- Overall calibration: is consensus appropriately calibrated, too bullish, or too sceptical?

**Coverage:** 8-12 parent bullets + sub-bullets. Pool size Z + Y/Z ratio mandatory in this section.

**End with sceptical bullet:** "What might invalidate the consensus read? Through what mechanism might the apparent consensus be a one or two analysts dominating with the rest passive?"

---

### §2 — Rating distribution + migration

**Open with J-front verdict bullet:** Net signal on rating distribution health and migration direction — ≤30w.

**Canonical signpost vocabulary:** "Buy count:", "Hold count:", "Sell count:", "Neutral count:", "Consensus rating:", "Migration L3M:", "Migration L6M:", "Migration L12M:", "Recent upgrade:", "Recent downgrade:", "Recent initiation:", "Herding signal:", "Diversity signal:", "Hold/sell credibility:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Current rating distribution: number and % of Buy, Hold, Neutral, Sell, Outperform, Underperform.
- Consensus rating if available (e.g., "overweight" if more buys than sells).
- Migration of ratings over L3M, L6M, L12M: any analysts moving more bullish/sceptical?
- Most bullish (highest price targets) — track record and credibility.
- Most sceptical (lowest price targets, holds, sells) — track record and credibility.
- Do hold/neutral/sell ratings come from credible contrarian thinkers or are they outliers?
- Is there herding (majority of same rating) or diversity?
- Recent initiations, upgrades, downgrades in past 12M? Timing and rationale?

**Coverage:** 10-15 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on the rating distribution? Through what mechanism might the buy consensus be too default? What's the credibility-adjusted read on the contrarian holds/sells?"

---

### §3 — Price targets + valuation

**Open with J-front verdict bullet:** Net signal on price-target dispersion + implied return — ≤30w.

**Canonical signpost vocabulary:** "Consensus PT:", "PT range:", "Highest PT:", "Lowest PT:", "Implied return:", "Best case:", "Worst case:", "Valuation method:", "P/E assumed:", "EV/EBITDA assumed:", "DCF assumption:", "PT trend L1M:", "PT trend L3M:", "PT trend L12M:", "PT accuracy:", "Sector premium:", "Sector discount:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Consensus price target: average and median across all analysts.
- Price target range: highest target (most bullish) and lowest (most sceptical).
- Implied return from consensus target: vs current price, upside/downside %.
- Implied return from high and low targets: best/worst case scenarios.
- Valuation assumptions behind consensus target: P/E multiples, EV/EBITDA, DCF.
- Changes in price target consensus over L1M, L3M, L12M: trending higher or lower?
- Which analysts have been most accurate on price target calls historically?
- Valuation vs sector/peers: premium, parity, or discount? Justified?

**Coverage:** 10-15 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on price target credibility? Through what mechanism might targets be assuming continued strong execution? What's the bear-case valuation?"

---

### §4 — Earnings estimate changes

**Open with J-front verdict bullet:** Net signal on estimate revision momentum — ≤30w.

**Canonical signpost vocabulary:** "Consensus EPS — FY:", "Consensus EPS — FY+1:", "Consensus EPS — FY+2:", "Implied EPS growth:", "Revision direction L1M:", "Revision direction L3M:", "Revision direction L12M:", "Magnitude:", "Broad-based revision:", "Concentrated revision:", "Revision timing:", "Reactive vs proactive:", "vs management guide:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Consensus EPS estimates: current FY, next FY (FY+1), FY+2.
- EPS growth rates implied by consensus: 12M forward, 24M forward.
- Direction of consensus revisions over L1M, L3M, L12M: upgraded, maintained, or downgraded?
- Magnitude of revisions: which analysts moving most? Biggest upside and downside revisions?
- EBIT/EBITDA estimate changes: direction, magnitude, which analysts.
- Revenue estimate changes: direction, magnitude, which analysts.
- Pattern: broad-based or concentrated revisions?
- Timing: reactive (post-earnings) or proactive (pre-announcement)?
- Consensus vs company guidance: do analysts believe management?

**Coverage:** 12-18 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on estimate momentum? Through what mechanism might revisions be assuming revenue growth that is slowing? Are margin assumptions realistic?"

---

### §5 — Revenue + growth forecasts

**Open with J-front verdict bullet:** Net signal on growth assumption credibility — ≤30w.

**Canonical signpost vocabulary:** "Consensus revenue — FY:", "Consensus revenue — FY+1:", "Organic vs inorganic:", "Segment forecast:", "Geographic forecast:", "Revision L1M:", "Acceleration assumed:", "Deceleration assumed:", "Market growth assumed:", "Share gain assumed:", "Pricing assumed:", "End-market outlook:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Consensus revenue growth expectations: current FY, next FY, FY+2.
- Organic vs inorganic (M&A) growth assumptions in consensus forecasts.
- Revenue forecast by segment/geography where analysts provide detail.
- Changes in growth expectations over L1M, L3M, L12M: upgraded or downgraded?
- Do analysts expect acceleration or deceleration in growth trajectory forward?
- Consensus assumptions on market growth, market share gains/losses, pricing power.
- End-market outlook from analyst commentary.

**Coverage:** 10-15 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on growth forecasts? Through what mechanism might assumptions be unachievable? What would cause revenue miss?"

---

### §6 — Margin + profitability outlook

**Open with J-front verdict bullet:** Net signal on margin assumption credibility — ≤30w.

**Canonical signpost vocabulary:** "Consensus gross margin:", "Consensus EBIT margin:", "Consensus net margin:", "Margin trend assumed:", "Productivity assumption:", "Pricing assumption:", "Mix assumption:", "Operating leverage:", "Fixed cost:", "One-off vs structural:", "Margin downgrade:", "Margin upgrade:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Consensus margin expectations: gross, EBIT, net margin for current FY and next FY.
- Margin trend assumptions: expanding, contracting, or stable?
- Drivers of margin assumptions: productivity, pricing, mix, leverage.
- Operating leverage expectations: as revenue grows, do margins expand?
- Cost structure: fixed costs declining as % of revenue?
- One-off vs structural margin improvement.
- Changes in margin assumptions over L12M: downgrades or upgrades?

**Coverage:** 10-15 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on margin outlook? Through what mechanism might margin assumptions be aggressive? What could cause compression?"

---

### §7 — Narrative + market story

**Open with J-front verdict bullet:** Net signal on consensus narrative — bullish thesis, bearish thesis, narrative shift — ≤30w.

**Canonical signpost vocabulary:** "Bull case:", "Bear case:", "Bullish theme:", "Sceptical theme:", "Narrative shift L12M:", "Tone shift:", "Near-term focus:", "Medium-term focus:", "Original insight:", "Management echo:", "Narrative credibility:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Dominant bull case narrative among analysts (3-4 sentences).
- Dominant bear case narrative from hold/sell analysts (3-4 sentences).
- Key positive themes: what are analysts most bullish about?
- Key negative themes: what are analysts most concerned about?
- Changes in narrative tone over L12M.
- Are analysts focused on near-term results or medium-term transformation?
- Quality of analyst commentary: original insights or repeating management?
- Credibility of key narrative drivers.

**Coverage:** 12-18 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on the bull narrative? Does it assume continued execution that may not materialise? What hidden risks?"

---

### §8 — Hold/sell analyst deep dive (LOAD-BEARING)

**Open with J-front verdict bullet:** Net signal on contrarian view credibility — ≤30w.

**Canonical signpost vocabulary:** "Hold/sell analyst:", "Specific concern:", "Valuation-driven:", "Fundamentals-driven:", "Track record:", "Tenure of skepticism:", "Upgrade trigger:", "Outlier insight:", "Missing information:", "Contrarian conviction:". Invent where pattern warrants.

**Analytical sub-questions to address (LOAD-BEARING — most valuable contrarian insight):**
- Identify all hold/neutral/sell-rated analysts by name and firm.
- For each: specific concern or thesis.
- Valuation-driven (stock expensive) or fundamentals-driven (earnings concerns)?
- Track record and credibility of skeptical analysts: right or wrong historically?
- How long have they maintained these ratings?
- What would need to change for them to upgrade?
- Are skeptical analysts outliers with unique insight, or missing something obvious?

**Coverage:** 10-15 parent bullets + sub-bullets. **Per-analyst treatment** for every hold/sell/neutral analyst (named).

**End with sceptical bullet:** "Are the contrarian analysts correctly identifying risks the consensus is missing, or are they wrong? What's the credibility-weighted read?"

---

### §9 — Changes in analyst estimates + ratings over L12M

**Open with J-front verdict bullet:** Net signal on revision momentum and direction — ≤30w.

**Canonical signpost vocabulary:** "Analyst:", "Change date:", "Direction:", "Magnitude:", "Rationale:", "Reactive:", "Proactive:", "Pattern:", "Momentum:", "Recent shift:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Each analyst who has made changes to ratings or price targets in L12M.
- Timing relative to company announcements or earnings.
- Direction: upgrades, downgrades, initiations.
- Magnitude: PT changes as $ and %, rating moves.
- Rationale: what drove the moves?
- Pattern: broad consensus shift or concentrated?
- Reactive or proactive?
- Momentum: are recent changes still pointing up/down?

**Coverage:** 10-15 parent bullets + sub-bullets. Mandatory: revision-history table (analyst × date × old rating / new rating × old PT / new PT × rationale).

**End with sceptical bullet:** "What's the bearish read on revision momentum? If multiple analysts have downgraded, is consensus following? If nobody downgraded, are they complacent?"

---

### §10 — Specific analyst perspective summary (PER-ANALYST)

**Open with J-front verdict bullet:** Net signal on per-analyst landscape — ≤30w.

**Canonical signpost vocabulary:** "Analyst:", "Firm:", "Rating:", "PT:", "Thesis:", "Recent change:", "Track record:", "Unique perspective:", "Watch item:", "Credibility:". Invent where pattern warrants.

**Analytical sub-questions to address (PER-ANALYST):**

For EACH major analyst covering {TICKER}, provide a brief profile:
- Analyst name, firm, rating, price target.
- Key thesis (2-3 sentences): bullish or skeptical about what?
- Recent changes: rating/target in L6M? Direction and magnitude?
- Historical track record (if known): accurate on this stock? On the sector?
- Unique perspective or following consensus?
- Key watch items from their notes.
- Credibility assessment.

**Coverage:** ONE parent bullet per analyst (with sub-bullets for thesis + watch items + credibility). If 8 analysts cover the stock → 8 parent bullets minimum. Market-cap-weighted emphasis (focus on larger brokers and influential analysts first, but cover every named analyst).

**End with sceptical bullet:** "Across the analyst pool, where is original insight vs herding? Which analyst has the most credible non-consensus view?"

---

### §11 — Consensus calibration + risks + sceptical synthesis

**Open with J-front verdict bullet:** Cross-cutting bearish synthesis — what is the strongest bearish case given everything above? — ≤30w.

**Canonical signpost vocabulary:** "Consensus calibration:", "Sound analysis:", "Questionable assumption:", "Underweighted risk:", "Tail risk — downside:", "Tail risk — upside:", "Reverse-engineered bear:", "Single largest risk:", "Estimate downside:", "Red flag:". Invent where pattern warrants.

**Analytical sub-questions to address:**
- Is consensus appropriately calibrated to opportunity/risk? Explain judgment.
- What is consensus getting right? Where is analysis sound?
- What is consensus getting wrong? Where are assumptions questionable?
- Top 3-5 risks consensus is underweighting.
- What would need to go wrong for consensus to be significantly revised down?
- Tail risks (downside scenarios) analysts haven't fully priced.
- Upside scenarios analysts are missing.
- Reverse-engineer the most credible bear case from analyst commentary.
- Highest-conviction risks mentioned across skeptical analysts.

**Coverage:** 12-15 parent bullets + sub-bullets. This is the dedicated cross-cutting sceptical synthesis.

**End:** No sceptical bullet (whole section is sceptical). Instead end with: "Confidence in consensus calibration: HIGH / MEDIUM / LOW — verbal verdict only, ≤30w, NOT a grade."

---

## AGGREGATE BLOCKS (after §11)

### Weak Signals / Downside (❌)

**Required:** 0-5 parent bullets. Each ❌ marks a finding clearly worse than peer median.

**Format:** `❌ Signpost: finding statement. Peer anchor. [Cross-ref: §X]`

**Example:** `❌ Hold/sell ratio: 5 of 8 analysts at hold/sell — only 1 of 12 sector peers exceeds 60% non-buy ratio. [Cross-ref: §2]`

### Outliers (⚡)

**Required:** 0-3 parent bullets. Sparse-by-design.

**Format:** `⚡ RARE: signpost: finding statement. Peer / base-rate anchor. [Cross-ref: §X]`

**Example:** `⚡ RARE: Skeptic credibility: 4 of 4 hold-rated analysts have positive 5Y track record on this stock — only 1 of 50 European stocks has all skeptics historically right. [Cross-ref: §8]`

---

## QC AUDIT PANEL (validator-filled at post time)

The validator script writes this panel into the memo at post time. **5L gate is LOAD-BEARING for Q6** — Q6 is the SS-survey query, so SS breadth is the central QC check.

### Required block structure

```
---

## QC Audit

**Status:** PASS / PASS+warn / FAIL
**Source:** [AS]
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
| **SS breadth ratio (LOAD-BEARING)** | YY% (Y of Z) | Q6 is the SS-survey query — breadth is the central metric |
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
| **5L** | **SS breadth ratio ≥40% (LOAD-BEARING for Q6)** | **Hard** | **✓ / ~ / ✗** |
| 5M | Expert call breadth — count + named | Warn | informational |

### Bypass flags (if any)
- `legitimate_source_paucity: true` — reason: {free text} — common for Q6 on small-caps with thin SS coverage.

### Warnings (if any)
- {Gate}: {one-line description}
```

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 3-4 free-flowing bullets summarising what the structured numbers say. **For Q6, the SS breadth note is mandatory and load-bearing.**

### Required block structure

```
### QC Commentary

- **Net QC verdict:** {≤30w headline judgement on memo quality}
- **Warning context:** {≤30w if any warnings fired — why and whether they matter}
- **SS breadth note (LOAD-BEARING for Q6):** {≤30w on SS breadth — pool size Z, brokers cited Y, ratio Y/Z, named brokers omitted with reason}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view + counter-hypothesis + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing.}
```

### Authoring rules

1. **3-4 bullets, each ≤30 words.**
2. **Signposted with verdict-flavoured labels.**
3. **Specific not generic.** "SS breadth 75% (6 of 8 named brokers cited; UBS + Citi omitted with explicit no-coverage notes)" not "SS breadth fine."
4. **Cross-reference the body.** "Surfaced in §1 + §10 per-analyst section."
5. **No A-F or R/O/Y/G grades.**
6. **STRICTLY separate SS and expert call counts.** "SS: 6 of 8 named brokers cited; experts: 0 expert calls (Q6 is SS-only)."
7. **No empty restating.** Add interpretation, not echo.

---

## SOURCE-SPECIFIC DELTA — [AS] version (NO [C] VERSION)

This is an **AS-only query**. Sell-side research is the core competency required — AS provides direct access to analyst reports, consensus databases, and rating changes. Native Claude research cannot replicate the depth of analyst coverage analysis.

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

**LOAD-BEARING for Q6** — the entire query is about SS breadth.

Before extracting any content, perform this pre-flight check:

1. **Query AS for SS pool size:** "How many sell-side analysts in the AlphaSense library currently cover {COMPANY} ({TICKER})? List the broker names." Record this as the AS pool size `Z` and the broker name list. **For Q6, Z populates §1 directly.**

2. **Consult the FULL pool — every named broker.** Do NOT default to citing one or two preferred brokers. For Q6 specifically, EVERY named broker in the AS pool gets at least one mention in §10 (Specific Analyst Perspective). Where a broker has no relevant research for this query, note that explicitly (e.g. "UBS — no recent post-earnings note found in last 12M; coverage paused pending FY24 results").

3. **Name each broker cited.** When citing SS material, name the broker every time. Format: "[AS-Berenberg]" or "[AS-Citi]" prefix on the bullet, or inline framing.

4. **Strict separation from expert calls.** Expert calls are a distinct source type. Mark expert calls as `[AS-Expert]` (with anonymised role/title), never as `[AS-Broker]`. **For Q6, expert calls are typically rare** — Q6 is SS-survey, not expert-call-survey.

5. **Output the breadth metadata at memo-end.** Ensure metadata.json contains: `ss_pool_size` (Z), `ss_brokers_cited` (list), `expert_calls_cited` (list, often empty for Q6), `expert_call_count` (typically 0 or low for Q6).

**Why this matters for Q6:** Q6 IS the SS-survey query. A Q6 memo citing 2 of 8 covering brokers isn't a survey — it's a sample. The 5L gate enforces breadth structurally; this prompt instruction enforces it at source.

**Data sources for [AS] version:**
- AlphaSense research database: all analyst reports on {TICKER} covering L12M.
- Consensus data: analyst ratings, price targets, earnings estimates, revisions over L12M.
- Company earnings calls & CMDs: analyst Q&A and commentary L12M.
- Sell-side initiation and upgrade/downgrade notes: rationale for changes.

**Execution:**
- Open AlphaSense Deep Research mode (full-screen 1920×1080).
- Search query: `"{TICKER} {COMPANY} sell-side analyst coverage ratings price targets"`.
- Secondary searches: analyst consensus, earnings estimate revisions, rating changes L12M.
- Screenshot verification: confirm Deep Research mode active, verify data sourcing.
- Screenshot ALL analyst-level data (ratings, targets, estimates) for fact-checking.
- Read `notion-posting-sop.md` before posting output to Notion.
- Post to Notion Stock Notes with `[AS]` tag and date.

**NOTE: This template is AlphaSense ONLY. No Claude [C] native research version.**

---

## VALIDATION GATES (auto-applied at post time)

| Gate | Threshold | Action on fail |
|---|---|---|
| metadata.json present + schema valid | required | BLOCK post (no bypass) |
| Word count ≥50% of {WORD_TARGET} | hard floor | BLOCK post; regenerate or escalate |
| Word count ≥75% of {WORD_TARGET} | quality gate | BLOCK pending section coverage check |
| Section coverage: §1-§11 all present | required | BLOCK post |
| BLUF present in first 800w | required | BLOCK post |
| Signpost coverage on parent bullets | ≥80% | BLOCK or regenerate |
| Peer-context density on quantitative claims | ≥30% | quality_flag: thin_peer_context, post with flag |
| J-front ordering (first bullet of each section) | required | quality_flag: ordering_violation, post with flag |
| Per-section sceptical bullet present | required (§1-§10) | BLOCK post |
| Aggregate Weak Signals block present | required | BLOCK post |
| ❌ markers used appropriately (not overused) | guideline | quality_flag if >10 ❌ in memo |
| ⚡ RARE markers sparse | ≤3 per memo | quality_flag if exceeded |
| Invented signposts logged in QC footer | required if any used | BLOCK post if missing |
| Mandatory revision-history table (§9) | required | BLOCK post |
| Per-analyst coverage in §10 (one bullet per Z brokers) | required | BLOCK post |
| **SS breadth ratio (5L) ≥40% — LOAD-BEARING for Q6** | hard floor | BLOCK or regenerate (legitimate_source_paucity bypass available if Z<3) |
| **SS breadth ratio (5L) ≥70%** | quality gate | quality_flag: ss_breadth_thin, post with flag |
| **Expert call breadth (5M)** | informational | count + named list logged in QC table; no blocking |
| **In-memo QC Audit panel + Qualitative Commentary** | required | BLOCK post if missing |
| **No A-F or R/O/Y/G grades anywhere** | required (RESEARCHER does NOT grade) | BLOCK post + escalate |

**Bypass:** `legitimate_source_paucity: true` — when AS returns genuinely thin SS coverage (e.g. small-cap with Z<3 covering brokers), word-count gate AND 5L gate bypass with reason logged. Common for Q6 on small-caps. APM ratifies at Phase 4.5 hot wash.

---

## QUALITY CHECKLIST (RESEARCHER's pre-submit self-check)

- [ ] Mission compass clear: have I surveyed all SS analysts covering {TICKER} with rating distribution + revision pattern + narrative themes?
- [ ] Reader priorities applied: hold/sell credibility front-and-centre (sceptical analysis is key for Q6).
- [ ] All 11 sections present, each with J-front verdict bullet and sceptical bullet.
- [ ] Every quantitative claim has a peer / base-rate anchor.
- [ ] No A-F grades, no R/O/Y/G grades anywhere.
- [ ] No prose paragraphs (except optional 1-2 sentence inline scene-setter top of §1).
- [ ] Parent bullets ≤30 words; sub-bullets ≤25 words; max 2 nesting levels.
- [ ] Signpost prefix on every parent bullet; canonical vocabulary used; invented signposts logged.
- [ ] IAJA suffix tag on every parent bullet.
- [ ] Aggregate Weak Signals block present, cross-referenced to sections.
- [ ] Aggregate Outliers block sparse and substantive.
- [ ] Mandatory revision-history table (§9) present.
- [ ] §10 per-analyst section covers EVERY named broker in Z (one parent bullet per analyst minimum).
- [ ] metadata.json written.
- [ ] Sceptical synthesis in §11 actually synthesises — doesn't just restate per-section sceptical bullets.
- [ ] **AS pool size Z queried and recorded in metadata.json (`ss_pool_size`).**
- [ ] **Distinct named SS brokers cited (Y); ratio Y/Z computed; `ss_breadth_gate` result recorded.**
- [ ] **Y ≥ 70% of Z (target) OR Y ≥ 40% of Z (hard floor) OR `legitimate_source_paucity: true` with reason logged.**
- [ ] Expert calls counted SEPARATELY (no conflation with SS); typically 0 or low for Q6.
- [ ] In-memo QC Audit panel rendered at bottom of memo (validator-filled).
- [ ] Qualitative QC Commentary block authored — **SS breadth note mandatory and load-bearing for Q6.**

---

## NOTION POSTING CONVENTION

Title: `[W] {TICKER} — Sell-Side Commentary [AS] @ DD-Mon-YY`
Tags: `#Triaging #SellSide #Survey #Pillar5`
Highlighting: 30%+ coverage via `process_report.py`. Inline phrase-level highlights only.

---

## EXECUTION

**AlphaSense [AS] only.** No Claude [C] version. Sell-side research is core competency required for Q6.

Parent RESEARCHER handles extraction, highlighting, formatting, and Notion posting.

---

*End of Q6 Triaging SS Commentary — AFTER v1 draft (v2.1 pattern, 5L LOAD-BEARING). Awaiting Richard's review with rest of BATCH 1.*
