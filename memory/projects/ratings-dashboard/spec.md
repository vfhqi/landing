# Ratings Dashboard — MEMO Spec
<!-- [W] Created 21-Apr-26 from MEMO view MASTER CORRECT (21_04_2026 0709 file). -->

## Source of truth

**File:** `Files/NOT BACKED UP/RB downloads/RB excel tools/For Watson - APM Dashboard 4 views - 21_04_2026 0709.xlsx`
**Sheet:** `MEMO view MASTER CORRECT`

If a newer file exists with the same naming pattern, prefer the newer one. Always re-read the sheet at the start of any spec-impacting work.

## Section architecture (canonical)

The MEMO has **six top-level sections: A, B, C, D, E, F.** Earlier dashboard work used A/B/C/D only — that was incomplete. Stage toggle build must accommodate the full A-F structure.

## Page-to-word convention

The sheet expresses budgets in **pages**. We use **300 words per page** as the working convention until Richard says otherwise. Visual fidelity to page count is what matters at sign-off.

## Budgets per stage (pages → words at 300w/page)

### A. Financials section

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| A.I.1 | Table - historicals, guidance, sell side, VF | Populated table | Populated table | Populated table |
| A.I.2 | TSR dupont (table) | Populated table | Populated table | Populated table |
| A.II.1 | Guidance - Watson analysis/judgement | 1p / 300w | 2p / 600w | 3p / 900w |
| A.II.2 | Financial estimates - SS - Watson analysis/judgement | 1p / 300w | 2p / 600w | 3p / 900w |
| A.II.3 | Financial forecasts - VF modal case - Watson analysis/judgement | 1p / 300w | 2p / 600w | 3p / 900w |
| A.II.4 | TSR dupont - Watson analysis/judgement | 1p / 300w | 2p / 600w | 3p / 900w |

**Note:** Sheet has typo "A.I.1" at row 12 for Guidance; correct ID is A.II.1 (under A.II Financials - written analysis).

### B. Investment case - executive summary

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| B.I.1 | Written executive summary of entire MEMO | 2p / 600w | 3p / 900w | 4p / 1200w |

### C. Investment case "attributes"

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| C.I.1 | Ratings - all pillars and TCs/As/Qs (tabular + short summary) | Filled in | Filled in | Filled in |
| C.II.1 | TECHNICAL STRENGTH (Pillar 1) | 2p / 600w | 3p / 900w | 3p / 900w |
| C.II.2 | FUNDAMENTAL INVESTMENT CASE (Pillars 3, 4) | 5p / 1500w | 10p / 3000w | 15p / 4500w |
| C.II.3 | FIT FOR MARKET PARADIGM (Pillar 2) | 2p / 600w | 3p / 900w | 4p / 1200w |
| C.II.4 | SELL SIDE MOMENTUM (Pillar 5) | 1p / 300w | 2p / 600w | 2p / 600w |
| C.II.5 | UPSIDE (Pillar 6 + TSR Dupont) | 1p / 300w | 1p / 300w | 1p / 300w |

**C.II totals:** Triaging 11p/3300w · ESA 19p/5700w · DD 25p/7500w

### D. Investment case "components" / "mechanics"

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| D.I.1 | KDICs (PD/SD/TD/LI tree visualisation) | 1p hypoth. / 300w | 2p / 600w | 3p / 900w |
| D.I.2 | KHF/As (key hygiene factors/assumptions) | n.a. | 0.5p / 150w | 1p / 300w |
| D.I.3 | KCs/KUs (key confusions/unknowns) | 1p / 300w | 2p / 600w | 0.5p / 150w |
| D.I.4 | KR (key risks) | 1p / 300w | 2p / 600w | 2p / 600w |
| D.I.5 | KPO (key positive optionality) | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| D.II.1 | 10 standard ACH invalidation scenarios | n.a. | 1p hypoth. / 300w | 1-2p / 450w |
| D.II.2 | List of all plausible fundamental invalidation thresholds | 0.5p / 150w | 2p / 600w | 3p / 900w |
| D.II.3 | List of negative, should-be-expected developments | 0.5p / 150w | 1p / 300w | 1p / 300w |
| D.III.1 | KOQs (key open questions) | 1p / 300w | 2p / 600w | 1p / 300w |
| D.III.2 | KAs (key actions for next stage) | 1p / 300w | 1p / 300w | 1p / 300w |

### E. Actions section

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| E.I.1 | Pros/cons of prioritising vs other opportunities | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| E.II.1 | Monitoring plan (RESEARCHER) for TIs/ICDs/peers | n.a. | 1p hypoth. / 300w | 1-2p / 450w |
| E.II.2 | KQs/KAs if/when progressed to next stage | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| E.III.1 | Reasons for parking ("gaps" analysis) | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| E.III.2 | Re-assessment criteria for re-activation | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| E.III.3 | Monitoring plan for re-assessment criteria | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |

### F. Appendices

| Sub | Description | Triaging | ESA | DD |
|-----|-------------|----------|-----|----|
| F.I | Basic checks (ADV > $3m, mcap > $1bn, listed > 12mo) | 0.5p / 150w | 0.5p / 150w | 0.5p / 150w |
| F.II | Any appendices / rough notes | Supplementary | Supplementary | Supplementary |

## "n.a." cells

Some sub-sections are explicitly **n.a.** at certain stages (e.g. D.I.2 at Triaging, D.II.1 at Triaging, E.II.1 at Triaging). At those stages the section header should still render, with a "n.a. at this stage" placeholder under it — do NOT generate filler content there.

## "Hypothesising" cells

Some cells (D.I.1 Triaging, D.II.1 ESA, E.II.1 ESA) say "X page, hypothesising". This means content is provisional/best-guess at that stage — render with the same word count but with a leading italic note: `*Hypothesising at this stage — to be firmed up in next stage.*`

## Stage totals (corrected — sum of MEMOview cells, with D.II.1 1-2p averaged at 1.5p)

| Stage | Section A | Section B | Section C | Section D | Section E | Section F | TOTAL writing |
|-------|-----------|-----------|-----------|-----------|-----------|-----------|---------------|
| Triaging | 1200w | 600w | 3300w | 1650w | 900w | 150w | ~7800w |
| ESA | 2400w | 900w | 5700w | 4200w | 1050w | 150w | ~14400w |
| DD | 3600w | 1200w | 7500w | 4350w | 1200w | 150w | ~18000w |

(C.II is the bulk; that's where MEMOview discipline matters most. D.II.1 "1-2 pages" averaged at 1.5p / 450w in DD. F.II is rough notes — not counted in totals.)

**Earlier spec.md had a math error in D and E section totals (added 6450/1500 for DD instead of 4350/1200). Corrected 21-Apr-26 09:30.**

## Reconciliation with v3.1 budgets

v3.1 spec used C.II.2 budgets of 2100/4250/7000w. MEMOview spec gives 1500/3000/4500w (at 300w/page).

**Decision:** Use MEMOview as authoritative for the stage toggle build. v3.1 floors and rules (R5/R14, two-shape rule, anchor counts) still apply for FORM. MEMOview governs LENGTH.

If formal validators block on length mismatch, prioritise MEMOview length (Richard's sign-off criterion).
