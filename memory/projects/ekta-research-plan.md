# EKTA Research Execution Plan
## AS/Claude Research SOP — IG through ESA Phase 1
**Created:** 15-Apr-26 | **Scheduled execution:** 16-Apr-26 05:00 UK

---

## Stock
- **Name:** Elekta
- **Ticker:** EKTA.B-SE (FactSet) / EKTA-B.ST (yfinance)
- **Stage at launch:** [?] Triaging → [?] ESA (update as queries post)
- **Peers:** Siemens Healthineers, IBA, ViewRay, RaySearch, Philips, GE HealthCare (Varian = now Siemens Healthineers)

---

## Decisions confirmed (15-Apr-26)

| # | Decision |
|---|----------|
| Q1 | #10 Short Sellers — **KEEP/REUSE** Feb-26 reports. Count as done. |
| Q2 | #1 BD + #2 Change Forces — **REDO** standalone under new naming convention |
| Q3 | AS wave — **one wave, 05:00 UK onwards** (all submissions together) |
| Q4 | Stop at #13. APM gate before #14. |
| Q5 | Peers confirmed: Siemens Healthineers, IBA, ViewRay, RaySearch, Philips, GE HealthCare |
| Q6 | Watson to update EKTA stage in Stocks DB (Triaging → ESA as queries post) |

---

## Query execution plan

### SKIPPED (already done)
| # | Query | Evidence |
|---|-------|---------|
| #3 | IG — Technical Momentum [C] | `[+] EKTA - Positive technical and negative SS momentum (Elekta) @ 14-Apr-26` — valid, posted correctly |
| #10 | ESA — Short Sellers [AS+C] | `[W] Elekta Short Report [Claude] 11-Feb-26` + `[W] Elekta Short Report [AS] 11-Feb-26` — reused |

### TO EXECUTE (05:00 UK, 16-Apr-26)

| # | Query | Source | Stage | AS prompt file |
|---|-------|--------|-------|---------------|
| #1 | IG — Business Description | AS only | IG | 01-ig-bd.md |
| #2 | IG — Change Forces | AS + C dual | IG | 02-ig-cf.md |
| #4 | Triaging — Earnings Trends | AS + C dual | Triaging | 04-triaging-earnings-trends.md |
| #5 | Triaging — Earnings Delivery LTM | AS + C dual | Triaging | 05-triaging-earnings-delivery.md |
| #6 | Triaging — SS Commentary | AS only | Triaging | 06-triaging-ss-commentary.md |
| #7 | Triaging — KD Assessment | AS + C dual | Triaging | 07-triaging-kd-assessment.md |
| #8 | ESA — BM & Sector Primer | AS + C dual | ESA | 08-esa-bm-sector-primer.md |
| #9 | ESA — Earnings History L3Y | AS only | ESA | 09-esa-earnings-history.md |
| #11 | ESA — Value Chain Map | C only | ESA | 11-esa-value-chain-map.md |
| #12 | ESA — Value Chain Analysis | AS only | ESA | 12-esa-value-chain-analysis.md |
| #13 | ESA — Guidance & Tracking | AS only | ESA | 13-esa-guidance-tracking.md |

**Total AS submissions:** 8 (#1, #2, #4, #5, #6, #7, #8, #9, #12, #13 minus #6 AS-only = 9 AS queries)
Wait: #1=AS, #2=AS+C, #4=AS+C, #5=AS+C, #6=AS, #7=AS+C, #8=AS+C, #9=AS, #12=AS, #13=AS → **9 AS submissions**
All within single wave (≤10 limit). [C] sub-agents run in parallel simultaneously.

**#14 (ESA KD Assessment Phase 2):** Held pending APM interlude. Richard gates this.

---

## Execution sequence at 05:00

1. Submit all 9 AS queries to AlphaSense (Haiku, Deep Research mode) — one wave
2. Dispatch all [C] sub-agents simultaneously (##2, 4, 5, 7, 8, 11)
3. Wait 45+ min for AS generation
4. [C] returns will come in during wait — save to COWORK/Files/ immediately on return
5. Extract AS results, clean via process_report.py pipeline
6. Merge dual-source queries (##2, 4, 5, 7, 8) per SOP backbone rules
7. Post all to Notion Stock Notes DB — new naming convention
8. Update EKTA Stocks DB: stage → [?] ESA once #8-13 posted
9. Hand to APM with summary note

---

## Notion naming convention (V2, from 13-Apr-26)

`[W] EKTA (Elekta) — {Stage} — {Description} [{SOURCE}] @ DD-Mon-YY`

Examples:
- `[W] EKTA (Elekta) — IG — Business Description [AS] @ 16-Apr-26`
- `[W] EKTA (Elekta) — IG — Change Forces [C+AS] @ 16-Apr-26`
- `[W] EKTA (Elekta) — Triaging — Earnings Trends [C+AS] @ 16-Apr-26`
- `[W] EKTA (Elekta) — Triaging — SS Commentary [AS] @ 16-Apr-26`
- `[W] EKTA (Elekta) — ESA — BM & Sector Primer [C+AS] @ 16-Apr-26`

---

## File save locations (auto-save before posting)

| Query | File |
|-------|------|
| #1 [AS] | COWORK/Files/EKTA-ig-bd-AS.md |
| #2 [C] | COWORK/Files/EKTA-ig-cf-C.md |
| #2 [AS] | COWORK/Files/EKTA-ig-cf-AS.md |
| #4 [C] | COWORK/Files/EKTA-triaging-earnings-trends-C.md |
| #4 [AS] | COWORK/Files/EKTA-triaging-earnings-trends-AS.md |
| #5 [C] | COWORK/Files/EKTA-triaging-earnings-delivery-C.md |
| #5 [AS] | COWORK/Files/EKTA-triaging-earnings-delivery-AS.md |
| #6 [AS] | COWORK/Files/EKTA-triaging-ss-commentary-AS.md |
| #7 [C] | COWORK/Files/EKTA-triaging-kd-assessment-C.md |
| #7 [AS] | COWORK/Files/EKTA-triaging-kd-assessment-AS.md |
| #8 [C] | COWORK/Files/EKTA-esa-bm-primer-C.md |
| #8 [AS] | COWORK/Files/EKTA-esa-bm-primer-AS.md |
| #9 [AS] | COWORK/Files/EKTA-esa-earnings-history-AS.md |
| #11 [C] | COWORK/Files/EKTA-esa-value-chain-map-C.md |
| #12 [AS] | COWORK/Files/EKTA-esa-value-chain-analysis-AS.md |
| #13 [AS] | COWORK/Files/EKTA-esa-guidance-tracking-AS.md |

---

## Handoff trigger
On completion, Watson posts a summary note to Notion Tasks DB and updates this file with status.
APM to be invoked by Richard for Analysis + Judgement interlude before #14.

---

## AS Submission URLs (16-Apr-26)

| # | Query | URL |
|---|-------|-----|
| #1 | IG — Business Description [AS] | https://research.alpha-sense.com/gensearch/409385__1776316001832 |
| #2 | IG — Change Forces [AS] | https://research.alpha-sense.com/gensearch/409385__1776316132658 |
| #4 | Triaging — Earnings Trends [AS] | https://research.alpha-sense.com/gensearch/409385__1776316234517 |
| #5 | Triaging — Earnings Delivery LTM [AS] | https://research.alpha-sense.com/gensearch/409385__1776316332707 |
| #6 | Triaging — SS Commentary [AS] | https://research.alpha-sense.com/gensearch/409385__1776316461145 |
| #7 | Triaging — KD Assessment [AS] | https://research.alpha-sense.com/gensearch/409385__1776316704247 |
| #8 | ESA — BM & Sector Primer [AS] | https://research.alpha-sense.com/gensearch/409385__1776316836686 |
| #9 | ESA — Earnings History L3Y [AS] | https://research.alpha-sense.com/gensearch/409385__1776316957992 |
| #12 | ESA — Value Chain Analysis [AS] | https://research.alpha-sense.com/gensearch/409385__1776317270307 |
| #13 | ESA — Guidance & Tracking [AS] | https://research.alpha-sense.com/gensearch/409385__1776317348758 |

---

## Status
- [x] AS wave submitted (10 queries, 16-Apr-26)
- [x] [C] agents dispatched (16-Apr-26)
- [x] [C] agents returned (16-Apr-26) — all 6 [C] outputs saved to COWORK/Files/
- [x] AS results extracted (16-Apr-26) — all 10 AS PDFs downloaded and extracted
- [x] All pages posted to Notion (16-Apr-26) — 16 pages total (see Notion URLs below)
- [x] EKTA Stocks DB updated → ESA (16-Apr-26)
- [ ] APM gate triggered — READY. Richard to invoke APM for #14 (ESA KD Assessment Phase 2)

## Notion Pages Posted (16-Apr-26)
| # | Title | URL |
|---|-------|-----|
| #1 [AS] | IG — Business Description | https://www.notion.so/31435e909b0b8188a53dece4de0c6b7a |
| #2 [AS] | IG — Change Forces | https://www.notion.so/31435e909b0b81f09df2e8bd01a76abc |
| #2 [C] | IG — Change Forces | (posted) |
| #4 [C] | Triaging — Earnings Trends | (posted) |
| #4 [AS] | Triaging — Earnings Trends | (posted) |
| #5 [C] | Triaging — Earnings Delivery LTM | (posted) |
| #5 [AS] | Triaging — Earnings Delivery LTM | (posted) |
| #6 [AS] | Triaging — SS Commentary | (posted) |
| #7 [C] | Triaging — KD Assessment | (posted) |
| #7 [AS] | Triaging — KD Assessment | (posted) |
| #8 [C] | ESA — BM & Sector Primer | (posted) |
| #8 [AS] | ESA — BM & Sector Primer | (posted) |
| #9 [AS] | ESA — Earnings History L3Y | https://www.notion.so/34435e909b0b81f7b108d3cdc0b167ce |
| #11 [C] | ESA — Value Chain Map | (posted) |
| #12 [AS] | ESA — Value Chain Analysis | https://www.notion.so/34435e909b0b81f1ae98fa495b46e764 |
| #13 [AS] | ESA — Guidance & Tracking | (posted) |
