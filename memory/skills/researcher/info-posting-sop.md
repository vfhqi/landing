# Info Posting SOP
<!-- [W] Created 10-Apr-26. Governs posting ad-hoc research and information lookups to Notion Stock Notes. -->
<!-- Updated 18-Apr-26: Formatting rules now governed by Notion Posting Format Standard. -->
<!-- Referenced by: RESEARCHER role file -->

## Purpose

This SOP governs how Watson posts **ad-hoc research outputs** — one-off questions, quick lookups, targeted investigations — to the Notion Stock Notes database. It covers the specific workflow for taking completed information/analysis and getting it into Notion with correct properties, highlighting, and formatting.

**For formatting rules** (IAJA tagging, bullet structure, headers, bold, colour coding, BLUF, italic summaries), see the **Notion Posting Format Standard** (`memory/skills/notion-posting-standard/SKILL.md`). Load it before any Notion posting.

**This SOP does NOT replace** the triaging, IG, KQ, or any other research-specific posting workflows. Those have their own SOPs. This SOP is for everything else — the ad-hoc questions Richard asks that produce useful stock-specific intelligence worth preserving.

---

## When This SOP Triggers

Any time Watson completes ad-hoc research that:
1. Is **stock-specific** (relates to a company in the pipeline or squad)
2. Produces information/analysis worth preserving (not just a one-line answer)
3. Does **not** fall under an existing posting pathway (triaging, IG, KQ, ESA, etc.)

**Examples:**
- "Who is selling down their stake in HTWS and why?"
- "What's the regulatory timeline for X approval at XVIVO?"
- "What happened at the DKSH capital markets day?"
- "What's the short interest picture on FLTR?"

**Non-examples (do NOT use this SOP):**
- Triaging prompt outputs → use notion-posting-sop.md
- IG Business Description / Change Forces → use IG SOP
- KQ research → use KQ workflow SOP
- Quick factual answers that don't warrant a Notion page (e.g., "What's DHER's market cap?")

---

## Step 1: Assess IAJA Tag

Before posting, Watson determines which IAJA classification applies based on content:

| Tag | When to use |
|---|---|
| **Information** | Pure fact-finding: who, what, when. No Watson judgement added. Example: shareholder register lookup, regulatory timeline, event summary |
| **Information, Analysis** | Facts plus Watson's interpretation of what they mean for the investment case. Example: shareholder selling analysis with implications for thesis |
| **Analysis** | Watson's analytical work building on information Richard already has. Example: scenario analysis on a known driver |

Default is **Information**. Upgrade to **Information, Analysis** when Watson makes explicit interpretive judgements beyond reporting facts.

---

## Step 2: Apply Highlighting & Formatting

**Inherit ALL rules from `notion-posting-sop.md`**, specifically:

- **Sentiment highlighting** (Step 1): green_bg / yellow_bg / red_bg spans. Sentence-level, not paragraph-level. 30%+ coverage target.
- **Formatting** (Step 2): Aggressive headers (H1/H2/H3), heavy bold on metrics/names/ratings, bullet points for summaries, markdown tables for data.
- **Pre-flight quality gate** (Step 2.5): Run the checklist. All items must pass.

### Adaptation for Shorter Posts

Ad-hoc research is often shorter than full triaging memos (1,000-5,000 words vs 7,000-15,000). Adjust header targets proportionally:

| Post length | H2 target | H3 target |
|---|---|---|
| <2,000 words | 3-5 | 5-10 |
| 2,000-5,000 words | 5-8 | 8-15 |
| >5,000 words | Full Format Standard targets (8-15 H2, 15-25 H3 — flexible per §7) |

Highlighting coverage target remains **30%+ regardless of length**.

---

## Step 3: Set Page Properties

### Target Database

Stock Notes DB: `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2`

### Properties

```
Note title: [W] {TICKER} - {Description} [{SOURCE}] @ DD-Mon-YY
date:Date:start: YYYY-MM-DD
date:Date:is_datetime: 0
Main focus of note: Stock(s)
Info, analysis, judgement and/or action: {IAJA tag from Step 1}
Depth of note: Watson posting of information
Case component: {Inferred from content — see below}
Stock(s): "https://www.notion.so/{page_id_no_dashes}"
```

### Title Convention

Same format as all Watson postings: `[W] {TICKER} - {Description} [{SOURCE}] @ DD-Mon-YY`

**Description** should be concise and descriptive of the specific question answered. Examples:
- `[W] HTWS - Newlight/QSP Shareholder Analysis [C] @ 10-Apr-26`
- `[W] XVIVO - FDA Timeline & Regulatory Pathway [C] @ 12-Apr-26`
- `[W] FLTR - Short Interest & Positioning Analysis [C] @ 15-Apr-26`
- `[W] DKSH - CMD 2026 Key Takeaways [C] @ 18-Apr-26`

### Case Component — Watson Infers

Watson selects the most appropriate case component based on the content of the research:

| Content type | Case component |
|---|---|
| Shareholder/ownership analysis | Inputs / change forces |
| Regulatory/approval timelines | Inputs / change forces |
| Management/governance changes | Inputs / change forces |
| Competitive dynamics, market structure | Inputs / change forces |
| Financial data lookups, consensus changes | Inputs / change forces |
| Valuation-related analysis | Valuation / market pricing |
| Thesis-testing, bear case exploration | Key risks / key confusions |

Default: **Inputs / change forces**. Override when content clearly fits another component.

### Source Tag

- `[C]` — Claude (web research, native analysis)
- `[AS]` — AlphaSense
- `[W]` — Watson synthesis (combining multiple sources)

---

## Step 4: Post to Notion

### Short Posts (<15K characters)

Single `create-pages` call with full content.

### Long Posts (>15K characters)

Follow chunking protocol from `notion-posting-sop.md` Step 3:
1. Create page with first chunk via `create-pages`
2. Append remaining sections via `update-page` with `update_content`
3. Fetch page first if match fails

### Stock Page ID Lookup

If the stock's page ID is not in the known IDs table (in `notion-posting-sop.md`), search for it:
1. Search Notion for the ticker/company name
2. Verify the result is in the main Stocks DB (`collection://25435e90-9b0b-80ec-909d-000ba746fa2d`)
3. Use the full URL format for the relation: `https://www.notion.so/{page_id_no_dashes}`

---

## Step 5: Confirm & Log

After posting:
1. Confirm to Richard with the page title and a one-line summary of what was posted
2. If the research surfaced anything that warrants a follow-up action, flag it explicitly using the IAJ+2DSA framework:
   - **Judgement:** What does this mean for the investment case?
   - **Action 1:** Immediate next step
   - **Action 2:** Downstream action

---

## References

- Highlighting, formatting, quality gate, chunking: `memory/skills/researcher/notion-posting-sop.md` (canonical — this SOP inherits from it)
- Research pipeline: `memory/skills/researcher/SKILL.md`
- Known stock page IDs: maintained in `notion-posting-sop.md`
