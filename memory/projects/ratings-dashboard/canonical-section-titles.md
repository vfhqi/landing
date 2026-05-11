# Canonical Section Titles — Universal Naming Rule
<!-- [W] Created 21-Apr-26. Source: spec.md (extracted from "MEMO view MASTER CORRECT" sheet of For Watson - APM Dashboard 4 views - 21_04_2026 0709.xlsx). -->

## Status

**Live Excel file currently locked** (showing as 38KB and unreadable zip — Richard likely has it open). Falling back to spec.md, which was extracted from the same source earlier today (21-Apr-26). When the file becomes readable again, run a verification pass to catch any mismatches.

## The rule

**Use the full Excel column B + C titles, not shorthand, EVERYWHERE.** Applies to: section headers in dashboard, subsection titles in JSON, validator messages, mockup labels, build script comments, all Notion postings, all memo files. The aim is consistent surface language that maps 1:1 to Richard's mental model from the Excel.

## Source-of-truth columns

- **Column B** = the section/subsection ID (e.g. `A`, `A.I.1`, `C.II.2`)
- **Column C** = the canonical full title (e.g. `Table - historicals, guidance, sell side, VF`)

## Section A — Financials section

| ID | Canonical full title |
|----|----------------------|
| A | Financials section |
| A.I | Financials - tabular |
| A.I.1 | Table - historicals, guidance, sell side, VF |
| A.I.2 | TSR dupont (table) |
| A.II | Financials - written analysis |
| A.II.1 | Guidance - Watson analysis/judgement |
| A.II.2 | Financial estimates - SS - Watson analysis/judgement |
| A.II.3 | Financial forecasts - VF modal case - Watson analysis/judgement |
| A.II.4 | TSR dupont - Watson analysis/judgement |

**Note from spec.md:** sheet has typo "A.I.1" at row 12 for Guidance; correct ID is A.II.1.

## Section B — Investment case - executive summary

| ID | Canonical full title |
|----|----------------------|
| B | Investment case - executive summary |
| B.I.1 | Written executive summary of entire MEMO |

## Section C — Investment case "attributes"

| ID | Canonical full title |
|----|----------------------|
| C | Investment case "attributes" |
| C.I.1 | Ratings - all pillars and TCs/As/Qs (tabular + short summary) |
| C.II.1 | TECHNICAL STRENGTH (Pillar 1) |
| C.II.2 | FUNDAMENTAL INVESTMENT CASE (Pillars 3, 4) |
| C.II.3 | FIT FOR MARKET PARADIGM (Pillar 2) |
| C.II.4 | SELL SIDE MOMENTUM (Pillar 5) |
| C.II.5 | UPSIDE (Pillar 6 + TSR Dupont) |

**Per H3 (no UPPERCASE under lowercase):** the Excel uses UPPERCASE here as section labels — but inside the dashboard, render as title case to honour the V5 hierarchy rule (e.g. `Technical Strength (Pillar 1)`). The all-caps form is preserved in the Excel column for reference; the *displayed* form follows V5 typography.

## Section D — Investment case "components" / "mechanics"

| ID | Canonical full title |
|----|----------------------|
| D | Investment case "components" / "mechanics" |
| D.I | Mechanics — KDICs, KHF/As, KCs/KUs, KRs, KPOs |
| D.I.1 | KDICs (PD/SD/TD/LI tree visualisation) |
| D.I.2 | KHF/As (key hygiene factors / assumptions) |
| D.I.3 | KCs/KUs (key confusions / unknowns) |
| D.I.4 | KR (key risks) |
| D.I.5 | KPO (key positive optionality) |
| D.II | Violations — invalidation scenarios, thresholds, expected negatives |
| D.II.1 | 10 standard ACH invalidation scenarios |
| D.II.2 | List of all plausible fundamental invalidation thresholds |
| D.II.3 | List of negative, should-be-expected developments |
| D.III | Open topics — KOQs, KAs |
| D.III.1 | KOQs (key open questions) |
| D.III.2 | KAs (key actions for next stage) |

**Note:** D.I, D.II, D.III branch labels are inferred groupings — Excel may have explicit branch titles in column B/C that I haven't surfaced yet. Verify against live Excel when unlocked.

## Section E — Actions section

| ID | Canonical full title |
|----|----------------------|
| E | Actions section |
| E.I.1 | Pros/cons of prioritising vs other opportunities |
| E.II.1 | Monitoring plan (RESEARCHER) for TIs/ICDs/peers |
| E.II.2 | KQs/KAs if/when progressed to next stage |
| E.III.1 | Reasons for parking ("gaps" analysis) |
| E.III.2 | Re-assessment criteria for re-activation |
| E.III.3 | Monitoring plan for re-assessment criteria |

## Section F — Appendices

| ID | Canonical full title |
|----|----------------------|
| F | Appendices |
| F.I | Basic checks (ADV > $3m, mcap > $1bn, listed > 12mo) |
| F.II | Any appendices / rough notes |

## Display rules

1. **JSON `title` field** = canonical full title from column C (verbatim).
2. **Dashboard rendered header** = canonical title, with V5 typography rules applied (no UPPERCASE under lowercase, sentence case for display where Excel has all-caps).
3. **Collapsed-tab label** = canonical title abbreviated only if it exceeds the badge width — never lossy. If abbreviated, full title shows as tooltip on hover.
4. **Validator messages** = full canonical title in error text so Richard sees the same language as in the Excel and dashboard.
5. **Build script comments** = canonical title in comment headers for grep-ability.

## Length constraint check

Longest titles by section:
- A.II.3: `Financial forecasts - VF modal case - Watson analysis/judgement` (62 chars)
- E.II.1: `Monitoring plan (RESEARCHER) for TIs/ICDs/peers` (47 chars)
- D.II.2: `List of all plausible fundamental invalidation thresholds` (57 chars)
- C.II.5: `Upside (Pillar 6 + TSR Dupont)` (29 chars in display form)

All are below the 80-char practical badge-width cap. **No abbreviations needed for V1.**

## Application checklist

When this map is approved, sweep through:

- [ ] `databases/memos/NVTK/Triaging.json` — all subsection.title fields
- [ ] `databases/memos/NVTK/ESA.json` — all subsection.title fields
- [ ] `databases/memos/NVTK/DD.json` — all subsection.title fields
- [ ] `databases/memos/HTRO/Triaging.json` — all subsection.title fields (where present)
- [ ] `databases/scripts/build-memos.py` — comment headers + any hardcoded titles
- [ ] `databases/scripts/validate-memo.py` — error message strings
- [ ] `databases/scripts/generate-memo-md.py` — section header strings
- [ ] `databases/mockups/section-d-cards-v1.html` — use canonical titles from D.I.* / D.II.* / D.III.*
- [ ] Future Section A v3-replication mockup
- [ ] Future Section C.I integration mockup
- [ ] `memory/skills/memo-view-formatting/SKILL.md` — example labels
- [ ] `memory/skills/assistant-portfolio-manager/*.md` — example labels

## Verification when Excel unlocks

When `For Watson - APM Dashboard 4 views - 21_04_2026 0709.xlsx` is readable again (or a newer version exists), run:

```python
import openpyxl
wb = openpyxl.load_workbook('Files/.../latest.xlsx', data_only=True, read_only=True)
ws = wb['MEMO view MASTER CORRECT']
for row in ws.iter_rows(min_col=2, max_col=3, values_only=True):
    if row[0]:
        print(f"{row[0]}\t{row[1]}")
```

Diff output against this file. Any mismatch = Excel wins.
