# Phase 0 Hunt Checklist — A&J SOP v2.5

**Use this checklist BEFORE any RESEARCHER reading or substantive analysis on a stock-specific A&J. Estimated time: ~30 minutes.**

**Why mandatory:** discovered HTRO V3→V4 10-May-26 — 51,629-word "deep" mega-A&J was anchored on stale share price + missed Richard's existing model + used wrong peer multiples. V4 corrections were 100% from this hunt. Phase 0 hunt prevents compound error.

---

## Hunt 1 — Existing financial model (Files/Financial models/)

```bash
find /sessions/*/mnt/COWORK/Files -iname "*{TICKER}*.xlsm" -o -iname "*{TICKER}*.xlsx"
```

Common location: `Files/Financial models/{TICKER} SS - Master Model.xlsm`

If found, extract:
- [ ] Sheet names list
- [ ] Identify HTRO-specific sheets vs template content from other stocks
- [ ] SF Output tab — Bull/Base/Bear SP scenarios (if exists)
- [ ] Consensus tab — full FactSet figures
- [ ] Trading Multiples tab — historical multiple range
- [ ] Sell-side ratings + PTs tab — current broker view
- [ ] Loss Analysis tab — downside floor methodologies
- [ ] UpDown tab — probability-weighted SP forecast
- [ ] Ratings tabs (1L, EGPIBC, Case Difficulty, SP Fragility, GTH, GTA) — Richard's own ratings
- [ ] Capital at Risk + Case Edge tab

**CAVEAT:** Not every sheet is HTRO-specific. Many tabs may contain template content from prior stocks (e.g., HTRO model had Hilton Food, Carlsberg, Banca Mediolanum content in some tabs). Apply judgement — don't treat every sheet as authoritative.

If NOT found: explicitly note "no existing model" in Phase 0.3 record.

---

## Hunt 2 — Master Dashboard pillar data

Read the following JSON files for the ticker:

- [ ] `databases/master/ic-ratings-current.json` — current pillar ratings P1-P6, stage, action, triggers
- [ ] `databases/detail/p1-technical-momentum.json` — MM99/Minervini score + RS rating
- [ ] `databases/detail/p2-market-paradigm-fit.json` — macro fit + AI exposure
- [ ] `databases/detail/p3-fundamental-change.json` — attribute ratings
- [ ] `databases/detail/p4-building-blocks.json` — attribute ratings
- [ ] `databases/detail/p5-ss-earnings-momentum.json` — SS EPS/EBITDA/PT momentum
- [ ] `databases/detail/p6-valuation.json` — forward EBITA multiple + percentile + peer discount

Document existing dashboard ratings as the BASELINE. Any APM-proposed revision must justify with new evidence.

---

## Hunt 3 — Current share price

WebSearch one of:
- "{COMPANY} share price {TICKER} today"
- "{COMPANY} stock price"
- "{TICKER} {EXCHANGE} quote"

Sources to prefer (in order): Yahoo Finance, Bloomberg, MarketScreener, Investing.com.

- [ ] Current SP: SEK / EUR / GBP / USD ___
- [ ] Source URL
- [ ] Date (verify ≤5 trading days old)

**DO NOT** rely on RR-text SP (often 1-3 months stale).
**DO NOT** rely on training-data SP (knowledge cutoff months back).

---

## Hunt 4 — Recent catalysts (post-last-results developments)

WebSearch a combination of:
- "{COMPANY} acquisition press release {recent year}"
- "{COMPANY} broker upgrade downgrade target price"
- "{COMPANY} {most recent quarter} results"
- "{COMPANY} profit warning OR capital raise OR M&A"

Look for:
- [ ] M&A announcements (size, multiple, strategic logic)
- [ ] Capital raises (size, discount, lock-up)
- [ ] Profit warnings or guidance changes
- [ ] Broker action (upgrades, downgrades, target price changes)
- [ ] Management changes (CEO/CFO/key exec departures)
- [ ] Sector-wide events (e.g., for fibre stocks: Corning AI deals, NVIDIA infra commitments)

Document each catalyst with: Date | Event | Likely impact direction (positive/negative/mixed) | Materiality (high/medium/low).

---

## Hunt 5 — Verified peer multiples

For each named peer in the ticker's sector (typically 4-6 peers), WebSearch:
- "{PEER} EV/EBITDA {recent year}"
- "{PEER} stock valuation forward multiple"

Build verified table:

| Peer | EV/EBITDA Forward | EBITA Margin | EBITDA CAGR | Source URL |
|---|---|---|---|---|
| Peer A | XX.Xx | XX.X% | XX% | url |
| Peer B | XX.Xx | XX.X% | XX% | url |
| ... | ... | ... | ... | ... |

**DO NOT** rely on training-data approximations — they may be 50-100%+ off current verified figures.

---

## Phase 0.3 record (mandatory in working file §F.I notes)

Append to working file:

```
Phase 0.3 hunts complete (per A&J SOP v2.5):

Hunt 1 (Existing model):
  - Status: {found at PATH | not found}
  - Key data: {bullets if found}

Hunt 2 (Master Dashboard):
  - ic-ratings P1=X, P2=Y, P3=Z, P4=A, P5=B, P6=C
  - last_updated: DATE
  - stage: STAGE
  - action: TEXT

Hunt 3 (Current SP):
  - Current SP: CURRENCY VALUE
  - Source: URL
  - Date: DATE

Hunt 4 (Recent catalysts):
  - DATE | Event | Direction | Materiality
  - ...

Hunt 5 (Peer multiples):
  - Peer | Multiple | source
  - ...

Phase 0.3 EXIT: PASS (all 5 hunts documented)
```

---

## Cross-references

- Originating incident: `memory/corrections.md` 2026-05-10 entry "Stale SP + Missing Existing Model + Underpriced Peer Multiples"
- A&J SOP: `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` Phase 0.3 [A19, NEW v2.5]
- Universal winning behaviour: CLAUDE.md "Stock-specific work requires Phase 0 hunt"

