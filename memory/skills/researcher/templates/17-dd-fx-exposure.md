# Query 17: FX Exposure — Claude ONLY (DD)

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/17-dd-fx-exposure.md`. Standard v2.1 pattern. NO BB#2 overlay. **5L SS breadth gate SKIP per D-RSR-20 ([C]-only).** **DD stage.** Public-filings-driven FX risk analysis.

> **⚠️ NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT (locked 30-Apr-26 by Richard).** Reader has read Q1 IG BD. Start directly with the FX exposure analysis.

---

## MISSION

Comprehensive FX risk analysis for {TICKER} ({COMPANY}). Quantify revenue/cost currency mismatch, translation vs transaction exposure, hedging policy effectiveness, and forward FX-as-tailwind-or-headwind for the thesis.

Output: comprehensive memo, target {WORD_TARGET} words (default ~5,000-6,000w under v2.1 density doctrine; legitimate-paucity bypass available — see VALIDATION GATES). Structured by analytical section per the bulleted-format doctrine below. Every quantitative claim peer-anchored. Every section opens with a J-front verdict bullet. Sceptical lens per section. **Mandatory FX sensitivity table** + **mandatory revenue-by-currency table** + **mandatory cost-by-currency table**.

---

## CONTEXT — What the Reader Cares About

**Audience:** Richard Black, concentrated long-only equity investor (5-15 positions), UK/European focus, $5-50bn market cap. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**Stage — DD:** Resolve hidden earnings drivers. FX is often the most-under-modelled translation risk (especially for UK/European stocks with USD-denominated revenue or EUR-denominated cost base). Quantify exposure + sensitivity + hedging discipline.

**Why this query matters:** FX can flatter or undermine the EPS trajectory thesis materially. A stock guiding 12% EPS growth with a 4% FX tailwind is actually growing 8% organically. A stock guiding 8% with a 3% FX headwind is growing 11% organically. Without quantified FX, EPS growth analysis is incomplete. Q17 produces specific sensitivity tables Richard can plug into his own forecast.

**Mental models:** Translation exposure (P&L impact from foreign currency revenue/cost translation), transaction exposure (economic impact from currency mismatch on actual cash flows), natural hedging (cost in same currency as revenue eliminates risk), hedging policy effectiveness (does the company hedge transactional risk while accepting translational risk, or vice versa?).

**What downstream uses this output:** APM Pass 3 + DD-stage decision. Q17 feeds Pillar P3 IC#1 RA1 + RA2 (financial-output predictability — if FX volatility is high, output predictability is lower). Memo also surfaces on RESEARCH STAGES dashboard tab. **No-AS-access ([C]-only)** because FX exposure data is in public filings — segment revenue, geographic revenue mix, hedging policy disclosures, sensitivity tables management often provides themselves.

---

## DEPTH AND COMPLETENESS — MANDATORY

Every analytical sub-question named in SECTIONS TO COVER must be addressed substantively. The bulleted format constrains the *shape* of output, not its *depth*. Quantify every claim. FX analysis is intrinsically numeric — qualitative-only is failure mode.

**The test:** would Richard learn something about {COMPANY}'s FX exposure that he couldn't get from reading the FX section of the annual report? If the bullet just restates the company's own disclosure, it's filler. If it triangulates revenue mix + cost mix + translation impact + transaction impact + hedge effectiveness + macro outlook to surface a specific quantified sensitivity — that's analytical content.

---

## OUTPUT DOCTRINE (mandatory format)

Standard v2.1 OUTPUT DOCTRINE applies. RESEARCHER does NOT grade. Tables are first-class for Q17.

**⚡ marker scope:** encompasses (a) statistical outliers (top/bottom 5% on some dimension — e.g. hedging discipline duration in top decile of cohort; FX-translation exposure in bottom-decile transparency), (b) deliberately-weird signals — qualitative oddities (e.g. unexplained hedge-instrument switch, unusual currency-mix changes), cross-roads exposures the consensus is ignoring, "things that make me go hmmmm". Sparse-by-design — ≤3 per memo.

### Memo skeleton

```
1. METADATA HEADER
2. KEY FINDINGS (BLUF) — 5-10 parent bullets
3. §1-§9 Body Sections
4. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
5. AGGREGATE OUTLIERS (⚡)
6. QC AUDIT PANEL (validator-filled — no 5L for Q17)
7. QC COMMENTARY (RESEARCHER-authored)
8. QC FOOTER
```

---

## SECTIONS TO COVER

### §1 — Revenue by Currency (geographic breakdown + mix trends)

**Open with J-front verdict bullet:** Net signal on revenue-currency exposure — concentrated, diversified, or mismatched — ≤30w.

**Canonical signpost vocabulary:** "Reporting currency:", "USD revenue %:", "EUR revenue %:", "GBP revenue %:", "Other currency %:", "Geographic mix L3Y:", "Mix trend:", "FX-driven growth:", "Constant-currency growth:". Invent where pattern warrants.

**Analytical sub-questions:**
- Revenue split by reporting currency (and geographic if not 1:1).
- Mix trend L3Y: shifting toward / away from reporting currency?
- Recent FX-driven vs organic growth contributions.

**Coverage:** 6-10 parent bullets + sub-bullets. **Mandatory revenue-by-currency table** (currency × % L1Y × % L2Y × % L3Y × trend).

**End with sceptical bullet:** "What's the bearish read on revenue-currency mix? Through what mechanism might apparent diversification mask concentrated exposure?"

---

### §2 — Cost by Currency (natural hedges + mismatches)

**Open with J-front verdict bullet:** Net signal on cost-currency mismatch vs revenue — naturally hedged or exposed — ≤30w.

**Canonical signpost vocabulary:** "COGS currency mix:", "Opex currency mix:", "Capex currency mix:", "Natural hedge ratio:", "Mismatch — revenue vs cost:", "Margin FX sensitivity:", "Input cost currency:". Invent where pattern warrants.

**Analytical sub-questions:**
- Cost split by currency (COGS, opex, capex separately).
- Natural hedging: does cost mix match revenue mix?
- Mismatches: where revenue is in currency X but cost in currency Y.

**Coverage:** 6-10 parent bullets + sub-bullets. **Mandatory cost-by-currency table.**

**End with sceptical bullet:** "What's the bearish read on cost-currency exposure? Through what mechanism might apparent natural hedging be partial / break in stress scenarios?"

---

### §3 — Translation Exposure (reported earnings impact L3Y)

**Open with J-front verdict bullet:** Net signal on translation-driven P&L impact L3Y — ≤30w.

**Canonical signpost vocabulary:** "Reported FX impact L1Y:", "Reported FX impact L3Y average:", "Translation hit:", "Translation tailwind:", "Reporting currency strength:", "Reporting currency weakness:". Invent where pattern warrants.

**Analytical sub-questions:**
- Reported FX impact on revenue / EBITDA / EPS L3Y per period.
- Translation magnitude in average year vs stressed year.
- Reporting currency trajectory and impact on translation.

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on translation? Through what mechanism might apparent translation stability mask binary-event risk?"

---

### §4 — Transaction Exposure (economic impact)

**Open with J-front verdict bullet:** Net signal on transaction-exposure economic impact — ≤30w.

**Canonical signpost vocabulary:** "Transaction exposure:", "Cash-flow currency mismatch:", "Margin economic impact:", "Pricing pass-through:", "Cost pass-through:". Invent where pattern warrants.

**Analytical sub-questions:**
- Transaction-exposure points: where cash flows in one currency must convert to another.
- Magnitude vs translation exposure.
- Pricing power — can {COMPANY} pass through FX moves to customers?
- Cost pass-through ability.

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on transaction exposure? Through what mechanism might apparent pass-through pricing fail in real FX shock?"

---

### §5 — Hedging Policy Assessment

**Open with J-front verdict bullet:** Net signal on hedging discipline — comprehensive, partial, ad-hoc, or absent — ≤30w.

**Canonical signpost vocabulary:** "Hedging mandate:", "Hedge horizon:", "Hedge ratio:", "Hedge instruments:", "Translation hedging:", "Transaction hedging:", "Hedge effectiveness:", "Hedge cost:", "Recent hedge realisation:". Invent where pattern warrants.

**Analytical sub-questions:**
- Hedging policy from public disclosure: hedge ratio, horizon, instruments, board mandate.
- Translation hedging (often not done, deliberately).
- Transaction hedging (typical).
- Hedge effectiveness L3Y.
- Hedge cost / hedge income recognition.

**Coverage:** 8-12 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on hedging discipline? Through what mechanism might disclosed hedging policy be less effective than implied?"

---

### §6 — Quantified Sensitivity Analysis (LOAD-BEARING for Q17 — DOMINATES the summary)

**Open with J-front verdict bullet:** Net signal on EPS sensitivity to major currency moves — ≤30w. **This is the single most quoted output of Q17 in the BLUF and §11 Watson Verdict.** A Q17 memo where the sensitivity table is hidden deep is a failed memo.

**Canonical signpost vocabulary:** "USD ±10% impact:", "EUR ±10% impact:", "GBP ±10% impact:", "Single-currency sensitivity:", "Multi-currency simulation:", "Stress scenario:", "Bull scenario:", "Base scenario:", "Translation effect:", "Transaction effect:", "Hedge break point:", "Second-order pricing pass-through:", "Tail-currency stress:". Invent where pattern warrants.

**Analytical sub-questions (expanded per D-RSR-33):**
- Build sensitivity table: ±5% / ±10% / ±20% moves in major currencies → revenue, EBITDA, EPS impact.
- **Decompose translation vs transaction effect** explicitly per currency. Translation is mechanical and reverses; transaction is durable. Don't conflate.
- Cross-currency: combined moves (e.g. USD strength + EUR weakness; commodity-block FX shock).
- **Stress scenarios beyond ±20%:** stress at ±30% / ±40% to surface non-linearities (hedge break points, customer-pass-through ceilings, supplier-renegotiation triggers).
- **Hedge break point:** at what FX move does the disclosed hedging programme stop being effective? (e.g. duration shortfall — hedges roll off mid-shock; quantum shortfall — only X% of exposure hedged; counterparty-credit risk if hedge issuer is regional bank).
- **Second-order pricing pass-through:** can {COMPANY} pass through FX-driven cost inflation? At what lag? In which segments? Pricing power is the FX shock-absorber that doesn't show in the static sensitivity table.
- Compare to historical realised FX impact L3Y — does management's stated sensitivity match the L3Y empirical record, or has the disclosed sensitivity been understated?
- **Tail-currency exposures** (smaller currencies that compound in stress — e.g. EM currency basket in commodity correction). Surface even if individual exposure is sub-5%.

**Coverage:** 12-18 parent bullets + sub-bullets (raised from 8-12 per D-RSR-33 — sensitivity is the load-bearing output).

**Mandatory tables (TWO, not one):**
1. **Static sensitivity table:** currency × ±5% × ±10% × ±20% × revenue impact × EBITDA impact × EPS impact, separated translation vs transaction.
2. **Stress sensitivity table:** ±30% / ±40% moves with hedge-break flagging + pricing-pass-through flagging + named tail-currency stress scenarios.

**End with sceptical bullet:** "What's the bearish read on sensitivity? Through what mechanism might non-linear effects (hedge break mid-shock, second-order pricing failure, tail-currency cascade, segment-specific FX-cost pass-through ceilings) amplify the impact materially beyond the disclosed sensitivity table? Has management's disclosed sensitivity been benchmarked against the L3Y empirical FX-impact record — and if it diverges, in which direction?"

---

### §7 — Peer FX Exposure Comparison (EXPANDED — sector hedging principles + named-peer comparison)

**Open with J-front verdict bullet:** Net signal on {COMPANY}'s FX exposure AND hedging discipline vs {PEERS} — ≤30w. **Hedging discipline is as load-bearing as exposure** — two peers with identical exposures but different hedging programmes have materially different FX-shock fragility.

**Canonical signpost vocabulary:** "Peer revenue mix:", "Peer cost mix:", "Peer hedging discipline:", "Hedge duration:", "Hedge ratio:", "Hedge instrument mix:", "{COMPANY} vs peer median:", "Outlier exposure:", "Outlier discipline:", "Hedging philosophy:", "Sector hedging norm:", "Counter-cyclical hedging:", "Pro-cyclical hedging:". Invent where pattern warrants.

**Sector-general FX-hedging principles (NEW per D-RSR-33 — apply universally):**

These are the cross-sector principles RESEARCHER applies when analysing hedging quality. Make them explicit in the memo so APM can use them as benchmarks:

- **Hedge duration matters more than hedge ratio.** A company that hedges 100% of next-quarter exposure but 0% of next-year exposure is more fragile to a sustained FX shock than a company that hedges 70% across 18 months. Long-duration hedging ladders are the gold standard.
- **Counter-cyclical hedging beats pro-cyclical.** Companies that increase hedge ratios when FX is cheap (counter-cyclical) preserve optionality. Companies that increase hedges only when FX is moving against them (pro-cyclical) lock in unfavourable rates.
- **Instrument mix reflects discipline.** Forwards + collars (asymmetric protection) > forwards alone > options-only (often expensive) > no hedging. Instrument concentration in a single counterparty is a counterparty-credit signal worth flagging.
- **Disclosed hedging policy ≠ realised hedging.** Cross-check disclosed policy against L3Y realised gain/loss on derivative instruments (FRS 102 / IFRS 9 disclosure) — the realised numbers are the truth.
- **Natural hedging (matching geographic revenue and cost) > financial hedging.** Companies with structurally matched geographic revenue and cost have lower hedging-programme cost AND lower programme-execution risk. Operating-side hedging is the structural advantage; financial-side hedging is the band-aid.
- **The "boring" hedger wins.** Companies that publish quarterly hedge-position summaries, name their hedge horizon, and report realised effectiveness ratios are usually well-disciplined. Companies that obfuscate ("we hedge our material exposures") usually aren't.

**Analytical sub-questions (expanded per D-RSR-33):**
- {PEERS} revenue/cost currency exposure for context — name peers explicitly with currency-mix figures.
- {PEERS} hedging discipline — pull disclosed hedge ratio, hedge duration, instrument mix per peer where disclosed.
- {COMPANY} vs peer median: more / less exposed? More / less disciplined? Outlier in either direction?
- Sector-level FX commentary — what is the sector's hedging philosophy?
- **Named-peer hedging comparison (REQUIRED — at least one named-peer pair):** e.g. "Carlsberg's hedging horizon (12M rolling, 70% covered) vs Royal Unibrew (24M rolling, 80% covered) — Royal Unibrew's longer-duration hedge is more protective in a sustained EUR-strength scenario." Use peers RESEARCHER and APM both recognise. The named-peer comparison is the load-bearing analytical move that surfaces hedging discipline as differentiated, not aggregated.
- Apply the sector-general principles above to rank {COMPANY} on each dimension (duration / ratio / cyclicality / instrument mix / natural vs financial / transparency).

**Coverage:** 10-15 parent bullets + sub-bullets (raised from 6-10 per D-RSR-33). **Mandatory peer hedging table** (peer × hedge ratio × hedge duration × instrument mix × natural-hedge presence × disclosure quality) — populate with named peers + figures where disclosed; use "n.d." cell + "ESA depth" cross-ref where not.

**End with sceptical bullet:** "What's the bearish read on peer-relative FX position AND hedging discipline? Through what mechanism might {COMPANY}'s exposure prove more fragile than peers in stress — and would the gap be visible in the static peer table, or only in the stress scenario where peers' longer-duration / counter-cyclical / natural-hedge advantages compound? Where does {COMPANY} sit on the 'boring hedger' transparency spectrum vs peers?"

---

### §8 — Macro FX Outlook (N12-24M)

**Open with J-front verdict bullet:** Net signal on macro FX direction relevant to {COMPANY}'s mix — tailwind, headwind, or neutral — ≤30w.

**Canonical signpost vocabulary:** "USD outlook:", "EUR outlook:", "GBP outlook:", "Consensus FX view:", "Range outlook:", "Tail risk — currency:", "Macro driver:", "Rate differential:". Invent where pattern warrants.

**Analytical sub-questions:**
- N12-24M consensus FX outlook for major currencies in {COMPANY}'s mix.
- Range of forecasts (consensus dispersion).
- Macro drivers (rate differentials, current account, political risk).
- Tail risks.

**Coverage:** 6-10 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish FX-outlook read? Through what mechanism might consensus underestimate currency volatility on {COMPANY}'s mix?"

---

### §9 — FX as Tailwind/Headwind for Thesis + Sceptical Synthesis (cross-cutting)

**Open with J-front verdict bullet:** Cross-cutting: net FX impact on the EPS-trajectory thesis — ≤30w.

**Canonical signpost vocabulary:** "Net FX vs thesis:", "Tailwind quantified:", "Headwind quantified:", "Thesis robustness vs FX:", "Reverse-engineered FX bear:", "Single largest FX risk:". Invent where pattern warrants.

**Analytical sub-questions:**
- Combine §1-§8 to assess: is FX a tailwind, headwind, or neutral for the thesis?
- Quantify the thesis's FX-dependence: if FX moves adversely, what happens to EPS?
- Reverse-engineer FX bear case.

**Coverage:** 8-12 parent bullets + sub-bullets.

**End:** "Confidence in FX-resilience of thesis: high plausibility / medium plausibility / low plausibility — verbal verdict only, ≤30w, NOT a grade."

---

## AGGREGATE BLOCKS

### Weak Signals (❌) — 0-5 bullets, peer-anchored.

**Example:** `❌ FX-driven growth: 4.2% L3Y average revenue growth from FX vs peer median 0.8% — top-decile FX-flattering of EPS in sector. [Cross-ref: §1 + §3]`

### Outliers (⚡) — 0-3 bullets sparse-by-design.

**Example:** `⚡ RARE: Hedging discipline: 95% of net transaction exposure hedged with 18M horizon — top-decile of European industrials. [Cross-ref: §5]`

---

## QC AUDIT PANEL (validator-filled)

Standard v2.1 panel + Q17-specific tables. **5L + 5M SKIP** ([C]-only).

```
| Gate | Check | Type | Result |
|---|---|---|---|
| 5A-5K | Standard v2.1 gates | Hard / Warn | as applicable |
| **5L** | **SKIP — Q17 [C]-only** | n/a | n/a |
| **5M** | **SKIP — Q17 [C]-only** | n/a | n/a |
| Q17-RT | Revenue-by-currency table (§1) | Hard | ✓ / ✗ |
| Q17-CT | Cost-by-currency table (§2) | Hard | ✓ / ✗ |
| Q17-ST | FX sensitivity table (§6) | Hard | ✓ / ✗ |
```

---

## QC COMMENTARY

After the validator-filled QC Audit panel above, RESEARCHER writes 4-5 free-flowing bullets summarising what the structured numbers say. **Counter-hypothesis check is mandatory** per D-RSR-33.

```
### QC Commentary

- **Net QC verdict:** {≤30w}
- **Warning context:** {≤30w}
- **Source breadth note:** {≤30w on [C]/WebSearch source breadth — 10-K FX disclosures, geographic revenue tables, hedging policy disclosures; no SS / expert call (Q17 [C]-only)}
- **FX exposure quantification edge case:** {≤30w on any nuance — incomplete disclosure, currency mix shift, hedge break scenario}
- **Counter-hypothesis check (AI-Dunning-Kruger):** {≤40w stating: leading view on FX risk + counter-hypothesis (e.g. apparent low FX risk reflects translation-only and ignores transaction exposure mid-shock) + ONE piece of disconfirming evidence that, if true, would invalidate the leading view. If you can't surface a counter-hypothesis, the memo isn't done — return to stewing.}
```

---

## SOURCE-SPECIFIC EXECUTION — [C] only (NO [AS] VERSION)

[C]-only. Q17 uses public filings — segment / geographic revenue tables, FX disclosure sections in 10-K / annual report, hedging policy sections, management's own sensitivity tables where provided.

**Data sources:** 10-K + annual report + 20-F (foreign-issuer filings) FX disclosure + geographic / segment revenue tables + hedging policy + sensitivity tables (often appendix); Bloomberg / Reuters consensus FX outlook for N12-24M; peer 10-Ks for comparison.

**Execution:** WebSearch for `"{COMPANY} FX exposure"`, `"{COMPANY} 10-K geographic"`, `"{COMPANY} hedging policy"`, `"{COMPANY} foreign currency"`, `"{INDUSTRY} FX sensitivity"`. Notion post with `[C]` tag.

> **Legacy note:** This query originated as a ChatGPT-prompt template (REFV01CGPT). Functional but flagged for future rewrite. v2.1 refactor preserves analytical scaffolding while applying format-aware envelope.

---

## VALIDATION GATES

Standard v2.1 gates apply EXCEPT 5L + 5M (skip per [C]-only). Q17-RT + Q17-CT + Q17-ST tables mandatory. Standard 5A-5K.

---

## QUALITY CHECKLIST

Standard v2.1 + Q17-specific:
- [ ] 9 sections present, each with J-front verdict + sceptical bullet.
- [ ] Mandatory revenue-by-currency table (§1).
- [ ] Mandatory cost-by-currency table (§2).
- [ ] Mandatory FX sensitivity table (§6) — at minimum ±5/10/20% for major currencies.
- [ ] Translation vs transaction exposure separated and quantified.
- [ ] Hedging policy + effectiveness L3Y.
- [ ] Peer FX exposure comparison.
- [ ] N12-24M macro FX outlook.
- [ ] FX-as-tailwind-or-headwind synthesis vs thesis.
- [ ] 5L + 5M SKIP confirmed.
- [ ] Verbal FX-resilience verdict.

---

## NOTION POSTING + EXECUTION

Title: `[W] {TICKER} — FX Exposure [C] @ DD-Mon-YY`. Tags: `#DD #FXExposure #Pillar3 #HiddenEarningsDriver`. [C]-only.

---

*End of Q17 DD FX Exposure — AFTER v1 (v2.1 pattern, [C]-only, 5L/5M SKIP, mandatory Q17-RT + Q17-CT + Q17-ST tables). Awaiting Richard's BATCH 4a review.*
