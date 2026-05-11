# Wisdom Library — Candidate Queue

**Purpose.** Append-only staging file for Wisdom Library candidates that surface during sessions but are not yet ready to file. Examples: needs more cases, needs Richard's approval, needs cross-check, evidence too thin for Bronze tier.

**Owner.** Whoever surfaces a candidate appends. Richard reviews periodically (weekly or at last-Friday-of-month WFP). Approved candidates get authored to `wisdom-library/{category}/{slug}.md` + indexed in `INDEX.json`. Rejected candidates get a deletion note + reason.

**Created.** 03-May-26 by Watson per AJ SOP v2.3 §Phase 4.5 + session-handoff SKILL V2 §Step 5.5 + RESEARCHER SKILL-V2.11 Rule #37 (the Wisdom Library bookend pattern).

**Format per entry:**

```
### {DD-MMM-YY} — {SOURCE-SESSION} — {CANDIDATE NAME}
- **Tier proposed:** {Bronze / Silver / Gold}
- **Category:** {situational/X / general/Y}
- **Evidence:** {1-3 sentences on what surfaced it; cite the session / stock / artefact}
- **Why deferred:** {needs more cases / needs Richard sign-off / needs cross-check / other}
- **Sourcing path to file:** {trigger that would promote — e.g., "1 more case observed in Q3 2026"}
- **Disposition:** {pending / approved / rejected — Richard's call when reviewed}
```

**Cross-ref:**
- `wisdom-library/SKILL.md` (consultation conventions + entry format)
- `wisdom-library/INDEX.json` (where approved entries get indexed)
- `memory/skills/session-handoff/SKILL.md` §Step 5.5 (the workflow that feeds this queue)
- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.3 §Phase 4.5 (APM-specific feeder)
- `memory/skills/researcher/SKILL-V2.md` v2.11 Rule #37 (RESEARCHER consults the library before any query)

---

## Entries

*(no entries yet — first entry on first deferred candidate from session-end Hot Wash + WL Survey)*

### 03-May-26 PM — v2.3 bookend integration session — Cross-role lock-step pattern
- **Tier proposed:** Bronze
- **Category:** general/decision-making
- **Evidence:** When a new rule needs to fire across multiple roles (today: WL bookend across APM + RESEARCHER + session-handoff), ALL touched SOPs must reference each other explicitly. Without bidirectional cross-refs, a future SOP edit could break one side without anyone noticing. Today's 3-SOP cross-ref network is the textbook implementation.
- **Why deferred:** One observation is too thin for Bronze; needs 1-2 more cross-role rule integrations to validate.
- **Sourcing path to file:** Next cross-role rule integrated (likely Components SOP when authored, or any future cross-role workflow change).
- **Disposition:** pending

### 03-May-26 PM — v2.3 bookend integration session — Pre-write JSON validation discipline
- **Tier proposed:** Bronze (sibling) OR promote `memory-needs-workflow-binding` to Silver
- **Category:** general/decision-making
- **Evidence:** The 1-May-26 INDEX.json corruption pattern was directly caused by skipping pre-write validation; today's discipline (`python3 -c "import json; json.load(...)"` before every INDEX edit) prevented recurrence across 3 separate INDEX edits this session.
- **Why deferred:** Conceptually covered by `memory-needs-workflow-binding` (already Bronze, today). This is a specific instance, not a new general pattern. Better to promote `memory-needs-workflow-binding` to Silver after 2-3 more confirmations than create a sibling.
- **Sourcing path to file:** 2-3 more "memory-rule-without-binding-fails" observations → promote `memory-needs-workflow-binding` Bronze → Silver.
- **Disposition:** pending

### 03-May-26 PM — v2.3 bookend integration session — Override-the-trial pattern
- **Tier proposed:** Bronze (Watson behavioural) OR not-yet-Wisdom-Library-worthy (file under HPC observations instead)
- **Category:** Watson behavioural pattern (HPC) — possibly general/decision-making at Bronze
- **Evidence:** The TRIAL MODE pattern (1-May-26 AJ SOP review's "trial for ~3 weekly cycles before integrating") was overridden TWICE this week (v2.2 integration on 03-May-26 + v2.3 integration today). Pattern: when Watson recommends "wait for evidence," Richard often sees the answer as already-known and integrates immediately. Watson's default trial-recommendation may be miscalibrated (over-cautious).
- **Why deferred:** Could be Watson behavioural calibration (HPC concern, not WL entry) OR a general "premature trial-mode is over-caution" decision-making rule (WL entry). Need Richard's judgement on framing before filing.
- **Sourcing path to file:** Richard's framing decision next session, OR 1-2 more override observations to confirm the pattern is structural not session-specific.
- **Disposition:** pending

### 04-May-26 — Cohort layer codification session — Stacked workflow extensions pattern
- **Tier proposed:** Bronze
- **Category:** general/decision-making
- **Evidence:** KZN-003 (bookend) + KZN-004 (cohort) demonstrate that workflow extensions stack additively when each successive layer wraps prior layers without replacing them. KZN-004 added cohort layer on top of KZN-003 bookend; per-stock Phase 0.2 / Phase 4.5 / G16 still fire unchanged when no cohort manifest exists. Backward-compatibility-by-construction is the load-bearing property. Pattern likely generalises to future workflow extensions (e.g. portfolio-construction layer above cohort layer; multi-cohort campaign layer above sub-cohort layer).
- **Why deferred:** One observation; need a third instance (a future workflow layer that stacks on cohort) to confirm pattern is structural not coincidental.
- **Sourcing path to file:** Next workflow-layer extension that stacks additively without replacing prior layers. Promote when 3rd instance observed.
- **Disposition:** pending

### 04-May-26 — Cohort layer codification session — FUSE truncation defence pattern reinforced
- **Tier proposed:** Bronze (sibling) OR promote `memory-needs-workflow-binding` to Silver (per existing 03-May-26 deferred candidate)
- **Category:** general/decision-making
- **Evidence:** Mid-session multi-edit Edit-tool sequence on AJ SOP truncated mid-pass, losing ~150 lines from end. Recovery via byte-verified backup restoration was clean. ALL subsequent SOP edits used Python heredoc + atomic mv + assert-anchor pattern (zero failures across 4 file amendments). Reinforces the 28-Apr-26 / 30-Apr-26 / 03-May-26 prior observations of the same pattern. Recommendation: refresh `feedback_silent_file_truncation.md` with this incident as the 4th confirmed instance.
- **Why deferred:** Same as 03-May-26 deferred entry — better to promote `memory-needs-workflow-binding` to Silver than create sibling. This is a specific instance of the parent pattern. Now 4 confirmed instances of the parent pattern (28-Apr / 30-Apr / 03-May / 04-May) — meets Silver promotion threshold.
- **Sourcing path to file:** Author should propose `memory-needs-workflow-binding` Bronze → Silver promotion at next quarterly review (or earlier if prompted). The 4-instance count is now over the Silver threshold.
- **Disposition:** pending — recommendation: promote parent to Silver

### 04-May-26 — Cohort layer codification session — Cross-fertilisation requires structural binding (cohort layer hypothesis)
- **Tier proposed:** Bronze (NEW pattern, distinct from `memory-needs-workflow-binding`)
- **Category:** general/decision-making (or potentially situational/portfolio-construction)
- **Evidence:** The 03-May-26 EKTA/HTRO/PRY/COTN-CH session produced 5 cross-stock WL entries that no per-stock memo could surface in isolation. Without the cohort layer (KZN-004), those entries existed only because of timing-coincidence. Pattern: cross-fertilisation between analytical units (stocks, projects, decisions) requires explicit structural binding (cohort manifest + Phase 4.6 wash-up); cross-fertilisation does NOT happen by accident at scale even when the analyst is good at it. The general principle: insights that require N≥2 units in adjacent context will be lost without a workflow ceremony forcing the comparison.
- **Why deferred:** Hypothesis from one cohort batch (03-May-26). Need 2-3 more cohort cycles to confirm: (a) cohort wash-up reliably produces cross-unit insights, (b) absence-of-cohort-layer reliably produces ZERO cross-unit insights. The empirical case for KZN-004 is the pattern's first observation; tier promotion comes after operational testing.
- **Sourcing path to file:** First 3 cohort cycles under v2.4. If wash-up consistently produces ≥1 cross-stock WL entry, file as Silver. If only 1 of 3, demote / archive.
- **Disposition:** pending

### 04-May-26 — RESEARCHER batch session (38-page posting) — AS coverage ceiling is not a process signal
- **Tier proposed:** Bronze
- **Category:** general/decision-making (data-quality diagnosis)
- **Evidence:** AENA/BUFAB/DCC/DKSH 06-SS queries all returned 1,400–1,700w vs 3,000w target. Richard confirmed re-running AS would not yield better results — ceiling is set by broker coverage indexed in AlphaSense, not by query quality. Single-session observation; 4 tickers sharing the same pattern.
- **Why deferred:** One session, though 4 instances. Need confirmation on different stock universes (different industry, different broker coverage profile) before promoting.
- **Sourcing path to file:** 2-3 more batch sessions where thin AS SS is confirmed as a ceiling not a process gap. Also: does RESEARCHER SKILL-V2 Rule #17 already capture this adequately? If yes, no new WL entry needed — just a Rule #17 annotation.
- **Disposition:** pending

### 04-May-26 PM — base-identification before patch
- **Tier proposed:** Bronze
- **Category:** general/decision-making
- **Evidence:** Watson patched the live v1 dashboard for ~3 hours when the actual target was the v2.1 rebuild with Harvey balls. Single observation, but cost 3 hours of work + Richard's correction.
- **Why deferred:** One session. Pattern needs to recur or be Richard-validated before filing.
- **Sourcing path to file:** Next dashboard session. If base-identification gate fires correctly and prevents wrong-base error, log success and promote toward Silver.
- **Disposition:** pending
- **Cross-ref:** `feedback_quality_gate_must_run_at_decision_point.md` (capability-check pattern)

### 04-May-26 PM — project backups search before asking
- **Tier proposed:** Bronze
- **Category:** general/decision-making
- **Evidence:** When asked "find v2.1 link", Watson asked Richard for the path instead of grep'ing project backups directory where the file sat under a self-explanatory filename. Cost: Richard's correction, ~5 min wasted.
- **Why deferred:** One session.
- **Sourcing path to file:** Next time Watson is asked to locate a session artefact, document whether project-backups-search fired first.
- **Disposition:** pending
- **Cross-ref:** session-handoff/SKILL.md Step 0 + Step 6 (project-folder routing)

### 04-May-26 PM — two storage conventions for A&J memos
- **Tier proposed:** Bronze
- **Category:** situational/process — A&J memo file conventions
- **Evidence:** A&J memos have TWO storage locations on disk:
  - V20-doctrine JSON: `databases/memos/{TICKER}/{Stage}.json` (used for EKTA, HTRO, PRY, COTN-CH)
  - Markdown: `Files/{TICKER}/{Stage}/aj-memo-v1.md` (used for GYM, BFIT, SATS gym-trio)
  - Cohort outputs: `Files/{COHORT-NAME}/synthesis/...`
  Watson searched only databases/memos/ and reported "not found" — failed to find 6 gym-trio memos that exist on disk.
- **Why deferred:** Will be promoted once integrated into APM SKILL Step 3.5 as part of a structural fix, not just a memory entry.
- **Sourcing path to file:** Add structural extension to APM SKILL Step 3.5 covering both A&J locations. Then archive this WL entry as "fixed structurally."
- **Disposition:** pending — convert to APM SKILL extension in next SA pass

### 04-May-26 PM — compromise-recommendation reflex
- **Tier proposed:** Bronze
- **Category:** general/decision-making
- **Evidence:** Watson framed gym-trio markdown→V20 render as "Option X (partial fidelity, faster) vs Option Y (full fidelity, harder)" and recommended Option X. Richard rejected as "compromised short cut" and stopped the work. Same pattern as kaizen Root Cause B (false economy).
- **Why deferred:** One session. The pattern is documented in kaizen lesson already; needs to be hard-coded rather than just memory-logged.
- **Sourcing path to file:** Watch for compromise-recommendation reflex in next 3 sessions. Each instance Richard catches escalates toward a structural fix.
- **Disposition:** pending
- **Cross-ref:** kaizen `2026-05-04-quality-gate-failures.md` Root Cause B; D-DMRL-11

### 04-May-26 PM — phantom-deadline same-day recurrence
- **Tier proposed:** Bronze with escalation note
- **Category:** general/decision-making — behavioural priors override rules
- **Evidence:** Morning kaizen lesson `2026-05-04-quality-gate-failures.md` documented self-imposed tempo pressure as Root Cause B. Same afternoon, Watson generated multiple time-pressure narratives around the 17:09 UK daily-push (which was structurally irrelevant). Same-day recurrence of a documented pattern.
- **Why deferred:** Same-day recurrence makes this Bronze-with-escalation. Recommendation: escalate to a session-start protocol gate (forced check at session start: "is there any deadline imposed by Richard for this work? If no, narrate that no deadline exists.").
- **Sourcing path to file:** If this recurs again in next session (despite kaizen + corrections.md + this WL entry), escalate to hard-coded session-start gate.
- **Disposition:** pending escalation review at next weekly review
- **Cross-ref:** kaizen `2026-05-04-quality-gate-failures.md`; this session's corrections.md entry 4

### 05-May-26 — bracketed-figures-in-termsheets-are-indicative
- **Tier proposed:** Silver
- **Category:** general/decision-making — source quality
- **Evidence:** UBS AMC termsheet showed credit ratings as `[Aa2 Moody's / A+ S&P / AA- Fitch]`. Square brackets in legal/structured-product documents signal "indicative / to-be-confirmed at final terms," not authoritative. Watson cited them as authoritative facts in v1-v3 memos. Audit caught it; v4 dropped specific ratings in favour of "investment-grade".
- **Why deferred (not Gold):** observed in one document type (structured-product termsheet). Need confirmation that the convention extends to other legal-doc archetypes (offering memos, prospectuses, draft contracts) before promotion.
- **Sourcing path to file:** observe in 2 more documents from different counterparties / asset classes.
- **Disposition:** pending; revisit at next external-doc-derived deliverable.
- **Cross-ref:** corrections.md correction 7 (this session); D-AMC-7.

### 05-May-26 — generalist-vs-sophisticated-investor-memos-pair
- **Tier proposed:** Bronze
- **Category:** general/decision-making — communication / audience-segmentation
- **Evidence:** Richard chose to produce TWO parallel memos for the same announcement — generalist HNW (4 pages, plain English, omits SSPA codes / floor / deleverage trigger / structural risk language) vs sophisticated ex-finance HNW (4 pages, full structural detail, termsheet table, §871(m), no-segregation language). One memo for both audiences would have been a worse compromise than two well-targeted ones. Pattern: when the audience splits, write the document twice rather than once for the lowest-common-denominator.
- **Why deferred (not Silver):** observed once. Could be a Richard-specific preference rather than a universal pattern.
- **Sourcing path to file:** observe at next wide-audience external communication.
- **Disposition:** pending; revisit at next IR/LP communication.
- **Cross-ref:** D-AMC-5; this session's deliverables.

### 05-May-26 — fact-audit-before-shipping-external-doc
- **Tier proposed:** Silver
- **Category:** general/decision-making — quality / verification
- **Evidence:** Richard explicitly requested an "exhaustive fact audit" of every claim, figure and name before final shipment. Audit produced 11 flagged items, 7 of which carried into v4 changes (ratings dropped, "as of May 2025" qualifier added, "operating as Viewforth" softened, JM Finn / HL caveat added, transfer integration). 4 items left as-is (ISA/SIPP "platform can confirm", ISIN "mid-May", SOFR detail dropped, Aptos font availability). Without the audit gate, the memo would have shipped with the bracketed ratings stated as fact.
- **Why deferred (not Gold):** strong pattern but limited cross-cases yet. Operational equivalent of the Quality Gate (kaizen 2026-05-04) for external-document workflows.
- **Sourcing path to file:** apply pre-ship audit to next 2 external deliverables; if always net-positive, promote to Silver, then Gold.
- **Disposition:** make the audit step a default gate on the IR/LP deliverable workflow.
- **Cross-ref:** kaizen `2026-05-04-quality-gate-failures.md`; corrections.md correction 7 (this session).

### 05-May-26 — utf8-mojibake-on-python-heredoc-write
- **Tier proposed:** Bronze
- **Category:** general/operating — file-system / SA-track
- **Evidence:** Recovery write via Python heredoc with non-ASCII content (em-dash, smart quotes) produced double-encoded bytes (`c3 a2 c2 80 c2 94` = UTF-8 bytes for `—` re-interpreted as Latin-1 then re-encoded). Rendered as mojibake in docx. Repaired via byte-level find-and-replace.
- **Why deferred (not Silver):** companion to existing Silver `feedback_silent_file_truncation.md`. Observed once. Could fold into that entry as a sub-case.
- **Sourcing path to file:** observe one more occurrence; consider amalgamating into the silent-truncation auto-memory entry.
- **Disposition:** pending; SA may want to handle inline as a defensive Python wrapper in the docx-build workflow.
- **Cross-ref:** corrections.md correction 10 (this session); `feedback_silent_file_truncation.md`.

## 2026-05-09 — SA - LANDING PAGE session — 3 candidates

### Candidate 1: "Sketch ambiguity = back-brief mandatory"
- **Tier candidate:** Bronze (specific to visual/diagram work)
- **Source:** SA - LANDING PAGE session 1, decisions.md D-LP-04 → D-LP-04-rev pivot
- **Insight:** Hand sketches (especially with colour markup) have multiple valid interpretations. Always back-brief the cluster decoding + ask 3 specific gap-Qs before any build. Three Gaps + Mission Command saved at least one round of rework on every iteration in this project.
- **Counter-evidence:** none in this session. Pattern held across 5 iterations.
- **Domain:** project management / visual design / requirements gathering

### Candidate 2: "Inline JSON `<script>` for single-file dashboards"
- **Tier candidate:** Silver (universal applicability across dashboard projects)
- **Source:** SA - LANDING PAGE session 5, D-LP-23
- **Insight:** Pattern for embedding data into self-contained HTML that needs to work from `file://` AND on GH Pages without CORS issues. `<script type="application/json" id="X">` block in the same HTML; JS reads via `JSON.parse(document.getElementById('X').textContent)`. Watson can grep the same data the page renders. Single source of truth in one file.
- **Counter-evidence:** introduces fragility — when underlying data changes, both the source JSON file AND the inline copy in HTML must update. Mitigation: build script that does both in one pass (deferred to next iteration).
- **Domain:** software architecture / dashboard design / data flow

### Candidate 3: "GH Pages + underscore folders requires .nojekyll"
- **Tier candidate:** Silver (cross-cuts SA - GITHUB SOP, every GH Pages repo Watson ships)
- **Source:** SA - LANDING PAGE session 6, D-LP-33
- **Insight:** GH Pages defaults to Jekyll. Jekyll silently 404s any folder/file starting with underscore. `.nojekyll` (empty file) at repo root disables Jekyll processing; underscore paths then resolve normally. Universal trap when shipping any structure with `_source-research/`, `_raw-research/`, `_archive/`, `_meta/`, etc.
- **Counter-evidence:** none. Standing rule for all future GH Pages repos.
- **Cross-ref:** SA - GITHUB SOP follow-up brief Step 8.6 (lock as standing SOP rule).
- **Domain:** publishing / GitHub Pages / static site generators

