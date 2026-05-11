# D8 Data Plan — Tree Data for Non-NVTK Stocks
<!-- [W] Drafted 28-Apr-26 morning. SHOW TO RICHARD BEFORE WRITING CODE. -->

## What I found (root cause)

Line **73869** of `databases/ic-ratings-dashboard-v2.html`:

```javascript
var treeData = stock.ticker === 'NVTK' ? treeDataNVTK : null;
```

That's the entire bug. Every non-NVTK stock gets `null`, which falls through to "Tree data not yet populated for this stock."

Currently in the dashboard:
- **NVTK** gets the full `treeDataNVTK` object (416 KB JSON, 6 pillars, deep tree with families/TCs/CQs)
- **HTRO + IGG** have a *partial* fix via `momentumDataByTicker` (P5 only) and `valuationDataByTicker` (P6 only) — but P1/P2/P3/P4 are still null
- **ENAV, EKTA, DCC, GET, PRY, DIE** have nothing — all 6 pillars null

## Tree-data shape (from NVTK reference)

```
treeData = {
  ticker, company_name, sector, industry, market_cap_eur_bn, stage, status, last_updated,
  pillars: {
    p1: { id, label, type, nature: "formulaic",   rating, judgement, analysis, metrics, dimensions }
    p2: { id, label, type, nature: "qualitative", rating, judgement, analysis }
    p3: { id, label, type, nature: "qualitative", rating, judgement, analysis, families: [...] }  ← DEEP
    p4: { id, label, type, nature: "qualitative", rating, judgement, analysis, families: [...] }  ← DEEP
    p5: { id, label, type, nature: "momentum",    rating, judgement, analysis, momentum_data }
    p6: { id, label, type, nature: "valuation",   rating, judgement, analysis, metrics }
  }
}
```

Per-pillar payload sizes for NVTK: P1 2.4KB, P2 0.5KB, P3 73KB, P4 49KB, P5 1.6KB, P6 1.1KB. P3 and P4 are 95% of the bulk — the case-tree pillars.

## Master Dashboard coverage matrix (per MD1: primary data source)

The 8 non-NVTK ratings dashboard tickers map to Master Dashboard like so:

| RD ticker | MD ticker | prices.json | filter-results.json | factset-ssem.json | factset-valuation.json |
|-----------|-----------|-------------|---------------------|-------------------|------------------------|
| HTRO | HTRO-SE | ✓ | ✓ | ✓ | ✓ |
| IGG  | IGG-GB  | ✓ | ✓ | ✗ | ✗ |
| ENAV | ENAV-IT | ✓ | ✓ | ✓ | ✓ |
| EKTA | EKTA-SE | ✓ | ✓ | ✗ | ✗ |
| DCC  | DCC-GB  | ✓ | ✓ | ✓ | ✓ |
| GET  | GET-FR  | ✓ | ✓ | ✗ | ✗ |
| PRY  | PRY-GB  | ✓ | ✓ | ✓ | ✓ |
| DIE  | DIE-BE  | ✓ | ✓ | ✗ | ✗ |

**Verdict:** P1 (Technical Momentum) is fully sourceable from MD for all 8 stocks. P5 (SS Earnings Momentum) and P6 (Valuation in Range) are MD-sourceable for 4 of 8 (HTRO, ENAV, DCC, PRY); the other 4 (IGG, EKTA, GET, DIE) need MD3 placeholder treatment ("—" + tooltip "Not in Master Dashboard universe yet").

## Field-level sourcing plan

For each pillar, here's where every field comes from:

### P1 — Technical Momentum (formulaic, MD-sourced, ALL 8 stocks)

| Field | Source |
|-------|--------|
| `rating` | Computed from `filter-results.json[mm99].score` (MM99 0-11 score) using existing scoring rule (already in dashboard for NVTK) |
| `judgement[]` | Templated: "MM99 {score}/11. {qualifying_filter} qualified. RS {rs_excess}." |
| `analysis[]` | Templated bullets from `prices.json` MA structure + `mm99` test-by-test breakdown |
| `metrics` | `prices.json` (price, MA50/100/150/200, 52W high/low, RS) + `filter-results.json[mm99]` |
| `dimensions[]` | The 11 MM99 tests from `filter-results.json[mm99].test_results` |

### P2 — Market Paradigm Fit (qualitative, APM-authored)

| Field | Source |
|-------|--------|
| `rating` | From memo `sections.C.subsections.['C.II.3'].pillar_block.rating` (HTRO/IGG/ENAV/EKTA/DCC/GET/PRY/DIE all have memo JSONs at Triaging stage) |
| `judgement[]` | From memo C.II.3 pillar_block bluf + bullet items |
| `analysis[]` | From memo C.II.3 pillar_block analysis bullets |

### P3 — Fundamental Change (qualitative, APM-authored, DEEP TREE)

| Field | Source |
|-------|--------|
| `rating` | Memo `sections.C.subsections.['C.II.2'].pillar_block.rating` (P3 portion) |
| `judgement[]` | Memo C.II.2 P3 bluf + IC#1/IC#2/IC#3 family rollups |
| `analysis[]` | Memo C.II.2 P3 analysis bullets |
| `families[]` | Memo C.II.2 IC#1, IC#2, IC#3 family_blocks → mapped into the tree shape (CQs, RAs, TCs as children) |

### P4 — Building Blocks (qualitative, APM-authored, DEEP TREE)

| Field | Source |
|-------|--------|
| `rating` | Memo C.II.2 pillar_block.rating (P4 portion) |
| `families[]` | Memo C.II.2 BB#1–BB#8 family_blocks → mapped into the tree shape |

### P5 — SS Earnings Momentum (momentum, MD-sourced for 4 stocks)

| Field | Source |
|-------|--------|
| `rating` | Computed from `factset-ssem.json[ticker].momentum` score using existing 5×3 matrix scoring (≥12=A, ≥10=B, ≥8=C, ≥6=D, else=F) |
| `momentum_data.eps_change.{l1m,l3m,l6m}` | `factset-ssem.json[ticker].eps_rev.{L1M,L3M,L6M}` |
| `momentum_data.ebitda_change.*` | `factset-ssem.json[ticker].ebitda_rev.*` |
| `momentum_data.revenue_change.*` | `factset-ssem.json[ticker].sales_rev.*` |
| `momentum_data.price_target_change.*` | `factset-ssem.json[ticker].tp_rev.*` |
| `momentum_data.pct_buy_change.*` | `factset-ssem.json[ticker].buy_rev.*` |
| `judgement[]` | Templated from raw values |

For IGG / EKTA / GET / DIE: rating = "—", momentum_data zeroed, judgement = `["Not in Master Dashboard SSEM universe yet — placeholder."]` per MD3.

### P6 — Valuation in Range (valuation, MD-sourced for 4 stocks)

| Field | Source |
|-------|--------|
| `metrics.forward_pe` | `factset-valuation.json[ticker].pe_current` |
| `metrics.pe_percentile` | `factset-valuation.json[ticker].pe_percentile` |
| `metrics.ev_sales_current` | `factset-valuation.json[ticker].ev_sales_current` |
| `metrics.pe_10y_range` | `[pe_10y_low, pe_10y_high]` |
| `metrics.pe_sparkline` | `pe_sparkline` array |
| `rating` | Computed from `pe_percentile` (≤25th=A, ≤40th=B, ≤60th=C, ≤80th=D, else=F) |

For IGG / EKTA / GET / DIE: same MD3 placeholder treatment.

## Build approach

**Single Python build script:** `databases/scripts/build-tree-data.py`

Inputs:
- `master-dashboard/data/prices.json`
- `master-dashboard/data/filter-results.json`
- `master-dashboard/data/factset-ssem.json`
- `master-dashboard/data/factset-valuation.json`
- `master-dashboard/data/ticker_mapping.json` (RD ticker → MD ticker bridge)
- `databases/memos/{TICKER}/{Stage}-v3.json` for each ticker

Outputs:
- A new `treeDataByTicker` JS object containing entries for all 9 stocks (NVTK preserved unchanged, other 8 newly built)
- Patches the dashboard at the line 73869 site:
  - Replace `var treeData = stock.ticker === 'NVTK' ? treeDataNVTK : null;` with `var treeData = treeDataByTicker[stock.ticker] || null;`
  - Inject the new `treeDataByTicker` block after the existing `treeDataNVTK` block (idempotent, marker-wrapped)

**Markers:** `TREE_DATA_BY_TICKER_START` / `TREE_DATA_BY_TICKER_END` so the script can re-run safely.

**Validation gate:** After patch, run the standard checks (ends `</html>`, no `var PB`, scripts balanced, `renderMinervini` present) PLUS new checks (`treeDataByTicker` defined, all 9 ticker keys present, each pillar has required fields).

## Estimated payload

- P1 + P5 + P6 templated for 8 stocks: ~50 KB total
- P2 from memos for 8 stocks: ~20 KB
- P3 + P4 from memos (deep tree) for 8 stocks: this is the big one

P3 + P4 from existing memos is a meaningful translation job. The memo JSONs use the `pillar_block` / `family_block` / `bullet_group` schema, but `treeDataNVTK` uses `families: [{children: [...]}]` shape with different field names. **This is a non-trivial schema bridge.**

Two options for P3 + P4 here:

**Option A — full deep-tree translation (correct):** Build a memo-to-tree converter that walks family_blocks → families, bullet_groups → children, and produces the same nesting shape NVTK has. Higher fidelity, more work (~2 hours of code), produces real CQ/RA/TC drilldown for all 8 stocks.

**Option B — pillar-summary-only (cheap):** Skip the deep tree for now. P3 / P4 entries get `rating`, `judgement`, `analysis` populated from the memo's pillar_block, but `families: []` is empty. The pillar card opens but shows no drill-down. Still fixes D8 (no more "Tree data not yet populated"), still fixes D1/D3/D4/D10. Just no rich drill-down on P3/P4 for the 8 stocks until you author it properly.

**My recommendation: Option B** for today, Option A as a follow-up project. Reasons:

1. The deep tree is APM-authored content. Copying it from memo to tree should be lossless, but every translation introduces drift risk. Better to keep memos as the SSoT and have one rich source of P3/P4 content (the memo) than two diverging copies.
2. Option A is two hours of code + risk of bugs + need for visual sign-off on the drill-down rendering. Option B fixes D8 in 30 minutes and we move to the rest.
3. You can already see P3/P4 drill-down via the MEMO button on each row — that's the canonical path. The tree's P3/P4 drill-down is duplication.
4. If you later disagree, Option A can be added later as a separate workstream — the data shape is documented and the converter is the only piece missing.

## Three questions before I code

1. **Option A or Option B for P3/P4 deep tree?** I recommend B.
2. **For the 4 stocks missing from MD SSEM/Valuation (IGG, EKTA, GET, DIE):** "—" placeholder + tooltip "Not in Master Dashboard universe yet" (per MD3) — confirm?
3. **NVTK itself:** keep `treeDataNVTK` as-is and preserve it inside the new `treeDataByTicker` object (so no NVTK content changes), or rebuild NVTK from memo/MD too (consistency at the cost of touching working content)? **I recommend keeping NVTK as-is** — touching what already works is risk for no benefit.

Once you answer, I'll code the build script, run it, snapshot, and push for visual verification.
