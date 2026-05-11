# IR Role Notes — LP Communications Memo (UBS AMC migration)
## 2026-05-05

This is a role-notes record for an IR-flavoured workstream that sits OUTSIDE the existing IR Two-Pager SKILL (which is for institutional-PM-audience two-pager investment memos on stocks). This work is **LP communications** — explaining a structural change to existing investors. Filed here as the closest existing skill folder; flag for SA review whether a separate IR-LP-Communications SKILL should be split out.

---

## What was produced

Two LP memos for Viewforth investors explaining the move from the existing Cayman fund to a UBS-issued Actively Managed Certificate (AMC) wrapper:

- **Generalist HNW memo** — 4 pages A4, plain English, structural detail stripped, audience = HNW investors who need clarity not jargon.
- **Sophisticated ex-finance memo** — 4 pages A4, full structural detail (issuer credit risk, no segregation, deleverage trigger, §871(m), termsheet table), audience = ex-finance HNW.

Both shipped as final v4 docx files. Project home: `PROJECTS/EA - UBS AMC/`.

---

## Pattern: when to write two memos, not one

The HNW investor base is mixed. Some are professional-finance backgrounds and want structural detail; some are generalists who need plain English. A single memo for both audiences is a worse compromise than two well-targeted ones. Pattern: if the audience splits on financial sophistication, write the document twice rather than once for the lowest common denominator.

---

## Voice and formatting standard (locked this session — D-AMC-8)

- **Typeface:** Aptos / Aptos SemiBold
- **Colour:** off-black `#2A2A2A` ink, no chromatic colour
- **Layout:** A4 portrait, 2cm margins, 1.25× line spacing, ~480 DXA spacing before headings
- **Inline emphasis:** semi-bold (Aptos SemiBold face), not bold
- **Header bar:** `VIEWFORTH — UBS AMC Information Note` (no segment-specific suffix)
- **Footer:** `Page X of Y`, centre-aligned
- **Sign-off:** `Viewforth — May 2026` in italics (institutional voice, not personal)
- **Endnote section labelled:** `Sources` (not `Endnotes`)
- **Bullets:** ≤50 words each
- **Source line:** Memo A includes upfront line stating information is drawn from UBS materials and public sources, with termsheet provided alongside.

---

## Author voice rule (D-AMC-9)

LP / IR external memos sign off as **Viewforth**, not as Richard personally. Richard appears as the first contact in the Contacts section, not as author. Personal voice is reserved for direct outreach (email follow-ups, calls, individual responses).

---

## Pre-ship fact audit (proposed default gate)

Before shipping any external-document deliverable, run an exhaustive fact audit:

1. Every figure, name, date, ratio cross-checked against the source document.
2. Square-bracketed values in legal/structured-product termsheets (`[Aa2 Moody's / A+ S&P / AA- Fitch]`) treated as **indicative, NOT authoritative**. Do not cite as fact unless cross-verified against an independent source.
3. Self-references / working drafts removed from footnote lists.
4. Time-stamped metrics qualified ("as of May 2025") not implied as current.
5. Editorial extrapolations between named entities flagged ("operating as Viewforth" was Watson's invention, not termsheet wording).
6. Audit produces a flagged-items list with concerns categorised (red = must fix; yellow = consider; blue = observation). Richard signs off on each.

Filed to `wisdom-library/_meta/candidate-queue.md` as Silver-tier candidate `fact-audit-before-shipping-external-doc`. Pattern observed once (this session) but operationally analogous to the Quality Gate (kaizen 2026-05-04).

---

## Audience-specific filtering rules

For the **generalist HNW** version:
- Strip technical wrapper detail: SSPA codes, listing/clearing references, Floor, deleverage trigger, §871(m), VaR specification.
- Plain-English equivalent of trading fees ("when the fund buys or sells stocks for the portfolio") rather than "rebalance fee."
- AMC explained in 3 sentences as "a security like a share or a bond, but tracking a managed portfolio, issued by UBS."
- Comparison section is prose, not a table (tables suggest the reader should compare line-by-line).

For the **sophisticated ex-finance** version:
- Full termsheet table.
- "Three structural points worth holding in mind" frames issuer credit risk, no-segregation, securitised-fungible-transferable.
- "Points worth understanding before you reallocate" enumerates the wrapper-feature trade-offs neutrally — not as warnings, as facts.
- §871(m), §50% deleverage, key-person clauses called out by name.

Both versions:
- Cayman wind-down framed as "as part of the move to AMC" (directional/positive), not "closing" or "running alongside."
- Don't highlight cash-out option for investors who don't want to migrate.
- Section 7 covers the four-route transfer mechanic per Richard's LP draft.
- Section 8 lists Richard first as portfolio/strategy contact.

---

## Files (provenance)

- Source — UBS deck: `Files/Documents/20250520_AMC AMS Deck_WF1850750 HIGHLIGHTS.pdf`
- Source — Termsheet: `Files/NOT BACKED UP/Chrome downloads/Generated_Termsheet_20260430_182029 (1).docx`
- Source — Richard's LP draft notes: `Files/NOT BACKED UP/Chrome downloads/Email draft to LPs.docx`
- Build script: `outputs/build_memos.js` (24.4 KB, near silent-truncation boundary)
- Final deliverables (project): `PROJECTS/EA - UBS AMC/deliverables/Viewforth UBS AMC - {Generalist HNW | Sophisticated Investor} Memo - 2026-05-05 v4.docx`
- Final deliverables (Richard's view): `Files/NOT BACKED UP/Watson downloads/`

---

## SA flag for review

The existing `ir-two-pager` SKILL is for institutional-PM two-pager investment memos on stocks. This LP-communications work is a different deliverable archetype. Recommend:

- Either (a) split a new `lp-communications` SKILL with this file as the seed, or
- (b) extend `ir-two-pager` with a "Mode B: LP Communications" section and rename the skill to `ir`.

Cross-ref `D-AMC-5` through `D-AMC-10` for full decision basis.

---

## Cross-references

- Project: `PROJECTS/EA - UBS AMC/` (state, decisions, corrections, deliverables, transcript)
- Handoff: `PROJECTS/EA - UBS AMC/handoffs/handoff-2026-05-05-1430.md`
- WL candidates: `wisdom-library/_meta/candidate-queue.md` entries dated 05-May-26
- Auto-memory: `feedback_neutral_fact_phrasing.md`
- Existing IR skill: `memory/skills/ir-two-pager/SKILL.md` (different audience / deliverable)
- Comms principles: `memory/skills/communication-principles/SKILL.md`
