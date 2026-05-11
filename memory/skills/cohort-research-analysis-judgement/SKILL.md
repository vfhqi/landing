# Cohort-centric IAJA Cycle — Master SKILL

**Status:** LOAD-BEARING — wraps the per-stock bookend pattern (AJ SOP v2.4.1 §Phase 0.2 / §Phase 4.5 + RESEARCHER SKILL-V2.13 Rule #37 + session-handoff SKILL §Step 5.5) with a cohort layer.
**Created:** 04-May-26 v1.0
**Updated:** 04-May-26 v1.1 — terminology rename ("wash-up" → "hot wash"; "cohort cycle" → "Cohort-centric IAJA cycle"); status tracker defers to RESEARCH STAGES dashboard tab (single source of truth); §3.3 dashboard integration spec; clarification that Query #8 stays full-size at ESA (6,000-8,000w per D-RSR-7).
**Author:** Watson (SA primary, with APM + RESEARCHER as subject roles)
**Owner roles:** RESEARCHER, APM, SA, session-handoff (cross-role)
**Ancestor lessons:** KZN-003 (Wisdom Library bookend pattern) + KZN-004 (cohort layer).

---

## 1. Purpose

The Wisdom Library bookend (KZN-003, 03-May-26) closed the per-stock loop: every memo opens with a WL consult and closes with a WL hot wash. **This SKILL adds the next layer up — the cohort.** It enforces:

- **Default cohort mode:** RES and APM never operate on a solo stock by default. Default unit of work = a sub-cohort of 3-5 structurally similar stocks. One named exception (SOLO REACTIVE MODE).
- **Cohort open-bookend:** A single shared cohort manifest + shared-context briefing memo authored once, referenced by every per-stock RES + APM run in the cohort. Replaces N× duplicated WL consults with 1× cohort consult + N× delta-only consults.
- **Cohort close-bookend:** A single **cohort hot wash** authored ONCE per stage transition after the LAST per-stock memo at that stage in the sub-cohort ships. Surfaces differential ranking, shared invalidations, WL promotion candidates, and portfolio implications that no per-stock memo can produce.
- **Token efficiency:** Cohort context (industry primer, peer memos, WL precommits, fulcrum-driver class, archetype tags) read once across N stocks instead of N× duplicated.
- **Decision quality:** Forces structural grouping discipline (you can't research a "lonely" stock without explicit declaration), and the cohort hot wash surfaces cross-stock insights at the time they're cheapest to extract.

**The cohort layer is ADDITIVE.** All v2.3 / V2.11 / Step 5.5 quality gates remain. G16 still fires per stock. New G17 gate fires once per sub-cohort per stage transition.

---

## 2. The Trio Rule (with 4 mitigations)

### 2.1 Default

**RES and APM operate by default in COHORT MODE.** Minimum cohort = 3 stocks. Maximum sub-cohort = 5 stocks. If cohort total > 5, split into structural sub-cohorts of 3-5 each. Cohort manifest authored before any per-stock work begins.

### 2.2 Mitigation 1 — Peer-memo-as-leg

A trio can include up to 2 archived peer memos as legs (i.e., new research can be on as few as 1 stock provided 2+ peer memos are loaded as cohort context). Cross-fertilisation works just as well against archived peer memos. The peer-memo legs must be from `databases/memos/{TICKER}/{Stage}.json` or `Files/{TICKER}/{STAGE}/` and tagged in the manifest.

### 2.3 Mitigation 2 — Sub-cohort grouping by structure, not timing

The trio rule applies AT THE SUB-COHORT level, not the batch level. A 12-stock auto-IG batch becomes 3-4 sub-cohorts of 3-5 each. Grouping criterion is **structural similarity** (same setup family / same industry / same fulcrum-driver class / same investment-case archetype), NOT timing. The grouping criterion must be stated explicitly in the manifest.

**Acceptable grouping axes (pick the dominant one for each sub-cohort):**

- **Industry / sub-industry** (e.g., specialty cables, radiation oncology, semicap WFE)
- **IC#3 setup family** (Demand-Driven EPSU, Corporate Change EPSU/EPT, Product Cycle, Earnings Upgrade Cycle, Mis-modelled HQ EPS upgrader, Trough-on-trough cyclical)
- **Business-model archetype** (serial acquirer, asset-light services, R&D-heavy, infrastructure-monopoly)
- **Fulcrum-driver class** (capacity-cycle bottleneck, regulatory tailwind, cost-out execution, cyclical revenue inflection)
- **Stock archetype** (per stock-archetypes.md / WL situational/simple-patterns)

Single-axis groupings preferred. Mixed-axis groupings allowed only if explicitly justified in the manifest.

### 2.4 Mitigation 3 — Sub-cohort cap at 5

Cognitive load and token budget prevent meaningful cohort hot wash beyond 5 stocks. Sub-cohort >5 = split into two cohorts. The cohort hot wash runs PER sub-cohort, not per batch.

### 2.5 Mitigation 4 — SOLO REACTIVE MODE exception

One named exception to the default trio rule:

**SOLO REACTIVE MODE** — single-stock work driven by an event that demands today-action. Triggers:

- Earnings-day post-earnings reaction (≤24h window)
- Post-IR / post-CEO meeting deep-dive (≤48h window)
- Acute M&A / regulatory event with binary near-term outcome
- Live position deterioration tripping a sell trigger (30-day shot clock, cockroach pattern firing, technical Stage 2→3 transition)
- Richard's explicit "single-stock now" instruction

**Discipline when invoked:**
1. Declare SOLO REACTIVE MODE explicitly at session start with one-line reason.
2. Log to `memory/staging/solo-reactive-log.md` (append-only).
3. Watson STILL runs the per-stock bookend (Phase 0.2 + Phase 4.5).
4. Watson STILL surfaces ≥2 closest-archive peer memos as comparative context — even in solo mode, isolation is forbidden.
5. At session close, Watson asks: "should this solo run feed a future cohort?" — if yes, the work product gets tagged for inclusion in the next cohort manifest.

**Audit:** SOLO REACTIVE MODE invocations are reviewed monthly. If ≥30% of sessions are solo-reactive, the cohort discipline is breaking down — escalate to HPC for review.

---

## 3. Cohort Manifest (the authoritative artefact)

**Location:** `memory/staging/cohort-{name}-{YYYY-MM-DD}.md`

**Naming:** `{name}` = short slug describing the dominant grouping axis (e.g., `probing-bet-may26`, `medtech-radiation-oncology-may26`, `cables-overhang-may26`). Date = manifest creation date.

### 3.1 Manifest format

```markdown
# Cohort Manifest — {NAME}

**Created:** {YYYY-MM-DD HH:MM UK}
**Author:** Watson (SA / APM / RESEARCHER — declare primary)
**Cohort scope:** {one-paragraph — what this cohort is, why these stocks, what we expect to learn}
**Grouping axis:** {industry / setup / business-model / fulcrum-driver / archetype}
**Stage assumed:** {IG / Triaging / ESA / DD — dominant stage; per-stock can vary}
**Sub-cohorts:** {count of sub-cohorts inside this manifest}

(Status is NOT recorded in this file — see §3.2 below. Status lives in the RESEARCH STAGES dashboard tab.)

## Sub-Cohort 1: {name}

**Grouping criterion:** {single sentence}
**Stocks (3-5):**
| Ticker | Stage | Source | Type | Notes |
|--------|-------|--------|------|-------|
| {TICKER} | {stage} | {filter-results.json / pipeline / Richard} | new-research | {one-liner} |
| {TICKER} | {stage} | databases/memos/{TICKER}/{Stage}.json | peer-memo-leg | {one-liner} |
| ... | ... | ... | ... | ... |

**Wisdom Library precommits:** {list 5-10 model slugs with one-liner why each is relevant}
- `{slug}` (Tier) — {why relevant}
- ...

**Peer-memo precommits:** {list 1-3 prior memos that should be loaded as cohort context, even if not legs}
- `databases/memos/{TICKER}/{Stage}.json` (DD-Mon-YY) — {one-liner what's portable}

**Expected fulcrum-driver class:** {one sentence}
**Expected primary risk class:** {one sentence}
**Cohort-level CQ precommits:** {3-5 questions every per-stock memo should answer EXPLICITLY because the cohort raises them}
1. {Question 1}
2. {Question 2}
...

## Sub-Cohort 2: {name}

{same structure}

## Cohort-Shared Context Briefing Memo

**Location:** `databases/memos/_cohort/{cohort-name}/shared-context.md`
**Status:** {pending / authored / approved} — also visible on RESEARCH STAGES tab
**Length target:** 1,500-3,000 words. Read once by every per-stock RES + APM run AND visible on the RESEARCH STAGES dashboard tab for Richard's reading. Includes:
- Industry / sector / business-model framing (briefing material — NOT a substitute for per-stock Query #8 BM/Sector Primer at ESA, which stays at full 6,000-8,000 word target (raised from 3,000w per D-RSR-7) unchanged)
- Cohort-level WL model summaries (the precommits, expanded)
- Cohort-level expected priors (what we expect to find on every stock; what would surprise us)
- Cohort-level invalidation candidates (ACHs that could fire across multiple stocks at once)

**This memo serves DUAL purpose:** (a) Watson briefing — RES + APM consume it as cohort context (token-efficiency lever); (b) Richard reading — surfaced on the RESEARCH STAGES dashboard tab so Richard can read the cohort framing alongside per-stock work. **It is in addition to, not in replacement of, per-stock Query #8 BM/Sector Primer (which stays full-size at ESA (6,000-8,000w per D-RSR-7)).**

## Cohort-Level CQ Bank

**Location:** `databases/memos/_cohort/{cohort-name}/cq-bank.md`
Cross-stock comparative questions to be answered DURING per-stock runs, then synthesised at cohort hot wash.

## Audit Trail

| DD-Mon-YY | Event |
|-----------|-------|
| {YYYY-MM-DD} | Manifest created |
| {YYYY-MM-DD} | Sub-cohort 1: {TICKER} per-stock memo shipped (Stage X) |
| ... | ... |
| {YYYY-MM-DD} | Cohort hot wash authored at Stage X |
```

### 3.2 Cohort status tracking — defers to RESEARCH STAGES dashboard tab (NEW v1.1)

**The cohort manifest does NOT carry a status field.** Status is read from the RESEARCH STAGES dashboard tab (the visual source of truth for ALL Watson research and APM work — per-stock and per-cohort). The manifest is the cohort DEFINITION; the dashboard tab is the cohort STATE.

**Rationale:** Single source of truth. Per Richard's instruction (04-May-26): "the RESEARCH STAGES tab of the RATINGS DASHBOARD — to be able to visually see what status of work per query for RESEARCHER and APM" should track ALL state including cohort artefacts. A status field in the manifest would duplicate (and risk diverging from) the dashboard.

**Status values (read from dashboard data feed):**
- `RESEARCH_OPEN` — manifest signed off, RES dispatches in flight, no APM started
- `RESEARCH_COMPLETE` — all per-stock RES queries shipped, APM not started
- `APM_OPEN` — APM has begun on at least one per-stock memo
- `APM_COMPLETE_STAGE_{X}` — all per-stock memos at Stage X have shipped Phase 4.5; cohort hot wash for Stage X owed
- `HOT_WASH_DONE_STAGE_{X}` — cohort hot wash for Stage X authored
- `ARCHIVED` — sub-cohort closed (typically after DD or after all stocks parked)

**Phase 0.0 / Step 5.5.0 / Phase 4.6 read this state from the RESEARCH STAGES data feed** (`databases/research-stages-data.json` or whatever the SA names it — see `databases/research-stages-cohort-spec.md` for the schema spec).

### 3.3 RESEARCH STAGES dashboard integration (NEW v1.1)

**Three entity types appear on the RESEARCH STAGES tab:**

| Entity | Row type | Per-row content | Trigger to populate |
|--------|----------|-----------------|---------------------|
| **Per-stock memo** (existing) | `{ticker × stage × query}` row | RES query OR APM memo: title, status, link to Notion + local file | Per-stock RES query OR APM memo shipped |
| **Cohort manifest** (NEW v1.1) | `{cohort × ALL_STAGES}` row | Cohort name, grouping axis, sub-cohort list, member tickers, status, link to manifest + shared-context briefing memo | Manifest authored at Step 1 |
| **Cohort hot wash** (NEW v1.1) | `{cohort × stage}` row — one row per (sub-cohort × stage transition) | Cohort name, stage, status, link to hot wash artefact + Notion page | Per-cohort-per-stage when last per-stock memo at that stage in the sub-cohort ships |

**For a 5-stock sub-cohort going through Triaging → ESA → DD, the RESEARCH STAGES tab shows:**
- 1 cohort manifest row (lifetime of the cohort)
- 1 cohort-shared-context briefing memo link (within the manifest row)
- ~75-105 per-stock RES query rows (5 stocks × 5-7 queries × 3 stages)
- 15 per-stock APM memo rows (5 stocks × 3 stages)
- 3 cohort hot wash rows (Triaging-cohort-hot-wash, ESA-cohort-hot-wash, DD-cohort-hot-wash) — one per stage transition

**Critical: SOPs document the requirement; the SA implements the dashboard integration in a separate workstream when their current RESEARCH STAGES WIP is complete.** The schema spec for the data feed is at `databases/research-stages-cohort-spec.md` — Watson's RES + APM SOPs reference the spec but do NOT touch the live dashboard code or HTML.

### 3.4 Manifest authoring SOP

**Step 1 — Cohort source.** Identify candidate stocks from one of:
- `master-dashboard/data/filter-results.json` (PROBING BET pass list, MM99 score field, Basing Plateau pass list, VCP pass list, Uptrend Retest)
- `memory/projects/pipeline.md` (active stages — when up to date)
- Richard's direct ticker list
- Auto-IG nightly batch output

**Step 2 — Sub-cohort grouping.** Cluster candidates by structural similarity per Mitigation 2. Document the grouping axis. Aim for 3-5 stocks per sub-cohort.

**Step 3 — Peer-memo leg substitution.** For sub-cohorts <3, identify archived peer memos to add as legs (per Mitigation 1). For sub-cohorts >5, split.

**Step 4 — WL precommit pass.** For each sub-cohort, query `wisdom-library/INDEX.json` by the grouping axis + industry + setup type. Load 5-10 matching models. Document each model + one-liner relevance.

**Step 5 — Peer-memo precommit pass.** Identify 1-3 archived memos (from `databases/memos/` or `Files/{TICKER}/`) that are directly portable. Even non-leg peer memos earn cohort-context status if their conclusions transfer.

**Step 6 — Cohort-shared context briefing memo.** Author the 1,500-3,000 word shared-context memo (industry framing + WL summaries + priors + cohort invalidations). One-time write, N-time read. Briefing material — does NOT replace per-stock Query #8 BM/Sector Primer at ESA (which stays full-size, unchanged).

**Step 7 — Cohort CQ bank.** Generate 3-5 cohort-level CQs that must be answered explicitly in each per-stock memo (informs differential ranking at hot wash).

**Step 8 — Sign-off.** Manifest reviewed by Richard before per-stock work begins (sign-off can be 1-line "GO"). Without sign-off, work is in DRAFT mode; per-stock memos are tagged accordingly. Manifest gets a row on RESEARCH STAGES tab when authored; status updates as work progresses.

---

## 4. The Cohort Open-Bookend (Phase 0.0 — APM, Rule #38 — RES)

### 4.1 RESEARCHER SKILL-V2.13 Rule #38 (cross-ref RES SKILL §Critical Rules)

**Before any per-stock query dispatch:**

1. Check `memory/staging/cohort-*-*.md` for an active manifest matching the ticker. Cross-check status from the RESEARCH STAGES data feed.
2. **If cohort manifest exists** for the active ticker:
   - Read the cohort manifest in full
   - Read the cohort-shared-context briefing memo
   - Cite cohort manifest path + shared-context memo path in the per-stock query template's `cohort_context_path` placeholder
   - Run Rule #37 (WL pre-query consult) in **DELTA-ONLY MODE** — load only WL models NOT already in the cohort precommit list
3. **If no cohort manifest exists** for the active ticker:
   - Either (a) author a manifest now (default) OR (b) declare SOLO REACTIVE MODE with reason logged
   - Run Rule #37 in full mode

The per-stock query template inherits the cohort context. Sub-agents read cohort context FIRST, query template SECOND. Token efficiency: cohort context read once per cohort; per-stock template adds only the stock-specific delta.

### 4.2 APM AJ SOP v2.4.1 §Phase 0.0 (cross-ref AJ SOP §Phase 0)

**Phase 0.0 sits BEFORE Phase 0.1 (RESEARCHER coverage check) and Phase 0.2 (WL consult).**

1. Check `memory/staging/cohort-*-*.md` for an active manifest matching the ticker. Cross-check status from the RESEARCH STAGES data feed.
2. **If cohort manifest exists:**
   - Load the cohort manifest in full
   - Load the cohort-shared-context briefing memo
   - Load any prior per-stock memos in the same sub-cohort (the comparative anchor)
   - Cite cohort manifest path + shared-context memo path + prior-per-stock memo paths in F.I process notes
   - Phase 0.2 runs in **DELTA-ONLY MODE** — load only WL models not in cohort precommit list (cap: 3 delta models max)
   - Inherit the cohort-level CQ precommits — these become MANDATORY content sections in C.II of this stock's memo
3. **If no cohort manifest exists:**
   - Author manifest now OR declare SOLO REACTIVE MODE
   - Phase 0.2 runs in full mode (5-10 models)

**Exit criteria:** explicit confirmation in the working file that (a) cohort manifest is loaded (or SOLO REACTIVE MODE declared), (b) Phase 0.1 RESEARCHER inputs present, (c) Phase 0.2 WL models loaded (full or delta).

---

## 5. The Cohort Close-Bookend (Phase 4.6 — APM, post per-stock Phase 4.5)

### 5.1 Trigger

Phase 4.6 runs **ONCE per sub-cohort PER STAGE TRANSITION**, AFTER the last per-stock memo at that stage in the sub-cohort has shipped (Phase 4.5 complete on every stock at that stage). The APM author of the LAST per-stock memo at that stage is responsible for triggering Phase 4.6, unless Richard reassigns.

**A 5-stock sub-cohort going through Triaging → ESA → DD produces 3 cohort hot washes** — one when the 5th Triaging memo ships, one when the 5th ESA memo ships, one when the 5th DD memo ships (if all 5 progress that far; typically the cohort filters down).

### 5.2 Cohort hot wash structure (4 cohort questions)

**1. Differential ranking — which stocks are differentially attractive WITHIN this cohort?**
   - Apply consistent peer base-rates across the cohort
   - Stack-rank the stocks by case-level attractiveness
   - Identify the structural reason for the ranking (not just rating arithmetic)
   - Flag where the cohort context CHANGED a per-stock judgement vs what it would have been in isolation
   - Format: ranked table + 1-paragraph rationale per pair-wise comparison

**2. Shared invalidations — what ACHs fire across the cohort simultaneously?**
   - Identify D.II.1 invalidation thresholds that would fire on ≥2 stocks at once
   - Format: per-shared-ACH, list affected stocks + the trigger condition
   - These are higher-priority monitoring items than per-stock ACHs (they fire once, kill multiple cases)
   - Feed the Monitoring Plan with cohort-level monitoring items (one item per shared ACH)

**3. WL promotion candidates — what cross-stock pattern emerges?**
   - Run the cohort-aware WL survey: 6 categories matching Step 5.5 / Phase 4.5
     - sectors / industries / business-models / investment-cases / setups / anything-else
   - Specifically test: does the cohort confirm an existing Bronze model (promote to Silver)? Contradict an existing Silver/Gold (demote)? Generate a new pattern that no single stock could surface (file as Bronze)?
   - The 03-May-26 worked example: HTRO/EKTA contrast → `single-leg-case-downgrade` (Silver, cross-stock pattern that needed 2+ stocks to define)

**4. Portfolio construction implications — what does this cohort tell us about position sizing across the live portfolio?**
   - If we own one of these, what does the cohort tell us about owning more (correlation risk)?
   - If we own none, what does the cohort suggest about prioritising entries?
   - If a shared ACH fires, what positions deteriorate simultaneously?
   - Cross-ref: live portfolio in pipeline.md / live positions JSON / position-management WL models

### 5.3 Cohort GNG CHECKS

After the 4 cohort questions are answered, author **Cohort GNG CHECKS** — 6-10 stack-ranked questions probing the cohort-level judgements (NOT the per-stock judgements; those live in per-stock GNG CHECKS files).

**Stack ranking criterion:** which cohort-level question, if Richard answers differently, would most change Watson's per-stock recommendations? #1 = highest impact.

### 5.4 Cohort hot wash artefact

**Notion artefact:** posted to Stock Notes DB with title `[W] Cohort Hot Wash — {Cohort Name} — {Stage} @ {DD-MMM-YY}`. Properties: cohort name, stage, all member tickers in Stock(s) relation, date.

**Local artefact:** `databases/memos/_cohort/{cohort-name}/hot-wash-{stage}.md` — full markdown version with the 4 questions answered + Cohort GNG CHECKS + WL candidates + portfolio implications.

**RESEARCH STAGES dashboard surface (NEW v1.1):** The cohort hot wash gets its own row on the RESEARCH STAGES tab — `{cohort × stage}` — with status, links to the artefacts. This is the visual record Richard reads. SA implements via `databases/research-stages-cohort-spec.md` schema; cohort SOPs require the row to be populated when the hot wash ships.

**Cross-link:** every per-stock memo in the cohort updated to reference the cohort hot wash in F.I process notes (post-hoc edit, allowed).

### 5.5 Quality Gate G17 (NEW v1.1 wording)

A session containing cohort work CANNOT close (cannot run Step 5.5) without:
- Cohort hot wash authored (`databases/memos/_cohort/{cohort-name}/hot-wash-{stage}.md` exists with all 4 questions answered)
- Cohort GNG CHECKS posted (6-10 questions)
- ≥1 WL outcome (entry filed / candidate logged to queue / "no cohort-level candidates" explicit note)
- Per-stock memos updated to cross-link the hot wash
- RESEARCH STAGES tab row populated (when SA's dashboard integration is live; until then, requirement is documented in the SOPs and a placeholder note in the manifest's Audit Trail records the hot wash event)

**Enforcement:** session-handoff SKILL Step 5.5 (Step 5.5.0 below) checks for cohort hot wash presence when cohort manifest exists.

---

## 6. Token efficiency math (the empirical case)

For a 5-stock sub-cohort, the per-stock orientation cost across RES Rule #37 + APM Phase 0.2 is approximately:
- WL consult: 5 models × ~500 tokens = 2,500 tokens per stock
- Industry primer: ~1,500 tokens per stock
- Peer-memo equivalents: ~1,000 tokens per stock
- **Per-stock orientation total: ~5,000 tokens**
- **5-stock cohort total without sharing: ~25,000 tokens**

With cohort manifest + shared-context briefing memo:
- Manifest: ~800 tokens (read once)
- Shared-context briefing memo: ~3,000 tokens (read once)
- Per-stock delta WL consult: ~1,000 tokens × 5 = 5,000 tokens
- **5-stock cohort total with sharing: ~8,800 tokens**

**Savings: ~65% on orientation.** Across a 12-stock auto-IG batch (3 sub-cohorts of 4): proportionally larger.

The savings are realised only IF the per-stock RES + APM dispatches actually inherit cohort context. The `cohort_context_path` placeholder mechanism is the technical lever — every per-stock query template gains this field; sub-agent prompts include the cohort context FIRST.

---

## 7. Three layers of hot wash (NEW v1.1 — explicit summary)

The **Cohort-centric IAJA cycle** has three hot wash ceremonies, firing at three different layers. Together they form the full close-bookend.

| Hot wash | Fires when | Authored by | Output | Frequency | Surface |
|----------|------------|-------------|--------|-----------|---------|
| **Per-stock hot wash** (AJ SOP v2.4.1 §Phase 4.5) | After every per-stock APM memo ships at Triaging / ESA / DD | APM | 3-question hot wash + WL survey, written into the memo's F.I process notes | Every memo. Triaging + ESA + DD = 3 per stock per full funnel | Within per-stock memo (already on RESEARCH STAGES) |
| **Cohort hot wash** (AJ SOP v2.4.1 §Phase 4.6) | After the LAST per-stock memo at a given stage in a sub-cohort ships | APM | Standalone artefact: 4 cohort questions + Cohort GNG CHECKS + WL promotion candidates + portfolio implications | Once per sub-cohort per stage (3 per sub-cohort across full funnel) | Dedicated `{cohort × stage}` row on RESEARCH STAGES (NEW) |
| **Per-session hot wash** (session-handoff SKILL §Step 5.5) | At session close | Session-handoff role | Session hot wash + WL survey + cohort presence check (Step 5.5.0) | Once per session | Within session handoff note |

**For a 5-stock sub-cohort going through Triaging + ESA + DD:**
- 5 × 3 = 15 per-stock hot washes (within memos)
- 3 cohort hot washes (Triaging / ESA / DD stage transitions; each a standalone artefact)
- N per-session hot washes (one per session worked)

**Why three layers, not one:** different scope, different artefact. Per-stock hot wash captures lessons specific to ONE stock at ONE stage. Cohort hot wash captures cross-stock lessons no single memo can surface. Per-session hot wash captures process / SA / Watson-behavioural lessons.

**De-duplication rule:** if a cohort hot wash fired during a session, its outcomes are listed in the per-session hot wash WITHOUT re-surveying. Step 5.5 §2 surveys ONLY content NOT already covered by Phase 4.6.

---

## 8. Integration with live SOPs (cross-reference table)

| Live SOP | Section affected | Amendment |
|----------|------------------|-----------|
| AJ SOP v2.4 → v2.4.1 | §Phase 0.0, §Phase 4.6, §Quality Gates | Phase 4.6 renamed "wash-up" → "hot wash"; status read from RESEARCH STAGES feed; G17 surfacing requirement |
| RES SKILL-V2.12 → V2.12.1 → V2.13 | Rule #38, Query #8 note, v2.1 promotion | Terminology pass (V2.12.1); full template promotion + Concepts A+B (V2.13, 06-May-26) |
| session-handoff SKILL §Step 5.5.0 | Step 5.5.0 + Change log | Terminology pass; status read from feed |
| Wisdom Library SKILL §5.5 | §5.5 | Terminology pass |
| `wisdom-library/_meta/candidate-queue.md` | unchanged | Cohort hot wash outputs feed same queue |
| **NEW** `databases/research-stages-cohort-spec.md` | new file | Schema spec for cohort manifest + cohort hot wash rows on RESEARCH STAGES tab. Owned by SA to implement when their current dashboard WIP is complete. |

All amendments are ADDITIVE. Backwards compatible — when no cohort manifest exists for a stock, all live SOPs operate exactly as before.

---

## 9. Operating discipline (the load-bearing rules)

1. **Default cohort mode.** RES + APM operate on cohorts unless SOLO REACTIVE MODE explicitly declared with reason logged.
2. **Manifest before work.** No per-stock RES dispatch or APM Phase 0.2 starts until cohort manifest is authored and the shared-context briefing memo is in place.
3. **Sub-cohort discipline.** 3-5 stocks per sub-cohort; structural grouping axis explicit; peer-memo legs allowed up to 2.
4. **Cohort context inherited, not duplicated.** Per-stock RES + APM use `cohort_context_path` mechanism; full-mode WL consult only when no cohort manifest.
5. **Cohort hot wash unconditional per stage transition.** Every sub-cohort closes each stage with Phase 4.6 hot wash before session close. G17 gate.
6. **Cohort outputs feed shared queue.** WL candidates from cohort hot wash go to `wisdom-library/_meta/candidate-queue.md` (same file, no fork).
7. **Per-stock bookend unchanged.** Phase 0.2 + Phase 4.5 still fire per stock (in delta mode); G16 still applies. Cohort layer wraps, doesn't replace.
8. **Solo audit.** Monthly review of solo-reactive-log.md. >30% solo = discipline broken; escalate to HPC.
9. **Status from RESEARCH STAGES tab (NEW v1.1).** Cohort state is read from the RESEARCH STAGES dashboard data feed, never from the manifest text. Single source of truth.
10. **Query #8 unchanged (NEW v1.1).** Per-stock Query #8 BM/Sector Primer at ESA stays at full 6,000-8,000 word target (raised from 3,000w per D-RSR-7). Cohort-shared-context briefing memo is in addition to, not in replacement of, Query #8.

---

## 10. Worked example reference

The 03-May-26 EKTA / HTRO / PRY / COTN-CH ESA batch is the textbook worked example. Although authored before this SOP existed, it produced exactly the artefacts a cohort hot wash should produce:

- **Differential ranking:** EKTA flipped to PARK; HTRO PROGRESS-with-cockroach; PRY PROGRESS clean; COTN-CH PROGRESS-gated-on-RES-coverage. Ranking emerged from cross-stock comparison.
- **Shared invalidations:** capacity-overhang ACH (PRY/NKT/NEX/FEVR fibre); bundle-moats ACH candidates (medtech sector cross-cutting).
- **WL promotion candidates:** 5 of the 12 entries filed are inherently cross-stock — `bundle-moats-medtech`, `cable-capacity-overhang-timing`, `single-leg-case-downgrade`, `fulcrum-narrowing-pattern`, `stage-gating-bidirectionality`. Each REQUIRED ≥2 stocks in adjacent context to define.
- **Portfolio implications:** cables sub-cohort raised the question of whether owning PRY + NKT + NEX is owning one bet three times.

The empirical case for this SOP is that it would have produced the same outputs SYSTEMATICALLY rather than as a happy by-product of timing.

---

## 11. Cross-references

- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.4.1 — APM consumer of cohort manifest (Phase 0.0, Phase 4.6, G17)
- `memory/skills/researcher/SKILL-V2.md` V2.13 — RESEARCHER consumer of cohort manifest (Rule #38)
- `memory/skills/session-handoff/SKILL.md` Step 5.5 + Step 5.5.0 — cohort presence check at session close
- `wisdom-library/SKILL.md` §5.5 — cohort-driven tier promotion protocol
- `wisdom-library/_meta/candidate-queue.md` — shared candidate queue (cohort hot wash feeds same queue)
- `projects/SA - Watson Kaizen Lessons/lessons/KZN-003-wisdom-library-bookend-pattern.md` — ancestor lesson
- `projects/SA - Watson Kaizen Lessons/lessons/KZN-004-cohort-layer-on-bookend.md` — this SOP's Kaizen lesson (created same session)
- `master-dashboard/data/filter-results.json` — cohort enumeration source (PROBING BET, MM99, BP, VCP, UTR)
- `memory/projects/pipeline.md` — cohort enumeration source (when current)
- `memory/staging/cohort-{name}-{date}.md` — cohort manifest location convention
- `databases/memos/_cohort/{cohort-name}/` — cohort artefact location convention (shared-context.md, cq-bank.md, hot-wash-{stage}.md)
- `memory/staging/solo-reactive-log.md` — SOLO REACTIVE MODE audit trail
- **`databases/research-stages-cohort-spec.md`** — NEW v1.1 — schema spec for RESEARCH STAGES dashboard tab integration of cohort artefacts. SA-owned implementation.

---

## 12. Change Log

- **04-May-26 v1.0** | SA + APM + RESEARCHER (joint) | v1.0 created. Cohort layer on top of live bookend pattern (KZN-003). Trio rule + 4 mitigations + cohort manifest + open/close cohort bookends + G17 gate. Lock-step amendments to AJ SOP v2.3→v2.4, RES SKILL-V2.11→V2.12, session-handoff SKILL Step 5.5 (sub-step 5.5.0), Wisdom Library SKILL §5.5. Worked example: 03-May-26 EKTA/HTRO/PRY/COTN-CH batch.
- **04-May-26 v1.1** | SA | Terminology rename: "wash-up" → "hot wash" (Richard's instruction); "cohort cycle" → "Cohort-centric IAJA cycle" (Richard's instruction). Status tracker explicitly defers to RESEARCH STAGES dashboard tab as single source of truth (manifest does NOT carry status field). New §3.3 RESEARCH STAGES dashboard integration spec. Clarified cohort-shared-context briefing memo serves DUAL purpose (Watson briefing + Richard reading) and is in addition to per-stock Query #8 (which stays full-size at ESA (6,000-8,000w per D-RSR-7)). New §7 explicit three-layer hot wash summary. New `databases/research-stages-cohort-spec.md` cross-reference. SA does NOT touch RESEARCH STAGES live code in this round (SA is mid-WIP); SOPs document the requirement; SA implements when WIP complete. Backup at `.bak-pre-v11-20260504`.

---

*[W] v1.1 authored 04-May-26 by Watson (SA primary) per Richard's instructions on terminology, dashboard integration, status tracking, and Query #8 preservation. Lock-step with AJ SOP v2.4.1, RES SKILL-V2.13, session-handoff SKILL Step 5.5.0 v1.1, Wisdom Library SKILL §5.5 v1.1. Backups suffix `.bak-pre-v11-20260504`.*
