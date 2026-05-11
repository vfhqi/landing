# Thematics + Portfolio Construction — Master Skill

**Created:** 4 May 2026
**Status:** Live
**Owner:** Richard (decisions) | Watson (execution + maintenance)
**Tier:** First-class skill, equal stature with APM and RESEARCHER
**Mandatory loading:** APM, RESEARCHER, COS roles must load this skill on session start

---

## Why This Skill Exists (Higher Intent)

> *"If you get the right thematics correct, then picking the individual stock is very simple. But there is no amount of stock analysis that will help you if the individual company is not well aligned with the thematics that are driving the stock market at the time."* — Richard, 4-May-26

Five years of evidence — the Covid-stay-at-home call (Ocado / Avanza / MIPS, all +100% in months) being canonical — has convinced Richard that **picking the right thematic dominates picking the right stock.** The portfolio construction problem is upstream of the stock-selection problem.

This skill exists to make sure that conviction is **operationalised across every research and analysis act** — not just when Richard explicitly requests thematic work. **Thematics must be FRONT OF MIND for Watson at all times.** When in doubt about whether to consult thematics, the default is: do.

---

## Three-Pillar Doctrine

### Pillar 1 — Thematics dominate stock selection in importance

The value-add is not the individual stock analysis; it is **(a) identifying the major thematic** that will drive markets over the next 12-18 months, then **(b) ensuring picked individual companies do not have major issues that prevent the stock market from bidding their share prices up.** Stock analysis serves thematic alignment, not the other way around.

### Pillar 2 — Active thematics must be loaded automatically by every role on every session

APM, RESEARCHER, COS — and any other role doing stock-related work — must consult `memory/thematics/active.md` at session start. The thematics are not optional context; they are the operational backdrop within which every stock decision is made.

### Pillar 3 — Composite alignment is the prioritisation signal

The COS workflow planning system prioritises stocks-to-work-on by **composite thematic alignment score** (defined below), not by ad-hoc judgement. Stocks well-aligned with active thematics get more research, more monitoring, more portfolio-construction attention. Stocks poorly aligned get less or get stopped out faster.

---

## What Counts as a Thematic

A thematic is a **macro / strategic / structural force** that creates **systematic beneficiary and at-risk profiles** across the European-listed investment universe over a **12-18 month** horizon (with some thematics having longer half-lives).

A thematic must have:
1. **A clear definition** — 2-3 sentences, with the transmission mechanism to corporate earnings stated explicitly.
2. **A clear beneficiary profile** — attribute lists that can be matched against real stocks.
3. **A clear at-risk profile** — attribute lists for vulnerability identification.
4. **A clear regime / catalyst structure** — what makes this thematic ACTIVE NOW vs latent or retired.
5. **A measurable monitoring set** — data points / indicators that confirm or invalidate the thematic.

Things that are NOT thematics:
- Sector rotations driven by short-term earnings cycles (these are sector-strategy work, not thematics).
- Single-stock catalysts (these are research targets, not thematics).
- Long-term secular trends that don't have actionable 12-18 month drivers (these are interesting context, not thematics).
- Trading-style observations about market microstructure (these belong in market-strategy notes).

The bar for declaring a new thematic is high; once declared, the thematic is treated as load-bearing across all roles and all stock decisions.

---

## Lifecycle SOP — Birth → Research → Refine → Monitor → Retire

### Stage 1 — Birth

**Trigger:** Richard identifies a candidate thematic. Watson can propose candidates but Richard decides.

**Required birth artefact:** `memory/thematics/[thematic-name]/birth-justification.md` — short document containing:
1. **Working hypothesis** — what is the thematic, in 2-3 sentences.
2. **Triggering signal** — what specifically prompted Richard to declare this now.
3. **Falsification test** — what evidence would prove the thematic wrong / not-load-bearing.
4. **Expected horizon** — how long Richard expects this thematic to be active (12-18m default).
5. **Initial beneficiary / at-risk hints** — Richard's priors, to be validated/expanded by research.

**Output:** Thematic added to `memory/thematics/active.md` with status `RESEARCH PENDING`.

### Stage 2 — Research

**Owner:** RESEARCHER (per existing thematics-research-sop.md, Query #23).

**Process:** Dual-source [C]+[AS] research producing the 7 deliverables (definition; beneficiary summary; at-risk summary; beneficiary attributes; beneficiary probable setups; at-risk attributes; at-risk probable setups). 1,200-2,200 words structured output.

**Critical addendum (4-May-26):** For thematics expected to be load-bearing for the full 12-18m horizon, also produce:
- **Three-pass thematic memo** following the AI thematic template — Pass 1 (value-chain map), Pass 2 (mental-model lenses, with Wisdom Library consultation mandatory), Pass 3 (pre-mortem inversion). Length 10-15k words. Saved as PROJECTS/RES - [Thematic] Research/.
- **Delta report** if a second-pass research wave is run (e.g. mid-cycle [AS] cross-check after initial [C] memo).
- **Notion Journal post** of the polished memo for Richard's reference.

**Output:** All 7 deliverables populated in `memory/thematics/active.md` under the relevant thematic. Three-pass memo cross-linked. Birth-justification updated with research-completion date.

### Stage 3 — Refine

**Trigger:** Material new evidence (earnings cycle, regime data point, second-pass research). Quarterly default; on-event ad hoc.

**Process:**
1. RESEARCHER runs a focused second-pass query targeting the most contested calls in the existing thematic.
2. RESEARCHER produces a delta report (CONFIRMED / CONTRADICTED / ADDED per call).
3. APM re-runs Mode 1 batch on affected stocks if any thematic call REVERSED.
4. Update `memory/thematics/active.md` with refined attribute tables + setup descriptions.
5. Notion Journal post with `[REFINE]` tag; cross-link to original.

**Refinement is structural, not exceptional.** Thematics are living frameworks; the AI thematic v1→v2 cycle (memo + delta report + tracked-changes v2) is the canonical refinement template.

### Stage 4 — Monitor

**Owner:** RESEARCHER (mechanics) + APM (interpretation).

**Process:** Each thematic has a monitoring set defined at research-completion time:
- **Catalyst calendar** — quarterly earnings, regulatory events, macro data prints, geopolitical inflections.
- **Leading indicators** — data points that signal regime change (oil price, capex commentary, central bank language, etc).
- **Invalidation triggers** — specific evidence that would shift the thematic from active to refine-or-retire.

Monitoring data lives in the existing RESEARCHER Monitoring Plan database, tagged by thematic. APM consumes monitoring updates during weekly review and quarterly Mode 1 batch.

### Stage 5 — Retire

**Trigger:** Thematic no longer load-bearing. Examples: Iran de-escalates and oil price normalises; AI capex retrenches and the thematic shifts from "buildout" to "post-cycle digestion" requiring a new framing; Bear Market regime resolves into a new bull cycle.

**Process:**
1. Richard or APM proposes retirement; Richard decides.
2. Thematic moved from `memory/thematics/active.md` → `memory/thematics/_archive/[thematic-name]/`.
3. Retirement note added explaining what changed and what evidence triggered retirement.
4. APM portfolio impact matrix and composite scores updated to remove the retired thematic from the active rating set.
5. Historical ratings preserved for reference (so we can study which thematics worked and which didn't).

**Retirement is not deletion.** Retired thematics inform future thematic recognition — pattern library matters.

---

## A-F Rating Scale (Universal)

Used by APM for stock × thematic ratings. Consistent with FCS rating scale.

- **A** — Strong beneficiary. Multiple attribute matches, clear EPS transmission. Stock thesis is *fundamentally amplified* by the thematic.
- **B** — Beneficiary. 2-3 attribute matches, plausible EPS uplift. Thematic supports but isn't core to thesis.
- **C** — Neutral / mixed. Some attributes match both sides, or thematic is immaterial to the stock.
- **D** — Mild headwind. 1-2 at-risk attributes, limited EPS drag.
- **E** — At-risk. 3+ at-risk attributes, clear negative EPS transmission.
- **F** — Strong headwind. Core business model directly threatened by the thematic.

Discipline rules:
- Match attributes from the tables in `active.md`, not vibes. Cite specific attributes.
- Transmission mechanism must be stated explicitly (not just the rating).
- Historical parallel where possible.
- Track-record check: has Richard held a similar stock during a similar thematic episode? What happened?

---

## Composite Alignment Score (NEW — 4-May-26)

The **composite alignment score** translates per-thematic A-F ratings into a single number for each stock, used by COS for workflow prioritisation and by APM for portfolio construction.

### Methodology

For each stock:
1. Convert A-F ratings to numeric scores: A=+3, B=+2, C=0, D=-1, E=-2, F=-3.
2. **Equal-weight by default** — sum across all active thematics, divide by number of thematics. (Equal-weighting starting point; can be overridden if Richard declares a thematic "dominant" — see Override below.)
3. Round to nearest integer for dashboard display, retain decimal for sorting.

**Composite score interpretation:**
- **+2.0 to +3.0** — Strong tailwind portfolio. Prioritise for research, sizing, monitoring. Candidate for upsizing if FCS conviction supports.
- **+1.0 to +1.9** — Mild tailwind. Standard workflow priority. Hold or accumulate per FCS.
- **-0.5 to +0.9** — Neutral. No thematic-driven prioritisation either way. Stock thesis must stand on FCS alone.
- **-0.6 to -1.5** — Mild headwind. Deprioritise new research. Tighten invalidation thresholds on existing positions.
- **-1.6 to -3.0** — Strong headwind. Immediate review. New positions require explicit override justification. Existing positions on 30-day shot clock.

### Dominant Thematic Override

When Richard declares a thematic "dominant" (e.g., Covid stay-at-home in April 2020 was singularly dominant), composite weighting shifts to:
- Dominant thematic = 60% weight
- Other active thematics = remainder split equally

A thematic is dominant when Richard judges that misalignment with it will *override* alignment with all other active thematics combined. Dominant declarations are explicit, dated, and recorded in `memory/thematics/active.md`.

### Source of Truth

Composite scores live in `memory/thematics/composite-scores.md` — refreshed by APM after each Mode 1 batch (quarterly + on-event). Composite is also a column on the ratings dashboard.

---

## Portfolio Construction Rules (Thematic Integration)

These rules supersede / extend the existing APM Section 0b portfolio construction rules:

1. **No E/F concentration on same thematic.** Portfolio cannot have >3 stocks rated E or F on the same thematic. Correlated drawdown risk. Hard rule, COS flags if breached.

2. **Composite-score-weighted prioritisation.** COS workflow planning is primarily driven by composite alignment, secondarily by FCS conviction. If a stock has +2.5 composite + B FCS, it ranks above a stock with +1.0 composite + A FCS for new-position research. (Existing positions follow FCS for sizing.)

3. **Dominant thematic override.** When a dominant thematic exists, all portfolio construction is filtered through alignment with that thematic first. Misalignment with the dominant thematic is grounds for exit even of high-FCS positions.

4. **Tightened stops on E/F thematic-rated holdings.** If a held stock receives an E or F rating on any active thematic during a Mode 1 batch, automatically tighten the invalidation threshold by one level (e.g., 15% → 10%).

5. **Composite +2.0 unlocks upsizing eligibility.** Combined with FCS B+, this is sufficient to move sizing from 8% → 10%. Composite alone is not sufficient; FCS conviction must also be present.

6. **Composite -2.0 triggers 30-day shot clock.** Existing position must either be (a) sold, (b) re-rated upward on the next refresh with explicit evidence, or (c) explicitly retained by Richard with documented override reasoning.

7. **New thematic adoption triggers full Mode 1 batch within one week.** No exceptions. Mode 1 batch produces the new column of the portfolio impact matrix and updated composite scores.

8. **Quarterly Mode 1 batch is mandatory.** APM owns the cadence; COS prompts if missed.

---

## Integration Hooks (How Roles Consume Thematics)

### APM Integration

- **Mandatory load on session start:** `memory/thematics/active.md` (operational state) + this SKILL.md (doctrine).
- **A&J SOP:** Thematic alignment is a required section in every A&J memo. Validator gate fails memos missing per-thematic ratings.
- **Mode 1 (batch refresh):** Quarterly + on regime change. Output = Portfolio Impact Matrix + Composite Scores. Posted to Notion Journal.
- **Mode 2 (inline FCS):** Per-stock thematic alignment integrated into FCS deliverables #10 (ICDs), #11 (ACH), #13 (KRs), #15 (KPOs), #18 (Invalidation Thresholds), #20 (Monitoring Plan).
- **Mode 3 (IG screening):** Quick attribute-table check before committing RESEARCHER time. Thematic tailwind = positive signal for IG progression.

### RESEARCHER Integration

- **Mandatory load on session start:** `memory/thematics/active.md` (read attribute tables for context on every stock query).
- **Stock-level templates (IG/Triaging/ESA/DD):** New required section "Thematic Alignment" — RESEARCHER flags which active thematics this stock plausibly aligns with (beneficiary or at-risk) and why. RESEARCHER does NOT score (that is APM's job) but flags for APM scoring.
- **Query #23 (thematic research):** Existing SOP at `memory/skills/researcher/thematics-research-sop.md`. This master skill cross-links and supersedes; researcher SOP is the execution-mechanics document.
- **New / refreshed thematics:** RESEARCHER produces three-pass memo (Pass 1 value-chain, Pass 2 mental models with Wisdom Library consultation MANDATORY, Pass 3 pre-mortem) for any thematic expected to be load-bearing 12+ months. AI thematic build (3-May-26) is the template.
- **Wisdom Library contribution:** RESEARCHER must add ≥1 transferable concept to `wisdom-library/situational/thematics/` per completed thematic build. Examples: pricing-model erosion as cross-sector AI signal; bottleneck migration in tech buildouts.

### COS Integration

- **Mandatory load on session start:** `memory/thematics/active.md` + `memory/thematics/composite-scores.md`.
- **Workflow planning:** Stocks-to-work-on are prioritised by composite alignment score, with FCS conviction as secondary filter. When in doubt, work on stocks with positive composite first.
- **Weekly review:** Composite-score deltas vs prior week are flagged. Stocks moving from positive → negative composite get review attention.
- **Quarterly review:** Confirms Mode 1 batch ran; flags any thematic refresh / retirement candidates; consults Richard on whether composite-score thresholds need tuning.
- **Workflow Planning System** (in-build, mid-May-26): Thematics are the primary input to the prioritisation algorithm.

### Wisdom Library Integration

- **Situational thematics category:** `wisdom-library/situational/thematics/` houses transferable concepts that emerge from thematic builds. Each entry is a Gold / Silver / Bronze tier mental model or pattern that applies across thematics or across non-thematic stock analysis.
- **Pass 2 consultation mandatory:** When running Pass 2 of a three-pass thematic memo, RESEARCHER must consult the situational/thematics WL category PLUS the general/decision-making category PLUS any other relevant categories. WL-not-consulted is a SOP violation.
- **Per-thematic-build contribution mandatory:** Each completed thematic build must add ≥1 entry to WL.

### CLAUDE.md Integration (UWB-6)

- **Universal Winning Behaviour 6 (NEW):** *Thematics Front of Mind.* When in doubt, consult thematics. Default to up-weighting the thematic frame in any decision about what to research, what to analyse, what to prioritise, what to monitor, what to flag for Richard. The five-year evidence base says picking the right thematic dominates picking the right stock; act accordingly.

---

## Anti-Drift Mechanisms

To prevent the thematics frame from being silently dropped over time:

1. **Mandatory loading enforced via session-start checks.** Each role's SKILL has a startup-checklist line: "thematics/active.md loaded? Y/N". If N, halt and load.

2. **SOP-required-section checks.** APM A&J validator (existing) extended with a "thematic-alignment-section-present" rule. RESEARCHER templates have a structural placeholder that fails QC if empty.

3. **Validator gates (later phase).** Once SOP-required sections have run for a quarter and proven their ergonomics, add validator gates that mechanically fail outputs missing thematic content. Build order: soft hooks → SOP-required → validator gates.

4. **Quarterly self-audit.** APM runs a self-audit: of last quarter's stock-related outputs, what fraction explicitly referenced thematics? Target 100%; investigate any below 95%.

5. **Drift report quarterly.** COS produces a 1-page drift report: are composite scores being used in workflow planning? Are tightened-stops on E/F holdings being honoured? Are new thematics being adopted in Mode 1 batch within 1 week? Surface to Richard.

---

## Governance

| Aspect | Owner | Cadence |
|---|---|---|
| New thematic identification | Richard (final), Watson can propose | Ad hoc |
| Thematic research | RESEARCHER | At birth + quarterly + on regime change |
| A-F scoring (Mode 1 batch) | APM | Quarterly + on regime change + on new thematic |
| Composite score refresh | APM (mechanical, after Mode 1) | After every Mode 1 batch |
| Workflow prioritisation by composite | COS | Continuous |
| Lifecycle review (refine vs retire) | APM proposes, Richard decides | Quarterly |
| WL situational/thematics maintenance | RESEARCHER | After every thematic build |
| SOP / skill maintenance (this file) | Watson (Systems Architect mode) | On material learning |
| Anti-drift audit | COS | Quarterly |

---

## Reference Files

| File | Purpose |
|---|---|
| `memory/thematics/active.md` | **Operational state** — current thematics + 7-deliverable tables |
| `memory/thematics/portfolio-impact-matrix.md` | Stock × thematic A-F grid (APM Mode 1 output) |
| `memory/thematics/composite-scores.md` | Stock-level composite alignment scores (used by COS) |
| `memory/thematics/[thematic]/` | Per-thematic working folder (birth justification, research links, monitoring data) |
| `memory/thematics/_archive/` | Retired thematics (preserved for pattern library) |
| `memory/skills/researcher/thematics-research-sop.md` | RESEARCHER execution mechanics for Query #23 |
| `memory/skills/assistant-portfolio-manager/SKILL.md` §0b | APM thematic overlay rules (Modes 1/2/3) |
| `memory/skills/chief-of-staff/SKILL.md` §Workflow Planning | COS prioritisation algorithm |
| `wisdom-library/situational/thematics/` | Transferable concepts from thematic work |
| `PROJECTS/RES - [Thematic] Research/` | Per-thematic working artefacts (memos, delta reports, AS extracts) |

---

## Build History

- **15-Apr-26:** Original thematics infrastructure built — researcher/thematics-research-sop.md, active-thematics.md, APM Section 0b. Three thematics scored: Bear Market, AI Disruption, Iran/Oil.
- **2-3 May 26:** AI thematic deepened via dual-source [C]+[AS] three-pass memo (15.5k words v1 → v2 with delta report). Process learnings codified.
- **4-May-26:** This master skill created. Thematics promoted to first-class skill stature. Composite alignment score methodology added. CLAUDE.md UWB-6 added. Wisdom Library situational/thematics category created. Integration hooks codified across APM, RESEARCHER, COS.
