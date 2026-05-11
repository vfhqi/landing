# RESEARCHER Role Skill — V2

## Operating Anchors (from CLAUDE.md — see there for full text) [Locked 28-Apr-26]

- **Quality > Speed** (operating value)
- **NEXT TOOL CALL** (rule) — statement of intent must include first concrete tool call in same turn
- **FRICTION = ENGAGE** (rule) — when stuck, double down on the OBJECTIVE
- **SOP CITATION GATE** (rule) — for this role, governing SOPs are: researcher/SKILL-V2.md, researcher/as-claude-research-sop-v2.md, researcher/notion-posting-sop.md, notion-posting-standard/SKILL.md, researcher/updating-old-research-memos-SOP.md. Any proposal touching these workflows must cite the specific §X.Y in-turn.
- **DEAD-TIME DEFAULT** (rule) — during wait windows: re-read SOP/brief, verify state, write status, wait silently. No inventing parallel work.
- **FIRST FILE IN 5 MIN** (rule) — for this role, first stub file = state.md in active research dir, or query-tracker.json for batch queries

These anchors take precedence over any role-specific procedure that conflicts with them.

---
<!-- [W] V2 created 14-Apr-26. Major restructure: 23-query framework, per-query source assignment, self-contained templates, Haiku AS submission. -->
<!-- V2.1 15-Apr-26: Six Pillars integration. Monitoring Plan database. A-F scale. ICD/TI framework integration with APM. -->
<!-- V2.2 15-Apr-26: Query #23 (Thematic Research) added. 22→23 queries. Dual-source always. SOP: thematics-research-sop.md. -->
<!-- V2.3 15-Apr-26: Dual-source merge protocol. Rules #13-18: 4 IG/Triaging queries (#2,#4,#5,#7) merge to single [C+AS] pages. Pre-merge validation gate, backbone defaults, contradiction handling, thin-AS handling. 4-stock evidence base (HTRO, DEC, DCC, AENA). -->
<!-- V2.4 18-Apr-26: Concise writing voice. All min word counts reduced 25%. Key findings summary mandatory. Short declarative sentences. Same breadth, tighter expression. Rules #22-23. All 23 templates updated. -->
<!-- V2.5 24-Apr-26: OUTPUT DEPTH FIX. Root cause: V2.4 concise voice sent to AlphaSense (third-party LLM) caused systematic length drops — CKN BD at 2,535w vs 7,000 min. Evidence: 144 metadata files audited, 9 outputs <70% of min. Fix: (1) Split writing voice — [C] keeps concise, [AS] gets depth-first instruction. (2) Min word counts restored to pre-V2.4 levels. (3) Validation gate rebuilt as two-tier (50% hard floor, 75% quality gate with section completeness check). (4) Merge backbone override raised from 2,000→3,500w + proportional override added. (5) Hard minimum enforcement added to bottom of all 23 templates. Rules #10, #14, #15, #18, #22 updated. All 23 templates updated. -->
<!-- V2.6 28-Apr-26: OVERNIGHT RELIABILITY REFORM. Rules #28/#29/#30 (added 28-Apr-26 morning) absorbed into structural enforcement and removed from this rule list — they now live as defaults in `scheduled-tasks/CANONICAL-PROMPT.md` and `BRIEF-INTAKE-SOP.md`. Rule #21 (unattended autonomy) absorbed — it is a settings.json fact, not a rule to remember. Rule #14 (pre-merge validation) kept here but cross-referenced to canonical template where it is structurally enforced. Net rule count: 30 → ~22. Aligned with 24-Apr-26 "Do It Right" quality reform: structural enforcement over procedural sprawl. -->
<!-- V2.7 28-Apr-26: HAIKU AS SUBMISSION LESSONS. Concurrent Haiku agent contamination confirmed (MTRS-SE, 28-Apr-26): multiple simultaneous agents share browser session state, causing duplicate URL reporting and cross-navigation. Fix: sequential submission or explicit tab isolation. Also: AlphaSense SPA DOM enumeration unreliable — use innerText sidebar scan for thread title confirmation. URL capture must occur immediately at step 10 (post-submission URL change), not retrospectively. See lessons-and-mistakes.md "MTRS-SE Live Session — AS Submission URL Verification" for full detail. -->
<!-- V2.8 30-Apr-26: FOUR-PHASE AS MODEL + AUTO-RESUBMIT + QC FOOTER + BRIEF-CARD APPEND FIX. Rule #30 (four-phase model: Phase 1 submit+verify+close window, Phase 2 cold reopen+extract at 02:00 UK, Phase 3 merge, Phase 4 publish). Rule #31 (auto-resubmit if extraction fails after 2-3 retries over 15min AND original >120min ago — AS resubmission is free). Rule #32 (QC audit footer block mandatory on every Notion memo). Rule #33 (brief-card append-not-overwrite — manifest header + read-modify-write + banned suffixed variants). Rules #28/#29 unchanged (still load-bearing). All structural enforcement, not declarative. Locked 30-Apr-26 per Richard's instruction. -->
<!-- V2.9 30-Apr-26 (later same session): Rule #34 added — Communication Principles (cross-role skill). Every memo must apply principles #1 (peer/base-rate context) + #2 (A/B/C/D/F grading) + #3 (invert and call out D/F with ❌) + #4 (🚩 RARE outlier flagging). Underlying mental models cross-listed in Wisdom Library: `peer-and-base-rate-anchoring`, `top-decile-top-quartile-grading`, `invert-and-call-out-bottom-quartile`, `outlier-flagging-rare-data` (all Gold tier 30-Apr-26). New SKILL: `memory/skills/communication-principles/SKILL.md`. APM SKILL.md and notion-posting-standard SKILL.md cross-referenced same session. -->
<!-- V2.10 1-May-26: Rule #35 added — STAGE PROGRESSION SOP (cross-role). RES is informant in Step 1 (briefed by APM if Step 2 needs more info to proceed) and optional attendee in Step 4 (weekly review meeting; provides info-layer context if disputed). RES's role in Step 4: be ready to defend the information layer (sources, freshness, contradiction handling) IF Richard or APM disputes a fact. RES does NOT vote on the case-level decision. Cross-ref: `memory/skills/stage-progression/SKILL.md` v1.0. TRIAL MODE DISCONTINUED 03-May-26 — fully integrated. -->
<!-- V2.11 03-May-26 PM: Rule #37 added — WISDOM LIBRARY PRE-QUERY CONSULT (cross-role bookend with AJ SOP v2.3 §Phase 0.2 + session-handoff SKILL V2 §Step 5.5). Before submitting any AS prompt or running any [C] query for a stock, RESEARCHER queries `wisdom-library/INDEX.json` for matching models by industry/sector/business-model/setup-archetype. Library tells RESEARCHER what to look for vs noise. Cross-ref: `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.3 §Phase 0.2 (APM consults same library before reading RESEARCHER output) + `memory/skills/session-handoff/SKILL.md` §Step 5.5 (WL survey + propose entries at session close). -->
<!-- V2.12 04-May-26: Rule #38 added — COHORT MANIFEST PRE-CONSULT (cross-role lock-step with AJ SOP v2.4 §Phase 0.0 + session-handoff SKILL §Step 5.5.0 + master cohort SOP `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0). Before any per-stock query dispatch, RESEARCHER checks for an active cohort manifest in `memory/staging/cohort-*-*.md`. If present, RESEARCHER inherits cohort context (manifest + shared-context memo + cohort CQ precommits) and runs Rule #37 in DELTA-ONLY MODE (only WL models NOT already in cohort precommit list). Token efficiency: cohort context read once per cohort; per-stock template adds only stock-specific delta. The trio rule (3-5 stocks per sub-cohort) is enforced via the cohort manifest. Backup: SKILL-V2.md.bak-pre-cohort-20260504. -->
<!-- V2.13 06-May-26: RESEARCHER SOP REFINEMENTS PROMOTION. All 22 templates (Q1-Q22) replaced with v2.1 pattern: format-aware content generation, J-front verdicts, QC audit tables, SS breadth gates (5L Hard + 5M Warn), BB#2 coverage maps (Q1/Q8), canonical taxonomy references (APM A&J SOP per D-RSR-33), ⚡ marker (outliers + deliberately-weird), Counter-hypothesis check (AI-Dunning-Kruger) in every QC Commentary, ACH explicit in Q10/Q14/Q19/Q22, M/M/O in Q19/Q20/Q21/Q22. Concepts A+B Operating Disciplines section added (edge-detection + cognitive discipline under disagreement). 7 Wisdom Library GOLD entries authored. Q19-Q22 renumbered per D-RSR-32 (Q20=CEO/CFO Meeting Prep, Q21=KQ Research, Q22=KQ Analysis). Q23 thematic-research untouched. 34 decisions locked (D-RSR-1 to D-RSR-34). Per SA - RESEARCHER SOP REFINEMENTS project. -->
<!-- V2.12.1 04-May-26 LATER: Terminology + Query #8 patch (no behavioural change). (a) Rule #38 status check now reads from RESEARCH STAGES dashboard data feed (single source of truth — per cohort SKILL §3.2 v1.1) — manifest carries cohort definition only, NOT status. (b) "Cohort cycle" → "Cohort-centric IAJA cycle" globally. (c) Query #8 (BM/Sector Primer at ESA) STAYS FULL-SIZE at ~3,000-word target. The cohort-shared-context briefing memo authored at cohort manifest Step 6 (cohort SKILL §3.4) is in addition to, NOT in replacement of, Query #8. Cohort primer is briefing material; Query #8 is full reading document. Cross-ref: AJ SOP v2.4.1 + cohort SKILL v1.1. Backup: SKILL-V2.md.bak-pre-v11-20260504. -->
<!-- V2.13.1 06-May-26: Q1 (Business Description) source changed from AS-only to AS+C dual-source per D-RSR-36. Master Table, Rule #12, Rule #14 (backbone default: [AS]), IG execution flow (Steps 3/7/8/9), Page Count Summary all amended. Template 01-ig-bd.md updated with [C] DELTA block + merge instructions. as-claude-research-sop-v2.md Step 6c merge list updated. Richard's rationale: "it is so important a query for me that I want the richness of both sources." -->
<!-- V2.13.3 07-May-26: QUERY DISPLAY NAME RENAME (Option A, display-only). Q4 "Earnings Trends" → "Earnings trends vs. peers (L2Yish)"; Q5 "Earnings Delivery" → "Most recent earnings delivery (L6Mish)"; Q9 "Earnings History" → "Earnings delivery record (L3Yish)"; Q11 "Value Chain Map" → "Value chain info map". Richard's rationale: old names too similar, new names clarify analytical scope and time horizon. Filenames unchanged. Master Table, template headings, AS SOP references all updated. Dashboard commit b3f73b5. -->
<!-- V2.13.2 06-May-26: UNIVERSAL SINGLE-MEMO MERGE per D-RSR-37. ALL dual-source queries now merge to single [C+AS] page — Q8, Q10, Q14, Q19, Q20 changed from "2 [AS] + [C]" to "1 merged [C+AS]", matching IG/Triaging pattern. Resolves Rule #12 vs Master Table contradiction (Rule #12 already said "single page"; table said "2 pages" — never explicitly decided). Master Table, Page Count Summary, Rule #14 (backbone defaults for all 10 dual-source queries + merge content-retention gate ≥70%), ESA execution flow (merge steps for #8/#10 Pass 1, #14 Pass 2), DD execution flow (merge step for #19), Any Stage (#20). Templates 08/10/14/19/20 updated (posting → raw save, Notion convention → merged title). as-claude-research-sop-v2.md Step 6c expanded to all stages. Q23 thematic also updated to merged. Full IG-to-DD: 19 core pages per stock (down from 24). Richard's rationale: "1 longer memo is better than 2 separate memos." -->

## ⚠️ MANDATORY PRE-LOAD — SCHEDULED/UNATTENDED CONTEXTS (revised 28-Apr-26)
**When this role runs in a scheduled task, read in order:**
1. `memory/skills/scheduled-task-preamble.md` — Brief Reception, Delivery Verification, Sub-Agent Management, Quality Over Speed.
2. `memory/skills/researcher/scheduled-tasks/CANONICAL-PROMPT.md` — the template the task was generated from. Definition of Done lives here.
3. `memory/skills/researcher/scheduled-tasks/WATCHDOG-SOP.md` — the watchdog at 03:30 + 06:30 will retry/flag if you fail. You are not the last line of defence; quality discipline is unchanged.

The `scheduled-tasks/` subfolder is the operational specification for overnight RESEARCHER work. SKILL-V2 (this file) governs the query framework content (22 v2.1 templates Q1-Q22 + Q23 thematic-research, legacy format). The two are complementary.

## Purpose

Watson acts as Richard's primary research engine — generating ideas, running structured research workflows, extracting insights from multiple sources, and posting formatted outputs to Notion. This is the master file for the RESEARCHER role. It defines the query framework (22 v2.1 templates Q1-Q22, promoted 06-May-26 per D-RSR-34, + Q23 thematic-research in legacy format), orchestration logic, and quality standards. Execution mechanics live in the referenced SOPs. Each query has a self-contained agent template in `templates/`.

---

## When to Activate

- Ideas Generation (IG) stage workflows
- Triaging stage workflows
- Early-Stage Assessment (ESA) workflows
- Deep-Dive (DD) workflows
- Key Question (KQ) research at any stage
- CEO/CFO meeting preparation
- Earnings preparation and post-earnings analysis
- Industry/thematic research
- Monitoring (TIs, Drivers, Reassessment Criteria)
- Info Flow SOPs

---

## Referenced SOPs

| SOP | File | Covers |
|---|---|---|
| **Research Execution SOP** | `as-claude-research-sop-v2.md` | Claude [C]: native execution (Sonnet) via web search + writing. AlphaSense [AS]: Haiku browser submission, fire-and-forget, URL bookmarking. Extraction by Sonnet. Batch planning. |
| **Notion Posting SOP** | `notion-posting-sop.md` | Sentiment highlighting → format → post to Stock Notes DB → verify. Full-length rule. Chunking for large memos. |
| **Notion Posting Format Standard** | `../notion-posting-standard/SKILL.md` | **Cross-cutting. V2 18-Apr-26.** IAJA bullet tagging (#J/#A/#I/#T/#O/#KR/#OQ), colour-label prefixes, J→A→I ordering, BLUF (page + section), italic summaries, pipe tables (never HTML), emphasis rules, pre-flight quality gate. Load before ANY Notion posting. This standard governs rendering; role SOPs govern content. |
| **Updating Old Research Memos SOP** | `updating-old-research-memos-SOP.md` | **v2.0 (06-May-26). FORMATTING ONLY.** Takes existing raw/highlighted markdown memos and adds HTML structure, signposts, highlights, splits long text into scannable bullets. Cardinal Rules: do not reword, do not drop content (90% word floor), do not change analytical temperature. 6-step pipeline: Load & Count → Plan Sections → Format HTML → Wrap → Validation Gate → Deploy to GitHub Pages. Validator: `databases/scripts/validate-memo.py`. Self-contained — does NOT reference the old formatting spec. |
<!-- Briefing Note SOP REMOVED 28-Apr-26. The brief-card produced by `scheduled-tasks/BRIEF-INTAKE-SOP.md` is structurally the same thing — durable record of the brief, the parsed plan, special angles, expected outputs — saved in COWORK as `memory/staging/researcher-brief-{date}.md` and referenced from Task A/Task B prompts. The Notion-side briefing-note page was redundant ceremony. Old SOP archived at `_archive/briefing-note-sop.md.archived-28-Apr-26`. -->

**All research types below use these SOPs.** This file defines pipeline logic: which queries, which sources, what sequencing.

---

## Critical Rules

1. **Per-query source assignment.** Each of the 22 queries specifies its LLM source(s) in the master table below. Some are AS-only, some Claude-only, some dual-source. The source assignment is the rule — not a blanket dual-source mandate. [D]
2. **Full-length posting.** Never summarise. The Notion page IS the memo. [D]
3. **30%+ highlighting.** Mandatory on all postings. Sentence-level precision, not paragraph-level. [D]
4. **IAJA synthesis.** SKIPPED at IG stage. Mandatory at ESA and DD stages. Uses [W] tag. [D]
5. **Premortem variant.** Always use REFV02_RB. REFV01_RB and REFV01_Cowboy are permanently discarded. [D]
6. **Native [C] execution.** Claude [C] research is done natively by Watson (Sonnet) using web search — NOT via browser submission to claude.ai. [D]
7. **Haiku AS submission.** AlphaSense [AS] prompts are submitted by a Haiku-mode agent via Chrome browser. Sonnet prepares the prompts; Haiku executes the browser protocol; Sonnet validates verification evidence on return. See Research Execution SOP. [D]
8. **Self-contained agent templates.** Each query dispatches using its numbered template from `templates/`. The template contains the complete agent brief (mission, context, prompt). The parent RESEARCHER (Sonnet) handles orchestration, posting, and verification — the research agent is a pure writer/researcher. [D]
9. **Diligence checks mandatory.** All sub-agent outputs must be validated on return. All AlphaSense submissions must be screenshot-verified. See `memory/skills/diligence-checks/SKILL.md`. [D]
10. **Output validation gates — two-tier (revised 24-Apr-26).** On every sub-agent return, verify: (a) word count vs minimum (see per-query Master Table), (b) correct company/ticker in output, (c) all expected sections present. **Two-tier enforcement:** [D]
    - **Hard floor (<50% of minimum):** Do NOT post under any circumstances. Save raw output to local Files/. Log failure with word count, query, source. Escalate to Richard immediately. Regenerate if [C]; flag AS failure if [AS].
    - **Quality gate (50-75% of minimum):** Post is BLOCKED pending section completeness check. Watson reads the template, counts how many specified sections/sub-questions are present in the output, calculates coverage %. If section coverage <80% of required sections → do not post, regenerate or escalate. If coverage ≥80% (output is short but substantively complete) → post with metadata flag `"quality_flag": "below_target"` and note in Notion page footer.
    - **Pass (>75% of minimum):** Post normally. No flag needed.
    - **Rationale (24-Apr-26):** The prior single 50% threshold let the CKN BD through at 48% (2,535 words vs 5,250 min). A 2,535-word BD for a £2.6bn company cannot cover 19 sub-questions adequately. The two-tier system catches thin outputs that the old binary gate missed.
<!-- Rule #11 (Briefing note auto-save at ESA/DD) DELETED 28-Apr-26 — superseded by the brief-card produced by `scheduled-tasks/BRIEF-INTAKE-SOP.md`. Rationale: brief-card is structurally the same thing (durable record of the brief, plan, angles, expected outputs) but lives in COWORK and is referenced from Task A/Task B prompts. The Notion-side briefing-note page was redundant ceremony. Old SOP file archived at `_archive/briefing-note-sop.md.archived-28-Apr-26`. -->
11. **KQ standing instruction.** When Richard asks Watson to run research at any stage, Watson always asks: "Are there any specific KQs you want investigated alongside the standard reports?" [D]
12. **Dual-source merge protocol (15-Apr-26; Q1 added D-RSR-36; all stages confirmed D-RSR-37).** For ALL dual-source queries (#1, #2, #4, #5, #7 at IG/Triaging; #8, #10, #14, #19 at ESA/DD; #20, #21, #22 at Any Stage), RESEARCHER produces [C] and [AS] independently (preserving intellectual independence), then merges into a **single Notion page** per query. Raw [C] and [AS] outputs are saved locally as audit trail (`COWORK/outputs/{ticker}/raw/`) but NOT posted to Notion separately. The merged page is the only Notion posting. [D]
13. **Pre-merge validation gate (15-Apr-26, thresholds revised 24-Apr-26).** Before merging, RESEARCHER verifies: (a) [AS] output answers the same query as [C] (same query type, same time period, same scope — not a different question), (b) [AS] meets minimum substance threshold (≥3,500 words or ≥40% of [C] length), (c) correct ticker/company throughout. If any check fails → post [C]-only page; save [AS] as local reference only. Log validation failure. [D]
14. **Backbone selection defaults (15-Apr-26, revised 24-Apr-26; Q1 added D-RSR-36; Q8/Q10/Q14/Q19/Q20 added D-RSR-37).** Each merged page has one "backbone" source providing the structure, with the other source's unique material woven in. Defaults: [D]
    - **IG/Triaging:**
    - **#1 (Business Description):** [AS] backbone. Broker initiation reports provide the richest factual base for what the business does, how it makes money, financials, and industry context. [C] enriches with analytical framing, cross-sector parallels, quality flags, and BB#2 CQ coverage from public sources. Override: thin [AS] (<3,500 words) → [C] backbone.
    - **#2 (Change Forces):** [AS] backbone. Override: thin [AS] (<3,500 words) → [C] backbone.
    - **#4 (Earnings Trends):** [C] backbone. Override: [AS] richer on sub-query → [AS] backbone.
    - **#5 (Earnings Delivery):** [C] backbone. Override: heavy-coverage stock with data-rich [AS] → [AS] backbone.
    - **#7 (KD Assessment — Triaging):** [C] backbone. Override: thin-coverage stock where [AS] broker research is dominant → [AS] backbone.
    - **ESA/DD (D-RSR-37, 06-May-26):**
    - **#8 (BM/Sector Primer):** [AS] backbone. Broker sector primers + expert calls provide the richest industry structure + competitive analysis. [C] enriches with public-domain peer analysis, cross-sector framing, and creative interpretation of public data. Override: thin [AS] (<3,500 words) → [C] backbone.
    - **#10 (Short-Sellers):** [C] backbone. Public bear-case material (short-seller reports, Substack, Reddit, YouTube) is the unique value — AS cannot access these. [AS] enriches with per-broker bearish views + expert sceptics. Override: heavy-coverage stock with rich [AS] bear survey → [AS] backbone.
    - **#14 (KD Assessment — ESA):** [C] backbone. Watson's own driver synthesis is the intellectual spine. [AS] enriches with per-driver SS dispersion + expert commentary. Override: thin-coverage stock where [AS] per-driver broker research is dominant → [AS] backbone.
    - **#19 (Pre-mortem):** [C] backbone. Framework/conceptual failure-mode reasoning structures the narrative; ACH matrix draws on all evidence. [AS] enriches with empirical evidence (expert calls, bear notes, management credibility stress-tests). Override: thin [C] or very rich [AS] expert evidence → [AS] backbone.
    - **#20 (CEO/CFO Meeting Prep):** [C] backbone. Framework-driven question generation structures the document. [AS] enriches with what SS has already asked and where expert evidence points. Override: heavy-coverage stock with rich [AS] Q&A history → [AS] backbone.
    - **Proportional override (all queries, 24-Apr-26):** If [C] output is >2x the word count of [AS], always use [C] backbone regardless of query-specific defaults. The deeper analysis should structure the page.
    - **Merge content-retention gate (D-RSR-37):** After merge, verify merged word count ≥70% of (raw-C + raw-AS) combined word count. Ensures content was codified/organised, not cut. Failure = flag for review before posting.
15. **Source attribution in merged pages (15-Apr-26, syntax revised 30-Apr-26).** Every factual claim must be traceable to [C] or [AS]. Use inline attribution per `notion-posting-standard/SKILL.md` §15 Source Attribution Markers: `**[AS·{broker}]:**` for AS-sourced claims (e.g. `**[AS·Jefferies]:**`); `**[AS·company]:**` for AS-indexed primary docs; `**[AS·expert]:**` for expert calls; `**[AS·multiple]:**` when multiple brokers cited. `**[C]:**` for Claude-analytical points where distinction matters; default voice (no marker) = backbone source. **Deprecated 30-Apr-26: the prior `==Per [AS]/[broker]:==` syntax — `==text==` does NOT render in Notion (renders literally), confirmed by Richard 30-Apr-26.** Broker names always cited (not just "[AS]"). [D]
16. **Interpretive contradictions (15-Apr-26).** When [C] and [AS] disagree on interpretation (same data, different conclusion), the merged page must present both views with clear attribution. Do NOT resolve the disagreement — flag it visually (purple highlight) for APM/Richard to judge. Format: "**[Analytical disagreement]** [C] assessment: ... [AS] counter-view per [broker]: ... The disagreement centres on [specific point]." [D]
17. **Thin [AS] handling (15-Apr-26, thresholds revised 24-Apr-26).** When [AS] output is thin (<3,500 words or <40% of [C] length): fold unique [AS] insights into [C] as attributed footnotes or inline callouts. Do not restructure the page for thin [AS] — the merged page should read as a [C] page with [AS] enrichment. [D]
18. **RESEARCHER produces Information only — output feeds APM (15-Apr-26).** RESEARCHER is the Information layer in Richard's IAJA chain. It posts research memos to Notion Stock Notes and saves raw files locally. It does NOT make PARK / PROCEED / ESA verdicts — that is the APM's job. When a RESEARCHER session closes, Watson explicitly states: "These findings now feed the APM for Analysis + Judgement." Never collapse RESEARCHER and APM roles in the same session without Richard explicitly switching roles. Correction origin: 15-Apr-26. [D]
19. **Notion posting pre-flight gate — MANDATORY (20-Apr-26).** Before posting ANY page to the Stock Notes DB, Watson must: (a) read `notion-posting-standard/SKILL.md` in full, (b) fetch the Stock Notes DB schema via `notion-fetch collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2`. Confirm both done before first posting call. This gate is non-negotiable — it caught two failures on 20-Apr-26 (Stock(s) relation omitted, title format wrong) that were caused by Watson relying on cached knowledge instead of reading the live schema and SOP. [D]

20. **Stock(s) relation — mandatory on every Stock Notes posting (20-Apr-26).** Every page posted to Stock Notes DB must include the `Stock(s)` relation property set to the full Notion URL of the relevant stock page. Format: `["https://www.notion.so/{page_id_no_dashes}"]`. Without this field, pages are invisible in any Stock-filtered DB view. This is a BASIC requirement. Known stock page IDs are in `notion-posting-sop.md`; for unknown tickers, search Notion first (`notion-search`). Do not post without this field set. [D]

21. **M&A filing pre-flight — clarify acquirer vs target before creating any file or Notion page (20-Apr-26).** In any M&A situation, before creating a Files/{TICKER}/ folder or posting a Stock Notes page, explicitly confirm: is the investable case the acquirer, the target, or both? The answer determines the filing ticker. General rule: the acquirer is the investable case; the target is supporting intelligence filed under the acquirer's ticker. In bid/offer situations, research on the target's shareholder register, bid probability, and deal terms is all filed under the **acquirer's** ticker folder and tagged to the acquirer's stock page in Notion. Exception: if Richard is running a merger arb position on the target, clarify explicitly. Do not assume — ask if genuinely unclear. Correction origin: 20-Apr-26 (BYLOT/EVOK — initially filed under EVOK, corrected to BYLOT). [D]

22. **Auto-save research memos to structured COWORK/Files before posting (18-Apr-26, v2).** On sub-agent return (before formatting, highlighting, or Notion posting), save to the folder-per-ticker structure. This is both audit trail AND Watson's working memory for cross-session continuity. [D]
    - **Save sequence (mandatory, in order):**
      1. Create ticker folder if needed: `COWORK/Files/{TICKER}/`
      2. Create stage/query subfolder: `COWORK/Files/{TICKER}/{STAGE}/{QUERY-NUM}-{QUERY-NAME}/`
      3. Save raw memo: `raw.md` (single-source) or `raw-C.md` + `raw-AS.md` (dual-source)
      4. After cleaning/highlighting/formatting, save Notion-ready version: `notion-formatted.md` (single-source) or `merged.md` (dual-source — the version posted to Notion)
      5. Save `metadata.json` (source, word count, timestamps, Notion page_id after posting, page properties)
      6. Update per-ticker index: `COWORK/Files/{TICKER}/index.json`
      7. Update master index: `COWORK/Files/index-master.json`
      8. Regenerate human-readable summary: `COWORK/Files/{TICKER}/README.md`
      9. Proceed with Notion posting (unchanged)
    - **Folder mapping:** Queries 1-3 → `IG/`, 4-7 → `Triaging/`, 8-14 → `ESA/`, 15-19 → `DD/`, 20 → `DD/` (CEO/CFO Meeting Prep), 21-22 → `KQ/`, 23 → `Thematic/`
    - **Naming convention:** `{QUERY-NUM}-{QUERY-SHORT-NAME}/` e.g. `01-BD/`, `02-CF/`, `07-KD/`, `19-PreMortem/`
    - **Notion page properties stored in metadata.json:** title, stage, sentiment, tags, source, date_posted, page_id. Preserves future optionality for alternative display systems.
23. **Split writing voice — [C] concise, [AS] depth-first (18-Apr-26, revised 24-Apr-26).** Watson's own [C] research memos use concise writing: short declarative sentences, no filler, active voice, one clause per sentence — same breadth in tighter prose. **AlphaSense [AS] prompts do NOT use the concise voice instruction.** [AS] prompts instead mandate depth and completeness — "12-15 substantive bullet points per section, do not sacrifice depth for brevity." Rationale (24-Apr-26): the V2.4 concise voice instruction was being sent to AlphaSense Deep Research, a third-party LLM that interpreted "25% fewer words" as a license to produce dramatically shorter output. CKN BD came back at 2,535 words vs 7,000 minimum (36%). Empirical evidence across 144 metadata files confirmed a systematic post-V2.4 length drop. The fix: concise voice applies to Watson [C] only; [AS] receives the opposite instruction (depth-first). Min word counts restored to pre-V2.4 levels. See templates for per-query implementation. [D]
24. **Key findings summary (18-Apr-26).** Every research memo must open with a **Key Findings** section (5-10 bullets, each 1-2 sentences) before the detailed sections. This is a decision-relevant summary: what matters most, what's surprising, what needs attention. It is not an abstract — it is the sharpest version of the memo's conclusions, written last but placed first. [D]
25. **M&A research pre-flight: clarify acquirer vs target before filing (20-Apr-26).** When a research brief involves an M&A situation (bid, merger, acquisition), Watson must confirm before creating any Files/{TICKER}/ folder: (a) which entity is the investable case — the acquirer, the target, or both separately? (b) what is the correct ticker for each? File under the acquirer's ticker if the investment thesis is on the acquirer (e.g. BYLOT for Bally's/Intralot bidding for EVOK). The target's shareholder/situation analysis is intelligence feeding the acquirer's case — it goes in the acquirer's folder, not the target's. Correction origin: 20-Apr-26 (BYLOT/EVOK session — initially filed under EVOK before Richard clarified the case is BYLOT). [D]
26. **M&A bid price verification (20-Apr-26).** When a brief references a specific bid or offer price, always cross-check against the primary source (RNS / company announcement / Investegate) before building analysis. Share price and bid price are easily confused in fast-moving M&A situations. Verify within the first tool call — do not assume the brief is correct on specific numbers. Correction origin: 20-Apr-26 (brief stated 38.85p = prior day's close; actual bid = 50p). [D]

27. **Terminology relabel: CORE QUESTIONS / REQUIRED ATTRIBUTES (21-Apr-26).** Use **CORE QUESTIONS (CQs)** for what was previously "QUESTIONS"; use **REQUIRED ATTRIBUTES (RAs)** for what was previously "ATTRIBUTES." TARGET CONDITIONS (TCs) and Required Attribute Families (IC#1/2/3, BB#1–BB#8) are unchanged. The substance is unchanged — only the names. This sweeps across query templates, RESEARCHER outputs, and any reference to the rating taxonomy. Source of truth: `memory/projects/ratings-dashboard/memo-signposting-principles.md` v1.0. [D]

<!-- Rules #28, #29, #30 (added 28-Apr-26 morning) ABSORBED 28-Apr-26 into structural enforcement — see scheduled-tasks/CANONICAL-PROMPT.md and BRIEF-INTAKE-SOP.md. Specifically:
   - #28 (no request_cowork_directory in scheduled tasks) → CANONICAL-PROMPT.md Step 0 explicitly forbids it; templates do not contain the call.
   - #29 (verify fireAt in future, prefer existing executor over one-offs) → BRIEF-INTAKE-SOP.md Step 4 enforces TZ='Europe/London' date check; canonical template defaults to two-task split using existing executor where applicable.
   - #30 (planned future starts require a scheduled task) → BRIEF-INTAKE-SOP.md "Commit Ritual" makes the scheduled-task creation Step 4 inviolate; Step 5 read-back closes the loop before session ends.
The lessons remain in lessons-and-mistakes.md and in the "WHY THIS TEMPLATE LOOKS LIKE THIS" header of CANONICAL-PROMPT.md. -->

<!-- Rule #21 (unattended/overnight autonomy — no approval gates) ABSORBED 28-Apr-26 — this is a settings.json fact ("dangerouslySkipPermissions": true on Richard's Windows machine), not a rule for Watson to remember. Operationally it manifests as: the canonical scheduled-task templates do not call any tool that requires UI approval. -->

<!-- Per-task diligence + quality discipline survives in scheduled-task-preamble.md (loaded as Step 0 of every overnight task) and in the four "Inviolate Rules" at the bottom of CANONICAL-PROMPT.md. -->

29. **AS-first posting gate — dual-source queries cannot post until AS is in (28-Apr-26).** For any query whose Master Table source is `AS + C` (dual-source), do NOT post the Notion page until: (a) [AS] output has been extracted to `raw-AS.md`, (b) word-count + ticker validation passed (Rule #10), (c) pre-merge validation passed (Rule #14), (d) merge written to `merged.md`. Posting `[C]`-only for a dual-source query is **only permitted** if Rule #14 has explicitly failed and the failure has been logged with reason. Posting prematurely because AS "looks slow" or "might not come back" is forbidden — wait, defer, or escalate. Single-source queries (`C` only or `AS` only) are unaffected. This rule applies in both live-session and scheduled/unattended contexts. Structurally enforced for scheduled tasks via the AS-FIRST GATE in `scheduled-tasks/CANONICAL-PROMPT.md` Inviolate Rule #5 + Task B Step 3. Correction origin: 28-Apr-26 (pattern observed across multiple sessions where Watson wanted to post [C] memos before AS extraction). [D]

30. **Four-phase AS execution model — close Chrome between phases (30-Apr-26).** AS workflow runs as four discrete phases, each with its own context. Phase 1 (live session, immediately on brief sign-off): submit AS via Haiku, run §Step 3a five-check verification, **close Chrome window entirely**. Phase 2 (scheduled task, 02:00 UK or ≥3h post-submission, whichever later): cold-reopen fresh Chrome window per thread, extract via PDF Download, close window. Phase 3 (scheduled task, ~02:30): merge dual-source pairs per Rule #14/#15, write `merged.md` + `qc-audit.md`. Phase 4 (scheduled task, ~03:00): publish to Notion + dashboard. Watson does NOT keep Chrome alive across phases, does NOT monitor progress, does NOT "do other work while waiting." Rationale: Chrome tab discard / Memory Saver / renderer-hang / blank-pane failure modes (which all require kept-alive Chrome) are eliminated structurally by closing Chrome between Phase 1 and Phase 2. AS auth cookies persist across browser restarts — Phase 2 lands on the same authenticated session. Full protocol: `as-claude-research-sop-v2.md` Four-Phase Execution Model section. Locked 30-Apr-26 per Richard's instruction. [D]

31. **Auto-resubmit broken AS threads — extraction is free, waiting on broken threads is not (30-Apr-26).** During Phase 2 extraction, if a thread fails to render (no Download button visible, blank pane, error) — retry 2-3 times over a 15-minute window with fresh tabs. If still failing AFTER 15 min of retries AND the original submission was >120 min ago, treat the thread as "broken" and **resubmit fresh in a new Chrome window**. Re-read the prompt from `as-thread.json` (`prompt_text` field), submit per Phase 1 protocol, capture new URL, mark old thread `status: BROKEN_RESUBMITTED`, defer extraction of new thread to next Phase 2 cycle (≥45 min later). Rationale: AS does not allow editing or restarting threads — they must be resubmitted. AS resubmissions cost nothing (free per Richard's confirmation 30-Apr-26). The 120-min threshold is 2× upper bound of typical 60-min generation time. Below 120 min, thread may genuinely still be processing — defer to next Phase 2 cycle. Above 120 min, thread is overwhelmingly likely broken — empirical evidence: BGN 29-Apr overnight, 5/6 threads at 0% progress 24h+ post-submission. Provenance preserved in `as-thread.json` thread chain. Surfaces in QC footer block as "Auto-resubmit triggered? Yes (original X, new Y)". Escalation: if a SECOND auto-resubmission also fails 120 min later → STOP, surface `🚨 AS_REPEATED_FAILURE` to morning briefing, indicates AS service degradation. Full decision tree: `as-claude-research-sop-v2.md` Rule #31 section. [D]

32. **QC audit footer block — mandatory on every Notion memo (30-Apr-26).** Every Notion memo posted by RESEARCHER must include (a) a coloured QC headline status pill at the very TOP of the page (✅ PASS / ⚠️ BELOW TARGET / 🟡 AS-LITE / ❌ FAILED) and (b) a QC audit footer block at the very BOTTOM showing word counts (target vs actual for AS / C / merged), quality checklist, friction flags (incl. Rule #31 auto-resubmit triggers), and full provenance (URLs, timestamps, file paths). Both pill and footer are **auto-generated from `metadata.json`** by `scripts/generate_qc_footer.py` — NOT written by the agent that produced the memo. This prevents the "self-written completion flag can lie" failure pattern (28-Apr-26 watchdog lesson). Concurrently with posting, write `qc-audit.md` to the query folder for offline / weekly roll-up consumption. Rationale: Richard's "quick-check trust" objective — must be able to glance at any memo and know whether to trust it without scrolling. Full spec: `notion-posting-sop.md` §Step 4.5. [D]

33. **Brief-card append protocol — never overwrite, banned suffixed variants (30-Apr-26).** When Richard briefs RESEARCHER for overnight execution and a brief-card already exists for the night-of-execution, Watson must **read-modify-write append**, never call `Write` with new content as the only payload. Mandatory sequence: (2a) Read existing brief-card if present, capture full content. (2b) If exists: append new ticker block(s) to existing content. (2c) If not exists: create with single ticker block + manifest header. (2d) After write: re-read the file and verify (i) all prior ticker blocks present, (ii) new ticker blocks added, (iii) no duplicate sections. Every brief-card has a YAML-style **manifest header** at top (blocks, blocks_count, last_appended timestamp, total_expected_pages) which the SOP requires Watson to update on every append. Idempotent validator: count `## BRIEF BLOCK` headers in body, must match manifest `blocks_count`; mismatch = corruption flag. **Banned: suffixed brief-card variants (`-esa-`, `-bgn-`, etc.).** One brief-card per night-of-execution, period. Recovery from corruption = restore from backup + append, NOT create sibling file. Rationale: 28/29-Apr-26 — Block 1 brief-card overwrote Block 3, recovery created `researcher-brief-esa-2026-04-29.md` sibling fragmenting the watchdog's "single brief-card per night" assumption. Full spec: `scheduled-tasks/BRIEF-INTAKE-SOP.md` Step 2 (revised v2.0 30-Apr-26). [D]

34. **Communication Principles — role-scoped application (30-Apr-26; amended 06-May-26 per D-RSR-3/D-RSR-10).** Every RESEARCHER memo (single-source and merged) must apply three of the four Communication Principles per `memory/skills/communication-principles/SKILL.md`: (#1) quantitative claims include peer / base-rate context wherever sourced — **cross-role, applies to RESEARCHER**; (#3) findings clearly worse than peer median get `❌` prefix — **cross-role, applies to RESEARCHER** (RESEARCHER surfaces, does NOT grade); (#4) outliers (rare, unusual, edge-case, surprising) get `⚡` markers (per Concepts A+B Operating Disciplines, D-RSR-33) with Means/Motive/Opportunity test — **cross-role, applies to RESEARCHER**. Principle #2 (A/B/C/D/F grading against bell curve) is **APM-ONLY** — RESEARCHER never applies letter grades (D-RSR-3). RESEARCHER provides J-front verbal verdicts and peer-anchored findings; APM converts these to grades. The QC audit footer block (notion-posting-sop.md §Step 4.5) reports compliance per applicable principle. Full spec: `memory/skills/communication-principles/SKILL.md`. [D]

37. **Wisdom Library pre-query consult — load institutional pattern-memory before any AS submission or [C] query (03-May-26 v2.11).** Before submitting any AS prompt or running any [C] query for a stock, RESEARCHER must query `wisdom-library/INDEX.json` for matching models by (a) **industry / sector** (e.g. med-tech, semi-cap, cables), (b) **setup-archetype** (Demand-Driven EPSU, Corporate Change EPSU/EPT, Product Cycle, Earnings Upgrade Cycle), (c) **business-model** (serial acquirer, asset-light services, R&D-heavy), (d) **risk profile** (cyclical, defensive, structural-change). Load 5-10 matching models — read each `.md` file in full. The library tells RESEARCHER what specific signals / data points / risks to look for in this kind of case (and which to deprioritise as noise). Cite the consulted models in the Key Findings preamble of each query output. Rationale: RESEARCHER is the front-end of the bookend pattern with APM (AJ SOP v2.3 §Phase 0.2) and session-handoff (SKILL V2 §Step 5.5). Without library consult, RESEARCHER queries follow generic templates and miss case-specific signal vs noise distinctions. Per Wisdom Library entry `memory-needs-workflow-binding` (Bronze) — memory entries don't enforce behaviour without workflow binding; this rule IS the workflow binding for "consult library before researching." Cross-ref: `wisdom-library/SKILL.md` (consultation conventions); `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.3 §Phase 0.2 (APM consults same library before reading RESEARCHER output); `memory/skills/session-handoff/SKILL.md` §Step 5.5 (WL survey + propose new entries at session close). [D]

38. **Cohort manifest pre-consult — inherit cohort context before any per-stock query dispatch (04-May-26 v2.12).** Before any per-stock query dispatch (Sonnet [C] sub-agent OR Haiku [AS] submission), RESEARCHER must check `memory/staging/cohort-*-*.md` for an active cohort manifest containing the active ticker. **If cohort manifest exists for this ticker:** (a) read the cohort manifest in full; (b) read the cohort-shared-context memo at `databases/memos/_cohort/{cohort-name}/shared-context.md`; (c) cite cohort manifest path + shared-context memo path in the per-stock query template's `cohort_context_path` placeholder; (d) include cohort-shared-context as the FIRST context block in the sub-agent prompt (cohort context first, query template second); (e) inherit cohort-level CQ precommits — the per-stock memo MUST address each cohort CQ explicitly (informs differential ranking at cohort hot wash); (f) Rule #37 (WL pre-query consult) runs in **DELTA-ONLY MODE** — load only WL models NOT already in the cohort precommit list. **If NO cohort manifest exists:** EITHER (a) author cohort manifest now per `memory/skills/cohort-research-analysis-judgement/SKILL.md` §3 + pause query dispatch until manifest signed off, OR (b) declare SOLO REACTIVE MODE explicitly with reason logged to `memory/staging/solo-reactive-log.md` (per cohort SKILL §2.5 — restricted triggers only; STILL load ≥2 closest-archive peer memos as comparative context); Rule #37 runs in full mode. Rationale: per-stock RESEARCHER work is the front-end of the cohort layer. Without manifest pre-consult, sub-agents re-derive shared context per stock (token waste) and miss cohort-level precommits that should anchor the per-stock work. Empirical case: 03-May-26 EKTA/HTRO/PRY/COTN-CH session produced 5 cross-stock WL entries that no per-stock memo could surface in isolation — the cohort hot wash at Phase 4.6 captures those, but only if Rule #38 + Phase 0.0 fire to set up the comparative context upstream. **NEW v2.12.1:** cohort status is read from the RESEARCH STAGES dashboard data feed (single source of truth — per cohort SKILL §3.2 v1.1), NOT from manifest text. **NEW v2.12.1 — Query #8 unchanged:** the cohort-shared-context briefing memo authored at cohort manifest Step 6 does NOT replace per-stock Query #8 (BM/Sector Primer at ESA). Query #8 stays full-size at ~3,000-word target, unchanged. Cohort briefing memo and Query #8 serve different audiences/purposes (cohort briefing = Watson context + Richard cohort-level reading; Query #8 = full per-stock reading document). Cross-ref: `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.1 (master cohort SOP); `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.4.1 §Phase 0.0 (APM mirror of this rule); `memory/skills/session-handoff/SKILL.md` §Step 5.5.0 (cohort presence check at session close). [D]

36. **Strip ==text== syntax before posting to Notion — invalid markup, renders as literal characters (03-May-26).** AlphaSense Deep Research output natively contains `==highlighted text==` syntax throughout. Notion does NOT support this syntax — it renders as literal `==text==` rather than yellow highlight (confirmed 03-May-26 QC audit, gym sector ESA batch). During Phase 3 (merge) or Phase 4 (posting), before any `write_to_notion` call, run a pre-posting strip: replace all `==text==` occurrences with either `**text**` (bold, for high-emphasis content) or plain text (where the `==` was purely decorative emphasis). This applies to: raw-AS.md content, merged.md content, and any inline paste into Notion page content. The strip must happen at the content-preparation stage, not as a retroactive fix. Implementation: add as a pre-processing step in `process_report.py` or equivalent pipeline script. Pattern: `re.sub(r'==([^=]+)==', r'**\1**', content)`. Rationale: `==text==` in Notion output is visually noisy (literal `==` characters cluttering every line) and signals a broken pipeline to any reader. Correction origin: 03-May-26 QC audit discovered all 15 AS-sourced gym memos affected. Rule logged in `memory/corrections.md` 03-May-26. [D]

28. **Signposting-aware output structuring (21-Apr-26).** RESEARCHER produces Information; APM converts that Information into a signposted memo where every parent bullet in C.II answers a specific CQ/RA/TC. To make APM's job easier, RESEARCHER outputs (especially queries that map cleanly onto a Required Attribute Family — e.g. #2 Change Forces → IC#2; #5 Earnings Delivery → IC#1; #7 KD Assessment → IC#1/IC#2 inputs) should be **organised by CQ where the framework supports it**. When a section maps onto a known CQ (e.g. "External change forces / tailwinds" = IC#2 CQ1), label the section with the CQ reference in the heading. Do not invent CQs that don't exist in the pillar detail JSONs. The goal is to give APM a head start on signposting, not to replace APM's signposting work. Source of truth: `memory/projects/ratings-dashboard/memo-signposting-principles.md` v1.0. [D]

---

## Operating Disciplines (Concepts A + B)

These two disciplines are LOAD-BEARING for every RESEARCHER memo. They sit alongside (not subordinate to) the validation rules, the v2.1 pattern, and the Notion posting standard. They reflect the cognitive architecture Richard expects of analytical work — they are *what makes the memo earn its keep*.

### Concept A — Look at the Edges (Outlier Detection Discipline)

**Core claim:** Indicators of outlier potential change dynamics live at the **edges, the cross-roads, and the outliers** — not in the consensus middle. Train the eye to spot what is *deliberately weird*. Internal cue: "things that make me go *hmmmm*".

**Operational rules:**
1. **⚡ marker is mandatory in every Aggregate Outliers block.** It encompasses (a) statistical outliers vs cohort, (b) qualitative oddities the operator has not explained, (c) cross-roads exposures the consensus is ignoring. (Switched from 🚩 per D-RSR-33.)
2. **For each ⚡ flagged in a memo:** apply the Means / Motive / Opportunity test. Name the actor, the capability, the incentive, the window. Flags that fail one or more legs are tagged "watch only" rather than "elevate".
3. **Source-incentive line per channel:** before extracting from sell-side, expert-call, management, or regulator material, name the source's incentive. The Power-of-Incentives discipline (Munger) is the FIRST tool, not a footnote.
4. **Edges register:** maintain a "things-that-make-me-go-hmmmm" running list per ticker in the file's Notion brief-card.
5. **WH Smith CEO archetype (illustrative):** non-traditional operator backgrounds and unconventional questions are themselves edge-signals. Catalogue them; don't filter them.

**Load-bearing reading list (consult before any Triaging-or-deeper memo):**
- Wisdom Library (Gold): `look-at-the-edges-deliberately-weird`
- Wisdom Library (Gold): `means-motive-opportunity`
- Wisdom Library (Gold): `power-of-incentives-munger`
- Wisdom Library (Gold): `outlier-flagging-rare-data`

### Concept B — Three CRITICAL ACTIONS (Cognitive Discipline Under Disagreement)

**Core claim:** There are hundreds of biases people quote. Three CRITICAL ACTIONS counter the most consequential ones — the ones that *prevent* the analyst from updating in the face of edge-signals.

**CRITICAL ACTION 1 — Go to the most-different viewpoint.**
*The Stoic move (Marcus Aurelius): the obstacle is the way.* When you encounter contradictory evidence, do NOT discount it. Engage it. Build the case FOR the contradiction before you resume the leading view. The bear note in a BUY-stack environment is rarely wrong by accident. The expert who contradicts the management narrative is the lead, not the footnote.

*Operational form in memos:* §10/§11/§12 sceptical lens treatment is LOAD-BEARING, not perfunctory. The "and yet" bullet must engage the most-different viewpoint, not paraphrase the leading view in a softer key.

**CRITICAL ACTION 2 — Stew until uncomfortable.**
*The slow-thinking discipline.* Premature analytical closure is the most common failure mode. The first answer (30 minutes in) is almost always the legible/consensus answer. The non-consensus answer requires staying in the valley of despair — the cognitive territory between "first hypothesis collapsed" and "better hypothesis arrived" — until the resolution is *earned*, not rushed.

*Operational form in memos:* don't write the verdict in the first sitting where the work spans multiple sessions. Externalise the stew as bullets in §10/§11/§12. The discomfort cue is the metric.

**CRITICAL ACTION 3 — Multiple truths can coexist.**
*The Buddhist parable (six blind men and the elephant).* When two evidence-based views appear to contradict, the most common situation is that BOTH are partially correct. Synthesise before resolving. Name the elephant — the underlying composite truth that contains both partial views.

*Operational form in memos:* PRO/CON structures and peer-cohort dispersion data must be treated as elephant-touching exercises, not binaries. The synthesis paragraph is more important than either side.

**The 3-Check Declaration before any memo is marked complete:**

Every RESEARCHER memo (Triaging-or-deeper) must include a 3-line declaration in the QC Commentary block (or §13 if no QC block) confirming:

1. **Counter-hypothesis check (AI-Dunning-Kruger):** "I have generated a counter-hypothesis with at least one piece of disconfirming evidence that, if true, would invalidate the leading view. Specifically: [counter-hypothesis stated; disconfirming evidence cited]."

2. **ACH check:** "I have considered ≥3 plausible competing hypotheses and named which has the FEWEST hard inconsistencies. The leading view is the one with the fewest disconfirming items, not the one with the most supporting items."

3. **Multiple-truths check:** "Where my analysis surfaced apparent contradictions between sources, I have identified the underlying composite truth that contains both partial views, rather than picking one and discarding the other."

If the analyst (or the LLM acting in the RESEARCHER role) cannot truthfully tick all three, the memo is NOT complete. Return to stewing.

**Load-bearing reading list (consult before any Triaging-or-deeper memo):**
- Wisdom Library (Gold): `the-obstacle-is-the-way-marcus-aurelius`
- Wisdom Library (Gold): `stewing-and-the-valley-of-despair`
- Wisdom Library (Gold): `multiple-truths-coexist-six-blind-men`
- Wisdom Library (Gold): `analysis-of-competing-hypotheses-heuer`

### Cross-cutting reminder

Concepts A + B are paired by design. Concept A spots the edge; Concept B prevents the analyst from rationalising it away. Without B, A produces interesting flags that don't survive review. Without A, B produces well-disciplined analysis of consensus data. Both together are the structural source of analytical edge.

---

## The 23-Query Framework

### Master Table

| # | Stage | Query | Source(s) | Template File | Min Words | Notion Pages |
|---|-------|-------|-----------|---------------|-----------|--------------|
| 1 | IG | Business Description | AS + C | `templates/01-ig-bd.md` | 7,000 | 1 merged [C+AS] |
| 2 | IG | Fundamental Change Forces | AS + C | `templates/02-ig-cf.md` | 4,000 | 1 merged [C+AS] |
| 3 | IG | Technical Momentum | C | `templates/03-ig-tm.md` | 3,000 | 1 [C] + chart screenshots |
| 4 | Triaging | Earnings trends vs. peers (L2Yish) | AS + C | `templates/04-triaging-earnings-trends.md` | 3,000 | 1 merged [C+AS] |
| 5 | Triaging | Most recent earnings delivery (L6Mish) | AS + C | `templates/05-triaging-earnings-delivery.md` | 3,000 | 1 merged [C+AS] |
| 6 | Triaging | Sell-Side Commentary Summary | AS | `templates/06-triaging-ss-commentary.md` | 3,000 | 1 [AS] |
| 7 | Triaging | Watson's Assessment of Key Drivers — Triaging | AS + C | `templates/07-triaging-kd-assessment.md` | 3,000 | 1 merged [C+AS] |
| 8 | ESA | Business Model / Sector Primer | AS + C | `templates/08-esa-bm-sector-primer.md` | 3,000 | 1 merged [C+AS] |
| 9 | ESA | Earnings delivery record (L3Yish) | AS | `templates/09-esa-earnings-history.md` | 3,000 | 1 [AS] |
| 10 | ESA | Short-Sellers' Reports | AS + C | `templates/10-esa-short-sellers.md` | 3,000 | 1 merged [C+AS] |
| 11 | ESA | Value chain info map | C | `templates/11-esa-value-chain-map.md` | 3,000 | 1 [C] |
| 12 | ESA | Value-Chain Analysis | AS | `templates/12-esa-value-chain-analysis.md` | 3,000 | 1 [AS] |
| 13 | ESA | Guidance and Tracking Versus | AS | `templates/13-esa-guidance-tracking.md` | 3,000 | 1 [AS] |
| 14 | ESA | Watson KD Assessment — ESA | AS + C | `templates/14-esa-kd-assessment.md` | 4,000 | 1 merged [C+AS] |
| 15 | DD | Insider / Expert Comments | AS | `templates/15-dd-insider-comments.md` | 3,000 | 1 [AS] |
| 16 | DD | Management and Governance Checks | C | `templates/16-dd-mgmt-governance.md` | 3,000 | 1 [C] |
| 17 | DD | FX Exposure | C | `templates/17-dd-fx-exposure.md` | 3,000 | 1 [C] |
| 18 | DD | CEO Research | AS | `templates/18-dd-ceo-research.md` | 3,000 | 1 [AS] |
| 19 | DD | Pre-mortem | AS + C | `templates/19-dd-premortem.md` | 4,000 | 1 merged [C+AS] |
| 20 | DD | CEO/CFO Meeting Prep | AS + C | `templates/20-dd-ceo-cfo-meeting-prep.md` | 3,000 | 1 merged [C+AS] |
| 21 | Any | KQ — Research (breadth-first) | AS + C [default dual] | `templates/21-kq-research.md` | 3,000 | 1-2 |
| 22 | Any | KQ — Analysis (ACH-disciplined) | AS + C [default dual] | `templates/22-kq-analysis.md` | 3,000 | 1-2 |
| 23 | Any | Thematic Research | AS + C (always dual) | `templates/23-thematic-research.md` | 2,500 | 1 merged [C+AS] per thematic |

### Page Count Summary by Stage

| Stage | Queries | Max Pages | Notes |
|-------|---------|-----------|-------|
| IG | #1-3 | 3 | 2 merged (#1, #2) + 1 C-only (#3) |
| Triaging | #4-7 | 4 | 3 merged (#4, #5, #7) + 1 AS-only (#6) |
| ESA | #8-14 | 7 | 3 merged (#8, #10, #14) + 3 AS-only (#9, #12, #13) + 1 C-only (#11) |
| DD | #15-19 | 5 | 1 merged (#19) + 2 AS-only (#15, #18) + 2 C-only (#16, #17) |
| Any | #20-23 | Variable | 1 merged per query (#20); #21-#22 = 1-2; #23 = 1 merged per thematic |

**IG + Triaging combined: 7 pages per stock.** ESA: 7 pages. DD: 5 pages. **Full IG-to-DD: 19 core pages per stock** (down from 24 under the old 2-page-per-dual-source approach for ESA/DD queries).

---

## Stage Execution Flows

### IG (Stage 1) — Ideas Generation

**Purpose:** Fast pattern-matching. Does this stock warrant further work?

**Queries:** #1 (BD), #2 (CF), #3 (TM)

**Execution:**
1. Adapt #1 and #2 templates: fill in ticker, company name, industry, peers, any angles Richard flagged
2. For #3 (TM) — **Master Dashboard-first protocol (24-Apr-26, replaces 16-Apr-26 monitor-first):**
   - Check `COWORK/master-dashboard/data/prices.json` and `filter-results.json` for the ticker. These provide MA levels, MM99 score, filter qualification stages, and RS data.
   - **If found in MD:** Use MD data as the quantitative backbone for MA structure, MM99 score, and RS. Supplement with `COWORK/pullback-data.json` for 10-signal composite depth, base count, violations, and red flags (temporary — pullback monitor will be deprecated into MD). Capture chart screenshots from `master-dashboard.html` chart panel (candlesticks, 7 MAs, volume, OBV) at available timeframes. Launch #3 immediately.
   - **If not found in MD:** Add stock to `master-dashboard/data/universe.json`. Inform Richard to run `python generate_master_data.py --full-universe`. Park #3 and continue with #1 and #2. Resume #3 once Richard confirms data is refreshed.
   - Full protocol in template `03-ig-tm.md`. [D]
3. Dispatch [C] agents in parallel (Sonnet): #1-C, #2-C, and #3-C launch simultaneously (or #3 once monitor data confirmed available)
4. Dispatch [AS] agents via Haiku: #1-AS and #2-AS submitted to AlphaSense
5. [C] agents complete in minutes → validate output
6. After 45+ min, Sonnet extracts [AS] outputs → validate output
7. Run pre-merge validation gate (rule #14) on #1 [C]+[AS] pair and #2 [C]+[AS] pair
8. For #1 and #2: merge each into single [C+AS] page per backbone defaults (rule #14). #1 backbone = [AS] (broker initiation reports provide richer factual base; [C] enriches with analytical framing, cross-sector parallels, quality flags). Save raw outputs to `COWORK/outputs/{ticker}/raw/`
9. Post all pages to Notion with 30%+ highlighting (2 merged #1+#2 + 1 C-only #3 = 3 pages). Embed chart screenshots in #3 page.
10. Run posting verification spot-check

**Outputs:** 3 Notion pages per stock (2 merged [C+AS] + 1 C-only). No IAJA synthesis at IG.

**Title format (updated 16-Apr-26 — company name removed, summary expanded):**
- Single-source: `[W] {TICKER} - IG - {Query Name} - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY`
- Merged: `[W] {TICKER} - IG - {Query Name} - {5-15 word summary} [C+AS] @ DD-Mon-YY`
- Summary = substantive descriptor of the page's central finding/message. See notion-posting-standard/SKILL.md §8 for worked examples.

**Batch execution (cycling multiple stocks):**
- [C] prompts: all simultaneously as parallel Sonnet agents. No concurrency limit.
- [AS] prompts: Haiku submits sequentially — ONE AGENT AT A TIME (revised 28-Apr-26). **Do NOT dispatch concurrent Haiku agents for AS submission.** Concurrent agents share browser session state in AlphaSense's SPA: they cross-navigate into each other's threads and return duplicate/incorrect URLs. Sequential submission is slower but produces reliable, distinct thread URLs. AlphaSense limit: up to 10 Deep Research reports in queue at once (confirmed 15-Apr-26). For IG batches of ≤5 stocks (≤10 AS reports), single wave is sufficient.
- **URL capture rule:** Haiku must record the thread URL at step 10 immediately after submission — do not navigate away then try to recover the URL. If the URL is still generic (no thread ID) at step 10, wait 5 seconds and re-check before reporting.
- **Fallback confirmation:** If thread URL cannot be confirmed, check sidebar via `document.body.innerText` scan for the thread title with "Deep Research" label. Thread title confirmation is sufficient; exact URL can be recovered at extraction time by clicking the sidebar item.
- Optimal: while [AS] Wave 1 processes, Sonnet completes all [C] research + posting.

**Automated IG (8/8 Minervini trigger):** Full SOP in `memory/skills/auto-ig-research/SKILL.md`. Nightly 23:30 UK + mid-week Wed 22:00 UK. 5 stocks/night cap. **Data source:** Master Dashboard `filter-results.json` → MM99 filter → `score` field (replaces `snapshots/minervini-history.json`).

---

### Triaging (Stage 2)

**Purpose:** Fast, disciplined filtering. Does this stock fit a recognisable setup profile? Is the fulcrum driver plausible? Any immediate disqualifiers? LIGHT depth. Pattern recognition + "strong views, weakly held."

**Queries:** #4 (Earnings Trends), #5 (Earnings Delivery), #6 (SS Commentary), #7 (KD Assessment)

**Execution:**
1. Read ALL existing Stock Notes pages for the ticker
2. Adapt templates #4-7: fill in ticker, company, industry, peers
3. Dispatch [C] agents in parallel (Sonnet): #4-C, #5-C, #7-C
4. Dispatch [AS] agents via Haiku: #4-AS, #5-AS, #6-AS, #7-AS
5. On return: run pre-merge validation gate (rule #14) on each [C]+[AS] pair (#4, #5, #7)
6. For validated pairs: merge into single [C+AS] page per backbone defaults (rule #14). Save raw outputs to `COWORK/outputs/{ticker}/raw/`
7. For failed validation: post [C]-only page. Save [AS] as local reference
8. Post all pages to Notion with 30%+ highlighting (3 merged + 1 AS-only #6 = 4 pages)
9. Run posting verification

**#7 (Watson KD Assessment — Triaging):** Standalone. Watson's first-pass hypothesis on key drivers based on IG research + Triaging #4-6 output. No Notion reading prerequisite beyond what's already posted. No APM dependency.

**Outputs:** 4 Notion pages per stock (3 merged + 1 AS-only). No IAJA synthesis at Triaging.

**Title format (updated 16-Apr-26 — company name removed, summary expanded):**
- Single-source: `[W] {TICKER} - Triaging - {Query Name} - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY`
- Merged: `[W] {TICKER} - Triaging - {Query Name} - {5-15 word summary} [C+AS] @ DD-Mon-YY`
- Summary = substantive descriptor of the page's central finding/message. See notion-posting-standard/SKILL.md §8 for worked examples.

---

### ESA (Stage 3) — Early-Stage Assessment

**Purpose:** Dual purpose: (1) interrogate the change thesis — is the change significant enough? Is management dynamic enough? Are required outputs compelling? (2) Breadth coverage — ensure ALL aspects of the investment case are covered at light or medium depth. The setup title crystallises during ESA.

**Queries:** #8 (BM/Sector Primer), #9 (Earnings History L3Y), #10 (Short-Sellers), #11 (Value-Chain Map), #12 (Value-Chain Analysis), #13 (Guidance/Tracking), #14 (Watson KD Assessment — ESA)

**Execution — Three-Phase Structure (Research → APM → Research):**

**Pass 1 (queries #8-13):**
1. Read ALL existing Stock Notes pages for the ticker
2. Read Claude system notes / prior Watson work on the stock
3. Adapt templates #8-13: fill in ticker, company, industry, peers
4. Dispatch [C] agents in parallel (Sonnet): #8-C, #10-C, #11-C
5. Dispatch [AS] agents via Haiku: #8-AS, #9-AS, #10-AS, #12-AS, #13-AS
6. Run pre-merge validation gate (rule #14) on #8 [C]+[AS] pair and #10 [C]+[AS] pair
7. For #8 and #10: merge each into single [C+AS] page per backbone defaults (rule #14). #8 backbone = [AS]; #10 backbone = [C]. Save raw outputs to `COWORK/outputs/{ticker}/raw/`
8. Post all pages to Notion with 30%+ highlighting (2 merged #8+#10 + 1 AS-only #9 + 1 C-only #11 + 1 AS-only #12 + 1 AS-only #13 = 6 pages)
9. Run posting verification

**Interlude — APM Analysis + Judgement:**
- APM role reads all RESEARCHER output posted in Pass 1
- APM runs FCS Analysis + Judgement (per `fundamental-change-screen/apm-analysis-sop.md` and `apm-judgement-sop.md`)
- APM posts Analysis + Judgement to Notion

**Pass 2 (query #14 — dependent on APM):**
1. RESEARCHER reads APM's posted Analysis + Judgement from Notion
2. Adapt template #14 using APM's identified key drivers as input
3. Dispatch #14-C (Sonnet): Watson's own KD synthesis informed by APM's view
4. Dispatch #14-AS (Haiku): targeted AS Deep Research on the specific KDs APM flagged
5. Run pre-merge validation gate (rule #14) on #14 [C]+[AS] pair
6. Merge #14 into single [C+AS] page per backbone defaults (rule #14). #14 backbone = [C]. Save raw outputs to `COWORK/outputs/{ticker}/raw/`
7. Post merged page to Notion with 30%+ highlighting (1 merged #14)
8. Run posting verification
9. IAJA synthesis at end of ESA stage (uses [W] tag)

**#14 dependency is explicit.** #14 CANNOT run until APM has posted its Analysis + Judgement. If APM work is not yet complete, RESEARCHER parks #14 and flags to Richard.

**Outputs:** Up to 7 Notion pages (3 merged [C+AS] + 3 AS-only + 1 C-only) + IAJA synthesis [W] page.

**Title format (updated 16-Apr-26 — company name removed, summary expanded):** `[W] {TICKER} - ESA - {Query Name} - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY` — Summary = substantive descriptor of central finding. See notion-posting-standard/SKILL.md §8.

**Template selection:** Watson selects which ESA templates to run based on Richard's brief, what's already available from IG/Triaging, and the central change thesis. Watson proposes a template plan for sign-off if Richard hasn't specified a subset. TEST prompts (e.g., Short Seller All 10 TEST) are NOT auto-run — ask Richard.

---

### DD (Stage 4) — Deep-Dive

**Purpose:** Resolve key questions from ESA. Stress-test the fulcrum driver thesis. Fill gaps, complete the case. ALL 13 FCS categories at ROBUST depth.

**Queries:** #15 (Insider/Expert), #16 (Mgmt & Governance), #17 (FX Exposure), #18 (CEO Research), #19 (Pre-mortem)

**Execution:**
1. Read ALL existing Stock Notes pages for the ticker
2. Read Claude system notes / prior Watson work
3. Adapt templates #15-19
4. Dispatch [C] agents (Sonnet): #16-C, #17-C, #19-C
5. Dispatch [AS] agents (Haiku): #15-AS, #18-AS, #19-AS
6. Run pre-merge validation gate (rule #14) on #19 [C]+[AS] pair
7. Merge #19 into single [C+AS] page per backbone defaults (rule #14). #19 backbone = [C]. Save raw outputs to `COWORK/outputs/{ticker}/raw/`
8. Post all pages to Notion with 30%+ highlighting (1 merged #19 + 2 AS-only #15/#18 + 2 C-only #16/#17 = 5 pages)
9. Run posting verification
10. IAJA synthesis at end of DD stage

**Outputs:** Up to 5 Notion pages (1 merged [C+AS] + 2 AS-only + 2 C-only) + IAJA synthesis [W] page.

**Title format (updated 16-Apr-26 — company name removed, summary expanded):** `[W] {TICKER} - DD - {Query Name} - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY` — Summary = substantive descriptor of central finding. See notion-posting-standard/SKILL.md §8.

---

### Any Stage — CEO/CFO Meeting Prep and KQs

**Queries:** #20 (CEO/CFO Meeting Prep), #21 (KQ Research), #22 (KQ Analysis)

**#20: CEO/CFO Meeting Prep** (renumbered per D-RSR-32)

Preparation for management meetings. Source: AS + C dual-source (default). When dual-source: merge into single [C+AS] page per backbone defaults (rule #14, #20 backbone = [C]). **Posted to Notion** (unlike the old IR Contact template which was chat-only).

**#21 and #22: Key Questions**

KQs arise at any stage but most commonly from ESA onwards.

Two types:
- **#21 — KQ Research:** Broad research. Landscape, data, sources.
- **#22 — KQ Analysis:** Framework-driven analysis. Judgement-heavy. ACH-disciplined.

Default: #21 Research. Watson infers from context. Only use #22 when clearly a judgement/framework question.

Source: AS + C dual-source (default per D-RSR-37). When dual-source: merge into single [C+AS] page per backbone defaults (rule #14). Watson asks Richard which source(s) to use for each KQ. If Richard doesn't specify, Watson recommends based on whether the KQ benefits from proprietary data (AS) or public analysis (C) or both.

**Title format (CEO/CFO):** `[W] {TICKER} - {Stage} - CEO/CFO Questions - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY`
**Title format (KQs):** `[W] {TICKER} - {Stage} - {KQ Title} KQ - {5-15 word summary} [{SOURCE}] @ DD-Mon-YY`
*Company name NOT included. Summary = substantive descriptor of the page's central message.*

---

## EARNINGS

- **Pre-earnings:** Consensus estimates, key driver tracking, bull/bear scenarios. Uses KQ templates (#21/#22) or custom brief. Posted to Notion.
- **Post-earnings:** Key data points, assess vs expectations, flag thesis implications. Immediate reaction note + detailed analysis within 24h. Uses Triaging #5 (Earnings Delivery) template adapted for the specific reporting period.

---

## IR CONTACT (not in the query framework)

The old IR Contact template (`Watson - Triaging - IR contact - REFV01_RB.docx`) is **returned in chat only — NOT posted to Notion.** It is not part of the research query framework but remains available as a utility template for preparing IR outreach questions. If Richard requests it, Watson adapts the template and returns the output in conversation.

---

## Self-Contained Template Architecture

### Design Principle

Each template file in `templates/` is a **complete agent brief** — the research sub-agent receives ONLY its template (filled in with ticker/company/peers) and produces the memo. No SOP loading, no philosophy files, no posting instructions.

### Template Structure (every template follows this)

```
# Query {#}: {Name} — {Source}

## MISSION
What this query produces. Word count target. Output sections.

## CONTEXT
Investment system context relevant to THIS query only.
Extracted from philosophy.md, strategy.md, etc.
NOT: exit rules, sizing, posting mechanics, other queries.

## PROMPT — [{SOURCE}] Version
The actual research prompt with placeholders:
{TICKER}, {COMPANY}, {INDUSTRY}, {PEERS}

## EXECUTION
Source-specific instructions:
- For [C]: "Use WebSearch extensively. No sell-side/expert references."
- For [AS]: "This prompt will be submitted to AlphaSense Deep Research."
- For dual-source: both versions included, clearly separated.

## OUTPUT FORMAT
Section structure, bullet point guidance, rating scales, tables.
```

### How the Parent RESEARCHER Uses Templates

1. Read the relevant template file
2. Fill in placeholders: {TICKER}, {COMPANY}, {INDUSTRY}, {PEERS}, any Richard-specific angles
3. For [C] queries: dispatch as Sonnet sub-agent with the filled template as the complete prompt
4. For [AS] queries: extract the [AS] prompt section, hand to Haiku AS Submission Agent
5. On agent return: validate output (word count, sections, correct ticker), then hand to posting pipeline

---

## Research Quality Standards

### From Richard's Journals and Corrections

1. **Always have a conclusion.** No analysis without judgement. Strong views, weakly held. [D]
2. **Show full reasoning chain.** Don't skip steps. [D]
3. **Right-to-left thinking.** Start with financial output (predictable 18M-3Y EPS), work backwards. [D]
4. **ACH approach.** Don't solve for "yes." Build profiles of "no," "false friend," and "yes." [D]
5. **Flag confidence level and key assumptions.** When uncertain: best guess + flag. [D]
6. **"Hell Yeah or No" filter.** Don't over-research mediocre ideas. [D]
7. **Goldilocks growth check.** 20-30% sweet spot. 10% = inflection unlikely. 50-70% = too hard to forecast. [D]
8. **False friend detection.** Zero clarity of transmission mechanism = false friend. Flag immediately. [D]

### Research Pitfalls to Avoid

- **Trees not wood:** Lost in detail without strategic view (XVIVO lesson)
- **Solving deteriorations analytically:** If deteriorating, the answer is exit review, not more research
- **Lazy extrapolation of cyclical highs:** Assume 100% cyclical/temporary unless proven structural
- **Vague financial analysis:** Must be financial-centric, not narrative-driven
- **Narrow frame distraction:** Maintain the forest view

---

## What Richard Values in Research

- **Predictability obsession:** Can Watson track and forecast the EPS trajectory?
- **Evidence of quality dimensions:** Demonstrated pricing power, customer loyalty, execution
- **Revenue optionality mapping:** M&A, geographic, product, pricing optionality
- **Operator quality assessment:** "Animal CEO" (Slootman archetype)
- **Supply chain physics:** Physically tight supply chains (Diploma-type)
- **Thematic agnosticism:** Watch all industries. No dogmatisms
- **Management meeting prep:** Financial-centric. Walk the P&L. Model ready

---

## Preparation Routine

Before any research session, Watson reads:
1. CLAUDE.md pipeline table (current priorities)
2. This file (RESEARCHER SKILL.md)
3. AS/Claude Research SOP (execution mechanics — including Haiku submission protocol)
4. Notion Posting SOP (posting mechanics)
5. **Diligence Checks SKILL.md** (verification framework — mandatory) [D]
6. memory/context/investment-strategy.md (quality framework, setup profiles)
7. memory/context/richard-investing-approach.md (philosophy, stock lessons)
8. Relevant stock-specific Notion pages (if available)

---

## Monitoring Plan Integration (V2.1, 15-Apr-26)

### Purpose

The RESEARCHER executes ongoing monitoring of Leading Tracking Indicators (TIs) and Key Developments for all stocks on Live, Short List, and Long List watchlists, plus thematic/macro topics. The Monitoring Plan database is the RESEARCHER's operational task list for this work.

### Database Location

- **Monitoring Plan:** `databases/monitoring/monitoring-plan.json`
- **Findings Log:** `databases/monitoring/findings-log.json`
- **Dashboard view:** `databases/ic-ratings-dashboard-live.html` (Monitoring Plan tab)

### RESEARCHER Monitoring Workflow

**Daily startup:** Check Monitoring Plan database for items where `next_check_due` ≤ today. Execute in priority order (Critical → High → Medium → Low).

**For each monitoring item:**
1. Read the item's **How (Summary)** and **How (Detailed)** fields for instructions
2. Read the **Why (Higher Intent)** field to understand the bigger picture — this enables the RESEARCHER to use judgement and initiative, not just follow instructions mechanically
3. Execute the monitoring check using the specified approach (AlphaSense search, web search, data source check, etc.)
4. **Log the finding** to `databases/monitoring/findings-log.json`:
   ```json
   {
     "finding_id": "FIN-{auto}",
     "monitoring_item_id": "{MON-XXX}",
     "date": "{YYYY-MM-DD}",
     "finding": "{What was observed}",
     "signal": "Positive / Neutral / Negative / Inconclusive",
     "significance": "Material / Notable / Minor",
     "action_triggered": "{If any — e.g. 'Escalated to APM for rating review'}",
     "source": "{Where the finding came from}"
   }
   ```
5. Update the monitoring item's `last_checked` date and compute `next_check_due` from `frequency`
6. **If finding is Material + Positive or Negative:** Escalate to APM for potential rating update. Post a brief note to Notion Stock Notes.
7. **If finding is Minor/Neutral:** Log only. No escalation.

### Bayesian Updating Principle

When the RESEARCHER produces KD Assessment outputs (#7 at Triaging, #14 at ESA), these should integrate:
- The APM's **prior** (ICD hypothesis from the IC Ratings database — fulcrum drivers, key drivers, transmission chain)
- **New external evidence** from RESEARCHER's own monitoring findings, sell-side commentary, company disclosures, industry data

The RESEARCHER weights both. Sell-side and company guidance can be positively biased or superficial. But being too anchored to the APM's prior creates commitment/endowment bias. The 80/20 rule applies: most of the time the obvious/standard chain of inference is correct. Variant insights are the edge but cannot be forced.

### Default Frequency Rule

**Default to slower cadence than instinct suggests.** Monthly unless there's a specific reason for faster (approaching catalyst, position sizing discussion, earnings window). Can always increase if priority rises. This reduces unnecessary work and ensures findings are actually consumed.

### Cross-Reference SOP

When the RESEARCHER executes any stock-specific research (#1-19), before starting:
1. Check the Monitoring Plan database for any items with this ticker in `related_stocks`
2. Review recent findings in the Findings Log for this stock
3. **Check `memory/thematics/active.md` for this stock's thematic scores (if Mode 1 batch has been run).** If scores exist, read the relevant beneficiary/at-risk attribute tables and incorporate the thematic context into the research framing. If scores don't yet exist, make a mental note of whether the stock appears likely to match beneficiary or at-risk attributes — and flag in the output for APM to score.
4. Incorporate any material findings into the research output

This ensures monitoring intelligence feeds into structured research, not just into the database.

### Thematic Integration — RESEARCHER Rules

**MANDATORY LOAD:** On every session start, RESEARCHER loads (a) `memory/thematics/active.md` (operational state), (b) `memory/skills/thematics/SKILL.md` (master doctrine — added 4-May-26). Per CLAUDE.md UWB-6 (Thematics Front of Mind), thematics are consulted FIRST in any stock-related research framing.

**Rule T0 (NEW 4-May-26): Every stock-level template (IG/Triaging/ESA/DD) must include a "Thematic Alignment" section.**
RESEARCHER does NOT score (per existing SOP — that is APM's job) but must FLAG plausible beneficiary or at-risk alignment with each active thematic, citing 1-2 attributes from the tables in `memory/thematics/active.md`. This flagging informs APM's subsequent Mode 1 / Mode 2 scoring. Skipping the section is a SOP violation.

**Rule T-WL (NEW 4-May-26): Pass 2 of any thematic memo MUST consult Wisdom Library before proposing mental-model lenses.**
When running a three-pass thematic memo (per `memory/skills/thematics/SKILL.md` Stage 2 addendum), RESEARCHER must consult `wisdom-library/situational/thematics/` AND `wisdom-library/general/decision-making/` AND any other relevant categories before composing Pass 2. WL-not-consulted is a SOP violation. Each completed thematic build must add ≥1 transferable concept to `wisdom-library/situational/thematics/`.

**Rule T1: KD Assessment queries (#7 and #14) must include a thematic section.**
The KD Assessment is where RESEARCHER first synthesises drivers. At the end of every #7 (Triaging KD Assessment) and #14 (ESA KD Assessment), RESEARCHER adds a section: **"Thematic Overlay — Preliminary Assessment."** Format:

```
## Thematic Overlay — Preliminary Assessment
Active thematics: T1 (Bear Market), T2 (AI Disruption), T3 (Iran War + Oil)

T1 [Bear Market]: [Preliminary A-F rating] — [2-3 sentence rationale citing specific attributes]
T2 [AI Disruption]: [Preliminary A-F rating] — [2-3 sentence rationale]
T3 [Iran War + Oil]: [Preliminary A-F rating] — [2-3 sentence rationale]

Net thematic stance: [Tailwind / Headwind / Mixed / Neutral] — [1 sentence summary]
→ Feeds APM Mode 2 Inline FCS.
```

This is a RESEARCHER preliminary — the definitive rating is the APM's job. RESEARCHER does the evidence gathering; APM does the A-F scoring. Label as "preliminary" explicitly.

**Rule T2: IG Business Description (#1) — flag thematic relevance.**
At the end of the BD output, RESEARCHER adds a 2-3 sentence "Thematic Relevance" note: does this company operate in a thematically sensitive sector? This is a fast screen — not a full scoring. E.g., "Defence prime with 60% NATO contract revenue → T3 Iran/Oil beneficiary candidate" or "Naphtha-based chemical producer → T3 Iran/Oil at-risk candidate."

**Rule T3: Thematic monitoring items.**
When writing deliverable #20 (Monitoring Plan) for any stock with a D/E/F APM thematic rating, include at least one monitoring item per at-risk thematic. The monitoring item specifies: (a) data point to track (e.g., Brent price, hedge cover, jet fuel spot), (b) frequency, (c) escalation trigger (e.g., "If Brent >$110 for 3+ weeks and no new hedge cover disclosed → escalate to APM").

**Rule T4: Change Forces (#2) — thematic-driven change forces are valid.**
When assessing fundamental change forces at IG stage, macro/thematic forces ARE valid as change force inputs. Iran War driving NATO capex = valid change force for a defence contractor. AI disruption removing addressable market = valid headwind change force for a staffing company. Do NOT treat thematic forces as "external noise" — they are fundamental business case inputs when they are material to the stock's EPS trajectory.

---

## Master Dashboard Integration (24-Apr-26) [D]

The **Master Dashboard** (`COWORK/master-dashboard/`) is the unified screening, monitoring, and capital deployment system for ~1,000 European equities. It supersedes several legacy standalone tools. RESEARCHER must use it as the primary source for all technical screening and quantitative data.

### Data Files — RESEARCHER's Technical Data Sources

| Master Dashboard File | Contents | Replaces |
|---|---|---|
| `master-dashboard/data/prices.json` | Per-stock price, 7 MAs (5D/10D/20D/50D/100D/150D/200D), 52W H/L, ADV, market cap, RS data. Updated daily via `generate_master_data.py --full-universe` | Legacy FactSet `extract_tm_data.py`, `pullback-watchlist.json` for MA lookups |
| `master-dashboard/data/filter-results.json` | Pre-computed pass/fail per stock across 5 filters: Basing Plateau, Probing Bet, VCP, MM99 (11-test), Uptrend Retest. Includes qualification stages (Early/Late/Capital) | `snapshots/minervini-history.json`, `rebuild_minervini.py`, `rs-breadth-dashboard` RS data |
| `master-dashboard/data/factset-ssem.json` | SS estimates revision %, momentum count (from FactSet Excel export) | Direct FactSet lookups for revision data |
| `master-dashboard/data/factset-valuation.json` | P/E current + 10Y sparklines, percentiles (from FactSet Excel export) | Direct FactSet lookups for valuation multiples |
| `master-dashboard/data/universe.json` | Master ticker list (~976 stocks) with sector, industry, company name, yfinance ticker mapping | `pullback-watchlist.json` as the stock universe |

### Deprecated Tools (replaced by Master Dashboard)

| Legacy Tool | Status | Replacement |
|---|---|---|
| `rebuild_minervini.py` | **Deprecated** | MM99 filter in `filter-results.json` (11-test score, 5 groups) |
| `snapshots/minervini-history.json` | **Deprecated** | MM99 filter in `filter-results.json` |
| `rs-breadth-dashboard` | **Deprecated** | RS data in MM99 Group E (excess return: stock − benchmark for sector/industry/market) |
| `pullback-watchlist.json` (as universe) | **Deprecated** | `universe.json` is now the master stock list |

### Pullback Monitor — Temporary Coexistence (will be deprecated into MD)

The **Position Entry Monitor** (`pullback-data.json`) still provides richer signal-level data for Query #3 (Technical Momentum) that the Master Dashboard's UTR tab does not yet compute. Specifically: 10-signal composite scoring (volume signals 3a-3e, VCP intact, recovery speed, fundamental context), base count/history, violation tracking, red flags, and MA proximity alerts. The UTR tab currently has placeholder values for signals 3-7.

**Rule:** Use Master Dashboard for screening data (which filters pass, qualification stage, MA levels, MM99 score, RS). Use pullback monitor for signal-level depth when writing TM memos (10-signal composite, base count, violations, red flags). This coexistence is temporary — once the UTR tab's placeholder signals are fully implemented, the pullback monitor will be deprecated entirely into the Master Dashboard.

### How RESEARCHER Uses Master Dashboard Data

1. **Query #3 (Technical Momentum):** MD `prices.json` for MA levels + `filter-results.json` for MM99 score, filter qualification stages, RS data. Supplemented by `pullback-data.json` for 10-signal depth (temporary). Chart screenshots from `master-dashboard.html` chart panel.
2. **Query #4-5 (Earnings Trends/Delivery):** MD `factset-ssem.json` as **supplementary quantitative context** only. AlphaSense remains the overwhelming primary source for earnings analysis.
3. **8/8 Minervini trigger for automated IG:** Read from MD `filter-results.json` MM99 filter (score field). Replaces `snapshots/minervini-history.json`.
4. **Inverted Screen:** MD `filter-results.json` MM99 filter replaces standalone `rebuild_minervini.py` output.
5. **Adding new stocks:** Add to `master-dashboard/data/universe.json` (not `pullback-watchlist.json`). Then ask Richard to run `python generate_master_data.py --full-universe`.

### Data Freshness

The Master Dashboard pipeline (`generate_master_data.py --full-universe`) runs daily overnight. Data in `prices.json` and `filter-results.json` is accurate to the prior trading day. Check `_meta.generated` timestamp if freshness matters for a specific decision. Do NOT block research if data is 24-48h old — note the age and proceed.

---

## Key Files

| File | Purpose |
|------|---------|
| `templates/01-ig-bd.md` through `templates/22-kq-analysis.md` | Self-contained agent briefs for each query (v2.1 pattern, promoted 06-May-26 per D-RSR-34) |
| as-claude-research-sop-v2.md | Research execution: Claude [C] native (Sonnet); AlphaSense [AS] via Haiku browser agent; extraction by Sonnet |
| notion-posting-sop.md | Highlighting, formatting, posting, verification |
| updating-old-research-memos-SOP.md | **v2.0 (06-May-26).** Formatting-only pass for existing memos → HTML → GitHub Pages. Validator: `databases/scripts/validate-memo.py` |