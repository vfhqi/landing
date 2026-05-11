---
name: AlphaSense URL Registry
description: Persistent log of every AlphaSense query URL — enables direct navigation for extraction without sidebar scrolling. 30-day TTL.
type: reference
---

# AlphaSense URL Registry

## Protocol
- **Capture timing:** Watson records the thread URL immediately after submitting any AlphaSense query (from browser address bar once the thread loads).
- **Manual backfill:** If Richard submits queries outside a Watson session, he pastes URLs into this file or tells Watson to add them.
- **Cleanup:** At each session start, Watson deletes rows where `Date Submitted` is >30 days old.
- **Usage:** When extracting a report, Watson navigates directly to the URL rather than scrolling the AS sidebar.
- **Mode:** ALL AlphaSense queries MUST be submitted in Deep Research mode. No exceptions.

## Registry

| Ticker(s) | Report Type | URL | Date Submitted | Date Extracted | Status |
|---|---|---|---|---|---|
| ATS | BD | — | 2026-04-03 | 2026-04-03 | Posted to Notion |
| ATS | CF | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| KIT | BD | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| KIT | CF | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| ERIC | BD | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| ERIC | CF | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| YSN | BD | — | 2026-04-03 | 2026-04-04 | Posted to Notion |
| YSN | CF | `https://research.alpha-sense.com/gensearch/409385__1775166843449` | 2026-04-03 | 2026-04-04 | Posted to Notion |
| PANDOX | BD | `https://research.alpha-sense.com/gensearch/409385__1775167239340` | 2026-04-03 | 2026-04-04 | Posted to Notion |
| PANDOX | CF | `https://research.alpha-sense.com/gensearch/409385__1775167693560` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| INVE.B+peers | BD | `https://research.alpha-sense.com/gensearch/409385__1775168086493` | 2026-04-03 | 2026-04-04 | Posted to Notion |
| INVE.B+peers | CF | `https://research.alpha-sense.com/gensearch/409385__1775168588576` | 2026-04-03 | 2026-04-04 | Posted to Notion |
| JEN | BD | `https://research.alpha-sense.com/gensearch/409385__1775169483145` | 2026-04-03 | 2026-04-04 | Posted to Notion |
| JEN | CF | `https://research.alpha-sense.com/gensearch/409385__1775169709474` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| AIXA | BD | `https://research.alpha-sense.com/gensearch/409385__1775169944443` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| AIXA | CF | `https://research.alpha-sense.com/gensearch/409385__1775170186357` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| Nokia+ADVA | BD | `https://research.alpha-sense.com/gensearch/409385__1775170447605` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| Nokia+ADVA | CF | `https://research.alpha-sense.com/gensearch/409385__1775170898946` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| Nordic+Barco+Shelly | BD | `https://research.alpha-sense.com/gensearch/409385__1775171344607` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| Nordic+Barco+Shelly | CF | `https://research.alpha-sense.com/gensearch/409385__1775171494684` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| HMS+Invisio+Cicor | BD | `https://research.alpha-sense.com/gensearch/409385__1775171052847` | 2026-04-03 | 2026-04-05 | Posted to Notion |
| HMS+Invisio+Cicor | CF | `https://research.alpha-sense.com/gensearch/409385__1775171195552` | 2026-04-03 | 2026-04-05 | Posted to Notion |
