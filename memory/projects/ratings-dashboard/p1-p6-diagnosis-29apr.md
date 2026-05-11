# P1–P6 Rendering Diagnosis — 29-Apr-26
<!-- [W] Phase 1 of the "fix P1-P6 visuals" chunk. Diagnosis only — no edits made. Delivered to Richard for sign-off before any code changes. -->

## Source artefact
- Dashboard: `databases/ic-ratings-dashboard-v2.html` (5,257,597 bytes, md5 `25aeee69...`, restored from 28-Apr-08:39 baseline)
- Richard's screenshot of local file (29-Apr-26) — used as authoritative visual reference

## Symptom (what Richard sees)

Three distinct rendering states across the 9 stocks' P1–P6 pillar cells:

| State | Stocks | Visual |
|---|---|---|
| Coloured badge | NVTK, HTRO, IGG (where rating ∈ {A, B, C, D, F}) | Green/amber/red filled box with rating letter |
| Cream "—" badge | All stocks where rating value = "—" (em dash) | Cream box with em dash, looks correct |
| **Plain coloured text — BUG** | EKTA, DCC, GET, PRY, DIE (where rating has + or − modifier) | Bare text "C+", "B-", "C+" with no badge background |

ENAV: every cell is "—". This is a *data* state (all pillars unrated), not a rendering bug — the cells render correctly as cream "—" badges.

## Root cause (presentation layer)

**`getRatingClass()` at line 72940 (and CSS at lines 231–275) only handle base ratings A/B/C/D/E/F + blank.**

```javascript
// line 72940
function getRatingClass(rating) {
    if (!rating || rating === "—") return "rating-blank";
    return 'rating-' + rating.toLowerCase();
}
```

When passed `"C+"`, this returns `"rating-c+"`. CSS then has no rule matching `.rating-c\+` (and `+` is not a valid CSS class character without escaping), so:
- The class is set on the span
- No background-color / color rule fires
- The span renders with default browser styles
- Result: bare text in the table cell

CSS at lines 242–270 only defines: `.rating-a`, `.rating-b`, `.rating-c`, `.rating-d`, `.rating-e`, `.rating-f`, `.rating-blank`. No rules for `+` / `−` modifier ratings.

This is consistent across all 6 render sites I found that use `getRatingClass`:
- Main RATINGS table (lines 74054–74059) — main table
- Map view, list view, memo view sub-renderers
- All hit the same bug for the same input

## Root cause (data layer)

The `masterData.stocks` block (line 68558) hard-codes the pillar values for each stock. Reading it directly:

| Stock | P1 | P2 | P3 | P4 | P5 | P6 | Source comment |
|---|---|---|---|---|---|---|---|
| NVTK | B | — | B | C | A | B | Hard-coded in dashboard |
| HTRO | A | C | B | C | F | C | Hard-coded |
| IGG | — | B | C | C | F | — | Hard-coded |
| ENAV | — | — | — | — | — | — | Hard-coded — all blank |
| EKTA | C+ | B− | C+ | — | — | — | Hard-coded — uses + modifiers |
| DCC | C+ | C | C | — | — | — | Hard-coded — uses + modifier |
| GET | C | C+ | C | — | — | — | Hard-coded |
| PRY | B− | B | B | — | — | — | Hard-coded — uses − modifier |
| DIE | C | C+ | C+ | — | — | — | Hard-coded |

**Two distinct data issues:**

1. **Inconsistent rating granularity.** Some stocks use only base letters (NVTK/HTRO/IGG), others use letter+modifier (EKTA/DCC/GET/PRY/DIE). This is the immediate trigger for the rendering bug.

2. **Data may not match underlying truth.** The `masterData.stocks.pillars` is hand-entered. Per MD1/MD2/MD3 (locked 28-Apr), the Master Dashboard is supposed to be the primary data source for P1 (technical), P5 (SS earnings momentum), and P6 (valuation). Currently the dashboard does not pull from `master-dashboard/data/*.json` at all — these values are static literals in the HTML. So the values may be stale, may not match the MD pipeline, may be wrong substantively. We don't yet know which.

3. **NVTK P5 = "A".** Given NVTK is fictitious test data, this may be deliberate placeholder. Worth confirming.

## Fix paths (proposed — no edits made yet)

### Path A — Presentation only, accept current data
Add CSS rules for modifier ratings: `.rating-aplus`, `.rating-bplus`, `.rating-bminus`, `.rating-cplus`, `.rating-cminus`, `.rating-dplus`, `.rating-dminus`. Update `getRatingClass()` to map `"C+"` → `"rating-cplus"` (sanitising the `+`/`−` for CSS). Hue/intensity ladder: A → B+ → B → B− → C+ → C → C− → D+ → D → D− → F. Result: every existing rating renders as a coloured badge. No data changes.

**Pro:** ~30 min including snapshot + screenshots. Fixes the immediate visual bug. Quality bar Q1 (full visual parity) achieved for what's currently in the data.
**Con:** Doesn't address whether the data is correct. If a rating is wrong, it'll still be wrong, just better-looking.

### Path B — Data correctness alongside presentation
Path A + Phase 4 review: I walk through every P1–P6 rating with you, sourcing each one from MD where possible (P1 from filter-results.json + prices.json; P5 from factset-ssem.json; P6 from factset-valuation.json) and from the memo JSONs for P2/P3/P4. We agree the correct rating, I update `masterData.stocks` to match. Eventually MD2 says "build pipeline reads from MD data files, not hand-entered" — that's the durable fix, but it's a bigger change and I propose we defer it.

**Pro:** Fixes both the visual bug AND the substantive correctness question.
**Con:** Slower. Requires your time per pillar per stock — 9 stocks × 6 pillars = 54 ratings to sign off, though many are "—" placeholders that need no review.

### Path C — Rebuild masterData from MD pipeline (durable)
Write a build script that reads `master-dashboard/data/*.json` + the 8 ticker memo JSONs and emits a fresh `masterData.stocks` block. Patcher injects it into the dashboard. Future dashboard refreshes are one command. Implements MD2 properly.

**Pro:** Fixes data drift permanently.
**Con:** Larger change. Schema bridge between MD ticker IDs (HTRO-SE) and RD ticker IDs (HTRO). Some stocks (IGG, EKTA, GET, DIE) aren't in MD SSEM/Valuation universe — needs MD3 placeholder logic. Probably 2–3 hours to do correctly.

## Recommended sequencing

**Now (this chunk):** Path A — fix the rendering for what's already in the data. Quick, mechanical, independently reversible. Get the visual right.

**After sign-off on Path A:** Phase 4 (Path B's data review) — walk through P1–P6 of each stock, agree corrections, edit `masterData.stocks`.

**Future chunk (separate decision):** Path C — durable build pipeline from MD. Don't bundle into this chunk.

## What I have NOT yet checked

- The exact rating ladder you want (A, A−, B+, B, B−, C+, C, C−, D+, D, D−, F? Or simpler — A, B+, B, B−, C+, C, C−, D, F?). I'll need this before writing the CSS.
- Whether any other components in the dashboard (MAP view, LIST view, MEMO view) render P1–P6 ratings — they likely do (line 73911, 74880 etc. all use `rating-badge` + `getRatingClass`), so the same fix needs to flow to all of them. I will trace the call sites and fix all of them in Path A.
- Whether the modifier rating values map to a numeric scale somewhere (sorting, scoring) — if so, the data model needs awareness of `C+ > C > C−` ordering.

## Proposed next action

Bring this diagnosis to Richard. Get sign-off on:
1. Path A as the immediate fix (presentation-only, mechanical CSS + class-mapping)
2. The rating ladder to support
3. Whether to fix only the main RATINGS table first, or all render sites in one pass

No code touched until Richard confirms.
