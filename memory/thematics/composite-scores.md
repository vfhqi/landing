# Composite Alignment Scores — Stock-Level Thematic Aggregate

**Owner:** APM (mechanical regeneration after each Mode 1 batch)
**Consumer:** COS (workflow prioritisation), APM (portfolio construction), Watson (research prioritisation)
**Source of truth:** Derived from `portfolio-impact-matrix.md`. Refresh-after-Mode-1 is automatic.

---

## How to Read This File

Each row = a stock.
Composite score = numeric aggregate of A-F ratings across all active thematics.

**Default weighting:** Equal weight per active thematic. Composite = mean of (A=+3, B=+2, C=0, D=-1, E=-2, F=-3) across all active thematics.

**Dominant thematic override:** When a thematic is declared dominant by Richard, weighting shifts to 60% dominant + 40% split equally across others. Dominant thematic, if any, is named at top of file.

---

## Score Interpretation

| Composite | Label | Workflow Priority | Sizing Implication |
|---|---|---|---|
| **+2.0 to +3.0** | Strong tailwind | Highest priority for new research; flag for upsizing if FCS B+ | Upsizing eligible (8% → 10% if FCS supports) |
| **+1.0 to +1.9** | Mild tailwind | Standard priority; hold or accumulate per FCS | FCS-determined |
| **-0.5 to +0.9** | Neutral | No thematic-driven prioritisation; FCS alone | FCS-determined |
| **-0.6 to -1.5** | Mild headwind | Deprioritise new research; tighten invalidation thresholds on holdings | Tighten stops by 1 level |
| **-1.6 to -3.0** | Strong headwind | Immediate review; new positions need explicit override; existing on 30-day shot clock | 30-day shot clock |

---

## Active Period

**Current:** Q2 2026
**Dominant thematic (if declared):** None currently dominant (all three weighted equally)
**Last refresh:** Pending — APM Mode 1 batch due post AI thematic v2 evidence (3-May-26)

---

## Live Positions

| Ticker | Name | T1 | T2 | T3 | Composite | Label | Action |
|---|---|---|---|---|---|---|---|
| TBC | Awaiting Mode 1 refresh | | | | | | |

---

## Short List + Long List (high-relevance subset)

| Ticker | Name | T1 | T2 | T3 | Composite | Label | Action |
|---|---|---|---|---|---|---|---|
| TBC | | | | | | | |

---

## COS Workflow Implications

**Prioritise research on:** Stocks with composite ≥ +1.0 AND no existing FCS Live position. These are tailwind-positive ideas that haven't yet earned portfolio status.

**Deprioritise:** Stocks with composite ≤ -0.6 AND no existing FCS rating. Don't waste research bandwidth on headwind-negative names absent strong stock-specific catalyst.

**Flag for Richard's review:** Any stock that crossed a threshold (e.g., moved from +1.5 → +0.5 between batches) — the directional change matters as much as the level.

---

## Build History

- **4-May-26:** File created as part of thematics promotion to first-class skill. Composite-score methodology codified in `memory/skills/thematics/SKILL.md`. Awaiting first Mode 1 batch refresh.
