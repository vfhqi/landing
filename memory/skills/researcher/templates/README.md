# ESA Research Templates — Usage Guide

## What These Files Are
These are **research template/SOP files** for the RESEARCHER role at Stage 3 (ESA). Each file (08-14) is a self-contained guide that tells you:
1. **What to research** (MISSION, CONTEXT)
2. **Exactly how to research it** (detailed PROMPT for [AS] and/or [C] versions)
3. **Where to find sources and how to execute** (EXECUTION section)
4. **What quality to target** (word count, quantification, bullet discipline, tables)

## What These Files Are NOT
These templates are NOT the final research output. The word counts shown in each template file's metadata are for the *instructions themselves* (the MISSION, CONTEXT, PROMPT, EXECUTION sections). When you execute the template:
- You will produce **3,000-4,000 words of actual research output** per query (depending on query)
- That research output will be posted as a [W] page in Notion
- The template acts as your guide; the Notion page is the deliverable

## How to Use a Template

### 1. Select Your Template
You're researching {TICKER} at ESA stage. Choose which query (8-14) you're executing:
- **Query 8:** Business Model & Sector Primer (foundational)
- **Query 9:** Earnings History L3Y (foundational)
- **Query 10:** Short-Sellers & Bear Case (foundational)
- **Query 11:** Value-Chain Map (support)
- **Query 12:** Value-Chain Analysis (support)
- **Query 13:** Guidance Tracking & Credibility (support)
- **Query 14:** KD Assessment (strategic — requires APM Pass 1 input)

### 2. Read the Entire Template
- **MISSION:** Understand what output you're producing and for whom
- **CONTEXT:** Internalise why this query matters and what the reader cares about
- **PROMPT:** Read the full prompt (either [AS] or [C] or both)
- **EXECUTION:** Understand source requirements and quality gates

### 3. Gather Context / Inputs
For most queries: Standard {TICKER}, {COMPANY}, {INDUSTRY}, {PEERS} placeholders. Fill these in.

For **Query 14 ONLY**: Get {APM_KD_SUMMARY} from the APM (their Pass 1 findings). This is critical — don't start Query 14 without this input.

### 4. Execute Research
Use the PROMPT section as your literal research brief. For [AS] queries, run through AlphaSense using the prompt verbatim (or close). For [C] queries, feed the prompt to Claude with WebSearch enabled.

The prompt is structured in numbered sections with detailed instructions on what to search for, what to include, what to quantify, what to challenge with scepticism.

### 5. Synthesise Output
As you research, write your findings in real-time or synthesise into a structured output:
- Lead with 500-word executive summary
- Detailed sections (follow the PROMPT structure)
- Quantified assertions
- Tables/summaries (see EXECUTION section for table types required)
- Red/Orange/Yellow/Green ratings where specified

### 6. Post to Notion
Follow the "Notion Posting Convention" section at the bottom of each template:
- Title format: `[W] {TICKER} — Query Name [Source] @ DD-Mon-YY`
- Tags: #ESA #{QueryTheme}
- Highlight 30%+ with process_report.py
- Cross-link to related pages (stock notes, APM Pass 1 for Query 14, etc.)

## Word Count Gates (Actual Research Output)

These are the word counts you should target for your **research output** (the Notion page), not the template file:

| Query | Single-Source | Dual-Source | Per-Driver (Q14) |
|-------|---------------|-------------|-----------------|
| 08 BM | — | 3,000+ per version (AS + C) | — |
| 09 Earnings | 3,000+ | — | — |
| 10 Short | — | 3,000+ per version (AS + C) | — |
| 11 Value-Chain Map | 3,000+ | — | — |
| 12 Value-Chain | 3,000+ | — | — |
| 13 Guidance | 3,000+ | — | — |
| 14 KD | — | 4,000+ per version (AS + C) | 400-600 per driver |

**Note on Query 14:** If the APM identified 6 key drivers, your [AS] output should be ~5,000-6,000 words total (500-word summary + 6 drivers × 500-700 words each). Same for [C] version.

## Quality Gates (All Queries)

### Quantification
- Every assertion about market size, growth rates, margins, returns, market share, concentrations, probabilities, or trends must include a specific number or percentage
- "The company is growing" ❌
- "The company is growing at 12% CAGR over L3Y" ✓

### Bullets & Structure
- Major sections: 12-18 bullets (Query 14: 8-12 per driver)
- Each bullet: 100-150 words max
- Self-contained bullets; avoid "as mentioned above" references

### Tables
- Every query requires at least 1-2 summary tables
- Tables must be clean, readable, quantified, and easily referenced from text
- See EXECUTION section of each template for specific table requirements

### Scepticism / Red Flags
- Every query must include explicit bear-case or sceptical view section
- Do not dismiss counter-arguments; present them fairly with evidence
- Rate drivers/assertions on **Red/Orange/Yellow/Green scale** with explanation:
  - **Green:** High confidence; bull case well-supported
  - **Yellow:** Medium confidence; uncertainty remains
  - **Orange:** Low confidence; bear case stronger
  - **Red:** Very low confidence; unlikely to work as assumed

### Highlighting
- 30%+ of content highlighted in Notion using process_report.py
- Highlight key evidence, inflection points, risk statements, quantified milestones, ratings

### No Repetition
- Each section must add new information
- Don't restate the same insight across multiple sections
- If using the same data point twice, reference it rather than repeat

## Source Selection (AS vs C)

### [AS] = AlphaSense Deep Research
Use for:
- Sell-side research access (equity reports, consensus estimates, revision trends)
- Earnings call transcripts (company management, customers, suppliers, competitors)
- Expert network calls (industry experts, management interviews)
- Proprietary financial data (FactSet, Bloomberg)

**Queries using AS only:**
- Query 9 (Earnings History) — need quarterly/semi-annual consensus vs actual data
- Query 12 (Value-Chain Analysis) — need sell-side commentary on customers/suppliers/competitors
- Query 13 (Guidance Tracking) — need sell-side estimate revisions and management guidance history

**Queries using AS + C:**
- Query 8 (BM Primer) — AS gives sell-side research + FactSet; C gives WebSearch + public filings
- Query 10 (Short-Sellers) — AS gives sell-side bearish research; C gives published short reports + public commentary
- Query 14 (KD Assessment) — AS gives sell-side deep evidence; C gives WebSearch + public filings

### [C] = Claude with WebSearch
Use for:
- Public company filings (10-K, 10-Q, annual reports, proxy statements)
- Press releases, news archives, investor announcements
- Competitor analysis via public sources
- SEC Edgar data
- Industry reports, analyst summaries, public research

**Query using C only:**
- Query 11 (Value-Chain Map) — structural mapping using public sources, competitor research, industry analysis

## Critical Handoff: Query 14 (KD Assessment)

**This query is different.** It runs AFTER the APM has completed ESA Pass 1.

**Sequence:**
1. APM completes FCS Analysis & Judgement (Pass 1), posts to Notion
2. APM (or parent RESEARCHER) extracts the following into a summary:
   - Specific 5-8 key drivers identified as material to the case
   - Which 2-3 drivers does APM suspect are fulcrum-level?
   - What evidence gaps did APM flag?
   - What's the preliminary setup classification hypothesis? (HQI, BFF, Turnaround, etc.)
   - What open questions should Query 14 research answer?
3. RESEARCHER (you) read the summary, fill in {APM_KD_SUMMARY} placeholder in Query 14 template
4. RESEARCHER executes Query 14, targeting research specifically on APM-identified drivers
5. RESEARCHER posts Query 14 output including "Watson Back-Brief" section with:
   - Per-driver plausibility rating (Red/Orange/Yellow/Green)
   - Fulcrum-level confirmation/challenge
   - Setup classification confirmation/challenge
   - Key monitoring metrics for each fulcrum driver
   - DD priorities
6. APM reads Query 14 back-brief, uses to refine Pass 1 judgement, completes ESA Pass 3

**Critical:** Do NOT start Query 14 without {APM_KD_SUMMARY}. This creates a feedback loop between APM judgement and RESEARCHER evidence.

## Integration with Other Skills

These templates sit within the broader RESEARCHER skill architecture:

```
RESEARCHER Skill
├── Stage 1: Ideas Generation (IG) — 3 templates (01-03)
├── Stage 2: Triaging — 5 templates (04-07)
└── Stage 3: ESA — 7 templates (08-14) ← YOU ARE HERE
    ├── Pass 1: APM FCS Analysis & Judgement
    ├── Pass 2: RESEARCHER deep-dive (Queries 8-14)
    └── Pass 3: APM refinement & setup finalization
```

Related skills/frameworks:
- **ASSISTANT-PORTFOLIO-MANAGER:** APM runs FCS Analysis; ECO/Pass 1/Pass 3 steps
- **kq-workflow:** Different research methodology (Key Question deep-dives) — used during DD, not ESA
- **high-performance-coach:** Coaching on investment process, decision-making quality

## Quick Checklist Before You Start

- [ ] Template file selected (08-14)?
- [ ] {TICKER}, {COMPANY}, {INDUSTRY}, {PEERS} defined?
- [ ] For Query 14: {APM_KD_SUMMARY} provided by APM?
- [ ] [AS] or [C] source(s) available and logged in?
- [ ] Read template CONTEXT section — understand why this query matters?
- [ ] Understand EXECUTION section — know source requirements & quality gates?
- [ ] Time budget: 2-4 hours per query (varies by query complexity)?
- [ ] Ready to quantify everything and include sceptical view?

## Troubleshooting

**Q: Template says "3,000 words" but I've written 1,500. Am I done?**
A: No. The 1,500 words are likely your template instructions/planning. The actual research output needs to be 3,000+ words. Keep researching and synthesising findings.

**Q: Do I have to follow the PROMPT sections verbatim?**
A: Treat the PROMPT as a detailed research brief, not a script. You can adapt based on source findings, but cover all major instruction points. If you skip major instruction sections, you'll leave coverage gaps.

**Q: What if a section in the PROMPT doesn't apply to this stock?**
A: Still attempt it. Document your reasoning for why it doesn't apply. Example: "This stock has no published short-seller reports (unlike many Tech/fintech stocks). Short interest is <1% and show no activist history." That's useful information.

**Q: Can I combine Queries 8 and 9, or 11 and 12?**
A: Not recommended. Each query is self-contained and posts separately to Notion. Combining dilutes focus and makes it hard for APM to cross-reference specific insights. Post separately; include cross-references in each Notion page.

**Q: When should I post to Notion?**
A: As you complete each query. Don't wait to finish all 7 queries and then post. Post Queries 8-13 within 2-3 days; Query 14 follows after APM provides KD summary (typically 4-5 days into ESA phase).

**Q: Should I read all prior Notion pages before starting Query 8?**
A: Yes. Read Stock Notes from Triaging phase (Queries 1-7), any APM commentary, any context from the APM's Pass 1 FCS Analysis. This ensures you're not repeating work and you're calibrated to APM's thinking.

## Final Note

These templates are thorough and detailed by design. They represent the institutional knowledge of Richard's investing system, calibrated through years of experience. Trust them. They exist to ensure you don't miss critical angles, evidence, or red flags.

When in doubt, err toward **more research, more quantification, more scepticism**. It's better to over-prepare for APM's refinement than to under-prepare and create blind spots.

Good luck.
