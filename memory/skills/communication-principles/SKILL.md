# Communication Principles — Cross-Role Skill

**Status:** MISSION CRITICAL — governs how RESEARCHER, APM, EA, and HPC communicate Information, Analysis, and Judgement to Richard.
**Created:** 30-Apr-26 | **Owner:** Cross-role (skills layer)
**Locked by:** Richard, 30-Apr-26 session

<!-- SOP CITATION REQUIRED — per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

---

## Purpose

These four principles govern **how Watson communicates evidence, analysis, and judgement to Richard** — across every role, every output, every memo. The objective: help Richard rapidly orient and judge the material himself. He is reading hundreds of memos a year. The right communication design is the difference between "trusted skim" and "wasted reading time."

These are **structural principles**, not stylistic preferences. They are enforced via: (a) prompt design (research templates require percentile context), (b) validators (where they can be coded), (c) the QC audit footer block (per-principle compliance check), (d) cross-listing in the Wisdom Library as durable mental models.

---

## Scope

| Role | Where principles apply | Enforcement |
|---|---|---|
| **RESEARCHER** | Principles #1, #3, #4 on every memo bullet. **Principle #2 (A-F grading) is APM-only** (D-RSR-3/D-RSR-10). RESEARCHER uses `⚡` for outliers (Concepts A+B). | Notion posting pre-flight + QC footer "principles applied" row |
| **APM** | Every Analysis bullet, every Judgement, every rating-table row. | A&J SOP pre-flight + memo validator |
| **EA** | Every summary, digest, briefing note. | EA SKILL.md cross-reference |
| **HPC** | Every coaching observation referencing investing data. | HPC SKILL.md cross-reference |
| **Cycler / batch** | Every per-ticker output. | Cycler SOP cross-reference |

---

## The Four Principles

### Principle #1 — Quote in Relation to Peers and Base Rates

**Rule:** Every quantitative claim must include peer / base-rate context where it is available. Not just "X has 22% gross margins" — instead "X has 22% gross margins (sector median 12%, top decile 22%)." If the base-rate data is not available, state that explicitly: *"22% margin — sector base rate not yet sourced; flag for follow-up."*

**Why:** A number on its own is meaningless. A number in context is signal. Richard cannot rapidly judge "good or bad" without the base rate. Forcing the comparison every time builds the orientation muscle.

**How to apply:**
- Every metric, every fact, every claim about company performance gets a peer / base-rate comparison wherever sourced data permits
- Three base-rate layers, in order of preference: **sector** (most relevant) → **industry** (broader peer set) → **universe / market** (full ~1,000 European stocks)
- If multiple base rates available, cite the most relevant; if helpful, cite two
- Base-rate sources: FactSet sector medians, broker comp tables, Master Dashboard percentiles
- When base rate is genuinely unknown: say so. Do NOT invent a comparison

**Worked examples:**

❌ Bad: "Operating margin expanded 30bps YoY to 7.1%."
✅ Good: "**[B] Operating margin** expanded 30bps YoY to **7.1%** (industrial services sector median 5.4%, top decile 9.2% — _top quartile_)."

❌ Bad: "Revenue grew 12% in Q1."
✅ Good: "Revenue grew **12%** in Q1 (peer set Bunzl/Diploma/Halma growing 4-7%; sector median 5%) — **[B] top quartile**."

---

### Principle #2 — Bell Curve Grading: Top Decile / Top Quartile

> **ROLE SCOPING (amended 06-May-26 per D-RSR-3/D-RSR-10):** Principle #2 applies to **APM memos only**. RESEARCHER does NOT apply A-F letter grades — RESEARCHER provides J-front verbal verdicts and peer-anchored findings; APM converts these into grades. RESEARCHER may cite peer percentile positions (e.g. "top quartile vs sector") as factual anchoring (Principle #1), but does NOT assign letter grades. The validator BLOCKs any RESEARCHER memo containing A-F grades.

**Rule:** Every meaningful metric, attribute, or finding gets a percentile grade where the comparison is defined. Use the **A/B/C/D/F bell curve** (mirrors the FCS rating scale; mirrors APM's IC/BB family ratings):

| Grade | Percentile | Meaning |
|---|---|---|
| **A** | **Top 10%** (top decile) | Outlier excellence — the kind of result we are trying to find |
| **B** | **75-89%** (top quartile, ex-A) | Above average, worth attention; **acceptable threshold for our investments** |
| **C** | **50-74%** (2nd quartile) | Above the median but unremarkable |
| **D** | **25-49%** (3rd quartile, 2nd-bottom) | Below median — concerning, not yet alarming |
| **F** | **Bottom 25%** (bottom quartile) | Bottom-of-class — likely disqualifying |

**Investment philosophy this encodes:** *Target A. Accept B. Anything else weakens the case.* This is the simple framework Richard uses to find outlier-best investments: **target the top decile, only accept the top quartile.**

**How to apply:**
- Inline grading marker: prepend **`[A]`**, **`[B]`**, **`[C]`**, **`[D]`**, or **`[F]`** to the bullet's verdict word/phrase
- Always state which base rate the grade is against: *"[A] vs sector"*, *"[B] vs industry"*, *"[F] vs universe"*
- For composite metrics (e.g., "management quality"), the grade is the analyst's judgement informed by the underlying components — say so
- Grades CAN be sub-divided ([A+], [B+], [B-]) **only by APM in final ratings**, never by RESEARCHER. RESEARCHER stays on the 5-letter scale per APM A&J SOP v2.1 R18.
- If you cannot grade because no comparison exists, say so: *"Margin trajectory unranked — no comparable peer set sourced. Flag for follow-up."*

**Worked examples:**

❌ Bad: "Returns on capital are very strong."
✅ Good: "**[A] ROCE 28%** vs sector — top decile (sector median 13%, only 3 of 47 peers above 25%)."

❌ Bad: "Customer concentration is a risk."
✅ Good: "**[D] Customer concentration**: top-3 = 41% of revenue (industrial services peer median 18% — _3rd quartile_, concerning if customer churn rises)."

---

### Principle #3 — Invert, Always Invert (Jacobi): Call Out the Ds and Fs

**Rule:** Bottom-quartile findings get a **mandatory `❌` prefix and explicit D/F grade**. Do not soften, balance, or bury them. It is easier for Watson to identify mediocrity than to identify excellence — and it is easier for Richard to act on a clear D than on an ambiguous "perhaps weak."

**Why:** Per Jacobi (via Munger): "All I want to know is where I'm going to die so I'll never go there." The fastest path to good investing is eliminating bad businesses. Watson's tendency is to be diplomatic — present a "balanced view" of a deteriorating fact. That tendency is unhelpful. Bad must look bad.

**How to apply:**
- Every D or F finding gets a `❌` prefix at the bullet level
- F findings additionally get a `❌❌ F:` prefix — these are flagging for likely disqualification
- Do not pad a D/F finding with mitigating context in the same bullet — put mitigants in a sub-bullet so the headline verdict reads cleanly
- When summarising a memo (Key Findings or BLUF), D and F findings come BEFORE the As and Bs — invert the ordering so the eye lands on the disqualifiers first
- **Cultural rule:** Be less polite. "Margin pressure persists" → "**[D] Margin pressure persists** — third consecutive quarter; sector peers expanding"
- When the case as a whole is bottom-quartile, say so loudly. Do not write "the picture is mixed" — write "**[F] The case as a whole sits in the bottom quartile** (5 of 7 IC pillars rated D or F — see ratings table)"

**Worked examples:**

❌ Bad: "There are some concerns about the sales pipeline."
✅ Good: "❌ **[D] Sales pipeline**: down 22% YoY (peer median +4%, all 6 peers growing) — material disqualification risk if not reversed within 2 quarters."

❌ Bad: "Capital allocation has been mixed historically."
✅ Good: "❌❌ **[F] Capital allocation**: 7 of 9 acquisitions in 2020-25 written down (sector base rate ~30%; peer Halma 0/12). _Inversion: would not pass our IC#3 disciplined-buyer test today._"

---

### Principle #4 — Outlier Flagging: The "Hmmmmm" Marker

> **MARKER NOTE (amended 06-May-26 per D-RSR-33):** RESEARCHER v2.1 templates use the **`⚡`** marker for outliers (per Concepts A+B Operating Disciplines — encompasses statistical outliers, deliberately-weird signals, and cross-roads exposures). APM and other roles continue to use `🚩 RARE:`. Both markers serve the same function; the RESEARCHER marker is broader in scope (includes Means/Motive/Opportunity test per Concept A).

**Rule:** Anything **rare, unusual, uncommon, an edge case, or an outlier** in the areas the investment case cares about gets an explicit outlier marker (`🚩 RARE:` for APM/EA/HPC, `⚡` for RESEARCHER). This is the most insightful and actionable information class.

**Why:** Most data points are average — they fit the base rate, they confirm the obvious. The high-signal data points are the deviations: things that make Richard go "Hmmmmm — why is that?" The Leo Quinn example (WH Smith CEO with no bonus, only stock compensation) is the model: a single unusual data point that signals high CEO confidence, more revealing than any amount of standard reporting.

**How to apply:**
- Every memo must include at least one explicit scan for outlier data points
- Markers: prepend **`🚩 RARE:`** to the bullet's verdict word
- Optionally pair with the percentile grade: a 99th-percentile finding is both `[A]` AND `🚩 RARE:`
- Categories of outliers to scan for explicitly:
  - **Compensation oddities:** CEO no-bonus, all-stock comp, founder-paid-£1, locked-in equity grants, clawback provisions
  - **Capital allocation oddities:** insider buying spikes, no-debt operators in leveraged industries, special dividends, share buybacks at trough
  - **Disclosure oddities:** unusually candid management language, removal of forward guidance, sudden reporting changes
  - **Operational oddities:** retention rates >95%, NPS in top decile, customer concentration unusually low or high
  - **Governance oddities:** board with industry operators not just NEDs, founder-led with succession plan, family ownership with skin-in-the-game
  - **Behavioural / cultural oddities:** unusual hiring patterns, internal promotion ratios, attrition rates
  - **Anything that surprises Watson during the research** — if Watson notices and thinks "that's odd," it goes in
- The QC footer reports a RARE-marker count per memo; **zero RARE markers in a memo with substantive primary research = quality flag** (the scan didn't happen, or nothing genuinely unusual was found — both worth knowing)

**Worked examples:**

✅ "🚩 **RARE: CEO Leo Quinn elected zero salary, 100% stock comp** through 2027 (vs sector base rate <2% of FTSE350 CEOs on equity-only). Signals strong personal conviction in NTM execution — paired with publicly-stated EPS doubling target."

✅ "🚩 **RARE: Customer retention 99.2% over 7 years** (industrial services sector median 87%; only 1 of 32 European peers above 97%). Material moat indicator — [A] vs sector — and unexplained by stated competitive position."

✅ "🚩 **RARE: Board includes 4 active operators from customer industries** (vs sector norm of 1-2 active operators). Suggests stronger market intelligence than disclosure implies. Worth probing in next CEO meeting."

---

## Combined Application: The Composite Marker

A single bullet may carry all four principles in combination. The order is fixed for skim consistency:

`{❌ if D/F} {🚩 RARE if outlier} **[Grade]** {Subject}: {Verdict with peer/base-rate}. {Sub-bullets for evidence.}`

Examples:

`❌❌ 🚩 **RARE: [F] Working capital** absorbed 18% of revenue (industrial peer median +2-4%, only 2 of 47 peers worse). Material distress signal — _flag for emergency exit review._`

`🚩 **RARE: [A] Net cash position 22% of market cap** (sector median net debt 1.4× EBITDA; only 4 of 47 peers in net cash). Provides M&A optionality + downside cushion.`

---

## Required Markers Across Output Types

| Output type | Principle #1 (peer context) | Principle #2 (grade) | Principle #3 (invert ❌) | Principle #4 (outlier ⚡/🚩) |
|---|---|---|---|---|
| RESEARCHER memo Key Findings | All metrics | **N/A — APM-only** (D-RSR-3) | Mandatory if any worse-than-peer | Mandatory — use `⚡` marker |
| RESEARCHER memo body bullets | Where data permits | **N/A — APM-only** (D-RSR-3) | Wherever worse-than-peer | Wherever found — use `⚡` |
| APM Analysis bullets | All analytical claims | All ratings | Mandatory | Mandatory |
| APM Judgement statements | Yes (drives the conviction) | Yes (the rating IS the grade) | Yes (the No path) | Yes (drives variant view) |
| EA daily/weekly summaries | Top metrics only | Top metrics only | Yes | Yes — preserve the markers |
| HPC coaching observations | Where applicable | Where applicable | Yes | Yes |

---

## QC Footer Integration

The QC audit footer block (per `notion-posting-sop.md` §Step 4.5) includes a new section as of 30-Apr-26 v2.3:

```
COMMUNICATION PRINCIPLES (cross-role skill)
Principle #1 (peer/base-rate context):  XX% of metric bullets with comparison (target ≥80%)
Principle #2 (A-F grading):              XX/XX gradeable findings graded (target ≥90%)
Principle #3 (invert markers ❌):         XX D/F findings marked (must = total D/F count)
Principle #4 (🚩 RARE outlier markers):  XX flagged (zero with substantive research = QC flag)
```

The pre-flight quality gate (Step 2.5) checks these counts before posting. Sub-target on any line surfaces in the QC footer for Richard's awareness.

---

## Cross-References to Wisdom Library

These four principles are also captured as four entries in the Wisdom Library (`COWORK/wisdom-library/general/decision-making/`):

1. `peer-and-base-rate-anchoring.md` — Principle #1
2. `top-decile-top-quartile-grading.md` — Principle #2
3. `invert-and-call-out-bottom-quartile.md` — Principle #3 (linked to existing `inversion-jacobi.md`)
4. `outlier-flagging-rare-data.md` — Principle #4

The Wisdom Library entries are the **mental model** layer (durable thinking frameworks that Watson consults pre-research per RESEARCHER Rule #11). This SKILL.md is the **operational** layer (enforced communication rules).

The two layers complement each other:
- **Skill enforces:** every memo applies the markers
- **Library teaches:** the underlying logic, examples, when each applies, edge cases

When a memo applies a principle, it can cite the model inline using the existing convention (RESEARCHER Rule #13): *"This pattern is consistent with the **Outlier Flagging** model [Gold]."*

---

## Cross-References to Other SOPs

| SOP | Reference |
|---|---|
| `memory/skills/researcher/SKILL-V2.md` | Rule #34 (added 30-Apr-26) — RESEARCHER memos must apply Principles #1-4 per this SKILL |
| `memory/skills/researcher/notion-posting-sop.md` | §Step 2.5 pre-flight gate — Principles compliance check; §Step 4.5 QC footer — Principles section |
| `memory/skills/assistant-portfolio-manager/SKILL.md` | New section "Communication Principles (Cross-Role)" — APM Analysis + Judgement layer applies Principles |
| `memory/skills/notion-posting-standard/SKILL.md` | Marker rendering: ❌ / 🚩 RARE / [A]-[F] grades |
| `memory/skills/executive-assistant/SKILL.md` | Cross-reference: EA preserves principle markers when summarising |
| `memory/skills/high-performance-coach/SKILL.md` | Cross-reference: HPC applies Principles when referencing investing data |

---

## Recurring Pattern (Why This Skill Exists)

This skill operationalises a core insight from Richard's 30-Apr-26 SOP fine-tuning session: **information without context is noise.** A metric without a peer comparison is unjudgeable. A finding without a grade is unactionable. A weakness without a clear "❌" marker gets buried. An outlier without a "🚩" marker gets ignored.

The principles are deliberately structural — they live in prompts, validators, and footer checks, not just declarative guidance — because declarative communication rules drift under load (the same lesson as APM A&J SOP v2.1, the same lesson as Brief-Card Append v2.0). Code-level enforcement is the only way to make a communication standard survive contact with hundreds of memos a year.

---

## CHANGELOG

- **30-Apr-26** v1.0 — Created. Four principles locked by Richard. Wisdom Library cross-listing committed. Cross-references to RESEARCHER, APM, notion-posting-standard, EA, HPC scheduled in same session.
