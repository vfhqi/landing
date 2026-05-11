# MEMO View Build — durable project state

**Started:** 20-Apr-26
**Status:** D.I approved (20-Apr-26 evening). Section C next.

---

## Memo taxonomy (authoritative — from `databases/memo-schema.md` + Excel MEMO view)

Source of truth: `C:\Users\richb\Documents\COWORK\Files\NOT BACKED UP\RB downloads\RB excel tools\For Watson - APM Dashboard 4 views - 20_04_2026 - 1152h.xlsx` → sheet **MEMO view**.

Sections A-F. Word-count convention: 1 page ≈ 300 words.

### A — FINANCIALS
- A.I — Financials tables
  - A.I.1 Table: historicals / guidance / sell-side / VF — populated table (T/ESA/DD)
  - A.I.2 TSR DuPont — populated table
- A.II — Financials written analysis & judgement
  - A.II.1 Guidance — 1p / 2p / 3p
  - A.II.2 Financial estimates — SS — 1p / 2p / 3p
  - A.II.3 Financial forecasts — VF modal case — 1p / 2p / 3p
  - A.II.4 TSR DuPont — 1p / 2p / 3p

### B — EXECUTIVE SUMMARY
- B.I.1 Written executive summary of entire MEMO — 2p / 3p / 4p

### C — ATTRIBUTES (investment case attributes)
- C.I — Ratings (graphical form)
  - C.I.1 Ratings for all pillars + TCs + As + Qs [tabular] + short summary judgement — Filled in (T/ESA/DD)
- C.II — Investment case write-up
  - **C.II.1 TECHNICAL STRENGTH (Pillar 1)** — 5p / 10p / 15p
  - **C.II.2 FUNDAMENTAL INVESTMENT CASE (Pillars 3 + 4)** — 5p / 10p / 15p
  - **C.II.3 FIT FOR MARKET PARADIGM (Pillar 2)** — 2p / 3p / 4p
  - **C.II.4 SELL SIDE MOMENTUM (Pillar 5)** — 1p / 2p / 2p
  - **C.II.5 UPSIDE (Pillar 6 Valuation + cross-ref A.II.3 TSR DuPont)** — 1p / 1p / 1p

### D — COMPONENTS / MECHANICS
- D.I Mechanics / building blocks
  - D.I.1 KDICs (PDs, SDs, TDs, LIs) — 1p / 2p / 3p
  - D.I.2 KHF/As Key hygiene factors — n.a. / 0.5p / 1p
  - D.I.3 KCs/KUs Key confusions / unknowns — 1p / 2p / 0.5p
  - D.I.4 KRs Key concerns/risks — 1p / 2p / 2p
  - D.I.5 KPOs Key positive optionality — 0.5p / 0.5p / 0.5p
- D.II Fundamental violation thresholds
  - D.II.1 10 general/standard ACH invalidation scenarios — n.a. / 1p / 1-2p
  - D.II.2 Plausible invalidation thresholds list — 0.5p / 2p / 3p
  - D.II.3 Expected negative developments — 0.5p / 1p / 1p
- D.III Open topics / questions
  - D.III.1 KOQs Key open questions — 1p / 2p / 1p
  - D.III.2 KAs Key actions — 1p / 1p / 1p

### E — ACTIONS
- E.I Summary judgement (if case sufficiently meritorious)
  - E.I.1 Analysis re. prioritising vs other opportunities — 0.5p / 0.5p / 0.5p
- E.II If compelling case
  - E.II.1 Monitoring plan for TIs/ICDs/peers — n.a. / 1p / 1-2p
  - E.II.2 KQs/KAs if progressed next stage — 0.5p / 0.5p / 0.5p
- E.III If uncompelling / middling
  - E.III.1 Gaps analysis + parking reasons — 0.5p / 0.5p / 0.5p
  - E.III.2 Re-assessment criteria — 0.5p / 0.5p / 0.5p
  - E.III.3 Monitoring plan for re-assessment criteria — 0.5p / 0.5p / 0.5p

### F — APPENDICES
- F.I Basic checks (ADV>$3m, mcap>$1bn, listed>12mo) — 0.5p / 0.5p / 0.5p
- F.II Optional appendices / rough notes

---

## Pillar → C.II map (confirmed 20-Apr-26)

| Pillar | Name | C-section |
|--------|------|-----------|
| P1 | Technical Strength | C.II.1 |
| P2 | Fit for Market Paradigm | C.II.3 |
| P3 | Fundamental Investment Case (part) | C.II.2 |
| P4 | Fundamental Investment Case (part) | C.II.2 |
| P5 | Sell Side Earnings Momentum | C.II.4 |
| P6 | Valuation (+ cross-ref A.II.3 TSR DuPont) | C.II.5 |

C.II.2 covers **two pillars** (P3 + P4) — hence the same budget (5/10/15p) as C.II.1.

---

## Style principles (established in D.I trial, to carry forward)

- Tight-bullet skeleton: BLUF (italic, "BLUF:" label) → top-level ≤15-25w semi-bold (font-weight 600) → 1-3 sub-bullets ≤10-20w each at weight 400 → summary (italic, "SUMMARY:" label).
- IAJA tags: [J] purple #7955bf, [A] blue #3b73c9, [I] black #000000, [ACT] green, [OQ] amber. Tag font-weight 400 across all classes.
- Tree block (D.I.1) = 4-tier KDICs (PDs/SDs/TDs/LIs) with prose AFTER the tree.
- (i)/(ii)/(iii) lowercase-Roman parenthetic enumerators for compound sentences.
- J→A→I order within IAJA content.
- Word-count badges "Xw / Xt": green on-target, red over, grey under. Every topic has one.
- Light off-white palette: #f7f5ef bg, #efebdc raised, #1a1a1a text.

---

## Progress log

- **20-Apr-26 evening:** D.I approved. Next = Section C.
- **20-Apr-26 evening:** Excel MEMO view re-loaded; C.II pillar map confirmed by Richard; persisting to durable memory before any build.
- **20-Apr-26 evening:** Pillars/AFs/TCs/Attributes/Questions extracted from dashboard MAP_STRUCTURE JS object + Excel LIST view. Taxonomy persisted to `memo-section-c-taxonomy.md`. Richard confirmed: all 11 AFs as sub-sub-topics; C.I.1 default = EXPANDED with RATINGS ONLY / SUMMARIES toggle; Minervini 4 pairs of 2; C.II.4 split into 5 + summary.
- **20-Apr-26 evening:** Section C JSON written for NVTK Triaging (17 ratings rows + 5 C.II.x topics with sub-topics and sub-sub-topics). Renderer extended (V2 ratings table with toggle, topic block, sub-topic, bullet tree, inline markup). CSS added for V2 elements. Built + deployed.
- **Live URL for review:** https://vfhqi.github.io/dashboards/ → NVTK → MEMO → Section C.
- **Next:** Richard review of Section C. Likely calibration on bullet density, level indentation, and sub-sub-topic depth at Triaging. Then prose fleshout from (a)-placeholder to real content.

---

## Open decisions awaiting Richard

- C.II sub-topic taxonomy (to be proposed once dashboard hierarchy extracted).
- C.II at Triaging: default per-topic inherits budgets above — confirm no deviations.
- C.I.1 toggle copy: "RATINGS ONLY" / "SUMMARIES" confirmed.
