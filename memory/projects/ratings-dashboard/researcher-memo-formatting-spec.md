# Researcher Memo Formatting Spec v1.0

**Status:** v1.2 — aggressive splitting + inline highlights + full re-render mandate (05-May-26)  
**Scope:** All researcher memos (v0.1 patched + batch-rendered = 346 files). NOT V20/APM memos.  
**Query types covered:** BD, CF, SS, KD, ET, ED (all stages: IG, Triaging, ESA)  
**Base:** Notion posting standard, adapted for HTML, with specific APM rules ported.

---

## 1. Document Structure

| Element | Rule |
|---------|------|
| **H1** | Memo title (ticker + query name). One per memo. |
| **H2** | Major sections (descriptive names: "Key Findings", "Revenue Model", "Competitive Dynamics" — never generic like "Section 1") |
| **H3** | Sub-sections where needed within an H2 block. Optional. |
| **No H4+** | Maximum three levels of heading hierarchy. |
| **Horizontal rules** | Between H2 sections only. Visual breathing room, not clutter. |

## 2. Key Findings Block (BLUF)

Every memo opens with a **Key Findings** section immediately after the metadata header:

- 5–10 parent bullets maximum
- Each bullet = one headline judgement or critical finding (≤30 words)
- Ordered J→A→I (judgements first, then analysis, then information)
- Highlighted per existing colour system (green/yellow/red)
- This is the "skim layer" — a reader who reads nothing else gets the picture

## 3. Bullet Discipline

| Rule | Spec |
|------|------|
| **Parent bullet length** | ≤30 words. Headline/verdict. No prose paragraphs disguised as bullets. |
| **Sub-bullet role** | Evidence, data, or elaboration supporting the parent. |
| **Max sub-bullets** | 6 per parent. If more needed, split the parent or promote to new section. |
| **Max nesting** | 2 levels only (parent → sub-bullet). No grandchildren. |
| **No trailing periods** | Bullets are fragments, not sentences. No full stops at end. |
| **No em-dashes** | Use colons, commas, or parentheses instead. |

## 4. Emphasis & Skim Anchors

| Tool | Usage |
|------|-------|
| **Underline** | 10–30% of each parent bullet's text. Anchor to verb/number/pivoting-phrase/flip-condition. The "eye-catch" for fast scanning. |
| **Bold** | First occurrence of key terms, company names, financial figures. Primary skim tool distinct from underline. |
| **Highlights** | Maintain existing 30%+ density. Green = positive/strength. Yellow = neutral/notable. Red = risk/concern/critical. |
| **Italic** | Section-level summary sentence under each H2 — one sentence stating that section's verdict before bullets begin. |

## 5. IAJA Tagging & Ordering

- **Suffix tags:** Every parent bullet tagged `#J` (judgement), `#A` (analysis), or `#I` (information)
- **Ordering within sections:** J→A→I. Lead with the verdict, support with analysis, underpin with raw information
- **Don't bury the lede:** If a section's most important point is a judgement, it goes first regardless of how it was discovered

## 6. Signposting

Parent bullets labelled with which dimension of the query they address. Lighter than APM's CQ/RA system.

**Format:** Demi-bold prefix label followed by colon, then the bullet content.

**Examples by query type:**
- BD: "Revenue model:", "Competitive position:", "Customer base:", "Cost structure:"
- CF: "Demand drivers:", "Regulatory shift:", "Technology disruption:", "Management change:"
- SS: "Consensus view:", "Variant perception:", "Catalyst timing:"
- KD: "Primary driver:", "Sensitivity:", "Structural vs cyclical:"
- ET: "Trend direction:", "Inflection signal:", "Base-rate context:"
- ED: "Beat/miss pattern:", "Guidance trajectory:", "Quality of earnings:"

## 7. Source Attribution

- Factual claims prefixed with provenance: `[AS-BrokerName]`, `[AS]`, or `[C]`
- One source tag per claim where the source is identifiable
- Not required on obvious/well-known facts or on judgements (which are Watson's synthesis)

## 8. Communication Principles (Content-Level)

These are NOT just formatting — they shape how content is written:

| Principle | Application |
|-----------|-------------|
| **Peer/base-rate context** | Every metric anchored to sector median, peer group, or historical average. Never a number in isolation. |
| **A–F inline grades** | Qualitative assessments get letter grades where applicable. Bell-curve distribution (A=top 10%, B=top 25%, C=middle, D/F=bottom). |
| **❌ Invert / call out D/F** | Weak areas get explicit ❌ prefix. Don't hide bad news in neutral language. |
| **🚩 RARE outlier** | Genuine statistical outliers (top/bottom 5%) flagged with 🚩. Use sparingly — if everything is flagged, nothing is. |

## 9. Section-Level Italic Summary

Under each H2 heading, before the bullets begin, one italic sentence summarising that section's overall verdict. Enables a reader to scan H2 + italic line and get the full story without reading any bullets.

**Example:**
```
## Competitive Position
*AENA holds an unassailable domestic monopoly but faces margin pressure from airline pushback on tariff increases.*

- Monopoly position: ...
- Airline resistance: ...
```

## 10. QC Footer

Every memo ends with a small metadata block:

```
---
Source: [AS] / [C] | Stage: Triaging | Generated: 19-Apr-26 | Words: 3,883 | Ticker: HFG
```

## 11. Horizontal Rule (Test Item)

HR between H2 sections — included as a test. Richard to confirm whether this adds visual clarity or creates clutter after seeing test memos.

## 12. Source Attribution Density (Test Item)

`[AS-Broker]` / `[C]` prefixes on individual claims — included as a test. Richard to confirm whether this level of attribution is useful vs noisy for researcher memos.

## 13. Analytical Dimension Splitting (v1.1)

**Principle:** One analytical dimension per bullet or sub-bullet. When a bullet mixes different dimensions (timing, valuation, benchmarking, significance, mechanism, profitability), split into separate bullets or sub-bullets, each with its own signpost label.

**When to split:**
- A bullet combines timing + significance → separate bullets
- A sub-bullet packs multiple facts from different dimensions (price + timing + benchmark) → split into labelled sub-bullets
- A parent bullet describes an event AND its financial terms AND its strategic context → parent = event, subs = terms/context/timing

**When NOT to split:**
- A bullet contains a single coherent thought that happens to be detailed
- Splitting would create trivially short fragments that add no scanning value
- The dimensions are so tightly coupled that separation breaks comprehension

**Signpost labels on sub-bullets:** When a parent's sub-bullets address different dimensions, each sub-bullet gets its own signpost prefix (Timing:, Multiple:, Benchmarking:, Profitability:, Plan:, etc.)

**Examples:**

Before:
```
* Healthcare sale: Sold to Investindustrial for £1.05bn EV (completed Sep 2025) #I
  * Represented ~12.2x division's 2024 adj OP; substantially above Group trading multiple
```

After:
```
* Healthcare sale: Sold to Investindustrial for £1.05bn EV #I
  * Timing: Completed September 2025
  * Multiple: ~12.2x division's 2024 adjusted operating profit
  * Benchmarking: Substantially above Group trading multiple
```

Before:
```
* Timing: November 2024; most significant strategic shift in DCC's fifty-year history
```

After:
```
* Timing: November 2024
* Significance: Most significant strategic shift in DCC's fifty-year history
```

## 14. Surface Buried Judgements (v1.1)

**Principle:** Source material often contains judgements buried in connective prose ("has fundamentally reshaped", "represents a decisive pivot", "marks a structural inflection"). These must be surfaced as explicit, signposted parent bullets positioned at the top of their section or bullet group.

**Rules:**
1. When restructuring prose into bullets, scan for judgemental language — verbs/adjectives that express evaluation, not just description
2. Extract the judgement and make it a standalone parent bullet with a verdict-flavoured signpost label: "Verdict:", "Net signal:", "Implication:", "Strategic read:", "Overall:"
3. Position the judgement bullet FIRST in its group (J→A→I ordering), before the supporting evidence bullets
4. Do NOT use "BLUF:" as a signpost label inside body sections — that label is reserved for the top-of-memo Key Findings block
5. Do NOT generate judgements that aren't in the source material — only surface those that are already present but buried

**Example:**

Source prose: "The divestment program has fundamentally reshaped DCC's capital allocation framework, enabling the company to fund its energy transition while executing a massive return of capital to shareholders."

Before (v1.0):
```
* Return programme: Divestments enabled £800m return to shareholders #I
  * £100m on-market buyback completed September 2025
  * ...
```

After (v1.1):
```
* Implication: Divestment programme has fundamentally reshaped DCC's capital allocation framework #J
* Enabler: Divestment proceeds fund energy transition + massive shareholder returns
* SBB: £800m return to shareholders (~16% of market cap at announcement) #I
  * £100m on-market buyback completed September 2025
  * ...
* Balance sheet: DCC expects to maintain investment-grade rating and ~0.9x net debt/EBITDA pro forma leverage, despite these massive distributions #J
```

Note: The judgement ("fundamentally reshaped") was in the source but got dropped in v1.0. v1.1 surfaces it. The balance sheet bullet is also reordered — key point first ("maintain investment-grade"), supporting context second ("despite distributions").

## 15. Aggressive Sub-Bullet Splitting (v1.2)

**Principle:** When a parent bullet contains semicolons, commas, or conjunctions separating distinct facts about different sub-topics (geographic regions, time periods, different metrics, different entities), ALWAYS split into parent + sub-bullets with inferred signpost labels.

**When to split:**
- A bullet uses semicolons to separate facts about different regions → split by region (Nordics:, UK:, etc.)
- A bullet packs headline metric + multiple contextual points → parent = headline, subs = context
- A bullet combines an event + its market share + its strategic significance → separate sub-bullets
- A bullet lists multiple entities or segments with individual data points → one sub-bullet per entity

**Inferred signpost labels:**
- Watson SHOULD infer contextual signpost labels even when not explicit in source text
- Geographic: "Nordics:", "UK:", "India:", "Western Europe:"
- Thematic: "Market share:", "Strategic priority:", "IPO:", "Timing:"
- Dimensional: "Volume:", "Price:", "Mix:", "Leverage:", "Organic:"

**Examples:**

Before:
```
* India: Continued positive momentum with ~20% market share and distribution expansion; medium-term IPO narrative rather than Q1 2026 material driver
```

After:
```
* India: Continued positive momentum
  * Market share: ~20%
  * Strategic priority: Distribution expansion
  * IPO: Medium-term narrative, not a Q1 2026 material driver
```

Before:
```
* Western Europe: +1.2% reported (+2.4% ex-San Miguel); Nordic weather tailwind non-recurring; Britvic soft drinks mid-single-digit growth in UK/Ireland
```

After:
```
* Western Europe: +1.2% reported (+2.4% ex-San Miguel)
  * Nordics: Weather tailwind non-recurring
  * UK/Ireland: Britvic soft drinks mid-single-digit growth
```

**When NOT to split:**
- A bullet is already a single coherent thought under 30 words
- Splitting would create trivially short fragments (<5 words) that add no scanning value
- The sub-topics are so tightly coupled that separation breaks comprehension

## 16. Inline Phrase-Level Highlights (v1.2)

**Principle:** Highlights (green/yellow/red) apply to specific PHRASES within bullets, NOT to entire bullets. The reader's eye should be drawn to the key number, verdict, or phrase — not a coloured box around everything.

**Rules:**
1. Use `<span class="m-hl-green">key phrase</span>` within bullet text
2. NEVER apply highlight class to `<li>` elements
3. Target: highlight 30%+ of text, but distributed across many inline spans (not one big block)
4. What to highlight:
   - Green: positive metrics, strength signals, favourable verdicts
   - Yellow: notable/neutral data points, things worth flagging
   - Red: risks, concerns, negative signals, weak metrics
5. Highlight the SPECIFIC phrase that carries the signal, not the entire sentence

**Example:**

Before (v1.0/v1.1 — whole bullet highlighted):
```html
<li class="m-parent m-hl-green"><span class="m-signpost">Revenue model:</span> Highly recurring with 85% contracted revenue</li>
```

After (v1.2 — inline phrase highlight):
```html
<li class="m-parent"><span class="m-signpost">Revenue model:</span> Highly recurring with <span class="m-hl-green">85% contracted revenue</span></li>
```

## 17. Two-Pass Rendering Pipeline (v1.2) — LOCKED

**LOCKED RULE:** Memo rendering is a TWO-PASS pipeline. The passes have different purposes and MUST NOT be conflated.

### Pass 1: Content Restructure (LLM, done ONCE per memo)

**Purpose:** Transform source prose into structured bullet hierarchy with IAJA tags, sections, italic summaries, highlights, signposts. All content decisions happen here.

**Input:** Source markdown file from `Files/{TICKER}/{STAGE}/{NN-CODE}/`
**Output:** Body HTML with full content preserved in structured format
**Content rule:** ALL substantive information from the source MUST appear in the output. Restructuring changes the SHAPE of content (prose → bullets), not the QUANTITY. Word count of output should be 40-60% of source word count (compression comes from removing connective prose, not from dropping facts).

**When to run:** Once per memo. The v1.0/v1.1 renders are Pass 1 outputs.

### Pass 2: Formatting Pass (mechanical, repeatable, scriptable)

**Purpose:** Apply v1.2 formatting rules to existing structured HTML. NO content decisions. NO content removal.

**Input:** Pass 1 body HTML (the v1.0 or v1.1 render)
**Output:** Same content with v1.2 formatting applied

**Operations (ONLY these, nothing else):**
1. **Split compound bullets:** Where a parent bullet contains semicolons/commas separating distinct sub-topics → split into parent + sub-bullets with inferred signpost labels
2. **Add signpost labels:** Ensure every parent bullet and dimensional sub-bullet has a signpost label
3. **Convert highlights:** Move `m-hl-*` classes from `<li>` elements to `<span>` elements wrapping specific phrases within the bullet text
4. **Consistency check:** Verify signpost labels present throughout (no "falling off" in second half)

**Content rules — HARD CONSTRAINTS:**
- Output word count MUST be >= input word count (splitting adds words)
- Output section count MUST be >= input section count (never drop H2 sections)
- NEVER summarise, condense, or rephrase existing bullet text
- NEVER drop bullets, sub-bullets, or data points
- ONLY add structure (new sub-bullets from splits, new signpost labels)

### Validation Gate (mandatory before presenting any memo)

Before presenting any formatted memo to Richard:
1. Word count check: v1.2 words >= v1.1 words
2. Section count check: v1.2 H2 count >= v1.1 H2 count
3. No H2 sections from v1.1 missing in v1.2
4. Signpost labels present on all parent bullets throughout

### Rollout Implication

For the 346-memo rollout:
- Memos that already have a v1.0/v1.1 Pass 1 render: apply Pass 2 only (formatting script)
- Memos that have no structured render yet: run Pass 1 (LLM restructure from source) then Pass 2
- Pass 2 is scriptable in Python (HTML transformation, no LLM needed for most operations)

---

## Anti-Patterns (What We're Fixing)

| Problem | Current state | Target |
|---------|---------------|--------|
| Wall of text | Entire paragraphs as single highlighted blocks (see AENA BD) | Break into ≤30w parent bullets + sub-bullets |
| No hierarchy | Flat sequence of `<p>` tags, no sections | H2 sections with descriptive names |
| No skim layer | Must read everything to find the point | Key Findings BLUF + italic summaries + bold/underline |
| Inconsistent emphasis | Some memos highlighted, some not; no underline | Consistent highlight + underline + bold system |
| No structure cues | Reader doesn't know what dimension is being discussed | Signpost labels on parent bullets |
| Missing verdict ordering | Information before judgement | J→A→I throughout |

---

## Technical Notes (for rendering script)

- Source: markdown files in `Files/{TICKER}/{STAGE}/{NN-CODE}/`
- Renderer must parse existing highlight tokens (`<span color="green_bg">` etc.)
- Output: HTML with `memo-style.css` link (stylesheet to be updated with new classes)
- New CSS classes needed: `.m-italic-summary`, `.m-signpost`, `.m-source-attr`, `.m-qc-footer`, `.m-underline`
- IAJA tags rendered as small pills (similar to existing source/stage badges)
- Communication principle markers (❌, 🚩, A–F) rendered inline, not as separate elements
