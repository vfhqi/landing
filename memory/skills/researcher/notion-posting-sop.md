# Notion Posting SOP — Researcher Role

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] Created 02-Apr-26. Canonical reference for sentiment highlighting, posting mechanics, and Notion page properties for RESEARCHER role. -->
<!-- V2 18-Apr-26: Formatting rules migrated to notion-posting-standard/SKILL.md. This file retains: sentiment highlighting, content rules, page properties, naming conventions, chunking, verification. -->
<!-- Referenced by: RESEARCHER role file (SKILL-V2.md), IG workflow, KQ workflow -->

## Purpose

This SOP governs how Watson applies sentiment highlighting and posts research outputs to the Notion Stock Notes database. It is the RESEARCHER-specific posting mechanics file. All research types (IG, KQ, ESA, DD, monitoring, info flow) use this SOP.

**For formatting rules** (IAJA tagging, bullet structure, headers, bold, colour coding, BLUF, italic summaries, tables, text emphasis), see the **Notion Posting Format Standard** (`memory/skills/notion-posting-standard/SKILL.md`). That standard is cross-cutting and governs all roles. Load it before any Notion posting.

---

## Step 1: Apply Sentiment Highlighting

**Mandatory on ALL Notion postings. Never skip.**

### Colour System

- `<span color="green_bg">text</span>` — positive signals, bullish findings, strong competitive positions, upside scenarios, confirming evidence
- `<span color="yellow_bg">text</span>` — neutral observations, mixed signals, uncertainties, caveats, "watch this space"
- `<span color="red_bg">text</span>` — risks, bearish signals, threats, downside scenarios, negative data, execution concerns

### What to Highlight — Individual Key Points, NOT Whole Paragraphs

Highlighting targets the specific sentence or phrase that carries the signal. Do NOT wrap entire paragraphs in a single highlight span.

**Good example:**
```
Instalco reported mixed Q4 results. <span color="green_bg">Adjusted EBITA margin expanded 30bps YoY to 7.1%, beating consensus by 50bps.</span> Management maintained a cautious tone. <span color="red_bg">Net debt/EBITDA remains elevated at 2.8x, above the 2.5x ceiling target.</span> The company hosted an analyst day in Stockholm.
```

**Bad example (do NOT do this):**
```
<span color="green_bg">Instalco reported mixed Q4 results. Adjusted EBITA margin expanded 30bps YoY to 7.1%, beating consensus by 50bps. Management maintained a cautious tone. Net debt/EBITDA remains elevated at 2.8x, above the 2.5x ceiling target. The company hosted an analyst day in Stockholm.</span>
```

### Coverage Target

**30%+ of text must be highlighted.** Err on more. Achieve through many precisely targeted highlights, not a few massive blocks.

### Method

Apply highlighting BEFORE posting. Sentiment is Watson's judgement of positive/neutral/negative signals for the investment case. Richard should skim green and red highlights to grasp the key data points without reading every word.

**Selection criteria:**
- Specific numbers, percentages, financial metrics → highlight the containing sentence
- Analyst ratings, target price changes → highlight the specific statement
- Strategic pivots, management quotes → highlight the key sentence
- Risk factors, threats → highlight the specific risk statement
- Growth drivers, competitive advantages → highlight the specific positive claim
- Do NOT highlight transitional sentences, scene-setting context, or filler

### Sentiment Highlighting + IAJA Colour Coding

These are two separate visual layers that coexist. See §2 of the Notion Posting Format Standard for how they interact. A bullet can carry both a sentiment highlight (green/yellow/red background) and an IAJA prefix label (Judgement:/Analysis:/Action:).

---

## Step 2: Format Content for Notion Readability

**Load and follow the Notion Posting Format Standard** (`memory/skills/notion-posting-standard/SKILL.md`). It governs:

- IAJA bullet suffix tags (#J, #A, #I, #T, #O, #KR, #OQ)
- Colour-label prefixes (Judgement:, Analysis:, Action:)
- J → A → I ordering within parent + sub-bullet structures
- BLUF at page level (3-5 bullets) and section level (italic opening sentence)
- Bullet structure (parent + sub-bullets, 100-word cap, shorter sentences)
- Italic summary sentences at section close
- Headers (clear, descriptive, scaled to length)
- Bold (heavy — metrics, analysts, ratings, percentages, conclusions)
- Tables (pipe only, never HTML)
- Text emphasis (bold, italic, underline, strikethrough)
- Horizontal rules between major sections

### Structure Conventions by Research Type

- **Most Recent Earnings Review:** H2 for each memo section. 10-18 bullets per section. Overall Summary at front with 10-20 bullets. BLUF at top.
- **GTH Analysis:** H2 for each of 3 sections (Market Perception, Fundamental Delivery, Peer/Sector Relative). H3 for numbered sub-sections. BLUF at top and per H2.
- **Peer GTH Analysis:** H2 for Overall Summary + each analysis dimension. H3 per company.
- **GTA Unknown KDs:** H2 for each key driver (stack-ranked). Within each driver, H3 for guidance, plausibility, bearish view, end-market conditions.
- **Sell Side (SS) Analysis:** H2 for each of 3 sections + Overall Summary. H3 per analyst within each section. **SS = Sell Side, NOT Short Seller.**

---

## Step 2.5: Pre-Flight Quality Gate — MANDATORY

**Load and apply the Pre-Flight Quality Gate from the Notion Posting Format Standard** (§14). The checklist there supersedes any prior version in this file.

Additional RESEARCHER-specific checks:

- [ ] **Two-tier word count gate (revised 24-Apr-26):** Output passed the two-tier validation in as-claude-research-sop-v2.md Step 5? (<50% = hard floor, 50-75% = quality gate with section completeness, >75% = pass). If `"quality_flag": "below_target"` in metadata, confirm section coverage was ≥80% before posting.
- [ ] **Content completeness:** Word count of formatted content matches source file within 90%?
- [ ] **Full-length posting:** No summarisation, abridging, or truncation of source output?

### Protocol

1. Run the Format Standard checklist + the above checks on actual formatted content
2. If ANY item fails → fix before proceeding to chunking/posting
3. On batch operations: full checklist on FIRST page. If passes, proceed. If fails, fix and re-run.
4. Log pass/fail result before posting

---

## Content Rule

**Post the COMPLETE output.** Never summarise, condense, abridge, or truncate. The Notion page IS the memo.

- Research output of 5,250 words → 5,250 words go into Notion
- AlphaSense output of 10,000 words → 10,000 words go into Notion
- The only acceptable reason for a shorter posting is if the source output itself was short

---

## Target Database

Stock Notes DB: `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2`

---

## Page Properties

```
Note title: [W] {TICKER} - {Stage} - {Research Type} - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY
date:Date:start: YYYY-MM-DD
date:Date:is_datetime: 0
Main focus of note: Stock(s)
Info, analysis, judgement and/or action: Information
Depth of note: Watson posting of information
Case component: Inputs / change forces
Stock(s): [linked to the stock's Notion page — use full URL format]
```

### Stock(s) Relation — Correct Format

Use the **full Notion URL** for the relation property, NOT the `relation:` prefix:
```
"Stock(s)": "https://www.notion.so/{page_id_no_dashes}"
```

#### Known Stock Page IDs (main Stocks DB)
| Ticker | Stock Page ID | URL |
|---|---|---|
| HFG | 25e35e90-9b0b-80f0-9731-c9a15a581e25 | `https://www.notion.so/25e35e909b0b80f09731c9a15a581e25` |
| INSTAL | 29d35e90-9b0b-80ce-b0e1-e34013671e11 | `https://www.notion.so/29d35e909b0b80ceb0e1e34013671e11` |
| EVOK | 2bf35e90-9b0b-838d-ac69-016f1851a915 | `https://www.notion.so/2bf35e909b0b838dac69016f1851a915` |
| BYLOT (Bally's Intralot) | 26835e90-9b0b-8044-b7f8-fa1431655195 | `https://www.notion.so/26835e909b0b8044b7f8fa1431655195` |

**Always verify the stock page is in the main "Stocks" DB** (collection://25435e90-9b0b-80ec-909d-000ba746fa2d), not the backup DB.

- `{SOURCE}` = `[C]` for Claude, `[AS]` for AlphaSense, `[W]` for Watson synthesis
- Date = execution date (when the research was run, not when it's posted if different)

---

## Naming Conventions

See §12 of the Notion Posting Format Standard for the full title convention, rules, and examples. The title format and all examples are maintained there as the single source of truth.

**Briefing Note special properties:** Depth = "Watson back-brief", IAJA = `["Analysis", "Judgement", "Action needed - Research"]`, Case component = blank. Full SOP: `briefing-note-sop.md`.

---

## Step 3: Chunking for Large Memos

Notion has content size limits. For memos exceeding **15K characters**:

1. Create the page with the first chunk (BLUF + first sections) via `create-pages`
2. Append remaining sections via `update-page` with `update_content` command
3. Match the last line of existing content as `old_str` and append new content as `new_str`
4. If the match fails, fetch the page first to see exact Notion-rendered content, then match against that

**This is not optional.** Large memos MUST be chunked and fully posted, not cut short.

---

## Step 4: Quality Verification — Automated Spot-Check

**After each posting wave**, Watson runs a verification agent on a sample of posted pages. Mandatory and automatic.

### Verification Agent Protocol

1. **Sample selection:** Pick 1-2 pages at random from the wave
2. **Fetch the page** from Notion
3. **Check highlighting coverage:** 30%+ minimum. 40-50% is the sweet spot.
4. **Check content completeness:** Word count >80% of source file. If less, content was truncated.
5. **Check properties:** Date, case component, depth, stock relation, source tag all correct.
6. **Check Format Standard compliance:** BLUF present, suffix tags present, J→A→I ordering.
7. **If a page fails:**
   - Highlighting <30%: Re-highlight and repost
   - Content truncated: Append missing sections
   - Wrong properties: Fix via update_properties
   - Missing BLUF/tags: Re-format and repost
8. **Log result:** Report pass/fail before proceeding to next wave

---

## References

- **Formatting standard:** `memory/skills/notion-posting-standard/SKILL.md` — load FIRST
- Research execution: `memory/skills/researcher/as-claude-research-sop-v2.md`
- Research pipeline logic: `memory/skills/researcher/SKILL-V2.md`
- Prompt templates: `memory/skills/researcher/templates/`
