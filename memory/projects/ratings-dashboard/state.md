# Ratings Dashboard — Live State
<!-- [W] Updated 6-May-26 ~PM UK — SOP v2.1 (pre-mortem fixes) + validator v2.1 (multi-source + bracket exclusion). Ready for Sonnet re-testing. -->

## 6-May-26 — SOP v2.1 (PRE-MORTEM FIXES) + VALIDATOR v2.1

**Objective:** Define and apply a consistent formatting standard for all ~346 researcher memos to enable skim reading with proper hierarchy, emphasis, and structure.

**Status:** SOP v2.1 WRITTEN + VALIDATOR v2.1 UPDATED. Pre-mortem identified 7 issues (5 fixed, 1 noted, 1 fixed in validator). Awaiting Sonnet re-test. See `sop-premortem-v2.1-06-may-26.md` for full history.

---

### CURRENT STATE

**Rollout standard:** SOP v2.1 — FORMATTING ONLY (not content restructure). Self-contained SOP at `memory/skills/researcher/updating-old-research-memos-SOP.md`. Does NOT reference the old v1.1 spec (which caused contradictions).

**Cardinal Rules:** (1) Do not reword — use source's exact words, (2) Do not drop content — 90% word floor, (3) Do not change analytical temperature — preserve verdicts/ratings/qualifiers.

**Key changes (v1.0→v2.0→v2.1):** Removed IAJA tags, sub-bullet hierarchy, dimension splitting, judgement surfacing, J→A→I ordering, source attribution. Added splitting rule (>2 sentences AND >25 words → split recursively). Flat bullet structure only. BLUF/Key Findings is only additive content. v2.1 added: merge [AS]+[C] sources into single memo (include all, tag each bullet, don't synthesise), multi-source validator, bracket-tag word count exclusion.

**v1.0 SOP test results (FAILED — 7 memos tested by Richard in Sonnet):**

| Memo | Word ratio | Verdict |
|------|------------|---------|
| AUTO-01-BD | 21.6% | CATASTROPHIC content loss + rewording |
| AUTO-02-CF | 15.9% | CATASTROPHIC content loss + rewording |
| AUTO-03-TM | 21.8% | CATASTROPHIC content loss + rewording |
| BRAV-02-CF | 107% | OK ratio, v1.1 highlight style |
| BRAV-06-SS | 36% | FAILING, content loss |
| BRAV-07-KD | 116% | OK ratio, v1.2 highlight style |
| BRAV-09-EH | 122% | OK ratio, metadata wrong (Q5 Triaging → Q9 ESA) |

**Root cause:** SOP v1.0 gave Sonnet editorial licence ("restructure", "surface judgements", "dimension splitting"). Sonnet treated 35% floor as a target. Content systematically reworded with judgements neutralised, verdicts dropped, analytical temperature cooled.

**Previously deployed memos (pre-SOP, still live on GitHub):**

| Memo | Version | Word ratio | Status |
|------|---------|------------|--------|
| DCC-02-CF | v1.1 | 49.8% | DEPLOYED |
| AENA-01-BD | v1.1 | 71.1% | DEPLOYED |
| CARLB-05-ED | v1.1 | 50.9% | DEPLOYED |
| DCC-06-SS | v1.0 | — | DEPLOYED |
| HFG-07-KD | v1.0 | — | DEPLOYED |
| AUTO-05-ED | v1.0 | — | DEPLOYED |

**Remaining:** ~340 memos need v2.1 formatting. Source files in `Files/{TICKER}/{STAGE}/{NN-CODE}/`.

---

### DELIVERABLES THIS SESSION

**1. SOP v2.1:** `memory/skills/researcher/updating-old-research-memos-SOP.md`
- Role: RESEARCHER
- Model: Sonnet (recommended) or Opus
- 6-step pipeline: Load & Count → Plan Sections → Format as HTML → Wrap → VALIDATION GATE → Deploy
- Cardinal Rules: do not reword, do not drop content (90% floor), do not change analytical temperature
- Splitting rule: >2 sentences AND >25 words → split recursively into separate bullets
- Flat bullet structure only (no sub-bullets, no nesting)
- 13-rule formatting checklist (F1-F13) with CSS class reference
- 3 prior failure lessons baked in (content loss + rewording, falling off, FUSE truncation)
- Merge rule: when both [AS] and [C] sources exist, merge into single memo (longer source = section backbone, tag each bullet, don't synthesise/de-duplicate)
- Batch workflow guidance (3-5 memos per session, single git push)

**2. Validator script v2.1:** `databases/scripts/validate-memo.py`
- 11 checks: 5 hard gates (word ratio >= 90%, H2 count >= 3, signpost consistency, sub-bullet nesting = 0, em-dashes = 0, structure sanity) + 6 warnings
- Multi-source: accepts multiple source.md files, sums word counts for merged memos
- Bracket-tag exclusion: [AS], [C], [AS+C] stripped from output before word counting
- Prints single-line PASS/FAIL summary with all metrics
- Returns exit code 1 on hard failure, 0 on pass/warn

**3. Harvey ball logic documented:** The `lcGlyphForState()` function maps state 1-5 to harvey ball glyphs. Clickability is independent — driven by `covMemoManifest` lookup in `lcCellHref()`. A cell can show ◕ (Submitted) but be clickable if a memo file exists in the manifest.

---

### RELATIONSHIP TO OTHER PROJECTS

**SA - Dashboard Memo Read Layer (DMRL):** PAUSED, NOT DEPRECATED. DMRL owns the *dashboard infrastructure* — the Research Stages tab UI, lifecycle data pipeline, Harvey balls, cell rendering, patcher. The memo formatting SOP owns the *content* — taking raw markdown and producing spec-compliant HTML. They are sibling workstreams:
- DMRL = the container (dashboard UI that houses memos)
- Memo SOP = the content (structured HTML memos that go inside the container)
- DMRL is paused at Phase R3-v2 (rebuild after quality failure, 04-May-26)
- Memo formatting is active under RATINGS DASHBOARD project

**Ratings Dashboard project** (`memory/projects/ratings-dashboard/`) is the parent project that encompasses both the dashboard itself and the memo formatting work. The formatting spec, SOP, and validator all live under this project.

---

### KEY FILES

| File | Purpose | Status |
|------|---------|--------|
| `memory/skills/researcher/updating-old-research-memos-SOP.md` | 6-step formatting SOP for Sonnet | **LIVE** v2.1 (6-May-26) |
| `memory/projects/ratings-dashboard/sop-premortem-v2.1-06-may-26.md` | Pre-mortem findings, version history, design decisions | **Reference** |
| `memory/projects/ratings-dashboard/researcher-memo-formatting-spec.md` | Old formatting spec (v1.1 + v1.2 parked) | **SUPERSEDED** by SOP v2.1 |
| `databases/scripts/validate-memo.py` | Validation gate script (multi-source, bracket exclusion) | **LIVE** v2.1 (6-May-26) |
| `databases/scripts/wrap-memo-html.py` | Wrapper: body HTML → full document | **LIVE** |
| `databases/scripts/v12-formatting-pass.py` | v1.2 mechanical pass (PARKED with v1.2) | PARKED |
| `databases/memos/memo-style-v2.css` | Shared stylesheet | DEPLOYED to GitHub |
| `databases/memos/*-v11-body.html` | v1.1 body HTML intermediates (3 files) | Archive |
| `databases/memos/*-v11.html` | v1.1 wrapped memos (3 files) | DEPLOYED to GitHub |

### GITHUB STATE

- Repo: `vfhqi/dashboards` (PAT in `.secrets/github-pat.txt`)
- Live URL: `https://vfhqi.github.io/dashboards/memos/`
- Latest memo commit: `9fb0304` (v1.2 files — defective content but harmless alongside v1.1)
- v1.1 commit: `7eac14e`
- 28 memo HTML files in `databases/memos/` locally (mix of v1.0, v1.1, v1.2, body files, previews)

---

### NEXT STEPS

1. **Richard re-tests SOP v2.1 in Sonnet** — testing AUTO Q1 BD + Q2 CF (includes merge test for CF which has both [AS] and [C]) and AIXTRON Q1 BD + Q2 CF
2. **Iterate SOP v2.1 if needed** — based on re-test results
3. **Begin batch rollout** — 3-5 memos per Sonnet session, ~15-20 sessions for full ~340 memo coverage
4. **DMRL resume (separate)** — when Richard is ready to resume the dashboard UI rebuild (Phase R3-v2)

**SOP location:** `memory/skills/researcher/updating-old-research-memos-SOP.md` (v2.1, self-contained)

### Journey So Far (Condensed)

| Date/Time | Milestone |
|-----------|-----------|
| 05-May ~22:45 | Spec v1.0 written + agreed (14 rules). 6 test memos selected |
| 05-May ~23:30 | First 6 test renders complete (format-only pass — too mechanical, lost content) |
| 05-May ~00:30 | Second 6 renders (LLM full restructure from source). All pass programmatic QC |
| 05-May ~01:00 | Em-dash cleanup (67 found in CARLB alone). CSS path fix. Deployed to GitHub |
| 05-May ~02:00 | Chrome visual audit + programmatic QC audit passed. Presented to Richard |
| 05-May ~03:00 | Richard's v1.1 feedback: (A) MORE CLARITY — split compound bullets by dimension, add sub-bullet signposts; (B) MORE JUDGEMENTS — surface buried judgements from source |
| 05-May ~04:00 | Spec updated to v1.1 (Rules 13 + 14 added). DCC CF fully re-rendered from source with v1.1 |
| 05-May ~05:00 | AENA BD + CARLB ED amended with targeted v1.1 edits (NOT full re-renders — caused "falling off" problem) |
| 05-May ~15:30 | All 3 v1.1 memos wrapped + deployed to GitHub. Comparison links presented |
| 05-May ~16:00 | **Richard's v1.2 feedback received (see below)** |
| 05-May ~20:00 | SOP v1.0 written for Sonnet execution. Validator script built + tested against 3 v1.1 memos |
| 05-May ~21:30 | Comprehensive project save. Richard starts Sonnet testing |
| 06-May ~AM | Richard reports v1.0 SOP test failures (7 memos). Audit confirms catastrophic content loss + rewording |
| 06-May ~AM | Root cause diagnosed: SOP gave too much editorial licence. Richard instructs scope reduction to formatting only |
| 06-May ~AM | SOP v2.0 written: Cardinal Rules, 90% floor, flat bullets, splitting rule, no IAJA/sub-bullets |
| 06-May ~AM | Validator v2.0 updated to match (90% floor, IAJA removed, sub-bullet nesting = hard fail) |
| 06-May ~PM | SOP v2.0 comparison widget built (before/after). Cross-references added to SKILL-V2 |
| 06-May ~PM | Sonnet test of v2.0 identifies merge issue ("Do NOT merge sources" contradicts intent). Richard clarifies: merge both [AS]+[C], include all content |
| 06-May ~PM | Pre-mortem identifies 7 issues. 5 fixed in SOP v2.1, 1 noted (context window), 1 fixed in validator (bracket exclusion) |
| 06-May ~PM | SOP v2.1 + Validator v2.1 shipped. Backup saved. Pre-mortem documented. Richard re-testing in Sonnet |

### Richard's v1.2 Feedback (4 Issues)

**Issue 1: "Falling off" — inconsistent quality in second half of AENA and CARLB**
- Cause: Watson applied targeted edits to v1.0 base rather than full re-renders. Second half stayed at v1.0 quality.
- Fix: All future renders must be FULL END-TO-END re-renders from source. No partial patching.

**Issue 2: Insufficient sub-bullet splitting**
- Example (CARLB): `Western Europe: +1.2% reported (+2.4% ex-San Miguel); Nordic weather tailwind non-recurring; Britvic soft drinks mid-single-digit growth in UK/Ireland` — should be parent bullet + 2 sub-bullets (Nordics: / UK:)
- Example (CARLB): `India: Continued positive momentum with ~20% market share and distribution expansion; medium-term IPO narrative...` — should be parent + 3 sub-bullets (Market share: / Strategic priority: / IPO:)
- Pattern: When a parent bullet contains semicolons or commas separating distinct analytical points, SPLIT into sub-bullets with contextual signpost labels
- Question outstanding: Can Watson infer contextual signpost labels (geographic, thematic) not explicit in source? Richard's examples suggest YES

**Issue 3: Highlight granularity**
- Current: Whole-bullet background highlighting (entire `<li>` gets green/yellow/red background)
- Requested: INLINE phrase-level highlighting — highlight specific words/phrases WITHIN bullets, not the entire bullet
- This is a CSS + rendering change: use `<span class="m-hl-green">key phrase</span>` within bullet text rather than class on the `<li>` element
- Density question outstanding: Keep 30%+ target or reduce given more granular application?

**Issue 4: Signpost bolding inconsistency**
- Signpost labels (demi-bold prefix like "Revenue model:") present in first half of memos but missing in second half
- Same root cause as Issue 1 — the targeted-edit approach only fixed the first half

### Spec Amendments Needed for v1.2

1. **Rule 13 STRENGTHENED:** More aggressive splitting. If a parent bullet contains semicolons/commas separating distinct facts about different sub-topics (geographic regions, time periods, different metrics), ALWAYS split into sub-bullets with inferred signpost labels
2. **Rule 4 (Emphasis) CHANGED:** Highlights apply at PHRASE level within bullets (`<span class="m-hl-green">phrase</span>`), NOT at whole-bullet level. Same colour system (green/yellow/red). Target density TBD (30% or 15-25%)
3. **Rendering method LOCKED:** Always full re-render from source. Never patch v1.0 base.
4. **Signpost labels MANDATORY throughout** — not just where Watson notices them. Every parent bullet MUST have a signpost label. Sub-bullets get signpost labels when they address different dimensions.

### Next Steps

1. Update spec to v1.2 incorporating the 4 amendments above
2. Update CSS (`memo-style-v2.css`) to support inline phrase highlighting
3. Full re-render all 3 test memos from source with v1.2 rules
4. Deploy + present comparison links
5. Richard reviews → approve or iterate

### Live Files

| File | Purpose | Status |
|------|---------|--------|
| `databases/memos/AENA-01-BD.html` | v1.0 test memo | Deployed |
| `databases/memos/DCC-02-CF.html` | v1.0 test memo | Deployed |
| `databases/memos/CARLB-05-ED.html` | v1.0 test memo | Deployed |
| `databases/memos/AENA-01-BD-v11.html` | v1.1 test memo | Deployed |
| `databases/memos/DCC-02-CF-v11.html` | v1.1 test memo | Deployed |
| `databases/memos/CARLB-05-ED-v11.html` | v1.1 test memo | Deployed |
| `databases/memos/memo-style-v2.css` | Shared stylesheet | Deployed (needs v1.2 update for inline highlights) |
| `databases/scripts/wrap-memo-html.py` | Wrapper script | Working (CSS path sed fix needed after every run) |
| `memory/projects/ratings-dashboard/researcher-memo-formatting-spec.md` | Formatting spec SSoT | v1.1 (needs v1.2 update) |

### Technical Notes

- **GitHub deploy:** Clone via PAT in `.secrets/github-pat.txt`, commit, push. URL: `https://vfhqi.github.io/dashboards/memos/`
- **wrap-memo-html.py:** Requires absolute paths. Generates `href="../memo-style-v2.css"` which must be fixed to `href="memo-style-v2.css"` via sed after every run
- **FUSE truncation risk:** Files >28KB may truncate on COWORK mount. Write to `/sessions/*/mnt/outputs/` first if needed, then copy
- **Source files:** `Files/{TICKER}/{STAGE}/{NN-CODE}/` — markdown with highlight tokens
- **v1.0 memos deployed at:** `https://vfhqi.github.io/dashboards/memos/{TICKER}-{NN}-{CODE}.html`
- **v1.1 memos deployed at:** same path with `-v11` suffix

### Agreed Guidelines (14 rules)

1. **IAJA suffix tags** — `#J`/`#A`/`#I` on every parent bullet
2. **J→A→I ordering** — Judgements first within each section
3. **BLUF / Key Findings** — 5–10 bullet summary at memo top
4. **Section-level italic summary** — One italic sentence under each H2
5. **Bold key terms** — First occurrence of key terms/names/figures bolded
6. **Header hierarchy** — H1 title, H2 major sections (descriptive), H3 sub-sections, no H4+
7. **Horizontal rules between H2s** — INCLUDED AS TEST (Richard to confirm)
8. **Bullet structure** — Parent = headline/verdict (≤30w), sub-bullets = evidence/data
9. **Max 6 sub-bullets per parent**
10. **No grandchildren** — 2 nesting levels max
11. **Source attribution** — `[AS-Broker]`/`[C]` prefixes — INCLUDED AS TEST (Richard to confirm density)
12. **Signposting** — Demi-bold prefix labels on parent bullets (e.g. "Revenue model:", "Demand drivers:")
13. **QC footer** — Source, stage, date, words, ticker
14. **Communication principles** — Peer/base-rate context, A–F grades, ❌ D/F callout, 🚩 RARE outliers. CONTENT-LEVEL (not just formatting) — applies where source data supports it; gaps flagged for future enrichment pass.

**Additional rules ported from APM:**
- ≤30w bullet cap (HARD)
- Underline 10–30% of parent bullet text
- No em-dashes
- No trailing periods
- 30%+ highlight density (already in RESEARCHER SOP)

### Test Plan — Phase 1 (6 memos)

| # | Ticker | File | Query | Stage | Words | Rationale |
|---|--------|------|-------|-------|-------|-----------|
| 1 | AENA | ig-01-business-description.html | BD | IG | 4,164 | Worst wall-of-text, AS source |
| 2 | DCC | ig-02-change-forces.html | CF | IG | 3,172 | Different query type, mid-length |
| 3 | DCC | triaging-06-sell-side-commentary.html | SS | Triaging | 1,385 | Short memo, tests spec at low word count |
| 4 | HFG | triaging-07-key-drivers.html | KD | Triaging | 3,841 | Claude source, has KEY FINDINGS already |
| 5 | AUTO | triaging-05-earnings-delivery.html | ED | Triaging | 5,708 | Longest, stress-tests bullet cap + nesting |
| 6 | CARLB | triaging-05-earnings-delivery-ltm.html | ED | Triaging | 3,430 | Active pipeline stock |

**Test process:** Re-render each → deploy to GitHub → Richard reviews in browser → adjust spec if needed.

### Rollout Plan (after test approval)

| Phase | Scope | Purpose |
|-------|-------|---------|
| Phase 1 | 6 memos (above) | Spec validation |
| Phase 2 | Next 25 stocks (~75 memos) | Scale test, catch edge cases |
| Phase 3 | Next 50 stocks (~150 memos) | Broader QC |
| Phase 4 | Remainder (~120 memos) | Complete rollout |

Each sub-phase: render → deploy → Richard QC spot-check → proceed.

**Script:** `reformat-researcher-memos.py` (to be built). Reads source markdown, applies all 14 rules + emphasis/structure rules, validates constraints, outputs HTML with updated `memo-style.css`. Validation checks: ≤30w bullets, 2-level nesting, ≤6 sub-bullets, no em-dashes, no trailing periods, underline 10–30%, highlight ≥30%.

**Important:** Communication principles (#14) require content-level re-analysis, not just reformatting. Script applies structural rules to existing content. Peer/base-rate and A–F grades applied only where source data already contains the relevant comparisons. Gaps flagged in a report for future enrichment.

---

## 5-May-26 ~21:30 UK — MEMO FORMATTING + COVERAGE FIX (deployed, verified)

**Objective:** Fix two problems with memo links: (A) formatting variance (some memos render as unreadable walls of text), (B) coverage gap (165 cells with content but no rendered memo).

**Root cause:**
- (A) All 184 v0.1 memo HTML files were bare `<article>` fragments — no DOCTYPE, no stylesheet, no CSS at all
- (B) `covMemoManifest` only had 220 entries; 165 cells had source markdown in `Files/` but no rendered HTML

**Implementation — 4 scripts + shared CSS:**
1. **memo-style.css** (NEW, 282 lines): Shared stylesheet for all researcher memo pages. Body layout, headings, highlights (green/yellow/red), source/stage badges, QC footer, responsive+print.
2. **patch-memo-stylesheet.py** (NEW): Wrapped 178 bare v0.1 fragments in proper document structure with stylesheet link. 31 V20 files skipped (self-contained with embedded CSS/JS).
3. **batch-render-missing-memos.py** (NEW): Rendered 165 new memos from source markdown in `Files/`. Handles highlight token conversion, markdown→HTML with `m-*` classes. Manifest expanded 220→385.
4. **deploy-via-github-api.py** (NEW): API-based deploy script (no git CLI needed).

**Deployed:** Commit `44be34a` pushed via PAT from `.secrets/github-pat.txt`. 393 files changed. GitHub Pages live.

**Verified end-to-end in Chrome:**
- ATS Q2 (was wall of text → now formatted with highlights and spacing)
- AENA Q1 (was unclickable → now opens rendered memo)
- Dashboard click-through → memo in new tab confirmed working

**Three generations of memo HTML now coexist:**
1. **v0.1 patched** (184 files) — researcher outputs from `render_memo_to_html.py`, now wrapped with shared CSS link. Flat paragraphs with highlights. Example: AUTO Sell Side Commentary.
2. **Batch-rendered** (165 files) — researcher outputs from `batch-render-missing-memos.py`, built from source markdown in `Files/`. Simple metadata header + paragraphs. Example: AENA Business Description.
3. **V20** (31 files) — APM memo doctrine renders from `build-rendered-memo.py`. Full pillar structure, CQ/RA tables, navigation panel, embedded CSS/JS. Example: HTRO Triaging.

v0.1 and batch-rendered are **researcher memos** — they don't need pillar trees or CQ/RA mappings. V20 is the **APM memo** standard. These are fundamentally different document types serving different purposes. No rendering standard has been defined yet for what "good" researcher memo formatting looks like beyond readable/highlighted/accessible.

**Coverage:** 385/398 cells clickable (96.7%). Remaining 13 genuinely have no source data.

**Dashboard file:** `databases/ic-ratings-dashboard-v2.html` — 5,379,224 bytes.

---

## 5-May-26 ~20:15 UK — MEMO LINKS FIX (deployed to test, verified)

**Objective:** Fix research cell links that were returning 404 errors. Make cells clickable to open the actual rendered memo in a new window.

**Root cause:** Two issues:
1. Wrong repo name in URL (`master-dashboard` → should be `dashboards`)
2. Wrong URL pattern (GitHub tree view → should be GitHub Pages rendered HTML)

**Implementation — Python patcher (patch-memo-links.py):**
1. **Manifest injection:** Embedded `covMemoManifest` (220 entries across 53 tickers) as a JS object. Maps `TICKER/qnum` → actual filename (e.g. `"AENA/2":"ig-02-fundamental-change-forces.html"`)
2. **lcCellHref() rewrite:** Extracts ticker from `qd.folder.split("/")[0]`, qnum from `qd.folder.split("/")[2]` (parses leading digits from segment like `"02-CF"` → 2). Looks up manifest → constructs `https://vfhqi.github.io/dashboards/memos/TICKER/filename.html`. Falls back to Notion link if no manifest entry.
3. **Popover link fix:** Same manifest lookup using `qNum` parameter (already numeric from call site).

**Result — verified on deployed test URL:**
- 203 total cell links: 187 memo (GitHub Pages), 16 Notion fallback, 0 broken
- End-to-end test: AENA Q2 cell → memo page loads with full rendered content
- All broken `master-dashboard` URLs eliminated
- Notion fallback works for queries without rendered memos

**Manifest organisation system for going forward:**
- Rendered memos live at `memos/{TICKER}/` in the dashboards repo
- Naming: `{stage}-{qnum}-{query-name-slug}.html` (some legacy tickers use consolidated files)
- Manifest embedded as `covMemoManifest` in dashboard JS — update when new memos are built
- `build-rendered-memo.py` generates `{Stage}.html` per memo; filename convention varies by ticker

**Current file state:**
- `databases/ic-ratings-dashboard-v2.html`: 5,362,621 bytes
- Deployed to test/ — GitHub commit `4e8df5a`
- Test URL: `https://vfhqi.github.io/dashboards/test/ic-ratings-dashboard-v2.html?v=memofix1`

---

## 5-May-26 ~18:30 UK — FLEX COLUMNS (deployed to test, Richard signed off)

**Objective:** Eliminate horizontal scrolling on RS tab across all screen sizes. Dynamic column sizing so everything fits in one screen.

**Implementation — 2 patches applied via Python atomic-write scripts:**

### Patch 1: table-layout fixed + percentage CSS (patch-flex-columns.py)
16 CSS changes converting all fixed px width constraints to flexible percentages:
1. Lifecycle `.cov-table`: `width:max-content; min-width:100%` → `width:100%`
2. Base `.cov-table`: `table-layout:auto` → `table-layout:fixed`
3. Ticker column: 120px fixed → 8% flex + `white-space:normal; word-wrap:break-word; overflow-wrap:break-word`
4. Ind/Sec column: 100px fixed → 6% flex (column is display:none per pre-existing CSS)
5. Stage column: 48px fixed → 3% flex
6. Audit cells: 48px fixed → 2% flex
7. Memo cells: 32px fixed → 1.8% flex
8. Action column: 132px fixed → 9% flex
9. Pillar ratings: 28px fixed → 1.8% flex
10. Base query cells: 42-58px → 1.8% flex
11. Base audit cells: 26-30px → 2% flex
12. Base ticker: 110-160px → 8% flex with wrapping
13. Base ind/sec: 90-120px → 6% flex
14. Query header row 3: 42-58px constraints removed
15. Priority column nth-child(4): both lifecycle (36px) and base (48px) → 1.8% flex
16. Base th/td: added box-sizing:border-box

### Patch 2: colgroup injection (patch-colgroup.py)
- 42 `<col>` elements injected via `<colgroup>` into `covRender()` table creation
- Percentages: Company 7%, IndSec 5.5%, Stage 2.8%, 23 query cols 2.05% each, 5 audit ✓ 1.5% each, 3 memo 1.8% each, SOP 5%, 6 pillar 1.5% each, Action 8%
- Total ~97.35% — leaves ~2.65% for border/padding flex

**Result — JS-verified on deployed test URL:**
- `hasHScroll: false`, `overflow: 0`, `tableWidth == wrapWidth == 1858px`
- Company names wrap correctly ("BEmiconductor Industries" wraps over 2 lines)
- All 42 columns visible on screen without scrolling
- Colour bands, checkmarks, dates, audit scores all render correctly

**Known trade-offs (inherent in 42 columns on one screen):**
- Master header text truncates on narrow groups: "ANALYSIS / JU..." (3 cols = 90px), "Q..." for QUALITY CONTROL (1 col = 32px)
- Query column headers are narrow (~36px) — Q-number + description wraps tightly
- Stage column renders at 97px (wider than needed — could tune)

**Current file state:**
- `databases/ic-ratings-dashboard-v2.html`: 5,352,594 bytes, MD5: 92a1c21af661ecf0ba595d1768fcf198
- Ends `</html>` ✓, colgroup present with 42 cols ✓
- Deployed to test/ — GitHub commit `90d63d4`, deployment #156 green
- Test URL: `https://vfhqi.github.io/dashboards/test/ic-ratings-dashboard-v2.html?v=flex4`

**Next steps:**
1. Richard sign-off on flex column layout
2. Optional: tune percentage allocations if header truncation is unacceptable
3. Promote to live root

---

## 5-May-26 ~16:30 UK — RS TAB FORMATTING (8 changes + 3 tweaks, deployed to test)

**Objective:** 8 formatting changes to RESEARCH STAGES tab per Richard's request, plus 3 follow-up column width/wrap tweaks.

**Changes applied (all within COVERAGE_JS_V1 fence + CSS):**
1. **Remove horizontal scrolling** — `.container { max-width: none }` + `.cov-table { width:100%; table-layout:auto }`
2. **Full browser width** — uses existing margin space
3. **Remove PRIORITY column** — header removed from `covMasterRow()`, data cell removed from `covDataRow()`
4. **Larger COMPANY/ticker column** — min-width:110px, max-width:160px, width:130px; truncation raised 16→28 chars
5. **Rename INFORMATION RESEARCH → RESEARCH** — in `covMasterRow()` colspan 28
6. **AUDIT → own group QUALITY CONTROL** — new `<th colspan='1'>QUALITY CONTROL</th>`, A&J colspan reduced 4→3
7. **Rename FCS RATINGS → SIX MASTER RATINGS** — in `covMasterRow()`
8. **Column group colour bands (MM 99 style)** — rgba tints at header + data cell level via data-grp attributes
9. **Narrow audit column** — matched to query cell width (48px)
10. **Double company column** — 60px → 120px
11. **Action column 50% larger + text wrap** — 88px → 132px with white-space:normal

**data-grp implementation:**
- Query cells: dynamic `_grp` from q index (0-2=ig, 3-6=tri, 7-13=esa, 14-18=dd, 19-22=any)
- Stage audit cells: `data-grp='"+stgDef.color+"'`
- Memo cells: `covMemo(has,grp)` with "aj" param
- SOP/audit: `data-grp='qc'`
- Pillar ratings: `data-grp='rat'` (×6)

**Colour band CSS:**
- Header tints: .cov-stage-ig/tri/esa/dd/any/meta/qc/ratings at ~0.10-0.12 opacity
- Data tints: td[data-grp] at ~0.03-0.04 opacity
- Priority row override: .cov-priority-high td at rgba(183,28,28,0.04) !important

---

## 5-May-26 ~06:00 UK — REBUILD INTEGRATION SHIPPED LIVE

**Objective:** Transplant the "rebuild" version of the RESEARCH STAGES tab (lifecycle indicators, stage sub-buttons, Show Company toggle) from `preview/ic-ratings-dashboard-v2-rebuild.html` into the main live dashboard.

**What shipped:**
- LIFECYCLE_V1_CSS (417 lines) transplanted — Harvey ball glyphs, lifecycle cell styling
- COVERAGE_JS (715 lines) transplanted — lifecycle rendering, stage sub-buttons (IG/Tri/ESA/DD/Any), Show Company toggle, restructured column headers
- Fresh COVERAGE_DATA (77 tickers) from `build-coverage-data-v2.py`
- All other tabs (RATINGS, JUDGEMENTS, ANALYSIS, KEY, FUNDAMENTAL, COLOUR, PILLAR TREE) untouched

**Transplant method:** Python patcher script spliced 2 of 6 fenced sections (LIFECYCLE CSS = new, JS = expanded) from the v21-final rebuild backup into the live dashboard. CSS, BTN, CONTAINER sections were identical between live and rebuild — left untouched. DATA section regenerated fresh.

**Pipeline change — CRITICAL:**
- `patch-coverage-tab.py` V5 **ARCHIVED** as `patch-coverage-tab-V5-ARCHIVED-05May26.py` — running it would DESTROY the transplanted JS by overwriting with old V5 code
- **NEW:** `patch-coverage-data-only.py` V1 — replaces ONLY the COVERAGE_DATA section, all other fences untouched. Dry-run tested, 5/5 validation checks pass. Use this for all future daily pushes.
- `build-coverage-data-v2.py` unchanged (safe to run)

**Files:**
- Live dashboard: `databases/ic-ratings-dashboard-v2.html` (5,359,013 bytes, MD5: e6f9764b55ce5fd3b731817155127881)
- Backup: `memory/backups/2026-05-05-pre-rebuild-integration/ic-ratings-dashboard-v2.html`
- Test deployment: `test/ic-ratings-dashboard-v2.html` (GitHub Pages)
- Data-only patcher: `databases/scripts/patch-coverage-data-only.py`

**GitHub commits:** `b7328b6` (test/), `16a5450` (live root). Deployments #152, #153 both green.

**Quality gate:** 11/11 checks passed — RS tab renders, lifecycle glyphs, stage filters, Show Company toggle, RATINGS tab intact, console clean, visual parity with rebuild preview confirmed.

**Post-integration remaining:**
- GNG CHECKS + MEMO page functionality to be built fresh (not carried from rebuild — Richard's instruction)
- Consider renaming GitHub repo from `dashboards` to `ratings` (Richard raised 5-May-26)

---


## 1-May-26 ~07:40 UK — Cross-ref: V11→V20 morning arc informed APM SKILL ecosystem reform

**Context:** This Ratings Dashboard project produced the V20 memo template (the canonical APM memo render). Per Richard's reframe (1-May-26 morning), the memo template is treated as an APM ROLE artefact (output spec), not a SA project deliverable — SA owns the rendering mechanics only.

**Downstream artefacts authored today (1-May-26 morning):**
- `memory/projects/ratings-dashboard/v11-v20-summary.md` — rollup of the morning's 10-version arc (FIRST)
- `memory/coaching/lessons-and-mistakes.md` — 2 bright-spot 5-whys entries on back-briefing + persistent saving (SECOND)
- `wisdom-library/general/decision-making/judgement-analysis-information-ordering.md` — Gold tier model (SECOND)
- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP-review-2026-05-01.md` — AJA review of APM A&J SOP v2.1 against V20 + Richard's reframe; identifies 6 gaps requiring v2.2 rewrite (THIRD)
- `memory/skills/stage-progression/SKILL.md` — NEW cross-role SOP authored at Richard's instruction; 4-step pipeline (Brief → APM A&J → Richard's review → Weekly review meeting); APM is Step 2 (THIRD)
- Cross-refs added: APM SKILL.md, COS SKILL.md, RES SKILL-V2.md, memo-view-formatting SKILL.md all now point to STAGE PROGRESSION SOP and AJ SOP review

**SA project posture going forward:** This project file (`memory/projects/ratings-dashboard/`) remains the SA-role's record of how the dashboard was built and how to amend it. The substantive doctrine (memo template, weight tiers, signposting) is now governed by the APM ROLE files (APM SKILL + AJ SOP + memo-view-formatting SKILL). When APM authors a memo, the APM-side files are SSoT; when SA needs to modify the dashboard's rendering of those memos, this project file is SSoT.

**MILESTONE FULL-BACKUP:** `memory/session-handoffs/transcripts/2026-05-01-V20-MILESTONE-COMPLETE/` (8 files, taken at FIRST step)

**Next: AM-FULL-BACKUP-COMPLETE/** — final all-three-actions backup at THIRD.G.

> **OPEN ISSUES (lily pad):** See `memory/apm/open-issues-stage-progression.md` — master index of 8 open issues from STAGE PROGRESSION SOP rollout (1-May-26). When an issue surfaces in real work, process it then. Do not pre-emptively action.

**SA-relevant open issues (subset):** Issue #3 (Ratings Dashboard RESEARCH STAGES tab needs to render GNG CHECKS link per cell). Pick this up next time SA touches the dashboard.


---


## 1-May-26 ~06:37 UK — V20 SHIPPED (line-items element nav-RA suppression)

**Brief:** V10 made the line-items element render as a placeholder row in the main pane (no expanded RA rows). The nav-pane was overlooked — it still iterated the 7 RAs (Revenue growth, Margin trends, EPS growth, Cash returns, Change in multiple, FCF generation, Leverage) with audit chips + ratings. V20 fixes the parity gap.

**Implementation:** In `build_nav_html()`, after opening the line-items element's `<div class="nav-ra-list">`, immediately close it and `continue` (skip the inner attrs loop). Element banner remains in nav so user can still scroll-jump to it; only the inner RAs/CQs/audit chips are suppressed.

**Counts (V20 vs V19):**
| Metric | V19 | V20 | Δ |
|---|---|---|---|
| Nav RA items | 70 | 63 | -7 (line-items) |
| Nav CQ items | 182 | 175 | -7 (line-items TBDs) |
| File size | 898,021 | 893,215 | -4,806 |

**File:** 893,215 bytes. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=20
**FULL-BACKUP:** `memory/session-handoffs/transcripts/2026-05-01-0637-V20-FULL-BACKUP/`

---


## 1-May-26 ~06:35 UK — V19 SHIPPED (Ratings button = nav-only)

**Brief:** The Ratings button was toggling chips in BOTH nav AND main pane. User wanted nav-only.

**Implementation:** Removed the single CSS rule `body:not(.show-pills) .main-pill { display:none }` that was gating main-pane P/G/E/RA/CQ inline prefix pills. Main-pane pills now unconditionally visible. Nav-pane scope preserved: nav rating chips (A/B/C/D/F) and nav prefix tags (P/G/E/RA/CQ before nav items) still toggle with Ratings button. Tooltip updated to "Toggle rating chips in navigation pane".

**File:** 898,021 bytes. **Commit:** `feat(V19): nav-only Ratings`. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=19

---

## 1-May-26 ~06:33 UK — V18 SHIPPED (nav RA labels: strip Advantaged business parenthetical)

**Brief:** V10 added `strip_quoted_parenthetical()` for main-pane RA labels in the Advantaged business element ("Strong operational/competitive advantages? (does company demonstrably have…?) [MOAT]?" → "Strong operational/competitive advantages? [MOAT]?"). Nav-pane was overlooked. V18 fixes the parity gap.

**Implementation:** In `build_nav_html()`, when iterating attrs for the Advantaged business element, apply `strip_quoted_parenthetical()` to `ra_name` before display. Source TREE / canonical JSON unchanged — render-time strip only, same pattern as V10 main-pane.

**5 nav-RA labels affected:**
- Strong operational/competitive advantages? [MOAT]?
- Strong operational outputs? [OPERATE]?
- Strong financial outputs? [GENERATE]?
- Gets stronger as it gets bigger/time passes? Gravitational pull?**?
- Plausible scope for improvement over mid-term in the financial outputs? [SCOPE]?

**File:** 898,039 bytes. **Commit:** `6385b02`. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=18

**FULL-BACKUP (V18+V19 combined):** `memory/session-handoffs/transcripts/2026-05-01-0635-V19-FULL-BACKUP/`

---


## 1-May-26 ~06:32 UK — V17 SHIPPED (Element details default ON; active-state visual lifted)

**Brief items shipped (2/2):**

1. **Element details defaults ON** — added `element-details` to body default class + `.active` class to button. (Ratings was already default ON via `show-pills`.) On page load: Ratings + Element details lit; All RAs on / All CQs on / Audit dark.
2. **Stronger active-state visual** — inactive buttons now ghost-style (8% white bg + 65% white text on navy header). Hover lifts to 18%/100%. Active state = solid white fill + navy text + bold + subtle ring (`box-shadow: 0 0 0 1px rgba(255,255,255,0.4)`). Visually unambiguous on/off state.

**File:** 898,179 bytes. **Commit:** 1-line: `feat(V17): default ON + active visual`. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=17

**FULL-BACKUP:** `memory/session-handoffs/transcripts/2026-05-01-0632-V17-FULL-BACKUP/`

---

## 1-May-26 ~06:30 UK — V16 SHIPPED (nav button polish)

**Brief items shipped (5/5):**

1. **Renames:** "RAs on" → **"All RAs on"**; "CQs on" → **"All CQs on"**.
2. **Smaller buttons:** font 8.5pt → 7.5pt; padding 2px 6px → 1px 5px.
3. **Audit moved to end** (position 7 in button row).
4. **Element details moved to position 2** (right after Ratings).
5. **Two spacers added:** between Element details ↔ All RAs on, and between All CQs on ↔ Audit.

**Final button order:** Ratings | Element details | [spacer] | All RAs on | All CQs on | [spacer] | Audit

**Implementation:** `<span class="nav-toggle-spacer"></span>` (10px wide, flex:0 0 10px). All other CSS + JS semantics preserved.

**File:** 897,755 bytes. **Commit:** `997f0c0`. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=16
**FULL-BACKUP:** `memory/session-handoffs/transcripts/2026-05-01-0630-V16-FULL-BACKUP/`

---


## 1-May-26 ~06:28 UK — V15 SHIPPED (Pills nav button renamed to "Ratings")

**Brief:** Single-line label change in nav header.

**Implementation:** changed button label "Pills" → "Ratings" + tooltip "Toggle pill labels" → "Toggle rating chip labels". Kept `id="pill-toggle"` + `body.show-pills` CSS class semantics intact (renaming those would cascade through ~10 CSS selectors that gate the rating-pill chip visibility — wasteful churn for no functional gain). Visible label now reflects what the button actually toggles (the rating-letter chips on nav items).

**File:** 897,571 bytes. **Commit:** `2419a17`. **URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=15

**FULL-BACKUP:** `memory/session-handoffs/transcripts/2026-05-01-0628-V15-FULL-BACKUP/` (2 files: html + py; doctrine unchanged from V14).

---


## 1-May-26 ~06:20 UK — V14 SHIPPED + STATIC-AUDITED (4 nav-pane toggles)

**Session continuation:** SA role, EXECUTION mode. Nav-pane UX delta on top of V13.

**Brief items shipped (4/4):**

1. **Audit toggle** — shows audit chip inline next to each nav RA: word count vs target band + weight badge. Hidden by default; on when `body.show-audit`. Colour-coded chip (green = in band, amber = out of band; weight badge: normal grey / double navy / quadruple magenta).
2. **RAs on toggle** — `body.ras-always-on` overrides default focus-driven nav-ra-list expansion. All 70 nav-RA items visible regardless of which element is focused.
3. **CQs on toggle** — `body.cqs-always-on` overrides default click-to-expand nav-cq-list. All 182 nav-CQ items visible (and implicitly all RAs to support them).
4. **Element details toggle** — JS walks up from focused nav-RA/CQ to its parent element, then adds `.force-show` to all sibling RAs + their CQ lists. Re-applies on every scroll-driven focus change. Most-permissive precedence: RAs on > Element details for RAs; CQs on > Element details for CQs.

**Audit chip data:** computed at build time per RA via existing `compute_ra_metrics()`. Format: `{words}w /{target_lo}-{target_hi} {weight}`. Pass band check: words within target band → green; outside → amber.

**Implementation:**
- 5 nav header buttons in flex container (Pills + 4 new). Same `.nav-toggle-btn.active` styling.
- `_ra_audit_data()` + `_render_nav_audit_html()` Python helpers.
- Each nav-ra now carries `data-element-id` (parent element's anchor id); each nav-cq same. Used by Element-details JS to find sibling RAs.
- 4 new CSS toggle classes: `body.show-audit`, `body.ras-always-on`, `body.cqs-always-on`, `body.element-details`.
- `setupV14Toggles()` JS binds 4 button click handlers; `applyElementDetails()` JS implements the focused-element walk-up.

**Pre-write backup pattern this round:** Initial single-shot patch failed mid-flight (one assertion error → entire patch lost). Recovered by restoring from `.bak-pre-v14-...` and re-applying via incremental `step()` function that writes back to disk after each successful step. **Pattern flagged:** for multi-step build script patches, always use incremental write-back, not single-shot.

**File:** `databases/memo-style-sheet3-htro.html` (897,585 bytes — V14). Backup `.bak-pre-v14-20260501-061614`.
**Build script:** `databases/scripts/build-style-sheet3-htro.py` (84,297 bytes). Backup `.bak-pre-v14-20260501-061614`.
**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=14
**GitHub commit:** `854270f` (1 file changed, 375 insertions(+), 287 deletions(-)).

**Counts (V14 vs V13):**
| Metric | V13 | V14 | Δ |
|---|---|---|---|
| File size | 864,396 | 897,585 | +33,189 (+3.8%) |
| Elements | 19 | 19 | 0 |
| RAs | 63 | 63 | 0 |
| CQs | 175 | 175 | 0 |
| Nav RA items | 63 (+7 line-items) | 70 | n/a |
| Nav CQ items | 175 (+7 line-items) | 182 | n/a |
| Nav audit chips | 0 | 70 | +70 |
| Toggle buttons | 1 (Pills) | 5 | +4 |

**Doctrine:** No principles or SKILL changes — V14 is renderer + UX only. Doctrine remains v3.8 / SKILL v2.8.

**Pre-write backups taken:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v14-20260501-061614`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v14-20260501-061614`
- `databases/memo-view-formatting-principles.md.bak-pre-v14-20260501-061614`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v14-20260501-061614`

**FULL-BACKUP folder:** `memory/session-handoffs/transcripts/2026-05-01-0620-V14-FULL-BACKUP/` (7 files).

**Open questions (live audit):**
- Q1: Audit chips readable at 7pt? May need bumping to 8pt if too small on iPad.
- Q2: With "RAs on" + "Audit" both ON, does the nav pane stay scannable, or does the chip clutter overwhelm the RA labels?
- Q3: Element details — when scrolling between elements, does the force-show set update smoothly, or does it flicker? Watch for race condition with V8 scroll-tracker.

---


## 1-May-26 ~06:10 UK — V13 SHIPPED + STATIC-AUDITED (1 brief item)

**Session continuation:** SA role, EXECUTION mode. Single-RA delta on top of V12.

**Brief item shipped:**

- **Plain sight risks RA → DOUBLE weight.** WEIGHT_OVERRIDES entry #11 added. The "no slowing of core engine / no mediocre CEOs / no big Hmmms" screen joins #7 Lessons check, #8 Negative earnings momentum, #10 Crash through stops as RA-level doubles inside G4 Case riskiness (alongside G4 quadruples Q1 Sector strength + Q2 General ACHs).
- **Verified:** 3 CQs × 22.3 bullets/CQ avg = 67 total bullets. Per-CQ in DOUBLE ESA band (18-30).

**Doctrine cascade locked:**
- `databases/memo-view-formatting-principles.md` v3.7 → **v3.8** (entry #11 added to §IV.H double-weight table).
- `memory/skills/memo-view-formatting/SKILL.md` v2.7 → **v2.8** (mirror).

**File:** `databases/memo-style-sheet3-htro.html` (864,396 bytes — V13). Backup `.bak-pre-v13-20260501-060831`.
**Build script:** `databases/scripts/build-style-sheet3-htro.py` (78,239 bytes). Backup `.bak-pre-v13-20260501-060831`.
**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=13
**GitHub commit:** `b0bf915` (1 file changed, 147 insertions(+), 147 deletions(-)).

**Counts (V13 vs V12):**
| Metric | V12 | V13 | Δ |
|---|---|---|---|
| File size | 860,920 | 864,396 | +3,476 |
| Elements | 19 | 19 | 0 |
| RAs | 63 | 63 | 0 |
| CQs | 175 | 175 | 0 |

**G4 Invalidating attributes element — current weight tier roll-up (post-V13):**
| RA | Tier (V13) |
|---|---|
| General ACHs? | QUADRUPLE (Q2) |
| Plain sight risks? | **DOUBLE (#11, V13 NEW)** |
| No mediocrity? | normal |
| Negative earnings momentum? | DOUBLE (#8) |
| Lessons check? | DOUBLE (#7) |

3 of 5 RAs in Invalidating attributes are now elevated above normal weight — reflecting the load-bearing role this element plays in invalidation discipline.

**Pre-write backups taken:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v13-20260501-060831`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v13-20260501-060831`
- `databases/memo-view-formatting-principles.md.bak-pre-v13-20260501-060831`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v13-20260501-060831`

**FULL-BACKUP folder:** `memory/session-handoffs/transcripts/2026-05-01-0610-V13-FULL-BACKUP/` (7 files).

---


## 1-May-26 ~05:59 UK — V12 SHIPPED + STATIC-AUDITED (2 brief items)

**Session continuation:** SA role, EXECUTION mode. Two-item delta on top of V11.

**Brief items shipped:**

A. **General ACHs RA escalated DOUBLE → QUADRUPLE.** WEIGHT_OVERRIDES entry #9 weight changed; doctrine §IV.H entry #9 marked "(escalated v3.7)" + new Q2 row added to quadruple table. Verified: 39 bullets per CQ (QUADRUPLE ESA band 36-60). Weight badge in metric subtext = "quadruple".

B. **BQ summary-only element reorder.** New `BQ_SUMMARY_ORDER` constant + `reorder_bq_elements()` helper. BQ summary block now shows: Row 1 = great operator + value chain + high secular growth; Row 2 = advantaged business + industry structure + paradigm fit. Main-pane element banners + nav-pane element list KEEP canonical TREE order (canonical-vs-narrative decoupled). Verified: summary headers in correct V12 order on both rows; main-pane banners still canonical.

**Doctrine cascade locked:**
- `databases/memo-view-formatting-principles.md` v3.6 → **v3.7**:
  - §IV.H entry #9 marked "escalated v3.7" — General ACHs DOUBLE → QUADRUPLE.
  - §IV.H Quadruple table: new entry Q2 (General ACHs) alongside Q1 (Sector strength).
  - §IV.J.1 (NEW): BQ summary-only element reorder doctrine + R26b validator.
- `memory/skills/memo-view-formatting/SKILL.md` v2.6 → **v2.7** (mirror).

**File:** `databases/memo-style-sheet3-htro.html` (860,920 bytes — V12). Backup `.bak-pre-v12-20260501-055701`.
**Build script:** `databases/scripts/build-style-sheet3-htro.py` (77,968 bytes). Backup `.bak-pre-v12-20260501-055701`.
**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=12
**GitHub commit:** `ed162e9` (1 file changed, 394 insertions(+), 394 deletions(-)).

**Counts (V12 vs V11):**
| Metric | V11 | V12 | Δ |
|---|---|---|---|
| File size | 861,412 | 860,920 | -492 (negligible) |
| Elements | 19 | 19 | 0 |
| RAs | 63 | 63 | 0 |
| CQs | 175 | 175 | 0 |

V12 file size barely changed — General ACHs went up (~17 more bullets at quadruple vs double) but Lorem variance offset; BQ reorder is structurally identical (just different element column order).

**Pre-write backups taken:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v12-20260501-055701`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v12-20260501-055701`
- `databases/memo-view-formatting-principles.md.bak-pre-v12-20260501-055701`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v12-20260501-055701`

**FULL-BACKUP folder:** `memory/session-handoffs/transcripts/2026-05-01-0600-V12-FULL-BACKUP/` (4 files: html, py, principles md, SKILL md).

**Open questions for sign-off:**
- Q1 (live): does the BQ summary now read more clearly with the narrative row grouping?
- Q2 (live): is General ACHs at 39 bullets visibly heavier than the other RAs in its element (which sit at double = ~22 bullets)?

---


## 1-May-26 ~05:50 UK — V11 SHIPPED + STATIC-AUDITED (9 brief items: doctrine v3.6 + 9 renderer changes)

**Session:** SA role, EXECUTION mode. V11 round of refinements on the Sheet 3 visual style memo specimen.

**Brief items shipped (all 9 verified at HTML level via static audit; live Chrome audit deferred to Richard):**

1. **Conservative IR RA → NORMAL weight** (was inheriting double from element). New WEIGHT_OVERRIDES entry N1. Verified: 14 bullets per CQ (NORMAL ESA band 9-15).
2. **BQ summary columns split 2 rows × 3 cols** (was single row × 6 cols). New §IV.J doctrine. BQ has 6 elements → splits into 2 chunks of 3. data-n-elements="6", data-row-index="0" + "1" both present in HTML.
3. **Nav CQ unroll on RIGHT DIRECTION RA scroll-focus** — JS bug fixed. V8 scroll-tracking expanded parent nav-ra-list but not the focused nav-ra itself, so `.nav-ra.expanded + .nav-cq-list` selector never matched. Fix: scroll-focus now adds `.expanded` to focused nav-ra (and clears it from siblings). Also added nav-cq scroll-focus handling (when scroll lands on a CQ row, parent RA + ra-list both expanded). LIVE-VERIFY ONLY (JS behaviour).
4. **GROUP + ELEMENT summary rating pills ~25% smaller** — new `.summary-rating-chip` modifier on `.rating` chips. font-size 10pt → 7.5pt, padding 2px 8px → 1px 5px, min-width 22px → 16px. 20 occurrences in HTML.
5. **ELEMENT summaries span cols 2-4** (col 1 empty) — colspan 4 → 3, leading empty `<td class="col-cq elem-summary-empty-cq">`. New §IV.L doctrine. 0 colspan=4 elem rows; 14 colspan=3 + 15 empty-cq cells in HTML.
6. **GENERAL ACHs RA → DOUBLE weight** (audit found rendering normal). New WEIGHT_OVERRIDES entry #9. Verified: 22 bullets per CQ (DOUBLE ESA band 18-30).
7. **Crash through stops risk RA (SHMLP CQ) → DOUBLE weight** (audit found rendering normal). New WEIGHT_OVERRIDES entry #10. Verified: 43 bullets across 2 CQs (DOUBLE × 2-CQ band 36-60).
8. **Sector strength RA → QUADRUPLE weight** (new tier). New WEIGHT_OVERRIDES entry Q1. New §IV.F multiplier table row + WEIGHT_MULTIPLIER quadruple=4.0. Verified: 57 bullets per CQ (QUADRUPLE ESA band 36-60).
9. **CASE OPTIONALITY GROUP summary → 3 columns (1 general + 2 RA columns)** (was skipped per V9 single-element rule). New §IV.K doctrine + `build_g5_optionality_columns()` builder + build() guard updated to permit single-element Case optionality. Verified: G5 group-summary-row data-n-elements="2" data-layout="single-row" with cols for "Additional upside?" + "Self-righting behaviour ATM?".

**Doctrine cascade locked:**
- `databases/memo-view-formatting-principles.md` v3.5 → **v3.6**:
  - §IV.F: weight table extended with `quadruple` (4.0×) row.
  - §IV.F: floor formula updated to half/normal/double/quadruple (0.5×/1×/2×/4×). New example: ESA × quadruple = 36-60 bullets.
  - §IV.H: 3 new override entries (#9 General ACHs DOUBLE, #10 Crash through stops DOUBLE, Q1 Sector strength QUADRUPLE) + 1 defensive normal restatement (N1 Conservative IR NORMAL).
  - §IV.J (NEW): group summary 2-row layout (>3 elements → 2 rows × max 3 cols).
  - §IV.K (NEW): G5 Optionality 3-column override (1 general + 1 col per RA).
  - §IV.L (NEW): element summary spans cols 2-4 only.
  - R25b/R26/R27/R28 validator rows added.
- `memory/skills/memo-view-formatting/SKILL.md` v2.5 → **v2.6** (mirror).
- 4 new pre-flight checklist items (#21 quadruple, #22 element summary cols 2-4, #23 group summary multi-row, #24 G5 override).

**File:** `databases/memo-style-sheet3-htro.html` (861,412 bytes — V11). Backup `.bak-pre-v11-20260501-052917`.
**Build script:** `databases/scripts/build-style-sheet3-htro.py` (76,293 bytes). Backup `.bak-pre-v11-20260501-052917`.
**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=11
**GitHub commit:** `ac218ce` (1 file changed, 720 insertions(+), 651 deletions(-)).

**Counts (V11 vs V10):**
| Metric | V10 | V11 | Δ |
|---|---|---|---|
| File size | 757,664 | 861,412 | +103,748 (+14%) |
| Elements | 19 | 19 | 0 |
| RAs | 63 | 63 | 0 |
| CQs | 175 | 175 | 0 |

V11 size increase driven by (a) Sector strength QUADRUPLE → +43 bullets vs V10 normal, (b) General ACHs + Crash through stops → ~+30 bullets each, (c) G5 Optionality summary block added (was skipped in V10), (d) BQ summary now in 2 rows (slightly more HTML wrapping).

**Pre-write backups taken:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v11-20260501-052917`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v11-20260501-052917`
- `databases/memo-view-formatting-principles.md.bak-pre-v11-20260501-052917`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v11-20260501-052917`

**FULL-BACKUP folder:** `memory/session-handoffs/transcripts/2026-05-01-0600-V11-FULL-BACKUP/` (7 files: html, py, principles md, SKILL md, state.md, pillar-tree-canonical.json, pillar-tree-new-taxonomy.html).

**Process notes:**
- Patches written via Python heredoc + `Path.write_text()` to avoid Edit-tool truncation pattern (per `feedback_edit_tool_truncation_bug`). 0 truncation events this session.
- HTRO_CONTENT_JSON missing in this session (was at `/sessions/optimistic-kind-tesla/mnt/outputs/htro_content_v2.json`, now `/sessions/zealous-ecstatic-dirac/...`). Build script V11 patched with graceful fallback to all-Lorem rendering. 175/175 CQs rendered as Lorem (vs ~29/175 real HTRO in V10). Visual structure unchanged — V11 brief items are renderer/doctrine-level, not data-level.
- ROOT path also updated in script: `optimistic-kind-tesla` → `zealous-ecstatic-dirac` (this session's mount).
- Build → push → static audit cycle: ~25 minutes from brief acceptance to live commit. Quality > speed honoured throughout (doctrine update FIRST, code update SECOND, static audit before push, no shortcut on the 25% over floor checks).

**Item 3 (nav CQ unroll on RIGHT DIRECTION RA scroll) is JS-only** — not directly verifiable in static HTML. Logic added: scroll-tracker now (a) adds `.expanded` to the focused nav-ra so its CQ list unfolds, (b) clears `.expanded` from sibling nav-ras to keep the tree clean, (c) handles the nav-cq case (when scroll-focus lands on a CQ row, parent RA + parent ra-list both expand). LIVE-VERIFY in Chrome on iPad/desktop is the acceptance test.

**Open questions for sign-off:**
- Q1 (live): does scrolling the main pane to "Right direction" RA unroll its CQs in the nav pane? (Item 3 verification.)
- Q2 (visual): does the BQ 2×3 grid look right, or does the empty general-column slot on row 2 need styling tweaks?
- Q3 (visual): are the rating pills in summary blocks visibly smaller — i.e., enough to be felt as "smaller" (~25% target)?
- Q4 (visual): does the col-1-empty element summary look right, or is the leading empty cell visually awkward?

---


## 30-Apr-26 ~13:00 UK — MEMO SHEET 3 SPECIMEN V3 (doctrine reform + summaries + nav refinements) — IN FLIGHT

**Session:** SA role, EXECUTION mode. Substantial reform — doctrine + content + UX.

**Brief items in flight (Round 7 + Round 8 combined):**

### Doctrine reform (memo-view-formatting-principles.md v3.1 → v3.2)
- **Weight system** (half/normal/double) per item, propagating DOWN the taxonomy.
- **Triaging "normal" floor**: 3-5 bullets per CQ (1 anchor + 2-4 subs).
- **Stage scaling**: ESA = 3× Triaging, DD = 5× Triaging. SUPERSEDES v3.1 stage-gated-depth rule.
- **Bullet COUNT scales** with the multiplier (not just word counts).
- **"≥25% over floor"** authorial principle (SOFT validator warning).
- **Section-specific weight overrides** for 5 named scopes (entire elements/groups/RAs).
- v3.1 §IV.B sub-section word budgets + §IV.C family floors marked DEPRECATED.

### Specimen V3 (memo-style-sheet3-htro.html)
- Right-align CQ column.
- Add ToC nav pane (left 25%, sticky, internally scrollable).
- Tree-diagram nav: Pillar → Group (BB) → Element → RA (expand-on-focus).
- IntersectionObserver-driven focus (top-quarter trigger).
- Click any nav node → smooth-scroll main pane.
- RA-section metrics subtext: word count, target, audit checks (R14, R5, R17 = "word limit", "BP #", "highlighting density").
- Extra line break after last sub-bullet of last CQ per RA.
- Sub-bullet underline 10-30% (same target as anchor).
- Toggleable nav pills (header button RHS).
- **NEW: RA summary judgement block** when RA has >1 CQ. Full-width across cols 2-4. Bold + italic. Count = max(4, ceil(1.5 × CQ count)).
- **NEW: Element summary judgement** at top of each element. ≥8-10 bullets. ≥1 per RA. Single-line per bullet spanning cols 2-4. RA ref + rating + bold-italic text.

### Confirmed (back-brief 1A-1H all answered):
- 1A propagating weights ✅
- 1B entire scope (case-fit = G2 entire; outputs = both elements) ✅
- 1C bullet COUNT scales (not just word lengths) ✅
- 1D ≥25% authorial principle (SOFT) ✅
- 1E supersede stage-gated-depth rule ✅
- 1F double-weight inherits down ✅
- 1G full-width across cols 2-4 (CQ + R + A&J) ✅
- 1H single-line bullets spanning cols 2-4 (RA ref + rating + text inline) ✅

### Files to touch:
- `databases/memo-view-formatting-principles.md` → v3.2 (new §IV.F-H + DEPRECATED markers).
- `memory/skills/memo-view-formatting/SKILL.md` → v2.4 (mirror).
- `databases/scripts/build-style-sheet3-htro.py` → V3 rewrite.
- `databases/memo-style-sheet3-htro.html` → regenerated V3.

### Pre-write backups taken:
- `databases/memo-style-sheet3-htro.html.bak-pre-v3-20260430-125813`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v3-20260430-125813`
- `databases/memo-view-formatting-principles.md.bak-pre-v32-20260430-125813`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v32-20260430-125813`

### Full backup folder:
`memory/session-handoffs/transcripts/2026-04-30-1100-FULL-BACKUP/` (7 files including pillar-tree-new-taxonomy.html for nav reference)

---

## 30-Apr-26 ~17:10 UK — V10 SHIPPED + LIVE-AUDITED (6 changes: doctrine + group summary + line-items + BQ strips)

**Brief items shipped (all 6 verified live in Chrome):**

1. **Line-items element renders as placeholder** — "Required financial outputs (line items)?" element banner followed by single-cell row "Financial model table to follow: Revenue growth, Margin trends, EPS growth, Cash returns, Change in multiple, FCF generation, Leverage". 7 RAs no longer expanded as table rows; nav still shows them. Build counts dropped 70/182 → 63/175 (RAs/CQs).
2. **Case simplicity group double-weight removed; element-level override added** — `DOUBLE_WEIGHT_OVERRIDES` entry #4 changed from `{"group": "Case simplicity"}` to `{"element": "Required simplicity guardrails"}`. Acceptable + Unacceptable case setups now NORMAL weight. Verified: "Fit with acceptable case setups?" element banner shows no "double weight" badge.
3. **DD stage multiplier 5.0 → 3.75** — `STAGE_MULTIPLIER["DD"] = 3.75` (= ESA × 1.25). Doctrine v3.5 §IV.G updated. Skill v2.5 mirror updated.
4. **Group summary blocks for BB groups** — multi-column layout: leftmost 22% = 3 general bullets; remaining 78% split equally among per-element columns. Each element column has a header showing the element name + ≥4 bullets each linked to an RA in that element with rating chip + IAJA suffix. Skipped when group has only 1 element (G5 Optionality). Background `#E8F5EE` matching group banner mint. 4 group summary rows in HTML (G1, G2, G3, G4).
5. **Advantaged business RA parenthetical strip** — render-time strip of `\s*\("[^"]*"\)` from RA labels in this element only. Verified: "Strong operational/competitive advantages? [MOAT]?" (was "Strong operational/competitive advantages? ("does company demonstrably have…?") [MOAT]").
6. **Business quality prefix strip** — render-time strip of "Business quality - " prefix from BQ element titles + title-case first letter. Applied to both main-pane element banners AND nav-pane element entries. Verified: "Great operator", "Advantaged business + widening SRCA?", etc. Zero "Business quality - " strings remaining in HTML output.

**Doctrine updates locked:**
- `databases/memo-view-formatting-principles.md` v3.4 → v3.5 (DD multiplier + §IV.H entry #4 narrowing)
- `memory/skills/memo-view-formatting/SKILL.md` v2.4 → v2.5 (mirror)

**File:** `databases/memo-style-sheet3-htro.html` (757,664 bytes — V10). Backup `.bak-pre-v10-20260430-164320`.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=10

**Audit results (live in Chrome):**
- Title V10 ✓
- 4 group summary rows (G1, G2, G3 with 6 element cols, G4) ✓
- 1 line-items placeholder ✓
- "Great operator" (no BQ prefix) in main pane ✓
- "Strong operational/competitive advantages? [MOAT]?" RA (parenthetical stripped) ✓
- "Fit with acceptable case setups?" element shows normal weight (not double) ✓

**Pattern flagged again:** Edit-tool truncation struck twice during V10 build (line 1252 mid-`if len(attrs)`, line 1239 mid-print of an earlier session). Recovered both via Python tail rewrite. ~13 truncation events this session.

**Pre-write backups:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v10-20260430-164320`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v10-20260430-164320`
- `databases/memo-view-formatting-principles.md.bak-pre-v10-20260430-164320`
- `memory/skills/memo-view-formatting/SKILL.md.bak-pre-v10-20260430-164320`

**Full backup folder:** `memory/session-handoffs/transcripts/2026-04-30-1700-FULL-BACKUP/` (7 files)

---

## 30-Apr-26 ~16:18 UK — V9 SHIPPED + LIVE-AUDITED (single-RA elements skip summary)

**Brief:** When an element has only 1 RA, skip the element summary block entirely. Element rating = that single RA's rating (already true via existing `_modal_rating` of single-element list).

**Implementation:**
- In `build()`, wrap the element summary emission in `if len(attrs) > 1:`. Single-RA elements skip `build_element_summary_bullets()` + `render_element_summary_row()` entirely.
- The element banner is followed directly by the RA's summary row (if RA has >1 CQ) or by CQ rows (if RA has 1 CQ).
- `_elem_rating()` unchanged: returns modal of RA ratings, which is the single RA's rating when N=1.

**Single-RA elements affected (4):**
1. Strong sell-side earnings momentum?
2. Business quality - High secular / long-term growth potential?
3. Business quality - Fit with stock market paradigm / regime / thematics?
4. AUM-constraining attributes

**Live audit verified:**
- `n_elem_summary_rows: 15` (was 19; dropped 4)
- Strong sell-side earnings momentum banner followed by `ra-summary-row` (no element summary in between) ✓
- Required input forces banner followed by `elem-summary-row` (multi-RA, summary preserved) ✓

**Pattern flagged:** Edit-tool truncation hit again during V9 build (line 1239 mid-print). Recovered via Python tail rewrite. ~11 truncation events this session.

---

## 30-Apr-26 ~16:10 UK — V8 SHIPPED + LIVE-AUDITED (scroll-tracking nav focus)

**Brief:** As user scrolls main pane, nav focus highlight follows whatever's at the top of the viewport (just below sticky stack), tracking down to RA-level granularity. Element + RA tracking only (no CQ-level — would flicker too much).

**Implementation:**
- Replaced V5 `IntersectionObserver`-based focus with explicit scroll listener + rAF-throttled `getBoundingClientRect()` polling.
- Anchors tracked: pillar banners + group banners + element banners + RA-summary-row[id] + cq-row[id^="ra-"] (= 96 anchors total).
- Trigger line = `paneRect.top + stickyStackHeight + 10px` (just below sticky table thead).
- Pick the LAST anchor whose `top <= triggerY` (deepest currently-above-line).
- Auto-expand: if focused on RA, expand parent's nav-ra-list. If focused on element, expand its nav-ra-list. Walk up parent if needed.
- Auto-scroll-into-view: nav-pane scrolls so focused item is visible (block:'nearest', smooth).
- Throttled with `requestAnimationFrame` for performance.

**Live audit verified:** Scrolled main pane to Robust base RA → "Robust base?" RA highlighted purple in nav with parent "Required input forces?" element auto-expanded and CQ list visible. Element banner at top of viewport per V5 sticky behaviour, sticky stack sums to ~107px.

**Pattern flagged:** Edit-tool truncation hit again during V8 build (line 1202 mid-`print(f"Backed`). Recovered via Python tail rewrite. ~10 truncation events this session.

**Bullet rule clarification (per Richard's question):** Locked rules permit 0-6 sub-bullets per anchor (R5 hard cap = 6). The V7 specimen often shows 5 because the Lorem renderer was using `min(6, remaining)` as the upper bound; this is mechanical not editorial. Real authoring should vary the count freely between 0-6 based on content. Future Lorem renderer fix: randomise n_subs in [2..6] per anchor instead of always maxing.

---

## 30-Apr-26 ~15:45 UK — V7 SHIPPED + LIVE-AUDITED (5 polish refinements)

**Brief items shipped (all 5 verified live in Chrome):**

1. **Drop RA summary label** — Removed `<div class="ra-summary-label">RA summary judgement (N bullets)</div>` from both render points. Summary blocks now flow directly into bullets. 0 ra-summary-label divs in HTML (was 34).
2. **Bold-first sort in RA summaries** — Added `bullets.sort(key=lambda b: 0 if b["bold"] else 1)` in `build_ra_summary_bullets()`, plus safety check ensuring at least one bullet is bold. 34/34 RA summary blocks now start with a bold bullet.
3. **Nav: CQs visible on RA click** — `build_nav_html()` now emits `<div class="nav-cq-list">` after each RA in nav, with all CQs nested. CSS hides by default; CQs become visible when parent RA has `.expanded` class. Click handler toggles `.expanded` on the clicked RA. 182 nav-cq nodes in HTML.
4. **Column re-proportion 15/15/6/64** — RA shrunk 18→15, CQ grew 12→15 (+25% on CQ relative to V6). CQ column visibly wider; RA column slimmer.
5. **RA modal rating chip in main pane** — Computed via `_modal_rating([rec.rating for ... in records])`, rendered inline next to RA label using existing `.rating` chip class with new `.ra-rating-chip` modifier (smaller font, 8.5pt). 70 ra-rating-chips in HTML (one per RA).

**File:** `databases/memo-style-sheet3-htro.html` (851,844 bytes). Backup: `.bak-pre-v7-20260430-153159`.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=7

**Audit numbers:**
- 0 ra-summary-labels (V7 removed them)
- 34/34 RA summary blocks start with bold bullet (bold-first sort working)
- 182 nav-cq nodes (one per CQ in main pane)
- 70 ra-rating-chips (one per RA)
- ra_col + cq_col widths both 207.141px (15% each — equal width)

**Pattern flagged again:** Edit-tool truncation struck once during V7 build (line 1123 mid-comment). Recovered via Python tail rewrite. Total ~9 truncation events this session.

---

## 30-Apr-26 ~15:15 UK — V6 SHIPPED — MULTI-ANCHOR FIX (doctrine compliance restored)

**Bug found:** V5 renderer was producing only 1 anchor + ≤6 subs per CQ regardless of stage×weight target. This was clipping ESA × normal CQs to 7 bullets (target 9-15) and ESA × double CQs to 7 bullets (target 18-30). Root cause: `lorem_row()` clamped subs to 6 to satisfy R5 but never split overflow into additional anchor groups.

**Fix shipped (V6):**
- Data structure: CQ record now contains `groups[]` list. Each group = `{anchor, anchor_iaja, subs}` with subs ≤6 per group (R5 satisfied per group).
- `lorem_row(weight, stage)`: computes total target bullets, splits across multiple anchor groups (1 anchor + ≤5 subs per group = ≤6 bullets per group).
- `render_aj_cell()`: iterates `groups[]`, emits each anchor + its subs with a `bullet-anchor-spacer` (6px gap) between groups.
- `compute_ra_metrics()`: walks groups[] to count anchors, subs, breaches.
- Back-compat: HTRO real content (single anchor+subs) is wrapped as `[{anchor, subs}]` single-element groups list at render time.

**Doctrine compliance verified (post-V6):**
| Stage × Weight | Anchor groups | Total bullets | §IV.F target |
|---|---|---|---|
| Triaging × normal | 1 | 5 | 3-5 ✓ |
| Triaging × double | 2 | 9 | 6-10 ✓ |
| ESA × normal | 2 | 11 | 9-15 ✓ |
| ESA × double | 4 | 21 | 18-30 ✓ |
| DD × normal | 5 | 25 | 15-25 ✓ |
| DD × double | 9 | 49 | 30-50 ✓ |

**Output deltas (V5 → V6):**
- Anchors in HTML: 182 → 665 (3.6× — multi-anchor structure)
- Sub-bullets: ~1,000 → 2,891 (~3×)
- Anchor spacers: 0 → 483 (visual gaps between groups)
- File size: 394 KB → 790 KB (~2× because more bullets)
- Metric bands passing (green): mostly warn → 52 pass / 18 warn

**File:** `databases/memo-style-sheet3-htro.html` (790,562 bytes). Backup: `.bak-pre-v6-20260430-150905`.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=6

**Pattern flagged again:** Edit-tool truncation struck once during V6 build (line 1111 mid-`final_parts`). Recovered via Python tail rewrite. Total ~8 truncation events this session.

---

## 30-Apr-26 ~14:35 UK — V5 SHIPPED + LIVE-AUDITED (10 polish refinements)

**Brief items shipped (all 10 verified live in Chrome):**

1. **Rating pills in nav** — 96 nav-rating-pills emitted across pillar/group/element/RA tiers, derived from modal of children ratings. A=green / B=blue / C=khaki / D=amber / F=red.
2. **Pills ON by default** — `body class="show-pills"` on load; "Pills" toggle button starts in active state.
3. **Prefix pills in main pane** — Element banner `[E]`, RA cell `[RA]`, CQ cell `[CQ]`, pillar banner `[P]`, group banner `[G]`. Single-letter tier labels matching nav legend.
4. **RA summary left-aligned + bold/non-bold** — `text-align:left` on ra-summary-row td (was inheriting right-align from CQ col). Per-bullet `bold` field; ~30% of generated Lorem bullets marked bold. 91 bold + ~180 non-bold = ~270 RA summary bullets across 34 RAs.
5. **IAJA suffix on summary bullets** — `[J]` purple pill at end of each RA + element summary bullet. Default kind = J (judgement).
6. **Sticky element banner** — CSS-only `position:sticky; top:107px` (main-header 77px + thead ~30px). Element banner stays at top during scroll.
7. **Tree connector** — RA col-1 indented to 24px padding-left (16px content + 8px buffer). Vertical line at left:8px running full height of RA cell + horizontal arm at top:18px. Last RA shortens line to L-shape.
8. **CQ column 2/3 width** — Column widths now 18/12/6/64 (RA grew +2, CQ shrunk -6, A&J grew +4).
9. **Audit checks stacked vertically** — 210 `metric-line` spans (70 RAs × 3 audit lines: word limit, BP #, highlighting density).
10. **General element-summary bullets** — 57 general bullets (19 elements × 3) prepended before RA-linked bullets in each element summary. No RA-ref pill, no rating chip — pure bold-italic + IAJA suffix. No divider line between general and RA-linked groups.

**File:** `databases/memo-style-sheet3-htro.html` (394,274 bytes). Backup: `.bak-pre-v5-20260430-141339`.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=5

**Audit results (live in Chrome):**
- Title V5 ✅
- `body_class: "show-pills"` ✅
- 19 main-pill-e + 70 main-pill-ra + 182 main-pill-cq ✅
- 96 nav rating pills (13 A + 22 B + 31 C + 15 D + 15 F) ✅
- 57 general element-summary bullets ✅
- 91 bold RA summary bullets (~30%) ✅
- 210 metric-line spans (vertical stack) ✅
- `sticky_element_top: "107px"` (main-header + thead) ✅
- `ra_col_padding_left: "24px"` (tree connector indent) ✅
- `ra_summary_text_align: "left"` ✅

**Pattern flagged again:** Edit-tool truncation struck twice during V5 build (line 965 mid-build(), line 1067 mid-print). Recovered both via Python tail rewrite. 7+ truncation events this session — pattern is now reliable enough to formally codify in feedback memory.

**Pre-write backups:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v5-20260430-141339`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v5-20260430-141339`

---

## 30-Apr-26 ~13:45 UK — V4 SHIPPED (4 visual refinements after first browser review)

**Brief items shipped (all 4 audited live in Chrome):**

1. **Click-to-scroll offset fix** — Nav-click target now lands JUST BELOW the sticky header stack rather than behind it. JS computes `getStickyStackHeight()` = main-header (77px) + table thead (~30px) and subtracts from scroll target.

2. **Memo title frozen sticky** — Wrapped page-title + page-subtitle in `.main-header` div with `position:sticky; top:0; z-index:4`. Stays visible during scroll. Table thead now stacks below it via `top: var(--main-header-h, 70px)` (CSS var set by JS at runtime via `setMainHeaderCssVar()`).

3. **RA summary moved to TOP of RA group** — Was rendered after the last CQ row; now rendered before the first CQ row. RA-row anchor `id` moved to the summary row so click-on-RA scrolls to summary first. Rowspan logic preserved.

4. **Element summary cleanup** — (a) Removed "Summary" label cell in col 1 (now spans all 4 cols), (b) removed "ELEMENT SUMMARY JUDGEMENT [DOUBLE]" header line, (c) bullets sit close to banner with `padding-top:2px` after banner, (d) background changed from `#fef9e7` to `#FAEEDA` matching the element banner — they read as one unit. Element banner's `border-bottom:none` so visual continuity preserved.

**File:** `databases/memo-style-sheet3-htro.html` (357,559 bytes). Backup: `.bak-pre-v4-20260430-133442`.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=4 (CDN was stale on first audit; cache-buster `?cb=v4-fresh-...` confirmed V4 served).

**Audit results (live in Chrome):**
- Title V4 ✅. `has_main_header: true`, `main_header_h: 77px`, `--main-header-h` CSS var set ✅
- Table thead `top: 77px` (stacks below sticky main header) ✅
- 19 element summary rows / 34 RA summary rows / 70 RA metric subtexts ✅
- 0 col-ra-summary cells (V3 cell removed) ✅
- elem_summary_bg = elem_banner_bg = `rgb(250, 238, 218)` (#FAEEDA — unified) ✅
- Visual: RA summary judgement appears IMMEDIATELY AFTER element summary, BEFORE first CQ row "Demand: changes in customer..." ✅

**Pattern flagged again:** Edit-tool truncation struck once during V4 build (line 919 mid-string). Recovered via Python tail rewrite. Adding to count of session-level truncation events.

**Pre-write backups:**
- `databases/memo-style-sheet3-htro.html.bak-pre-v4-20260430-133442`
- `databases/scripts/build-style-sheet3-htro.py.bak-pre-v4-20260430-133442`

---

## 30-Apr-26 ~13:10 UK — V3 BUILD COMPLETE + LIVE-AUDITED IN CHROME

**Doctrine updates shipped:**
- `databases/memo-view-formatting-principles.md` v3.4: §IV.F (weight system + per-CQ floor), §IV.G (stage scaling 3×/5×), §IV.H (8 named double-weight scopes). v3.1 stage-gated-depth + family floors marked DEPRECATED. R22, R23, R24, R25 added to validator coverage.
- `memory/skills/memo-view-formatting/SKILL.md` v2.4 mirrors §IV.F-H in pre-flight #17-20 and adds 3 new anti-patterns (weight-system ignorance, stage-skipping CQs, floor-hugging).
- R17 underline rule extended to sub-bullets (10-30% same target as anchors).

**V3 specimen shipped:**
- `databases/memo-style-sheet3-htro.html` 360,072 bytes (vs V2 152KB → ~2.4× growth from element + RA summaries).
- `databases/scripts/build-style-sheet3-htro.py` rewritten 935 lines / ~42KB. Three-part Python builder pattern preserved (defeats Edit-tool truncation cap).

**Audit results (live in Chrome at https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=3):**
- Layout: 2-pane shell, nav pane left 25% sticky internally scrollable, main pane right 75%. ✅
- Nav tree: 2 pillars + 5 groups + 19 elements + 70 RAs (auto-expand on focus). ✅
- Pill toggle button present in nav header (RHS). ✅
- 19 element banners + 19 element summary rows (one per element) ✅
- 34 RA summary rows (RAs with >1 CQ; ~half qualify) ✅
- 70 RA metric subtexts (word count / target / weight badge / R14, R5, R17 checks) ✅
- 85 `double` weight badges across page (8 named scopes propagating through descendants) ✅
- 182 CQ rows preserved from V2 ✅
- CQ column right-aligned ✅
- 183 anchor underlines + 936 sub-bullet underlines (R17 extended to subs) ✅
- IntersectionObserver-driven nav focus: "Required input forces?" auto-focused on load with its 3 RAs expanded. ✅

**Key V3 behavioural sample (as visible on first viewport):**
- "Required input forces?" element banner shows `double weight` badge ✅
- Element summary block lists 9 bullets, each formatted: `[RA name pill] [rating chip] [bold-italic text]` ✅
- First RA "Strong external change forces / tailwinds?" metric subtext: `234w / target 1925-3185w` `double` `word limit ✓ BP # ✓ highlighting density ✗18`
- The R17 `✗18` flags 18 anchors+subs out-of-band on underline density (Lorem rows tend to fail; HTRO content in this RA has 7 CQs of mixed real+Lorem).

**Stress-test conclusion:**
- File 360KB. Page height likely ~30+ viewport screens (V2 was 22; V3 adds element + RA summaries).
- Per-RA target band at ESA double-weight: 1925-3185w (= 7 CQs × per-CQ band 275-455w). Most RAs land below their target band — expected for a Lorem-heavy specimen, surfacing where real authoring is needed.

**Pending:**
- Richard's visual sign-off.
- Real authoring of element + RA summary content for HTRO (Lorem placeholders currently).
- Possible iteration on metric subtext density / weight badge placement.

---

## 30-Apr-26 ~05:50 UK — MEMO SHEET 3 SPECIMEN V2 (full new-taxonomy stress test)

**Session:** SA role, EXECUTION mode. Continuation of Sheet 3 visual style test. Expanding from 19-CQ HTRO subset to **full new-taxonomy scope** (70 RAs / 182 CQs across both pillars).

**Brief items in flight:**
1. Column proportion change: RA 10% / CQ 17% / Rating 6% / A&J 67% (left 1/3 vs right 2/3).
2. Underline 10-20% of anchor bullet body — load-bearing words.
3. IAJA tags `[J]/[A]/[I]` as inline suffix at end of every bullet.
4. **No em-dashes (`—`) anywhere** — replace with `: ` (colon-space). Locked as new rule R20.
5. **No trailing period** at end of any bullet — strip last `.` if present. Locked as new rule R21.
6. Remove divider bar between CQ rows within same RA (keep between RA groups).
7. **Expand specimen to full new-taxonomy scope** — every RA + CQ in both pillars (IC first, BB below). Lorem-Ipsum at matched density (~80w/CQ row) for non-HTRO entries.

**Files to touch:**
- `databases/scripts/build-style-sheet3-htro.py` — major expansion; walks pillar-tree-canonical.json.
- `databases/memo-style-sheet3-htro.html` — regenerated.
- `databases/memo-view-formatting-principles.md` — adds R20 + R21.
- `memory/skills/memo-view-formatting/SKILL.md` — mirrors R20 + R21.

**HTRO content mapping (existing 19 CQs):**
- IC element 1 "Required input forces?" — 7 CQs from IC#2 family in HTRO ESA memo.
- IC element 2 "Required financial outputs?" — 12 CQs from IC#1 family in HTRO ESA memo.
- All other 163 CQ rows = Lorem-Ipsum at matched density.

**New formatting rules (R20, R21) being locked into doctrine:**
- R20: No em-dashes (`—`) in any bullet text. Use `: ` (colon-space) for verdict→evidence joins.
- R21: No trailing period at end of any bullet. Strip last `.` if present. Internal periods kept. `?` and `!` untouched.

**Backup planned:** `.bak-pre-v2-{ts}` before file mutation.

**Live audit URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=2 (commit pushed 30-Apr-26 ~05:50 UK).

**Live audit results in Chrome:**
- 2 pillar banners + 5 group banners + 19 element banners + 182 CQ rows ✅
- 182 [J] suffixes + 263 [A] + 240 [I] = 685 IAJA tags ✅
- 183 underline spans across 182 anchor bullets ✅
- 0 em-dashes in rendered HTML ✅
- 0 trailing periods on any bullet ✅
- Page height 20,049 px = ~22 viewport screens (at 911px viewport)
- File size 152 KB
- Visual: column 1/3 + 2/3 working, IAJA tags coloured (J=purple, A=blue, I=grey) inline at end of each bullet, no horizontal divider lines between CQs within same RA group (zebra fill alone separates), banner row hierarchy clear (purple pillar, green group, cream element)

**Stress-test conclusion:** Full memo at Sheet 3 V2 density = ~75-80 standard pages (~22 viewport screens). At ~80w per CQ row × 182 rows = ~14,500w of A&J text alone. Provides reference baseline for whether to compress further or accept this density.

**Files touched (final state):**
- `databases/memo-style-sheet3-htro.html` (152,270 bytes)
- `databases/scripts/build-style-sheet3-htro.py` (rewritten, 31,283 bytes)
- `databases/memo-view-formatting-principles.md` (R20 + R21 added in §IV.E)
- `memory/skills/memo-view-formatting/SKILL.md` (R20 + R21 in pre-flight checklist + anti-patterns)
- `memory/projects/ratings-dashboard/session-log-29apr26-sheet3-style-test.md` (Round 6 narrative)

**Pre-write backups (all 4 retained):**
- `.bak-pre-v2-20260430-054114` on memo HTML, build script, principles, SKILL.md
- `transcripts/2026-04-30-0552-FULL-BACKUP/` (full backup folder)

**Standing rules in force:**
- Quality > speed.
- Pre-write snapshot mandatory.
- Edit tool truncation cap → use Python build script (struck again this session at line 645 of build-style-sheet3-htro.py; recovered via Python tail rewrite).
- Chrome MCP file:// rewrite blocked → GitHub Pages workflow used.

**Pending:**
- Richard's visual sign-off on V2.
- Iteration on density or rule choices if needed.

---

## 30-Apr-26 ~05:45 UK — PILLAR TREE V9 (tier spacing + BB groups standard colour + G2 rename)

**Session:** SA role, EXECUTION mode. V8 → V9 (in-place patch).

**Brief items shipped:**
1. **Tier-aware vertical spacing** between RAs (6px each) and between Elements (10px each). CQs stay tight (2px). Mechanism: data-tier attribute threaded through renderer; CSS targets `.v-drop[data-tier="element"]`, `.v-drop[data-tier="ra"]`, `.v-drop[data-tier="cq"]` separately.
2. **BB groups reverted to standard mint colour.** Stripped `_group_class: "gc-positive-fit"` from G2 and `gc-negative-fit` from G4 in TREE. All 5 BB groups now share default `.pill-group` background (mint #E1F5EE). Element colours INSIDE groups preserved (Quality elements stay mint, Simplicity/Acceptable elements stay yellow, Unacceptable/Riskiness elements stay rose).
3. **BB G2 renamed** "Case fit" → "Case simplicity". `group_short` updated to "Simplicity".

**Implementation:** `outputs/build_v9.py` — Python in-place patcher (no rebuild needed). Uses `re.sub` to find the 3 v-drop emission points in JS and add `data-tier="..."` per call site. Uses JSON parse/write for the TREE mutations.

**File:** `databases/pillar-tree-new-taxonomy.html` (39,607 bytes). Backup: `.bak-pre-v9-20260430-052739`.

**Live audit URL:** https://vfhqi.github.io/dashboards/pillar-tree-v6.html?v=9

**Audit results (live in Chrome at "+ Core questions" depth):**
- 5 BB groups all have `pill pill-group` class (no gc-* override) and identical mint background `rgb(225, 245, 238)` ✅
- G2 reads "Case simplicity" / short "Simplicity" ✅
- Tier counts: 19 v-drop[data-tier=ra] + 5 v-drop[data-tier=element] + 70 v-drop[data-tier=cq] ✅
- Visual: RAs in Pillar 1 elements have visible breathing room between them; BB elements within their groups have wider gaps; CQ rows under each RA stay tight as before.
- Body class still `len-long`, "Long" button active ✅.

**Pending:**
- Richard's visual sign-off.
- Iteration on spacing values (6/10/2 px) if still feels too tight or too loose.

---

## 30-Apr-26 ~05:30 UK — PILLAR TREE V8 (indented vertical CQs in Pillar 1, ? on all labels, default Long)

**Session:** SA role, EXECUTION mode. V7 → V8 (correction round).

**Brief items shipped:**
1. **Pillar 1 CQ layout corrected** — V7 misread the image; built horizontal-chip-strip. V8 correct: CQs vertically stacked under each RA, but indented so the CQ column starts past the RA1 badge (in the column where the RA's text begins). Implemented via new `.v-drop.v-drop-indent` CSS variant — `padding-left:36px`, rail at `left:28px`, arms 8px stubs. Pillar 2 keeps standard `.v-drop`.
2. **Question marks** appended to every RA and CQ label (long + short forms) across both pillars where missing. Build script `build_v8_part2.py` walks TREE and idempotently appends `?`. 70 RAs + 182 CQs swept.
3. **Default Long view** — `currentLen = "long"` on init; body class `len-long`; "Long" button rendered with `.active` class.

**File:** `databases/pillar-tree-new-taxonomy.html` (39,352 bytes). Backup: `.bak-pre-v8-20260430-051841`.

**Live audit URL:** https://vfhqi.github.io/dashboards/pillar-tree-v6.html?v=8

**Audit results (live in Chrome):**
- Title V8 ✅. Body class `len-long` ✅. Long button active ✅. 2 pillar sections ✅.
- 18 `.v-drop-indent` containers in Pillar 1 (3+8+7 RAs = 18) ✅. 73 `.v-drop` non-indent in Pillar 2 ✅.
- Visual matches the image Richard sent: RA pill on top row; CQs below stacked vertically; CQ column indented to start where the RA's text begins; vertical rail between RA-text-column and CQ column.
- Sample RA: "Strong external change forces / tailwinds?External change?" (long+short concatenated in textContent — both forms have `?`).
- Sample CQ: "Demand: changes in customer purchasing behaviour, volumes, pricing power, discou..." (long form, ends `?`).

**Pending:**
- Richard's visual sign-off.
- Iteration on indent depth if too tight/loose.

---

## 30-Apr-26 ~05:10 UK — PILLAR TREE V7 (stacked rollback + horizontal CQs in Pillar 1)

**Session:** SA role, EXECUTION mode. V6.1 → V7.

**Brief items shipped:**
1. **Rollback the two-screen split** — both pillars now stack on one page (V5-style) with a divider between them. Page scrolls if content exceeds viewport. Pillar toggle button group removed entirely from `head-m`.
2. **Horizontal CQ rendering in Pillar 1 (Investment Case Elements) only.** Each RA in Pillar 1 now renders its CQs as a horizontal chip strip to the right of the RA pill. Wraps to next line if row width is exceeded. Pillar 2 (Building Blocks) keeps the existing vertical CQ rendering unchanged.

**Implementation:**
- New CSS classes `.ra-with-h-cqs`, `.ra-label`, `.h-cq-strip`, `.h-cq-chip` for the horizontal layout.
- `renderAttr(attr, showCq, raNum, cqMode)` now takes a `cqMode` arg ("horizontal" or "vertical").
- `render()` passes `cqMode = "horizontal"` for Pillar 1 (s===0) and `"vertical"` for Pillar 2.
- `buildHeaderControls()` no longer emits the Pillar toggle.

**File:** `databases/pillar-tree-new-taxonomy.html` (40,500 bytes). Backup: `.bak-pre-v7-20260430-050551`.

**Live audit URL:** https://vfhqi.github.io/dashboards/pillar-tree-v6.html (commit pushed)

**Audit results (live in Chrome at depth = "+ Core questions"):**
- 2 pillar sections both rendered (rollback confirmed). ✅
- 0 pillar buttons (toggle removed). ✅
- 18 `.h-cq-strip` containers in Pillar 1 (one per RA across 3 elements: 3 RAs in Inputs, 8 in Outputs meta, 7 in Outputs line items = 18). ✅
- 36 `.h-cq-chip` chips at default depth — wait that count was BEFORE setting depth to cq. After: pillar1 has all RAs as h-cq-strip, pillar2 has 146 v-drop CQ pills. ✅
- Visual: Inputs RA1 "External change" shows 7 CQ chips wrapping to 7 lines (each with full CQ text); RA2 "Internal change" shows 5 CQs same pattern; RA3 "Robust base" shows 5 short CQ texts on fewer lines. Outputs (meta) RAs each show their 1-2 CQs inline neatly. Outputs (line items) RAs show "CQ1 TBD" inline.
- Pillar 2 still vertical (Quality, Risk, etc.) — unchanged from V6.1.

**Pending:**
- Richard's visual sign-off.
- Iteration on chip wrapping density (some RAs with 5-7 long CQ texts take many lines — could move to a smaller CQ font or different chip density if needed).

---

## 30-Apr-26 ~04:25 UK — PILLAR TREE V6 + V6.1 (two-screen split, no auto-fit, connector fix)

**Session:** SA role, EXECUTION mode. V5 → V6 → V6.1.

**Brief items shipped:**
1. Removed `autoFit()` font scaling (V5 made text unreadable). Pill sizes bumped above V4 baseline (pill 11px, element 11.5px, attr 10.5px, cq 9.5px).
2. Two-screen split via Pillar toggle in header (IC default, BB on click). Each pillar fills the viewport at readable type.
3. Header renames: "RAs" → "Required attributes", "CQs" → "Core questions", "Length" → "Item length". Pillar toggle added.
4. Connector fix: pillar stem now JS-positioned via `--stem-left` CSS var to match horizontal bar's leftmost X (was 22px off in V5/V6 initial). Robust init via double-rAF + 3 setTimeout fallbacks + document.fonts.ready.

**V6.1 file:** `databases/pillar-tree-new-taxonomy.html` (38,899 bytes). Backup: `.bak-pre-v6-20260430-040504`.

**Live audit URL:** https://vfhqi.github.io/dashboards/pillar-tree-v6.html (commit `74521ef`).

**Audit results (live in Chrome via Chrome MCP):**
- IC pillar: stem at 61.1px, bar.left at 60.4px (0.75px diff = sub-pixel aligned). 3 elements, single screen, no scroll.
- BB pillar: stem at 78.4px, bar.left at 77.7px (0.75px diff). 5 groups, all G→E drops clean, single screen, no scroll.
- Header buttons render with correct labels.

**Pending:**
- Richard's visual sign-off on the live URL.
- Any further iteration on font sizes (could go bigger if too small; could go smaller if cramped).
- Any tweaks to short-form labels or underline-word choices.

**Pattern flagged for SA log:**
- Write tool 28KB truncation cap confirmed again — applied edits got truncated mid-file. Recovery: restore from GitHub repo, rebuild via three-part Python.
- Chrome MCP file:// rewrite bug — workaround is GitHub Pages push.

---

## 30-Apr-26 ~03:35 UK — PILLAR TREE V5 REFORM (11-item brief)

**Session:** SA role, EXECUTION mode. V4 → V5 reform of `databases/pillar-tree-new-taxonomy.html`.

**Brief items (all shipped):**
1. Dynamic compress to fit one page no scroll — `autoFit()` with transform:scale, floor 0.55×.
2. Underline most important word(s) in each title/term — data-encoded `*_underline` arrays of word indices, rendered as `<u>` in long form.
3. New IC element "Required financial outputs (line items)?" with 7 RAs (Revenue, Margin, EPS, Cash returns, Multiple Δ, FCF, Leverage). CQs all TBD.
4. Length toggle (Short/Long) — paired `label-long` / `label-short` spans, body class `len-short` / `len-long` controls visibility.
5. Quality one colour — all 6 BQ elements share `ec-quality` (mint green).
6. Simplicity + Acceptable setups one colour — share `ec-positive-fit` (yellow-cream) + G2 group `gc-positive-fit`.
7. Acceptable + Unacceptable elements moved from Pillar 1 IC to Pillar 2 BB G2 ("Case fit" — new group name).
8. "Required fit with acceptable case setups?" → "Fit with acceptable case setups?" (Required prefix dropped).
9. Riskiness elements + Unacceptable element one colour — share `ec-negative-fit` (rose).
10. Vertical lines connect to pill — `fixChildRails()` measures pill bounding rect, sets per-child rail X/H via CSS vars; `fixHSpreadBars()` updated to use pill centres for endpoints.
11. Layout: legend → top-right (`#head-r`); depth + length toggles → top-middle (`#head-m`); title → top-left (`#head-l`).

**Final structure:**
- Pillar 1 (Inv. Case Elements): 3 elements (Inputs, Outputs meta, Outputs line items).
- Pillar 2 (Inv. Case Building Blocks): 5 groups (Momentum, Case fit, Quality, Riskiness, Optionality) × varying elements = 16 elements.
- Total: 19 elements / 70 RAs / 182 CQs (vs V4's 18/63/175).

**Build method:** Three-part Python builder used to defeat the Write tool's 28,070-byte truncation cap (file is 37,254 bytes). Backups: `.bak-pre-v5-20260430-033512`.

**Validation:**
- Static: scripts/styles balanced, ends `</html>`, TREE parses as JSON, zero unescaped `</` in script body.
- jsdom audit: 19 element pills with correct colour class distribution (6 quality + 2 positive-fit + 4 negative-fit), 5 BB group children, 3 IC element children, 27 underline tags across 26 long labels, 26/26 long/short label pairs, header controls in correct positions, no JS errors.
- LibreOffice: only renders static HTML (no JS) — confirmed structural intactness, not rendered tree.
- Chrome live audit: blocked. Chrome MCP `navigate` tool forcibly rewrites `file://` URLs to `https://file:///...` which fails. Geometric items (auto-fit, connector rails) NOT verified in real browser yet.

**Pending:**
- Richard's real-browser visual sign-off — opening file in Chrome/Edge.
- Iteration on short-form labels (Watson authored heuristically).
- Iteration on which words to underline per label (Watson chose one or two semantically-loaded words).
- Possible auto-fit floor adjustment if Richard's screen clips at 0.55×.

**Files touched:**
- `databases/pillar-tree-new-taxonomy.html` — V5 (37,254 bytes)
- `databases/pillar-tree-new-taxonomy.html.bak-pre-v5-20260430-033512` — V4 backup
- `memory/projects/ratings-dashboard/session-log-29apr26-pillar-tree-v5.md` — full session narrative
- `outputs/build_v5_part{1,2,3}.py`, `outputs/jsdom_audit_v5.js` — build + audit harness

---

## 29-Apr-26 EVE (later) — SHEET 3 VISUAL STYLE TEST — HTRO IC ELEMENTS

**Session:** SA role, EXECUTION mode. New deliverable: standalone HTML rendering HTRO ESA IC content in Sheet 3 visual style.

**What was delivered:**
1. **Standalone HTML specimen** — `databases/memo-style-sheet3-htro.html` (17,032 bytes). Renders two elements stacked: "Required input forces?" (7 CQs) and "Required financial outputs?" (12 CQs). 4-column table (RA italic / CQ bold / Rating chip / A&J bullets). Aptos typography. Zebra fills `#FAF8D2` / `#FDFCF1`. Sheet 3 rating-chip palette. Option-β minimal title bar.
2. **Re-runnable build script** — `databases/scripts/build-style-sheet3-htro.py` (~500 lines). Validates R14/R5/R4=10 + word band. Backs up to `.bak-pre-rebuild-{ts}` before each write. Idempotent.

**Decisions locked by Richard (29-Apr-26):**
- Q1 = C → R4 raised 7→10 **specimen-local only**, not system-wide.
- Q2 = B → minimal title bar (option β).
- Q3 = anchor + sub density Watson's judgement, optimised for clarity per row.
- Q4 = single HTML file, both elements stacked vertically.
- Sheet 3 bullet count + length = arbitrary placeholders. Locked length rules apply with **+50% on count and word budget; R14 hard cap 30w preserved unchanged**.

**+50% maths:** IC family ESA floor 390w × 1.5 = ~585w/element. Band 497-673w. Achieved: ELEM1 579w, ELEM2 544w. Both PASS.

**A&J source:** All 19 specimen CQs (7 input + 12 outputs) sourced from real HTRO ESA bullets in IC#1/IC#2 family blocks of `databases/memos/HTRO/ESA.json`. **No Lorem-Ipsum used.** Full real-content fidelity (override of original Q2-confirm — turned out unnecessary because HTRO has rich coverage). Compression from ~3,500w in memo to 585w/element.

**QA self-verification (LibreOffice → PDF → JPEG → Read on qa2-1..6.jpg):**
- Mapping coverage: 7/7 + 12/12 (100%).
- R14, R5, R4=10: all PASS.
- Word band: both PASS.
- Visual structural confirms: bullet structure, 4-col layout, RA rowspan, zebra fills, element separator.
- LibreOffice-only limitations (NOT browser issues): rating chip backgrounds stripped, italic stripped. Real-browser rendering will show them correctly.

**Pending:**
- Richard's real-browser visual sign-off (Q3).
- Element-content corrections (if any).
- Decision on whether to promote to live dashboard tab.
- GitHub push if signed off.

**Pattern note for SA:** **Three file-truncation events** during this build (script tail truncated at lines 433, 466, 477). Edit/Write tool may have a pathological interaction with em-dash + Aptos special chars. Recovered each time via Python in-place patching + AST validation. Adding to feedback log.

**Files touched:**
- `databases/memo-style-sheet3-htro.html` (NEW)
- `databases/scripts/build-style-sheet3-htro.py` (NEW)
- `databases/memo-style-sheet3-htro.html.bak-pre-rebuild-20260429-201153` (auto-backup)
- `databases/memo-style-sheet3-htro.html.bak-pre-rebuild-20260429-201253` (auto-backup)
- `memory/projects/ratings-dashboard/session-log-29apr26-sheet3-style-test.md` (NEW, full session narrative)

---

## 29-Apr-26 EVE — NEW TAXONOMY STANDALONE PILLAR TREE (from workbook NEW tab)

**Session:** SA role, EXECUTION mode. Pillar tree rebuild from new workbook taxonomy.

**What was delivered:**

1. **Updated `pillar-tree-canonical.json`** — rebuilt from `For Watson - Families - 29-Apr.xlsx` (NEW tab). 12 families, 41 TCs, 62 RAs, 165 CQs. Backup at `pillar-tree-canonical.json.bak-pre-29apr-update`.

2. **Standalone new-taxonomy pillar tree** — `databases/pillar-tree-new-taxonomy.html` (~23KB). Faithful to NEW tab's 3-tier structure (Element → Required Attribute → Core Question), NOT forced into old 4-tier schema. Two pillars: Investment Case Elements (IC) and Investment Case Building Blocks (BB).

**Layout features (all working):**
- **Numbering badges:** G1..G5 (groups), E1..En (elements, restarting per parent), RA1..RAn (attrs, per element), CQ1..CQn (CQs, per attr). Coloured badges: green/brown/blue/grey.
- **IC section:** elements run horizontally via `h-spread` (tree diagram connectors: vertical stem from pillar → horizontal bar → vertical drops to each element). Attrs/CQs drop vertically below each element.
- **BB section:** 5 groups run horizontally via `h-spread`. Elements drop vertically below each group via `v-drop`. Attrs/CQs drop vertically below each element.
- **Pillars stacked vertically** (IC on top, BB below) via `flex-direction:column`.
- **Depth controls:** Groups only / + Elements / + Attributes / + Core Questions.
- **Vertical-drop connector lines** from bottom of every pill at every tier (group→elem, elem→attr, attr→CQ).

**CSS patterns:**
- `.v-drop` / `.v-drop-child`: unified vertical-drop (left rail + horizontal arm)
- `.h-spread` / `.h-spread-child` / `.h-spread-stem`: horizontal tree layout with parent-to-bar stem + horizontal bar + child vertical drops
- `.num` / `.num-g` / `.num-e` / `.num-ra` / `.num-cq`: numbered badge pills
- `.block`: inline-flex column wrapper for each node + its children

**JS patterns:**
- `renderCQ(cq, num)`, `renderAttr(attr, showCq, raNum)`, `renderElement(elem, showAttr, showCq, elNum)` — all accept numbering params
- `render()` — splits IC (no named groups → h-spread elements) from BB (named groups → h-spread groups with v-drop elements below)
- All `</` escaped as `<\/` inside `<script>` block to prevent HTML parser breakage. `</script>` and `</body>` and `</html>` closing tags are NOT escaped.
- `esc()` function for XSS-safe text rendering

**Data source:** `new_tree_data.json` (session outputs) parsed from workbook. Also baked into HTML as `var TREE = [...]`.

**Key technical lessons this session:**
1. `</` inside `<script>` breaks HTML parsing — must escape as `<\/` (44 occurrences)
2. Edit tool truncates large files — use Python Write for files >800KB
3. Blanket `</` → `<\/` replacement must NOT touch the actual `</script>` closing tag — escape JS body BEFORE assembling into template
4. Minified JS (no linebreaks) causes statement boundary loss — always use properly formatted JS

**V3 refinements (same session, later):**
- **5 BB groups locked on one horizontal row**: `flex-wrap:nowrap` + `flex:1 1 0` + `min-width:0` — equal-width columns share available space.
- **Text wraps within columns**: `word-wrap:break-word` + `overflow-wrap:break-word` + `hyphens:auto` on pills. Long CQ/RA text (e.g. "2. Great, smart strategy...") wraps onto multiple lines within its column.
- **Dangling lines removed**: Old CSS `h-spread::before` (full-width bar) replaced with JS-positioned `h-spread-bar` elements drawn precisely between child connector points only. `v-drop` rails use CSS variable `--vd-rail-bottom` set by `fixVDropRails()` to end at last child's arm.
- **Pillar pill connected**: `.pillar-stem` (1.5px, 12px tall, #bbb) connects each pillar pill down to its h-spread children.
- **Connector lines refined**: 1.5px width, #bbb colour (lighter, cleaner than previous #333/2px).
- **`overflow-x:hidden`** on body as safety net.
- **Responsive font scaling**: `@media (max-width:1200px)` and `(max-width:820px)` step pill fonts down to maintain 5-column layout.
- **Pillar d