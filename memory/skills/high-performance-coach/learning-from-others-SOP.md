# Learning From Others SOP
<!-- [W] Created 10-Apr-26 by Systems Architect for HPC role -->

## Purpose

Structured process for extracting, synthesising, and applying lessons from great thinkers — investing, psychology, philosophy, strategy, science, leadership, or any domain. The goal: help Richard learn in the evenings from the best minds, with high practical utility, in a format that sticks.

This is an HPC sub-skill. It serves the broader development agenda of building Richard's mental model library and connecting external wisdom to his investing system.

---

## When to Trigger

- Richard requests a "Learning From Others" session on a specific author/book
- A Notion Task in the Tasks DB references this SOP or requests author summaries
- Watson identifies a gap in Richard's framework that a specific thinker addresses (propose, don't execute without approval)

---

## Inputs

Richard provides:
- **Author and/or book/framework** to study
- **Level of back-brief** (default: detailed brief first, then autonomous execution)

Watson determines:
- Research scope (web search breadth, training knowledge depth)
- Personalisation mapping (which parts of Richard's system connect)
- Podcast theme and angle

---

## Outputs — Two Deliverables Per Author/Book

### Output 1: Notion Journal Summary (~10,000 words)

**What it is:** A comprehensive, structured summary of the author's most important concepts, principles, mental models, and insights. Faithful to the author's thinking first. Practical applications to Richard second.

**Structure:**
1. **Opening Context** (~500 words) — Who is this person? Why do they matter? What's the core thesis? What should Richard pay attention to as he reads?
2. **Core Framework / Key Concepts** (~6,000-7,000 words) — Each major concept gets its own H2 section containing:
   - The idea itself (author's own language and reasoning)
   - Supporting evidence, data, examples, stories
   - **Applications to Richard** sub-section (H3) — mapped to his system, patterns, stocks, current situation. Uses IAJA, ETCs, 6-stage process, stock archetypes, track record examples where relevant
3. **Synthesis: The 10 Most Useful Principles** (~1,500 words) — Distilled, ranked by practical utility to Richard. Each principle: one sentence, then 2-3 sentences on how to apply it
4. **Challenges & Tensions** (~500 words) — Where does this author's thinking conflict with Richard's current approach? Where does it confirm? What's the productive tension?
5. **One-Page Cheat Sheet** (~500 words) — If Richard could only take one page of notes from this author, what would be on it? Bullet format, dense, actionable

**Formatting:** Per Notion Posting Format Standard (`memory/skills/notion-posting-standard/SKILL.md`):
- Headers proportional to length per Format Standard §7. BLUF at page + section level. IAJA suffix tags on bullets.
- Heavy bold on all key terms, frameworks, statistics, author names
- Sentiment highlighting:
  - `green_bg` = high-utility insights, directly actionable, confirms/strengthens Richard's system
  - `yellow_bg` = contextual, interesting but not immediately actionable, nuanced points
  - `red_bg` = warnings, tensions with Richard's approach, common mistakes, things to watch out for
- 30%+ highlighting coverage, sentence-level precision (not paragraph blocks)

**Posting location:** Notion Journal
**Title format:** `[W] {Author} — {Book/Framework Title} — Learning From Others [C] @ DD-Mon-YY`
**Properties:**
```
date:Date:start: YYYY-MM-DD
date:Date:is_datetime: 0
```

### Output 2: Podcast Script (30 minutes, ~4,500 words)

**What it is:** A coaching-style audio script derived from the Notion summary. Solo narrator voice (Watson as coach speaking to Richard). Follows the Daily Podcast SOP format rules.

**Relationship to summary:** The podcast is DERIVED from the summary, not independently written. It distils the highest-utility lessons into spoken format, with heavier personalisation than the written summary.

**Structure:**
1. **Opening hook** (~300 words) — Why this thinker matters to Richard right now. Connect to current pipeline, market context, or recent coaching themes
2. **Core lessons** (~3,200 words) — 4-6 of the most powerful concepts, delivered conversationally. Each lesson: explain the idea, tell the story/evidence, then apply directly to Richard's situation with specific stock examples and journal references
3. **The productive tension** (~400 words) — Where does this challenge Richard? What should he sit with?
4. **Single actionable takeaway** (~300 words) — One thing to do differently starting tomorrow
5. **Close** (~200 words)

**Format rules:** Per Daily Podcast SOP:
- No bullet points in spoken script — flowing speech only
- Short to medium sentences, varied rhythm, rhetorical questions
- [PAUSE], [slower], [with emphasis], [beat] markers
- No hedging, no corporate language, no emoji
- Journal quotes delivered slowly with space

**Saving:** `memory/coaching/podcast-library/YYYY-MM-DD-{author-slug}-learning-30.md`
**INDEX.md:** Updated with new entry

---

## Workflow — Step by Step

### Phase 1: Brief & Confirm

1. Load this SOP
2. Load HPC SKILL.md (for personalisation context, patterns, identity anchors)
3. If author is investing-related, also load relevant coaching reference files (risk-management-lessons.md, stock-archetypes.md, track-record-by-stock.md)
4. Present brief to Richard: what I'll cover, how I'll structure it, estimated scope
5. Ask up to 5 clarifying questions (concise bullets)
6. On confirmation, proceed autonomously

### Phase 2: Research

7. **Web search broadly** — search for the author's core framework, key concepts, interviews, summaries, reviews, critiques. Cast a wide net. Prioritise primary sources (the author's own words) over secondary summaries
8. **Cross-reference with training knowledge** — supplement web research with what Watson knows from training data
9. **Identify the 8-12 most important concepts** — these become the backbone of the summary
10. **Map to Richard's system** — for each concept, identify the connection point (which part of his process, which stock archetype, which behavioural pattern, which mental model)

### Phase 3: Write Summary

11. Write the full ~10K-word summary following the structure above
12. Apply sentiment highlighting throughout (green/yellow/red, sentence-level, 30%+ coverage)
13. Apply Notion formatting (headers, bold, tables where useful)
14. Run Pre-Flight Quality Gate (Notion Posting SOP Step 2.5):
    - H2 count: 8-15?
    - H3 count: 15-25?
    - Bold density: all key terms, metrics, framework names bolded?
    - Highlight coverage: 30%+?
    - Highlight precision: sentence-level, not paragraph-level?

### Phase 4: Post to Notion

15. Post to Notion Journal using chunking protocol for large memos (>15K characters)
16. Set properties (title format, date)
17. Verify posting quality (fetch page, spot-check highlighting, headers, content completeness)

### Phase 5: Derive Podcast

18. Read the posted summary (or working draft)
19. Select the 4-6 highest-utility concepts for the podcast
20. Load podcast preparation files:
    - `coaching/podcast-library/INDEX.md` (check recent themes/authors)
    - `coaching/track-record-by-stock.md` (pull specific stock examples — NOT just BFF/XVIVO/Goodwin)
    - `coaching/stock-archetypes.md` (identify matching archetypes)
    - `coaching/risk-management-lessons.md` (pull relevant Watson Coaching Prompts)
21. Write the 30-min script (~4,500 words) following podcast structure and format rules
22. Run podcast quality checklist (word count, spoken-aloud readability, stock depth check, archetype check, actionable takeaway)
23. Save to `coaching/podcast-library/` with correct naming
24. Update INDEX.md

### Phase 6: Quality Verification

25. Fetch the Notion page and verify:
    - Full content present (word count check)
    - Highlighting 30%+ and sentence-level
    - Headers and bold density correct
    - Properties correct
26. Verify podcast script:
    - Word count 4,500 ±450
    - Minimum 5-6 different stocks referenced
    - At least 2 archetypes named
    - Ends with single actionable takeaway
27. Report completion to Richard with links

---

## Quality Standards

### The Summary Must Be:
- **Comprehensive** — cover the author's full framework, not just the famous bits
- **Faithful** — represent the author's actual thinking, not a strawman or oversimplification
- **Practical** — every concept must answer "so what does Richard do with this?"
- **Stimulating** — the writing should be engaging, not encyclopaedic. Challenge Richard's thinking
- **Well-sourced** — use the author's own language, specific data points, named examples

### The Podcast Must Be:
- **Conversational** — sounds like a coach talking, not an essay being read aloud
- **Personal** — references Richard's specific stocks, patterns, and journal entries
- **Challenging** — doesn't just confirm existing beliefs; pushes on tensions and blind spots
- **Actionable** — ends with one concrete thing to do differently

### What "Good" Looks Like:
- Richard reads the summary in one evening sitting and marks up 10+ passages as personally useful
- The podcast makes Richard think about a current position differently
- 3 months later, Richard can recall 3-4 key principles from the author and has applied at least one

---

## Canon — Current Author List

This list grows over time. Add authors as Richard requests them.

### Requested (pending execution)
| Author | Book/Framework | Requested | Status |
|--------|---------------|-----------|--------|
| **Chris Hohn** | Investment strategy (podcast series) | 06-Apr-26 | Pending |
| **Jack Schwager** | Market Sense and Nonsense | 06-Apr-26 | Pending |
| **Steve Cohen** | Risk management & approach (podcast series) | 06-Apr-26 | Pending |

### Completed
| Author | Book/Framework | Completed | Notion Link |
|--------|---------------|-----------|-------------|
| **Lee Freeman-Shor** | The Art of Execution | 10-Apr-26 | [Notion](https://www.notion.so/33e35e909b0b81dc9afcdf1a0653d975) |
| **Stephen Bungay** | The Art of Action | 13-Apr-26 | [Notion](https://www.notion.so/34135e909b0b81638f57fde2b7098fa7) |

---

## Integration Points

| System | How Learning From Others connects |
|--------|-----------------------------------|
| **HPC SKILL.md** | Listed under Reference-Only loading section. Triggered explicitly by Richard or by Tasks DB |
| **Daily Podcast SOP** | Podcast output follows same format, saved to same library, shares canon list |
| **Coaching Frameworks** | New authors may be promoted to the coaching-frameworks.md canon if Richard finds them high-utility |
| **Notion Posting SOP** | All formatting, highlighting, and posting mechanics governed by that SOP |
| **Session Handoff** | Completion of a Learning From Others session logged in handoff notes |
| **CLAUDE.md** | Canon list cross-referenced with Extended Canon in Daily Podcast SOP |

---

## Key Files

| File | Purpose |
|------|---------|
| This file | SOP definition — workflow, standards, canon list |
| `../../coaching/podcast-library/INDEX.md` | Podcast episode index |
| `../../coaching/podcast-library/*.md` | Individual podcast scripts |
| `../references/coaching-frameworks.md` | Existing framework summaries (may be enriched by this SOP) |
| `../../skills/researcher/notion-posting-sop.md` | Formatting and posting mechanics |
| `../../coaching/track-record-by-stock.md` | Stock examples for personalisation |
| `../../coaching/stock-archetypes.md` | Archetype matching for personalisation |
| `../../coaching/risk-management-lessons.md` | Risk management rules for personalisation |
