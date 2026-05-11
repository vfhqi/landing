# Session Log — 29-Apr-26 EVE — Sheet3 Visual Style Test (HTRO IC#2 input forces)

**Role:** SYSTEMS ARCHITECT
**Mode:** EXECUTION
**Session start:** 29-Apr-26 (continuing from new-taxonomy pillar tree session)

## Brief (verbatim, paraphrased to anchor)

> CONTEXT: Testing a different way to display memo content.
> OBJECTIVE: Find a new way to display memo content that might be "clearer" for me to read/understand.
> PREPARATION: Open `29-Apr-26 - Memo formatting.xlsx` Sheet3. Go to NEW TAXONOMY PILLAR TREE. Load all style guidelines. Research UI best practices.
> REQUEST: Take the **required input forces** from NEW TAXONOMY PILLAR TREE for **HTRO** and present in the visual style of Sheet3.
> FIRST: Back-brief via Three Gaps + Mission Command. Only proceed once confirmed. Ask lots of questions. Anticompaction. Quality > speed.

## Source materials loaded

1. `databases/pillar-tree-new-taxonomy.html` — IC pillar, element "Required \"input\" forces?" with 2 RAs (Change forces?, Robust base?) and 7 CQs total.
2. `Files/NOT BACKED UP/RB downloads/RB excel tools/29-Apr-26 - Memo formatting.xlsx` Sheet3 — visual style mockup, three-column layout (RA / CQ / A&J), zebra fills, Aptos typography, rating chip in column E, pre-bullet em-dash markers " - ".
3. `databases/pillar-tree-canonical.json` — 165 CQs, 62 RAs, 18 elements (live taxonomy).
4. HTRO memo: `databases/memos/HTRO/ESA.json` (latest v3, 22-Apr-26 bake) — confirmed exists; needs read for IC#1/IC#2/IC#3 family blocks corresponding to "input forces" pillar of new taxonomy.

## Sheet3 visual style — observations from raw cell dump

**Layout:**
- Column C: RA label (italic, e.g., "#1 Longevity", "#5 Timeliness", "Change forces?", "Robust base?")
- Column D: CQ text (bold, prefixed with `#n  ` numbering)
- Column E: Rating chip (single character A/B/C/D/F)
- Column F: Analysis & Judgement bullets (anchor bullet bold/SemiBold; sub-bullets regular)
- Column I (right margin): tiny digits (5/10/20) — likely indent depth markers or grid hints, NOT user-visible content

**Typography:**
- Aptos throughout (matches Richard's preferred presentation register, per `feedback_ppt_build_pattern.md` and `feedback_presenter_prompts_register.md`)
- Headers (row 3 "Required attribute" / "Core question(s)" / "Analysis and judgement"): Aptos 11pt Bold
- RA labels: Aptos 10pt Regular Italic
- CQ text: Aptos 10pt Bold
- Anchor (lead) A&J bullet: Aptos SemiBold 10pt
- Sub bullets: Aptos 10pt Regular
- Rating: Aptos 10pt Regular

**Colour palette:**
- Header row fill: `#FDFCF1` (very pale cream)
- Zebra body fills alternate: `#FAF8D2` (pale yellow) / `#FDFCF1` (pale cream)
- Rating chips:
  - **A**: no fill (default white)  → "great"
  - **B**: no fill (default white)
  - **C**: no fill OR `#E7E3AB` (pale yellow-green) when emphasised
  - **D**: `#FFCC66` (amber)
  - **F**: `#FF7C80` (red)

**A&J bullet pattern:**
- All bullets prefixed " - " (em-dash style with leading space, NOT "•" or HTML <li>)
- First bullet (anchor) is **SemiBold/Bold** — verdict statement
- Subsequent bullets are **Regular** — evidence/elaboration
- This matches v3.1 two-shape rule (parent=verdict, sub=evidence) and Richard's locked R14 (parent ≤30w bold, sub regular)

**Grouping:**
- RA label (col C) shown ONCE at top of its CQ group (vertical merge style)
- Multiple CQs under one RA share the C-column space, repeating zebra fill
- Empty rows between RA groups create breathing room

## Mapping Sheet3 → New Taxonomy

Sheet3 actually shows **two different IC elements**, not just "input forces":
- Rows 6–8 (#1 Longevity / Three-year triple ratchet) → Element "Required financial outputs?", RA "#1 Longevity"
- Rows 11+ (#2 Growth) → Element "Required financial outputs?", RA "#2 Growth rate?"
- Rows 14+ (#3 Improvement) → Element "Required financial outputs?", RA "#3 Improving financials?"
- ... continues through #4, #5, #6, #7, #8 — all RAs of "Required financial outputs?"

→ **Sheet3 mockup uses the OUTPUTS element, not INPUTS.** The mockup gives me the visual STYLE; Richard's request is to apply that style to the INPUTS element (which has 2 RAs: Change forces? + Robust base?, 7 CQs total).

This is a key clarification candidate for the back-brief.

## What I have NOT yet done

- Read HTRO ESA memo for IC content corresponding to "Required input forces" (Change forces? + Robust base?). Old taxonomy maps IC#2 inputs ≈ "input forces" but exact CQ-level analysis text needs to be located.
- Read style guideline files (memo-view-formatting-principles, memo-signposting-principles, memo-header-design-system-v5).
- Researched broader UI best practices.

These will follow Richard's confirmation of the back-brief, so the work is scoped correctly before I invest effort.

## Anticompaction status

- This log saved before any authoring work begins.
- State.md will be updated after Richard confirms the back-brief.
- 15-minute floor will apply once execution starts (per C1/C2/C3).

---

## 29-Apr-26 — Round 2: Richard's reply

**Richard's answers:**
- "New taxonomy" = content structure guide. Sheet 3 = visual/style guide. Sheet 3's bullet count + sub-count + length are arbitrary placeholders.
- **Length style guide rules (locked v3.1) apply, increased by 50%** (i.e. 50% more bullet points and therefore 50% more word count).
- Q1 (test on OUTPUTS too): YES.
- Q2 (real-content fidelity): Lorem-Ipsum IS permitted where there is no relevant HTRO content (override of my proposal).
- Q3 (wrapping context): "can you explain" — Richard wants me to explain Q3 before answering.
- Asked: "Can you tell me the related length style guide information for bullets?"

**Locked length rules (R5, R14, family floors, stage-gated anchor count) — sourced from `databases/memo-view-formatting-principles.md` v3.1 + `memory/skills/memo-view-formatting/SKILL.md` v2.2:**

**Per-bullet length (R14 hard cap):**
- Parent bullet (depth 0): 15–25 words target, hard cap **30 words**.
- Sub-bullet (depth 1): 10–20 words target, hard cap **30 words**.
- No grandchild bullets — `sub[]` on a child is forbidden (R3).

**Per-parent child cap (R5 hard):**
- Each parent ≤ 6 sub-bullets (raised from 3 in v3.1; still inside Miller 7±2).
- Max words per parent anchor cluster = 25 + 6×20 = **145w**.

**Per-bullet_group cap (R4 hard):**
- 1–7 items per `bullet_group`. Target 3–6.

**Sub-section word budgets (locked v3.1):**

| Sub-section | Triaging | ESA | DD |
|---|---|---|---|
| C.II.1 Technical (P1) | 600w | 900w | 900w |
| C.II.2 Fundamental Case (P3+P4) | 2,100w | 4,250w | 7,000w |
| C.II.3 Fit for Paradigm (P2) | 600w | 900w | 1,200w |
| C.II.4 SS Momentum (P5) | 300w | 600w | 600w |
| C.II.5 Upside (P6) | 300w | 300w | 300w |
| **Total C.II** | **3,900w** | **6,950w** | **10,000w** |

Green band 0.85×–1.15× of target.

**Per-family floor (C.II.2 only, locked v3.1):**

| Family | Triaging | ESA | DD |
|---|---|---|---|
| IC#1 / IC#2 / IC#3 | 190w | 390w | 590w |
| BB#2 Foundation Quality | 380w | 780w | 1,180w |
| All other BBs | 95w | 195w | 295w |

**Stage-gated anchor count (flat sub-sections C.II.1/3/4/5):**
- Triaging: 3 anchors typical.
- ESA: 5 anchors typical.
- DD: 7 anchors typical.

**Sheet3 +50% application — Richard's instruction:**
- Bullet COUNT and word COUNT both bump 50%, NOT bullet LENGTH (R14 caps untouched).
- Mechanism: more parents and/or more sub-bullets per parent.
- Concrete: per-family ESA floor for IC#1/2/3 → 390w × 1.5 = **585w**. Per-family ESA floor for BB#2 → 780w × 1.5 = **1,170w**. Other BB ESA floor → 195w × 1.5 = **293w**. C.II.2 ESA total → 4,250 × 1.5 = **6,375w**. Other sub-sections scale equivalently: C.II.1 ESA 900 → 1,350w, C.II.3 ESA 900 → 1,350w, C.II.4 ESA 600 → 900w, C.II.5 ESA fixed 300 → 450w.
- ESA anchor count for flat sub-sections: 5 → ~7-8 anchors (still ≤ Miller 7±2 with R4 hard cap of 7 enforced — flag if conflict).

**R4 conflict flag:** R4 hard caps `bullet_group` at 7 items. If +50% pushes flat sub-sections from 5 to 8 anchors, that breaches R4. Need clarification — either (a) add more sub-bullets per parent rather than more parents, (b) split into multiple bullet_groups, or (c) raise R4 to 10 for this specimen only. **Will surface in next back-brief.**

## Q3 explanation (re Richard's "can you explain")

Q3 was: "Bare table only, or page-with-headers (HTRO ESA / Investment Case Elements / Required input forces?)?"

**Explanation:** Sheet3 in the workbook shows ONLY the body table — three columns (RA / CQ / A&J) with rows for each CQ. It doesn't show what wraps around the table. When I render this as an HTML page, I need to decide what extra page chrome to include:
- Option α — **bare**: just the table, nothing else. Cleanest test of the table style itself.
- Option β — **minimal context**: page title bar at top (e.g. "HTRO — ESA — Investment Case Elements — Required input forces"), then the table.
- Option γ — **full context**: ticker badge, stage indicator, conviction summary, breadcrumb (Pillar → Element → Section), then the table.

The choice matters because: (i) if we eventually promote this style into the dashboard, the dashboard already provides chrome — option α makes that promotion clean; (ii) if we want the standalone HTML to be readable on its own (e.g. you scroll to it on iPad and need to know what you're looking at), option β/γ is required.

My recommendation: **option β** — minimal title bar so the file makes sense out of context, but no heavy chrome that would conflict if we later embed in the dashboard.

---

## 29-Apr-26 — Round 3: Richard's answers

- **Q1 = C** → raise R4 from 7 → **10** for this specimen only. Specimen-local; not a system-wide change.
- **Q2 = B** → minimal title bar (option β).
- **Q3** = anchor + sub density is Watson's judgement, optimised for clarity per CQ row. Permission to vary within the specimen.
- **Q4** = single HTML file, both elements stacked.

## Locked execution plan

**File:** `databases/memo-style-sheet3-htro-inputs.html` (standalone, ~one page).

**Content scope:**
- Element 1: "Required input forces?" — 2 RAs, 7 CQs.
- Element 2: "Required financial outputs?" — 8 RAs, 12 CQs.
- Stacked vertically.

**A&J source for HTRO:**
- Pull from `databases/memos/HTRO/ESA.json` wherever a CQ has a clean match in old taxonomy IC#1/2/3 family blocks.
- Lorem-Ipsum where no HTRO content exists, marked with discreet `[placeholder]` chip in column F.

**Word budget per Richard's +50%:**
- IC family ESA floor 390w × 1.5 = ~585w per element-section.
- Element 1 (7 CQs) → ~80w/CQ average.
- Element 2 (12 CQs) → ~50w/CQ average.

**Rules in force for specimen:**
- R4 = 10 (specimen-local raise from 7).
- R14 = 30w hard cap (untouched).
- R5 = ≤ 6 subs/parent (untouched).
- R3 = no grandchildren (untouched).

**Visual style (Sheet 3, with extensions):**
- 4 columns: C (RA italic) / D (CQ bold #n) / E (rating chip) / F (A&J bullets).
- Aptos 10pt body, 11pt header.
- Header fill `#FDFCF1`. Zebra body fills `#FAF8D2` / `#FDFCF1` alternating per CQ group.
- RA label vertically merged across CQs of that RA (rowspan).
- Anchor bullet SemiBold; subs Regular. Em-dash " - " prefix.
- Rating chip fills: A green, B light blue, C `#E7E3AB`, D `#FFCC66`, F `#FF7C80`.

**Page chrome (β):**
- Top bar: "HTRO — ESA — Investment Case Elements" (Aptos 14pt Bold).
- Subtitle: "Sheet 3 visual style test, 29-Apr-26" (small grey).
- No toolbar, no badges, no controls.

**Verification:**
- Headless browser screenshot vs Sheet 3.
- R14, R5, R4=10 sweeps.
- Word count per element-section in [497w, 673w] (0.85×–1.15× of 585w).

## Round 4: HTRO content audit (29-Apr-26)

Read `databases/memos/HTRO/ESA.json` IC#1, IC#2, IC#3 family blocks. **Result: all 19 specimen CQs have real HTRO A&J content.**

**Mapping new-taxonomy → HTRO ESA memo content:**

Element 1 — Required input forces (7 CQs):
- Change forces? CQ1 (External tailwinds) → IC#2.CQ1 (DC demand, EU subsidies)
- Change forces? CQ2 (Internal change) → IC#2.CQ2 (CEO Fröberg, PIP, strategy)
- Robust base? CQ3 (No external headwinds) → IC#2.CQ3 (FS Chinese pricing, BEAD delays)
- Robust base? CQ4 (Well-invested base) → IC#2.CQ4 (20+ acquisitions, capex 2-3%)
- Robust base? CQ5 (Past/present congruency) → IC#2.CQ5 (acquisition→margin→diversification)
- Robust base? CQ6 (Large CfC/mispricing) → IC#2.CQ6 (FS+CEO, 4.3x vs 8-10x peers)
- Robust base? CQ7 (Low trading multiple) → IC#2.CQ7 (4.3x EV/EBITDA, 1.0x EV/Sales)

Element 2 — Required financial outputs (12 CQs):
- #1 Longevity → IC#1.CQ1 (triple ratchet, FY28 SEK 3.30-3.60)
- #2 Growth → IC#1.CQ2 (20-25% EPS CAGR, GARP)
- #3 Improvement → IC#1.CQ3 (margin trajectory, DC mix)
- #4 Setup fit → IC#1.CQ4 (DC Demand-Driven EPSU/EPT primary)
- #5 Timeliness → IC#1.CQ5 + CQ6 (post-CfC partial, 22M post-turn)
- #6 Monitorability → IC#1.CQ7 + CQ8 (segment reporting, hyperscaler capex)
- #7 Earnings upgrades → IC#1.CQ9 + CQ10 (consensus gap 32-44%, thin coverage)
- #8 Bankable multiple → IC#1.CQ11 + CQ12 (company vs exogenous, 80-120% TSR)

**No Lorem-Ipsum needed.** All real HTRO ESA-stage analysis. The +50% word budget will be sourced from the actual memo's bullet content (which is already richer than 390w/family — IC#1 alone is ~3,500w in the memo). Compression to ~585w/element will be the discipline, not expansion.

## Authoring approach

- Build a Python script `databases/scripts/build-style-sheet3-htro.py` that:
  1. Reads `databases/pillar-tree-canonical.json` for the new-taxonomy CQs.
  2. Reads `databases/memos/HTRO/ESA.json` for HTRO A&J text per CQ.
  3. Maps each new CQ to its HTRO ESA bullet via the mapping above.
  4. Compresses each bullet to anchor (~20w bold) + 1-4 subs (~15w each), target ~80w/CQ for input forces, ~50w/CQ for outputs.
  5. Emits self-contained HTML matching Sheet 3 visual style.

This keeps the data → render pipeline auditable. Re-runnable. No fabrication.

**Next concrete action (per UWB-1):** write the build script.

---

## Round 5: Build complete (29-Apr-26 ~20:13 UK)

**File shipped:** `databases/memo-style-sheet3-htro.html` (17,032 bytes)

**Mapping coverage:** 7/7 + 12/12 = 100%. Zero missing, zero extra.

**Word counts:** ELEM1 = 579w (target 585w; band 497-673w; PASS). ELEM2 = 544w (target 585w; band 497-673w; PASS). Total = 1,123w.

**Validation passed:** R14 (≤30w/bullet) all PASS. R5 (≤6 subs/parent) all PASS. R4=10 specimen-local (≤10 items/CQ-row) all PASS.

**Build script:** `databases/scripts/build-style-sheet3-htro.py` (rerunnable, idempotent — backs up existing HTML to `.bak-pre-rebuild-{ts}` before write).

**QA verification (LibreOffice → PDF → JPEG → Read):** 6 pages rendered. Confirmed working: 4-column layout, RA rowspan grouping, zebra fills (faint cream), anchor-bold + subs-regular, separator between elements. Confirmed limitation of LibreOffice rendering (NOT real-browser): rating chips render as bare letters (background-color stripped), italic on RA labels stripped. These will render correctly in Chrome/Edge/Safari on Richard's machine.

**Earlier issue cluster: file truncation.** Three separate file-truncation events occurred during this build (Edit/Write tool truncated the script tail at lines 433, 466, 477). Recovered each time via Python in-place patching. Root cause unknown — possibly a pathological interaction between Edit tool and the Aptos special characters / em-dashes in the bullet content. Mitigation: AST-parse-check after every Edit; Python-patch tail when it goes missing. Logged here for SA pattern-tracking.

**Not done:**
- Real-browser visual verification by Richard (Q3 standing rule discharged on my side via LibreOffice; only Richard can fully discharge it).
- Promotion to live dashboard tab. (Not requested. Standalone specimen only per Q4=stacked-single-file.)
- Push to GitHub. (Not requested.)

---

## 30-Apr-26 ~05:50 UK — Round 6: V2 SPECIMEN STRESS TEST (full new-taxonomy scope)

**Context:** Richard wants to expand the Sheet 3 specimen from the current 19-CQ HTRO subset to the **full new taxonomy** (70 RAs / 182 CQs across IC + BB pillars), with Lorem-Ipsum for non-HTRO entries, to stress-test how long a complete memo would be.

### Brief (verbatim, 30-Apr-26)

> Can you contain the attributes, questions and ratings to the left 1/3 of the page, and right 2/3 is for the analysis and judgement.
> What are relevant formatting guidelines for the MEMO in the RATINGS DASHBOARD that we can apply to the ANALYSIS and JUDGEMENT parts of this STYLE SHEET 3 test? Advise. Objective is to make key information stand out to me very clearly when skim reading.

> [After my recommendations]:
> Yes. try it.
> But do the [J], [A] etc. at end of bullet point as suffix.
> Ensure no "—" are used anywhere — include that in the formatting rules.
> Remove all "." from last sentences in any bullet point. Include that in formatting rules.
> Remove the "divider bar" between CQs within an RA.
> Include in the LHS "ToC" column every entry in the PILLAR TREE NEW TAXONOMY. Put the CASE ELEMENTS FIRST, then the BUILDING BLOCKs below. Use Lorem Ipsum for the analysis and judgement for these newly added entries. Aim here is to see how long the memo would be answering all the RAs and CQs.

### Confirmed via back-brief

- **1A** = scope: full 70 RAs / 182 CQs, both pillars, IC first then BB.
- **1B** = include element + group + pillar banner rows for visual hierarchy.
- **1C** = Lorem rows match existing HTRO row density (~80w each).
- **1D** = em-dashes replaced with `: ` (colon-space). New rule R20 added to locked principles.
- **1E** = strip ONLY the very last character of each bullet if `.`. Internal periods kept. R21 added.
- **1F** = IAJA `[J]/[A]/[I]` inline suffix at end of bullet, coloured (J=purple, A=blue, I=grey). Watson classifies HTRO content; cycles plausibly for Lorem.

### V2 Locked Execution Plan

**Files to touch:**
1. `databases/scripts/build-style-sheet3-htro.py` — major expansion:
   - Walk `databases/pillar-tree-canonical.json` to enumerate all 70 RAs + 182 CQs across both pillars.
   - For each RA/CQ, look up if HTRO has real ESA content (existing 19 CQs in IC#1 + IC#2 family blocks); if yes, use real content; if no, generate Lorem-Ipsum at ~80w density.
   - Add element + group + pillar banner rows to table structure.
   - Strip terminal `.` from every bullet (anchor + subs).
   - Replace `—` with `: ` everywhere.
   - Add `[J]/[A]/[I]` suffix to every bullet, coloured.
   - Add 10-20% underline (`<u>`) on anchor bullets — load-bearing words.
   - Column widths: RA 10% / CQ 17% / Rating 6% / A&J 67%.
   - Remove bottom border between CQ rows within same RA group (keep border between RA groups).

2. `databases/memo-style-sheet3-htro.html` — regenerated by the script.

3. `databases/memo-view-formatting-principles.md` — add new rules:
   - **R20 — No em-dashes (`—`) in any bullet text.** Use colon-space (`: `) for verdict→evidence joins.
   - **R21 — No trailing period at end of any bullet.** Strip last `.` if present. Internal periods kept. `?` and `!` untouched.

4. `memory/skills/memo-view-formatting/SKILL.md` — mirror R20 and R21 in the skill file's pre-flight checklist and validator coverage table.

**Validation:**
- Mapping: enumerate each pillar tree entry; assert every one has an A&J.
- R14 hard cap (≤30w/bullet) on every anchor and sub.
- R5 (≤6 subs/parent) on every CQ row.
- R20 — no `—` anywhere in rendered text.
- R21 — no bullet ends in `.`.

**Anti-compaction:**
- This log entry saved BEFORE authoring.
- State.md updated.
- Backup taken before file mutation.
- Save frequently during build (per C1/C2/C3 cadence rules).
- Push to GitHub Pages for live audit when done.

---

## 30-Apr-26 ~13:00 UK — Round 7+8: V3 SPECIMEN — DOCTRINE REFORM + SUMMARIES + NAV REFINEMENTS

**Brief Round 7 (formatting + nav refinements):**
- Right-align CQ column.
- Add ToC nav pane (left 1/4, sticky, internally scrollable).
- Tree-diagram nav: Pillar → Group (BB) → Element → RA (expand-on-focus).
- IntersectionObserver-driven focus (top-quarter trigger).
- Click any node → smooth-scroll main pane.
- RA-section metrics: word count, target, audit checks shown as small subtext.

**Brief Round 8 (length doctrine reform + content additions):**
- **Weight system** (half / normal / double) per item, propagating DOWN the taxonomy.
- **Triaging "normal" floor**: 3-5 bullets per CQ (1 anchor + 2-4 subs).
- **Stage scaling**: ESA = 3× Triaging length, DD = 5× Triaging.
- **Bullet COUNT scales** with the multiplier (not just word counts per bullet).
- **Authorial principle** "≥25% over floor": Watson should write more than floor in ≥25% of CQs when content is interesting. SOFT validator warning if breached.
- **Double-weight scope (entire elements/groups, inherited down):**
  1. Pillar 1 element "Required input forces?" (entire)
  2. Pillar 1 element "Required financial outputs?" + "Required financial outputs (line items)?" (both, entire)
  3. Pillar 2 G2 "Case simplicity" (entire group)
  4. Pillar 2 G3 "Business quality" (entire group)
  5. Pillar 2 G1 element "Case fit with current market paradigm's thematics?" (entire)
  6. Pillar 2 G4 element "Invalidating attributes" RA "Lessons check?" (RA-level)
  7. Pillar 2 G4 element "Invalidating attributes" RA "Negative earnings momentum?" (RA-level)
- **Formatting:** extra line break after last sub-bullet of last CQ in each RA; underline 10-30% on sub-bullets too.
- **Nav pills** (toggleable button, header right): show/hide small pill-shape badges in nav tree similar to pillar-tree-new-taxonomy diagram.
- **RA summary judgement** (only when RA has >1 CQ): bullets formatted bold + italic, no sub-bullets, count = max(4, ceil(1.5 × CQ count)). Layout = full-width row across CQ + R + A&J columns (option G).
- **Element summary judgement**: ≥8-10 bullets, ≥1 per RA, signposted with RA reference + RA's rating, single-line per bullet spanning columns 2-4 (CQ ref / Rating / bold-italic text).

**Doctrine reform scope:**
- `memo-view-formatting-principles.md` v3.1 → v3.2 with new §IV.F (weight system + per-CQ length), §IV.G (stage scaling 3×/5×), §IV.H (section-specific weight overrides). v3.1 §IV.B sub-section budgets + family floors marked DEPRECATED but preserved for rollback. v3.1 stage-gated-depth rule (Triaging=TC, ESA=+RA, DD=+CQ) SUPERSEDED — every CQ answered at every stage, length scales with stage.
- SKILL.md v2.3 → v2.4 mirrors §IV.F-H principles in pre-flight checklist + anti-patterns.

**Confirmed answers (8 questions):**
- 1A confirm: weight propagates DOWN.
- 1B Entire: case-fit = entire G2; outputs = both meta + line-items elements.
- 1C: # of bullets scales (not just word counts). Will adjust ratios if DD too long.
- 1D: yes — ≥25% over floor as authorial principle, SOFT validator warning.
- 1E: yes — supersede stage-gated-depth rule. Per-CQ floor scales 3×/5×.
- 1F option A: double-weight inherited to all RAs and CQs underneath named element/group.
- 1G: full-width row across "Core question", "R", "Analysis and judgement" columns (3 columns; col 1 RA label remains rowspanned). Spans col 2-4.
- 1H: single-line per bullet spanning col 2-4 — RA reference + rating + text inline.

**Authoring sequence:**
1. ✅ Pre-write backups + full backup folder + LATEST-FULL-BACKUP pointer.
2. ✅ Session log + state.md updated.
3. (Next) Update `memo-view-formatting-principles.md` to v3.2 with new §IV.F-H + DEPRECATED markers on superseded rules.
4. Mirror in SKILL.md (v2.4).
5. Update build script — weight tagging, summary blocks, formatting tweaks, nav pane, ToC, metric subtext, pill toggle.
6. Build, validate (R14, R5, R17, R20, R21 + new weight rules), push, audit live in Chrome.

**Anti-compaction status:**
- ✅ Pre-write backups: 4 files (.bak-pre-v3 / .bak-pre-v32).
- ✅ Full backup folder: `memory/session-handoffs/transcripts/2026-04-30-1100-FULL-BACKUP/` (7 files).
- ✅ LATEST-FULL-BACKUP pointer updated.
- ✅ Session log entry above (this entry).
- (Next) State.md update.
- During build: 15-min cadence saves per C1/C2/C3.

---

## 30-Apr-26 ~14:15 UK — Round 9: V5 — 10 visual + UX refinements

**Brief items (10):**
1. Rating pills next to nav items (all clickable: pillars + groups + elements + RAs).
2. Pills toggle ON by default (both nav + main pane).
3. Prefix pills in main pane (single letter E/RA/CQ matching nav).
4. RA summary text left-aligned + bold/non-bold per bullet (~30% bold for Lorem).
5. IAJA suffix on RA + element summary bullets (default [J] = judgement).
6. Sticky focused-element banner (CSS-only via position:sticky on element banner row).
7. Tree-diagram connector: indent RA col-1 by ~16px + L-shape (vertical + horizontal arm).
8. CQ column → 2/3 current width: 18 / 12 / 6 / 64.
9. Audit checks stacked vertically below RA band-and-weight line.
10. Element summary: 3 general bullets prepended (no RA-ref, no rating chip), no divider line.

**Confirmed answers:**
- 1A = (B) all clickable nav items get rating pills.
- 1B = pills ON by default, both panes.
- 1C = single-letter pills.
- 1F = CSS-only sticky element banner.
- 1G = options ii + iii combination.
- 1H = 18/12/6/64.
- 1I = vertical stack for audit checks.
- 1J = no divider line.

**Pre-write backups (.bak-pre-v5-20260430-141339):** memo-style-sheet3-htro.html, build-style-sheet3-htro.py.
**Full backup folder:** transcripts/2026-04-30-1345-FULL-BACKUP/.

---

## 30-Apr-26 ~15:20 UK — Round 11: V6 — multi-anchor fix (doctrine compliance restored)

### Bug found
V5 renderer was producing only 1 anchor + ≤6 subs per CQ regardless of stage×weight target. ESA × normal CQs were clipped at 7 bullets (target 9-15). ESA × double CQs were clipped at 7 bullets (target 18-30). Discovered when Richard observed that Case optionality / Nice to have attributes (normal weight, ESA stage) showed only 1 anchor + 6 subs, contradicting the 9-15 bullet target.

### Root cause
`lorem_row()` clamped subs to 6 to satisfy R5 (≤6 subs/parent) but never split overflow into additional parent anchor groups. The renderer then emitted a single anchor + clamped subs. Per locked principles §IV.F, bullet COUNT scales with stage × weight via MULTIPLE PARENT ANCHORS, not by bloating one anchor's subs.

### Fix shipped
1. Data structure: CQ record now carries `groups[]` list. Each group = `{anchor, anchor_iaja, subs}` with subs ≤6 per group (R5 satisfied per group, not per CQ row).
2. `lorem_row(weight, stage)`: computes total target bullets, splits across multiple anchor groups (1 anchor + ≤5 subs per group = ≤6 bullets per group).
3. `render_aj_cell()`: iterates groups, emits each anchor + its subs with `bullet-anchor-spacer` (6px gap) between groups.
4. `compute_ra_metrics()`: walks groups[] to count anchors/subs/breaches across all groups in CQ.
5. Back-compat: HTRO real content (single anchor+subs) wrapped as `[{anchor, subs}]` single-element groups list at render time. No HTRO data needed to change.

### Doctrine compliance verified
| Stage × Weight | Anchor groups | Total bullets | §IV.F target |
|---|---|---|---|
| Triaging × normal | 1 | 5 | 3-5 ✓ |
| Triaging × double | 2 | 9 | 6-10 ✓ |
| ESA × normal | 2 | 11 | 9-15 ✓ |
| ESA × double | 4 | 21 | 18-30 ✓ |
| DD × normal | 5 | 25 | 15-25 ✓ |
| DD × double | 9 | 49 | 30-50 ✓ |

### Live audit results in Chrome
- Title V6 ✓
- 665 anchors (was 182 in V5 = 1 per CQ; 665 = ~3.6 anchor groups per CQ avg)
- 2,891 sub-bullets (was ~1,000)
- 483 anchor-group spacers (visual gaps between groups within same CQ)
- 3,556 total A&J bullets (was ~1,200)
- 52 RAs in green target band; 18 in warn band — natural variance from random Lorem distribution

### File deltas
- HTML: 394 KB → 790 KB (~2× larger; reflects ~3× more bullets)
- Python script: 51,693 → 53,195 bytes (renderer changes only)

### Pre-write backups
- `databases/memo-style-sheet3-htro.html.bak-pre-v6-20260430-150905`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v6-20260430-150905`

### Full backup folder
`memory/session-handoffs/transcripts/2026-04-30-1520-FULL-BACKUP/` (7 files)

### Pattern flagged
Edit-tool truncation struck once during V6 build (line 1111 mid-`final_parts` list). Recovered via Python tail rewrite. Total ~8 truncation events this session — pattern formally needs codifying in feedback memory next session.

---

## 30-Apr-26 ~17:10 UK — Round 12: V10 — 6 changes (doctrine + group summary + line-items placeholder + BQ strips)

### Brief items
1. Strip bullets from "Required financial outputs (line items)?" element — render as banner + placeholder row only.
2. Doctrine: "Fit with acceptable case setups?" goes from double to normal weight. Implementation: drop Case simplicity group double + add Required simplicity guardrails element double (only).
3. Doctrine: DD multiplier 5× → 3.75× (= ESA × 1.25). Update §IV.G + §IV.F formula reference + SKILL.md.
4. Add group summary block to each multi-element BB group. Multi-column layout: leftmost = 3 general bullets; one column per element with ≥4 bullets per element column (each linked to an RA + rating + IAJA suffix). Skip when group has only 1 element.
5. Strip `\s*\("[^"]*"\)` parenthetical from RA labels in Advantaged business element only.
6. Strip "Business quality - " prefix from BQ element titles + title-case first letter. Apply to both main-pane banners AND nav-pane entries.

### Confirmed answers (8 questions)
- 1A correct: line-items renders as banner + placeholder only
- 1B correct: drop Case simplicity group double; add Required simplicity guardrails element double (simpler than explicit-normal-override mechanism)
- 1C yes: STAGE_MULTIPLIER DD = 3.75
- 1D yes: group summary multi-column layout per spec (general column 22% + element columns split rest)
- 1E agree: parenthetical strip on Advantaged business RAs only
- 1F agree: BQ prefix strip + title-case
- 1G agree: render-time strip in build script only (canonical taxonomy unchanged)
- 1H yes: update locked principles + SKILL.md

### Doctrine updates
- `databases/memo-view-formatting-principles.md` v3.4 → v3.5: §IV.G stage table updated (DD = 3.75); §IV.F formula updated; §IV.H entry #4 narrowed; example math updated (was 30-50 bullets at DD double; now 23-38).
- `memory/skills/memo-view-formatting/SKILL.md` v2.4 → v2.5: version header + governing-document reference + pre-flight #20 stage scaling text.

### Output deltas
- HTML: 847KB → 758KB (smaller by ~89KB because 7 line-items RA rows + their CQ rows removed)
- 70 RAs → 63 RAs (−7 line items)
- 182 CQs → 175 CQs (−7 line items)
- Group summary rows: 0 → 4 (G1 Momentum, G2 Case fit, G3 Business quality with 6 element columns, G4 Riskiness)
- Line items placeholder rows: 0 → 1
- "Business quality - " strings remaining: 0 ✓
- Advantaged business parentheticals remaining in RA labels: 0 ✓

### Live audit confirms
- Title V10 ✓
- 4 group-summary-row instances + 1 line-items-placeholder ✓
- BQ first element banner reads "Great operator" + double weight badge ✓
- Advantaged business first RA reads "Strong operational/competitive advantages? [MOAT]?" ✓
- "Fit with acceptable case setups?" element shows NO double weight badge (normal_OK) ✓

### Pattern flagged
Edit-tool truncation hit again during V10 build (line 1252 mid-`if len(attrs)`). Recovered via Python tail rewrite. Total ~13 truncation events this session.

### Pre-write backups
- databases/memo-style-sheet3-htro.html.bak-pre-v10-20260430-164320
- databases/scripts/build-style-sheet3-htro.py.bak-pre-v10-20260430-164320
- databases/memo-view-formatting-principles.md.bak-pre-v10-20260430-164320
- memory/skills/memo-view-formatting/SKILL.md.bak-pre-v10-20260430-164320

### Full backup folder
`memory/session-handoffs/transcripts/2026-04-30-1700-FULL-BACKUP/` (7 files)
