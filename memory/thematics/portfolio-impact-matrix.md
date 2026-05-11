# Portfolio Impact Matrix — Stock × Thematic A-F Grid

**Owner:** APM (Mode 1 batch output)
**Refresh:** Quarterly + on regime change + on new thematic adoption
**Source of truth:** This file. Mirrored to ratings dashboard.

---

## How to Read This File

Each row = a stock (Live position, Short List, or Long List).
Each column = an active thematic.
Cell = A-F rating per the thematics SKILL.md A-F scale.

A = strong beneficiary (+3); B = beneficiary (+2); C = neutral (0); D = mild headwind (-1); E = at-risk (-2); F = strong headwind (-3).

The composite alignment score for each stock is derived from this matrix and lives in `composite-scores.md`.

---

## Active Period

**Current:** Q2 2026 (April–June 2026)
**Active thematics (per `active.md`):**
- T1 — Bear Market / Top of Bull Market
- T2 — AI Disruption / Opportunities
- T3 — Iran War + Oil Price / Value Chain

**Last full Mode 1 batch:** 16-Apr-26 (per APM Section 0b). NEEDS REFRESH given T2 (AI) v2 evidence (3-May-26) and Q1 European earnings cycle complete.

---

## Live Positions

| Ticker | Name | T1 Bear Market | T2 AI Disruption | T3 Iran/Oil | Composite | Notes |
|---|---|---|---|---|---|---|
| TBC | Awaiting Mode 1 batch refresh post AI thematic v2 | | | | | Mode 1 batch due |

---

## Short List

| Ticker | Name | T1 | T2 | T3 | Composite | Notes |
|---|---|---|---|---|---|---|
| TBC | | | | | | |

---

## Long List (selected — high relevance to active thematics)

| Ticker | Name | T1 | T2 | T3 | Composite | Notes |
|---|---|---|---|---|---|---|
| TBC | | | | | | |

---

## Rating Discipline (reference)

When APM scores a stock × thematic cell:
1. Read the beneficiary attributes table for the thematic in `active.md`. Count attribute matches.
2. Read the at-risk attributes table. Count attribute matches.
3. Net score: 3+ beneficiary matches with clear EPS transmission = A or B. 2 matches = B or C. 1 or none = C. Mirror for at-risk: 3+ = E or F.
4. State the specific transmission mechanism in the Notes column, not just the rating.
5. Note if the thematic interacts with the stock's fulcrum driver — this is the highest-importance linkage.

---

## Refresh Workflow

1. APM runs Mode 1 batch (per APM SKILL §0b Mode 1 process).
2. APM updates this file with full A-F grid.
3. APM regenerates `composite-scores.md` mechanically from this matrix.
4. APM posts to Notion Journal: `[W] Portfolio Thematic Impact Matrix @ DD-Mon-YY`.
5. COS consumes composite scores into workflow planning.
6. Any cell change of ≥2 grades vs prior batch flagged for Richard's attention (e.g., B → D = 3-grade move = REVIEW).

---

## Build History

- **15-Apr-26:** Original portfolio impact matrix produced as part of initial thematics infrastructure. Lived in active-thematics.md.
- **4-May-26:** Promoted to standalone file. Refresh due post AI thematic v2 evidence. APM Mode 1 batch to follow.
