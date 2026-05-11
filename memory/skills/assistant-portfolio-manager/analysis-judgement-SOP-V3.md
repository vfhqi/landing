# APM Analysis & Judgement SOP — v3.0 (V3 framework, 8-May-26)

> **V3 vocabulary + framework note (8-May-26):** This SOP is patched for the V3 framework (`STREAM-A-COMPREHENSIVE-V2.html`). Vocabulary mapping for everything below:
> - **CQ (Core Question)** → **Sub-question within an Element** (no longer first-class)
> - **RA (Required Attribute)** → **A&J Element (E#, where # = E1–E32)**
> - **TC (Target Condition) within a family** → **Group rating (G1–G5 in Pillar II; G6/G7/G8 in Pillar III)**
> - **Stage TC** → qualitative alignment language, NOT rated [W4]
> - **IC#1 / IC#2 / IC#3** → **Pillar I (Case change elements)** — three elements: E1, E2, E3
> - **BB#1–BB#8** → **Pillar II (Case building blocks)** — five groups (G1–G5), 14 elements (E4–E20)
> - **Pillar III** in old vocabulary referred to "What's Changing" — in V3, Pillar III is now Investment case components (Position playbook + Monitoring plan + Key drivers); the old "What's Changing" maps to V3 Pillar I + Pillar II G1
> - **6-stage funnel:** I Generation/screening · II Filtering out · III Triaging · IV ESA · V DD · VI Live (replaces old IG/Triage/ESA/DD)
>
> **Key V3 changes:**
> - **Phase 2 execution mechanism:** Old "pillar-by-pillar analysis" replaced by **per-row authoring matrix walk** (Stream A § 9). APM walks the matrix at the current stage's column and produces content per cell instructions.
> - **Authoring order:** Old "C.II → A → D → C.I → B → E → F" replaced by **stage-row-walking** (top-to-bottom of matrix at the current stage).
> - **70/30 effort allocation rule retires.** The cell-instruction depth labels (First/Second/Third pass; light/solid/solid; robust) encode effort per-row, per-stage.
> - **Word targets retire.** Replaced by cell-instruction depth labels.
> - **Master ratings + Pillar ratings + Group ratings + Element ratings** all explicitly produced by APM (D2 hierarchical rating layer).
> - **Stage gates are NOT programmatic** [W4]. TCs are qualitative alignment; APM judgement is the gate.
>
> The phase architecture (Phase 0 / 1 / 2 / 3 / 4 / 4.5 / 4.6 / 5) and operational machinery (GNG CHECKS, calibration log, Wisdom Library bookend, cohort hot wash, judgement-importance-weighted escalation) all survive intact. The 10 INVALIDATION ACHs preserved verbatim.

---

# APM Analysis & Judgement SOP — v2.4.1 (legacy header preserved for context)

<!--
[W] Created 21-Apr-26 21:55 UK. Major rewrite 03-May-26 06:50 UK — v2.2.

VERSION HISTORY (most recent first):
  v2.4.1 (04-May-26 LATER): Terminology + dashboard integration patch (no behavioural change).
       - Phase 4.6 "cohort wash-up" renamed to "cohort hot wash" (Richard's instruction)
       - "Cohort cycle" renamed to "Cohort-centric IAJA cycle" (Richard's instruction)
       - Phase 0.0 status check now reads from RESEARCH STAGES dashboard data feed (single source
         of truth) — NOT from manifest text. Manifest = cohort definition; dashboard = state.
       - Phase 4.6 surfacing requirement added: cohort hot wash MUST surface as dedicated
         {cohort × stage} row on RESEARCH STAGES tab. Schema spec at
         databases/research-stages-cohort-spec.md (NEW; SA-owned implementation when current
         RESEARCH STAGES WIP completes).
       - G17 reworded for new terminology + surfacing requirement.
       Backup: analysis-judgement-SOP.md.bak-pre-v11-20260504

  v2.4 (04-May-26): COHORT LAYER. 3 amendments — A16 NEW Phase 0.0 (cohort manifest pre-load,
       sits BEFORE Phase 0.1) + A17 NEW Phase 4.6 (cohort wash-up, sits AFTER Phase 4.5,
       runs ONCE per sub-cohort) + A18 NEW Quality Gate G17 (cohort wash-up complete
       before session close when cohort manifest exists). Backup:
       analysis-judgement-SOP.md.bak-pre-cohort-20260504

       v2.4 amendments:
         A16  Phase 0.0 — Cohort manifest pre-load (NEW; sits BEFORE Phase 0.1)
         A17  Phase 4.6 — Cohort wash-up (NEW; sits AFTER Phase 4.5; runs once per sub-cohort)
         A18  Quality Gate G17 — Cohort wash-up complete (NEW; conditional on cohort manifest existing)

       Cross-role lock-step: RESEARCHER SKILL-V2.13 (Rule #38 cohort manifest pre-consult)
       + session-handoff SKILL Step 5.5.0 (cohort presence check) + Wisdom Library SKILL §5.5
       (cohort-driven tier promotion). Master cohort SOP at
       `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0 — read first
       before exercising any v2.4 amendment. Cohort layer is ADDITIVE. When no cohort
       manifest exists for the active ticker, all v2.3.1 behaviour is preserved exactly.

  v2.3.1 (03-May-26 PM, later): trigger-phrase binding to master brief template at
       `memory/staging/apm-aj-brief-template.md`. Phrasings like "run the hotwash related
       to integrating lessons into the wisdom library" now route to the template at
       Phase 4.5 + Phase 0.2 cross-ref. No SOP behaviour change — convenience layer only.

  v2.3 (03-May-26 PM): Wisdom Library bookend pattern. 2 amendments — A14 Phase 0 extension
       (Wisdom Library consult alongside RESEARCHER coverage check) + A15 NEW Phase 4.5
       (Hot Wash + Wisdom Library survey after Phase 4 ships). Backup:
       analysis-judgement-SOP.md.bak-pre-v23-bookend-20260503

       v2.3 amendments:
         A14  Phase 0 — Wisdom Library consult (NEW; alongside existing RESEARCHER coverage check)
         A15  Phase 4.5 — Hot Wash + Wisdom Library survey (NEW phase between Phase 4 and Phase 5)

       Cross-role lock-step: RESEARCHER SKILL-V2 + session-handoff SKILL V2 updated same date
       to enforce Wisdom Library bookend at start (RESEARCHER pre-query consult) and end
       (session-handoff Step 5.5 hot wash + survey).

  v2.2 (03-May-26): integrates 13 amendments — 6 from analysis-judgement-SOP-review-2026-05-01.md
       + 7 from 03-May-26 hot wash on EKTA/HTRO/PRY/COTN-CH production run.
       Backup: analysis-judgement-SOP.md.bak-pre-v22-integration-20260503

       v2.2 amendments integrated:
         A1  Coupling to STAGE PROGRESSION SOP (header + Phase 5 hook)
         A2  Phase 0 — Pre-flight RESEARCHER coverage check (NEW)
         A3  Phase 2 — Weight-driven effort allocation (NEW sub-section after 70/30 rule)
         A4  Phase 2 — Per-section word targets visible inline (memo SKILL extension)
         A5  Phase 2 — Signpost.level case-sensitivity reference + family extension to P1/P2/P5/P6
         A6  Phase 2 — R14 30w cap clarification — signpost-label exemption
         A7  Phase 2.5 — In-line validator dry-run (NEW phase between Phase 2 and 3)
         A8  Phase 3 — Judgement-importance-weighted escalation (NEW sub-section)
         A9  Phase 3 — R4 cohort-flag exemption for D.II.1
         A10 Phase 4 — GNG CHECKS (NEW sub-section, mandatory G13 quality gate)
         A11 Phase 4 — Calibration log (NEW sub-section, paired with GNG CHECKS)
         A12 Phase 4 — Handoff to Step 3 of STAGE PROGRESSION SOP (NEW sub-section)
         A13 Phase 5 — Case Components prep (NEW phase, conditional, forward-hook only)

       Validator updated in lock-step (same date):
         databases/scripts/validate-memo.py (R4 cohort flag; R14 signpost exemption;
           R16 case-insensitive level + extended family set; new R29 GNG CHECKS gate)

  v2.1 (28-Apr-26 EVE): R18 5-grade rule HARD; mandatory content scaffolds for flat pillars;
       bullet architecture (parent verdict + sub evidence); quality gates 10-12.
  v2.0 (28-Apr-26 PM): Notion lookup for Richard's voice notes; 70/30 P3+P4 time split;
       authoring order C.II→A→D→C.I→B→E→F; Opus mandatory.
  v1.0 (21-Apr-26): initial SOP.
-->

## Where this SOP sits in the STAGE PROGRESSION SOP [A1, NEW v2.2]

This SOP is **Step 2 of the 4-step STAGE PROGRESSION SOP** (`memory/skills/stage-progression/SKILL.md`). The four steps:

1. **Brief** — Richard briefs APM on the stock at the stage (back-briefed via Mission Command + 3 Gaps per CLAUDE.md Operating Method).
2. **APM A&J** — THIS SOP. APM produces the memo + GNG CHECKS artefact.
3. **Richard's review** — Richard reads the memo + GNG CHECKS; COS chases via morning routine within 24-48h.
4. **Weekly review meeting (chat-async, batch, Friday PM UK)** — Richard + APM debate; case-level decision = progress / park / kill.

APM's deliverable to Step 3 is the memo (Notion + dashboard) AND the GNG CHECKS (separate Notion page). APM's role in Step 4 is to defend/adapt the analysis, log calibration, and capture the meeting decision (with COS verifying + filing).

**Case-level decisions are APM RECOMMENDATION only.** Richard decides at Step 4. APM never finalises the progress/park/kill decision unilaterally — see §Phase 3 Judgement-importance-weighted escalation below.

---

## Purpose

This SOP governs APM work during the **memo authoring stages** of the 6-stage funnel — Triaging, ESA, and DD. It takes RESEARCHER output as Information, produces Analysis + Judgement, and writes both to:
- **Notion Stock Notes DB** (Richard's primary reading interface — live)
- **`databases/memos/{TICKER}/{Stage}.json`** (feeds the live IC Ratings Dashboard — structural)

This complements SKILL.md (which covers entry/exit/sizing/portfolio decisions — the **post-memo** APM decisions).

## ★ Model requirement: Opus ★

**This SOP MUST be executed in Opus model.** APM Analysis & Judgement is the highest-stakes analytical work Watson performs — it directly informs Richard's investment decisions. Sonnet and Haiku lack the nuance, creativity, and depth of reasoning required for defensible investment judgement. If the current session is not running Opus, escalate to Richard before proceeding.

## ★ Analytical quality mandate ★

**Prioritise creative, insightful, thoughtful analysis and judgement that is useful to Richard in understanding the company, the case, and making investing judgements.** Every bullet, every rating, every synthesis paragraph should make Richard think — surface non-obvious connections, challenge consensus narratives, identify what matters most and why. Speed, convenience, and comfort are explicitly deprioritised. If a section feels easy to write, Watson is probably not thinking hard enough. The test: would Richard learn something from reading this that he couldn't get from a sell-side note?

## Scope by stage [V3 — matrix-driven, 8-May-26]

**Old word-target system retires.** Depth at each stage is now encoded by the per-row authoring matrix in `STREAM-A-COMPREHENSIVE-V2.html` § 9. APM walks the matrix at the current stage's column and produces content per the cell instructions.

| Stage | Roman | What APM produces | Output verdict |
|---|---|---|---|
| Generation / screening | I | No A&J memo. Confirm E4 technical momentum. RR1+RR2 are RESEARCHER deliverables. | Park or proceed to Filter |
| Filtering out *(NEW)* | II | No A&J memo. Filter out on E5 thematic fit + E11 VC dynamics per Funnel view. RR3+RR4 are RESEARCHER deliverables. | Park or proceed to Triage |
| Triaging *(first A&J pass)* | III | First A&J memo. Walks matrix column III. In scope: rows 48 (exec summary 3rd pass), 49 (master ratings 1st pass — light), Pillar II G1+G2+G3+G4 group ratings (1st pass — light), E1, E5 (2nd pass), E7, E8, E11 (2nd pass). | Go / Park to ESA |
| ESA *(second A&J pass)* | IV | Memo deepens at column IV. Pillar I solidifies (E1 2nd, E2+E3 1st pass). Pillar II Core philosophy fills in (E9–E13 1st pass). Pillar II Risk transmission E18+E19 1st — light. Pillar III begins: G6 Position playbook, G7 Upstream, G8 Downstream all 1st — light. | Go / Park to DD |
| Deep dive *(third A&J pass)* | V | Memo at robust depth. Risk attributes (E15–E17) **first authored at DD only**. E6 SS earnings momentum 1st pass at DD. Pillar III deepens to 2nd pass — solid. | Go / Park / Size |
| Live | VI | No new A&J memo authoring; instead, **Stage VI Live operating system**: weekly RR23 monitoring + monthly review meeting + 10 INVALIDATION ACHs as exit triggers. Pillar III evolves to 3rd pass — robust. | Hold / Trim / Exit |

**Stage gates are NOT programmatic** [W4]. TCs are qualitative alignment language; APM does NOT rate the TCs. Go/no-go = combination of element/group/pillar/master ratings + integrated APM judgement.

Validator updated separately in Stream C2 (memo schema work).

## Inputs required before starting

1. **Researcher output** — local-first lookup per SKILL.md §3.5. Required:
   - At Triaging: `02-CF` (Change Forces), `03-TM` (Technical Momentum), `04-ET` (Earnings Trends), `05-ED` (Earnings Delivery), `07-KD` (Watson KD Assessment) at minimum.
   - At ESA: everything above + `08-BM` (Business Model / Sector Primer), `10-SS` (Sell-Side Analysis), `13-KQ` (Key Questions).
   - At DD: everything above + deep-dive queries RESEARCHER has run per the stage.

2. **Master Dashboard data** — read `master-dashboard/data/prices.json` + `filter-results.json` + `factset-ssem.json` + `factset-valuation.json` for the stock. These are auto-refreshed nightly — always check directly, never ask Richard if data exists. Provides:
   - **P1 (Technical Momentum):** MM99 score (11-test), filter qualification stages, RS excess returns, MA levels — formulaic foundation for Pillar I rating.
   - **P5 (SS Earnings Momentum):** revision %, momentum count. Supplementary quantitative context (AlphaSense and RESEARCHER output are the primary sources for earnings analysis).
   - **P6 (Valuation):** P/E, percentiles. Supplementary quantitative context.
   - **Entry timing context:** Filter qualification stage (Early/Late/Capital) informs trade-type readiness in §E.II actions.
   - Where Master Dashboard data and RESEARCHER output show incongruities, APM uses judgement to synthesise both in the Analysis + Judgement.

3. **Richard's own Notion notes on the stock** — MANDATORY at all stages. Search Notion Stock Notes DB for the ticker and read any pages that are NOT Notion-posted versions of local RESEARCHER files. Prioritise:
   - **"Case file"** — Richard's own case construction and thesis framing
   - **"RNTS"** — Richard's notes (earnings reactions, qualitative observations, thesis evolution)
   - Also: journal entries, pre-mortem notes, meeting notes, thematic annotations — anything in Richard's own voice. High-signal calibration input. APM analysis that ignores Richard's own framing is working blind.
   - **Exclude:** Pages whose titles match RESEARCHER query patterns — already in input #1.

4. **Canonical frameworks** — load from CLAUDE.md, pipeline.md, investment-strategy.md, risk-management-lessons.md, stock-archetypes.md.

5. **Dashboard pillar tree** — `memory/projects/ratings-dashboard/spec.md` + canonical pillar tree reference for IC#/BB# signposting.

## ☆ Proactive RESEARCHER briefing — APM's right and duty ☆

**If the required RESEARCHER inputs are missing or thin, APM does NOT proceed without them.** APM briefs the RESEARCHER sub-agent to run the AS + Claude RESEARCH SOP for the missing queries at the current stage, then resumes analysis once content lands.

**Briefing format:**
```
RESEARCHER brief:
  ticker: {TICKER}
  stage: {IG | Triaging | ESA | DD}
  queries needed: [list, e.g. 02-CF, 03-TM, 10-SS]
  why: {one-line — what APM judgement depends on this content}
  source protocol: dual-source (Claude [C] + AlphaSense [AS]) unless stage SOP says otherwise
  post to: Notion Stock Notes + local Files/{TICKER}/{STAGE}/{QUERY}/
```

If time-limited, APM can: queue to `memory/staging/researcher-queue.md`; proceed with partial analysis; flag coverage gaps in D.II.

## ★ Authoring order — Stage-Row-Walking [V3, 8-May-26 — REPLACES "C.II → A → D → C.I → B → E → F"] ★

**Old work-order vs communication-order distinction retires.** Under V3, APM writes the memo by **walking the rows of the per-row authoring matrix top-to-bottom at the current stage's column**. The matrix IS the SOP (`STREAM-A-COMPREHENSIVE-V2.html` § 9).

**At any given stage, APM walks the matrix in row order:**

| Row order | Topic | Cell instruction tells APM... |
|---|---|---|
| 1 | Row 48 — Executive summary judgement | Which pass to write (1st/2nd/3rd/4th/5th) |
| 2 | Row 49 — Master ratings (the 6) | Light/solid/robust depth (or "No" at I/II) |
| 3 | Pillar I rows (51–54) — E1, E2, E3 | When in scope, what depth |
| 4 | Pillar II rows (56–83) — G1–G5 groups + E4–E20 elements | Per cell |
| 5 | Pillar III rows (90–125) — G6 Position playbook, G7 Upstream, G8 Downstream + E21+E22 | Per cell + tabular spec § 7a |

**For each row at the current stage's column:**
- **Non-blank cell** → produce content per cell instruction (First/Second/Third pass; light/solid/robust)
- **Blank cell** → n.a. at this stage; skip
- **[no change]** → carry forward prior content unchanged

**Reading vs writing order are now the same.** Reader scans top-down (BLUF first via row 48 exec summary, then master ratings via row 49, then deeper into pillars/elements). APM writes in the same order the reader reads. The old "work order ≠ communication order" gymnastics retire.

**The "broadly" caveat from Triage onwards (Stream A § 11):** rows 48 + 49 are produced *light, full-case* even when most pillars are still under-informed. They are the *top of the matrix*, not a separate stream. Both happen at once: light at the top + deep for in-scope elements below.

**Memo section spine A/B/C/D/E/F preserved** — but the *content within each section* is dictated by the matrix rows, not by within-section authoring re-ordering. See Stream A § 10.1 for spine ↔ matrix mapping. Final reconciliation of section anchors (which matrix rows live in C vs D vs E) happens in Stream C2 (memo schema patch).

**For Pillar III tabular content** (Groups G7 + G8): APM produces driver rows per the per-component spec at Stream A § 7a (7 columns: I What / J LTI / K Count / L Modal / M Guidance / N Sell-side / O Invalidation threshold).

**Under V3 (8-May-26), reading and writing order are now the same — both follow the matrix top-to-bottom.** The old "reader sees B→A→C→D→E→F, APM writes C.II→A→D→C.I→B→E→F" gymnastics retire. APM walks the matrix at the current stage column; the resulting memo reads in the same sequence APM authored it.

## Six-phase process

### ★ Phase 0 — Pre-flight checks (extended v2.3) ★ [A2 + A14]

**Before anything else.** Three sequential checks that prevent 10-minute false starts, load institutional pattern-memory, AND inherit cohort context (when active) before analysis begins.

#### Phase 0.0 — Cohort manifest pre-load [A16, NEW v2.4]

**The first action.** Before Phase 0.1 (RESEARCHER coverage) or Phase 0.2 (WL consult) — check whether this ticker is part of an active cohort.

1. **Check `memory/staging/cohort-*-*.md`** for an active manifest containing the active ticker. **Cross-check cohort status from the RESEARCH STAGES dashboard data feed** (per cohort SKILL §3.2 — single source of truth for cohort state; manifest carries cohort definition only, NOT status).
2. **If cohort manifest exists for this ticker:**
   - Read the cohort manifest in full (typically 800-1,500 words)
   - Read the cohort-shared-context memo at `databases/memos/_cohort/{cohort-name}/shared-context.md` (typically 1,500-3,000 words)
   - Read any prior per-stock memos in the same sub-cohort that have already shipped (the comparative anchor)
   - Cite manifest path + shared-context memo path + prior-per-stock memo paths in F.I process notes (mandatory)
   - **Phase 0.2 will run in DELTA-ONLY MODE** (max 3 additional WL models, only those NOT already in cohort precommit list)
   - **Phase 2 inherits the cohort-level CQ precommits** — these become MANDATORY content sections in C.II of this stock's memo
3. **If NO cohort manifest exists for this ticker:**
   - Author cohort manifest now (per `memory/skills/cohort-research-analysis-judgement/SKILL.md` §3) AND PAUSE Phase 0.1+ until manifest signed off, OR
   - Declare **SOLO REACTIVE MODE** explicitly in the working file with one-line reason logged to `memory/staging/solo-reactive-log.md` (per cohort SKILL §2.5 — restricted triggers only)
   - Phase 0.2 runs in full mode (5-10 models)

**Why Phase 0.0 not Phase 0.1:** the cohort manifest determines the SCOPE of Phase 0.1 and Phase 0.2 — without knowing if a cohort is active, those steps don't know whether to run in full mode or delta mode. Phase 0.0 is the routing decision.

**Cross-ref:** `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0 (master cohort SOP); `memory/skills/researcher/SKILL-V2.md` V2.13 Rule #38 (RESEARCHER side of the same routing decision).

**Exit criteria:** explicit confirmation in the working file that EITHER (a) cohort manifest is loaded + shared-context memo read + prior-per-stock memos identified, OR (b) SOLO REACTIVE MODE declared with reason logged.

#### Phase 0.1 — RESEARCHER coverage check [A2, v2.2]

1. **Enumerate required inputs at this stage** per §Inputs required #1.
2. **Check `Files/{TICKER}/{STAGE}/` for each required query directory.** Present = at least `notion-formatted.md` or `cleaned.md` with non-trivial word count.
3. **Decision logic:**
   - **All required queries present** → proceed to Phase 0.2
   - **One or more required queries missing** → STOP. File RESEARCHER brief per §☆ Proactive RESEARCHER briefing. Decision: (a) wait for queries to land before authoring, OR (b) author with explicit gap flag in D.II.2 if time-limited and partial inputs are sufficient
   - **All inputs missing (no `Files/{TICKER}/` directory at all)** → STOP. RESEARCHER must run IG-stage queries first; this stock isn't ready for Triaging-stage A&J

**Why Phase 0.1 not part of Phase 1:** discovered on COTN-CH 02-May-26 — APM created tasks, drafted back-brief, started Phase 1 reading before realising ESA queue was empty.

#### Phase 0.2 — Wisdom Library consult [A14, NEW v2.3]

**Before any reading of RESEARCHER files.** Load the institutional pattern-memory that should frame the analysis.

1. **Query INDEX.json** at `wisdom-library/INDEX.json` for matching models by:
   - **Industry / sector** (e.g., med-tech, semi-cap, cables)
   - **Setup-archetype** (Demand-Driven EPSU, Corporate Change EPSU/EPT, Product Cycle, Earnings Upgrade Cycle)
   - **Business-model** (serial acquirer, asset-light services, R&D-heavy, etc.)
   - **Risk profile** (cyclical, defensive, structural-change, etc.)

2. **Load 5-10 matching models** — read each `.md` file in full. The library tells you what to expect, watch for, or avoid in this kind of case. **DELTA-ONLY MODE (NEW v2.4):** if Phase 0.0 confirmed an active cohort manifest, load only models NOT already in the cohort precommit list. Cap: 3 additional models max. The cohort precommits already cover the institutional pattern-memory for this kind of case; Phase 0.2 in delta mode adds only stock-specific lenses the cohort precommits don't anticipate.

3. **Take Phase 0.2 notes** in the working file: cite at least 3 models that informed your read. Note explicitly:
   - Which models confirm the case structure (positive evidence)
   - Which models warn against the case structure (negative evidence)
   - Which models suggest what to test for in Phase 1+ analysis

4. **Cite in F.I process notes** — list the models consulted and how they informed analysis. Mandatory.

**Why Phase 0.2 not Phase 1f:** v2.2 had Wisdom Library consult buried as Phase 1 sub-step 1f, after RESEARCHER + Master Dashboard + Notion + calibrate + archetype-tag. Promotion to Phase 0.2 enforces it as a gate. Without library consult, APM is reasoning from prior context only — losing the institutional pattern-memory.

**Cross-ref:** Per `memory-needs-workflow-binding` (Bronze) — memory entries don't enforce behaviour without workflow binding. Phase 0.2 IS the workflow binding for "consult library before working" rule.

**Exit criteria:** explicit confirmation in the working file that (a) required RESEARCHER inputs are present (Phase 0.1) AND (b) ≥5 Wisdom Library models loaded with notes (Phase 0.2).

**Cross-ref to brief template (NEW v2.3.1):** if Richard invoked this engagement via a trigger phrase (see §Phase 4.5 ★ Trigger-phrase binding ★), the master template at `memory/staging/apm-aj-brief-template.md` is the source-of-truth orientation document. Read it BEFORE this Phase 0.2 work begins.

### Phase 1 — Read + calibrate (10-20% of time)

Read ALL inputs in full before typing a single line of analysis.

**1a. RESEARCHER output** — read every local file for the ticker at this stage AND below. Triaging-depth authoring should also read ESA-level material if available — informs better judgement at no cost.

**1b. Master Dashboard data** — read `prices.json`, `filter-results.json`, `factset-ssem.json`, `factset-valuation.json`. Auto-refreshed nightly. Never ask Richard if data exists — check directly.

**1c. Richard's own Notion notes** — search Notion Stock Notes DB. Read all non-RESEARCHER, non-Watson pages. Prioritise "Case file" and "RNTS". Read journal entries, pre-mortems, meeting notes, thematic observations.

**1d. Calibrate:**
- Does the RESEARCHER narrative match the archetype expectation?
- What is the highest-conviction fact pattern?
- What is the biggest unresolved question?
- Where does evidence contradict itself? (Where judgement is most needed.)
- What does Richard already think about this stock?

**1e. Tag the archetype** using stock-archetypes.md (19 canonical types).

**1f. Wisdom Library consult** per SKILL.md §3.7 — load top 5-10 matching models.

**1g. Track record check** per SKILL.md §NON-NEGOTIABLE — track-record-by-stock.md for this stock and similar archetypes.

### Phase 2 — Matrix-Driven Analysis (V3, 8-May-26 — replaces Pillar-by-pillar)

> **V3 Phase 2 mechanism (load-bearing):** APM walks the per-row authoring matrix at the current stage's column, top-to-bottom, producing content per cell instructions. The "pillar-by-pillar" mental model is replaced by **row-by-row** at the current stage. The matrix encodes WHICH topics get touched at WHICH stages and at WHAT depth — APM does not need to decide effort allocation per pillar; the matrix decides.
>
> **Sub-blocks below operate within the V3 framing:**
> - The "70/30 time allocation rule" RETIRES under V3. Effort allocation is per-cell, not per-pillar.
> - "Per-section word targets" RETIRE under V3. Cell-instruction depth labels (First/Second/Third pass; light/solid/robust) replace word counts.
> - "Bullet architecture (parent = verdict, sub = evidence)" SURVIVES — operational discipline applicable per-row.
> - "Signposting field reference" SURVIVES with V3 vocabulary mapping per top-of-doc header note.
> - "Mandatory content scaffolds for flat pillar sections" SURVIVES — concrete bullet-types reference for any element/group APM authors.
> - "Phase 2.5 In-line validator dry-run" SURVIVES; validator scope updates in Stream C2 (memo schema work).

### ★ 70/30 time allocation rule (RETIRED under V3) ★

> **V3 (8-May-26):** This rule retires. Effort allocation is encoded per-cell in the per-row authoring matrix (Stream A § 9). At each stage, the matrix tells APM which rows are in scope and at what depth — the cell instruction (First/Second/Third pass; light/solid/robust) IS the effort signal. There is no separate 70/30 Pillar I/II/III/etc. effort split.
>
> Original v2.4.1 wording preserved below for context only:

**70% of Phase 2 + Phase 3 effort goes to P3 (Fundamental Investment Case) and P4 (Investment Case Building Blocks).** P1 (Technical), P2 (Paradigm), P5 (SS Momentum), P6 (Valuation) share the remaining 30%. Reflects Richard's priority order.

### ★ Weight-driven effort allocation (NEW v2.2) ★ [A3]

Memo doctrine v3.8 §IV.H assigns each element/RA a weight tier. **APM time per RA scales with weight:**

| Weight | Bullets per CQ (ESA) | APM effort | Examples (v3.8) |
|---|---|---|---|
| half (0.5×) | 5-8 | 0.5× | (None designated; reserved) |
| normal (1.0×) | 9-15 | 1× | Default |
| double (2.0×) | 18-30 | 2× | Required input forces; Required financial outputs; Business quality (whole group); Required simplicity guardrails; Paradigm fit (P2 G1); Lessons check; Negative earnings momentum; Crash through stops; Plain sight risks |
| quadruple (4.0×) | 36-60 | 4× | **Sector strength** (Q1 — peer-quality canary); **General ACHs** (Q2 — invalidation screening cohort) |

70% of analytical depth sits on the double + quadruple-weighted RAs.

### ★ Bullet architecture — parent = verdict, sub = evidence ★

- **Parent bullet (depth 0):** Verdict or judgement. **≤30w EXCLUDING signpost-label characters [A6 v2.2 clarification].** IAJA-tagged. Signposted (mandatory in C.II.2 family_blocks; OPTIONAL in C.II.1/3/4/5 flat pillars per A5). 10-30% underlined. Scanning layer (NN/g layer-cake).
- **Sub-bullets (depth 1):** Evidence, data points, supporting detail. ≤30w each. Up to 6 per parent (Miller 7±2). No grandchildren (max 2 disclosure levels). Flex sub-COUNT, not bullet LENGTH.

**R14 30w cap clarification (NEW v2.2) [A6]:** the 30w hard cap on parent bullets EXCLUDES signpost-label characters. A signposted parent like `**IC#3 RA1 — Sufficient longevity?** Yes, with a caveat. Cost savings are permanent.` (32w including bold-wrapped signpost) is COMPLIANT — signpost label `**IC#3 RA1 — Sufficient longevity?**` (8w) is doctrinal scaffolding, not verdict content. Verdict (`Yes, with a caveat. Cost savings are permanent.`) is 8w, well within cap. Validator updated in lock-step (v2.2).

**Non-signpost-bearing bullet >30w MUST be restructured** — split into parent verdict + sub-bullet evidence. Validator R14 enforces HARD on parents (depth=0).

### ★ Signposting field reference (NEW v2.2) ★ [A5]

**For C.II.2 (deep-shape) family_block bullets:** signposting MANDATORY (R15 HARD at ESA/DD, SOFT at Triaging).

**For C.II.1, C.II.3, C.II.4, C.II.5 (flat-shape pillars):** signposting OPTIONAL but encouraged for content scaffold components (a-f). Use P-prefixed family identifiers per the new v2.2 valid family set:

```
VALID_SIGNPOST_FAMILIES = {
  IC#1, IC#2, IC#3,        # Pillar 3 (deep-shape)
  BB#1...BB#8,             # Pillar 4 (deep-shape)
  P1, P2, P5, P6           # Flat-shape pillars (NEW v2.2)
}

VALID_SIGNPOST_LEVELS = {family, TC, RA, CQ}  # case-insensitive in validator (v2.2)
VALID_SIGNPOST_STYLES = {prefix, embedded}
```

**Signpost.level case-sensitivity (NEW v2.2 reference) [A4]:** authorial convention is `family` (lowercase) and `TC` / `RA` / `CQ` (uppercase). Validator (v2.2) accepts case-insensitive equivalents — fewer authoring gotchas.

**Example flat-pillar signpost (now valid in v2.2):**
```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {"level": "RA", "ref": "P1.RA1", "label": "Minervini 8-point pass?", "style": "prefix"},
  "text": "**MM99 score 8/8.** All 8 Minervini criteria pass..."
}
```

### ★ Per-section word targets visible inline (RETIRED under V3) ★ [A4]

> **V3 (8-May-26):** Word-count targets retire. Replaced by cell-instruction depth labels in the per-row authoring matrix (First / Second / Third pass; light / solid / robust). The matrix encodes depth at the cell level — APM does not work to fixed word counts. Validator update in Stream C2.
>
> Original v2.2 instruction preserved below for context only:

Embed target word counts as comments/scaffolds in the section template. Example:

```
# C.II.3 — P2 Fit for Market Paradigm (TARGET: 900w ESA / 600w Triaging)
#   Content scaffold (mandatory, all 6 components a-f):
```

**Why:** discovered on EKTA ESA + COTN-CH Triaging 02-May-26 — without inline targets, flat pillars authored at 0.45-0.70x of target. Inline targets force the author to track during drafting.

Walk the six pillars. For EACH pillar, produce:
- **Rating** (A/B/C/D/F — five grades only)
- **Summary judgement** (1-2 sentences, conclusion-forward)
- **Supporting bullets** (3-8, signposted to CQ/RA/TC; IAJA-tagged; parent ≤30w excluding signpost)
- **Confidence level** (high / medium / low)

**Analytical quality standard:** every bullet should make Richard think. Surface non-obvious connections, challenge consensus, identify what matters most. Test: does this bullet add something Richard doesn't already know?

Pillars:
- **P1** Technical Strength (C.II.1) — Master Dashboard formulaic + RESEARCHER Query #3 qualitative
- **P3** Fundamental Investment Case (C.II.2 — deep) — IC#1/2/3. **70% effort.**
- **P4** Investment Case Building Blocks (inside C.II.2 — deep) — BB#1-8. **70% effort.**
- **P2** Fit for Market Paradigm (C.II.3) — flat
- **P5** SS Earnings Momentum (C.II.4 — 5×3 matrix) — Master Dashboard SSEM supplementary
- **P6** Valuation & Scenario R/R (C.II.5) — Master Dashboard valuation supplementary

### ★ Mandatory content scaffolds for flat pillar sections ★

Each flat pillar (C.II.1, C.II.3, C.II.4, C.II.5) MUST contain ALL components below. Word targets are verification; components are spec.

**C.II.1 — P1 Technical Strength (TARGET: 600w Triaging / 900w ESA / 900w DD):**
- (a) MM99 score interpretation + filter qualification stage (Early/Late/Capital)
- (b) RS excess return analysis (vs sector, market, 13w/26w/52w)
- (c) MA structure (10/20/50/150/200 DMA alignment + slope)
- (d) Base formation / stage analysis (Weinstein stage, base count, tightness)
- (e) Volume patterns (accumulation/distribution, OBV)
- (f) Synthesis: institutional participation + timing readiness. Rating rationale.

**C.II.3 — P2 Fit for Market Paradigm (TARGET: 600w Triaging / 900w ESA / 900w DD):**
- (a) Me-state assessment
- (b) Sector/theme alignment
- (c) Macro exposure mapping (GDP, FX, rate, tariff)
- (d) Portfolio overlap/correlation
- (e) Sizing/liquidity fit
- (f) Synthesis. Rating rationale.

**C.II.4 — P5 SS Earnings Momentum (TARGET: 300w Triaging / 600w ESA / 600w DD):**
- (a) Revision trajectory direction + magnitude + acceleration
- (b) Estimate dispersion / range analysis
- (c) Coverage breadth + quality
- (d) Congruence check (SS vs RESEARCHER)
- (e) Momentum scoring 5×3 matrix (Revenue/EBIT/EPS × FY1/FY2/FY3) via momentum_table block
- (f) Synthesis. Rating rationale.

**C.II.5 — P6 Valuation & Scenario R/R (TARGET: 300w Triaging / 300w ESA / 300w DD):**
- (a) Primary metric assessment (P/E, EV/EBIT)
- (b) Percentile positioning (own history + peer)
- (c) Qualitative R/R framing
- (d) Scenario anchoring (upside/base/downside)
- (e) Synthesis. Rating rationale.

### ★ Phase 2.5 — In-line validator dry-run (NEW v2.2) ★ [A7]

**Between Phase 2 authoring and Phase 3 synthesis.** Catches structural rule violations 30s after authoring, not 30min after.

1. **After each section is authored** (e.g. after C.II.1 done, before C.II.2 starts), run validator dry-run on the section JSON.
2. **Helper script:** `databases/scripts/lint-section.py {section-json-path}` — accepts a single section, runs R3/R4/R5/R8/R9/R11/R14/R15/R16/R18 rules, reports violations immediately.
3. **Decision logic:**
   - **Hard violations** → fix immediately before moving to next section
   - **Soft violations (warnings)** → review; fix if cheap, defer if expensive (e.g. word-count under target may be intentional)
4. **At Phase 4 final validation,** the cumulative result should show only soft warnings — hard errors should be zero by construction.

**Why Phase 2.5 not part of Phase 4:** discovered on EKTA ESA 02-May-26 — validator failed on first authoring with 68 hard violations across all sections; 4 mechanical fix-passes required. Per-section dry-run would have caught violations as they occurred (~5 min per section vs ~45 min batch fix at the end).

**Exit criteria:** all hard violations resolved on the section before authoring next section.

### Phase 3 — Synthesis + Judgement (15-25%)

Phase 3 sections are written AFTER Phase 2. Synthesis crystallises what was discovered.

- **D.I** risk decomposition — what's driving the rating; what could break it.
- **D.II.1 invalidations** — the ten live-case invalidation thresholds specific to this stock. MANDATORY at every stage including Triaging. Use the **10 INVALIDATION ACHs** framework. **NEW v2.2 [A9]:** D.II.1 bullet_group is EXEMPT from R4 7-item Miller cap (use `cohort=true` flag) — the 10 ACHs + optional NEW stage-specific ACHs (#11, #12) form one coherent enumerated list, not chunked.
- **D.II.2** confidence / gaps.
- **D.II.3** negatives to expect (Triaging label: "Negative, should-be-expected developments").
- **C.I** ratings table — 283 rows. Judgement crystallisation of C.II.
- **B.I.1** exec summary (BLUF + 3-5 bullets + summary) — written LAST among analytical sections.
- **E.I** summary judgement — Go / No-go / Park with reasons.
- **E.II** if compelling → next-stage actions + KQs.
- **E.III** if uncompelling → park reasons + re-assessment criteria + monitoring plan.

### ★ Judgement-importance-weighted escalation (NEW v2.2) ★ [A8]

**One-line rule: the more important the judgement, the more you check with Richard.**

| Tier | Count per memo | APM autonomy | Mechanism |
|---|---|---|---|
| **CQ rating** | ~175 | Commit unilaterally | Inline in C.II bullets |
| **RA rating** | ~63 | Commit; flag uncertainty inline if conflicted | Inline RA-summary; italic "low conviction" tag if borderline |
| **Element rating** | ~19 | Commit; flag uncertainty inline; raise in handoff if material | Element-summary; material uncertainty → COS handoff |
| **Group rating** | ~5 | Commit; surface explicitly in handoff with confidence tag | Group-summary + handoff line referencing GNG CHECKS |
| **Pillar rating** | 6 | Commit BUT flag as "draft for Richard's review" | C.I.1 ratings table; `(draft)` annotation until Step 4 confirms |
| **Investment case rating** (P3+P4 synthesis → progress/park/kill) | 1 | **NEVER finalise unilaterally** | E.I = APM RECOMMENDATION only. Decision belongs to Richard at Step 4. |

**The APM's job is to PRODUCE the case-level judgement and surface it for debate, NOT to finalise it.** Get it wrong (under-rate an A as C) and an investable case dies; over-rate (call C an A) and Richard wastes time. **Highest-stakes single judgement in the entire APM workflow.**

### Phase 4 — Validation + Ship + Probing (5-10%)

- Run `validate-memo.py` against the written JSON — must pass (warnings OK, errors not).
- Word-count gate: each subsection within green band (0.85-1.15x target) unless flagged.
- Signposting coverage: every parent bullet has signpost ref per R15/R16.
- Underline emphasis: 10-30% of each parent bullet body text underlined per R17.
- IAJA tagging: every parent bullet has #J / #A / #I / #ACT per R8.

Dual-post:
- **Notion** Stock Notes page per notion-posting-standard SOP.
- **Memo JSON** committed to `databases/memos/{TICKER}/{Stage}.json`; rebake dashboard.

### ★ GNG CHECKS — proactive disagreement probing (NEW v2.2) ★ [A10]

After the memo ships, APM produces a separate **GNG CHECKS** artefact for the stock at this stage. The proactive probing mechanism — surfaces where APM most wants Richard's calibration on the case-level judgement.

**Format:**
- Notion page in Stock Notes DB AND/OR `.md` file at `databases/memos/{TICKER}/{Stage}-gng-checks.md`
- Title: `[W] {TICKER} ({Company}) — {Stage} — GNG CHECKS [W] @ {DD-MMM-YY}`
- Properties (Notion): Stock(s) relation, Stage, Source [W], Date, Case component = "GNG CHECKS"
- Linkable from Ratings Dashboard RESEARCH STAGES tab (one link per (ticker × stage) cell)

**Content — 6 to 10 questions, stack-ranked by impact on case-level judgement:**
- Probe the highest-stakes judgements (typically pillar-level or case-level)
- Vary the form: closed (yes/no), open, aggressive ("Why shouldn't this be a D?"), comparative, this-idea-centric
- Tone: direct, challenging, neutral-positive. NOT deferential. NOT defensive.
- Stack rank: #1 = most likely to change the case-level decision; #N = least
- Each question references the specific RA / element / group / pillar / ACH it probes

**Quality gate G13:** APM cannot ship without 6-10 GNG CHECKS posted (Notion or local .md).

### ★ Calibration log (NEW v2.2) ★ [A11]

When Richard overrules an APM rating (Step 4 review or inline note), APM logs the revision to `memory/apm/calibration-log.md`. **Append-only.**

**Format per entry:**
```
### {DD-MMM-YY} — {TICKER} {Stage} — {Pillar/Element/RA name}
- APM rating: {A/B/C/D/F} ({1-line rationale})
- Richard revision: {A/B/C/D/F} ({Richard's reason})
- Domain pattern: {if recurring}
- Calibration action: {what APM does differently next time}
```

**Review cadence — three-role co-review:**
- **APM owns the log** (writes entries; primary monthly review)
- **HPC reviews monthly** for performance patterns; integrates into HPC SKILL coaching observations
- **COS reviews monthly** for process/cadence patterns; integrates into COS SKILL delivery scorecard
- **Joint review:** APM + HPC + COS at last Friday of month WFP meeting. Surface 1-2 patterns to act on.

Cross-ref Wisdom Library: `peer-and-base-rate-anchoring`, `top-decile-top-quartile-grading`, `outlier-flagging-rare-data`.

### ★ Handoff to Step 3 of STAGE PROGRESSION SOP (NEW v2.2) ★ [A12]

When Phase 4 ships, APM does NOT close out. APM:

1. Writes a 3-line handoff to `memory/staging/apm-output-queue.md` so COS knows there's a memo + GNG CHECKS pending Richard's review.
2. Tags the stock in pipeline.md as "Stage X memo shipped, awaiting Richard review" (state field).
3. Surfaces the most-important uncertainty in the COS morning routine queue (so COS chases Richard within 24-48h).

**APM's analytical work is COMPLETE; the gate decision is open until Step 4 closes it.**

### ★ Phase 4.5 — Hot Wash + Wisdom Library survey (NEW v2.3) ★ [A15]

**After Phase 4 ships, before Phase 5 (Case Components, conditional) considered.** Closes the Wisdom Library bookend opened at Phase 0.2.

**★ Trigger-phrase binding (NEW v2.3.1) ★** — Richard may invoke this Phase 4.5 + the broader v2.3 bookend pattern at SESSION START via any of these phrasings (or close variants):
- "Run the hotwash related to integrating lessons into the wisdom library"
- "Run the WL hot-wash on this APM A&J project"
- "Run the bookend pattern on {STOCK}"
- "Brief APM A&J on {STOCK} {STAGE} per v2.3"
- "Run APM A&J with the Wisdom Library bookend"
- Any variant referencing "hot wash" + "wisdom library" + APM A&J context

**Watson's response when these trigger:** read `memory/staging/apm-aj-brief-template.md` (the master template — source of truth for the v2.3 APM A&J brief structure). Then read KZN-003 + this SOP §Phase 0.2 + this §Phase 4.5 + session-handoff §Step 5.5 + RESEARCHER §Rule #37 per the template's ORIENT block. Ask Richard for the `{STOCK + STAGE} BRIEF` slot details. Execute end-to-end per template + back-brief discipline.

The trigger-phrase recognition is a CONVENIENCE, not a substitute for the SOP. If Richard briefs the work without using a trigger phrase, the SOP still applies — Phase 0.2 + Phase 2.5 + Phase 4.5 + G16 are mandatory regardless of how the brief was framed.



**1. Hot wash** — run the 3-question structure on the memo authoring:
   - **What happened?** (factual — what was authored, what RESEARCHER inputs used, what calls made)
   - **What worked / what didn't?** (honest, blameless — Phase 0 catches anything? Phase 2.5 lint-section catches anything? Validator gates fire? Any sections under target / over target?)
   - **What do we change next time?** (actionable, owner-tagged — SOP refinement candidates; tooling improvements; process bindings)

**2. Wisdom Library survey** — based on the memo, identify candidate insights. Categorise per `wisdom-library/SKILL.md` §1:
   - **Sector / industry insights** → `situational/industries/`
   - **Business-model insights** → `situational/business-models/`
   - **Investment-case insights** → `situational/portfolio-construction/` or `situational/position-management/{entry,exit,management}/`
   - **Setup pattern insights** → `situational/simple-patterns/`
   - **Process / decision-making insights** → `general/decision-making/`

**3. Tier each candidate** per Wisdom Library SKILL §1:
   - **Bronze** — one observation, "watch for promotion"
   - **Silver** — multiple confirmations, structurally established
   - **Gold** — universally applicable, multiple cases, deep cross-ref network

**4. Author + file** — for each candidate Richard agrees to file:
   - Write `.md` per Wisdom Library SKILL §2 format (frontmatter + Definition + Why It Matters + Application + Examples + Cross-References + Change Log)
   - Pre-write JSON validation on INDEX.json per Wisdom Library SKILL §1 (`python3 -c "import json; json.load(open('wisdom-library/INDEX.json'))"`)
   - Heredoc + atomic mv + byte-verify per `feedback_silent_file_truncation.md` SOP
   - Update INDEX.json with new entry
   - Cite the new entry in the memo's F.I process notes (cross-link)

**5. Capture deferred candidates** — if a candidate surfaces but is deferred (Richard hasn't approved, evidence is too thin, cross-check needed):
   - Log to `wisdom-library/_meta/candidate-queue.md` (append-only)
   - Note the trigger that would promote (e.g., "1 more case observed")

**Quality gate G16 (NEW v2.3):** APM cannot ship Phase 5 (or close memo) without Phase 4.5 hot wash documented in F.I + at least one of {Wisdom Library entry filed, candidate logged to queue, "no candidates this memo" explicit note}.

**Why Phase 4.5 not part of Phase 5:** Phase 5 (Case Components) is CONDITIONAL on Step 4 progress decision; Phase 4.5 runs UNCONDITIONALLY on every memo authored. Different triggers. Phase 4.5 is the universal close-out; Phase 5 is the progression-specific next-step.

**Cross-ref:** session-handoff SKILL V2 §Step 5.5 (the cross-role parent of this Phase 4.5); RESEARCHER SKILL-V2 (Wisdom Library consult at front-end of any query).

### ★ Phase 4.6 — Cohort hot wash (NEW v2.4; renamed v2.4.1) ★ [A17]

**Conditional trigger:** runs ONCE per sub-cohort PER STAGE TRANSITION, after the LAST per-stock Phase 4.5 at that stage in the sub-cohort completes. The APM author of the LAST per-stock memo at that stage is responsible for triggering Phase 4.6 unless Richard reassigns. A 5-stock sub-cohort going through Triaging → ESA → DD produces THREE cohort hot washes (one per stage transition). Skipped entirely if Phase 0.0 declared SOLO REACTIVE MODE (no cohort to hot-wash).

**The four cohort questions** — answer each in the hot wash artefact:

**1. Differential ranking — which stocks are differentially attractive WITHIN this cohort?**
- Apply consistent peer base-rates across the cohort (per Communication Principle #1)
- Stack-rank the stocks by case-level attractiveness (A through F equivalent at the case level)
- Identify the structural reason for the ranking (not just rating arithmetic)
- Flag where the cohort context CHANGED a per-stock judgement vs what it would have been in isolation
- Format: ranked table + 1-paragraph rationale per pair-wise comparison

**2. Shared invalidations — what ACHs fire across the cohort simultaneously?**
- Identify D.II.1 invalidation thresholds that would fire on ≥2 cohort stocks at once
- Format: per-shared-ACH, list affected stocks + the trigger condition
- These are higher-priority monitoring items than per-stock ACHs (one trigger kills multiple cases)
- Feed the Monitoring Plan with one cohort-level monitoring item per shared ACH

**3. Wisdom Library promotion candidates — what cross-stock pattern emerges?**
- Run the cohort-aware WL survey across 6 categories (matching Phase 4.5 / Step 5.5):
  - sectors / industries / business-models / investment-cases / setups / anything-else
- Specifically test: does the cohort confirm an existing Bronze model (promote to Silver)? Contradict an existing Silver/Gold (demote)? Generate a new pattern that no single stock could surface (file as Bronze)?
- 03-May-26 worked example: HTRO/EKTA contrast → `single-leg-case-downgrade` (Silver, cross-stock pattern requiring 2+ stocks to define).
- Per Wisdom Library SKILL §5.5: cohort-driven tier promotion is the explicit mechanism for moving Bronze → Silver based on N-stock confirmation in a single cohort.

**4. Portfolio construction implications — what does this cohort tell us about position sizing across the live portfolio?**
- If we own one of these, what does the cohort tell us about owning more (correlation risk)?
- If we own none, what does the cohort suggest about prioritising entries?
- If a shared ACH fires, what positions deteriorate simultaneously?
- Cross-ref: live portfolio in pipeline.md / live positions JSON / position-management WL models

**Cohort GNG CHECKS** — after the four questions are answered, author 6-10 stack-ranked questions probing the COHORT-LEVEL judgements (NOT per-stock; those live in per-stock GNG CHECKS files from Phase 4 §A10).

Stack-ranking criterion: which cohort-level question, if Richard answers differently, would most change Watson's per-stock recommendations? #1 = highest impact.

**Hot wash artefact — triple posting per AJ SOP v2.4.1 convention (NEW v2.4.1):**

- **Notion artefact** posted to Stock Notes DB. Title: `[W] Cohort Hot Wash — {Cohort Name} — {Stage} @ {DD-MMM-YY}`. Properties: Stock(s) relation set to ALL sub-cohort member tickers; Stage; Source [W]; Date; Case component = "Cohort Hot Wash".
- **Local artefact** at `databases/memos/_cohort/{cohort-name}/hot-wash-{stage}.md` — full markdown with the 4 questions answered + Cohort GNG CHECKS + WL candidates + portfolio implications. ONE file per stage transition (so a sub-cohort progressing Triaging → ESA → DD creates `hot-wash-triaging.md`, `hot-wash-esa.md`, `hot-wash-dd.md`).
- **RESEARCH STAGES dashboard tab (NEW v2.4.1):** the cohort hot wash MUST be surfaced as a dedicated `{cohort × stage}` row on the RESEARCH STAGES tab — visible to Richard alongside per-stock RES + APM rows. Schema spec at `databases/research-stages-cohort-spec.md`. The actual dashboard integration is owned by SA and implemented when their current RESEARCH STAGES tab WIP is complete. Until then, the cohort hot wash event is logged to the manifest's Audit Trail as a placeholder.
- **Cross-link:** every per-stock memo in the cohort updated to reference the hot wash in F.I process notes (post-hoc edit allowed).

**Why Phase 4.6 not Phase 5:** Phase 5 (Case Components) is per-stock and CONDITIONAL on Step 4 progress decision. Phase 4.6 is per-cohort and runs UNCONDITIONALLY when a cohort manifest exists. They serve different purposes — Phase 5 is "what does THIS stock need next?", Phase 4.6 is "what did the cohort teach us as a group?".

**Why Phase 4.6 not part of session-handoff Step 5.5:** Step 5.5 is per-session and surveys the WHOLE session's work. Phase 4.6 is per-cohort and could span multiple sessions (the cohort manifest persists; cohort hot wash runs when the LAST stock at a stage in the cohort ships, regardless of which session). The cohort layer is structurally different from the session layer.

**Cross-ref:** `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.1 §5 (full cohort hot wash SOP); `wisdom-library/SKILL.md` §5.5 (cohort-driven tier promotion); session-handoff SKILL §Step 5.5.0 (cohort presence check at session close).

### Phase 5 — Case Components prep (NEW v2.2; conditional) [A13]

**Triggered when:** Step 4 review meeting decides to progress the stock to the next stage (or to keep it live in the portfolio).

**What APM does:** produces the **CASE COMPONENTS** artefact — a distilled in-flight checklist derived from the memo. Components include:
- **Key drivers** (1-2 fulcrum drivers + 4 key drivers — typically lifted from C.II.2 IC#3 setups + IC#1 outputs)
- **Invalidation thresholds** (10 INVALIDATION ACHs from D.II.1, distilled to the 2-3 that bite first for THIS stock)
- **Leading tracking indicators** (1-2 monitoring items per fulcrum driver — feeds the Monitoring Plan)
- Other components (TBD as case components SOP is authored)

Components are NOT part of the memo. Separate Notion artefact + linked from Ratings Dashboard + integrated with Monitoring Plan.

**Cross-ref:** `memory/skills/case-components/SKILL.md` (TBD — to be authored after Richard's case components brief). Forward-pointing hook only at v2.2.

## Judgement doctrine (standing — apply in every memo)

- **Strong views, weakly held.** Always have a conclusion. Revisable on new evidence.
- **Five grades only: A, B, C, D, F — NO modifiers.** No +, no -, no A-, no C+. Express nuance in summary text, not the rating letter. Applies everywhere — header conviction, C.I (all 283 rows), pillar_block, family_block. Validator R18 (HARD).
- **Rating means something specific.** A = best-in-class evidence + multiple independent signals. B = strong but one gap. C = mixed / balanced / partial. D = weak / concerning / gap-dominated. F = failed attribute / explicit red flag.
- **Evidence-based, not hedged.** Cite numbers, transcripts, specific facts.
- **Creative and insightful, not formulaic.** Every judgement reveals something — tension, non-obvious connection, reason to think differently.
- **Invalidations codified.** Every memo from Triaging onward carries 10 explicit invalidation thresholds (D.II.1).
- **Track-record-lens.** Check past holdings + similar archetypes before recommending.
- **Archetype discipline.** Honour archetype-specific sizing/exit rules.

## Quality gates — APM cannot ship without

1. ✓ All six pillars rated with summary judgement + supporting bullets.
2. ✓ Exec summary BLUF ≤60w (R5).
3. ✓ Every parent bullet signposted + IAJA-tagged + 10-30% underlined.
4. ✓ validate-memo.py passes (errors 0).
5. ✓ Dashboard rebake succeeds.
6. ✓ Notion post landed with correct properties.
7. ✓ RESEARCHER inputs satisfied OR explicit coverage gap flagged in D.II.
8. ✓ Richard's own Notion notes (Case files, RNTS, journal entries) read and integrated.
9. ✓ Analytical quality standard met: bullets insightful, not formulaic.
10. ✓ **Rating scale: A/B/C/D/F only.** R18 HARD.
11. ✓ **Content scaffolds complete** for all flat pillars (C.II.1/3/4/5) — all components a-f present.
12. ✓ **Bullet architecture.** Every parent ≤30w excluding signpost label per A6. Evidence in sub-bullets. R14 HARD.
13. ✓ **GNG CHECKS posted (NEW v2.2 [A10]).** 6-10 questions, stack-ranked, signposted.
14. ✓ **In-line validator dry-run completed (NEW v2.2 [A7]).** Per-section dry-runs at Phase 2.5 — no hard violations carried into Phase 4.
15. ✓ **Calibration log entry on Richard revision (NEW v2.2 [A11]).** If Step 4 changes any APM rating, append entry to `memory/apm/calibration-log.md`.
16. ✓ **Phase 4.5 hot wash + Wisdom Library survey complete (NEW v2.3 [A15]).** Hot wash documented in F.I; ≥1 of {WL entry filed, candidate logged to `wisdom-library/_meta/candidate-queue.md`, "no candidates" explicit note}.
17. ✓ **Phase 4.6 cohort hot wash complete when cohort manifest exists (NEW v2.4 [A18]; reworded v2.4.1).** Conditional gate — fires when Phase 0.0 confirmed an active cohort manifest AND this is the LAST per-stock memo at the active stage in the sub-cohort. Gate requires: (a) `databases/memos/_cohort/{cohort-name}/hot-wash-{stage}.md` exists with all 4 cohort questions answered; (b) Notion cohort hot wash page posted with Stock(s) relation covering all sub-cohort tickers; (c) Cohort GNG CHECKS (6-10 questions) authored; (d) ≥1 WL outcome at the cohort level (entry filed / candidate logged to queue / "no cohort-level candidates" explicit note); (e) per-stock memos cross-linked to the hot wash in F.I notes; (f) **NEW v2.4.1:** RESEARCH STAGES dashboard tab row populated for the `{cohort × stage}` event — until SA's dashboard integration is live, satisfied by an explicit Audit Trail entry in the manifest documenting the hot wash event with a link to the local artefact. **Skipped entirely** if Phase 0.0 declared SOLO REACTIVE MODE (log "G17 N/A — solo reactive mode" in F.I).

## Integration with the other APM activities

This SOP slots ABOVE the entry/exit decision. Entry decision (SKILL.md §Entry Decision Checklist) uses the memo as input — but the memo has to be written first, governed by this SOP.

The DD-stage memo should be complete enough that the entry decision checklist can be run directly from it without re-reading RESEARCHER output.

## Cross-references

- SKILL.md (root APM skill)
- `memory/skills/stage-progression/SKILL.md` — STAGE PROGRESSION SOP v1.0 (parent SOP; this AJ SOP is Step 2)
- `memory/projects/ratings-dashboard/spec.md` (memo structure spec)
- `memory/projects/ratings-dashboard/decisions.md` — **10 INVALIDATION ACHs**
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 (R5/R8/R14/R15/R16/R17/R18; weight system §IV.F-H)
- `databases/memo-view-formatting-principles.md` v3.8 (memo doctrine SSoT)
- `memory/skills/notion-posting-standard/SKILL.md` (Notion posting)
- `memory/skills/researcher/` (RESEARCHER templates — APM briefs these)
- `memory/skills/communication-principles/SKILL.md` (4 cross-role principles)
- `memory/skills/case-components/SKILL.md` — adjacent SOP (TBD; Phase 5 forward-hook only)
- `memory/apm/calibration-log.md` (NEW v2.2 — created on first Richard rating revision)
- `memory/apm/open-issues-stage-progression.md` (NEW v2.2 — STAGE PROGRESSION SOP friction log)
- `memory/staging/apm-output-queue.md` (Phase 4 handoff to COS)
- `memory/staging/researcher-queue.md` (Phase 0 RESEARCHER brief queue)
- `databases/scripts/validate-memo.py` v2.2 (validation gate; lock-step with this SOP)
- `databases/scripts/lint-section.py` (per-section dry-run helper for Phase 2.5; TBD)
- `databases/scripts/build-memos.py` (dashboard bake)
- `master-dashboard/data/prices.json` (P1 formulaic inputs)
- `master-dashboard/data/filter-results.json` (MM99 + filter qualification)
- `master-dashboard/data/factset-ssem.json` (SS revision %)
- `master-dashboard/data/factset-valuation.json` (P/E + percentiles)
- `memory/context/investment-process.md` (6-stage funnel)
- `memory/context/investment-strategy.md` (4-pillar framework, setups)
- `wisdom-library/general/decision-making/judgement-analysis-information-ordering.md` — Gold (J→A→I)
- `wisdom-library/general/decision-making/mission-command.md` — Step 1 back-brief
- `wisdom-library/general/decision-making/three-gaps-art-of-action.md` — Step 1 diagnostic

---

*[W] v2.3.1 authored 03-May-26 PM (later) by Watson (SA role) adding trigger-phrase binding to master brief template at `memory/staging/apm-aj-brief-template.md`. Convenience-layer minor-bump on top of v2.3 bookend pattern. v2.3 authored same day adding the bookend pattern (A14 + A15) on top of v2.2's 13 amendments. Cross-role lock-step with RESEARCHER SKILL-V2.11 + session-handoff SKILL V2 §Step 5.5. Backups: `.bak-pre-trigger-binding-20260503` (this v2.3.1 edit), `.bak-pre-v23-bookend-20260503` (v2.3 baseline), `.bak-pre-v22-integration-20260503` (v2.2 baseline).*

*[W] v2.4 authored 04-May-26 by Watson (SA primary, APM subject) adding cohort layer (A16 Phase 0.0 + A17 Phase 4.6 + A18 G17) on top of v2.3.1's bookend. Cross-role lock-step with RESEARCHER SKILL-V2.13 (Rule #38), session-handoff SKILL §Step 5.5.0 (cohort presence check), Wisdom Library SKILL §5.5 (cohort-driven tier promotion), and the new master cohort SOP at `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0. Backup at `analysis-judgement-SOP.md.bak-pre-cohort-20260504`. Earlier backups retained.*

*[W] v2.4.1 authored 04-May-26 (later same day) by Watson (SA primary) per Richard's instructions: terminology rename ("wash-up" → "hot wash"; "cohort cycle" → "Cohort-centric IAJA cycle"); status tracker defers to RESEARCH STAGES dashboard data feed (single source of truth, not manifest text); Phase 4.6 surfacing requirement on RESEARCH STAGES tab via dedicated {cohort × stage} row (SA-owned implementation when current dashboard WIP completes; spec at `databases/research-stages-cohort-spec.md`); Phase 4.6 trigger clarified as "per stage transition" not "once per cohort lifetime" (so a 3-stage sub-cohort fires Phase 4.6 three times, once per Triaging/ESA/DD). G17 reworded. Lock-step v1.1 patch with cohort SKILL.md v1.1, RES SKILL-V2.13, session-handoff SKILL Step 5.5.0 v1.1, Wisdom Library SKILL §5.5 v1.1. Backup at `analysis-judgement-SOP.md.bak-pre-v11-20260504`.*
