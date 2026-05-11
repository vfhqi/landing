# A&J Comms SOP — Per-Stage Memo Construction (1x weight)

**Version:** 1.0 — first standing version
**Authored:** 10-May-26 by Watson (APM role)
**Source:** distilled from HTRO V4 sculpt → Triaging/ESA/DD memos at Step 3 of Workstream 1 plan
**Test stock validation:** HTRO — three sculpted memos at `PROJECTS/SA - Reports & Memos Repository/htro-test-stock/`

**Weight in three-SOP hierarchy:** 1x — supporting the substance SOP. The substance is what matters; this SOP determines how the substance is communicated at each stage.

---

## §0 — PURPOSE + SCOPE

### What this SOP delivers

A standing methodology for sculpting an A&J master file (the substance) into per-stage memos at Triaging, ESA, and DD depths. Each stage has different reader expectations + different decision-grade requirements.

### Reader profiles by stage

**Triaging memo** — for the analyst (Richard or Watson) deciding "should I spend more time on this?" Reading time: 5-15 minutes. Decision: Park / Progress to ESA / Kill.

**ESA memo** — for the analyst (Richard or Watson) deciding "is the case credible enough for DD?" Reading time: 30-60 minutes. Decision: Park / Progress to DD / Kill.

**DD memo** — for the analyst (Richard) deciding "should I add this to the concentrated long-only book?" Reading time: 2-4 hours. Decision: Buy / Park / Kill + position size + entry triggers.

### Word target framework

| Stage | Word target | Section emphasis |
|---|---|---|
| Triaging | 2,000-5,000 | C-section pillar ratings (compact); strong BLUF; minimal decomposition |
| ESA | 4,000-12,000 | Pillar I/II/III decomposition; segment-level analysis; explicit ACHs |
| DD | 5,000-25,000 | Full sub-element decomposition; counter-hypothesis engagement; deep bear/bull cases; SOTP valuation |

The HTRO test produced Triaging 2,067w / ESA 4,105w / DD 5,723w — proportional to V4 source depth (5,269w). Word count should match the substance available, not be artificially inflated.

---

## §1 — STAGE-SPECIFIC SCULPT RULES

### Triaging memo sculpt rules

**Header (mandatory):**
- Primary setup statement (≤30 words)
- Secondary setup statement (≤30 words)
- Conviction (1-letter rating + brief reasoning)
- Time horizon
- Position-sizing recommendation (1-line)

**BLUF (mandatory, 3-5 bullets):**
- Each bullet is a judgement (no data, no hedging)
- Each tagged #J
- Together = the entire case in <100 words

**Sections (5 standard):**
- §A Financials (compact: snapshot + earnings trajectory + outliers; 300-500w)
- §B Setup classification + triple ratchet (300-500w)
- §C Pillar ratings compact (P1-P6 with brief justification each; 600-1000w)
- §D In-flight monitoring (5 metrics + 10 ACHs + 5 risks compact; 400-600w)
- §E Actions (recommendation + entry/exit framework + next stage gate; 200-400w)

**Forbidden at Triaging depth:**
- Sub-element decomposition for BB#2 (just headline rating)
- Per-ACH evidence chains (just list the 10 triggers)
- Sum-of-parts valuation tables (just the headline ratio)
- Mental-model lens application (defer to DD)
- 5-year vivid scenarios (defer to DD)

### ESA memo sculpt rules

**Header (same as Triaging, slightly fuller — 100-200w):**
- Add: 12-month fulcrum events list
- Add: composite Master Rating range with reasoning

**BLUF (mandatory, 4-6 bullets):**
- Slightly fuller than Triaging; can include 1-2 analytical points (#A) alongside judgements

**Sections (6 standard):**
- §A Financials with cycle context + segment margins (1,000-1,500w)
- §B Setup classification + triple ratchet quantified (800-1,200w)
- §C Pillar ratings deeper (P1-P6 with sub-element ratings for BB#2; 1,500-3,000w)
- §D In-flight monitoring with action protocols (800-1,500w)
- §E Actions + cohort framework (500-1,000w)
- §F Process notes (200-400w)

**Allowed at ESA depth:**
- Sub-element decomposition for Pillar I + BB#2 specifically
- Per-segment margin trajectory
- Peer comparable table (compact)
- Entry/exit framework with quantitative thresholds

**Still forbidden at ESA depth:**
- Full Pillar I/II/III sub-element decomposition (defer to DD)
- Mental-model lens application (defer to DD)
- 5-year vivid scenarios (defer to DD)
- Self pre-mortem (defer to DD)

### DD memo sculpt rules

**Header (full — 200-400w):**
- All Triaging + ESA elements
- Add: probability-weighted return calculation
- Add: position-sizing recommendation with entry/exit/trim/sell zones

**BLUF (mandatory, 5-8 bullets):**
- Mix of #J + #A + #I as appropriate
- Captures full case in ≤200 words

**Sections (6 standard, but each at DD depth):**
- §A Financials at DD depth: cycle context + segment financials + margin durability + beat/miss pattern + sandbagging dynamics (3,000-5,000w)
- §B Setup + triple ratchet quantified scenarios (Bull/Base/Bear with specific EBITA contributions per segment; 2,000-4,000w)
- §C Pillar ratings full decomposition (Pillar I E1-E3 + E1.5; Pillar II BB#1-#5 with full sub-elements; Pillar III D.I-D.IV; 5,000-12,000w)
- §D In-flight monitoring with full ACH evidence chains + risk specifications (2,000-4,000w)
- §E Actions + cohort framework + catalyst monitoring (1,000-2,000w)
- §F Process notes + Phase 0.3 hunts record + Wisdom Library models consulted + 3-Check Declaration (500-1,000w)

**Required at DD depth (15-box V3 stopping rule):**
- Full BB#2 sub-element decomposition with segment-isolated ratings
- Comparable-company quantitative table with verified peer multiples
- Sum-of-parts valuation with 3-4 scenarios
- Substantive opposing-view section (deep bear case ≥3,000w + symmetric deep bull case ≥3,000w) — OR clear cross-reference to V3-style standalone document if that exists
- Mental-model lenses (Buffett/Marks/Klarman/Munger/Druckenmiller — at least 5)
- 5-year vivid scenario narration (Bull/Base/Bear)
- "What if I'm completely wrong?" pre-mortem
- Cohort stress-test against named comparable cohort entries

---

## §2 — UNIVERSAL CONVENTIONS (apply at every stage)

### J → A → I bullet ordering
Lead with judgement (parent bullet); support with analysis (first sub-bullets); underpin with information (final sub-bullets). Reverse of academic writing — the reader needs the answer, not the buildup.

### IAJA suffix tags on every substantive bullet
- #J Judgement, #A Analysis, #I Information, #T Task, #OQ Open Question

### Colour-coded prefixes on parent bullets
- *(no prefix)* black for plain Information
- **Analysis:** blue for Analytical observations
- **Judgement:** purple for Conclusions
- **Action:** green for Tasks/Objectives/Open Questions

### BLUF (Bottom Line Up Front)
- Page-level: 3-5 judgement bullets immediately after H1
- Section-level: 1-2 italic sentences before detailed bullets

### Italic summary sentences at section ends
- Single most important takeaway from each section
- Compressed to one sentence
- No tag needed

### Outlier/sentiment markers
- 🚩 RARE for genuinely unusual + high-signal findings (use ≤3 per memo)
- ❌ for D/F findings
- ⚡ for outlier observations

### Bullet structure
- Hard cap ~30 words per parent bullet (signpost-label characters excluded)
- Sub-bullets up to 6 per parent (Miller 7±2)
- No grandchildren (max 2 disclosure levels)
- Flex sub-COUNT not bullet LENGTH

### Word target ranges (NOT hard caps)
- Triaging: 2,000-5,000 words
- ESA: 4,000-12,000 words
- DD: 5,000-25,000 words

The substance available determines the actual count. A V4-source DD memo at 5,723w is appropriate; a V3-source DD memo at 25k+ would also be appropriate. **Do NOT inflate word count for its own sake.**

---

## §3 — TRANSITIONS BETWEEN STAGES

### Triaging → ESA progression

When sculpting up a stage, EXPAND specific sections rather than rewrite from scratch. The Triaging memo's substance is preserved + deepened.

Specific expansions Triaging → ESA:
- §A: add cycle context, segment margins, beat/miss pattern
- §B: add quantified triple ratchet scenarios
- §C: add Pillar I/II/III decomposition, BB#2 sub-element ratings
- §D: add action protocols for tracking metrics, deeper risk specifications
- §E: add cohort framework, catalyst monitoring

### ESA → DD progression

Same principle — EXPAND, don't rewrite.

Specific expansions ESA → DD:
- §A: add full segment financials, margin durability assessment
- §B: add per-scenario quantification (Bull/Base/Bear EBITA per segment)
- §C: add full sub-element decomposition for all BBs, mental-model lenses, 5-year scenarios
- §D: add full ACH evidence chains, deeper risk specifications, soft signals
- §E: add catalyst monitoring with timing
- §F: add 3-Check Declaration, Phase 0.3 hunts record, Wisdom Library models consulted

---

## §4 — VALIDATION + CALIBRATION

### How to know if the Comms SOP worked

The Comms SOP worked if:
1. A Triaging memo gives Richard enough information to make Park/Progress/Kill decision in 5-15 minutes
2. An ESA memo gives Richard enough information to make Park/Progress/Kill + size starter position in 30-60 minutes
3. A DD memo gives Richard enough information to make full investment decision + position size + entry triggers in 2-4 hours
4. The progression Triaging → ESA → DD is incremental + expansive (not rewrite)

### Lessons from HTRO test

**Lesson 1:** Word count should match substance available. V4 source at 5,269 words → DD memo at 5,723 words is appropriate. Inflating to 25k just to hit the upper word target would have been padding.

**Lesson 2:** The polish layer (IAJA tags + prefixes + BLUF + italic summaries) adds ~15-20% words on convention overhead. This is acceptable for Triaging where it improves scannability; needs management on DD where 5,723 → ~6,500-6,800 polished is fine but 25k → 30k polished would be excessive.

**Lesson 3:** Section headers + structure must be CONSISTENT across stages. A reader who knows the Triaging structure can navigate the DD memo because §A/B/C/D/E/F mean the same thing at every depth.

**Lesson 4:** The italic section summaries at section ends are the single highest-leverage polish convention. They give a one-sentence takeaway for any reader who can't read the full section.

### Future SOP iterations

V1 (this document) is the first standing version. Subsequent versions should incorporate lessons from second-stock validation.

