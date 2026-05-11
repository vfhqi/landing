# C.I Integration Plan — V3 → V2 Dashboard
<!-- [W] Created 21-Apr-26 19:00 UK. Richard's answers to Q-CI-1 through Q-CI-5 locked. -->

## Source

V3 = `databases/ic-ratings-dashboard-v3.html` (reference design, has the full 5-depth C.I).
V2 = `databases/ic-ratings-dashboard-v2.html` (live dashboard, current target for integration).

## Richard's locked answers (21-Apr-26 evening)

| Q | Question | Answer | Design implication |
|---|----------|--------|---------------------|
| Q-CI-1 | Depth default on load — (A) Pillars, (B) Families, (C) TCs, (D) Attributes, (E) Questions? | **C — TCs** | Default depth = TCs. Richer-than-Families, still scannable; user drills down or up from there. |
| Q-CI-2 | MAP-style pillar cards above the table — preserve or drop? | **Preserve** | Keep the V3 MAP-style cards above the table. They provide at-a-glance pillar ratings and are the click-through anchors. |
| Q-CI-3 | Per-stage columns (Triaging/ESA/DD side-by-side)? | **Yes** | Three stage columns visible simultaneously. Lets Richard see stage progression in one glance. |
| Q-CI-4 | Clickable pillar-name jump anchors to C.II.1-5? | **Approved** | Wire pillar-card titles + pillar-row labels to scroll to matching C.II.N subsection on click. |
| Q-CI-5 | JUDGEMENTS + ANALYSIS column toggles — show/hide? | **Toggleable** | Two independent toggles above the table; start with both visible (per V3 default). |

## Synthesis — the integrated C.I design

### Top-of-section controls (three clusters, left-to-right)

1. **Depth selector** — five-button pill row: `Pillars · Families · TCs · Attributes · Questions`. Active state = current depth. Default = TCs.
2. **Column visibility toggles** — two switches: `JUDGEMENTS ✓` and `ANALYSIS ✓`. Both on by default.
3. **Stage columns indicator** — passive (all three columns always rendered, but header shows "Triaging / ESA / DD" labels).

### MAP-style pillar cards (between controls and table)

- Preserve V3 layout: horizontally-flowing cards, one per pillar (P1 / P2 / P3 / P4 / P5 / P6).
- Each card shows: pillar ID + name + rating chip + 1-line summary.
- Click card title → scrolls to matching C.II.N subsection anchor.

### Ratings table (core)

- Rows driven by depth selector (Pillars/Families/TCs/Attributes/Questions).
- Columns: `Label | Triaging rating + summary | ESA rating + summary | DD rating + summary | JUDGEMENTS column | ANALYSIS column`.
- JUDGEMENTS and ANALYSIS columns hide/show via toggles.
- Pillar label cells clickable → scroll to C.II.N.

### Default load

- Depth = **TCs**
- Judgements shown, Analysis shown
- All three stage columns rendered
- MAP cards rendered above

## Integration approach (step-by-step)

1. **Extract V3's renderMemoRatingsTable + renderMemoRatingsCards + renderDepthChildren + controls HTML** — read once, snapshot into a dedicated patch file under `databases/scripts/ci-v3-to-v2/`.
2. **Build marker-wrapped patcher** `databases/scripts/patch-ci-integration.py` with markers `CI_INTEGRATION_V1_START/END` — idempotent, re-runnable.
3. **Strip V2's current `memo-rtable-v2`** (mode-summaries/mode-ratings toggle + all lvl-* class handling) from the renderMemoSectionC path — replace with V3 renderer.
4. **Wire depth default to TCs** in the renderer's initial-state variable.
5. **Wire clickable anchors**: `pillarName.onclick = memoScrollTo('c-ii-1')` etc. — follow existing memoScrollTo signature.
6. **CSS**: port V3's C.I-specific styles into the live dashboard CSS using marker-wrapped block `CI_STYLES_V1_START/END`.
7. **Test locally**: bake dashboard, verify: depth toggles work, stage columns align, pillar clicks jump, judgement/analysis toggles hide/show columns, MAP cards render.
8. **Snapshot + validate** structure (no var PB, scripts balanced, ends `</html>`).

## Unknowns to confirm while integrating

- How many rows does each depth level produce for NVTK? At Questions depth, could be 200+ rows — needs verification for usability.
- Do Triaging/ESA/DD columns render *all three* stage values per row, or does the dashboard-level stage toggle still gate which values show? **Proposal:** all three always visible in C.I (C.I is the "progress across stages" view), while C.II and other sections honour the memo-level toggle. Surface this decision to Richard if it doesn't match intent.
- Where does the depth-state live — per-stock or global across stocks? **Proposal:** per-stock (each ticker's MEMO tab remembers its depth), consistent with how the stage toggle works.

## Files that will change

| File | Change |
|------|--------|
| `databases/ic-ratings-dashboard-v2.html` | CSS + JS + HTML control row added via marker-wrapped patch |
| `databases/scripts/patch-ci-integration.py` | NEW — idempotent patcher |
| `databases/scripts/ci-v3-to-v2/` | NEW folder — extracted V3 snippets for reference |
| `databases/memos/*/Triaging.json` etc. | No changes required — ratings_table data schema already supports the V3 renderer |
| `memory/projects/ratings-dashboard/decisions.md` | Add CI1-CI5 decisions block |
| `state.md` | Update when integration complete |

## Snapshot discipline

Before first patch run: copy current dashboard.html to `snapshots/{YYYY-MM-DD-HHMM}-pre-ci-integration/`.
