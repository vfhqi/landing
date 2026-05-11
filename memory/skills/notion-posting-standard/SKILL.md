# Notion Posting Format Standard

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- Cross-cutting reference. Not role-specific. All roles that post to Notion MUST follow this spec. -->
<!-- Created 15-Apr-26 by Watson (SA session). Triggered by HTRO FCS beta test formatting rework. -->
<!-- V2 18-Apr-26: Major overhaul — IAJA bullet tagging, colour coding, J→A→I ordering, BLUF, italic summaries, shorter sentences, more sub-bullets. -->
<!-- Referenced by: APM, RESEARCHER, FA, EA — any role posting content to Notion via MCP. -->

## Purpose

Single source of truth for how Watson formats and posts content to Notion via the Notion MCP. Any role posting to Notion loads this file first. Role SOPs govern content and analytical structure; this standard governs Notion rendering.

---

## 1. IAJA Bullet Tagging System

### Suffix Tags — Mandatory on Most Bullets

Every substantive bullet gets a suffix tag indicating its content type. The tag appears at the end of the bullet text, after a space.

| Tag | Meaning | When to use |
|-----|---------|-------------|
| `#J` | **Judgement** | Conclusions, ratings rationale, conviction statements, assessments, "what I think" |
| `#A` | **Analysis** | Analytical observations, pattern recognition, comparisons, decomposition, "why I think it" |
| `#I` | **Information** | Factual data, reported numbers, descriptions, quotes, "what the data says" |
| `#T` | **Task** | Next steps, research tasks, actions to take, monitoring triggers |
| `#O` | **Objective** | Strategic objectives, goals, targets |
| `#KR` | **Key Result** | Measurable outcomes, KPIs, success criteria |
| `#OQ` | **Open Question** | Unresolved questions, things to investigate, uncertainties that need answers |

### When to tag

- **Tag:** All parent bullets and all standalone bullets. Sub-bullets inherit the parent's tag by default — only tag a sub-bullet if its type differs from the parent.
- **Skip tagging:** Transitional sentences, table rows, header lines, BLUF bullets (these are inherently #J).

### Examples

```
- **Revenue growth decelerating.** Organic growth fell from 8% to 4% over L3Q. #I
  - Price/volume mix shifted negative in Q4 — volume -2%, price +6%. #A
  - This suggests pricing power is masking demand weakness. #J

- **Margin trajectory is the fulcrum driver.** If EBIT margins recover to 12%+ by H2, the re-rating thesis holds. If not, this is a value trap. #J
  - H1 EBIT margin: 9.8% (vs 11.2% prior year). #I
  - Management guided "progressive improvement" but gave no target. #I
  - Sell-side consensus at 11.5% for FY26 looks ambitious given H1 run-rate. #A

- **Investigate customer concentration risk.** Top 3 customers = 45% of revenue. #OQ
```

---

## 2. Colour Coding by Content Type

### Colour-Label Prefixes

Notion MCP does not support inline text colours. The workaround is bold text-label prefixes that map to colour intent, so the reader knows the register at a glance.

| Prefix | Colour Intent | Maps to | Use for |
|--------|--------------|---------|---------|
| *(no prefix)* | Black | `#I` | Factual data, reported numbers, descriptions |
| **Analysis:** | Blue | `#A` | Analytical observations, pattern recognition, comparisons |
| **Judgement:** | Purple | `#J` | Conclusions, ratings, conviction statements, assessments |
| **Action:** | Green | `#T`, `#O`, `#KR`, `#OQ` | Tasks, objectives, key results, open questions |

### Usage Rules

- Use the prefix on parent bullets where the register needs to be clear. Not every bullet needs a prefix — the suffix tag always provides the classification.
- The prefix is the primary skim tool. Richard can scan bold prefixes to find all judgements or all actions without reading the text.
- In sections that interleave multiple content types (e.g. FCS analysis sections, KD assessments), use prefixes consistently.
- The prefix and the suffix tag must agree. A bullet tagged `#J` should have the **Judgement:** prefix if prefixed at all.

### Colour Coding + Sentiment Highlighting — Two Layers

These are two separate visual systems that coexist:

| System | Purpose | Mechanism |
|--------|---------|-----------|
| **Sentiment highlighting** (green_bg / yellow_bg / red_bg) | Signal whether content is bullish, neutral, or bearish for the investment case | Background colour spans on individual sentences |
| **IAJA colour coding** (prefix labels) | Signal whether content is judgement, analysis, information, or action | Bold text-label prefixes on bullets |

Both apply simultaneously. A bullet can be a red-highlighted judgement: `<span color="red_bg">**Judgement:** Margin recovery thesis is at risk. FY26 consensus looks 15-20% too high. #J</span>`

---

## 3. Bullet Ordering — Judgement First

### J → A → I Hierarchy

Within parent + sub-bullet structures, order content top-down by decision value:

1. **Judgement first** — the conclusion, the "so what," the rating. This is the parent bullet.
2. **Analysis second** — the reasoning, the pattern, the comparison. First sub-bullet(s).
3. **Information third** — the data, the numbers, the quotes. Supporting sub-bullets.

This is the opposite of academic writing (which builds I → A → J). Richard reads for decisions, not education. Lead with the answer.

### Example — Old (I → A → J)

```
- Revenue grew 8% organically in Q4. #I
  - This compares to 6% in Q3 and 4% in Q2, suggesting acceleration. #A
  - The trend is positive and supports the re-rating thesis. #J
```

### Example — New (J → A → I)

```
- **Judgement:** Revenue momentum is accelerating and supports the re-rating thesis. #J
  - Growth trajectory: Q2 4% → Q3 6% → Q4 8% organic. Three consecutive quarters of improvement. #A
  - Q4 organic revenue growth: 8%. Price +5%, volume +3%. #I
```

### When I-first is acceptable

- Pure data sections (financial tables, earnings summary) where the reader needs numbers first
- Sections explicitly labelled "Data" or "Financials"
- Quoting management verbatim (the quote is the point)

---

## 4. BLUF (Bottom Line Up Front)

### Page-Level BLUF

Every Notion page opens with a BLUF section immediately after the H1 title. 3-5 bullets maximum. Each bullet is a judgement — no data, no hedging. Tagged `#J`.

```
# [W] EKTA - ESA - Value Chain Analysis - Competitive position improving [AS] @ 18-Apr-26

## BLUF
- **Competitive position is improving.** Radiation therapy market consolidation favours EKTA's installed base. #J
- **Pricing power is real but narrow.** Service contracts have escalators; equipment pricing is under pressure from Varian. #J
- **Key risk: China market access.** Regulatory barriers and local competition could cap Asia growth. #J
```

### Section-Level BLUF

Every H2 section opens with 1-2 italic BLUF sentences before the detailed bullets. This is the section's judgement in compressed form.

```
## Margin Profile & Evolution

_Margins expanding on mix shift and operating leverage. Sustainable if service revenue share continues to rise. Main risk: equipment pricing pressure in competitive tenders._

- **Judgement:** Margin trajectory is positive and structurally driven. #J
  - Service mix rose from 52% to 58% of revenue over L3Y. Higher-margin, recurring. #A
  - Gross margin: 42.1% (FY25) vs 39.8% (FY23). Expansion accelerating. #I
```

---

## 5. Bullet Structure

### Default: Parent + Sub-Bullets

The default format for any substantive bullet is parent + sub-bullets. Flat single bullets are only appropriate for standalone facts with no supporting context.

### Rules

- **Hard cap: ~100 words per bullet.** Split if longer.
- **Parent bullet = the judgement or headline claim.** Bold the key term. Tag with #J or #A.
- **Sub-bullets = evidence, context, data.** Tag with #A or #I. Each independently readable.
- **More sub-bullets, fewer flat bullets.** Break complex points into 2-4 sub-bullets rather than one long sentence.
- **Shorter sentences.** Prefer one clause per sentence. State the point and move on.

### Good Example

```
- **Judgement:** Sell-side consensus is too optimistic on FY26 margins. #J
  - Consensus EBIT margin: 14.2%. Implies 280bps YoY expansion. #I
  - H1 run-rate: 11.8%. No visible catalyst for H2 step-change. #A
  - Management guided "progressive improvement" — no specific target. #I
  - Last time margins expanded >200bps in a year was FY19, driven by restructuring one-offs. #A
```

### Bad Example (flat, long, no hierarchy)

```
- Sell-side consensus EBIT margin for FY26 is 14.2%, implying 280bps YoY expansion, but H1 run-rate is only 11.8% with no visible catalyst for a H2 step-change, and management guided only "progressive improvement" without a specific target, and the last time margins expanded more than 200bps was FY19 on restructuring one-offs.
```

---

## 6. Italic Summary Sentences

### Section-Closing Summaries

Every H2 section closes with an italic summary sentence — the single most important takeaway from that section. One sentence. No tag needed.

```
## Revenue Growth & Organic Dynamics

[detailed bullets...]

_Revenue momentum is real but narrow — driven entirely by pricing, not volume. Volume recovery is the key watch item._
```

### When to use italic elsewhere

- Section-opening BLUF sentences (see §4)
- Section-closing summary sentences (see above)
- Watson's qualitative assessments within body text
- Hedged or conditional statements
- "Watch this" items

---

## 7. Headers — Clear and Navigable

### Hierarchy

| Level | Use for |
|-------|---------|
| `#` (H1) | Page title / top-level identifier. One per page. |
| `##` (H2) | Major sections, key driver names, analyst names, topic areas. The primary navigation tool. |
| `###` (H3) | Sub-sections, sub-themes, individual data points within a section. |
| `####` (H4) | Attribute family headers, detailed sub-subsections (FCS memos). |
| `**Bold text**` | Inline sub-headers within body text. |

### Header Count Targets (flexible, scale with length)

- Shorter memos (2,000-3,000 words): 5-10 H2, 8-15 H3
- Longer memos (5,000+ words): 8-15 H2, 15-25 H3
- Use judgement. The goal is navigability, not a fixed count.

### Rule of Thumb

If Richard would have to read more than 3 paragraphs before hitting a header, add one.

### Header Style

Headers should be descriptive, not generic. Include the key finding or topic, not just a label.

- **Good:** `## Margin Profile — Expanding on Mix Shift`
- **Bad:** `## Margins`
- **Good:** `### Q4 Beat — Volume-Driven, Sustainable`
- **Bad:** `### Q4 Results`

---

## 8. Tables

### Rule: Pipe Tables ONLY. Never HTML.

Notion MCP's `replace_content` escapes all HTML `<table>` tags, rendering them as literal text. HTML tables also lose the first data row.

**Correct format:**
```
| Column A | Column B | Column C |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Table Formatting Rules

- **Header row always present** — first row treated as header
- **Bold key financial rows** — Revenue, EBITDA, EBITA, EPS, Operating Cash Flow, Net Debt rows use `**bold**` in the first column
- **Split financial data rows** where multiple sources exist (historical actuals, company guidance, sell-side consensus on separate rows)
- Notion auto-converts pipe tables to native table format. All rows preserved.

**Never use:** `<table>`, `<tr>`, `<td>`, `<th>` tags, or any HTML table syntax.

---

## 9. Text Emphasis

### Available Markup (Notion Enhanced Markdown)

| Syntax | Renders as | Use for |
|--------|-----------|---------|
| `**text**` | **Bold** | Key financial figures, ratings, section labels, analyst names, tickers, emphasis |
| `_text_` | _Italic_ | BLUF sentences, section summaries, qualitative assessments, caveats, "watch" items |
| `<u>text</u>` | Underline | Key concepts, defined terms, framework labels (e.g., <u>Fulcrum Driver</u>) |
| `~~text~~` | ~~Strikethrough~~ | Deprecated items, superseded data |
| `***text***` | ***Bold Italic*** | Sparingly — critical warnings or the single most important insight on a page |

### What Does NOT Work

| Syntax | Problem |
|--------|---------|
| `==text==` | Not supported by Notion. Renders as literal `==text==`. **Never use.** |
| `__text__` | Does NOT render as underline. Use `<u>` instead. |

### Bold — Use Heavily

Bold is the primary skim tool after headers. Richard scans bold text to find numbers and conclusions.

**Always bold:**
- All financial metrics: **7.1% EBITA margin**, **SEK 42.50 target price**, **2.8x net debt/EBITDA**
- All analyst names on first mention: **DNB Carnegie**, **Morgan Stanley**
- All ratings and recommendation changes: **Buy**, **Hold**, **upgraded from Hold to Buy**
- All percentage changes and beats/misses: **15% above consensus**, **beat by 50bps**
- Key strategic terms: **Instalco 2.0**, **margin restoration**
- Verdicts and conclusions: **Net assessment: improving but fragile**
- Time periods with analytical weight: **first YoY EBITA growth in seven quarters**

---

## 10. Horizontal Rules

Use `---` between major sections (between Pillars, between Section A/B/C/D boundaries in FCS memos, between major topic shifts). Do not overuse within sections.

---

## 11. Document Structure (FCS Memos)

### Section Ordering: A → B → C → D

| Section | Content | Display Order |
|---------|---------|---------------|
| A | Financials (P&L, CF/BS, Cash Returns, Multiples) | First |
| B | Summary (Pillar rollup, IC summary, ICDs, KQs, KAs) | Second |
| C | IC Analysis (6 Pillars, interleaved ratings + analysis + judgement) | Third |
| D | Actions (KPOs, KCs, KUs, Monitoring, Valuation, Next Steps) | Fourth |

### Pillar Structure Within Section C

**Pillars I, II, V, VI:** Flat structure
```
### Pillar [N] — [Name]: **[Rating]**
#### Ratings Table
[pipe table]
#### Analysis
[bullets with #A tags and Analysis: prefixes]
#### Judgement
[italic + bold summary with #J tags]
```

**Pillars III and IV:** 5-level nested hierarchy
```
### Pillar III — Fundamental Change: **[Rating]**
#### 3.1 — IC #1: Required Case OUTPUTS
**Ratings by Question**
[pipe table]
**Ratings by Attribute**
[pipe table]
**Target Conditions**
[pipe table]
**Attribute Family Summary:** [rating + rationale]
#### Analysis
[bullets with #A tags]
#### Judgement
[italic summary with #J tag]
```

### Interleaving Rule

Ratings table + analysis + judgement are interleaved per pillar. Do NOT group all ratings tables together. Each pillar is self-contained.

---

## 12. Stock Notes Page Title Convention

<!-- Updated 16-Apr-26: Company name REMOVED. Summary expanded to 5-15 word descriptor. Applies to all roles posting to Stock Notes. -->

**Universal format:** `[W] {TICKER} - {Stage} - {Research Type} - {summary} [{SOURCE}] @ DD-Mon-YY`

### Rules

| Element | Rule |
|---------|------|
| `[W]` prefix | Always present — marks Watson output |
| `{TICKER}` | Exchange ticker only (e.g. EKTA, INSTAL, CARLB) |
| `{Stage}` | IG / Triaging / ESA / DD / Any (as appropriate) |
| `{Research Type}` | Query name from RESEARCHER query framework (Q1-Q22 v2.1 + Q23 thematic) |
| `{summary}` | **5-15 word substantive descriptor** of the page's key content and finding. Informative enough to convey the central message without opening. |
| **Company name** | **NOT included.** Removed 16-Apr-26. |
| `[{SOURCE}]` | `[C]` Claude, `[AS]` AlphaSense, `[C+AS]` merged, `[W]` Watson synthesis |
| `@ DD-Mon-YY` | Execution date |
| Separators | All hyphens (`-`). No em-dashes. |

### Examples

| Research Type | Title |
|---------------|-------|
| IG Business Description | `[W] EKTA - IG - Business Description - Global radiation therapy leader with recurring service revenue base and strong R&D pipeline [AS] @ 16-Apr-26` |
| ESA Value Chain Analysis | `[W] EKTA - ESA - Value Chain Analysis - Positive competitive position that is improving; component supplier consolidation creating pricing power [AS] @ 16-Apr-26` |
| Triaging SS Commentary | `[W] INSTAL - Triaging - SS Commentary - Cautious consensus post-Q4 miss; margin recovery thesis intact but timeline pushed right [AS] @ 13-Apr-26` |
| KQ (stage known) | `[W] DCC - ESA - Competitive Moat KQ - Energy distribution switching costs support durable BtE; but commoditisation risk in adjacencies [C] @ 28-Mar-26` |
| Merged dual-source | `[W] DHER - IG - Change Forces - Profitability inflection thesis credible; market consolidation accelerating; margin path dependent on Germany recovery [C+AS] @ 01-Apr-26` |

### Exception

Thematic or multi-stock KQs: omit `{Stage}`, use topic instead of ticker. Format: `[W] {TOPIC} - {KQ Title} KQ - {summary} [{SOURCE}] @ DD-Mon-YY`

---

## 13. Posting Protocol

### Content Size Limits

- If content is <50K chars: single `replace_content` call
- If content is >50K chars: split into initial `replace_content` + subsequent `update_content` (append) calls
- Always verify after posting via `notion-fetch`

### Verification Checklist (run after every post)

1. Fetch the page via `notion-fetch`
2. Confirm: no escaped HTML tags (`\<table\>`, `\<tr\>`, etc.)
3. Confirm: no `==` highlighting remnants
4. Confirm: all sections present (check for truncation)
5. Confirm: tables rendered as native Notion tables
6. Confirm: bold, italic, underline rendering as expected
7. Confirm: page properties set correctly (Date, Case component, Depth, IAJA, etc.)
8. Confirm: BLUF present at page level and section level
9. Confirm: suffix tags (#J, #A, #I, #T, etc.) present on parent bullets

---

## 14. Pre-Flight Quality Gate — Mandatory

**Before chunking or posting, Watson verifies formatted content against this checklist. Every item must PASS.**

### Checklist (binary pass/fail)

- [ ] **BLUF present?** Page-level BLUF (3-5 bullets) immediately after H1?
- [ ] **Section BLUFs?** Italic opening sentence at each H2 section?
- [ ] **Suffix tags?** Spot-check 10 parent bullets — all tagged #J/#A/#I/#T/#O/#KR/#OQ?
- [ ] **J→A→I ordering?** Spot-check 5 parent+sub-bullet structures — judgement leads?
- [ ] **Colour-label prefixes?** Judgement:/Analysis:/Action: prefixes used where register is ambiguous? (Spot-check 5.)
- [ ] **H2 count:** Proportional to memo length? (5-10 shorter, 8-15 longer.)
- [ ] **H3 count:** Proportional to memo length? (8-15 shorter, 15-25 longer.)
- [ ] **Bold density:** Financial metrics, analyst names, ratings, percentages all bolded? (Spot-check 10.)
- [ ] **Highlight coverage:** 30%+ of sentences sentiment-highlighted? (green_bg/yellow_bg/red_bg)
- [ ] **Highlight precision:** Highlights are sentence-level, not paragraph-level?
- [ ] **Artifact contamination:** Zero AS source annotations, date stamps, broken tags?
- [ ] **Bullet length:** No bullet exceeds ~100 words?
- [ ] **Italic summaries?** Section-closing italic summary sentence at each H2?
- [ ] **Table formatting:** Pipe tables only, no HTML?
- [ ] **Content completeness:** Word count matches source within 90%?

### Protocol

1. Run this checklist on the actual formatted content (not raw source)
2. If ANY item fails → fix before proceeding to chunking/posting
3. On batch operations: run full checklist on FIRST page only. If it passes, proceed. If fails, fix the pipeline and re-run.
4. Log pass/fail result before posting

---

## 15. Role Integration

This standard is called by roles, not owned by any single role.

**How roles reference this file:**
- **APM:** Load before any FCS memo posting. FCS deliverable format follows §11 structure.
- **RESEARCHER:** Load before posting [C] or [AS] research pages. All formatting rules apply.
- **FA:** Load before posting financial model summaries or data tables.
- **EA:** Load before any Notion posting task. Responsible for verification checklist.

**Rule:** If a role's SOP conflicts with this standard on a Notion-specific formatting question, this standard wins. Role SOPs govern content and analytical structure; this standard governs Notion rendering.

---

## Quick Reference — Formatting at a Glance

```
# Page Title

## BLUF
- [3-5 #J bullets — the answer before the analysis]

## Section Name — Descriptive Finding

_Italic section BLUF — one sentence, the judgement._

- **Judgement:** Parent bullet with the conclusion. #J
  - Supporting analysis or pattern. #A
  - Supporting data point. #I
  - Follow-up question or uncertainty. #OQ

- **Analysis:** Second parent bullet. #A
  - Data evidence. #I
  - Data evidence. #I

- **Action:** Research task or next step. #T

_Italic section-closing summary — the single takeaway._

---
```

---

*[W] V1 created 15-Apr-26 | V2 major overhaul 18-Apr-26 | SA session | IAJA tagging, colour coding, J→A→I ordering, BLUF, italic summaries*
