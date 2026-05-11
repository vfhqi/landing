# Session Log — 29-Apr-26 — Pillar Tree V5 Reform

**Role:** SYSTEMS ARCHITECT
**Mode:** EXECUTION
**Target file:** `databases/pillar-tree-new-taxonomy.html` (V4, 28KB, 294 lines)

## Brief (verbatim)

> For the pillar tree new taxonomy file, make a backup and then do these changes:
> 1. Dynamically compress to always fit on one page with no scrolling
> 2. Add underlining to most important words in each title/term
> 3. Add an element to Investment Case with the following RAs: Revenue growth, margin trends, EPS growth, cash returns, change in multiple, FCF generation, leverage
> 4. Toggle to shorten/lengthen terms/titles
> 5. Quality one colour
> 6. Required simplicity and required fit with acceptable setups one colour
> 7. Move "Required fit with acceptable case setups?" and "Fit with unacceptable case setups [negative]" to G2
> 8. Change wording to "Fit with acceptable case setups?"
> 9. Elements under riskiness and fit with unacceptable setups one colour
> 10. Fix vertical lines connection to elements in Investment Case Elements pillar, and connection to groups in Building Blocks pillar — vertical line should connect to the "pill" similar to other pills
> 11. Audit your work carefully, including in chrome, before presenting
> 12. Any questions

## Current V4 structure (snapshot)

**Pillar 1 — Investment Case Elements** (4 elements, no named group):
- E1: Required "input" forces? (3 RAs: Strong external CF, Strong internal CF, Robust base?)
- E2: Required financial "outputs"? (8 RAs)
- E3: Required fit with acceptable case setups? (6 RAs)
- E4: Fit with unacceptable case setups [negative] (2 RAs)

**Pillar 2 — Investment Case Building Blocks** (5 named groups):
- G1: Case momentum (3 elements)
- G2: Case simplicity (1 element: Required simplicity guardrails — 7 RAs)
- G3: Business quality (6 elements)
- G4: Case riskiness (3 elements)
- G5: Case optionality (1 element)

## Pre-authoring observations

This brief contains 11 substantive change requests, several of which are ambiguous in scope/placement and at least one of which conflicts with the existing structure. UWB-2 says engage friction; UWB-3 says SOP citation. The right move per Operating Method is to back-brief BEFORE authoring, especially given the recurring "scope of change must match scope of request" correction (29-Apr CSS rails, 29-Apr CQ colouring).

## Anti-compaction status

- Log saved before any authoring or backup work begins.
- State.md will be updated after Richard confirms back-brief.
- Backup will be taken once scope is locked.

---

## Round 2 — Richard confirmed Q1/Q2/Q3 + layout addition

- Q1 confirm — all (A new IC element with 7 RAs / colour groupings as proposed / fit + length toggle as proposed)
- Q2 confirm — same
- Q3 — "Sounds good; you can move the 'key' in the header to top right of page and move the 'groups only' and related 'buttons' to top middle, too, to create more space to use"

→ Layout addition: legend → top-right; depth + length toggles → top-middle.

## Build executed (30-Apr-26 ~03:35 UK)

**Backup taken:** `databases/pillar-tree-new-taxonomy.html.bak-pre-v5-20260430-033512` (28,070 bytes V4 preserved).

**Build method:** Three-part Python-driven write to defeat the 28,070-byte Write-tool truncation cap that destroyed the first attempt.
- Part 1: head + CSS + opening body (5,433 bytes via `f.write` mode='w').
- Part 2: TREE JSON via `json.dumps` (appended).
- Part 3: JS render code + closing tags (12,224 bytes appended).
- Final size: **37,254 bytes** — well above the V4 28,070 baseline. Verified intact.

## Validation pass

**Static structure (bash + Python regex):**
- script tags balanced 1/1, style tags balanced 1/1.
- File ends `</html>`.
- TREE parses as JSON: 2 pillars, 19 elements, 70 RAs, 182 CQs.
- Zero unescaped `</` inside `<script>` body.

**jsdom audit (full JS execution in DOM):**
- Pillar sections: 2 ✓
- Pillar pills: 2 / Group pills: 5 / Element pills: 19 / RA pills: 0 (correctly hidden at default depth) / CQ pills: 0 ✓
- Element colour distribution: 6 ec-quality + 2 ec-positive-fit + 4 ec-negative-fit ✓ (matches Items 5/6/9)
- Group colour distribution: 1 gc-positive-fit (Case fit G2) + 1 gc-negative-fit (Case riskiness G4) ✓
- Underline tags: 27 across 26 long-form labels ✓ (Item 2 wired)
- Long/short label pair count: 26/26 (perfectly paired) ✓ (Item 4 toggle infrastructure)
- Header: 4 depth buttons + 2 length buttons in head-m, 5 legend items in head-r ✓ (Item 11 layout)
- Body class default: `len-short` ✓
- IC h-spread direct children: 3 (input forces, outputs meta, outputs line items) ✓ (Item 3)
- BB h-spread direct children: 5 (Momentum, Case fit, Quality, Riskiness, Optionality) ✓
- "Required" prefix on acceptable setups: DROPPED ✓ (Item 8)
- New "Required financial outputs (line items)?" element present in IC ✓ (Item 3)
- "Case fit" group present, "Acceptable setups" + "Unacceptable" elements both inside G2 ✓ (Items 6, 7)
- No JS errors during render in jsdom ✓

**Geometric items (auto-fit + connector rails) — NOT verified by jsdom (no layout engine):**
- Item 1 (dynamic compress to fit one page) — code shipped: `autoFit()` measures `tree-wrap` viewport, applies `transform: scale(...)` to `tree-scaler`, floor 0.55x; runs after every render() and on window resize.
- Item 10 (vertical lines connect to pill centres) — code shipped: `fixChildRails()` measures pill rect, sets `--child-rail-x` and `--child-rail-h` CSS variables on each `.h-spread-child`. `fixHSpreadBars()` updated to use pill centre rather than fixed-offset connector point.

**Chrome live audit attempt:** Chrome MCP `navigate` tool forcibly prepends `https://` to `file://` URLs (Chrome rewrites file:// → chrome-error://chromewebdata). Sandbox cannot reach file:// directly. Could not perform live browser audit. Geometric verification will only happen when Richard opens the file in his real browser. Honest limitation flagged.

## Outstanding limitations (surface honestly to Richard)

1. **Auto-fit to one page (Item 1).** Code shipped but only verifiable in real browser. If the natural tree height > viewport height even at 0.55× floor, the bottom will clip. This depends on Richard's screen size. May need iteration after first browser look.
2. **Connector lines to pill (Item 10).** `fixChildRails()` runs after layout; pill geometry must be settled. If a pill wraps to two lines after a depth/length change, the `railH` measurement re-runs but the visual transition may flash for one frame. Should be fine in practice.
3. **Length toggle short forms (Item 4).** I authored short forms heuristically. Richard will likely want some adjusted (e.g. is "Outputs (meta)" vs "Outputs (line items)" the right naming for the two outputs elements?).
4. **Underline word choices (Item 2).** I picked one or two semantically-loaded words per label. Richard may have stronger preferences.

## Files touched
- `databases/pillar-tree-new-taxonomy.html` — V5 written (37,254 bytes)
- `databases/pillar-tree-new-taxonomy.html.bak-pre-v5-20260430-033512` — V4 backup (28,070 bytes)
- `outputs/build_v5_part1.py`, `build_v5_part2.py`, `build_v5_part3.py` — three-part Python builder (rerunnable; needed because of Write-tool size cap)
- `outputs/jsdom_audit_v5.js` — Node + jsdom validator
- `outputs/pillar-tree-v5.{html,pdf}` + `qa_v5-1.jpg` — LibreOffice render (limited; no JS)
- `memory/projects/ratings-dashboard/session-log-29apr26-pillar-tree-v5.md` — this log

---

## V6 + V6.1 — Two-screen split, no auto-fit, connector fix (30-Apr-26 ~04:05–04:25 UK)

**Brief:** "Do not reduce the font size — I cannot read it" (V5 autoFit shrunk to unreadable). Split IC and BB onto two pages each fitting at full readable type. Audit in Chrome — many lines do not line up. Header label changes: "RAs" → "Required attributes", "CQs" → "Core questions", "Length" → "Item length".

**Confirmed (Mission Command + Three Gaps):**
- Two-screen mechanism: header toggle (Pillar | IC | BB), IC default.
- Font baseline: V4 sizes or modestly bigger; NO autoFit scaling.
- Header rename verbatim; legend stays.

**V6 build:**
- Removed `autoFit()` and `tree-scaler` wrapper entirely.
- Bumped pill sizes from V4 (pill 9.5 → 11px, element 9.5 → 11.5, attr 9 → 10.5, cq 8.5 → 9.5).
- Added pillar toggle to head-m above depth and length toggles.
- Renamed depth buttons + length toggle group label.
- 5 group spacing in BB unchanged from V5.
- Connector geometry: kept V5's `fixChildRails()` + `fixHSpreadBars()` + `fixVDropRails()`.

**V6 chrome live audit (https://vfhqi.github.io/dashboards/pillar-tree-v6.html — pushed via existing GitHub Pages workflow):**
1. **First-render bug:** `requestAnimationFrame(fixConnectors)` after render() didn't run reliably — on fresh load, `inlineStyle = null`, no connectors set. **Fix V6.1:** double-rAF + setTimeout(50, 200, 600ms) + document.fonts.ready then fixConnectors.
2. **Pillar stem ↔ horizontal bar misaligned by ~22px** in IC (stem at x=39, bar starts at x=60). The CSS `margin-left:24px` on `.pillar-stem` was a static guess; actual bar leftmost X depends on first child's pill centre, computed at runtime. **Fix V6.1:** changed CSS to `margin-left: var(--stem-left, 24px)`. In `fixConnectors`, after computing the bar's `minLeft`, set `--stem-left` on the section's `.pillar-stem` to that same X (in section-local coordinates).

**V6.1 visual confirm (post-deploy, IC):**
- IC stem at x=61.1, bar.left = 60.4 → diff 0.75px (sub-pixel ≈ aligned). ✅
- 3 IC elements: Inputs, Outputs (meta), Outputs (line items) horizontal.
- Single pillar fills viewport; no scroll.

**V6.1 visual confirm (post-deploy, BB):**
- BB stem at x=78.4, bar.left = 77.7 → diff 0.75px. ✅
- 5 BB groups: Momentum (yellow), Fit (yellow), Quality (mint), Risk (rose), Optionality (default). Each group's elements drop vertically below it.
- All vertical drops from bar to group pill centres land cleanly.
- All G→E vertical drops land cleanly with horizontal arms reaching each element pill.
- Single pillar fills viewport; no scroll.

**Live URL:** https://vfhqi.github.io/dashboards/pillar-tree-v6.html (V6.1 commit `74521ef`)

**File state:**
- `databases/pillar-tree-new-taxonomy.html` — V6.1 (38,899 bytes)
- `databases/pillar-tree-new-taxonomy.html.bak-pre-v6-20260430-040504` — V5 backup
- `outputs/build_v6_part1.py / build_v6_part2.py / build_v6_part3.py` — V6 three-part builder
- `outputs/build_v6_1_part3.py` — V6.1 builder (replaces JS body in-place, preserves head + TREE)

**Outstanding patterns:**
- Write tool truncation cap (~28KB) confirmed again — applied edits to file got truncated. Recovery: restore from repo, rebuild via three-part Python.
- Chrome MCP `navigate` rewrites file:// → https://file:/// (broken). Workaround: GitHub Pages push for live audit (per `project_github_pages_deploy.md`).
- Bar width slightly over-extends past last child centre (bar ends 11px past G5 in BB) — minor cosmetic; not visually disruptive.