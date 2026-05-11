# Memo Header Design System V5
<!-- [W] Created 21-Apr-26. Durable spec. Live across all memos, all sections A–F. -->

## TL;DR

Six-tier strictly-descending typographic hierarchy for memo content on the Ratings Dashboard. Applies to **every memo, every section (A/B/C/D/E/F), every stage (Triaging/ESA/DD)**. Pure CSS — no JS renderer changes. Shipped 21-Apr-26 at 11:03 UK via `databases/scripts/patch-header-hierarchy.py`.

## Design principles (learned the hard way)

1. **Strictly descending size.** Every child tier must be smaller than its parent. Violation: V2 had pillar (P3) at 20.5px below its parent C.II.2 at 17px. Richard immediately caught it: "Why is P3 Business quality bigger than the levels above it." **Never re-break this rule.**
2. **Strictly descending weight** (roughly). Main hierarchy uses 700 across tiers 1–5, then 600 for topic, then 400 body. Exception: the family-vs-topic pair explicitly uses weight-inversion — family 700, topic 600 (Option B). The rationale: family is the **reading unit** (the dominant bucket header); topic is a sub-label within it, so should be lighter.
3. **Monotone case.** Sentence case / title case throughout. **No UPPERCASE anywhere** in headers. V2 had "P3 BUSINESS QUALITY" (uppercase) below lowercase C.II.2 and Richard rejected: "I dont like UPPER CASE nested below lower case - please change that. It confuses me."
4. **ID badges sized to match their parent label.** If the parent label is 18px, the ID badge should be ~15–16px (one step down, not four). Earlier drafts had IDs 4px smaller than their labels causing typographic mismatch. Richard: "C.II.2 seems smaller than the title 'Fundamental Investment Case (P3+P4)'."
5. **Badge colour ramp tracks hierarchy depth.** Deep navy at the top → mid blue → light blue inverted → pale grey → very pale grey. Visual depth mirrors semantic depth.
6. **Family > Topic in visual weight** (Option B). Family is the dominant bucket; topic is evidence *within* the family. Without this inversion, topics look more important than their containing families, which is wrong.
7. **Badges at every nested level, not just family.** Richard initially liked the family grey pill and asked: "Can we keep the badges, but make bigger. Can we add badges to higher levels?" Answer: yes, cascade the badge idea through all tiers with a colour ramp that signals depth.
8. **Memos ≠ data tables.** This system applies to memo content only. Data tables use a different typographic register (dense scanning surfaces vs prose-with-hierarchy). Richard asked whether to push V5 across the whole dashboard; answer was NO for this reason.

## The ramp

| Tier | Element | Font-size | Weight | Badge bg | Badge text | Badge size |
|------|---------|-----------|--------|----------|------------|-----------|
| 1 | `.memo-h1` (memo title) | 28px | 700 | — (no badge) | — | — |
| 2 | `.memo-section-title` (A–F) | 22px | 700 | `#1a365d` deep navy | `#fff` | 20px |
| 3 | `.memo-subsection-header` (e.g. C.II) | 18px | 700 | `#2c5282` mid blue | `#fff` | 15px |
| 4 | `.memo-pillar-label` (e.g. P3 Business Quality) | 15.5px | 700 | `#dde7f5` light blue | `#1a365d` navy | 13px |
| 5 | `.memo-family-label` (e.g. IC#2 Competitive Moats) | 14px | 700 | `#f0f0f0` pale grey | `#4a4a4a` | 12px |
| 6 | `.memo-topic-header` (e.g. 2.a Switching Costs) | 13px | 600 | `#f7f7f7` very pale | `#6b6b6b` | 11px |
| 6a | `.memo-subtopic-header` | 13px | 500 italic | — | — | — |
| body | `.memo-prose`, `.memo-para` | 13px | 400 | — | — | — |

Line-heights ramp from 1.2 (h1) to 1.55 (body). Badges use `inline-flex` with `border-radius: 4px` (3px for topic tier). Section header also has `border-bottom: 2px solid #1a1a1a` rule. Pillar header has `border-left: 3px solid #c8c8c8` accent bar.

## Required DOM shape

The JS renderers must emit these span classes (they already do — no changes needed):

- Section: `<h2 class="memo-section-title">` with sibling `<span class="memo-letter-badge">A</span>` inside `<div class="memo-section-header">`
- Subsection: `<h3 class="memo-subsection-header">` containing `<span class="memo-subsection-id">C.II</span>` + title text
- Pillar: `<div class="memo-pillar-header">` containing `<span class="memo-pillar-id">P3</span>` + `<span class="memo-pillar-label">Business Quality</span>`
- Family: `<div class="memo-family-header">` containing `<span class="memo-family-badge">IC#2</span>` + `<span class="memo-family-label">Competitive Moats</span>`
- Topic: `<h4 class="memo-topic-header">` containing `<span class="memo-topic-id">2.a</span>` + title text
- Subtopic: `<h5 class="memo-subtopic-header">`

Suppression rule (from v3.1 spec, still valid): single-pillar subsections (C.II.1/3/4/5) suppress the separate pillar header because the subsection header already names the pillar. Only C.II.2 shows pillars explicitly because it contains P3+P4.

## The patcher

- Path: `databases/scripts/patch-header-hierarchy.py`
- Idempotent via markers `/* HEADER_HIERARCHY_CSS_START */` … `/* HEADER_HIERARCHY_CSS_END */` — re-runs replace in place.
- Takes snapshot backup to `memory/projects/ratings-dashboard/snapshots/{YYYY-MM-DD-HHMM}-pre-v5-badges/` before writing.
- Runs 14 validation checks after write (markers present, balanced tags, no `var PB`, renderer functions intact, etc.). Fails loudly and points at backup if any check fails.
- Uses `!important` on every declaration because the existing dashboard has many high-specificity rules.

## Evolution history (why V5 exists)

V1 (24/19/16/14.5/13.5/13) → too tight, Richard asked to loosen.
V2 (pillar = section Tier 2) → violated descending rule AND mixed uppercase.
V3 (26/20.5/17/15/13.5/13 strict descent) → family lighter than topic (wrong).
V4 (28/22/18/15.5/14/13 + Option B weights) → ID labels mismatched parent labels.
**V5** → full badge system, IDs matched, colour ramp. Approved.

## What to do if Richard asks for another iteration

1. Read this file first.
2. Do NOT violate the "strictly descending" rule unless Richard explicitly authorises it.
3. Build a mockup in `memory/projects/ratings-dashboard/mockups/header-ramp-v{N}.html` with a density test (C.II.2 × 2 pillars × 2 families × 3 topics minimum) before touching the live dashboard.
4. Only after Richard approves, update `patch-header-hierarchy.py` and run it. The markers ensure safe replacement.
5. Snapshot pre and post. Report all 14 validation checks.

## What to do if this needs to be ripped out

The marker-wrapped block can be regex-deleted from `databases/ic-ratings-dashboard-v2.html` cleanly. Or restore from `snapshots/2026-04-21-1103-pre-v5-badges/ic-ratings-dashboard-v2.html`.
