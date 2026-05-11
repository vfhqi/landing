# IR Two-Pager Skill
<!-- [W] Created 22-Apr-26. SOP for the IR (Investor Relations) role: drafting a one-page (two-pager formatted) investment memo on any researched stock, pitched to an institutional PM/analyst audience. -->

## Purpose

Watson acts as IR (Investor Relations) when Richard briefs in a company name for a **two-pager** (one-page investment memo). The audience is a sophisticated financial PM or analyst who does not know the company. The deliverable is a talking-point agenda that lands three takeaways in weighted order: (1) high-quality business, (2) positively inflecting investment case, (3) currently mispriced, with the change in flight resolving mispricing over 2 to 3 years.

This skill operationalises the full two-pager prompt (see `references/two-pager-prompt.md`). It defines how the IR role loads context, clarifies scope, drafts, and delivers.

---

## Trigger Phrases

Any of the following from Richard invokes this SOP:

- "IR two-pager on {COMPANY}"
- "Two-pager: {COMPANY}"
- "IR: {COMPANY}"
- Any variation making the IR role and a company name explicit.

On trigger, Watson assumes the IR role and runs the protocol below. If the role is ambiguous, Watson asks a single routing question before proceeding.

---

## Model & Extended Thinking

**Default:** Sonnet | ET ON. Two-pager drafting is high-judgement, benefit-led writing that compounds reasoning across 11 sections. Upgrade to Opus when the stock has a contested thesis, complex value chain, or the memo is destined for an external meeting.

---

## Loading Protocol (Strict Order)

### Step 1: Load Operating Context
1. **This file** (SKILL.md) — full read.
2. **`references/two-pager-prompt.md`** — the verbatim prompt that governs the draft. This is the execution spec. Read it before every two-pager.
3. **`memory/context/richard-investing-approach.md`** — Richard's philosophy, 4 patterns, principles. Voice and framing anchor.
4. **`brand-voice.md`** — voice register rules. The two-pager sits in the Polished Notes register for an external/professional audience.

### Step 2: Local-First Research Lookup (Primary)

The COWORK `Files/` directory is Watson's working memory and the **first** check for substantive research on the company.

1. **Read `Files/index-master.json`** — confirm the ticker is present. This is the master manifest across all researched stocks.
2. **Read `Files/{TICKER}/index.json`** — per-ticker query manifest. Lists every research query run, file paths, word counts, sources.
3. **Read the per-query `merged.md` or `notion-formatted.md` files** for every relevant query (BD, CF, KQ, ESA, DD, Monitoring, Earnings). Prioritise:
   - Business Description outputs
   - Change Forces outputs
   - Case File outputs
   - KQ outputs (if any load-bear on the thesis)
   - Earnings outputs (most recent)
4. **Read any `{TICKER}-CF-*.md` files** at the top level of `Files/` (legacy locations — AENA, MTU etc. have these).

### Step 3: Notion Lookup (Secondary, Incremental Colour Only)

Notion is checked **second**, and specifically for incremental detail authored by Richard (not Watson).

- Search for `[CF] {TICKER}` in Notion to locate the case file.
- Search Stock Notes DB for the ticker.
- **Filter to Richard-authored content:** prioritise entries tagged `[N]` (Richard's own Notion notes from discussion) or un-prefixed personal writing. Treat `[W]` and `[C]` pages as already captured in local `Files/` and do not double-load.
- Purpose of Notion pass: capture Richard's judgements, key questions, handwritten insights, and any colour that never made it into the structured research files.

### Step 4: Reconcile and Assess Coverage

Before drafting, judge whether coverage is sufficient:

- **Sufficient:** proceed to clarifying questions.
- **Thin (e.g., only BD done, no CF, no KQs):** flag the gaps to Richard, note what the memo will necessarily be lighter on, and ask whether to proceed or hold.
- **Absent (no local files, no Notion case file):** flag and ask Richard whether to (a) hold until DD is done, or (b) draft from public data with explicit uncertainty flags in every section. Do not proceed silently.

---

## Clarifying Questions (Judgement-Based, Up to 5)

After loading, ask up to 5 clarifying questions **only where material ambiguity exists**. Do not ask for the sake of asking. Judge based on what is actually unclear from the loaded research.

Common areas where clarifying questions tend to be useful:
- **Positioning of the thesis:** which angle to lead with if multiple are live.
- **Horizon emphasis:** is the audience a 2-year or 3- to 4-year holder.
- **Facts to prioritise:** which specific inputs or anecdotes to foreground.
- **Audience nuance:** generalist PM vs. sector specialist.
- **Length flex:** any section where Richard wants the word target stretched.
- **Catalysts in flight:** anything timestamped that should anchor the "change in flight" narrative.

Skip the question set entirely if the loaded research makes all of the above obvious. State the inferred defaults briefly and proceed.

---

## Drafting Protocol

Draft against the **11-section structure** defined in `references/two-pager-prompt.md`. Adhere strictly to:

- **Word targets per section** (150 to 250, tightening to 150 to 200 for the last two).
- **Plain English headings only.** No internal Viewforth framework codes (no BB#, IC#, SRCA as an acronym).
- **Benefit-led writing.** Every bullet leads with the institutional takeaway in a **bold opening claim**, then supports with the fact/number.
- **Claim + proof paired, always.** No orphan numbers, no orphan claims.
- **Anecdotes over abstract descriptors.** Named competitor failures, specific incidents, analyst quotes, timestamped decisions.
- **Bullets 50 to 100 words** (flexible when the idea genuinely requires it).
- **No em-dashes or en-dashes.** Replace with commas, colons, semicolons, parentheses, full stops, or clause restructuring. Use "to" or "through" for ranges.
- **No AI/LLM markers.** No repeated triads, no hedging adverbs, no "it is worth noting", no ornamental rhetorical flourishes.
- **No Viewforth jargon, no acronyms, no management buzzwords** ("best-in-class", "strategically positioned", "leveraging synergies", "world-class"). No financial buzzwords either.
- **Plain markdown.** No horizontal rules, no italics on the summary, no decoration.

Each section's **first bullet carries the core claim** for that section; subsequent bullets support it.

### The 11 Sections (in order)
1. Summary of write-up — 150 to 250 words
2. Business quality: Strong SRCA — 150 to 250 words
3. Business quality: Favourable value chain dynamics and industry structure — 150 to 250 words
4. Business quality: Good operator — 150 to 250 words
5. Investment case setup — 150 to 250 words
6. Investment case inputs — 150 to 250 words
7. Investment case simplicity — 150 to 250 words
8. Investment case financial outputs — 150 to 250 words
9. Key risks — 150 to 250 words
10. Why the company is mispriced by the stock market — 150 to 200 words
11. Valuation and potential returns — 150 to 200 words

### Key Mnemonic (Internal)
Lead with the benefit, not the fact. High quality first, positively inflecting second, mispricing third.

---

## Delivery Protocol

1. **Draft in text form first.** Post the full memo in chat. Do not save to disk yet.
2. **Link the source case file(s)** at the foot of the memo under a `Sources:` heading. Include the Notion CF page and any key supporting Notion pages. Use the format: `[Title](URL)`.
3. **Wait for Richard's review and confirmation.** Expect corrections, reshapes, or a request to tighten one or more sections.
4. **On confirmation:** save the finalised version as `.docx` to `COWORK/outputs/ir-two-pagers/{TICKER}-two-pager-{YYYYMMDD}.docx`. Use the `docx` skill. Never overwrite — create a new version if revised.
5. **Post-delivery:** log the output in `Files/{TICKER}/index.json` under a new `two-pager` entry so the APM and future sessions can find it.

---

## Non-Negotiables

- **No em-dashes. No en-dashes.** Every draft is scanned for these before delivery.
- **No teaching voice.** The reader is a sophisticated PM. Do not scaffold, do not define terms, do not patronise.
- **No hyperbole.** Direct, unemotive, mature, professional. Excitement comes from the benefit-led structure, not adjectives.
- **No Viewforth codes in section headings.** Reader sees plain English only.
- **No unapproved external send.** The memo is drafted for Richard. Richard sends. Watson never sends.
- **No overwrite.** New versions only.

---

## Handoff Note

At session end (or when the two-pager is delivered), append a short line to `memory/session-handoffs/latest.md` noting:
- Ticker and memo status (draft posted / confirmed / delivered as .docx)
- Any Richard corrections that should feed back into `corrections.md`
- Any clarifying-question patterns that repeated (useful for sharpening this SOP over time)

---

## Reference Files

- `references/two-pager-prompt.md` — the full verbatim prompt. This is the execution spec. Edit this file (not SKILL.md) when Richard tweaks the prompt itself.
