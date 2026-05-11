# V11 → V20 Morning Arc Summary
<!-- [W] Created 1-May-26 ~07:00 UK. Rollup of the morning's 10-version refinement arc on the Sheet 3 visual style memo specimen. Use this as the canonical project-level summary; state.md has the per-version detail. -->

## Higher intent (the WHY)

Richard had a brief: refine the Sheet 3 visual style specimen (HTRO IC element render of the new memo template) to a state where it can serve as the **canonical APM memo render**. The template defines WHAT goes into a great memo — structurally, weights, signposting, summary blocks, navigation behaviour. The morning's work took the V10 specimen through 10 incremental versions to arrive at V20: a "beta version" of the memo template that's broadly complete subject to minor aesthetic refinements.

**The memo template is now canonical going forward.** It is treated as an APM role artefact (the APM's output spec) — not a SA project deliverable. SA owns the rendering mechanics (build script, CSS, deployment); APM owns the analytical substance.

## Versions shipped (10 in one morning, 1-May-26 ~05:30 → ~06:40 UK)

| Version | Brief items | Doctrine | Live URL |
|---|---|---|---|
| V11 | 9 items: QUADRUPLE tier introduced (Q1 Sector strength); BQ 2-row layout; G5 Optionality 3-col override; element summary cols 2-4; nav CQ unroll fix; rating pill -25%; Conservative IR normal; General ACHs/Crash through stops double | v3.5→v3.6 / SKILL v2.5→v2.6 | `?v=11` |
| V12 | 2 items: General ACHs DOUBLE→QUADRUPLE (Q2); BQ summary narrative reorder | v3.6→v3.7 / SKILL v2.6→v2.7 | `?v=12` |
| V13 | 1 item: Plain sight risks → DOUBLE | v3.7→v3.8 / SKILL v2.7→v2.8 | `?v=13` |
| V14 | 4 nav toggles: Audit + RAs on + CQs on + Element details | renderer only | `?v=14` |
| V15 | 1 item: Pills button → "Ratings" | renderer only | `?v=15` |
| V16 | 5 items: All RAs on / All CQs on rename, smaller buttons, reorder, spacers | renderer only | `?v=16` |
| V17 | 2 items: Element details default ON, stronger active-state visual | renderer only | `?v=17` |
| V18 | 1 item: Strip Advantaged business parenthetical from nav RAs | renderer only | `?v=18` |
| V19 | 1 item: Ratings button = nav pane only | renderer only | `?v=19` |
| V20 | 1 item: Suppress nav RAs + audit chips for line-items element | renderer only | `?v=20` |

**Total: 27 brief items across 10 versions.**

## Doctrine end state (1-May-26)

**`databases/memo-view-formatting-principles.md` v3.8** — formatting/shape rules + weight system (half/normal/double/quadruple) + stage scaling 3×/3.75× + group summary multi-row (BQ 2×3) + BQ summary-only element reorder + G5 Optionality 3-col override + element summary cols 2-4 + 11 named weight overrides (3 Pillar 1 elements DOUBLE; G3 Business quality group DOUBLE; G2 Required simplicity guardrails element DOUBLE; 4 RA-level DOUBLE: Lessons check, Negative earnings momentum, Crash through stops, Plain sight risks; 2 RA-level QUADRUPLE: Sector strength, General ACHs; 1 RA-level NORMAL defensive restatement: Conservative IR).

**`memory/skills/memo-view-formatting/SKILL.md` v2.8** — mirror of doctrine for SOP-citation purposes.

**Full quadruple-tier doctrine:**
- **Q1 Sector strength** (G4 / Strenuously seek-to-avoid attributes) — peer-quality canary RA
- **Q2 General ACHs** (G4 / Invalidating attributes) — canonical screening cohort for live-case discipline

**G4 Case riskiness weight roll-up (post-V20):**
| RA | Weight |
|---|---|
| General ACHs? | QUADRUPLE (Q2) |
| Plain sight risks? | DOUBLE (#11) |
| No mediocrity? | normal |
| Negative earnings momentum? | DOUBLE (#8) |
| Lessons check? | DOUBLE (#7) |
| Crash through stops risk? | DOUBLE (#10) |
| Mark-to-market risk? | normal |
| Sector strength? | QUADRUPLE (Q1) |
| Sentiment risk? | normal |

5 of 9 G4 RAs above normal weight — reflecting G4's load-bearing role in invalidation discipline.

## Live state

- **File:** `databases/memo-style-sheet3-htro.html` (893,215 bytes — V20)
- **Build script:** `databases/scripts/build-style-sheet3-htro.py` (85,542 bytes)
- **Live URL:** https://vfhqi.github.io/dashboards/memo-style-sheet3-htro.html?v=20
- **GitHub repo:** vfhqi/dashboards (public)
- **Latest commit:** `2f3e35b` — V20

## Build counts (V20)

- 19 elements
- 63 RAs in main pane (= 63 nav-RAs after V20 line-items suppression; was 70)
- 175 CQs in main pane (= 175 nav-CQs)
- 70 nav-audit chips (V14)
- 5 nav header toggle buttons: Ratings | Element details | [spacer] | All RAs on | All CQs on | [spacer] | Audit
- Defaults ON: Ratings, Element details

## Key process notes (carried forward)

1. **Every version backed up pre-write.** All 10 versions have `.bak-pre-vN-{timestamp}` siblings of the 4 mutated files.
2. **Every version has a FULL-BACKUP folder.** All 10 are in `memory/session-handoffs/transcripts/2026-05-01-*` (V11 through V20).
3. **Every version pushed live.** GitHub commits: `ac218ce` (V11), `ed162e9` (V12), `b0bf915` (V13), `854270f` (V14), `2419a17` (V15), `997f0c0` (V16), `086e7ef` (V17), `6385b02` (V18), `1f3ab94` (V19), `2f3e35b` (V20).
4. **0 truncation events this morning.** All multi-step build script patches applied via Python heredoc with incremental write-back per step (lesson learnt during V14 single-shot patch failure).

## Status going forward

V20 is **beta-canonical**: the memo template is broadly complete. Any further refinements are minor aesthetic. The CASE COMPONENTS work coming later today (key drivers / invalidation thresholds / leading tracking indicators — analogy: memo = "learning to fly", components = "in-flight checklist") may modify the SOP's downstream outputs but does NOT modify the memo template itself.

The morning's work is now treated as **APM role artefact**, not SA project deliverable. The APM A&J SOP review (1-May-26) takes the V20 template as input and asks: how does the APM produce work that fits this template?

## Cross-refs

- `memory/projects/ratings-dashboard/state.md` — per-version detail (V11→V20 entries at top)
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 — SOP mirror of doctrine
- `databases/memo-view-formatting-principles.md` v3.8 — full doctrine SSoT
- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP-review-2026-05-01.md` — APM SOP review (NEW, this morning)
- `memory/skills/research-stage-progression/SKILL.md` — Stage Progression SOP (NEW, this morning)
- `memory/session-handoffs/transcripts/2026-05-01-AM-FULL-BACKUP-COMPLETE/` — final FULL-BACKUP

## What's not in this rollup

- The per-version technical detail of each brief item (lives in state.md V11-V20 entries)
- The 9 incremental FULL-BACKUP folders (durable, kept for rollback)
- The HTRO real-content data (was at `htro_content_v2.json` in optimistic-kind-tesla session; absent in this session's mount; V11+ rebuilds rendered all-Lorem because brief items were renderer/doctrine-level not data-level)

---

*[W] Created 1-May-26 ~07:00 UK as part of FIRST step in three-action sequence (Save → Lessons → APM SOP review).*
