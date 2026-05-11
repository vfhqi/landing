# Ratings Dashboard — Locked Decisions
<!-- [W] Created 21-Apr-26. Append-only. Don't re-ask Richard anything in here. -->

## Build scope and approach

| # | Decision | Date | Source |
|---|----------|------|--------|
| 1 | Add stage toggle (Triaging / ESA / DD) to MEMO tab — toggle scopes the **entire memo**, not individual sections | 21-Apr-26 | "Q4 The toggle scopes the entire MEMO" |
| 2 | Default load on dashboard open = **highest available stage** for the stock | 21-Apr-26 | "Q5 Default load = highest stage" |
| 3 | If a stage has no content for a stock, **grey out the toggle/tab** (do not hide) | 21-Apr-26 | "Q6 = grey out the toggle/tab" |
| 4 | Save snapshots **as we go** to local backup folder. **No GitHub push during this build** — local only. | 21-Apr-26 | "just continually 'save up' versions as you go... I am not using GITHUB today ATM" |
| 5 | Sections C and D are treated as **"finished"** — ESA + DD versions for these sections must meet target word lengths | 21-Apr-26 | "we have 'worked on' Section C now and Section D (D is now 'finished'). So for every section finished, also ensure the ESA + DD version meets the target word length" |
| 6 | Use **Lorem-Ipsum** for placeholder content where live content doesn't exist | 21-Apr-26 | "Populate dummy placeholder text using LOREM IPSUM" |
| 7 | **Visual fidelity > formal validation.** If validators fight us on length, prioritise rendered visual length and look matching MEMOview | 21-Apr-26 | "I need them to visually be right length and formatting to sign off on it, so if that is hard, do that" |
| 8 | **MEMOview spec is authoritative for length.** v3.1 rules still apply for form (R5, R14, two-shape, anchor counts) | 21-Apr-26 | Inferred from "You have that in the excel file we are using as the guide" |
| 9 | **Six-section architecture: A/B/C/D/E/F.** Earlier dashboard's A/B/C/D was incomplete | 21-Apr-26 | MEMO view MASTER CORRECT sheet |
| 10 | **Words-per-page convention: 300.** Until Richard says otherwise | 21-Apr-26 | Working assumption pending explicit confirmation (flagged in open-questions.md) |
| 11 | **Source Excel: 21_04_2026 0709 file.** The 1152h file from 20-Apr was corrupt (Excel mid-save). Always use the most recent valid file matching the naming pattern. | 21-Apr-26 | "Use 'C:\Users\richb\Documents\COWORK\Files\NOT BACKED UP\RB downloads\RB excel tools\For Watson - APM Dashboard 4 views - 21_04_2026 0709.xlsx'" |

## Process discipline

| # | Decision | Date | Source |
|---|----------|------|--------|
| P1 | Read `state.md` first when resuming this project | 21-Apr-26 | Richard: "I tell you to save EVERYTHING so you do not lose ANY MEMORY" |
| P2 | Update `state.md` after every meaningful action (file written, build run, decision taken) — pre-empt compaction | 21-Apr-26 | Richard: "save to that folder regularly, to preempt the compacting" |
| P3 | Snapshot before touching live dashboard. Copy current dashboard.html + touched JSONs into `snapshots/{YYYY-MM-DD-HHMM}/` | 21-Apr-26 | Decision #4 |
| P4 | Don't ask Richard a question that's answered in `decisions.md` or `spec.md` | 21-Apr-26 | Richard: "You keep asking me the same questions every time" |
| P5 | If I think I need to ask a question, first check decisions.md, spec.md, open-questions.md. If still unsure, log to open-questions.md THEN ask. | 21-Apr-26 | Inferred from P4 |

## Memo header design system V5 (21-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| H1 | **Six-tier strictly-descending typographic hierarchy** for memo content. Tiers (size/weight): h1 28/700 → section 22/700 → subsection 18/700 → pillar 15.5/700 → family 14/700 → topic 13/600 → body 13/400 | 21-Apr-26 | V5 mockup approved |
| H2 | **Strictly descending size — every child smaller than parent.** Never violate this without explicit Richard authorisation. | 21-Apr-26 | "Why is P3 Business quality bigger than the levels above it" |
| H3 | **No UPPERCASE in headers, ever.** Sentence/title case throughout. Mixing UPPERCASE child below lowercase parent is forbidden. | 21-Apr-26 | "I dont like UPPER CASE nested below lower case - please change that. It confuses me" |
| H4 | **Family > Topic in weight (Option B).** Family is the dominant bucket header (700); topic is sub-evidence within it (600 muted). The natural instinct of "more nested = heavier" is wrong here. | 21-Apr-26 | Richard chose "Option B" twice |
| H5 | **Full badge system across all 5 nested tiers** (section/subsection/pillar/family/topic). Colour ramp: deep navy → mid blue → inverted light blue → pale grey → very pale grey. Visual depth tracks semantic depth. | 21-Apr-26 | "I like the badges a lot... Can we add badges to higher levels?" |
| H6 | **ID badge size matches its parent label height** (one step down, not four). No more "C.II.2 looks smaller than its title" mismatches. | 21-Apr-26 | "C.II.2 seems smaller than the title 'Fundamental Investment Case (P3+P4)'" |
| H7 | **V5 applies to memos only, NOT the entire dashboard.** Memos = prose-with-hierarchy register. Data tables = dense scanning surfaces. Different typographic registers; one system shouldn't rule both. | 21-Apr-26 | Richard accepted my NO answer to "even push to the entire dashboard?" |
| H8 | **Implementation: pure CSS, marker-wrapped, idempotent.** `databases/scripts/patch-header-hierarchy.py` is the only sanctioned mechanism. Markers `HEADER_HIERARCHY_CSS_START/END`. No JS renderer changes — all needed spans already exist. | 21-Apr-26 | Patch shipped at 11:03 UK |
| H9 | **Single global system applies across ALL memos, ALL six sections A–F, ALL stages.** CSS targets `.memo-*` classes globally so it scales automatically to NVTK, HTRO, and any future ticker. | 21-Apr-26 | "Push across the entire memo format, all sections" |

→ Full design spec: `memo-header-design-system-v5.md`

## Memo signposting — higher-intent doctrine (21-Apr-26)

These are the load-bearing rules. The memo's job is to make every analytical statement instantly traceable to the **Core Question / Required Attribute / Target Condition** it answers. Higher intent: Richard reads a bullet and knows in <1 second *why* he is reading it here-and-now. Without this, the APM's analytical work is wasted because the surface fails to telegraph the hierarchy.

| # | Decision | Date | Source |
|---|----------|------|--------|
| S1 | **Terminology relabel locked.** "QUESTIONS" → **CORE QUESTIONS** (CQs); "ATTRIBUTES" → **REQUIRED ATTRIBUTES** (RAs); "TARGET CONDITIONS" unchanged (TCs); "Required Attribute Families" (IC#1/2/3, BB#1–BB#8) unchanged. Sweep across SOPs, pillar detail JSONs, validator, dashboard ratings table, RESEARCHER templates. | 21-Apr-26 | Richard's higher-intent brief |
| S2 | **Two-layer fundamental architecture is the north star.** Pillar III = WHAT'S CHANGING (3× change AFs: IC#2 inputs, IC#3 setups, IC#1 outputs). Pillar IV = HOW BANKABLE (8 BB families). Both essential, neither sufficient. Plus I/II/V/VI as supporting pillars. Richard's priority order: A technical, B paradigm fit, C P3, D P4. | 21-Apr-26 | Richard's higher-intent brief |
| S3 | **Stage discipline.** Triaging = high-level analysis on every CQ + attempted RA/TC analysis. ESA = ingest ALL ESA RESEARCHER output, re-run every CQ + RA + TC at higher resolution. DD = same on DD RESEARCHER output, max depth, cross-references expected. Coverage is exhaustive at every stage; depth is gated by stage. | 21-Apr-26 | Richard's higher-intent brief |
| S4 | **Signposting is mandatory at parent-bullet level only.** Sub-bullets inherit context. Two patterns: **Pattern 1 prefix** (`**IC#1 CQ1 — Three-year triple ratchet step-up:** answer text...`) or **Pattern 2 embedded** (label inline as `**…**` markers). One pattern per sub-section, no mixing within a single `bullet_group`. | 21-Apr-26 | Richard's higher-intent brief |
| S5 | **Label form: rich.** `{Family}.{Type}{Number} — {Short label}` (e.g. `IC#1 CQ1 — Three-year triple ratchet step-up`). Short form `IC#1 CQ1` only for in-line cross-references. Long form only in C.I.1 ratings table. | 21-Apr-26 | Richard's Q1 answer: "Rich form" |
| S6 | **Visual treatment: demi-bold (font-weight 600).** Signpost label same colour as body, weight 600. Sits above body 400, below structural label 700. CSS class `.memo-signpost`. | 21-Apr-26 | Richard's Q2 answer: "Can you do semi/demi-bold?" |
| S7 | **JSON schema: optional `signpost` field on bullet items.** Fields: `level` (cq/ra/tc), `ref` (e.g. "IC#1.CQ1"), `label`, `style` (prefix/embedded), `synthesises` (optional array for compound signposts). Renderer auto-builds rich form. | 21-Apr-26 | Implementation plan |
| S8 | **Stage-flexed coverage rule (R16, validator).** Triaging: every CQ referenced (warning if breached). ESA: every CQ + RA + TC referenced (hard fail). DD: same as ESA + every parent bullet must have a signpost (hard fail). | 21-Apr-26 | Implementation plan |
| S9 | **Implementation order: SOPs before code, code before live data, live data before validator hardening.** Steps: 1 save proposal → 2 principles doc → 3 memo-formatting SKILL → 4 APM SKILL → 5 renderer patch → 6 relabel sweep → 7 NVTK IC#1 PoC → 8 validator. Snapshot before every live edit. | 21-Apr-26 | SA recommendation, Richard accepted |

→ Full proposal: `signposting-proposal.md`. Full principles (to be written): `memo-signposting-principles.md`.

## Universal naming rule (21-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| U1 | **Use full Excel column B + C titles, not shorthand, EVERYWHERE.** Applies to: JSON `title` fields, dashboard section headers, validator messages, mockup labels, build script comments, all Notion postings. | 21-Apr-26 | Richard: "Make this a universal rule for the naming of sections, please. Apply it everywhere." |
| U2 | **Canonical title map = `canonical-section-titles.md`** in project folder. Re-verify against live Excel when workbook unlocks; Excel wins on any diff. | 21-Apr-26 | Fallback while `21_04_2026 0709.xlsx` locked (38KB shadow visible) |
| U3 | **Display follows V5 typography.** Excel column C may be all-caps (e.g. "TECHNICAL STRENGTH (Pillar 1)"); rendered dashboard uses title case ("Technical Strength (Pillar 1)") to honour H3 (no UPPERCASE under lowercase). Underlying JSON title preserves Excel form verbatim. | 21-Apr-26 | Derivative of H3 |

## C.I integration from V3 (21-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| CI1 | **Default depth on load = TCs.** Five-button depth selector: Pillars / Families / TCs / Attributes / Questions. | 21-Apr-26 | Richard's Q-CI-1: "C" |
| CI2 | **Preserve V3 MAP-style pillar cards above the table.** At-a-glance pillar ratings, clickable to jump to C.II.N. | 21-Apr-26 | Richard's Q-CI-2: "Preserve that visual from V3" |
| CI3 | **Three stage columns rendered side-by-side in C.I** (Triaging / ESA / DD). C.I is the progress-across-stages view; memo-level stage toggle does not gate it. | 21-Apr-26 | Richard's Q-CI-3: "Yes" |
| CI4 | **Pillar name + card titles are clickable anchors** → scroll to matching C.II.N subsection. | 21-Apr-26 | Richard's Q-CI-4: "Your idea is good" |
| CI5 | **JUDGEMENTS and ANALYSIS columns are independently toggleable.** Both on by default. | 21-Apr-26 | Richard's Q-CI-5: "toggleable" |

→ Full plan: `ci-integration-plan.md`.

## Live-case invalidation thresholds — 10 INVALIDATION ACHs (21-Apr-26, renamed 22-Apr-26)

<!-- Renamed from D-INV-1 → 10 INVALIDATION ACHs on 22-Apr-26 per Richard. Old name was confusing; new name is the canonical reference everywhere. -->

Locked by Richard 21-Apr-26 19:43. **These 10 thresholds apply only while we own a case** — they are explicitly *different from* the screening thresholds used to assess new investments or re-investments. They live in **D.II.1** of every memo at every stage, and they are imprinted in the APM SOP as "live-case discipline."

Each is a one-strike rule. When triggered, APM escalates to Richard with a sell/trim recommendation.

| # | Name | Trigger condition |
|---|------|-------------------|
| 1 | **Top-line invalidation** | One probable/actual near-term revenue cut to SS/G caused by exogenous problem |
| 2 | **Cockroach invalidation** | One actual AND one probable, OR three probable/likely current/near-term problems (cause internal or exogenous; impact on profits or revenue) |
| 3 | **Ditherer invalidation** | Deterioration in operator assessment AND one or more current/near-term probable/actual problems (cause internal or exogenous; impact on profits or revenue) |
| 4 | **Cyclical invalidation** | SP underperformance of 15% or 3M FOLLOWED BY a plausible+ near-term revenue cut caused by threshold+ exogenous problem |
| 5 | **NT/MT one-two invalidation** | SP underperformance of 15% or 3M FOLLOWED BY any probable/actual near-term cut (cause internal or exogenous; impacting profits — revenue case is covered by #4) |
| 6 | **Wisdom of crowd invalidation** | SP underperformance of 15% or 3M FOLLOWED BY any plausible+ VF or actual SM threshold+ concerns re. mid/long-term growth rate, margins, SRCAs or predictability thereof |
| 7 | **Market catch-up with our existential concerns invalidation** | VF (not SM) plausible+ threshold+ concerns re. mid/long-term growth rate, margins, SRCAs or predictability thereof FOLLOWED BY SP underperformance of 15% or 3M |
| 8 | **Narrow frame invalidation** | Peerset underperformance of 15% or 3M FOLLOWED BY any actual cut/problem (cause internal or exogenous; impact on profits or revenue) |
| 9 | **SS EEG invalidation** | [2]% or greater SS EPS cuts AND SP underperformance of 15% or 3M (either order) |
| 10 | **Case outputs/attributes invalidation** | [8] or more case-output thresholds at D or F |

**Mirrored locations** (must stay in lockstep — single source of truth = this decision):
- `memory/skills/assistant-portfolio-manager/SKILL.md` — APM live-case discipline section
- `memory/skills/assistant-portfolio-manager/analysis-judgement-sop.md` (Stream 1, when authored) — invalidation gate
- `databases/memos/{TICKER}/{Stage}.json` — D.II.1 bullet group

When the rule text is updated, edit here first, then propagate to the three mirrored locations.

## RESEARCH STAGES tab (27-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| RS1 | **Tab name = "RESEARCH STAGES"**, placed in toolbar next to COLOUR in its own toolbar group with separator. | 27-Apr-26 | Richard confirmed spec |
| RS2 | **Show ALL tickers with any research** (55 tickers), not just active pipeline. Always visible, not filtered to dashboard-only. | 27-Apr-26 | Richard confirmed spec |
| RS3 | **23 query columns grouped by stage.** IG #1-3, Triaging #4-7, ESA #8-14, DD #15-19, Any #20-23. Standard queries show word count + Notion dot. Ad-hoc queries (#20-23) show short description. | 27-Apr-26 | Richard confirmed spec |
| RS4 | **APM memo columns (TRI/ESA/DD) + IN DASHBOARD flag.** Checkmarks for memo existence. | 27-Apr-26 | Richard confirmed spec |
| RS5 | **AUDIT column = SOP compliance.** PASS/FAIL based on whether completed queries have Notion postings. | 27-Apr-26 | Richard confirmed spec |
| RS6 | **NEXT ACTION column = short instruction (6-20 words)** with priority badge (high/medium/low). Backend JSON has detailed machine-readable instructions for Watson execution. | 27-Apr-26 | Richard confirmed spec |
| RS7 | **Implementation: idempotent marker-wrapped patcher** (`patch-coverage-tab.py`). 5 marker pairs: COVERAGE_CSS_V1, COVERAGE_BTN_V1, COVERAGE_BTN_V1_CONTAINER, COVERAGE_DATA_V1, COVERAGE_JS_V1. | 27-Apr-26 | SA decision |
| RS8 | **Data scanner** (`build-coverage-data.py`) handles 55+ tickers with varied folder naming conventions. Output: `coverage-data.json`. Re-run scanner then re-run patcher to refresh. | 27-Apr-26 | SA decision |
| RS9 | **Zero ES6.** `var` only, `function(){}` only, string concatenation only. iPad-safe. Consistent with all other dashboard JS. | 27-Apr-26 | Standing rule |

## 15-Minute Update + Save Cadence (28-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| C1 | **Watson sends Richard a progress update every ≤15 minutes during active build/work.** Concrete, evidence-based ("ran X, output is Y, next step is Z"), not aspirational. | 28-Apr-26 | Richard's standing instruction during D8 work |
| C2 | **Watson saves comprehensively to project files every ≤15 minutes** — state.md + log.md + relevant artefacts. | 28-Apr-26 | Same |
| C3 | **Each save is confirmed in writing to Richard** ("saved at HH:MM — state.md updated, log.md appended, X file written"). | 28-Apr-26 | Same |

This adds the long-missing structural enforcement to the anti-compaction protocol. The 5-minute save rule from `feedback_context_windows_sop.md` still applies (save immediately on decisions/corrections); the 15-minute cadence is the **mandatory floor**.

## Quality default — full visual parity for every stock (28-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| Q1 | **Every stock baked into the dashboard gets the same visual experience as NVTK.** Full 6-pillar drill-down, full CQ/RA/TC ladder inside P3 / P4 pillar cards, full SS Earnings Momentum data, full valuation data. No "cheap" / "summary-only" / "placeholder" treatments. If a stock can't get full parity right now, it doesn't get baked until it can. | 28-Apr-26 | Richard's correction on Option B proposal: "Stop being lazy. Aim to do very high quality work." |
| Q2 | **Speed is never the default tradeoff.** Quality and accuracy are the default. When estimating work, Watson presents the quality answer first; cheaper alternatives are only mentioned if Richard asks for tradeoffs. | 28-Apr-26 | Same correction |
| Q3 | **Test before presenting.** Watson runs the work end-to-end and verifies it works before bringing it to Richard. Self-verification is non-negotiable. | 28-Apr-26 | Same correction + standing "Do It Right" reform |

## Master Dashboard as primary data source (28-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| MD1 | **Master Dashboard is the primary data source for the Ratings Dashboard wherever the data exists there.** This applies to: P1 Technical Momentum (prices.json, filter-results.json, MM99 score, MA structure, RS), P5 SS Earnings Momentum (factset-ssem.json), P6 Valuation (factset-valuation.json), and any technical/screening data. **Logic: data congruity** — both dashboards must show the same numbers for the same stock at any point in time, or they'll silently disagree and erode trust. Locked 28-Apr-26 by Richard. | 28-Apr-26 | Richard's Q2 answer to Block 1 defect back-brief |
| MD2 | **Build pipeline reads from Master Dashboard data files, not from cached or hand-entered values.** When baking a new memo or rebuilding the Ratings Dashboard, the build script must pull live values from `master-dashboard/data/*.json`. No copy-paste of numbers between dashboards. | 28-Apr-26 | Derivative of MD1 |
| MD3 | **When Master Dashboard data is missing for a stock**, the Ratings Dashboard cell shows "—" with a tooltip "Not in Master Dashboard universe yet" rather than rendering a stale or fabricated value. APM judgement-only fields (P3 Fund Change, P4 Building Blocks, setup, fulcrum driver, recommendation) are exempt — those are authored, not pulled. | 28-Apr-26 | Derivative of MD1 |

## APM Analysis & Judgement SOP (28-Apr-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| AJ1 | **Authoring order: C.II → A → D → C.I → B → E → F.** Work order ≠ communication order. Analysis (C.II, A) first, then checks (D), then crystallise judgements (C.I), then summarise (B), then actions (E), then appendix (F). The reader sees B → A → C → D → E → F but APM writes in work order. | 28-Apr-26 | Richard's correction: "The author memo process is 1 READ, 2 ANALYSE, 3 FORM JUDGEMENTS, 4 PROPOSE ACTIONS. But for communication, the order is largely reversed." |
| AJ2 | **70% of Phase 2+3 effort on P3 (Fundamental Investment Case) and P4 (Investment Case Building Blocks).** The remaining 30% shared across P1/P2/P5/P6. These are supporting/formulaic pillars. | 28-Apr-26 | Richard: "70% of the time in Phase 2 and Phase 3 should be devoted to analysis of the FUNDAMENTAL INVESTMENT CASE and the INVESTMENT CASE BUILDING BLOCKS" |
| AJ3 | **Notion lookup for Richard's own notes is mandatory at all stages.** Before starting any A&J work, search Notion Stock Notes DB for the ticker. Read all pages titled "Case file" or "RNTS" plus any other Richard-authored notes (journal entries, pre-mortem, meeting notes). Exclude Watson-authored RESEARCHER output. Be creative in identifying Richard's own notes. | 28-Apr-26 | Richard: "Look for any other notes in Notion on the stock in question and read them, but only read the ones that are not Notion versions of local research files. In particular, look for notes with titles that include the terms 'Case file' and 'RNTS'." |
| AJ4 | **Opus model mandatory for A&J SOP execution.** No Sonnet, no Haiku. APM A&J is the highest-stakes analytical work Watson performs. | 28-Apr-26 | Richard: "Ensure it is done in Opus model." |
| AJ5 | **Creative, insightful, thoughtful analysis prioritised. Speed/convenience/comfort avoided.** Every bullet should make Richard think. Surface non-obvious connections, challenge consensus, identify what matters most and why. Formulaic observations waste Richard's time. | 28-Apr-26 | Richard: "prioritise creative, insightful, thoughtful analysis and judgement that is useful to me understanding the company and case and making investing judgements, and that speed/convenience/comfort should be avoided" |

→ Full SOP: `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` (updated 28-Apr-26)

## Standing global rules (apply here too)

- Backup discipline (auto-memory `feedback_dashboard_corruption_pattern.md`): validate dashboard structure after every edit (renderMinervini present, no var PB, ends `</html>`, scripts balanced)
- No Edit tool on files >800KB (auto-memory `feedback_edit_tool_truncation_bug.md`) — bash+Python only
- Edit tool ban tightened to >50KB on dashboard files per 27-Apr-26 build_dashboard.py truncation recurrence
- No bash heredoc with `!` in JS code (auto-memory `feedback_bash_heredoc_bang_escape.md`) — Write tool only
- **MD1/MD2/MD3 above** — Master Dashboard is primary data source; data congruity is non-negotiable

## Rebuild RS Tab Integration (5-May-26)

| # | Decision | Date | Source |
|---|----------|------|--------|
| RI1 | **Transplant method: fenced-section splice, not full file replace.** Only 2 of 6 fenced sections differ between live and rebuild (LIFECYCLE_V1_CSS = new, COVERAGE_JS = expanded). CSS, BTN, CONTAINER are identical. Splice the 2 differing sections + regenerate DATA. Preserves all non-RS-tab code untouched. | 5-May-26 | Watson analysis of fenced-section diffs |
| RI2 | **Source for transplant: v21-final backup, not live preview URL.** Fenced sections verified byte-identical between `backups/2026-05-04T115606Z-handoff-final-state/dashboard-v21-final.html` and the preview URL. Local file used to avoid download complications. | 5-May-26 | Watson verification via Chrome MCP diff |
| RI3 | **GNG CHECKS + MEMO page functionality to be built fresh post-integration.** Rebuild contains non-functional stubs for these — Richard prefers a clean rebuild rather than carrying stubs. | 5-May-26 | Richard: "we will need to create the GNG and MEMO page functionality AFTER we complete our current objective... I would prefer to rebuild fresh" |
| RI4 | **Daily-push pipeline: DATA-ONLY patcher replaces V5.** `patch-coverage-tab.py` V5 archived. New `patch-coverage-data-only.py` V1 replaces ONLY the COVERAGE_DATA_V1 section. Running V5 would DESTROY transplanted lifecycle JS. | 5-May-26 | Watson: V5 strips ALL fences and rebuilds with old JS code |
| RI5 | **Test-then-promote deployment pattern.** Deploy to `test/` first, run Chrome MCP quality gate (11 checks), get Richard's sign-off, then promote to live root. | 5-May-26 | Watson plan, approved by Richard |
| RI6 | **GitHub repo rename from `dashboards` to `ratings` raised but not actioned.** Richard asked about feasibility 5-May-26. Deferred — would require updating all hardcoded URLs (GitHub Pages, bookmarks, daily-push scripts). | 5-May-26 | Richard: "How easy is it to change the github directory for this project from DASHBOARDS to RATINGS?" |

## Pipeline protection rules (post-rebuild, 5-May-26)

| # | Rule | Rationale |
|---|------|-----------|
| PP1 | **NEVER run `patch-coverage-tab.py` (V5) on the live dashboard.** It will overwrite LIFECYCLE_V1_CSS and COVERAGE_JS with old V5 code. Archived copy preserved for reference only. | V5 strips ALL fences and rebuilds from scratch |
| PP2 | **Use `patch-coverage-data-only.py` for all daily data pushes.** Touches ONLY COVERAGE_DATA_V1 section. Has 5 built-in validation checks + read-back verification. | Preserves transplanted CSS/JS |
| PP3 | **`build-coverage-data-v2.py` is safe to run anytime.** It generates `coverage-data.json` independently of dashboard structure. | Data builder is decoupled from renderer |
| PP4 | **Before any JS edit to the RS tab, verify LIFECYCLE_V1_CSS_START and COVERAGE_JS_V1_START markers are intact.** These are the transplanted sections. | Guard against accidental overwrite |
