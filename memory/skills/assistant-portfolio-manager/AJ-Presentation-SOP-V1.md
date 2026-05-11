# A&J Presentation SOP — Formatting + Notion Conventions (1/10x weight)

**Version:** 1.0 — first standing version
**Authored:** 10-May-26 by Watson (APM role)
**Source:** distilled from `notion-posting-standard/SKILL.md` + HTRO Triaging V1→V2-polished transformation at Step 4
**Test stock validation:** HTRO Triaging memo polished at `PROJECTS/SA - Reports & Memos Repository/htro-test-stock/HTRO-Triaging-memo-V2-polished.md`

**Weight in three-SOP hierarchy:** 1/10x — supporting the Comms SOP. The polish layer is purely a presentation transformation. It makes the memo Notion-renderable + scannable + decision-grade. It does NOT change what the memo says.

---

## §0 — PURPOSE + SCOPE

### What this SOP delivers

Standing formatting + Notion conventions that any A&J memo applies as the final layer before posting to Notion. The conventions are documented in greater depth at `memory/skills/notion-posting-standard/SKILL.md` (V2, 18-Apr-26); this SOP is the A&J-specific subset relevant for memo presentation.

### What this SOP does NOT do

- Does NOT change the substance (content + ratings preserved from Comms output)
- Does NOT change the structure (sections + subsections preserved)
- Does NOT change the order of analysis (Pillars/BBs/Master Ratings preserved)
- Does NOT replace the analyst's content judgement — purely formats it

---

## §1 — THE 6 POLISH CONVENTIONS

### Convention 1 — IAJA suffix tags

Every substantive bullet gets a suffix tag indicating content type:
- `#J` Judgement (conclusions, ratings rationale, conviction statements)
- `#A` Analysis (analytical observations, pattern recognition, comparisons)
- `#I` Information (factual data, reported numbers, descriptions)
- `#T` Task (next steps, monitoring triggers)
- `#OQ` Open Question (unresolved investigation items)
- `#O` Objective (strategic objectives)
- `#KR` Key Result (measurable outcomes)

**When to tag:** all parent bullets + all standalone bullets. Sub-bullets inherit parent's tag by default — only tag a sub-bullet if its type differs.

**When to skip:** transitional sentences, table rows, header lines, BLUF bullets (inherently #J).

### Convention 2 — Colour-coded prefixes on parent bullets

Notion MCP doesn't support inline text colours. Workaround = bold text-label prefixes:

| Prefix | Colour Intent | Maps to | Use for |
|---|---|---|---|
| *(no prefix)* | Black | `#I` | Factual data, reported numbers, descriptions |
| **Analysis:** | Blue | `#A` | Analytical observations, pattern recognition, comparisons |
| **Judgement:** | Purple | `#J` | Conclusions, ratings, conviction statements |
| **Action:** | Green | `#T`, `#O`, `#KR`, `#OQ` | Tasks, objectives, key results, open questions |

**Usage rules:**
- Use prefix on parent bullets where register needs to be clear
- Not every bullet needs a prefix — the suffix tag always provides classification
- Prefix is the primary skim tool — Richard scans bold prefixes to find judgements/actions
- Prefix and suffix tag must agree (a #J bullet should have **Judgement:** prefix if prefixed)

### Convention 3 — BLUF (Bottom Line Up Front)

**Page-level BLUF:** every Notion page opens with BLUF section immediately after H1. 3-5 bullets max. Each bullet is a judgement (no data, no hedging). Tagged #J.

**Section-level BLUF:** every H2 section opens with 1-2 italic BLUF sentences before detailed bullets. The section's judgement in compressed form.

### Convention 4 — J → A → I bullet ordering

Within parent + sub-bullet structures, order top-down by decision value:
1. **Judgement first** — the conclusion, the "so what," the rating (parent bullet)
2. **Analysis second** — the reasoning, the pattern, the comparison (first sub-bullets)
3. **Information third** — the data, the numbers, the quotes (final sub-bullets)

This is OPPOSITE of academic writing (which builds I → A → J). Richard reads for decisions, not education. Lead with the answer.

**When I-first is acceptable:**
- Pure data sections (financial tables, earnings summary)
- Sections explicitly labelled "Data" or "Financials"
- Quoting management verbatim (the quote is the point)

### Convention 5 — Italic summary sentences at section ends

Every H2 section closes with an italic summary sentence — the single most important takeaway from that section. One sentence. No tag needed.

### Convention 6 — Outlier/sentiment markers

- 🚩 **RARE:** for genuinely unusual + high-signal findings (use ≤3 per memo)
- ❌ for D/F findings
- ⚡ for outlier observations
- 5-10% bullet underlining for the most important parent bullets in each section

### Convention 7 — Bullet structure rules

- Hard cap ~30 words per parent bullet (signpost-label characters excluded)
- Sub-bullets up to 6 per parent (Miller 7±2)
- No grandchildren (max 2 disclosure levels)
- Flex sub-COUNT not bullet LENGTH

---

## §2 — NOTION-SPECIFIC TECHNICAL CONSIDERATIONS

### Sentiment highlighting (background colours)

Notion supports background colour spans on individual sentences:
- `<span color="green_bg">positive content</span>`
- `<span color="yellow_bg">neutral/mixed content</span>`
- `<span color="red_bg">negative content</span>`

Apply sparingly — use to flag the most important bullish/neutral/bearish sentences. Over-application reduces signal.

### Two-layer color system

Sentiment highlighting (green_bg/yellow_bg/red_bg) and IAJA prefixes (Analysis:/Judgement:/Action:) coexist. A bullet can be a red-highlighted judgement:

`<span color="red_bg">**Judgement:** Margin recovery thesis is at risk. FY26 consensus looks 15-20% too high. #J</span>`

### Notion prefix conventions (Notion title bar)

| Prefix | Meaning |
|---|---|
| [+] | Active / positive conviction |
| [-] | Parked / negative |
| [?] | Under assessment / triage |
| [CF] | Case file in progress |
| [W] | Watson (AI) output |
| [N] | Notion notes from discussion |
| [C] | Source: Claude (suffix before date) |
| [AS] | Source: AlphaSense (suffix before date) |

Use these consistently in Notion page titles. Helps Richard scan database views.

### Title format

`# [W] {TICKER} - {Stage} - {COMPANY} - {Headline takeaway} [W] @ {DATE}`

Example: `# [W] HTRO - Triaging - Hexatronic Group AB — DC inflection + structural pivot real, but +113% YTD captures part of upside [W] @ 10-May-26`

The headline takeaway is itself a judgement — should fit on one line. The reader can decide whether to read the page from the title alone.

---

## §3 — TRANSFORMATION PROCESS

### From Comms output (Step 3) to Notion-ready (Step 4)

The transformation is mechanical but disciplined:

**Pass 1: Add IAJA suffix tags to every substantive bullet.**
- Read each parent bullet, classify as J/A/I/T/OQ
- Read each sub-bullet, classify (default = inherit parent)
- Add tag at end of bullet

**Pass 2: Add colour-coded prefixes to parent bullets where register needs to be clear.**
- For sections that interleave multiple content types
- Not every bullet needs a prefix — judgement-heavy sections benefit most

**Pass 3: Add page-level BLUF.**
- Immediately after H1 title
- 3-5 judgement bullets max
- Each captures one element of the case in <30 words

**Pass 4: Add section-level italic BLUF sentences.**
- 1-2 italic sentences immediately after each H2 heading
- Compressed judgement of what follows

**Pass 5: Reorder bullets to J → A → I where possible.**
- Identify any I → A → J ordering
- Restructure to lead with judgement (parent), support with analysis, underpin with data

**Pass 6: Add italic summary sentences at section ends.**
- Single most important takeaway from the section
- One sentence. No tag.

**Pass 7: Apply outlier/sentiment markers.**
- 🚩 RARE for genuinely unusual findings (≤3 per memo)
- ❌ for D/F findings  
- ⚡ for outlier observations

### Word-count overhead

The polish layer adds approximately +15-20% words on convention overhead. This is acceptable for:
- Triaging memo (2,000w → 2,300-2,400w polished)
- ESA memo (4,000-12,000w → 4,800-14,400w polished)
- DD memo (5,000-25,000w → 6,000-30,000w polished)

For DD memos at the upper word target, the +15-20% overhead becomes meaningful (4,000-5,000 additional words). Consider whether convention overhead is value-add or noise at that scale.

---

## §4 — VALIDATION + CALIBRATION

### How to know if the Presentation SOP worked

The Presentation SOP worked if:
1. Richard can scan a polished memo in <30 seconds and find the BLUF + section judgements + critical sub-bullets
2. The colour-coded prefixes and IAJA tags allow non-linear reading (read all judgements first, then all analysis, then all information)
3. The italic section summaries provide a one-sentence skim of any section
4. The polish layer doesn't OBSCURE the substance (over-formatting is worse than under-formatting)

### Lessons from HTRO Triaging V1→V2-polished transformation

**Lesson 1:** The italic section summaries are the single highest-leverage convention. Even a reader who skims only the italics gets the case.

**Lesson 2:** Page-level BLUF must commit to 3 specific judgements, not 3 generic statements. "Recommend buy" is generic. "Recommend BUY at SEK 39.86 to 4-6% MODERATE position" is specific.

**Lesson 3:** Over-tagging dilutes signal. Don't tag every sentence in a paragraph — tag the parent bullet, let sub-bullets inherit.

**Lesson 4:** The J→A→I ordering forces analytical discipline. If you can't lead with a judgement, you don't have one yet.

**Lesson 5:** The colour-coded prefixes work best when applied SELECTIVELY in interleaved sections. Applying them to every parent bullet creates visual noise.

### Future SOP iterations

V1 (this document) is the first standing version. Subsequent versions should incorporate lessons from second-stock validation + actual Notion posting feedback.

