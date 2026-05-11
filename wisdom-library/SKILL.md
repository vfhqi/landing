# Wisdom Library — Master SOP

**Status:** MISSION CRITICAL — this governs how Watson consults, updates, and maintains the Wisdom Library.
**Created:** 24-Apr-26 (SA - Wisdom Library project)
**Location:** `COWORK/wisdom-library/`
**Project:** `PROJECTS/SA - Wisdom Library/`

---

## 1. What the Wisdom Library Is

> **OPEN ISSUES (lily pad):** See `memory/apm/open-issues-stage-progression.md` — master index of 8 open issues from STAGE PROGRESSION SOP rollout (1-May-26). When an issue surfaces in real work, process it then. Do not pre-emptively action.

**Pre-write JSON validation (lesson 1-May-26):** Before writing INDEX.json, validate the EXISTING file is parseable (`python3 -c "import json; json.load(open('INDEX.json'))"`). On 1-May-26, INDEX.json was discovered pre-corrupted from a prior session (truncated mid-entry). Pattern: pre-write validate; if invalid, repair before adding new entry. See open issue #6 in `memory/apm/open-issues-stage-progression.md`.


A living, tiered, cross-referenced library of mental models, frameworks, insights and lessons. Three layers:

1. **General mental models** — apply to any decision. Three categories:
   - **Investing** — compounding, sizing-is-superpower, right-to-left thinking, predictability obsession, etc.
   - **Business** — economies of scale, network effects, moats, flywheel-vs-treadmill, etc.
   - **Decision-making / Life** — inversion (Jacobi), IAJA, mission command, Bayesian updating, AND-not-OR, etc.

2. **Situation-specific mental models** — apply to a class of investing situations. Sub-categories:
   - **Portfolio construction** — gross exposure, concentration, sizing frameworks, diversification
   - **Position management** — entry, exit, management (sub-folders)
   - **Industries** — per-industry/sector models (consulting utilisation, cable company dynamics, etc.)
   - **Business models** — serial acquirers, marketplaces, subscription/recurring, etc.
   - **Chain patterns** — combinations of simple patterns (e.g., scale economies shared)
   - **Simple patterns** — observable single patterns (animal CEO, cockroaches never alone, demand pulse reversion, etc.)
   - **Thematics (NEW 4-May-26)** — transferable concepts that emerge from portfolio-construction thematic builds (AI, Bear Market, Iran/Oil, future thematics). Examples: pricing-model erosion as cross-sector AI signal; bottleneck migration in tech buildouts; thematic dispersion within sub-themes; bear-case-lives-in-qualitative-not-quantified-models. **Pass 2 of any three-pass thematic memo MUST consult this category** (per RESEARCHER SKILL Rule T-WL). Each completed thematic build MUST add ≥1 entry here.

3. **Situation-specific information** — NOT in the library. This is what RESEARCHER produces per stock. The library provides the orientation that makes that information useful.

Categories can split recursively as the library grows. Target: 5-9 items per sub-category before splitting.

---

## 2. File Format (Every Model)

```markdown
---
name: {Model Name}
tier: gold | silver | bronze
category: general/investing | general/business | general/decision-making | situational/{sub-category}
keywords: [keyword1, keyword2, keyword3]
cross_references: [other-model-slug, ...]
authors: [Munger, Richard, ...]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
updated_by: APM | RESEARCHER | Richard | HPC
---

# {Model Name}

## Definition
{1-3 sentences. What is this model?}

## Why It Matters
{1-2 sentences. Why does this model improve analysis/judgement?}

## Application
{When you see X, think about Y. Concrete guidance for RESEARCHER/APM.}

## Examples from Track Record
{Stock-specific evidence. Format: "TICKER (Mon-YY): description". Tagged with date.}

## Cross-References
{Links to related models, coaching files, stock-specific notes.}

## Change Log
{Tier changes, additions. Format: "DD-Mon-YY | ROLE | description"}
```

### Depth Targets

| Depth | When | Size |
|-------|------|------|
| **Light** | Initial creation | Definition + Why It Matters + 1 example + cross-refs. ~20-30 lines. |
| **Medium** | After 2+ encounters | Add Application + 2-3 examples + counter-examples. ~40-60 lines. |
| **Rich** | Gold tier or heavily used | Add boundary conditions, pitfalls, external sources, 5+ examples. ~80-120 lines. |

**Writing-to instruction for RESEARCHER/APM:** When updating a model file, check current depth. If Light and you have material to add, upgrade toward Medium. If Medium and model is Gold tier, upgrade toward Rich. Always add new examples in the "Examples from Track Record" section with stock ticker and date. Never reduce depth.

---

## 3. Tier Definitions

| Tier | Definition | Promotion Criteria | Demotion / Archival |
|------|-----------|-------------------|---------------------|
| **Gold** | Battle-tested. High believability. Multiple confirmations OR externally validated by trusted author AND personally confirmed. | 4+ stock/situation confirmations OR 3+ confirmations + external validation (Munger, Douglas, Marks, etc.) | Counter-evidence from 2+ situations where model led to wrong conclusion |
| **Silver** | Confirmed. Observed in 2-3 stocks or situations with consistent outcome. | 2-3 stock/situation confirmations | Single significant counter-example that undermines the model |
| **Bronze** | Newly observed or hypothesised. Plausible but unproven or lightly proven in Richard's context. | N/A — entry tier | Not observed after 6+ months of active use → archive candidate |

**Promotion/demotion protocol:**
1. APM (or any role) identifies tier change evidence during normal work
2. Update the model file's `tier` field in frontmatter
3. Add entry to Change Log section of the model file
4. Log in `_meta/promotion-log.md`: date, model slug, old tier → new tier, author, one-line reason
5. Update INDEX.json tier field

---

## 4. INDEX System

### INDEX.md
Flat, human-readable taxonomy. Every model listed with: name, tier badge, category path, 1-line description. Keyword-searchable via Ctrl+F or grep.

### INDEX.json
Machine-readable for programmatic lookup. Structure per entry:
```json
{
  "slug": "cockroaches-never-alone",
  "name": "Cockroaches Never Alone",
  "tier": "gold",
  "category": "situational/simple-patterns",
  "keywords": ["deterioration", "exit", "red-flag", "management", "IR", "cockroach", "worser-odder-longer-further"],
  "path": "situational/simple-patterns/cockroaches-never-alone.md",
  "cross_references": ["worser-odder-longer-further", "30-day-shot-clock", "tip-of-iceberg"],
  "depth": "light"
}
```

**Keyword design:** Keywords include industry names, setup types, process stages, risk types, author names, and concept tags. Aim for 5-10 keywords per model. Broad enough to match, specific enough to filter.

**INDEX maintenance rule:** Every time a model file is created, edited, or deleted, the INDEX.json and INDEX.md MUST be updated in the same operation. Stale indexes are the #1 failure mode.

---

## 5. Role Integration

### 5.1 RESEARCHER — Consult Before + Update After

**Before research (mandatory, automatic):**
1. Read `wisdom-library/INDEX.json`
2. Filter by keywords matching: stock's industry/sector, setup type, process stage, known characteristics
3. Load top 5-10 matching model files (cap at 10 to protect context window)
4. Use models to frame/direct research — as orientation, not constraint
5. Do NOT inform Richard of which models are being applied. Just apply.
6. If genuinely confused about whether a model is relevant, ask Richard. Bias toward including.

**After research (mandatory, automatic):**
1. Scan research output for novel patterns, lessons, or framework insights
2. If genuinely new insight: create new Bronze model file + update INDEX
3. If existing model confirmed: update that model's Examples section + Change Log. Tag: `updated_by: RESEARCHER | DD-Mon-YY | from {TICKER} {STAGE} research`
4. If existing model contradicted: note counter-evidence in the model file. If 2+ contradictions, flag for tier review.
5. Do NOT propose updates to Richard. Just do them.

**In Notion postings:**
- Inline model references where relevant: "This pattern is consistent with the **Cockroaches Never Alone** model [Gold] — first red flag on IR quality suggests more problems underneath."
- Summary section at end: `**Mental Models Applied:** Cockroaches Never Alone (Gold), Demand Pulse Reversion (Silver), ...`

### 5.2 APM — Consult Before + Update After

Same as RESEARCHER, plus:
- APM loads broader set: include psychology/performance models and position management models
- APM is responsible for tier promotion/demotion decisions
- APM quarterly review: scan library for Bronze models >6 months old, propose archival. Scan Gold/Silver for counter-evidence. Report to Richard.

### 5.3 HPC — Anti-Pattern Monitor

HPC watches for library health issues:
- Models not being consulted (Watson skipping the consult-before step)
- Everything staying Bronze (no promotion discipline)
- Library growing without pruning (>200 models without archival review)
- Richard not applying models he's stated he believes in (coaching moment)
Flag at weekly review.

### 5.4 CoS — Monthly Health Check

Watson audits monthly:
- How many models consulted in last month?
- How many models updated?
- Any Bronze models >6 months old without confirmation?
- Any categories with >9 entries that should split?
- INDEX.json vs actual files — any drift?
Report to Richard in monthly summary.

### 5.5 Cohort-Driven Tier Promotion (NEW 04-May-26 — cross-role with cohort SKILL §5)

The cohort layer (`memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0) introduces a new tier-promotion pathway: **N-stock confirmation in a single cohort.**

**The mechanism:** Phase 4.6 cohort hot wash (AJ SOP v2.4.1 §Phase 4.6) explicitly tests every existing Bronze and Silver model against the cohort's evidence. When a sub-cohort of 3-5 stocks confirms a Bronze model, propose tier promotion at the cohort hot wash rather than waiting for confirmations to accumulate one stock at a time.

**Promotion rules (additions to §3 Tier Definitions):**

| Trigger | Tier change | Notes |
|---------|-------------|-------|
| Bronze model confirmed in 2-3 cohort stocks | Bronze → Silver | Cohort confirmation is structurally stronger than 2-3 isolated confirmations because the stocks are paired in adjacent context (cross-stock comparison surfaces the signal more cleanly). One cohort run can produce one Silver promotion. |
| Bronze model confirmed in 4-5 cohort stocks AND existing single-stock confirmations elsewhere | Bronze → Silver (or Silver → Gold if total ≥4 confirmations) | Cohort + isolated confirmations stack additively. |
| Silver model contradicted in ≥2 cohort stocks | Silver → Bronze (demote) | Cohort contradiction stronger than isolated contradiction for the same reason as above. Single cohort can demote. |
| New cross-stock pattern emerges in cohort that no single stock could surface | NEW Bronze entry, immediately | The 03-May-26 EKTA/HTRO contrast → `single-leg-case-downgrade` (Silver) is the canonical example. Cross-stock-only patterns are eligible for direct Silver tier when the cohort N≥3 + the pattern is well-formulated. |

**Mechanism in the cohort hot wash:**

1. APM authoring the cohort hot wash at Phase 4.6 surveys EVERY model that was loaded into the cohort precommit list (per cohort SKILL §3.1 manifest format).
2. For each model: tag the cohort stocks where the model APPLIED (positive confirmation), the stocks where it FAILED to apply (counter-evidence), and the stocks where it was IRRELEVANT (no signal either way).
3. Apply the promotion rules above. Document tier changes proposed in the hot wash's Wisdom Library Promotion Candidates section.
4. Promote (update model frontmatter `tier`, update INDEX.json `tier`, log to `_meta/promotion-log.md`) at hot wash authoring — do NOT defer to next quarterly review (per cohort SKILL §6 token efficiency principle, the cohort context is freshest at hot wash).

**Cross-stock-only models — file location convention:**

- Patterns that REQUIRE multi-stock observation to define (`single-leg-case-downgrade`, `bundle-moats-medtech`, `cable-capacity-overhang-timing` etc.) live in their natural category (`situational/portfolio-construction/`, `situational/industries/`, `situational/business-models/`) but include in their frontmatter `cohort_origin: {cohort-name}` to mark provenance.
- The cohort hot wash that birthed them is referenced in Examples from Track Record.

**Cross-ref:** `memory/skills/cohort-research-analysis-judgement/SKILL.md` v1.0 §5 (cohort hot wash SOP); `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.4 §Phase 4.6 (the hot wash where this promotion mechanism fires); 03-May-26 EKTA/HTRO/PRY/COTN-CH session that empirically validated the mechanism (5 cross-stock entries filed at appropriate tiers).

---

## 6. Anti-Patterns to Prevent

| # | Anti-Pattern | Prevention | Role(s) |
|---|-------------|-----------|---------|
| 1 | Library becomes a graveyard | Mandatory consult-before in RESEARCHER/APM loading protocol | RESEARCHER, APM |
| 2 | Consult-before becomes bottleneck | INDEX.json keyword filtering, max 10 files per consult | RESEARCHER, APM |
| 3 | Everything stays Bronze | APM quarterly tier review, Watson proposes promotions with evidence | APM |
| 4 | Models too abstract to apply | Every model has concrete track record examples, Application section | RESEARCHER, APM (when writing) |
| 5 | Duplication with existing files | Clear scope boundaries, cross-references not copies, redirects at old paths | SA |
| 6 | Library grows without pruning | Monthly health check, 6-month Bronze archival rule | CoS, HPC |

---

## 7. Migration Notes

Content migrated from these sources (24-Apr-26):
- `memory/context/mental-models.md` → general/ (redirect left at original path)
- `memory/coaching/stock-archetypes.md` → situational/simple-patterns + situational/position-management (redirect left at original path)
- Roam metacognition checklist → general/business (consolidated from 100+ to ~40 entries by grouping)
- Roam/Journal extractions → various categories
- External authors (Munger, Bevelin, Parrish, Taleb, Kahneman, Soros, Mauboussin, Marks, Dalio, Duke, Douglas, Bassham, Gallwey, Peters, Ward, King, Minervini, Van Tharp, Annie Duke) → general/

Original coaching files (`coaching/risk-management-lessons.md`, `coaching/track-record-by-stock.md`, `coaching/stock-trigger-cards.md`) REMAIN as coaching references. Cross-referenced from library, not absorbed.

---

## 8. Quarterly Review Protocol

Every quarter (first week of Jan/Apr/Jul/Oct), APM runs:

1. **Tier review:** Scan all models. Any with 4+ confirmations still at Silver? Promote. Any Gold with 2+ counter-examples? Demote. Any Bronze >6 month