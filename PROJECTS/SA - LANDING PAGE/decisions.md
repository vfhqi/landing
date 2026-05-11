# decisions.md — SA - LANDING PAGE

Append-only log of locked decisions. Each entry: ID, date, question, decision, why, blast radius. Never re-ask a locked decision.

---

## D-LP-01 — Project format and storage

**Date:** 2026-05-09
**Question:** Where should the landing page live?
**Decision:** Single self-contained HTML file at `databases/landing-page.html`. Symlink (or copy) to COWORK root as `landing-page.html` for one-click open.
**Why:** Pattern matches existing dashboards (`databases/*.html`); stays inside COWORK perimeter; no build step; portable to GitHub Pages later.
**Blast radius:** None — additive file.
**Locked by:** Watson (pending Richard confirm at back-brief).

## D-LP-02 — Diagram primitive

**Date:** 2026-05-09
**Question:** SVG vs Canvas vs DOM-only?
**Decision:** Inline SVG with `<a xlink:href>` overlays for clicks; HTML/CSS for surrounding chrome (legend, search box, header).
**Why:** SVG is crisp at any zoom, anchors are native + accessible, no JS dependency for the basic navigation, easy to print or screenshot.
**Blast radius:** Constrains future enhancements (live data badges) — but those can be added via SVG `<text>` updates without changing the primitive.
**Locked by:** Watson (pending Richard confirm).

## D-LP-03 — Honour sketch colour palette

**Date:** 2026-05-09
**Question:** Use sketch colours or recolour to match Richard's existing brand-voice palette (Purple/Blue/Green)?
**Decision:** Use the **sketch colours** (yellow/pink/blue/orange/cyan/green/red), because Richard chose them deliberately to disambiguate clusters and Gestalt grouping is load-bearing here. Brand palette (Purple = judgements, Blue = observations, Green = actions) does NOT translate to navigation clusters.
**Why:** The sketch's eight-colour scheme makes 8 clusters scannable in <1 second. Recolouring would delete information.
**Blast radius:** Mild — one-off colour map, doesn't propagate.
**Locked by:** Watson (pending Richard confirm).

## D-LP-04 — SUPERSEDED by D-LP-04-rev (Richard's redraw 09-May-26 PM)

Original 8-cluster spider mapping. Richard redrew the diagram cleaner. Keep this row for audit trail; the live mapping is D-LP-04-rev below.

## D-LP-04-rev — Seven clusters from Richard's redraw (09-May-26)

**Date:** 2026-05-09
**Decision:** Final cluster mapping for v1, taken from Richard's redrawn diagram (image attached to chat 09-May-26 PM).

| Sketch colour | Cluster name | Live destination | Click semantics |
|---------------|--------------|-----------------|-----------------|
| YELLOW (top) | **Strategic Targets** | `memory/context/values-and-behaviours.md` (ETCs); Notion OKRs page; `databases/pullback-watchlist.json` (target-sector lists) | Single click → Notion OKRs page (TBD URL) |
| MAGENTA (top-right) | **Market / Environment / Thematics** | `memory/thematics/active.md`; Notion thematics page; current-regime journal entry | Single click → thematics doc |
| ORANGE-FILL (centre, small) | **Portfolio** (current state) | `positions.json` rendered; portfolio summary view (does not yet exist as a distinct dashboard) | Single click → `position-manager.html` (until a dedicated portfolio view exists) |
| CYAN (centre) | **Position Management System** | `position-manager.html` at COWORK root | Single click → `position-manager.html` |
| BLUE (right) | **Workflow Priorities** | Notion Tasks DB / Kanban board; `memory/projects/pipeline.md`; `PROJECTS/INDEX.md` | Single click → Notion Tasks DB (TBD URL) |
| GREEN (left, big) | **Master (Technical) Dashboard** containing: 8 screen tabs + 2 quant inputs (Valuation in range, Sell-side estimate momentum) | `databases/master-dashboard.html` (build in flight — landing page links to spec page until live) | Per D-LP-08: each screen-tab clickable → opens dashboard at correct tab anchor |
| PINK (bottom-centre) | **Notes Repository** | `databases/ic-ratings-dashboard-v2.html` (qualitative pillars view); per-stock memos in `databases/memos/{TICKER}/` | Single click → `ic-ratings-dashboard-v2.html` |
| ORANGE-OUTLINE (bottom-right) | **Ratings Dashboard** with 4 columns (Timeliness / Knowledge / Interest / Master ratings) | `databases/ic-ratings-dashboard-v2.html` (master ratings view) | Per D-LP-09: single click for whole cluster — columns are NOT separately clickable |

**Substrate (uncircled, bottom-left):** **Stocks Universe Database** — feeds Master Dashboard (up) and Notes Repository (right). Per D-LP-11 rendered as a horizontal "ground" element under the diagram.

**Visible non-clickable element:** **Gap?** marker between Market/Environment cluster and ETCs cluster — per D-LP-12.

**Locked by:** Richard (09-May-26 PM, "Yes, agree with all else. Begin your work.").

## D-LP-05 — Drop hub-and-spoke, adopt directed flow layout

**Date:** 2026-05-09
**Decision:** No central hub. The diagram is a directed flow with arrows showing data/judgement flow direction. Layout follows Richard's redraw: ETCs top-centre, Market/Environment top-right, Portfolio centre, PMS below Portfolio, Workflow right, Master Dashboard left, Notes Repository bottom-centre, Ratings Dashboard bottom-right, Stocks Universe substrate at bottom.
**Why:** Richard's redraw replaced the spider with a flow diagram. Hub-and-spoke was my initial framing; the redraw answered Gap 2 visually and rejected the hub.
**Blast radius:** Visual — every prior layout note was hub-centric. Decisions D-LP-01, D-LP-02, D-LP-03 still hold (file location, SVG primitive, sketch colours).
**Locked by:** Richard.

## D-LP-06 — BLUE cluster repurposed: PINK now hosts "Notes Repository"

**Date:** 2026-05-09
**Decision:** The BLUE cluster name in the original sketch ("Qualitative IC Analysis / IAJA library") is gone. Richard's redraw moves "Notes Repository" to the PINK cluster (bottom-centre), fed by Stocks Universe and feeding the Ratings Dashboard.
**Why:** Richard redrew it that way and confirmed.
**Blast radius:** Cluster naming + click target. Picked up in D-LP-04-rev.
**Locked by:** Richard.

## D-LP-07 — GitHub Pages URL `vfhqi.github.io/landing/` via own repo

**Date:** 2026-05-09
**Decision:** Create new GitHub repo `vfhqi/landing`. File `index.html` at root. Enable GH Pages on `main` branch. Public URL: `https://vfhqi.github.io/landing/`. Local mirror: `databases/landing-page.html` + `landing-page.html` at COWORK root.
**Dual-mode link rewriting:** ~10 lines of inline JS detects `window.location.hostname`. If GH Pages, rewrite local hrefs (e.g. `databases/master-dashboard.html`) to their GH equivalents (e.g. `https://vfhqi.github.io/dashboards/master-dashboard.html`). If `file://` or local, use local hrefs as-is. One source file, two link contexts.
**Why:** Richard's stated wording "/landing" — own repo is the cleanest URL match. Burying inside `dashboards/` would invert the navigation hierarchy (landing IS the parent of the dashboards).
**Blast radius:** New repo to create. Maintenance is one `git push` per update. Mirrors the existing `vfhqi/dashboards` workflow.
**Locked by:** Richard.

## D-LP-08 — Master Dashboard click → opens correct tab

**Date:** 2026-05-09
**Decision:** Each of the **8 screen tabs** rendered inside the GREEN cluster opens `master-dashboard.html` at its corresponding tab via `#tab=<id>` anchor. Sub-elements within the cluster (5 pattern screens + SSEM + Val + Combos = 8) are NOT separately routed beyond the tab — they all land in the Master Dashboard. The 2 quant input boxes (Valuation in range, SSEM) feeding the Master Dashboard ALSO click into the Master Dashboard at their respective tabs (val, ssem).
**Master Dashboard tab IDs (from existing snapshot):** `bp`, `pb`, `mm99`, `vcp`, `utr`, `tech`, `ssem`, `val`, `combos`, `positions`. The 8 screen-flavoured ones for the landing page are: `bp`, `pb`, `mm99`, `vcp`, `utr`, `ssem`, `val`, `combos` (Tech and Positions excluded — Tech is utility, Positions duplicates the CYAN PMS cluster).
**Why:** Richard's instruction: "just go to master dashboard, not separately clickable, but open the respective tab in the master dashboard when clicked. Also, it is 8 screens, not 5."
**Watson interpretation flag:** Watson's reading of "8 screens" = the 8 cluster-feeding tabs above. If Richard meant something different (e.g. an unbuilt 8th screen), flag in v1 feedback.
**Blast radius:** Anchors only. If the Master Dashboard hash router uses a different format (e.g. `#bp` not `#tab=bp`), update the hrefs. Tested in v1 quality gate.
**Locked by:** Richard.

## D-LP-09 — Ratings Dashboard cluster = single click

**Date:** 2026-05-09
**Decision:** The four sub-boxes in the Ratings Dashboard cluster (Timeliness / Knowledge / Interest / Master ratings) are columns Richard plans to build inside one ratings view. They are NOT separately clickable. The whole cluster is one click → `ic-ratings-dashboard-v2.html`.
**Why:** Richard: "not separate views. columns we will build. So just click to ratings dashboard only as one 'click' for this area."
**Locked by:** Richard.

## D-LP-10 — Preserve arrowheads on rendered flow

**Date:** 2026-05-09
**Decision:** Render arrows with arrowheads (SVG `marker-end`) per Richard's redraw. Arrows carry information (data/judgement flow direction); they are not chrome to be tidied away.
**Why:** Richard: "Preserve."
**Implementation:** Inline SVG `<defs><marker id="arrow">...</marker></defs>`; every flow line uses `marker-end="url(#arrow)"`.
**Locked by:** Richard.

## D-LP-11 — Stocks Universe rendered as substrate ground bar

**Date:** 2026-05-09
**Decision:** The "Stocks Universe Database" node (uncircled, bottom-left in Richard's redraw) becomes a horizontal ground element under the whole diagram, communicating that the universe is the substrate everything sits on. Clickable → `databases/pullback-watchlist.json` rendered view (or Notion Stocks DB if URL known).
**Why:** Watson suggestion in back-brief, accepted ("Yes, agree with all else").
**Locked by:** Richard.

## D-LP-12 — Visible "GAP?" marker, non-clickable

**Date:** 2026-05-09
**Decision:** Render the `Gap?` arrow Richard drew between the Market/Environment cluster and the ETCs cluster as a dotted arrow with a "GAP?" label. Non-clickable. It surfaces an unfinished system-architecture question back to Richard's eyeline every time he opens the page.
**Why:** Richard: "Leave the gap visual but not clickable for now."
**Locked by:** Richard.

---

## D-LP-13 — Use full descriptions, not shorthand

**Date:** 2026-05-09 PM
**Decision:** Standing instruction across the landing page (and any future iteration): use full descriptive labels, not abbreviations. "Basing Plateau" not "Basing"; "Mark Minervini 99-Point Screen" not "MM 99"; "Sell-Side Earnings Momentum" not "SSEM"; "Researcher · Assistant Portfolio Manager" not "Res · APM"; "Evergreen Target Conditions" not "ETCs"; "stops, grace clocks, at-risk basis points" not "stops · grace · at-risk bps".
**Why:** Richard: "Use full descriptions here (as space is not an issue) — I find it clearer."
**Blast radius:** Universal across this project. Future-Watson should default to long-form labels in any landing-page edit unless explicitly told otherwise.
**Locked by:** Richard.

## D-LP-14 — One-page fit constraint

**Date:** 2026-05-09 PM
**Decision:** The whole diagram must render without scrolling on a typical 1080p Chrome viewport. SVG `viewBox` is `0 0 1500 760`; chrome (header + legend + footer) ~120px → SVG fills remaining ~860px area via `flex:1 1 auto; height:100%`. `body { overflow:hidden }` to enforce.
**Why:** Richard: "Make it fit on one page."
**Blast radius:** Constrains how much detail any cluster can hold. If a cluster needs more content, prefer denser typography over breaking the one-page rule.
**Locked by:** Richard.

## D-LP-16 — Non-clickable "Other large components" reminder block

**Date:** 2026-05-09 PM
**Decision:** Top-left of the SVG (490×160 area at x=40,y=20), behind a dashed neutral-grey border, render a 12-item reminder list. Items: Wisdom Library / Roles (skills, memory, other) / SOPs / Principles / Frameworks / System architecture / Auditing / Backing up / Coaching · High Performance / Calibration log + corrections / Kaizen lessons / Scheduled protocols. **No clicks, no underline, no anchor affordance** — `pointer-events="none"` on the whole `<g>`. Surfaces large system components to Richard's eyeline as a reminder of what isn't yet on the diagram.
**Why:** Richard: "Add in a section that is not linked nor has hyperlinks (but just a reminder for me ATM)." Watson recommended 4 strong adds beyond Richard's original 8; Richard accepted.
**Blast radius:** Visual real estate in upper-left quadrant only (was empty space). Doesn't affect any flow lines or other clusters.
**Locked by:** Richard.

## D-LP-18 — PAT scope widening (fine-grained, all-repos, Admin/Contents/Pages/Workflows)

**Date:** 2026-05-09 PM
**Question:** Existing PAT scoped only to `vfhqi/dashboards` + `vfhqi/master` with `Contents: R+W`. Cannot create new repos. How to widen?
**Decision:** Stay on fine-grained PAT (consistent with prior choice). Widen to:
- Repository access: **All repositories** under `vfhqi` (replaces "Only select")
- Permissions: **Administration: R+W** (allows repo create/delete), **Contents: R+W** (push), **Pages: R+W** (enable Pages via API), **Workflows: R+W** (future-proof for Actions)
- Token name: `Watson_VFHQI dashboards_push_2026-05-06`, expires 5 May 2027
**Why:** Need repo creation for `vfhqi/landing`. Widening to all-repos (vs adding repos one-by-one) avoids repeating this re-scope every time we add a new repo. Acceptable blast-radius trade-off given the token is fine-grained (single-user namespace, explicit expiry).
**Token file:** Active token now lives at canonical `COWORK/.secrets/github-pat.txt`. Old PAT (`cowork-dashboards`) archived as `.secrets/github-pat-OLD-cowork-dashboards-2026-05-09.txt` with a sidecar `.secrets/README.md` explaining what each file is.
**Verified working:** Test repo create + delete cycle passed via API.
**Blast radius:** Cross-cuts SA - GITHUB SOP. Follow-up brief filed at `PROJECTS/SA - GITHUB SOP/scratch/2026-05-09-landing-followup-brief.md`.
**Locked by:** Richard.

## D-LP-20 — Thematics dashboard (own dashboard, file-system-backed)

**Date:** 2026-05-09 PM
**Decision:** New dashboard at `databases/thematics-dashboard.html`. File structure: `databases/thematics/{slug}/{YYYY-MM-DD}-{title}.{md|docx|html}`. Slugs: `ai`, `iran-oil`, `recession-rollover`. Manifest at `databases/thematics/manifest.json` enumerates all reports per thematic with metadata (date, title, file, summary). Dashboard reads manifest via inline JSON `<script>` tag (no fetch — file:// safe). Each thematic gets its own section: header (name + status + last update) + chronological list of APM reports + small "raw research feeders" subsection where applicable.
**Why:** Pattern matches existing dashboards. Single source of truth. Scalable to N thematics. APM appends to manifest when new report written.
**Locked by:** Richard.

## D-LP-21 — Portfolio OKRs as period-stamped JSON with current pointer

**Date:** 2026-05-09 PM
**Decision:** Storage at `databases/portfolio-okrs/`. Files: `2026-05.json`, `2026-06.json`, ... + `current.json` (or "current": "2026-05" inside an index.json). Schema future-proofed for additional TC types beyond stock count: sector caps, position sizing, geographic concentration, max probing bets, conviction-weighted average — initially as placeholder fields.
**Why:** Period-stamped preserves audit trail of "what we said we wanted" — HPC/APM gold for retrospective analysis. Current pointer makes it cheap for landing page + Watson + future scripts to find the live OKR state.
**Locked by:** Richard.

## D-LP-22 — GAP repositioned + becomes substantive node, not annotation

**Date:** 2026-05-09 PM
**Decision:** GAP node moves from inter-cluster horizontal arrow (between Market/Environment and Strategic Targets) to a **centred coloured node** sitting between three feeders: Strategic Targets (top), Market & Environment (top-right), Portfolio (centre). Three dashed/dotted arrows fan IN from the three feeders. Visual: muted amber solid box (already in palette), distinct from the other clusters but visually integrated. Communicates "the gap between what the market says we should hold + what our strategy says we should hold + what we currently hold."
**Why:** Richard's framing — the gap IS the diff between three things, not a binary annotation. Repositioning makes it structurally correct.
**Locked by:** Richard.

## D-LP-23 — GAP card displays live OKRs from inline JSON

**Date:** 2026-05-09 PM
**Decision:** GAP card content rendered from inline `<script type="application/json" id="okrs">` in landing-page.html. Content of script tag = the current month's OKR JSON, copied from `databases/portfolio-okrs/current.json`. Display format: checklist with 0/N counts per OKR, last-updated stamp at bottom. Card itself is clickable → opens portfolio-okrs current view (TBD what — for now points at the JSON file directly).
**Why:** No fetch needed (file:// safe). Watson can grep the same JSON. Single source of truth. Edit the script-tag JSON when OKRs change; nothing else moves.
**Caveat:** When OKRs are updated in `databases/portfolio-okrs/current.json`, someone needs to also update the inline JSON in landing-page.html (or build a script that does both). For v4 it's a manual two-step until SA - GITHUB SOP next pass automates.
**Locked by:** Richard.

## D-LP-24 — Strategic Targets cluster: ETCs/TCs/OKRs equal-weight stack

**Date:** 2026-05-09 PM
**Decision:** Cluster contents render as three equal-weight rows: ETCs, then Portfolio TCs, then Portfolio OKRs. No title hierarchy (drop "Evergreen Target Conditions" as title-class, "Portfolio TCs" + "Portfolio OKRs" as sub-class). All three rendered at the same font-size/weight as section titles (currently `.title` class). Order = broad-to-narrow time horizon.
**Why:** Richard: "Evergreen target conditions should be same size of text/importance as the TCs and OKRs in that section." All three are first-class citizens of strategic targets.
**Locked by:** Richard.

## D-LP-25 — Move existing thematic content into new structure

**Date:** 2026-05-09 PM
**Decision:** Sweep existing thematic content into `databases/thematics/`:
- `PROJECTS/RES - AI Thematic Research/AI-thematic-memo-v1-2026-05-02.docx` and `v2-2026-05-03.docx` → COPIED (not moved) to `databases/thematics/ai/2026-05-02-ai-thematic-memo-v1.docx` and `2026-05-03-ai-thematic-memo-v2.docx`. Keep originals in source project untouched.
- `Files/THEMATIC-bear-market-AS-raw.md` → COPIED to `databases/thematics/recession-rollover/_raw-research/THEMATIC-bear-market-AS-raw.md`. Same for iran-war.
- `memory/thematics/active.md` and the operational scaffolding files (composite-scores.md, portfolio-impact-matrix.md, README.md) STAY in `memory/thematics/`. They're doctrine, not reports.
**Why:** COPY not MOVE for v4 — preserves source-of-truth in original projects until APM confirms the thematics dashboard is the canonical home. Promotes to MOVE in next APM SKILL pass.
**Locked by:** Watson per Richard's "B" answer to Gap 2.

## D-LP-27 — Manifest schema generalised: aj_memo + source_research + raw_research

**Date:** 2026-05-09 PM
**Decision:** `databases/thematics/manifest.json` schema bumped to v2. Each thematic now carries three arrays: `aj_memo` (canonical APM Analysis & Judgement memo, multiple versions allowed with current/superseded badges), `source_research` (researcher artefacts that fed the memo — brief, drafts, AS extracts, prompts, manifests, delta reports, consolidated notes), `raw_research` (raw AS feeders, kept as-is). Dashboard renders three colour-coded sections per thematic: A&J Memo (amber), Source Research Reports (green), Raw Research Feeders (grey). Empty arrays render as graceful empty-state messages.
**Why:** Richard explicit: "Generally, set it up to link to the A&J MEMO and to the source RESEARCH REPORTS." Schema supports per-thematic build-out as APM produces memos for Iran/Recession.
**Locked by:** Richard.

## D-LP-28 — Dead vfhqi/memory placeholder hrefs purged

**Date:** 2026-05-09 PM
**Decision:** All `data-href-gh="https://github.com/vfhqi/memory/blob/main/..."` placeholders in landing-page.html replaced with `data-href-gh="https://vfhqi.github.io/landing/"` so GH-mode clicks return to the landing page rather than 404. The two affected hrefs were Strategic Targets cluster (was pointing at `vfhqi/memory/blob/main/context/values-and-behaviours.md` — dead) and Workflow Priorities cluster (was pointing at `vfhqi/memory/blob/main/projects/pipeline.md` — dead). No memory repo exists.
**Why:** Richard hit the 404 when clicking the OKR/GAP region — landed on Strategic Targets href. Investigation revealed all `vfhqi/memory` references were placeholders Watson wrote in v1 expecting a future memory repo. None exists; all dead.
**Trade-off:** Local-mode clicks still work (point at COWORK files); GH-mode clicks now land on landing page (less informative but not 404).
**Future-fix candidate:** if/when a public memory repo (or sanitised mirror) is created, repoint these. Filed as a pending item in SA - GITHUB SOP follow-up brief.
**Locked by:** Richard.

## D-LP-29 — GAP card click points at 2026-05.json (real data, not pointer)

**Date:** 2026-05-09 PM
**Decision:** GAP card href changed from `databases/portfolio-okrs/current.json` (one-line pointer file `{"current_period": "2026-05", ...}`) to `databases/portfolio-okrs/2026-05.json` (real period file with full OKR content). Same change for GH href.
**Why:** Richard clicked the GAP and expected to see actual OKR content, not a single-line pointer.
**When the period rolls over:** the file path embedded in the GAP card needs updating to point at the new period file. Manual one-line edit until automated. Same trigger as updating the inline `<script id="okrs">` JSON.
**Locked by:** Richard.

## D-LP-30 — Market & Environment cluster shows live thematic names

**Date:** 2026-05-09 PM
**Decision:** Two italic subtitle lines in M&E cluster ("Fit for fighting · Radar process" / "Sector tilts · risk-on/off posture") replaced with: keep "Fit for fighting · Radar process" subtitle once; new title "Active thematics (3)"; below, three thematic names rendered ("AI", "Iran Oil", "Recession / Bear Market Roll-over"). Names read from `manifest.json` at build time (single source of truth — if manifest grows, cluster doesn't auto-update; rebuild required).
**Why:** Richard: "Actually show the active thematics (e.g. the 3 mentioned)."
**Future:** if active thematic count grows beyond 3, M&E cluster needs a layout change (cluster height fixed to 140 — fits 3-4 lines max). Flag for future iteration.
**Locked by:** Richard.

## D-LP-31 — GAP formatting fixes (arrow alignment, text fit, spacing)

**Date:** 2026-05-09 PM
**Decision:** Three fixes applied:
- (i) GAP node widened from 100px to 140px (x=830 width=140 — was x=870 width=100). Now x range 830-970, leaving 10px gap to Workflow Priorities at x=980.
- (ii) Arrow path coordinates recomputed to terminate at actual node edges: M780,160→C828,198 from Strategic Targets; M1020,160→C972,198 from Market & Environment; M770,265→C828,265 from Portfolio.
- (iii) OKR text size reduced 8.5px→8px; long descriptions truncated at 32 chars with ellipsis; left padding x=840 (4px from box edge); centre coords recomputed for new box centre x=900.
**Why:** Richard confirmed: "The things you found are what I meant" — referring to the 3 candidate issues Watson surfaced (arrow misalignment, text overflow, cluster overlap risk).
**Locked by:** Richard.

## D-LP-32 — Stocks Universe substrate shows real counts

**Date:** 2026-05-09 PM
**Decision:** Substrate ground-bar text updated from placeholder "~1,300 European stocks · pullback-watchlist.json · Notion Stocks Database" to "973 stocks · 24 industries · 154 sectors · pullback-watchlist.json". Numbers derived from `databases/pullback-watchlist.json` at build time. Click target unchanged (opens the JSON file).
**Why:** Richard: "List actual numbers of stocks in there and when clicked, open the source list file."
**Auto-update:** numbers are baked at build time, not live-fetched. If the watchlist grows/shrinks, rebuild required to refresh display. (Consistent with rest of the page — no live data fetches.)
**Locked by:** Richard.

## D-LP-33 — .nojekyll added to GH repo

**Date:** 2026-05-09 PM
**Decision:** Added empty `.nojekyll` file to `vfhqi/landing` repo root. Disables Jekyll processing on GH Pages.
**Why:** GH Pages defaults to Jekyll, which **ignores any folder/file starting with underscore**. Source research files were under `_source-research/` and raw research files under `_raw-research/`. All returned 404 on the live URL until `.nojekyll` was added, then all returned 200.
**Verified:** `https://vfhqi.github.io/landing/thematics/ai/_source-research/delta-report.md` returns 200 after `.nojekyll` push.
**Standing rule for future GH Pages content with underscore-prefixed folders:** ensure `.nojekyll` exists at the repo root.
**Locked by:** Watson per discovery during v5 verification.

## D-LP-26 — Watson SKILL operationalisation deferred

**Date:** 2026-05-09 PM
**Decision:** v4 ships landing-page changes ONLY. No APM SKILL edits, no scheduled-task wiring, no auto-ingest of OKRs into Watson workflow. JSON schema is structured to support future Watson use; the operational hook-up is Richard's later call.
**Why:** Richard explicit: "We won't right now get the PORTFOLIO OKRs integrated into the workflow, skills, memory files, of WATSON, the APM role, etc. I will do that separately."
**Implication:** Do NOT touch APM SKILL, RESEARCHER SKILL, scheduled tasks, CLAUDE.md operational rules in v4. Touch only: `databases/thematics-dashboard.html`, `databases/thematics/`, `databases/portfolio-okrs/`, `landing-page.html`, project files in `PROJECTS/SA - LANDING PAGE/`.
**Locked by:** Richard.

## D-LP-19 — vfhqi/landing repo created + Pages enabled + URL verified

**Date:** 2026-05-09 PM
**Decision:** Repo created via API (not manual UI). Public, no issues/projects/wiki. Pushed staged commit (README.md + index.html, 25,172 bytes byte-verified). Pages enabled via API on `main` branch / root path. First build completed in <45s. Live URL **`https://vfhqi.github.io/landing/`** verified: HTTP 200, body byte-identical to local landing-page.html, all 19 anchors present, REMINDER block + GAP? + Wisdom Library + Stocks Universe Database + Basing Plateau + Mark Minervini + Notes Repository all present, ends `</html>`, version marker `v3` present.
**Locked by:** Watson + verified live.

## D-LP-17 — Silent file truncation incident — recovery + standing rule

**Date:** 2026-05-09 PM
**Decision:** v3 build hit the documented silent file truncation bug (per `feedback_silent_file_truncation.md`). Edit tool calls on the 23KB v2 file silently truncated the source mid-content; the corruption propagated to all shipped files. Recovery: restored intact v2 from snapshot, applied v3 patches via Python single-pass write to /tmp, byte-verified, then atomic-cp into all 5 ship locations. All 5 files post-recovery match source byte-for-byte (25,172 bytes) and end `</html>`. Corrupted files preserved as `*.CORRUPTED-bak-*` per SOP.
**Standing rule for this project:** Edit tool BANNED on `landing-page.html` and any v* file >20KB. All future patches must use Python heredoc → byte-verify → atomic mv pattern.
**Locked by:** Watson per global SA standard.

## D-LP-15 — Drop "build in flight" subline on Master Dashboard

**Date:** 2026-05-09 PM
**Decision:** Replace "build in flight — opens at clicked tab" with "Click any screen above to open at that tab" on the Master Dashboard parent node.
**Why:** Richard: "Remove 'build in flight'." Implication: don't surface build status in the user-facing landing page.
**Locked by:** Richard.

---

## Parked / out of scope (noise from original sketch)

The following items appeared in Richard's original sketch (08-May-26) but he confirmed in his 09-May-26 redraw message that they are noise. **Do not re-debate.**

- **`25?b`** in the original CYAN cluster — meaning unknown, parked. PMS box has no number on the redraw.
- **Coloured-letter list** `Y - probel / G - MM 2 / G - VCP 2 / e - utr 2 / D - basing 2 / V - retypee / V - stage 4 / R - / R - stge 3` — parked. The Ratings Dashboard composite is now the four columns Timeliness/Knowledge/Interest/Master ratings.
- **`IASA library`** vs **IAJA library** debate — parked. Replaced by simple "Notes Repository" naming.
- **`L / SL / ML / LL / VLL / -`** sizing tier list — parked.
- **`4-5 master principles / A/B / degree of bull case / rate via my framework`** central scratch text — parked.
- **Coverage of Domain 3 (Market Environment)** as a separate question — answered: it's the new MAGENTA cluster on the redraw.

(More decisions added as design progresses.)
