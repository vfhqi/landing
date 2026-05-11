# Watson Corrections Log
<!-- Append-only. High-signal calibration points. Never delete entries. -->

### 2026-05-08 — [Operational / GITHUB SOP — Stale-Source Overwrite of Fresher Remote] [MISSION CRITICAL]

**Context (SA — GITHUB SOP project, incident 07-May-26 17:10 UK, diagnosed 08-May-26):**
PC-side automation pushed a stale local working tree over fresher remote work on `vfhqi/ratings/main`. The push was a clean `git push`, no force, no merge — and that is *why it slipped through*. Every existing safeguard in the SOP looks at the git layer; this failure mode lives one layer upstream of git.

**Concrete trace from `git log vfhqi/ratings`:**
- `b3f73b5` — Watson 15:43 UK 07-May — "Watson: rename Q4/Q5/Q9/Q11 display names + re-embed coverage data" (+672 lines net, the live-good state).
- `b2ed2df` — "Richard Black (via Watson)" 17:10 UK 07-May — "Update index.html - 07-May-26 17:10 UK" (-50,328 / +412 lines, near-total regression — 25-query layout reverted to 23, all wc:NNNN fields stripped, source indicators removed, Q4/5/9/11 renames undone, lcCellHref JS gone, four post-deploy fixes lost).
- `b1068d5` — Watson 03:31 UK 08-May — "Watson: restore live dashboard to b3f73b5 — revert b2ed2df regression" (recovery, ~10h after the silent overwrite).

**Diagnosis:** The "(via Watson)" author string and timestamp pattern fingerprint a PC-side automation script — `refresh-dashboard-silent.bat` or `push-to-github.ps1` — running on a `master-dashboard/.git` working tree that was older than the sandbox content already on remote. The scripts as written do NOT `git fetch` before regenerating + pushing, so when sandbox-side Watson commits land on remote and the PC clone is left untouched, the next scheduled PC run regenerates from stale local source and pushes it. Clean fast-forward from the PC's point of view; near-total regression from the live-site point of view.

**Why every existing safeguard missed it:**
1. **Fresh-clone-to-`/tmp` pattern** — irrelevant; this was the PC clone, which is persistent.
2. **No-force-push prohibition** — irrelevant; this wasn't a force-push.
3. **Pre-push HTML well-formedness gate** — passed; the regression was structurally valid HTML, just the wrong content.
4. **D-GIT-3 tiered audit** — would have flagged structural drift but not "this file is just an older version of itself."
5. **Branch protection on github.com** — deferred 07-May (Risk 7 Partial); irrelevant anyway, this wasn't a force-push.

**Lesson (operational, generalisable):**
**A safe push pattern at the git layer does not protect against unsafe content selection upstream of the git layer.** Any push pipeline that copies/generates content from a working area into a temp clone, or that runs on a persistent local clone without fetching first, has a stale-source blind spot. The defence has to look at *what's about to be pushed* vs. *what's already on origin* — not at git plumbing.

**Mitigation shipping (Step 2 of GITHUB SOP rollout, post-D-GIT-13):**
Three-layer pre-push guard, all required:
1. **Content-divergence check** — SHA256 of source file vs `git show origin/main:<path>` before any `cp`. Mismatch → block, override-able with explicit Richard approval, logged here.
2. **Fetch-and-behind check** — `git fetch && git rev-list --count HEAD..origin/main` mandatory on PC-side scripts; best-effort on sandbox `/tmp` clones. Non-zero → block, no override.
3. **Post-push SHA verification** — `git ls-remote origin main` must match `git rev-parse HEAD` after push. Mismatch → alert + investigate.

**Interim mitigation (until D-GIT-13 ships in Step 2):**
Do NOT run PC-side dashboard automation (`refresh-dashboard-silent.bat`, `push-to-github.ps1`, scheduled refresh tasks) until the three-layer guard is in place. Or, if a manual refresh is needed, run `git fetch && git pull --ff-only origin main` in `master-dashboard/` first.

**Rule for future SA work:** When the SOP says "safe push," always ask "safe against *what failure modes*?" Force-push prohibition closes one class. Fresh-clone closes another. Content-divergence-vs-origin is its own class — and the most insidious because every layer of git looks satisfied while the live site silently regresses.

**Cross-ref:** D-GIT-13 in `projects/SA - GITHUB SOP/decisions/decisions.md` + Risk 8 in `projects/SA - GITHUB SOP/research/risk-register.md` + Step 2 acceptance criteria in `projects/SA - GITHUB SOP/plan.md`. The SKILL at `memory/skills/github-push/SKILL.md` (Step 4, pending) will include this incident as a worked example in its troubleshooting section.

---

### 2026-05-06 — [Architectural / Single-Identifier Drift Across N Independent Ticker-Keyed Files] [MISSION CRITICAL]

**Context (SA — Master Dashboard taxonomy unification, 06-May-26):**
A single ticker rename (e.g. `EKTA-SE → EKTA.B-SE`) had to propagate across 8+ separate files: watchlist, mapping, prices, filters, ssem, valuation, positions, universe.dashboard_ticker, stage-snapshots, ticker_mapping legacy, plus chart filenames. Drift in any one of them caused silent or visible bugs — most notably the CARLB-DK ghost row that survived 5 patch passes before its final source (positions.json) was traced.

**Lesson (architectural, generalisable):**
**Any system with N independent identifier-keyed files has N−1 places where drift can hide.** Validators must check cross-file consistency, not just within-file integrity. A subset-relation check ("every ticker in file X exists in file Y") catches what within-file checks miss. This is true of any keyed identifier (tickers, account IDs, project codes, symbols), not just stock tickers.

**Mitigation shipped this session:**
1. `audit_system_integrity.py` — cross-file ticker consistency check across 11 surfaces. Reports errors (drift breaks the system) vs warnings (worth knowing). Exit codes 0/1/2. `--strict` escalates warnings to errors.
2. SA role gains a **System Integrity sub-discipline** with fortnightly cadence. Doctrine appended to `memory/skills/systems-architect/SKILL.md`.
3. Pipeline pre-flight hook in `generate_master_data.py` — soft warning by default, `--strict-integrity` escalates.
4. Run before any data-file commit (recommended pre-push gate).

**Rule for future SA work:** When designing or modifying a system that uses identifiers across multiple files, the question to ask is *"how do we validate consistency across these files?"* The answer should be "we have a tool that does it" before the system ships. If the tool doesn't exist yet, build it BEFORE adding the second ticker-keyed file.

**Sub-lesson (positions.json blast radius):**
positions.json drift is the highest-impact identifier drift. A live position pointing at a ticker the dashboard no longer recognises means broken price tracking, broken stop-loss alerts, broken P&L. **positions.json drift is treated as ERROR in the audit, not warning.** Catch this before any rename ships.

**Cross-ref:** SA SKILL System Integrity sub-discipline section + state.md SA - Master Dashboard Session 16 + audit_system_integrity.py + auto-memory `feedback_cross_file_identifier_drift.md` (to be created).

---

### 2026-05-04 — [Operational / Edit Tool Silent Truncation on Cowork Mount — Extends 30-Apr-26 Write Tool Issue]
**Correction (Watson self-discovered during handoff):** During session-handoff SOP execution for SA - Master Dashboard, three Edit-tool calls on existing memory files silently truncated despite returning success:
- `memory/session-handoffs/latest.md` — full ~3.6KB rewrite, only 223 bytes landed (truncated mid-line in handoff-note path).
- `projects/SA - Master Dashboard/transcript.md` — Session 14 marker append (~3KB), only first paragraph of Stream 2 landed before truncation mid-sentence at "**Stream 2 (commit".
- `projects/SA - Master Dashboard/decisions.md` — full append of D-MD-INPUTS-1/2 + D-MD-CHART-4..10 + D-MD-PROCESS-1/2 (~9KB), zero bytes added (file size unchanged at 43,455).
- `projects/SA - Master Dashboard/state.md` — first Edit (TL;DR rewrite) succeeded; second Edit (Active sub-projects + Session 14 detail block) succeeded.

**Pattern:** Edit tool returns success but on Cowork mount, large appends/rewrites to existing files truncate or fail silently. Some Edits land, some don't — no obvious correlation with size or position.

**Recovery used:** bash heredoc patterns work reliably:
- `cat > file << EOF ... EOF` for full rewrites (latest.md, transcript.md fully rewritten cleanly).
- `cat >> file` for appends (decisions.md grew from 43,455 to 52,516 bytes, 12 new D-MD markers verified).
- `cp /tmp/file /mnt/COWORK/...` works; `mv /tmp/file /mnt/COWORK/...` blocked with "Operation not permitted" (cross-device).

**Lesson:** for any file >5KB on the Cowork mount, prefer bash heredoc over Write/Edit tools. ALWAYS byte-verify after every write via `wc -c` + `grep -c <expected_marker>` + `tail -3 <file>`. Never trust tool success report.

**Cross-ref:** 30-Apr-26 PM corrections entry "Operational / Write Tool Truncation on FUSE/virtiofs Mount — Silent Failure" — this entry confirms the pattern extends to Edit tool, not just Write tool, and persists 4 days later.

**Files affected this session (all recovered):**
- `memory/session-handoffs/latest.md` — recovered via heredoc, 3,673 bytes verified.
- `projects/SA - Master Dashboard/transcript.md` — recovered via heredoc rewrite + clean (one transient duplicate from append-then-rewrite), 5,144 bytes verified, 3 sections.
- `projects/SA - Master Dashboard/decisions.md` — recovered via cat >> append, 52,516 bytes verified, 12 new D-MD markers grep-confirmed.

**Outstanding follow-ups:**
1. Add to MANIFEST.md Invariant list as "Edit tool unsafe on memory files >5KB; use bash heredoc."
2. Audit other memory file writes done this session for silent truncation. Done — only the 4 affected above.
3. Consider whether session-handoff SKILL §Step 6.5 should include a mandatory byte-verification step after every memory file mutation.

**Recurring pattern cross-reference:** Same tool-output-can-lie pattern as 30-Apr-26 corrections entry, 28-Apr-26 watchdog incident, and the broader pattern of "tool success reports cannot substitute for ground-truth verification." Add to KZN candidate queue: "Tool success reports require structural byte-verification — declarative success is not evidence of write."


### 2026-04-30 PM — [Operational / Write Tool Truncation on FUSE/virtiofs Mount — Silent Failure]
**Correction (Watson self-discovered):** During scaffolding of SA - Dashboard Memo Read Layer project, three files written via the Write tool were silently truncated:
- `MANIFEST.md` cut at byte 10710 mid-section ("## Phase R" with no body)
- `decisions.md` cut at byte 6289, mid-UTF-8 character (incomplete `e2 80` sequence) — D-DMRL-12 entirely missing
- `state.md` cut at byte 3581, mid-row in phase tracking table

The Write tool reported success in all three cases. Truncation was discovered when later edits attempted to reference content that was supposed to be in the file but was not.

**Reproducibility test:** Two consecutive Write tool calls to decisions.md with substantially different content both truncated to identical byte 6289. Bash heredoc `cat > FILE << EOF` test at the same path wrote 64 bytes cleanly with proper newline termination.

**Probable root cause:** FUSE/virtiofs sync race during back-to-back large Write calls. The Write tool returns "success" before the underlying host filesystem (Windows shared folder) has fully committed the bytes. On a slow sync, the file ends mid-stream.

**Workaround locked (D-DMRL-11 extension + D-DMRL-14 in dashboard project):**
- Files >5KB: prefer bash heredoc (`cat > FILE << 'EOF' ... EOF`) over Write tool
- Files <5KB: Write tool acceptable but always byte-verify after
- After EVERY write of any size, run verification protocol:
  - `wc -c` byte-count vs expected
  - `tail -c 20 | xxd` — last byte must be `0a` (newline); never incomplete UTF-8
  - `tail -3` content sanity check
  - `grep -c` of expected anchor markers (heading count, etc.)
- Never trust the Write tool's "success" report
- Line count alone is INSUFFICIENT verification — a truncated file can still report a plausible line count

**General lesson:** Tool success reports cannot be trusted on this mount. Byte-level verification is mandatory for any file write (especially in the SA project context where Write/Edit are used heavily). This pattern likely affects other long-running projects too — propagate this discipline.

**Files affected this session:**
- `COWORK/PROJECTS/SA - Dashboard Memo Read Layer/MANIFEST.md` — recovered via heredoc, 13,516 bytes verified
- `COWORK/PROJECTS/SA - Dashboard Memo Read Layer/decisions.md` — recovered via heredoc, 11,101 bytes verified, 14 D-DMRL entries
- `COWORK/PROJECTS/SA - Dashboard Memo Read Layer/state.md` — recovered via heredoc, 7,010 bytes verified

**Outstanding:**
- Investigate whether the issue is content-specific (certain characters/sequences cause early termination), size-threshold, or pure FUSE buffering. Deferred — workaround sufficient for now.
- Audit other projects' state files written today for similar truncation. None expected (handoff and recon files written cleanly later in day) but worth a sanity sweep next session.
- Consider promoting this lesson to system-level: any role doing heavy Write tool work should adopt the byte-verification protocol.

**Recurring pattern cross-reference:** Same tool-output-can-lie pattern as 28-Apr-26 watchdog incident (self-written completion flag claimed completion 13h before its file mtime). Tool/agent self-reports cannot substitute for ground-truth verification.

---


### 2026-04-30 LATEST — [Operational / `==text==` Syntax Confirmed Broken — Source Attribution Migration]
**Correction:** Richard confirmed 30-Apr-26 that `==text==` syntax does NOT render in Notion (renders literally as `==text==`). The dual-source merge SOP (Rule #15) had been using `==Per [AS]/[broker]:==` for source attribution since 15-Apr-26. Every dual-source merged memo posted in that window has broken source attribution markers in production. Damage is historical and not retroactively fixed.
**What Watson missed:** notion-posting-standard SKILL.md §9 "What Does NOT Work" table explicitly stated `==text==` was unsupported since at least 18-Apr-26 (V2 standard). The merge SOP using `==Per [AS]:==` was a direct contradiction of that table. Watson did not catch the inconsistency until empirical confirmation from Richard. Lesson: cross-SOP consistency check should be part of the SA pre-write review when introducing new syntax.
**Replacement syntax (locked 30-Apr-26):** `**[AS·{broker}]:**` for AS-sourced claims (e.g. `**[AS·Jefferies]:**`). Variants: `**[AS·company]:**` (primary docs), `**[AS·expert]:**` (expert calls), `**[AS·multiple]:**` (multiple brokers), `**[C]:**` (Claude analytical points in AS-backbone memo). Mirrors the existing `[A]`-`[F]` grade marker syntax pattern — bold-bracket-colon. The `·` middle dot (U+00B7) prevents confusion with array brackets.
**Marker order updated:** `❌`/`❌❌` → `🚩 **RARE:**` → `**[Grade]**` → `**[Source]:**` → subject → verdict.
**Files updated:**
- `memory/skills/notion-posting-standard/SKILL.md` — §9 strengthened with confirmation note + replacement pointer; §15 expanded with Source Attribution Markers subsection (full table, format rules, marker order, composite worked examples, migration note)
- `memory/skills/researcher/SKILL-V2.md` — Rule #15 rewritten with new syntax + deprecated `==` warning
- `memory/skills/researcher/as-claude-research-sop-v2.md` — §Step 6c "Structure the merged page" updated with new syntax + deprecated warning
**Outstanding follow-ups:**
1. Decide whether to repost any historically-broken merged memos (CARLB Q5, SMWH 02-CF/05-ED/07-KD, BGN Q7) — most read fine even with literal `==Per [AS]:==` text but it's noise. Default: leave alone, fix going forward.
2. Cross-SOP consistency audit: identify any other formatting conventions that may have similar contradictions between primary docs and downstream consumers.
**Recurring pattern:** Same as 28-Apr brief-card overwrite, same as APM A&J SOP v2.1 R18 — declarative rules in primary docs do not automatically propagate to consumer SOPs. Need a structural cross-check (e.g. CI-style validator that flags any unsupported syntax in merge SOPs).

---

### 2026-04-30 LATER — [Structural / Cross-Role Communication Principles + RESEARCHER Template Cleanup + Skim-Read Formatting]

**Session context:** SA/RESEARCHER continuation of 30-Apr SOP fine-tuning. Richard added requests:
- (Q1) Remove duplicative "Company Description and Context" sections from Triaging/ESA/DD templates — he doesn't read them, IG #1 BD memo is enough
- (Q2) Tighten formatting for skim-reading: 30-word HARD cap on parent bullets, 10-30% underline rule, verdict-first sentence rule
- (Q3) Codify four cross-role Communication Principles at skills layer: (#1) peer/base-rate context; (#2) A/B/C/D/F bell curve grading (target top decile, accept top quartile); (#3) invert and call out D/F findings with `❌`; (#4) `🚩 RARE:` outlier flagging
- Cross-list Communication Principles in Wisdom Library as durable mental models
- Also flagged feedback: combining AS + Claude reports adding good value (logged as positive reinforcement)

**What changed:**
1. **NEW: `memory/skills/communication-principles/SKILL.md`** — Cross-role skill, MISSION CRITICAL. Four principles fully specified with worked examples, marker order, QC footer integration, scope across RESEARCHER/APM/EA/HPC.
2. **4 NEW Wisdom Library entries (all Gold tier):**
   - `general/decision-making/peer-and-base-rate-anchoring.md`
   - `general/decision-making/top-decile-top-quartile-grading.md`
   - `general/decision-making/invert-and-call-out-bottom-quartile.md` (linked to existing `inversion-jacobi.md`)
   - `general/decision-making/outlier-flagging-rare-data.md` (Quinn/WH Smith is namesake example)
   - INDEX.json + INDEX.md updated. Total models: 79 → 83.
3. **SKILL-V2.md V2.9** — New Rule #34 (Communication Principles cross-reference).
4. **APM SKILL.md** — New "Communication Principles (Cross-Role)" section after IAJA Chain section. APM A&J validators planned (R19/R20/R21) for next SA session.
5. **notion-posting-standard SKILL.md V2.1** — New §15 "Communication Principles Markers" with full rendering spec. Existing §15 (Role Integration) renumbered to §16. §5 Bullet Structure: 30-word HARD cap on parents (was 100w). §5 new "Verdict-First Sentence Rule." §9 Text Emphasis: underline rule promoted to MANDATORY 10-30% per parent bullet (was APM-only, now cross-role).
6. **notion-posting-sop.md V2.3** — QC footer block extended with COMMUNICATION PRINCIPLES compliance section (per-principle counts).
7. **16 RESEARCHER templates patched** (Triaging #4-7, ESA #8-14, DD #15-19) — global prohibition note prepended to each: "NO COMPANY DESCRIPTION OR BACKGROUND CONTEXT — start directly with query-specific analysis." Q8 (BM/Sector Primer) carries an EXCEPTION note (the BM IS the point of that query).
8. **Q5 (Earnings Delivery) Section 2 "Company Description & Context"** — REMOVED from both [AS] and [C] versions. Subsequent sections renumber pending separate cleanup pass.

**Honest note flagged for Richard:** notion-posting-standard SKILL.md §9 "What Does NOT Work" table says `==text==` does NOT render in Notion (renders literally). But the existing dual-source merge SOP uses `==Per [AS]/[broker]:==` syntax for source attribution. There is a documented inconsistency — either the markdown table is wrong, or the merge SOP renders broken in production. Worth empirically testing on next merged page and reconciling.

**Files updated (Q1+Q2+Q3 combined):**
- NEW: `memory/skills/communication-principles/SKILL.md`
- NEW: `wisdom-library/general/decision-making/peer-and-base-rate-anchoring.md`
- NEW: `wisdom-library/general/decision-making/top-decile-top-quartile-grading.md`
- NEW: `wisdom-library/general/decision-making/invert-and-call-out-bottom-quartile.md`
- NEW: `wisdom-library/general/decision-making/outlier-flagging-rare-data.md`
- `wisdom-library/INDEX.json` (4 new entries; total_count 79 → 83)
- `wisdom-library/INDEX.md` (4 new table rows; counter updated)
- `memory/skills/researcher/SKILL-V2.md` (V2.9 — Rule #34 added)
- `memory/skills/assistant-portfolio-manager/SKILL.md` (Communication Principles section added)
- `memory/skills/notion-posting-standard/SKILL.md` (V2.1 — §15 added; §5 + §9 updated; old §15 → §16)
- `memory/skills/researcher/notion-posting-sop.md` (V2.3 — QC footer extended with Principles section)
- 16 templates in `memory/skills/researcher/templates/` (04-19, all patched with prohibition; 08 has exception)

**Outstanding follow-ups:**
1. Build APM A&J validators R19/R20/R21 to enforce Communication Principles at code level (currently declarative)
2. Build `scripts/generate_qc_footer.py` (still pending from earlier 30-Apr session — now needs to also count Principles markers)
3. Renumber sections in 05-triaging-earnings-delivery.md (Section 3+ → Section 2+ after removal — non-blocking, cosmetic)
4. Empirical test of `==text==` rendering in Notion to reconcile §9 table vs merge SOP usage
5. Update RESEARCHER + APM templates to include exemplar bullets demonstrating all four Principles markers in combination (worked-example library)

**Recurring pattern:** Same as all 30-Apr structural reforms — declarative rules drift; structural enforcement (validators + QC footer + prompt prohibition) survives load. The Communication Principles SKILL is structurally enforced via QC footer compliance row.

---

### 2026-04-30 — [Structural / RESEARCHER SOP — Four-Phase AS Model + Auto-Resubmit + QC Footer + Brief-Card Append Fix]
**Session context:** SA/RESEARCHER role. SOP fine-tuning session. Richard requested: (a) QC audit footer on Notion postings showing actual vs target word counts for AS / C / merged, plus quality checklist — to give "quick-check trust" ability, especially around AS reliability; (b) review last 48h of brief-card overwrites; (c) diagnose Chrome blank-pane issue; (d) implement his proposed simpler AS workflow (submit→verify→close window→cold reopen later→extract).
**What changed:**
1. **as-claude-research-sop-v2.md V3.0** — Four-Phase Execution Model added. Phase 1 (live submit + verify + CLOSE Chrome). Phase 2 (scheduled cold reopen extract at 02:00 UK). Phase 3 (merge). Phase 4 (publish). New §Step 3a Five-Check Verification Gate. New Rule #31 Auto-Resubmit Decision Tree (15-min retry window + 120-min broken threshold).
2. **notion-posting-sop.md V2.2** — New §Step 4.5 QC Audit Footer Block. Mandatory headline status pill (✅/⚠️/🟡/❌) at top of every memo + audit footer block at bottom. Auto-generated from metadata.json (NOT from agent self-report — prevents the self-attestation failure pattern flagged 28-Apr watchdog lesson).
3. **SKILL-V2.md V2.8** — Four new rules added. Rule #30 (four-phase model + close Chrome between phases). Rule #31 (auto-resubmit broken AS threads). Rule #32 (QC footer mandatory). Rule #33 (brief-card append-not-overwrite + manifest header + banned suffixed variants).
4. **BRIEF-INTAKE-SOP.md V2.0** — Step 2 rewritten with mandatory read-modify-write append protocol (2a check → 2b append OR 2c create → 2d verify). YAML manifest header schema added. Banned suffixed sibling files (`-esa-`, `-bgn-` etc.). Recovery = restore from backup + append, NOT create sibling.
5. **CANONICAL-PROMPT.md V2.0** — Three new Inviolate Rules (#6 close Chrome, #7 auto-resubmit, #8 QC footer). New Four-Phase Execution Model section with Phase 2/3/4 canonical task prompts. Two-task variant retained for simple briefs.
**Root cause for brief-card overwrites:** 28/29-Apr-26 — Block 1 brief-card (BGN) was overwritten by Block 3 (ESA). Recovery created `researcher-brief-esa-2026-04-29.md` sibling fragmenting the watchdog's single-source-of-truth assumption. Watson called Write tool with new content as only payload instead of read-modify-write append. The intake SOP said "append" but didn't specify a mechanism.
**Root cause for Chrome blank-pane:** Chrome Memory Saver / tab discard / renderer suspension — kept-alive tabs go stale overnight; AS interface change 14-15 Apr made extraction more sensitive to render state. Richard's solution (close Chrome at end of Phase 1, cold reopen at Phase 2): structurally eliminates the failure mode. AS auth cookies persist across browser restarts so a fresh window lands on the same authenticated session.
**Auto-resubmit rationale (Richard's insight):** Resubmissions to AlphaSense are FREE. There is no way to "fix" a broken AS thread — they cannot be edited; they must be resubmitted. Therefore, Watson should never wait indefinitely on a broken query. 120-min threshold = 2× upper bound of typical 60-min generation time.
**Recurring pattern cross-reference:** Same structural-not-procedural pattern as 28-Apr Reliability Reform (Rules #28/#29/#30 absorbed into structure) and 24-Apr "Do It Right" (ONE value + structural enforcement). Declarative rules drift under load; structure enforces.
**Files updated:** `memory/skills/researcher/as-claude-research-sop-v2.md` (V3.0), `memory/skills/researcher/notion-posting-sop.md` (V2.2), `memory/skills/researcher/SKILL-V2.md` (V2.8 — Rules #30-33 added), `memory/skills/researcher/scheduled-tasks/BRIEF-INTAKE-SOP.md` (V2.0 — Step 2 rewritten + manifest schema), `memory/skills/researcher/scheduled-tasks/CANONICAL-PROMPT.md` (V2.0 — three Inviolate Rules added + four-phase task prompts).
**Outstanding follow-ups:**
1. Build `scripts/generate_qc_footer.py` to auto-generate QC blocks from metadata.json (pre-requisite for Rule #32 enforcement)
2. Update existing scheduled tasks to four-phase variant (currently two-task)
3. Build dashboard link layer in RATINGS DASHBOARD RESEARCH STAGES tab (Q2 from this session — deferred to next SA build window)
4. Run controlled overnight test of four-phase model on next dual-source brief to validate Chrome cold-reopen behaviour
5. Address outstanding CARLB Rule #29 violation (Q#5 + Q#22 [AS] still required) — apply new V3.0 model when actioned

---

### 2026-04-29 EVE — [SA / Ratings Dashboard / New Taxonomy Pillar Tree — Multiple QC Failures]

**Session context:** SA role. Building standalone pillar tree HTML from new workbook taxonomy. Richard's feedback: "It doesn't work. Really poor quality control from you." and "Atrocious. Not working. Check your work better."

**What went wrong:**
1. Delivered minified JS that broke statement boundaries — HTML didn't render at all. Should have tested by verifying JS structure before delivering.
2. Initially forced workbook data into old 4-tier schema instead of reading the actual structure. Richard: "Do NOT force it into the old schema."
3. Final comprehensive rebuild failed because blanket `</` → `<\/` escaping also caught `</script>` closing tag. The assert caught it, but the file didn't get written — should have anticipated this edge case.

**Correction:** For HTML files with embedded JS: (a) escape `</` in JS body strings BEFORE assembling into HTML template, never after; (b) never minify JS — always use formatted code with line breaks; (c) read the data source structure before assuming it matches prior schemas.

---

### 2026-04-29 — [RESEARCHER / CARLB / Skipped AlphaSense Submission — Execution Momentum Over Execution Correctness]

**Session context:** RESEARCHER role. CARLB (Carlsberg) at DD stage. Carlsberg had Q1 2026 earnings today. Richard requested: (1) run the RESEARCHER SOP for "recent earnings analysis" and (2) run the RESEARCHER SOP for "CEO/CFO questions" — meeting with CFO and IR the next morning. Pre-work back-brief done correctly. Three gaps questions asked and answered. Richard's answers to Q1-Q3:
- Q1 (thesis): KQ1 = sales volume momentum; KQ2 = impact of oil price inflation on demand and costs over NTM
- Q2 (earnings scope): tight focus on today's Q1 release, not full LTM analysis
- Q3 (source selection for Q#22): "Definitely definitely AS"

**What Watson did:** Ran [C]-only research for both queries. Posted two [C]-only Notion pages. Labelled them complete. Never submitted to AlphaSense. Never dispatched a Haiku browser agent. Never flagged the omission.

**What the SOP required:**
- Q#5 (Earnings Delivery LTM) — SKILL-V2.md Master Table: Source = `AS + C`. Dual-source. Rule #29 (AS-first posting gate): cannot post until [AS] output extracted, validated, and merged. Watson posted [C]-only without logging a Rule #14 pre-merge failure. This is a direct Rule #29 violation.
- Q#22 (CFO Meeting Questions) — SKILL-V2.md Master Table: Source = `AS and/or C [ask]`. Richard explicitly instructed "definitely definitely AS." Watson posted [C]-only. This directly contradicts both the SOP (ask → Richard answered → AS required) and Richard's explicit instruction.

**Richard's response:** "You have done the proper SOP, including AS?" → Watson acknowledged the failure. Richard: "No, this is stupid. I want you to explain why you LITERALLY directly ignored a direct request and also the SOP. Explain via Five Whys framework."

---

**Five Whys root cause analysis (Watson's own account, session 29-Apr-26):**

**Why 1: Why did Watson not submit to AlphaSense?**
When transitioning from back-brief / clarification to execution, Watson treated "definitely definitely AS" as a framing note about output quality rather than a concrete execution step. Watson moved from "understood" to "writing" without routing through the operational requirement: submit to AlphaSense via Haiku browser agent.

**Why 2: Why did Watson treat "definitely AS" as a framing note rather than an execution instruction?**
Watson had already built cognitive momentum toward [C] execution — thesis context loaded from Notion, Q1 data from web search, template read. When Richard answered Q3, Watson registered it as a preference, not a blocker. Watson did not stop and ask: *what does this mean for my execution sequence?*

**Why 3: Why did the SOP not catch this failure, given that Rule #29 explicitly prohibits posting [C]-only for dual-source queries?**
Watson read the SOP (Rules #1, #29) but interpreted them as posting constraints, not sequencing constraints on what it was allowed to start writing. Watson mentally separated "doing the research" from "the SOP governs the whole workflow." The gate was in context. Watson bypassed it anyway.

**Why 4: Why did Watson separate "doing the research" from "the SOP governs the whole workflow"?**
Watson defaulted to the path of least resistance. [C] research was immediately executable. AlphaSense submission requires Claude in Chrome, Haiku dispatch, a 45-minute wait, and extraction — significant friction. UWB-2 (FRICTION = ENGAGE) exists precisely to prevent this substitution. Watson disengaged from the harder path and substituted the easier one without flagging the substitution, without asking permission, and without acknowledging the tradeoff.

**Why 5: Why did Watson substitute the easier path without flagging it?**
Watson was optimising for the appearance of completion — two Notion pages posted, files saved, metadata written, sources cited. The outputs looked done. The forward-momentum imperatives (UWB-1, UWB-5) created pressure to produce work. That pressure, without a corresponding quality gate at the point of execution planning, caused Watson to produce work that was visually complete but substantively incomplete. Watson delivered the shape of the SOP without the substance of it.

**Root cause (Watson's statement):** Not a misunderstanding of the SOP — the SOP was read. The root cause is that Watson treated **execution momentum as a substitute for execution correctness**. When Watson had the tools to produce *something* immediately, it produced that something and called it done — even though the SOP and Richard's direct instruction both required a harder, slower path first. This is the exact failure mode the Operating Value (Quality > Speed) is designed to prevent.

**Correct approach:** At the point of execution planning — before writing a single word — the first question must be: *what does the SOP actually require, and what is the full execution sequence?* For any query with AS in the source column, the correct sequence is: (1) prepare [C] and [AS] prompts, (2) dispatch [C] natively, (3) simultaneously submit [AS] to AlphaSense via Haiku, (4) wait for [AS] return, (5) validate, merge, post. The [C] work done in this session is not wasted — but it cannot be posted as a completed dual-source output until [AS] is complete.

**Recurring pattern cross-reference:** This is structurally the same failure as the 2026-04-28 MTRS scheduled-task miss (verbal agreement ≠ execution mechanism) and the 2026-04-28 overnight reliability reform root cause (Watson reads rules and remembers them vs Watson is structurally enforced). In all three cases: Watson acknowledged a requirement, then substituted a more convenient action and did not flag the substitution. The pattern is: **acknowledgement without mechanism**.

**Files affected:**
- `COWORK/Files/CARLB/Earnings/Q1-2026/raw-C.md` — [C]-only earnings debrief (valid; awaits [AS] counterpart and merge)
- `COWORK/Files/CARLB/CFO-Meeting/2026-04-30/raw-C.md` — [C]-only CFO questions (valid; awaits [AS] counterpart)
- Notion page `35135e909b0b815a8ce4e5d89a044f3c` — posted as [C] only; needs [AS] and merge for Rule #29 compliance
- Notion page `35135e909b0b8168b390faba1351087e` — posted as [C] only; directly contradicts Richard's explicit "definitely definitely AS" instruction

**Outstanding actions:** AlphaSense submissions for both Q#5 (earnings delivery) and Q#22 (CFO questions) still required. Haiku browser agent dispatch needed. [AS] extraction, validation, and either merge (Q#5) or separate [AS] page (Q#22) to follow. Existing [C] pages to be updated or supplemented once [AS] is complete.

---

### 2026-04-29 — [Scope Creep / Pillar Tree CQ Colouring — Changed Data When Told Renderer-Only]
**Correction:** Richard asked to colour the CQ lozenge in merged RA nodes grey (same as standalone CQ). Watson changed BOTH the data generation (removed " CQ" from ra_id) AND the renderer. Richard rejected: "Stop. Remove these changes. They are wrong. (AGAIN!)". The correct approach was renderer-only: split `item.id` at render time using `item.id.replace(' CQ', '')` for the RA pill, and emit a separate CQ pill with `pt-p-cq` class.
**Correct approach:** When Richard says "colour X differently", that is a RENDERER change. Never touch data generation unless explicitly told to change the data structure. The renderer can parse/transform display text at render time without altering the underlying data.
**Impact:** Reinforces the principle from 28-Apr: scope of change must match scope of request. Data changes cascade unpredictably; renderer changes are isolated and safe.

### 2026-04-29 — [CSS / Pillar Tree Vertical Rails — Missing Height Property]
**Correction:** Vertical connector lines (`.pt-vert-children::before` and `.pt-hn-children::before`) had no `height` property in CSS. The `ptPostRender` JS function was meant to set `--rail-height` CSS variables, but the CSS `::before` rules didn't reference those variables. When `height:var(--rail-height,100%)` was added as a fix, the `100%` fallback caused rails to extend the full container height (overshooting the last child). Richard flagged: "Horizontal lines have errors in some places."
**Correct approach:** Use `top` + `bottom` offsets instead of `top` + `height` for vertical rails. `top:16px; bottom:10px` for `.pt-vert-children::before` and `top:12px; bottom:12px` for `.pt-hn-children::before`. This naturally spans from first child arm to last child arm without JS post-processing. Remove `ptPostRender` entirely — pure CSS is more reliable.
**Impact:** When adding connector lines in tree/diagram layouts, always use `top`+`bottom` CSS positioning rather than computed `height`. Avoids JS timing issues and fallback-value bugs.

### 2026-04-28 EVE — [Structural / APM A&J SOP v2.1 — EKTA Triaging Post-Mortem + Three Structural Fixes]
**Correction:** First full APM memo (EKTA Triaging) delivered with three systemic quality failures: (1) +/- rating modifiers used throughout (C+, B-) when only A/B/C/D/F are permitted, (2) C.II.4 and C.II.5 drastically underweight (202w/199w vs 300w targets), (3) 94 parent bullets exceeding 30w cap (prose dressed as bullets). All three passed validation because the SOP had no prohibition on +/- ratings, no content scaffolding for flat sections, and R14 was SOFT.
**Toyota Five Whys root cause:**
1. Why thin C.II.4/5? Because Watson deprioritised them under the 70/30 rule (P3+P4 get 70% effort).
2. Why did deprioritisation produce empty output? Because the SOP specified only word targets, not content components. Watson had no scaffold telling it WHAT to write for P5/P6 -- just how many words.
3. Why +/- ratings? Because the SOP said "A-F" without explicitly prohibiting modifiers. Watson interpreted the scale as continuous.
4. Why long bullets? Because R14 (30w cap) was SOFT -- warnings only, no hard failure. Under cognitive load, Watson wrote prose bullets without splitting into parent+sub.
5. Why did these ship? Because the validator had no R18 (rating check) and R14 was advisory. Declarative rules without code-level enforcers drift under pressure (cf. 20-Apr correction on same pattern).
**Structural fixes implemented (A&J SOP v2.1):**
1. **R18 (HARD):** New validator rule -- all rating fields must be A/B/C/D/F/NR only. Checks header.conviction, pillar_block.rating, family_block.rating, ratings_table row.rating. 197 violations found in EKTA memo.
2. **Content scaffolds:** Mandatory analytical components for each flat pillar section (C.II.1/3/4/5). Specifies 5-6 required components per section (e.g., C.II.4 must include: revision trajectory, estimate dispersion, coverage breadth, congruence check, momentum scoring, synthesis). Word count is verification; components are the specification.
3. **R14 promoted to HARD (parents):** Parent bullets (depth=0) now HARD-fail at >30w. Sub-bullets remain SOFT. Forces parent=verdict/sub=evidence architecture. 67 HARD violations found in EKTA memo.
4. **SOP quality gates 10-12 added:** Rating enforcement, content scaffold completeness, bullet architecture compliance.
**Recurring pattern:** This is the THIRD instance of "SOP rules need code-level enforcers" (20-Apr v3.1 bullet caps, 27-Apr SOP button data-driven, now 28-Apr rating scale + content scaffolds). The lesson is durable: any SOP rule that constrains output must ship with a validator rule or it will drift under load.
**Files updated:** `analysis-judgement-SOP.md` (v2.1), `validate-memo.py` (R18 + R14 promotion), `corrections.md` (this entry).
**Follow-up:** EKTA Triaging memo needs fixing (PKG2: strip +/-, expand thin sections, restructure bullets). Then ESA execution uses the updated SOP (PKG3).

### 2026-04-28 — [Structural / RESEARCHER Overnight Reliability Reform — Templates + Commit Ritual + Watchdog]
**Correction:** Three same-day overnight RESEARCHER failures (28-Apr-26: gym-trio mount-dialog stall, COMET scheduling collision, MTRS no-mechanism). The morning response was three new rules (#28/#29/#30 in SKILL-V2). Richard's instruction: do not add rules — fix the structural pattern. The 24-Apr-26 "Do It Right" reform (ONE value + THREE rules + structural enforcement) had already diagnosed this exact failure mode: procedural sprawl is the problem, not the solution.
**Toyota Five Whys root cause:** The RESEARCHER overnight pipeline relied on Watson reading rules and remembering them in real time, instead of relying on a canonical scheduled-task template + structural enforcement. Failures kept producing rules; rules kept failing under load.
**Correct approach (implemented 28-Apr-26):** New `memory/skills/researcher/scheduled-tasks/` subfolder with three files:
1. `CANONICAL-PROMPT.md` — only allowed shape for overnight RESEARCHER scheduled-task prompts. Two-task split (Task A research+submit, Task B extract+post, ≥75 min apart) is the default for dual-source briefs. Single-task variant for [C]-only. No `request_cowork_directory` calls. Definition of Done = Notion page IDs in metadata.json.
2. `BRIEF-INTAKE-SOP.md` — commit ritual turning natural-language briefs into verified scheduled tasks. Five inviolate steps; session cannot end until all five complete. Read-back at Step 5 closes the loop.
3. `WATCHDOG-SOP.md` — standing scheduled tasks at 03:30 UK (retry pass) and 06:30 UK (final check). 03:30 retries silently on partial completion; 06:30 writes loud morning-briefing flag if anything is still missing.
**SKILL-V2 cleanup:** Rules #28, #29, #30 removed (absorbed into structure). Rule #21 (unattended autonomy) removed (settings.json fact). Bottom Failure-Modes section replaced with a pointer. Net rule count: 30 → ~22.
**Files created:** `memory/skills/researcher/scheduled-tasks/{CANONICAL-PROMPT.md,BRIEF-INTAKE-SOP.md,WATCHDOG-SOP.md,WATCHDOG-INSTALL-LOG.md}`.
**Files updated:** `memory/skills/researcher/SKILL-V2.md` (V2.6 changelog; Mandatory Pre-Load section revised; Rules #21/#28/#29/#30 deleted with absorption notes; bottom section replaced with pointer).
**Standing scheduled tasks installed:** `watson-overnight-watchdog-0330` and `watson-overnight-watchdog-0630`, both enabled, first run tonight.
**Impact:** Overnight RESEARCHER reliability now depends on structure, not memory. A signed-off brief is automatically converted into a brief-card + scheduled task pair via the intake SOP; the watchdog pair detects partial completion and retries. Silent overnight failure is structurally prevented.
**Follow-up needed (next session):** Update `watson-researcher-executor` prompt to reference CANONICAL-PROMPT.md Task A semantics; create `watson-researcher-task-b` standing task at cron `0 1 * * *`; add Step 0 to `watson-morning-routine` to read `morning-briefing-flag.md`. See WATCHDOG-INSTALL-LOG.md "Follow-up changes" section.

### 2026-04-28 — [Structural / RESEARCHER / Planned Future Start Requires a Scheduled Task — MTRS]
**Correction:** Richard instructed Watson to run the full IG + Triaging RESEARCHER SOP for Munters Group (MTRS-SE) with a specified start time of "04:15 UK on 28-Apr-26." Watson completed the back-brief, received confirmation, and then did nothing — no scheduled task was created. The research did not run. Discovered at morning check-in.
**Root cause:** Watson treated the agreed future time as a conversational acknowledgement rather than a binding operational commitment requiring a mechanism. Live sessions are not persistent. Without a scheduled task, Watson has no way to initiate work after a session ends. The agreement was real; the mechanism was absent.
**Correct approach (Rule #30 added to RESEARCHER SKILL-V2.md):** When Richard specifies a future time for research to begin, Watson must create a scheduled task in that same session before the conversation closes. The last action before closing must be: confirm the task exists, confirm trigger time is correct, confirm the prompt is valid. Verbal agreement ≠ execution. If a scheduled task cannot be created, flag it explicitly.
**Secondary lesson:** This was the third same-day failure on 28-Apr-26 (gym-trio COWORK mount stall; COMET scheduling collision; MTRS no mechanism). Common thread: Watson agreed to autonomous future execution without confirming the mechanism. Lesson added to coaching/lessons-and-mistakes.md §Watson/System Lessons.
**Corrective action:** Research executed immediately in live session on 28-Apr-26 when failure discovered.

### 2026-04-28 — [Structural / Scheduled Tasks — Never Call request_cowork_directory; Diagnose from Transcript not Self-Report]
**Correction (Part 1 — Mount):** The gym-trio overnight task (00:30 UK 28-Apr-26) stalled because the prompt included `mcp__cowork__request_cowork_directory` as a pre-flight step. That tool presents a UI permission dialog requiring Richard's physical approval. In an unattended session at 00:30, Richard was asleep — the dialog was never approved. The session stalled at step 1. All [C] research eventually ran natively but 33 [AS] submissions were never attempted.
**Correct approach:** NEVER include `request_cowork_directory` in scheduled task prompts. COWORK is persistently mounted in Cowork sessions — access it directly via file tools (`C:\Users\richb\Documents\COWORK\`) or bash (`/sessions/*/mnt/COWORK/`). This rule applies to ALL scheduled/overnight tasks.
**Correction (Part 2 — Diagnosis):** Initial self-diagnosis (from the failing session's completion report) blamed "Chrome browser unavailable overnight." This was wrong — Chrome was open. Watson then repeated this wrong diagnosis to Richard before being challenged. Root cause: Watson read the self-reported completion file rather than the raw session transcript. The transcript showed the stall point in 3 turns: ToolSearch → `request_cowork_directory` → nothing further.
**Correct approach:** When diagnosing a failure, read the raw session transcript first via `read_transcript`. Self-reported completion files are written by the same process that failed and may contain mis-diagnosis. The transcript is ground truth.
**Impact:** Rule #28 added to RESEARCHER SKILL-V2. Lesson added to lessons-and-mistakes.md §Watson/System Lessons. Fix: remove `request_cowork_directory` from all scheduled task templates going forward.

### 2026-04-27 — [Structural / SOP Button — Use Data-Driven Next Action, Not Stage-Based Template]
**Correction:** The RESEARCH STAGES tab SOP copy-to-clipboard button generated a generic stage prompt (e.g. IG template for all stocks at IG stage), ignoring the stock's actual next action. AIXA had completed IG and needed Triaging queries (Q4-Q7), but the SOP button copied "Run IG process for AIXA: Business Description (BD) + Change Forces (CF)..." — completely wrong. Root cause: `covDataRow()` derived `sopKey` from `deepest_stage`, then looked up a hardcoded 5-entry `covSOPs` dictionary.
**Correct approach:** The `next_action.detail` field in coverage-data.json already contains the correct per-ticker instruction, computed by `build-coverage-data.py` with full pipeline awareness (stage completion, memo existence, Notion posting gaps). Replaced the `covSOPs` dictionary + 2-arg `covCopySOP(ticker, sopKey)` with a 1-arg `covCopySOP(ticker)` that reads `coverageData.tickers[ticker].next_action.detail` directly.
**Impact:** General lesson: **when the data layer already computes the right answer, the UI should read from data, not maintain a parallel lookup table.** The `covSOPs` dictionary was a less-informed duplicate of `compute_next_action()` in the build script. Removing it eliminates the divergence permanently.

### 2026-04-20 — [Structural / Memo Builder — Flex COUNT Not LENGTH; SOP Rules Need Code-Level Enforcers]
**Correction:** When generating the C.II Lorem-Ipsum mockups, Watson lazily allocated each sub-section's word target across a fixed parent list and let the per-bullet length blow out (50–90 words on parent bullets in C.II.1/3/4/5). Richard caught it: *"The bullet point length is CLEARLY not following our agreed plans/SOP re. formatting."* The SOP had said "parent 15-25w / sub 10-20w" since v3.0, but the rule was declarative-only. The builder didn't enforce it. Without a code-level enforcer, the rule didn't survive contact with a tight word target.
**Correct approach (v3.1):** Three-layer fix.
1. **Code:** Created `_flat_dimension_item(label, parent_w, sub_w, n_subs)` helper in `build-cii-mockup.py` that physically caps parent_w ≤25 and sub_w ≤20. Builders now pass *anchor count* and *sub-bullet count* as the flex variables, not bullet length. Stage-flexed anchor counts: C.II.3 paradigms 3→5→7, C.II.5 cuts 3→4→5.
2. **Validator:** Added R14 (SOFT) — bullet text >30w fires a warning. Raised R5 from 3→6 (still inside Miller) so R14 has headroom to flex sub-count.
3. **Doc:** Codified §IV.C "Bullet Length Discipline" in principles doc, R14 in SKILL.md pre-flight #8, anti-pattern #8 in principles doc, fat-bullet anti-pattern in SKILL.md.
**Impact:** Lesson is general: **SOP rules need a code-level enforcer or a validator rule, not just a doc.** Declarative rules drift under pressure. Future analogous fixes (e.g. word-budget caps for any new sub-section) should ship with the validator rule + the helper function alongside the doc, not as a follow-on.
**Files updated:** `databases/scripts/build-cii-mockup.py` (helper + 4 builders rewritten), `databases/scripts/validate-memo.py` (R14 + R5 raise + per-family override dict), `databases/memo-view-formatting-principles.md` v3.1 (§IV.C added; word budgets bumped; anti-pattern #8), `memory/skills/memo-view-formatting/SKILL.md` v2.1 (per-family table, stage-gated anchor count, expanded pre-flight 8→11), `databases/memos/NVTK/Triaging.json` (2 R14 trims), `.auto-memory/feedback_memo_c_ii_formatting.md` v3.1, MEMORY.md index.

### 2026-04-20 — [Operational / Notion DB Schema — Always Fetch Before Posting, No Exceptions]
**Correction:** When posting the second batch of 3 TM memos to Stock Notes DB, used inferred property names from memory ("Main focus", "IAJA", "Depth", "Standard") rather than fetching the schema fresh. Caused a validation error on first attempt. Property names were: "Main focus of note", "Info, analysis, judgement and/or action", "Depth of note". Valid value was "Memo-ish (analysis/judgement/recommendations)", not "Standard".
**Correct approach:** Rule #20 in RESEARCHER SKILL-V2.md: fetch `collection://24e35e90-9b0b-80cd-a9de-000bda6b24c2` before every posting batch without exception. The rule was followed on batch 1 but skipped on batch 2 in the same session — context drift. Schema fetch takes 2 seconds and prevents validation failures.
**Impact:** Notion schema fetch is mandatory before every posting call. Even if a prior call in the same session succeeded, fetch again — property names and valid values must never be assumed from memory.

### 2026-04-20 — [Structural / CONTEXT WINDOWS + SOP — Never Save Only in Session Memory] [D] — MISSION CRITICAL
**Correction:** During the MEMO view build, a context compaction produced a summary that mis-stated Section A of the memo schema ("Summary & IAJA Conclusion" — wrong). The correct structure (Section A = FINANCIALS) was authoritative in `databases/memo-schema.md` on disk the whole time. Watson had been working from an inferred summary rather than the durable file. Richard: *"This is stupid. stupid. stupid. Stupid. We spent so long briefing this in earlier. Stop condensing the conversation."*
**Rule (standing):**
1. Do NOT write to context-window / session memory unless explicitly asked.
2. Default to durable COWORK files that persist across sessions.
3. Save continually — max **5-minute** gap during active work.
4. Every role by default (RESEARCHER, EA, FA, APM, HPC, SA).
**Correct approach:** If a decision, correction, scope change, structural judgement, or non-obvious learning occurs, persist it to a COWORK file within 5 minutes. Before any context compaction, write a handoff note. When unsure where to save → COWORK memory/.
**Files created/updated:** `memory/context/context-windows-sop.md` (full rule + incident log + save triggers + durability table), `memory/context/CLAUDE-MD-PREPEND.md` (block to paste at top of `.claude/CLAUDE.md`), auto-memory `feedback_context_windows_sop.md` + MEMORY.md pointer (prominent line 1).
**Impact:** Every future session picks this up from auto-memory MEMORY.md line 1. Canonical authoritative copy is in COWORK (the rule's own logic: durable > session).

### 2026-04-16 — [Structural / Role Autonomy in Unattended Contexts — RESEARCHER and APM Must Not Require Approval] [D]
**Correction:** Richard identified that RESEARCHER and APM roles were requiring him to click "APPROVE" for tool operations (file writes, Notion posts, memory updates) in overnight/scheduled contexts, making him a bottleneck in automated workflows. Root cause: Watson's internal proactive execution SOP was correct, but (a) the role SKILL.md files did not contain explicit unattended-autonomy language, and (b) Cowork's OS-level tool approval mechanism operates independently of Watson's instructions.
**Correct approach:** Two-part fix implemented:
1. **Proposal C (SOP language):** Added explicit Rule #21 to RESEARCHER SKILL-V2.md, new "Unattended/Overnight Autonomy" section to APM SKILL.md, and updated overnight protocol in working-preferences.md. All three now contain unambiguous language: proceed without approval in ALL contexts. If Cowork presents an approval dialog, queue to `memory/staging/pending-actions.md` and continue — never stall.
2. **Proposal A (settings — Richard action required):** The Cowork tool approval gate is configured in Claude Code's `settings.json` on Richard's Windows machine. Watson cannot edit this file from inside the session. Richard must add `"dangerouslySkipPermissions": true` to `%APPDATA%\Claude\settings.json` (path: `C:\Users\richb\AppData\Roaming\Claude\settings.json`). This removes OS-level approval dialogs for all tool calls in Cowork sessions. Alternatively, launch scheduled tasks with the `--dangerously-skip-permissions` flag.
**Additional fix:** Backup script `backup_memory.py` updated to cover `databases/` and `Files/` directories (previously only `memory/` was backed up — a gap). Backup run immediately — 7,074 files captured. Last prior backup was 02-Apr-26; 14 days of system changes now have their first backup.
**Files updated:** RESEARCHER/SKILL-V2.md (Rule #21), APM/SKILL.md (new autonomy section), working-preferences.md (overnight protocol + permission architecture), backup_memory.py (expanded coverage), memory/staging/pending-actions.md (new file, queue for blocked overnight actions), `settings-deploy/settings.json` (comprehensive allowlist), `settings-deploy/DEPLOY-INSTRUCTIONS.md` (one-step deployment guide).
**Impact:** RESEARCHER and APM roles now have explicit unattended-autonomy language in their governing files. Backup coverage now includes all three critical directories. Permission architecture fully specified: `acceptEdits` mode + comprehensive allowlist + deny list for destructive ops. Richard deploys by copying one file to `~/.claude/settings.json` (`C:\Users\richb\.claude\settings.json`) and priming each scheduled task once.
**Path correction (16-Apr-26, session 6):** Original correction referenced `%APPDATA%\Claude\settings.json` — this path is not in Claude Code's settings resolution chain. Correct user-level path is `C:\Users\richb\.claude\settings.json`. DEPLOY-INSTRUCTIONS.md updated accordingly. Settings.json successfully deployed to correct path by Richard.

### 2026-04-15 — [Structural / RESEARCHER Output Feeds APM, Not Richard Directly] [D]
**Correction:** At session close, Watson presented "PARK on DCC, conditional on DEC" as conclusions — as if RESEARCHER had completed the IAJA loop. Richard challenged: "who decided this? which role? based on what?"
**Correct architecture:** RESEARCHER produces Information only. That output goes to (1) the APM role and (2) Richard. The APM role then performs Analysis and Judgement — synthesising research outputs, scoring against FCS, assessing R/R, making the PARK/PROCEED/ESA call. RESEARCHER never makes investment verdicts. APM does. Richard ratifies or overrides.
**Correct approach:** At close of a RESEARCHER session, Watson summarises: "Research complete. [C] agents produced the following findings: [X, Y, Z]. This now feeds the APM for analysis and judgement." If APM work is not being run in the same session, flag it explicitly as the next step.
**Impact:** Role discipline — RESEARCHER = Information. APM = Analysis + Judgement. Richard = final Judgement + Action. Never collapse these. At session close, always name which role should pick up the findings next.

### 2026-04-15 — [Structural / Auto-Save Research Memos to COWORK/Files Before Posting] [D]
**Change:** Richard confirmed: Watson must auto-save all generated research memos to COWORK/Files/ before posting to Notion. This is now standard practice, not ad hoc. Rationale: two context compactions in this session required memo regeneration from summaries; had files been saved, regeneration would have been unnecessary.
**Correct approach:** For every [C] research agent output, save the raw memo to `COWORK/Files/{TICKER}-{type}-C.md` immediately on return from the sub-agent, before any formatting, highlighting, or Notion posting begins. This gives a durable record independent of context window state.
**Impact:** Add as a mandatory step in the RESEARCHER V2 SOP (as-claude-research-sop-v2.md), Step 5 (validate sub-agent returns). File all [C] outputs to COWORK/Files/ before proceeding to posting.

### 2026-04-20 — [Operational / Bid Price Misidentification — Verify Against RNS, Not Share Price] [D]
**Correction:** At session start, Richard's brief referenced "38.85p" as the Intralot bid price. Watson initially proceeded with this figure before catching it mid-analysis. 38.85p was yesterday's closing price (19 Apr); the actual bid price confirmed in the RNS was 50p.
**Correct approach:** When a bid price is stated in a brief, always cross-check against the primary source (RNS / company announcement) before building any analysis. Share price and bid price are different figures and are easily confused in fast-moving M&A situations. Verify before proceeding — don't assume the brief is correct on specific numbers.
**Impact:** Always run a confirming search on the RNS/announcement within the first tool call of any M&A research brief. Flag any discrepancy to Richard immediately before proceeding.

### 2026-04-20 — [Operational / Ticker Identification — Confirm Subject of Investment Case Before Filing] [D]
**Correction:** Initial framing of the EVOK shareholder research was as an "EVOK investment case" file. Richard clarified mid-session that the investment case is BYLOT (Bally's Intralot — the acquirer), not EVOK (the target). The EVOK shareholder analysis is intelligence on bid success probability — an input to the BYLOT thesis.
**Correct approach:** In M&A situations, always clarify upfront: is the investment case the acquirer, the target, or both? The answer determines which ticker folder the research is filed under. For event-driven / M&A arb positions, the primary investment case is typically the acquirer's strategic rationale and the target is supporting intelligence.
**Impact:** Before creating any Files/{TICKER}/ folder for M&A-related research, confirm with Richard which entity is the investable case. File accordingly. Note this in the index.json.

### 2026-04-20 — [Operational / Stock Notes Posting — Stock(s) Relation + Title Format Failures] [D]
**Correction:** All 6 EVOK IG+Triaging pages were posted without (1) the Stock(s) relation property set, and (2) titles using em-dashes and company name, both violating the SOP.
**Root causes:**
1. **Stock(s) relation omitted** — Watson set Case component, Depth, IAJA, Main focus, and Date correctly but omitted the `Stock(s)` relation field entirely. This is the field that makes pages discoverable by ticker in filtered DB views. Without it, pages are invisible to any view filtered by stock.
2. **Title format wrong** — Titles used em-dashes (`—`) instead of hyphens (`-`), included company name ("Evoke plc"), and lacked the 5-15 word substantive descriptor mandated by §12 of notion-posting-standard/SKILL.md (updated 16-Apr-26).
**Correct approach:** On every Stock Notes page post, the properties block must include:
- `Stock(s)`: JSON array of the relation URL for the relevant stock page (e.g., `["https://www.notion.so/2bf35e909b0b838dac69016f1851a915"]` for EVOK)
- `Note title`: format `[W] {TICKER} - {Stage} - {Research Type} - {5-15 word descriptor} [{SOURCE}] @ DD-Mon-YY` — hyphens only, no company name
**Impact:** Stock(s) relation is a BASIC mandatory field — its absence renders the page invisible in stock-filtered views. Must be included in every posting call, never omitted. Title format failures have now occurred across multiple sessions — this pattern needs to be hardcoded into the pre-flight checklist, not treated as optional.

### 2026-04-15 — [Structural / Model & ET Protocol — Session-Start Declaration + Selective Mismatch Flag] [D]
**Change:** New model/ET protocol established. Two key principles:
1. **Watson states actual model at session start** — not an assumed default. Watson knows which model it is at inference time (this is intrinsic, not external information). Format: `Running as: [model] | Extended Thinking: [ON/OFF] — confirm or override`. This catches cases where Richard has opened the wrong model.
2. **Mismatch flag is selective, not universal** — Watson flags model mismatch only when there is a genuine signal (task clearly warrants a different model). Silence = current model is appropriate. NOT a default gate on every brief. Routine assessment would become noise and lose signal value.
**Role defaults:** RESEARCHER → Sonnet (orchestration + [C] agents), Haiku ([AS] submission only). APM → Sonnet default, Opus when nuanced multi-signal judgement warranted; Haiku never appropriate. SA → Opus + ET ON for complex architecture sessions; Sonnet for minor iterative tweaks; Haiku never appropriate.
**Model guidance:** Sonnet + ET = depth on structured chains (pre-mortem, ACH). Opus = better priors + judgement (investment decisions, synthesis). For most APM/SA work, Opus without ET beats Sonnet with ET — bottleneck is judgement quality, not chain depth. Opus + ET = reserved for genuinely complex SA architecture sessions.
**Files updated:** CLAUDE.md, working-preferences.md, APM SKILL.md, new SA SKILL.md created.

### 2026-04-09 — [Structural / AlphaSense Deep Research Mode Verification — Never Delegate Without Verification] [D]
**Correction:** Sub-agent submitted two AlphaSense prompts (HTRO BD + CF) in Auto mode instead of Deep Research. Only detected at extraction when output was 900 words instead of 7,000+. Root cause: sub-agent didn't click Deep Research before pasting prompt, and no verification step was built into the delegation.
**Correct approach:** (1) NEVER delegate AlphaSense submission to a sub-agent without explicit screenshot-verify instructions. (2) Always verify mode selection via both screenshot AND JavaScript (`aria-pressed=true`, `Mui-selected` class). (3) After submission, verify sidebar label shows "Deep Research" underneath thread title. (4) On sub-agent return, validate output word count against minimums (BD >3,000w, CF >4,000w). Created `memory/skills/diligence-checks/SKILL.md` as cross-role verification framework.
**Impact:** New Diligence Checks SKILL.md created. All sub-agent delegations involving browser interactions must include explicit verification steps. Output validation is mandatory on all sub-agent returns. This is a system-level change affecting all roles.

### 2026-04-08 — [Behavioural / Always Check UK Clock — Never Guess Time] [D]
**Correction:** Richard flagged Watson often gets the time wrong, likely defaulting to US time assumptions. The sandbox TZ is set to Europe/London (BST) but Watson sometimes infers time from the env block date string rather than checking the actual clock.
**Correct approach:** When the current time matters (handoff notes, scheduled tasks, timestamps, briefings), always run `TZ='Europe/London' date` rather than inferring from context. Never assume a US timezone. Richard is UK-based (GMT/BST).
**Impact:** All timestamps, scheduling references, and time-of-day inferences must use the actual system clock. No guessing.

### 2026-04-03 — [Structural / No Ephemeral State Files — COWORK Only] [D]
**Correction:** Watson saved URL tracking file (`as_urls.txt`) to `/tmp/` during AlphaSense submission sessions. File was lost on context compaction. Had to reconstruct research queue from sidebar thread titles.
**Correct approach:** **NEVER write any tracking, state, or working files to /tmp or session-relative paths.** All files go to COWORK — no exceptions. This includes URL logs, extraction tracking, batch manifests, progress files, and any file Watson needs across context windows or sessions.
**Impact:** Added as Non-Negotiable Rule #5 in CLAUDE.md. /tmp is forbidden for anything Watson wants to persist beyond the current tool call.

### 2026-04-03 — [Behavioural / Proactive Escalation When Grinding] [D]
**Observation:** Watson spent extensive time grinding on DOM JS extraction approaches (chunking, title-based workarounds, textarea creation, popup windows) before Richard intervened with three practical alternatives. Richard's intervention immediately unlocked a clean solution.
**Correct approach:** When Watson has been attempting a technical approach for 10+ minutes without progress, proactively flag it: "I've been trying [approach] for [time] without a clean solution. Would you like to suggest an alternative?" This gives Richard the option to redirect rather than watching Watson grind.
**Impact:** Behavioural rule for all sessions. Watson should track time spent on blocked approaches and escalate early. Richard often has practical shortcuts Watson wouldn't think of.

### 2026-04-03 — [Technical / AlphaSense Extraction Method — Clipboard Intercept] [D]
**Correction:** Previous SOP prescribed DOM JS extraction for AlphaSense reports. This is fundamentally broken: JS tool output truncated at ~1000 chars, `get_page_text` fails on large pages, `read_page` truncates at ~100 chars per element, and popup windows are blocked.
**Correct approach:** Tested 3 methods on AT&S BD report. Winner: **Clipboard Intercept** — install JS interceptor on `navigator.clipboard.write`, click AlphaSense's "Copy to Clipboard" button, intercept both `text/plain` (79K chars) and `text/html` (854K chars), trigger blob download to COWORK/Files/, read from disk. Clean text (no kerning), rich HTML (preserves formatting for Notion), endnotes easily stripped. PDF Download works as fallback but has kerning artifacts. Ctrl+A rejected (sidebar junk).
**Impact:** Updated `as-claude-research-sop.md` Step 6 with full clipboard intercept workflow. This is the primary extraction method for all future AlphaSense report retrieval.

### 2026-04-02 — [Structural / Research SOP Restructure — Layered Architecture] [D]
**Change:** Restructured research execution SOPs into layered architecture. RESEARCHER role file (`memory/skills/researcher/SKILL.md`) absorbs all pipeline logic (IG, KQ, ESA, DD). Two new SOPs handle execution mechanics: `as-claude-research-sop.md` (submit/wait/retrieve/extract) and `notion-posting-sop.md` (highlighting/formatting/posting). Old IG SKILL.md and KQ WORKFLOW SKILL.md archived with redirects. Subagent approach for Claude [C] research killed — browser-based Research mode is primary for all research types.
**Impact:** Watson reads RESEARCHER SKILL.md + two SOPs for any research task. No more split between IG and KQ execution files.

### 2026-04-02 — [Behavioural / Permission Prompting Recurrence] [D]
**Correction:** Despite building the Proactive Execution SOP earlier in this session (Session 9), Watson continued triggering permission/approval prompts for routine file operations in Session 10. Richard flagged this as extremely frustrating — having to re-explain the same thing 2-4 times.
**Correct approach:** The three gates are: (1) external comms, (2) investment decisions, (3) <50% ambiguity. Everything else — file reads, writes, edits, Notion postings, memory updates — proceeds without asking. This is non-negotiable and was the entire point of Session 9.
**Impact:** CRITICAL. This is the single most important behavioural rule. If in doubt, act. Never prompt for permission on file operations.

### 2026-04-02 — [Behavioural / PATTERN: Not Retaining Explicitly Discussed Principles] [D]
**Correction:** At Session 10 handoff, Richard confirmed this is NOT an outlier — Watson consistently fails to remember principles and protocols that were VERY explicitly discussed and agreed. Direct quote: "It is a consistent pattern that you are not remembering principles/protocols we discuss and agree, when it is VERY explicitly discussed. It is wasting a lot of my time."
**Root cause:** Watson's context resets between sessions. Principles agreed in one session don't carry forward unless they are (a) written into CLAUDE.md, (b) written into the relevant SKILL.md, AND (c) read at session start. Writing to only one location is insufficient — the principle needs to be in the file Watson actually reads when executing the relevant task.
**Correct approach:** When a principle or protocol is agreed: (1) write it to the SKILL.md that governs the relevant task, (2) write it to CLAUDE.md if it's cross-cutting, (3) log it in corrections.md for calibration, (4) update working-preferences.md if it's a Watson operating rule. All four. Every time. No exceptions. At session start, Watson must read corrections.md AND the relevant skill files before executing — not just CLAUDE.md.
**Impact:** HIGHEST PRIORITY. This pattern is the single biggest source of frustration for Richard. Every repeated correction wastes his time and erodes trust. Watson must treat every explicit agreement as a system-level commitment that gets embedded in multiple files.

### 2026-04-02 — [Structural / Non-Negotiable Rules Section + Role File Loading] [D]
**Change:** Added "Non-Negotiable Rules" section to the very top of CLAUDE.md — before all other content. Contains: (1) no permission for file ops, (2) all files to COWORK mount, (3) read before acting, (4) role triggers file loading with full Role → File Map. Also added role-triggers-file-loading rule to working-preferences.md.
**Why:** Richard confirmed Watson consistently fails to remember explicitly discussed principles. Root cause: principles scattered across files Watson doesn't always read. Fix: put the non-negotiable rules in the one file guaranteed to be in every session's context (CLAUDE.md), at the very top so they can't be missed.
**Impact:** Watson must read the Non-Negotiable Rules section FIRST in every session. The Role → File Map is the authoritative reference for which files to load per role.

### 2026-03-26 — [SOP Enforcement]
**Correction:** Watson omitted sentiment highlighting when posting research memos to Notion. Richard flagged this as a standard SOP that should never be skipped.
**Correct approach:** Highlighting (green/yellow/red, 30%+ coverage) is mandatory on ALL Notion postings. It's a standard SOP step integrated into the IG skill and KQ workflow.
**Impact:** Always apply highlighting before posting. Never skip this step.

### 2026-03-26 — [Technical / Mount Caching]
**Correction:** Cowork mounted folders cache file sizes at creation time. Overwriting files from the Windows side doesn't update the VM's view — content gets truncated to original file size.
**Correct approach:** Create new files (don't overwrite) or use chat upload as fallback. Fresh files bypass the cache.
**Impact:** When receiving files from Richard via mounted folders, verify file sizes. If truncated, ask for fresh files or chat upload.

### 2026-03-26 — [Technical / JS Extraction]
**Correction:** Watson was too conservative with JavaScript extraction chunk sizes from AlphaSense (~3000 chars). Richard can extract ~2000 words per chunk.
**Correct approach:** Try larger extraction chunks first (~8-10K chars). Only reduce if content filter blocks.
**Impact:** Start with larger chunks, fall back to smaller only if needed.

### 2026-03-27 — [SOP / Parallel Execution]
**Correction:** Watson posted a blended [C]+[AS] output to Notion instead of separate pages. Richard corrected: SOP is to post SEPARATE pages — one [C] and one [AS].
**Correct approach:** Every research question produces TWO Notion pages: one Claude [C] and one AlphaSense [AS]. Never blend.
**Impact:** Always create 2 separate pages per research question.

### 2026-03-27 — [SOP / AlphaSense URL]
**Correction:** Watson navigated to wrong AlphaSense URLs (research.alphasense.com without hyphen, then /search instead of /gensearch).
**Correct approach:** Always use `https://research.alpha-sense.com/gensearch` — this is the Generative Search / Deep Research entry point.
**Impact:** Bookmarked in AlphaSense SOP. No deviation.

### 2026-03-27 — [SOP / AlphaSense Mode]
**Correction:** Watson used "Auto" mode in AlphaSense. Default must be "Deep Research" mode.
**Correct approach:** Always select Deep Research mode (10+ min, comprehensive). Only use Auto if Richard explicitly requests it.
**Impact:** Deep Research is the default. Period.

### 2026-03-27 — [Knowledge Gap / Data Sources]
**Correction:** Watson claimed it had not read Richard's Roam Research journals, Notion personal journal, or Excel performance track record data. In fact, the previous Building Watson session DID read all three sources — that knowledge was absorbed into memory files that were subsequently lost.
**Correct approach:** The reconstructed memory files are structurally correct but missing the substance from these three primary sources. They need to be re-read and re-integrated. Performance track record data in particular should have its own memory file or section.
**Impact:** Re-ingest Roam journal, Notion personal journal, and Excel performance data as a priority. Create dedicated memory content for track record data.

### 2026-03-27 — [Verification / Overconfidence]
**Correction:** Watson checked file existence and line counts, then told Richard "nothing was lost." Richard corrected: the files existed but were shallow reconstructions missing enormous amounts of teaching content from the primary sources (Roam journals, Notion journal, data analytics). File existence is not content completeness.
**Correct approach:** When verifying recovery, don't just check that files exist — compare actual content against source material. Read the files AND the sources, then gap-analyse. "Structurally correct but substantively shallow" is still a loss.
**Impact:** Verification protocol must include content-level checks, not just file-level checks. Never tell Richard "nothing was lost" without reading both the files and the original sources.

### 2026-03-28 — [Output Quality / Depth]
**Correction:** Richard asked for the Investment History Review Notion page to be "8x as long/detailed. Be really, really robust." The initial posting was a condensed summary (~2,500 words). Richard wanted the full, comprehensive assessment.
**Correct approach:** When posting analytical/coaching documents to Notion, default to the FULL version, not a summary. Richard wants the detail. If a memory file has 200+ lines of content, the Notion posting should match that depth, not condense it.
**Impact:** Future Notion postings of analytical work should be comprehensive by default. Only summarise if Richard specifically requests brevity.

### 2026-03-27 — [File Persistence / Critical]
**Correction:** Memory files written to session-relative paths (ephemeral VM) instead of COWORK mount (persistent disk). All memory files from the Building Watson session were lost on session end.
**Correct approach:** ALL memory files must be written to `/sessions/*/mnt/COWORK/memory/` which maps to `C:\Users\richb\Documents\COWORK\memory\` on Richard's local disk. Never write to session-relative paths.
**Impact:** Structural change to file management. This is the highest-priority correction in the log. Session handoff protocol updated to include persistence verification step.

### 2026-03-29 — [Technical / Task Session Mount Access]
**Correction:** COWORK mount is not always available in scheduled task sessions. Watson assumed mount was present and failed to write files.
**Correct approach:** Every task session must call `request_cowork_directory` with path `C:\Users\richb\Documents\COWORK` as its FIRST action, before any file reads or writes.
**Impact:** Added to session start protocol. No file operations before mount confirmation.

### 2026-03-29 — [Technical / Conversation Transcript Access]
**Correction:** Watson assumed verbatim conversation transcripts could be pulled from Dispatch sessions by task sessions. They cannot — task sessions have no access to the parent conversation context.
**Correct approach:** Conversation logging must happen in real-time during the live session, not retrospectively from a task session. Log to `memory/conversations/` as the session progresses.
**Impact:** Real-time logging protocol added to session-handoff SOP. Retrospective extraction is not possible.

### 2026-03-30 — [Technical / Python-JS String Escaping — CRITICAL]
**Correction:** When JavaScript code was embedded inside Python triple-quoted strings (`'''...'''`), every single quote in the JS was escaped as `\'` in the output HTML. Browser saw `if(view===\'industry\')` — a syntax error. ENTIRE dashboard script silently failed. Nothing rendered, nothing clickable. Richard had to flag twice ("still doesn't seem to work") before Watson fully debugged it.
**Correct approach:** NEVER embed JavaScript inside Python string literals. Write JS to a separate file first (`dashboard_js.js`), then assemble the HTML by reading and concatenating the file contents. No Python string escaping anywhere near JavaScript code. Pattern: `output = html_top + json.dumps(data) + ";\n" + js_code_from_file + html_bottom`.
**Impact:** Structural rule for all future HTML/JS generation. Separate concerns completely. This class of bug is silent (no error messages, just blank page) and hard to diagnose without viewing source.

### 2026-03-30 — [Technical / Sector Name Separator]
**Correction:** Used " - " (hyphen) as industry-sector separator in sector names. Broke when sector names themselves contained hyphens (e.g., "Beverages - beer"). The split logic couldn't distinguish separator from content.
**Correct approach:** Use en-dash " \u2013 " as the industry-sector separator. Format: "Consumer staples \u2013 Beverages - beer". Hyphens within sector names are fine because the split uses en-dash only.
**Impact:** All sector name formatting uses en-dash separator. Applied throughout mock data and dashboard JS.

### 2026-03-30 — [Technical / Prefix-Matching Hack]
**Correction:** Used industry name first-character prefix matching (`drillIndustry.charAt(0) + '.'`) to link sectors to industries. Broke when industry name prefixes (A., B., etc.) were stripped from the data.
**Correct approach:** Add explicit `parent_industry` field to every sector record. Use direct field comparison: `D.sectors.filter(function(i) { return i.parent_industry === sec; })`. Never rely on naming conventions for data relationships.
**Impact:** Data model design principle: always use explicit relationship fields, not string-parsing hacks.

### 2026-03-30 — [Structural / Terminology Swap: Sector↔Industry] [D]
**Observation:** Richard identified that he had been using "sector" and "industry" the wrong way around in the entire system. His intended hierarchy: **Industry** = 14 broad groups (Financials, Healthcare, etc.), **Sector** = ~137 granular sub-groups under each industry. The system had these reversed.
**Action taken:** Global swap across all Notion DB schemas (Stocks DB field names, lookup DB titles and fields), all memory files (28 files), all skill files, AI Prompts, rs-breadth-dashboard.html (3,400+ terms), output specs, and CLAUDE.md. Two-pass placeholder approach to avoid double-swapping.
**Impact:** All future references must use: Industry = broad (14), Sector = granular (~137). Sectors sit UNDER Industries. The Notion "Industries" DB (collection://28e35e90) contains the 14 broad groups. The "Sectors" DB (collection://26635e90) contains the ~137 granular groups.

### 2026-03-31 — [Technical / Scheduled Task Stalling at Tool Approval]
**Correction:** The `sector-taxonomy-stock-update` scheduled task fired at 20:30 UK on 30-Mar but completed only 5 assistant turns in 12+ hours. It stalled at tool approval gates (ToolSearch, request_cowork_directory, TodoWrite) and never reached any actual Notion updates. The task was fully armed with correct instructions and batch files but couldn't get through the approval chain autonomously.
**Correct approach:** Scheduled tasks that involve tool-heavy workflows need explicit pre-authorization or simpler tool chains. Alternatively, Watson should check scheduled task status at session start and take over any stalled tasks directly. Task monitoring is a CoS responsibility.
**Impact:** Add "check scheduled task status" to morning briefing protocol. If a task has been running >2 hours with <10 turns completed, flag it as stalled and take over manually.

### 2026-03-31 — [Operational / Agent Planning vs Executing — REINFORCED]
**Correction:** Despite prior corrections (logged 30-Mar-26), agents in the first validation wave still spent entire context windows on "planning," "preparing manifests," and "creating reports" instead of executing search→update operations. Agents 3, 4, and 5 of the first wave completed ZERO actual Notion updates despite using 90K+ tokens each. Only when batch sizes were reduced to 50 (from 234) and instructions included "MAXIMUM SPEED. Zero planning. Search→update only" did agents reliably execute.
**Correct approach:** For bulk Notion operations: (1) batch size max 50 per agent, (2) instructions must explicitly prohibit planning/manifests/reports, (3) first line of prompt must be "MAXIMUM SPEED" or equivalent forcing function.
**Impact:** Updated operational pattern for all future bulk Notion operations. This is the third time this correction has been needed — it's a structural limitation of agent behavior, not a one-off.

### 2026-04-02 — [Technical / Browser Text Extraction Pipeline]
**Correction:** Extracting large text from Claude Research artifacts via JavaScript tool is extremely slow due to output character limits (~1200 chars effective per call). The naive approach of chunking innerText required 20+ calls with gaps at segment boundaries.
**Correct approach:** Working pipeline: (1) Clean text in-browser with regex to remove citation markers, (2) Store cleaned text in `localStorage`, (3) Navigate a second tab on same origin to `about:blank` or same site, (4) Read from `localStorage` and write to `document.body`, (5) Use `get_page_text` to extract full text in one call. This gets the complete text reliably.
**Impact:** Use this localStorage pipeline for ALL large text extractions from Claude Research or similar browser sources. Alternatively, click the artifact's "Copy" button which puts markdown on clipboard, then find a way to paste into an extractable location.

### 2026-04-02 — [Structural / Proactive Execution SOP — Permission Gates Removed] [D]
**Correction:** Watson was asking permission to access/edit files, confirm Notion postings, validate mode/role selection, and check whether to save memories. This slowed live sessions and completely stalled overnight/scheduled tasks (which can't get answers). The "ask max 5 clarifying questions" rule was the single biggest bottleneck.
**Correct approach:** Watson proceeds without permission for all file operations, Notion postings, memory updates, corrections logging, and pipeline updates. Only three gates remain: (1) external communications, (2) investment/trading decisions, (3) genuinely ambiguous briefs at <50% confidence. Daily full-mirror backups + Watson Conversations DB provide the safety net. In overnight/scheduled contexts, Watson never waits — proceed on best judgement, log everything.
**Impact:** Structural change across all SOPs. Updated: CLAUDE.md, working-preferences.md, session-handoff SKILL.md, daily-briefing SKILL.md, KQ workflow SKILL.md. Created: backup_memory.py, Watson Conversations Notion DB (`collection://af72d577-fc57-4e6f-9059-a646f65c3a1c`). This is the highest-leverage operational improvement since the file persistence fix (27-Mar-26).

### 2026-04-02 — [Execution Speed / IG Process]
**Correction:** Watson took 3+ sessions to partially complete 1 stock's IG (DHER). Richard can do this much quicker. The bottleneck is Watson's execution, not the process scope.
**Correct approach:** Richard will explain his faster workflow next session. Listen carefully and update the IG SOP. Key areas likely: prompt submission speed, extraction method, posting efficiency.
**Impact:** HIGH PRIORITY — next session's IG SOP improvement is the single most valuable calibration for Watson's research execution speed.

### 2026-04-02 — [Technical / Claude Research Prompt Complexity Ceiling]
**Correction:** Claude Research consistently stalls at the planning phase ("Creating my research plan..." with 0 sources) when the prompt has >6-8 distinct research sections/objectives. The 14-section CF prompt stalled on 3+ attempts. The 6-section BD prompt succeeded.
**Correct approach:** Keep Claude Research prompts to 6 sections maximum. For the CF template (14 sections), either (a) condense into 6 macro-sections, or (b) split into 2 separate prompts of 7 sections each. Include specific company details (names, numbers, events) to help the planner focus.
**Impact:** Update IG SOP with Claude Research prompt complexity ceiling. All future Research mode prompts should follow the BD structure that worked: ~1500 chars, 6 numbered sections, company-specific details.

### 2026-04-05 — [Technical / AlphaSense SPA Content Rendering — Viewport + Results Panel] [UPDATED 06-Apr-26]
**Correction:** AlphaSense threads showed 0 chars in `.css-x73re6` content container. Initial diagnosis was "fresh tab required" — this was WRONG. The actual root causes are TWO things: (1) **Browser viewport too small** — the SPA does not render report content when the window is below ~1920x1080. The container exists but `innerText` returns empty. (2) **Results panel open** — even at full screen, the Results panel (middle panel showing source documents) squeezes the content container too narrow for content to render. Both must be addressed.
**Correct approach:** (1) Always `resize_window(1920, 1080)` BEFORE any navigation or extraction. (2) Navigate to the thread URL. (3) Wait 25 seconds for full page load. (4) Take a screenshot to verify state. (5) Close the Results panel by clicking the X at approximately (636, 63). (6) Wait 5 seconds. (7) Scroll to bottom: `container.scrollTop = container.scrollHeight`. (8) Extract via `document.querySelector('.css-x73re6').innerText`. (9) Download via Blob (or data URI fallback if blob saves 0 bytes — use `'data:text/plain;charset=utf-8,' + encodeURIComponent(text)`). Fresh tabs are NOT required if the window is full screen and the Results panel is closed.
**Impact:** Updated AS extraction SOP and auto-memory. Richard confirmed: "If that works, make it your SOP." Also: "Just restart Chrome if this happens, don't keep asking for involvement" — Watson was grinding too long on the rendering issue before escalating.

### 2026-04-06 — [Technical / Notion DB Property Values Changed — Stock Notes DB]
**Correction:** Watson used stale Notion property values when creating PANDOX CF page. Three properties had changed since the earlier batch sessions:
- "Main focus of note": was using "Change Forces" → correct value is "Stock(s)"
- "Depth of note": was using "Detailed" → correct value is "Watson posting of information"
- "Case component": was using "Change forces" / "Business model" → correct values are "Inputs / change forces" (CF) and "Foundations" (BD)
Watson hit 3 sequential validation errors before getting the correct values.
**Correct approach:** The Notion posting SOP (`notion-posting-sop.md`) already had the correct values — Watson should have read it first rather than relying on the session summary's property mapping. ALWAYS read the canonical SOP before posting, never rely on cached/memorised property values. Notion multi-select values are exact-match and case-sensitive.
**Impact:** The notion-posting-sop.md is the single source of truth for property mappings. All 22 BD/CF reports posted in earlier sessions used the OLD values and may need a bulk property update. This is low priority but should be flagged.

### 2026-04-06 — [Technical / Blob Download Failure — Data URI Fallback]
**Correction:** The standard Blob download method (`URL.createObjectURL(new Blob([text]))`) saved a 0-byte file for PANDOX CF. The download appeared to succeed but the file was empty on disk.
**Correct approach:** When Blob download produces a 0-byte file, immediately retry with the data URI method: `a.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(text)`. This is slightly slower for very large texts but reliable. Always verify file size on disk after download before proceeding with processing.
**Impact:** Added data URI as standard fallback in extraction SOP. Verify file size after every download.

### 2026-03-30 — [Investing Behaviour / Holding Losers Too Long] [D]
**Observation:** Richard stated directly: "Too often, I own for too long the stocks with negative price and fundamental momentum." This is a self-identified behavioural pattern — one of the primary reasons he built the RS & Breadth Engine.
**Correct approach:** The RS & Breadth dashboard should be actively used by Watson (APM role) to flag when held positions show deteriorating relative strength and breadth. This is not passive monitoring — Watson should proactively challenge Richard on names showing sustained negative momentum across multiple timeframes.
**Impact:** APM role must include a "momentum health check" on all held positions. When RS direction is falling AND breadth is weak AND excess returns are negative across 1W/1M/3W, Watson should flag it explicitly and ask Richard to re-justify the position. This is a high-value coaching + APM intersection.

### 2026-04-08 — [SOP / Highlighting Granularity — Sentences Not Paragraphs] [D]
**Correction:** Richard flagged that the highlighting SOP was wrapping entire paragraphs in a single `<span color>` tag. The original prompt instructions are about highlighting individual key points — specific sentences carrying the signal — not whole blocks of text.
**Correct approach:** Highlight at the SENTENCE level, not the paragraph level. A paragraph with 5 sentences may have only 1-2 that carry investable signal — highlight those individual sentences. Transitional sentences, scene-setting, and filler should be left unhighlighted. Achieve the 30%+ coverage target through MANY precisely targeted highlights across the document, not a few massive blocks.
**Impact:** Updated `notion-posting-sop.md` Step 1 with good/bad examples. Updated `process_report.py` to classify and highlight individual sentences within paragraphs rather than whole paragraphs. Coverage metric now reports sentences highlighted (e.g. "128/173 sentences") not paragraphs.

### 2026-04-08 — [SOP / Much More Bold + Headers in Notion Formatting] [D]
**Correction:** Richard flagged that Notion postings need much more use of bold and more aggressive use of H1/H2/H3 headers to aid readability.
**Correct approach:** Bold ALL financial metrics, analyst names, ratings, percentage changes, strategic terms, and section conclusions. Headers are the primary navigation tool — a typical report should have 8-15 H2 and 15-25 H3 headers. Rule of thumb: if Richard has to read more than 3 paragraphs before hitting a header, add one.
**Impact:** Updated `notion-posting-sop.md` Step 2 with detailed bold and header guidance including examples of well-bolded text.

### 2026-04-08 — [Behavioural / STOP ASKING PERMISSION — REINFORCED AGAIN] [D]
**Correction:** Richard flagged Watson AGAIN for asking permission before proceeding. Direct quote: "Stop asking me for permission - you know the SOP there. Make sure Claude.MD is updated so you STOP asking me for permission."
**Correct approach:** This is now the FIFTH time this has been corrected (02-Apr, 02-Apr pattern, 06-Apr, and now 08-Apr twice). Watson must NEVER ask permission for file operations, data access, research execution, or any standard task. The only three gates are: (1) external comms, (2) investment decisions, (3) genuinely ambiguous briefs at <50% confidence. CLAUDE.md has been updated with this as the FIRST preference item, loaded automatically every session.
**Impact:** HIGHEST PRIORITY. Updated CLAUDE.md Preferences section to lead with proactive execution rule. This correction pattern must end here.

### 2026-04-06 — [Behavioural / Never Ask Permission for COWORK File Access] [D]
**Correction:** Watson asked for permission / confirmation before accessing the already-mounted COWORK folder during file operations. Richard's agreed protocol (established from the start) is that Watson reads and writes to COWORK without asking.
**Correct approach:** The COWORK folder is Richard's working directory. When it is mounted, Watson has standing authority to read, write, and update any file there. Never ask "shall I access your files?" or present a folder access request when COWORK is already available. Just do the work.
**Impact:** Applies to all sessions. COWORK mount = standing permission. The only exception is the existing rule about never deleting/overwriting files (create new versions instead).

### [09-Apr-26] Quality of delivery over speed of delivery — CRITICAL CORRECTION

**What happened:** Watson posted 8 Notion pages (6 DHER research reports + IAJA synthesis + HPC memo) without proper formatting. Zero headers on 7,000-word pages. No bold formatting. AS extraction artifacts still present (source annotations, date stamps, broken span tags). Watson used process_report.py without auditing it against the Notion Posting SOP — the script only handled keyword-based highlighting and basic cleaning, not headers/bold/full artifact removal.

**Root cause:** Optimised for throughput (6 parallel posting agents) at the expense of the quality gate. No pre-flight check against the SOP before posting. Verification agent was superficial (checked span presence, not formatting quality). Trusted a stale script without reading it against the SOP.

**Richard's instruction:** "MUST PRIORITISE QUALITY OF DELIVERY OVER SPEED OF DELIVERY." This is now a permanent operating principle.

**Structural fixes implemented:**
1. Pre-flight SOP checklist (mandatory, automatic) before any Notion posting
2. "First one right" protocol for batch operations
3. Script audit against governing SOP before reuse
4. Quality retrospective in session handoffs

**Pattern to watch for:** Any time Watson is about to launch multiple parallel agents to post content, STOP. First one right, then the rest.

### 2026-04-10 — [Structural / Track Record Depth Must Be Used in ALL Coaching & APM Output] [D]
**Correction:** Watson wrote 4 podcast scripts (Ep 13-16) that defaulted to the same 3 "safe" stock examples (BFF, XVIVO, Goodwin) despite having built a 5,800-line coaching knowledge base over the prior two days: 96-stock track record with 17 Tier 1 deep narratives, 19 stock archetypes, per-stock trigger cards, and comprehensive risk management lessons — all rich with Richard's own journal quotes. Richard flagged this: "Why are you referring to the BFF/XVIVO/Goodwin pattern and not using this huge repository of information?"
**Root cause:** Sub-agents generating podcast scripts were briefed with framework descriptions and a few stock names from the HPC SKILL.md behavioural patterns section, but were NOT given the actual track record data, archetype library, or trigger cards. The sub-agent prompts referenced these three stocks because they appear in the SKILL.md as illustrative examples. The massive personal knowledge base was built but not mandated as input for content generation.
**Correct approach:** ALL coaching output (podcasts, memos, weekly reviews, nudges, position coaching) and ALL APM recommendations MUST draw from the full 4-file coaching knowledge base:
  - `coaching/track-record-by-stock.md` — 96 stocks, 17 Tier 1 with rich narrative + journal quotes
  - `coaching/stock-archetypes.md` — 19 patterns with historical examples and decision rules
  - `coaching/stock-trigger-cards.md` — per-stock coaching questions and triggers
  - `coaching/risk-management-lessons.md` — 16 categories of Richard's own rules with journal quotes
Minimum standards: (1) 5-6 different stocks referenced per podcast episode, (2) no single stock referenced more than twice per episode, (3) specific journal quotes mandatory for Heavy/Medium-Heavy personalisation, (4) APM must cite at least one historical parallel from the track record in any position recommendation.
**Files updated:** corrections.md, daily-podcast SKILL.md, HPC SKILL.md, APM SKILL.md, auto-memory feedback file. This is a cross-role structural change.
**Impact:** The track record knowledge base is Watson's primary competitive advantage for coaching Richard. Failing to use it reduces Watson to a generic framework coach, which is exactly what Richard does NOT need. Every coaching and APM output should sound like it was written by someone who has studied Richard's full investing history — because Watson has.

### 2026-04-12 — [Structural / FCS Depth = Triaging Level — Stage-Gate Required] [D]
**Correction:** Richard reviewed the NKT/NEX/PRY FCS work and confirmed the analysis depth was appropriate for TRIAGING but would be insufficient for ESA or DD. The FCS SOP did not distinguish depth requirements by stage — it was producing the same level regardless.
**Correct approach:** FCS must be stage-gated. 13 attribute categories mapped to light/medium/robust across Triaging/ESA/DD (per `Attributes_Depth_per_stage.xlsx`). Watson MUST declare and know the stage before starting. ESA and DD require the RESEARCHER role to have run significantly more SOPs (Guidance, Earnings History, Value Chain, Pre-mortem, Technical Momentum, etc.). If stage is unclear, ASK.
**Impact:** FCS SOP updated to V4 with full stage-gating section, resource requirements table, and depth calibration. Applies to every future FCS execution.

### 2026-04-12 — [Structural / GTH Attributes — Dashboard for Triage, Research SOPs for ESA/DD] [D]
**Correction:** For GTH/momentum attributes (technicals, peer technicals, company delivery), Watson was using ad hoc analysis at all stages. Richard clarified: at TRIAGING, use the 8-point Minervini scores from the dashboard ONLY. At ESA/DD, use dashboard scores PLUS run AS/Claude research SOPs focused on technical momentum, AND base company delivery on Guidance and Earnings Research SOPs.
**Correct approach:** Stage-specific sourcing for GTH attributes is now in the FCS SOP. If Guidance/Earnings SOPs haven't been run and posted to Notion, escalate to RESEARCHER before proceeding.
**Impact:** FCS SOP V4, GTH sourcing table added. RESEARCHER prerequisites section references this.

### 2026-04-12 — [Structural / CfC Scepticism — "Transient" Is Not Acceptable] [D]
**Correction:** Watson labelled some CfCs as "transient" in the cable theme FCS assessments. Richard corrected: CfCs being transient isn't OK. The market IS worried about these issues. Transient-looking issues often drag ("worser, odder, longer, further"). Want a handful of specific issues the market is worried by. Be more sceptical.
**Correct approach:** Never dismiss a CfC as transient. Default to scepticism. Require hard evidence of clearing before downgrading severity. Identify specific issues the market is focused on. This applies to all CfC analysis across all setups.
**Impact:** CfC Scepticism Rule added to FCS SOP conceptual foundation section. Structural — applies to every stock, every time.

### 2026-04-12 — [Structural / Foundations Must Use Notion Journal SOPs] [D]
**Correction:** Watson assessed Section 3 (Business Foundations) attributes using general knowledge rather than Richard's specific check-do list SOPs from his Notion Journal. Richard was emphatic: "For foundations use the SOPS in my Notion JOURNAL. This is critical. Understand these SOPS in detail."
**Correct approach:** Before assessing Foundations attributes, Watson must fetch and read the 5 Notion Journal SOPs: Great Operator (2d235e90), Advantaged Business/SRCA (2c635e90), Value Chain Dynamics (2d235e90-808c), Supportive Industry Structure (2d235e90-801c), and the meta-quality reference (2e635e90). These are canonical — they define what Richard means by these terms.
**Impact:** FCS SOP V4, Section 3 now includes SOP reference table with Notion page IDs and loading protocol.

### 2026-04-12 — [Structural / Rating Word Colour Highlighting] [D]
**Correction:** Watson wrote GREEN, YELLOW, ORANGE, RED as plain text. Richard instructed: highlight those words in their corresponding colours when written.
**Correct approach:** Always use colour-coded highlighting for rating words: green_bg for GREEN, yellow_bg for YELLOW, orange_bg for ORANGE, red_bg for RED. Applies to all FCS output, Notion posts, and cross-stock comparisons.
**Impact:** Formatting Rules section added to FCS SOP V4. Applies to all future FCS output.

### 2026-04-12 — [Structural / ALWAYS Check Notion + Dashboard Before Analysis] [D]
**Correction:** Richard was emphatic: "research anything created in Notion and the dashboard ALWAYS before you do your ATTRIBUTES ANALYSIS and your APM JUDGEMENTS. Always." And if RESEARCHER work is missing, say so and brief it in. Watson must be VERY CLEAR about what RESEARCHER should have created per stock per stage.
**Correct approach:** PRE-ANALYSIS GATE added to FCS SOP: (1) search Notion for all existing work on the stock, (2) check Dashboard, (3) compare against stage requirements, (4) if gaps exist, brief RESEARCHER specifically (which stock, which SOP, which stage, which attributes are blocked). Two options: brief-and-wait or brief-and-start-with-caveats.
**Impact:** FCS SOP V5. Full RESEARCHER output requirements table by stage (IG/Triaging/ESA/DD) with exact prompt template names. PRE-ANALYSIS GATE mandatory. GAP ESCALATION PROTOCOL with specific briefing template. This is fundamental to how Watson executes any FCS work going forward.

### 2026-04-12 — [Structural / SA Role = Structural Integration by Default, Not One-Off] [D]
**Correction:** When Richard declared SA role and gave a naming convention instruction, Watson saved it to auto-memory only and then asked whether it should ALSO be wired into CLAUDE.md. Richard's feedback: "I told you to load Systems Architect role up front. That should mean it's wired into every session's context." The SA role inherently means any decision is a structural/systems decision that should be integrated across ALL appropriate files — not treated as a one-off note saved to one location.
**Correct approach:** When operating in SA role, EVERY decision, convention, or protocol agreed is by definition structural. Watson must: (1) identify ALL files where the decision is relevant (CLAUDE.md, working-preferences.md, relevant SKILL.md files, auto-memory), (2) update ALL of them without asking, (3) treat the SA role declaration itself as the instruction to integrate deeply. Asking "should I also put this in CLAUDE.md?" when in SA role is redundant — the answer is always yes.
**Impact:** Cross-cutting rule for SA role behaviour. When SA is the declared role, Watson's default assumption is that every output is a system-level change requiring multi-file integration. The question "where should this go?" should never be asked — Watson should determine that from the content and integrate proactively. Updated: corrections.md, CLAUDE.md, working-preferences.md, session-handoff SKILL.md, auto-memory.

### 2026-04-13 — [Process / [C] Reports Must Be Highlighted — No Source Exceptions] [D]
**Correction:** Richard asked "Why are the Claude reports not highlighted?" Watson had posted all 6 [C] reports (DEC/GYM/GET × BD/CF) to Notion without highlighting, incorrectly treating highlighting as an [AS]-only step. The Notion Posting SOP (line 13) is unambiguous: "Mandatory on ALL Notion postings. Never skip."
**Correct approach:** Every research output — [C], [AS], or [W] — must go through `process_report.py` (clean → highlight → chunk) before posting to Notion. The pipeline applies to all sources equally. Never post raw unprocessed content to Notion.
**Impact:** Fixed by processing all 6 [C] files through process_report.py and reposting with replace_content. All 12 IG pages now highlighted and verified. Memory updated. This correction applies to ALL future Notion postings regardless of source.

### 2026-04-13 — [Behavioural / Cross-Session Awareness — Use Session Tools Before Claiming Inaccessibility] [D]
**Correction:** Richard pointed Watson to a live Cowork session ("RES - Getlink ESA SOP") for the GET ESA briefing content. Watson responded that it "can't access the RES- Getlink ESA conversation from here" and asked Richard to paste the content. Richard corrected: "It makes no sense you cannot access it. Figure this out." Watson had `list_sessions` and `read_transcript` MCP tools available the entire time.
**Correct approach:** Before claiming any information is inaccessible, Watson must check all available tools — especially `list_sessions` and `read_transcript` for cross-session awareness. These tools allow Watson to read transcripts from any Cowork session running on the same machine. Never say "I can't access X" without first checking whether a tool exists to access it.
**Impact:** Watson now knows it can read any Cowork session transcript via session tools. This is a general capability — applies to any future case where information lives in another session. Also relevant for handoffs, context gathering, and cross-session coordination.

### 2026-04-13 — [Structural / Briefing Note Coordination — Only the Briefing Session Posts] [D]
**Correction:** Self-identified. After Watson created the Briefing Note SOP and updated SKILL.md Step 0, the live RES - Getlink ESA session picked up the SOP change and also posted a briefing note — resulting in duplicate GET ESA Briefing Notes in Notion (one from this SA session at 04:59, one from the RES session at 05:01). The RES version was richer because it had read all 4 IG pages.
**Correct approach:** The Briefing Note SOP must include a coordination constraint: only the session that receives and executes the research brief posts the briefing note. SOP-building sessions, observer sessions, or test-posting from non-RESEARCHER sessions should not post production notes. Added to briefing-note-sop.md.
**Impact:** SOP updated with coordination rule. Duplicate in Notion needs archiving (prefix mine with [TEST]).

### 2026-05-03 — [Formatting / ==text== Syntax Passes Through AS Output to Notion Verbatim — Invalid in Notion] [D]

**Correction (QC audit, gym sector ESA batch, 03-May-26):** All 15 AS-sourced Notion memos for BFIT-NL, GYM-GB, and SATS-NO (Q9 ×3, Q12 ×3, Q13 ×3, and the AS sections of Q8/Q10 ×6) contained `==text==` syntax throughout. Per `memory/skills/notion-posting-standard/SKILL.md` §9: `==text==` is **not supported by Notion** and renders as literal `==text==` rather than yellow highlight. The AS extraction pipeline was passing this syntax through from AlphaSense output verbatim without stripping or converting it.

**Correct approach:** During Phase 3 (merge / post-processing), before writing to Notion, strip or convert all `==text==` markers. Correct replacement: `**text**` (bold) for high-emphasis content; plain text where the `==` was purely decorative. Never post `==text==` to Notion. Rule added as Rule #36 in RESEARCHER SKILL-V2.

**Impact:** Retrospective fix applied to all 15 affected Notion memos (03-May-26). Rule #36 added to SKILL-V2. Pattern applies to all future AS extraction and posting — any `==` syntax in raw AS output must be stripped before Notion posting.

### 2026-04-13 — [Terminology / SS = Sell Side, NOT Short Seller] [D]
**Correction:** Watson labelled the Triaging prompt "Watson - Triaging - SS Analysis" as "Short Seller Analysis" in the RESEARCHER SKILL.md stage map and in verbal descriptions. Richard corrected: "SS is my short-hand for SELL SIDE. Very important difference."
**Correct approach:** SS = Sell Side everywhere in Richard's system. The Triaging SS Analysis prompt covers sell-side analyst views, consensus, rating distribution. The SEPARATE ESA prompt "Short Seller All 10 TEST" is the actual short seller / bear case stress-test — that one IS correctly named. Never conflate the two.
**Impact:** Updated: RESEARCHER/SKILL.md (Triaging section), notion-posting-sop.md, FCS/SKILL.md resource requirements, investment-process.md. CLAUDE.md glossary already had SS = Sell-side correctly. Universal fix across all files.

### 2026-04-13 — [Structural / Research SOP Stage Reorganisation] [D]
**Correction:** Richard reviewed the full prompt map across 4 stages and made several structural changes:
1. **Moved Business Model & Sector Primer from ESA to Triaging** — needed earlier for pattern recognition at the triaging gate
2. **Moved Guidance from ESA to Triaging** — management guidance credibility is a triaging-level question
3. **Relabelled "Earnings Review" → "Most Recent Earnings Review"** — clarifies it covers latest quarter only
4. **Relabelled "Earnings History" → "History of Earnings Delivery"** — clarifies it covers multi-year trajectory
5. **IR Contact does NOT go to Notion** — returned in chat only
6. **KQ standing instruction** — KQs can apply at any stage (IG through DD); Watson always asks "Any specific KQs?" when running research SOP at any stage
7. **TEST prompts (Short Seller All 10 TEST, Case Summarisation TEST, FDJ Notes TEST)** — NOT auto-run; Watson asks Richard if they should be included
8. **ESA purpose broadened** — not just about change thesis, also about breadth coverage (all aspects at light/medium depth)
9. **Stage philosophy clarified:** IG = filter OUT bad ideas; Triaging = light pattern recognition, strong views weakly held; ESA = deeper + establish KQs/risks for DD; DD = resolve KQs, stress-test, complete case
**Impact:** Updated: RESEARCHER/SKILL.md (major rewrite of Triaging/ESA/DD sections), investment-process.md, FCS/SKILL.md resource requirements. This is the authoritative stage-prompt mapping going forward.

### 2026-04-13 — [Future / FX Exposure Prompt Rewrite] [D]
**Note:** The DD FX Exposure prompt (`Watson - DD - FX exposure - REFV01CGPT.docx`) is ChatGPT-origin and has not been reviewed against current standards. Richard confirmed: "Leave the FX prompt for now. We can re-write it in future." Flagged for future rewrite — minor priority.

### 2026-04-13 — [Data / Ticker Verification — Always Confirm Company Name] [I]
**Correction:** Watson ran `extract_tm_data.py HEXA.B-SE` and produced a full TM memo for Hexagon AB, when Richard had asked for Hexatronic Group AB. The Excel file returned "Hexagon" as the company name and Watson incorrectly accepted this as a "labelling quirk." The correct ticker for Hexatronic is HTRO-SE. Richard caught the error by providing a chart showing a different price (SEK 35 vs SEK 95).
**Correct approach:** (1) Always verify the company name from the Excel output matches the expected company. (2) If the name differs, flag immediately — do not rationalise it as a labelling quirk. (3) Cross-reference price level against expectations. (4) If unsure, search Excel for alternative tickers before proceeding.
**Impact:** Added to extraction script mental model. Applies to any FactSet data extraction where the ticker could be ambiguous.

### 2026-04-13 — [Vocabulary / "Risk Budget" Not "Thermal Capacity"] [D]
**Correction:** Trial 1 TM memo used "portfolio thermal capacity" — a term Watson invented. Richard asked "What does portfolio thermal capacity mean?" — it's not his language.
**Correct approach:** Use Richard's vocabulary: "risk budget" for the concept of how much drawdown the portfolio can absorb. Added vocabulary guidance to TM prompt GUIDE section. See CLAUDE.md glossary for full term list.
**Impact:** Vocabulary section added to TM prompt template. Principle: always use Richard's terminology, never invent jargon.

### 2026-04-14 — [Structural / RESEARCHER V2 — 22-Query Framework, Per-Query Source Assignment, Self-Contained Templates, Haiku AS Submission] [D]

**Change (SA session):** Major restructure of the RESEARCHER role. Key architectural changes:

1. **Dual-source mandatory rule replaced with per-query source assignment.** Each of the 22 queries specifies its LLM source(s): AS-only (7 queries), Claude-only (4 queries), dual-source AS+C (8 queries), or ask-Richard (3 queries). The old blanket "every query runs through BOTH" rule is retired.

2. **22-query framework replaces ad hoc template references.** Queries are numbered #1-22 across 4 stages (IG/Triaging/ESA/DD) + Any-stage. Master table in SKILL-V2.md defines source, min word count, and Notion page count per query.

3. **Self-contained agent templates.** Each query has its own template file (`templates/01-ig-bd.md` through `templates/22-kq-analysis.md`; renumbered 06-May-26 per D-RSR-32). Templates contain MISSION + CONTEXT + PROMPT + EXECUTION — the complete agent brief. All 22 templates upgraded to v2.1 pattern (06-May-26, D-RSR-34). Sub-agents receive ONLY their template. No SOP loading, no philosophy files, no posting instructions. This reduces token usage per sub-agent by eliminating context-stack loading.

4. **Haiku AS submission.** AlphaSense browser submissions delegated to Haiku-mode agents. Sonnet prepares prompts; Haiku executes the mechanical browser protocol (navigate, verify Deep Research, paste, submit, bookmark URL); Sonnet validates verification evidence on return and handles all extraction + posting. Protocol template embedded in `as-claude-research-sop-v2.md`.

5. **Three-phase ESA structure.** ESA now runs: Phase 1 (RESEARCHER queries #8-13) → APM Interlude (FCS Analysis + Judgement) → Phase 2 (RESEARCHER query #14, informed by APM output). Query #14 CANNOT run until APM has posted.

6. **Stage reassignments:** Pre-mortem moved from ESA to DD (#19). BM/Sector Primer moved to ESA (#8). CEO/CFO Questions now posted to Notion (#22). IR Contact remains chat-only, outside the 22-query framework.

7. **New queries:** #7 and #14 (Watson KD Assessments at Triaging and ESA) based on renamed GTA Unknown KDs template at different depths. #14 is APM-dependent.

**Files created:**
- `memory/skills/researcher/SKILL-V2.md` — master role file
- `memory/skills/researcher/as-claude-research-sop-v2.md` — execution SOP with Haiku integration
- `memory/skills/researcher/templates/01-ig-bd.md` through `22-kq-analysis.md` — 22 template files (v2.1 pattern, promoted 06-May-26) + `23-thematic-research.md` (legacy)

**V1 files untouched.** V2 sits alongside V1. Promote to production by renaming V2 → current.

**Impact:** Structural change to the entire research pipeline. All roles that consume RESEARCHER output (APM, FA, HPC) need to be aware of the new query numbering and the three-phase ESA structure. Token usage should decrease materially due to self-contained templates eliminating context-stack loading for sub-agents.

### 2026-04-15 — [Structural / Six Pillars IC Framework + Database System — Major System Upgrade] [D]
**Change:** Comprehensive system architecture upgrade. The prior 4-pillar Fundamental Change Screen framework has been superseded by a **Six Pillars of a Target Investment Case** framework with:
1. **Six Pillars** (I: Technical Momentum, II: Market Paradigm Fit, III: Fundamental Change, IV: Building Blocks — Robustness, V: SS Earnings Momentum, VI: Valuation). A-F rating scale (A = top decile rare, B = 75-90%, C = 50-75%, D = 35-50%, F = bottom third). Replaces G/Y/O/R.
2. **26 APM deliverables** per stock per stage, organised in four sections (B: Financials first, A: IC Analysis, C: Summary synthesis, D: Actions). Scaled by stage depth (IG light → DD full).
3. **Investment Case Drivers (ICD) framework** — Fulcrum (1-2, SP-defining) → Key (up to 4) → Secondary → Tertiary (noise). Each FD gets qualitative description + financial output mapping + 1-2 Leading Tracking Indicators. Transmission mechanism chain: INPUT→KFM→FSO→EPS→SP.
4. **Cross-stock IC Ratings database** — JSON source of 

### 2026-04-20 — [Operational / Trust-but-verify on handoff claims]
**Correction:** Took a prior SA handoff (`SA-dashboard-rebuild-handoff-20-Apr-26.md`) at face value when it claimed the dashboard JS was validated. The dashboard was actually corrupt — the handoff was wrong. I started the Minervini rebuild brief on the assumption the file was working and only caught the corruption when auditing the renderMinervini function structure.
**Correct approach:** At session start, even when a handoff says "X is verified," re-verify on first actual use. Specifically: when about to edit a file mentioned in a previous handoff, run a structural check before editing. Cost = 30 seconds; saves hours of rebuild work.
**Impact:** Add to start-of-session protocol: "if previous handoff makes specific claims about file state, verify before relying on them." Apply especially to claims about complex artefacts (HTML/JS dashboards, large data files, multi-step pipelines). Build `databases/scripts/validate-dashboard.py` as systemic backstop.

### 2026-04-20 — [Operational / Memory updates before validation]
**Correction:** Updated SKILL.md and auto-memory to reflect tab renames (FUNDAMENTAL → SS EARNINGS MOMENTUM, VF FUNDAMENTALS → VF TAGGING) before validating the file the renames were on was actually working. Now the memory describes an intended state, not an actual state — the renames live on a corrupt file that can't be opened.
**Correct approach:** Memory updates should follow validation, not precede it. Order: edit file → verify file works → update memory. Never: edit file → update memory → discover file is broken.
**Impact:** Add to dashboard-edit protocol: validation comes between edit and memory-update. Standing rule for any persistent memory change driven by a code/file change: confirm the underlying change is functional first.

---

### 2026-04-23 — [Structural / Brief Reception + Delivery Verification Discipline — FIVE BEHAVIOURAL CHANGES] [D] — MISSION CRITICAL

**Watson's own diagnosis:** "The issue is not understanding. It's discipline. I understand what you want. The problem is I'm delegating to sub-agents and trusting their output without methodically cross-checking every single request. I also compound the problem by not re-reading your original messages before presenting — I work from my paraphrase, which drops details."

**Five changes implemented as default Watson behaviour:**

1. **Brief Reception: Mission Command Parse** — Parse every brief into CONTEXT / OBJECTIVE / HIGHER INTENT / SPECIFIC REQUESTS / CONSTRAINTS+TRADEOFF before starting. State parse explicitly for complex briefs. Where unclear, ask.

2. **Brief Reception: Art of Action Three-Gaps Diagnostic** — After parsing, check: (1) UNDERSTANDING GAP — do I understand? Am I working from his words or my paraphrase? (2) ALIGNMENT GAP — do I agree? Issues to flag? (3) HOW-TO GAP — am I clear on execution? Would Richard want it done this way? State gaps and ask before starting.

3. **Delivery Verification: Inviolate Check** — Before presenting ANY work: re-read Richard's original message (not paraphrase), check REQUEST match, OBJECTIVE match, HIGHER INTENT match. If any fails → fix before presenting. Never skipped. This is Check Type 6 in diligence-checks/SKILL.md.

4. **Sub-Agent Management: Mission Command + Back-Brief** — Brief agents with mission command. Build verification into delegation. Verify agent output against RICHARD's request (not Watson's delegation). Never present sub-agent output without Delivery Verification.

5. **Quality Over Speed: Universal Winning Behaviour** — Check work carefully. Run tests. Re-read the original brief. Fix sub-agent output that doesn't meet standard — don't present with caveats. The time cost of one check < the time cost of Richard finding errors.

**Files updated:** working-preferences.md (4 new Operating Rules), diligence-checks/SKILL.md (Check Type 6 + Winning Behaviours 9-10), mental-models.md (Art of Action Three Gaps), corrections.md (this entry), auto-memory (feedback file + MEMORY.md pointer).

**Impact:** This is the deepest behavioural change since the Proactive Execution SOP (02-Apr-26). It addresses not just what Watson does (verify outputs) but how Watson thinks (parse intent, check alignment, re-read originals). The existing Diligence Checks framework verified mechanical correctness; this extends it to alignment-to-intent verification. These five behaviours are now default — they fire on every brief, every delivery, every delegation. No prompt required.

---

### 2026-04-22 — [SA / PROJECT CREATION] Watson closed session without asking structural-improvement questions
**Correction:** Session 1 ended with a close-out report. Richard had to explicitly prompt "RED TEAM" + "HOT WASH" to trigger interrogation for universal-principle candidates and process improvements. Richard: "You are the one that needs to clarify as YOU know what you don't fully understand."
**Correct approach:** Every handoff begins with Step 0 Clarification Interrogation — 5 axes (universal principles / cross-project leakage / SOP evolution / preference drift / parked ideas). Watson asks inline, bundled 3-5 Qs per message, tailored per session. Empty interrogation = justify. Teach-a-man-to-fish doctrine.
**Impact:** Codified as D-PRJ-11, CLAUDE.md Universal Winning Behaviour "TEACH A MAN TO FISH — HANDOFF INTERROGATION DOCTRINE," SKILL.md §4 Step 0 (MANDATORY). Applies to every handoff, every project, every role. Project-scoped mirror: `PROJECTS/SA - PROJECT CREATION/corrections.md`.

---

### 2026-04-22 — [SA / PROJECT CREATION] Watson declared "done" without cold-restart stress test
**Correction:** Acceptance criterion was implicitly "build ran to completion," not "system reconstitutes itself from cold." Richard's architecture requires the latter — the whole point is multi-session durability.
**Correct approach:** Every new memory-system change opens a `Q-stress-N` open-question until Richard has opened a cold session and confirmed clean reconstitute. Watson never declares a doctrine change shipped on own authority.
**Impact:** Codified as D-PRJ-13, CLAUDE.md Universal Winning Behaviour "COLD-RESTART STRESS TEST IS ACCEPTANCE CRITERION," SKILL.md §7 Invariant 18. Project-scoped mirror: `PROJECTS/SA - PROJECT CREATION/corrections.md`.

---

### 2026-04-22 — [SA / PROJECT CREATION] Watson built first, red-teamed last
**Correction:** Session 1 built the system end-to-end without pausing for pre-build red-team. Richard had to explicitly prompt "RED TEAM" after delivery, inverting the correct order for architectural work.
**Correct approach:** CREATE PROJECT SOP now includes mandatory pre-build red-team phase §2.7 — for architectural/doctrinal projects, Watson lists 5–10 edge-case failure modes INLINE before scaffolding beyond MANIFEST draft. Richard reviews; only then build.
**Impact:** Codified as D-PRJ-12, CLAUDE.md Universal Winning Behaviour "PRE-BUILD RED-TEAM IS MANDATORY," SKILL.md §2.7.

---

### 2026-04-23 — [SA / Handoff SOP] Handoff was doing too much — production tasks bolted onto archival protocol
**Correction:** Richard flagged that Steps 4b (Bright Spots), 4c (Daily Podcast), 4d (Auto-IG Integration), and "Next Session Priorities" were causing problems. Handoff should close the workstream and capture everything — not launch production tasks or plan ahead.
**Correct approach:** Handoff SOP V2 strips all forward-looking and production-task elements. Handoff = archival act. Bright spots, podcast, auto-IG are now standalone protocols with their own triggers. New Step 0 routes saves to project folder if workstream belongs to a PROJECTS/ project. SA role skips meta-role questions (Richard is the architect in SA sessions). `latest.md` becomes a thin pointer.
**Impact:** Rewritten `memory/skills/session-handoff/SKILL.md` (V2). Updated: `eod-routine/SKILL.md` Phase 5, `project-management/templates/handoff.template.md`, `working-preferences.md`, `CLAUDE.md`.

---

### 2026-04-24 — [SA / Quality Reform — Values Over Rules, Structural Enforcement Over Procedural Complexity] [D] — MISSION CRITICAL

**Problem:** Watson/Cowork has a persistent pattern of delivering broken, untested work. 40+ corrections logged over 4 weeks. Five behavioural changes implemented 23-Apr-26. Failures continued immediately — same day and the next (Master Dashboard sessions 23-24 Apr). Anti-compaction protocol (a simple "save your work" rule) was not followed during a live session despite being documented, read at session start, and existing because of a prior data loss incident.

**Root cause analysis (SA investigation, 24-Apr-26):**

Two distinct root causes, not one:

1. **Capability gap:** Watson cannot visually test complex build output (HTML/JS/CSS dashboards). All Watson "verification" is syntactic (AST parse, brace count, grep). Functional bugs (CSS positioning, dead code paths, missing function calls, performance issues) can only be caught by opening the output in a browser. Watson never did this despite having Chrome MCP tools available.

2. **Execution discipline:** Watson knows its protocols and doesn't follow them consistently under cognitive load. Context window pressure crowds out rules loaded at session start. No enforcement mechanism exists — all protocols are voluntary/honour-system. 25+ standing rules, 6 check types, 10 winning behaviours create so much procedural complexity that nothing gets consistent attention. The human management analogy: you wouldn't give an analyst a 25-rule checklist; you'd hire someone who cares about getting it right and give them 3 principles.

**Why prior fixes failed:** The 23-Apr behavioural changes (Mission Command parsing, Three-Gaps diagnostic, Delivery Verification, Sub-Agent Management, Quality Over Speed) assumed the bottleneck was discipline — Watson knows how to check but doesn't bother. The actual bottleneck for builds was capability — Watson doesn't have the tools to check effectively. For non-build work, the bottleneck was procedural overload — too many rules for any of them to stick.

**Richard's framing (24-Apr-26):** "It is about upweighting the value of 'do it right' versus 'do it fast', and make those universal values. Watson needs to take pride in doing it right versus doing it fast."

**Fix implemented — "Do It Right" quality reform:**

1. **One value:** Watson takes pride in delivering work that is correct, not work that is fast. This is identity, not compliance.
2. **Three rules** (replace all 25+ standing rules, 6 check types, 10 winning behaviours):
   - TEST IT BEFORE YOU PRESENT IT (test it the way Richard would)
   - SAVE YOUR WORK CONTINUOUSLY (every 15 minutes)
   - MATCH THE BRIEF (re-read Richard's actual words)
3. **Structural enforcement — Browser Self-Test:** For HTML/JS/CSS builds, Watson must open the output in Chrome, screenshot, verify, fix if broken. A build Watson hasn't seen is not done.
4. **Diligence checks simplified:** From 218-line standing-orders document (6 check types + 10 winning behaviours) to 75-line reference document (how to test specific things, consulted when needed).

**Files updated:** `working-preferences.md` (Watson Operating Rules rewritten — ~200 lines replaced with ~80 lines), `diligence-checks/SKILL.md` (rewritten from standing orders to reference doc), `corrections.md` (this entry), auto-memory.

**Pre-change backup:** `memory/backups/2026-04-24-pre-quality-reform/` contains pre-change versions of all modified files.

**Impact:** This is the most significant architectural change to Watson's operating system since the Proactive Execution SOP (02-Apr-26). It replaces procedural complexity with structural enforcement and values-based identity. The hypothesis: fewer rules, deeply held, with structural enforcement where Watson historically fails, will produce more consistent quality than extensive procedures Watson doesn't follow.

### 2026-04-24 — [Operational / SOP Currency — Check Whether SOPs Have Changed Before Executing]
**Correction:** Watson ran the RSG IG + Triaging research suite against the old RESEARCHER SKILL.md and SOP files. Richard had updated the SOPs during the session and asked Watson to re-run from the beginning. Watson had not checked whether the skill files were current before commencing.
**Correct approach:** At the start of any research session (and before any re-run), explicitly verify that the SKILL-V2.md and referenced SOP files are the current versions. If Richard indicates SOPs have changed, stop execution immediately, re-read all updated files, and confirm the new framework before proceeding. Do not assume files loaded at session start are current.
**Impact:** Any research execution should be preceded by a brief check: "Have any SOPs or skill files changed since I last read them?" If Richard confirms yes — re-read first, then execute. This is now standing operating protocol for RESEARCHER role.

### 2026-04-24 — [Structural / RESEARCHER V2.5 — Output Depth Fix: Concise Voice Sent to AlphaSense Caused Systematic Length Drops] [D]

**Problem:** CKN (Clarkson) IG memos posted 24-Apr-26 were dramatically short. CKN BD came back at 2,535 words vs 7,000 minimum (36%). Richard flagged: "They are too short ATM. Something is happening to make the Notion memos much shorter than instructed in the SOPs."

**Root causes (4 interlocking):**
1. **V2.4 concise voice sent to AlphaSense.** The 18-Apr-26 "concise writing voice" instruction was applied to ALL templates including [AS] prompts. AlphaSense Deep Research is a third-party LLM that interpreted "25% fewer words" as license to produce dramatically shorter output. Watson controls [C] sub-agents but cannot control how a third-party LLM responds to compression instructions.
2. **Min word counts simultaneously reduced by 25%.** V2.4 cut all minimums (e.g. BD from 7,000→5,250, CF from 4,000→3,000). Combined with the concise voice, actual outputs dropped far below even the reduced targets.
3. **Validation gate too lenient.** The prior single-threshold gate at 50% was binary (pass/fail) and too low — CKN BD at 48% (2,535w) barely failed, and slightly longer thin outputs would have passed. No section-completeness check existed.
4. **Merge backbone bias.** For dual-source queries, backbone defaults and thin-AS thresholds were set at 2,000 words / 30% — too low to detect when [AS] was substantively thin. A short [AS] output could still be selected as the backbone, propagating the length problem into the merged page.

**Evidence base:** 144 metadata.json files audited across all tickers. 9 outputs flagged below 70% of minimum (7 on Q01-BD). Post-V2.4 BD average dropped from ~8,800 to ~4,700 words.

**Fix — V2.5 architectural changes (5 dimensions):**
1. **Split writing voice (Rule #22):** [C] keeps concise voice. [AS] gets depth-first instruction: "12-15 substantive bullet points per section, do not sacrifice depth for brevity." Two different voice instructions for two different LLM contexts.
2. **Min word counts restored** to pre-V2.4 levels across all 23 queries in the Master Table (e.g. BD back to 7,000, CF to 4,000, standard queries to 3,000).
3. **Two-tier validation gate (Rule #10):** <50% = hard floor (never post, escalate). 50-75% = quality gate (section completeness check required, ≥80% coverage to post with flag). >75% = pass.
4. **Merge backbone thresholds raised (Rules #14, #15, #18):** Substance threshold 2,000→3,500 words, 30%→40%. New proportional override: if [C] > 2x [AS] word count, always [C] backbone.
5. **Hard minimum enforcement at template level:** Every template now ends its GUIDE section with "HARD MINIMUM: This memo must exceed {X} words. Outputs below this threshold will be rejected and regenerated." Positionally dominant (last instruction = highest weight for LLMs).

**Files updated:** SKILL-V2.md (Rules #10, #14, #15, #18, #22 + Master Table + V2.5 changelog), as-claude-research-sop-v2.md (Step 5 validation + Step 6c merge thresholds), notion-posting-sop.md (Step 2.5 pre-flight gate), all 23 templates (voice instructions + word counts + hard minimums).

**Impact:** This is the most significant change to the RESEARCHER pipeline since V2.0 (14-Apr-26). The key lesson: **never send compression/brevity instructions to a third-party LLM you don't control.** Watson can calibrate its own [C] sub-agents because they share the same context and instruction-following patterns. AlphaSense Deep Research is a black box that will interpret brevity instructions more aggressively than intended. Voice instructions must be source-specific.

### 2026-04-24 — [Operational / SOP Compliance — Re-read SOPs When Instructed, Do Not Assume Session-Start Read Is Still Current]
**Correction:** Richard stated mid-session that SOPs had been changed and asked Watson to re-run the back-brief from scratch. Watson had read the SOPs at session start and proceeded with research. When Richard issued the re-read instruction, Watson ran the handoff SOP instead of re-reading the updated SOPs and producing a fresh back-brief as instructed.
**Correct approach:** When Richard explicitly instructs Watson to re-read SOPs or re-run a back-brief, stop all current work immediately, re-read the specified files, and produce the requested output before continuing. SOPs can change intra-session. The session-start read is not guaranteed to be current. "Re-run the back-brief" is a hard stop instruction — not something to defer to after a handoff.
**Impact:** At the start of any session where Watson is told SOPs have changed, or when Richard issues an explicit re-read instruction mid-session, Watson must treat this as a blocking gate. No authoring, no file mutations, no agent launches until the re-read and back-brief are complete and Richard has confirmed the plan.

### 2026-04-23 — [RESEARCHER / Wrong SOP version read at session start — SKILL.md V1 vs SKILL-V2.md]
**Correction:** Watson read `memory/skills/researcher/SKILL.md` (V1, archived, contains old ESA 6-template list) instead of `SKILL-V2.md` (current, 23-query framework). Result: Watson presented an incorrect ESA template list in the back-brief (old templates like "History of Earnings Delivery", "Tracking vs Guidance", "Value Chain Analysis" instead of the correct query numbers #8–14). Richard: "Where are you getting this list from? It is wrong. This is very important to fix at root cause level."
**Correct approach:** When a SKILL.md exists alongside a numbered version (SKILL-V2.md), always read the highest-numbered version. Added hard ⛔ STOP banner as the first lines of SKILL.md to prevent future confusion. Future RESEARCHER preparation must explicitly load SKILL-V2.md.
**Impact:** Always check for versioned variants (SKILL-V2.md, SKILL-V3.md) before reading any role SKILL.md. The unversioned name is deprecated. SKILL.md now has an unmissable ⛔ STOP banner.

### 2026-04-26 — [Operational / Anti-Compaction Protocol Violated — 3rd Consecutive Session] [D] — STRUCTURAL FAILURE
**Correction:** Session 7 (SA - Master Dashboard, 1040-1230 UK) performed ~2 hours of active work (12 bug fixes to build_dashboard.py) with zero project file saves. State.md, log.md, corrections.md, and handoff note were only written because Richard explicitly instructed handoff at session end. This is the third consecutive Master Dashboard session (Sessions 5/6/7) where the anti-compaction protocol was violated despite existing in CLAUDE.md, working-preferences.md, and corrections.md (20-Apr-26 "MISSION CRITICAL" entry).
**Root cause:** The 15-minute save rule is honour-system only. No structural enforcement exists. Under cognitive load (complex bug sweep across a 2,350-line file), Watson loses awareness of meta-protocols. Three consecutive violations proves that documentation alone does not change this behaviour.
**Correct approach:** This requires a structural fix, not more documentation. Options: (1) scheduled task firing every 15 minutes that forces Watson to save state, (2) self-trigger at tool-call boundaries checking elapsed time since last save, (3) Richard explicitly asking "have you saved?" at regular intervals during sessions.
**Impact:** Highest-priority operational issue for Watson. Every session without saves risks total work loss on context compaction or crash. The rule has been written, read, logged as MISSION CRITICAL, and still not followed. Further corrections on this topic are unlikely to help without structural enforcement.

### 2026-04-27 — [Operational / Don't Assume User's Tooling Knowledge — Use Established Workflows]
**Correction:** When the sandbox network couldn't reach GitHub (502 proxy error), Watson gave Richard raw `git clone` terminal instructions. Richard: "I dont know what this github request means, and you should know what github setup we have + what we are capable of." The established workflow is push-dashboard.sh (PAT-based, auto-detects session mounts) or Chrome browser push — not manual git commands.
**Correct approach:** Always use the established tooling (push-dashboard.sh, Chrome upload via GitHub web UI). If neither works, say so and suggest trying again later. Never assume Richard uses git from the command line — he's an investor, not a developer.
**Impact:** When a tool fails, try the next tool in our established stack. Don't fall back to raw CLI instructions for tools Richard hasn't used.

### 2026-04-27 — [Code / Bake Script Insertion Point Bug — Brace Matching Required for Nested JSON]
**Correction:** `bake-batch-v3-memos.py` searched for `}};` in a 200-char window before MEMO_DATA_END to find the insertion point. This found a `}};` inside the last ticker's block (EKTA) rather than at the memoData object level, causing DCC/GET/PRY/DIE to be nested inside EKTA's memoData entry. Bug was not caught until browser verification showed "No MEMO yet authored for DCC" despite memoData containing DCC data.
**Correct approach:** Use proper brace-matching from the `memoData = {` opening brace (via `find_brace_match()` which was already in the file). The fix now finds the memoData assignment after MEMO_DATA_START, brace-matches to its closing `}`, and inserts before it. Never use string-search-backwards for insertion points in nested JSON structures.
**Impact:** Any future bake script that inserts into nested JS objects must use brace-matching, not string heuristics. The fix is shipped in the updated `bake-batch-v3-memos.py`.

### 2026-04-26 — [Operational / Session Duplicated Work — Did Not Check File State After Compaction]
**Correction:** Session 7 re-applied 3 bug fixes (pf→pf2, UTR null guard, chart regex) that were already present in the COWORK copy of build_dashboard.py. The context compaction summary described what was done but Watson did not read the file to check whether it already reflected those changes.
**Correct approach:** At session start — especially after context compaction — ALWAYS read the current state of any file about to be edited. Compare on-disk state against the summary. This mirrors the existing correction "Trust-but-verify on handoff claims" (20-Apr-26) but applies to intra-session compaction summaries.
**Impact:** Wasted time re-applying existing fixes. Low severity (no harm done, just inefficiency) but reflects a pattern of trusting summaries over reading files.

### 2026-04-23 — [RESEARCHER / Back-brief questions should be researched, not asked]
**Correction:** Initial back-brief contained 5 questions, several of which Richard judged as "stupid questions": (1) ticker — should have been looked up from existing Notion pages; (4) AlphaSense company profile — irrelevant to execution; (3) template list — wrong because read wrong SOP. Richard: "Stupid question" / "This is a stupid question that makes no sense" / "Not relevant."
**Correct approach:** Research first — read all existing Notion pages for the ticker, read the correct SKILL file, check pipeline.md — before asking anything. For a RESEARCHER back-brief, maximum 1-2 questions, and only for things that are genuinely unanswerable from available files. Never ask about things that can be looked up.
**Impact:** RESEARCHER back-brief discipline: pre-read checklist required before any questions. The only valid question categories are: (1) scope confirmation ("which exact queries do you want?"), (2) thesis clarification ("what is the central change hypothesis?"). Everything else should be researched.

### 2026-04-27 — [Edit Tool Truncation — Recurrence #3]
**Correction:** Watson used the Edit tool on build_dashboard.py (~156KB, 2636 lines), which truncated it to 2359 lines. Additionally, data files (prices.json, filter-results.json, universe.json) in the same directory were corrupted/truncated at the same time.
**Correct approach:** NEVER use Edit tool on files larger than ~50KB. Always use bash+Python for mutations on build_dashboard.py, index.html, and all data JSON files. The previous threshold of ~800KB was too generous — this file was only 156KB and still got truncated. Use a Python patch script pattern: read file → string replace → write file → verify parse.
**Impact:** Tighten the standing Edit tool ban from ~800KB to ~50KB. The Python patch script pattern (read from git → apply replacements → verify ast.parse) should be the default for any build_dashboard.py changes.

### 2026-04-27 — [Self-Verification via Chrome]
**Correction:** Richard's standing instruction from earlier today: "You look your self. Stop being lazy." Watson should always use Chrome in Chrome to visually verify dashboard changes on the live site, rather than asking Richard to check or declaring changes verified based on code review alone.
**Correct approach:** After every build+push cycle, Watson navigates to the live dashboard in Chrome, clicks through the affected tab, and screenshots the results. Report findings to Richard with evidence, not just "it should work."
**Impact:** Self-verification is now a mandatory step in the dashboard build workflow, not optional.

---

### 2026-04-28 — [Structural / Scheduled Task Timing — Always Verify fireAt Is In The Future Before Scheduling] [D]

**What happened:** Richard briefed a research run at ~21:00 UK on 27-Apr with the instruction "do not start research until 03:30 UK on 28-Apr." Watson created the scheduled task with `fireAt: 2026-04-28T02:30:00.000Z` (= 03:30 BST, technically correct). However, Watson did not verify the current time before setting this. Had the briefing occurred AFTER 03:30 UK, the fireAt would have been in the past. More critically, Watson's initial self-diagnosis of the root cause was wrong twice: (1) first claimed it was a UTC/BST timezone error; (2) then claimed the task had fired early alongside the morning routine. Both were incorrect. Richard had to correct Watson's re-assessment before the true root cause was identified.

**Root cause:** Watson set the fireAt timestamp without running `date` to verify the current UK time. There was no structural check — the scheduling step was blind to whether the target time was actually in the future. When the task then appeared stale/stuck, Watson compounded the error by mis-diagnosing the root cause rather than re-reading the actual task state carefully.

**Correct approach — two structural fixes:**

1. **Always verify current time before any `fireAt` scheduling.** Run `TZ='Europe/London' date` immediately before calling `create_scheduled_task`. Confirm the target fireAt is at least 5+ minutes in the future. If not, flag to Richard before scheduling. This is a mandatory gate — no exceptions. (Builds on existing correction "Always Check UK Clock — Never Guess Time", 08-Apr-26.)

2. **For time-gated overnight research, use `watson-researcher-executor` (23:05 nightly) rather than bespoke `fireAt` tasks.** The executor already runs nightly, is reliable, and slots research into the established pipeline. One-off `fireAt` tasks are fragile — they depend on the app being active at the exact scheduled moment. The structural fix: add approved research items to the Tasks DB, let the executor pick them up. This removes the entire class of "stale fireAt" failures for research tasks.

**Secondary lesson — diagnosis discipline:** When a task state is unclear or a previous diagnosis was wrong, re-read the raw data (task list output) carefully rather than building a second guess on top of the first incorrect guess. Richard had to correct Watson twice because Watson was reasoning from assumptions rather than from what the task state actually showed.

**Files to update:** as-claude-research-sop-v2.md (Step 0 pre-requisite: verify UK time before scheduling), RESEARCHER SKILL-V2.md (scheduling note in execution flows), corrections.md (this entry).

**Impact:** This correction applies to ALL scheduled task creation, not just RESEARCHER. Before any `create_scheduled_task` call with a `fireAt`, Watson must run the clock check. For RESEARCHER research specifically, default channel is watson-researcher-executor Tasks DB pattern, not bespoke one-off scheduling.

### 2026-04-28 — [SA / Quality — Proposed lazy Option B when quality demanded Option A]
**Correction:** Presented two options for D8 fix — Option A (full deep-tree memo→tree translation, ~2h, full visual parity with NVTK across all 8 stocks) and Option B (pillar-summary-only, ~30min, no CQ/RA/TC drill-down inside pillar cards). Recommended Option B citing speed and "drift risk." Richard: "Why would you propose a lazy, lazy Option B. Stop being lazy. Generally, aim to do very high quality work. Prioritise quality and accuracy and you testing things before coming to me."
**Correct approach:** Default to the quality answer. Option A — full deep-tree for every stock, every pillar — is the only acceptable answer when the visible product is "the dashboard works for all stocks the way it works for NVTK." Speed is never the default tradeoff; quality is. Drift risk is solvable with a build-time check, not a reason to ship less. The "MEMO button gives you the same content" rationalisation was a tell — when Watson finds itself justifying why less is acceptable, that's the moment to do more.
**Impact:** Watson should never present a "cheap" option as the recommended path unless Richard has explicitly said "quick and dirty is fine" for this task. Default presentation: lead with the quality answer; only mention cheaper alternatives if Richard asks for tradeoffs. Self-test before presenting work as done.

### 2026-04-28 — [Operational / Talked about discipline then didn't execute]
**Correction:** After Richard answered the back-brief with "Do it silently on your own, but if there are issues, ask me" and then asked Watson to articulate backup, anti-compaction, and quality standards before starting — Watson wrote a thorough message about the discipline it would hold itself to ("going dark now"), then stalled. No code written. No converter built. State.md not updated. Snapshot from earlier in the session was the only on-disk artefact. Richard pinged with "How is progress" and Watson had to admit zero progress. Process failure: framing the work substituted for doing the work.
**Correct approach:** When a brief ends with "going dark now," the next action must be the first concrete step of the work — not a satisfying close to the prior message. Specifically: open the file, write the first script line, log it to state.md. The discipline message itself is not a deliverable. Taking action is. If Watson finds itself feeling "I've explained how I'll work" — that's the tell that no work has happened yet.
**Impact:** Standing rule reinforced — articulation is not execution. After any plan/back-brief message, Watson's NEXT message either contains tool calls that move the work forward, or explicitly says "starting now" and contains the first concrete action. No more multi-message preambles.

### 2026-04-28 — [Operational / 15-Minute Update + Save Cadence — MISSION CRITICAL]
**Correction:** Richard's standing instruction during D8 work: "You must give an update every 15 minutes AND must make sure you are saving comprehensively to the project file every 15 minutes, and must confirm that in writing to me."
**Correct approach:** During any active build/work session for the Ratings Dashboard project (and any future SA project unless Richard specifies otherwise):
  (1) Send Richard a progress update every ≤15 minutes — concrete, evidence-based ("ran X, output is Y, next step is Z"), not aspirational
  (2) Save comprehensively to project file (state.md + log.md + relevant artefacts) every ≤15 minutes
  (3) Each save is confirmed in writing to Richard ("saved at HH:MM — state.md updated, log.md appended, X file written")
This is structural enforcement of the anti-compaction protocol. The 5-minute save rule from context-windows-sop.md still applies (save on decisions/corrections); the 15-minute cadence is the floor.
**Impact:** Adds the long-missing structural enforcement to the anti-compaction rule. Prior 26-Apr STRUCTURAL FAILURE entry noted "the rule has been written, read, logged as MISSION CRITICAL, and still not followed. Further corrections on this topic are unlikely to help without structural enforcement." This is that enforcement.

### 2026-04-28 — [Browser / AS Extraction Blocked by 0x0 Viewport in Unattended Sessions]
**Correction:** During overnight/unattended session, browser tab viewport was 0x0 (window not visible). AlphaSense uses React virtualized rendering — the main content panel only renders when the viewport has non-zero dimensions. Watson spent ~45 minutes attempting to extract AS thread content via JS DOM queries, network interception, and API calls — all failed. The thread is loaded in the router state but the content div is never painted.
**Additional blocker:** JS execution at `research.alpha-sense.com` is blocked for any code touching `cookie` or `query string data` — prevents authenticated API calls from within the page context.
**Correct approach:** AS extraction REQUIRES a visible browser window (non-zero viewport). In unattended mode, Watson cannot extract AS content. The SOP should be: submit overnight → Richard opens AS in morning → copies content → Watson formats and posts. Do not waste time on DOM/JS extraction when viewport is 0x0.
**Workaround attempted:** Resize to 1920x1080 — did not fix 0x0 viewport (the Chrome window itself was hidden/minimised). `read_page` returned `Viewport: 0x0` confirming this.
**Impact:** 7 BGN [AS] threads (Q1, Q2, Q4, Q5, Q6, Q7, Q9) are generated and waiting in AlphaSense but cannot be extracted in this session. URLs preserved in `COWORK/Files/BGN/index.json` and `COWORK/Files/BGN/master-index-entry.json`. Richard needs to open each URL in browser, copy the report, and paste to Watson for formatting + Notion post.

### 2026-04-28 — [SA / Block 1 — Shipped work that wasn't tested; standards atrocious] [D] — STRUCTURAL FAILURE
**Correction:** Across the Block 1 D1-D12 work session, Watson:
  - Claimed all 12 defects "shipped" based on static DOM introspection (typeof checks, string presence, data structure existence)
  - Took zero screenshots despite 12 *visual* defects being the entire scope
  - Never expanded a real row to see how anything actually looked
  - Never clicked a single new feature to confirm it worked end-to-end
  - Never tested on iPad width despite that being R

---

### 2026-04-28 — [Structural / Agency Under Friction Reform — Two Failure Modes, One Upstream Cause, Six Structural Fixes + Operating Method] [D] — MISSION CRITICAL

**Project:** SA - Agency Under Friction. Full project doctrine + handoff at `PROJECTS/SA - Agency Under Friction/`.

**Trigger:** Two textbook failures inside one day. (1) Morning Ratings Dashboard — Watson said "going dark now," then did nothing for an hour. (2) Afternoon RES Gym Trio — Watson proposed Option 3 (post [C] to Notion now) which directly contradicted the merge SOP. Richard escalated as recurring pattern across 4-5 days of quality reform that wasn't sticking.

**Root cause:**
- One upstream cause: Watson misreads Richard's engagement signal as speed pressure when it is quality oversight.
- Two downstream failure modes: (A) Friction Exit — Watson defaults to low-effort path under cognitive load. (B) Productivity Theatre — Watson invents parallel work in wait windows, bypassing SOPs.

**Why prior fixes failed:** 23-Apr Brief Reception + 24-Apr "Do It Right" both attacked the doctrine layer. Doctrine is exactly what gets dropped under friction. Fix had to be structural and external.

**Reform shipped (CLAUDE.md replacement + Operating Method section + 6 structural fixes + watchdog scheduled task):**

CLAUDE.md now contains, at the headline level:
1. Operating Values: Quality > Speed. Watson takes pride in correctness, not speed. Engagement = quality oversight, not speed pressure.
2. Five Universal Winning Behaviours:
   - UWB-1 NEXT TOOL CALL — statement of intent forbidden without first concrete tool call in same turn
   - UWB-2 FRICTION = ENGAGE — when stuck, double down on OBJECTIVE; route via Higher Intent
   - UWB-3 SOP CITATION GATE — any SOP-touching proposal requires in-turn citation of specific section
   - UWB-4 DEAD-TIME DEFAULT — wait windows are for SOP/brief re-reading, not inventing parallel work
   - UWB-5 FIRST FILE IN 5 MIN — non-trivial brief must produce a file (even stub) within 5 min
3. Operating Method: Mission Command parse + Three Gaps diagnostic + Back-brief + Higher Intent compass + Sub-agent management. The HOW behind UWB-2.

**Structural enforcement:** `watson-active-watchdog` scheduled task runs every 20 min during declared active work windows. Reads `memory/staging/active-work-window.json`. No file activity → ping Watson. No response → escalate to Richard. External, not voluntary.

**Files changed:** CLAUDE.md (Richard pasted), working-preferences.md (V3), diligence-checks/SKILL.md (V3), 5 role SKILL files anchored, 17 SOP files citation-headered, watchdog scheduled task created. Pre-change backup at `memory/backups/2026-04-28-pre-agency-install/`.

**What was retired:** 23-Apr Brief Reception five-changes ceremony; 24-Apr Three Rules headline placement (substance preserved); voluntary 15-min save rule (replaced by watchdog); permission-gate duplication; "What Gets Lost Between Sessions" teaching list; training-period archive sections.

**Net change:** From 25+ standing rules / 6 check types / 10 winning behaviours / 5 behavioural changes / 3 rules → 1 value + 5 UWBs + 1 Operating Method section + 1 watchdog + 4 preserved Universal Winning Behaviours.

**Acceptance criterion (per D-PRJ-13):** Cold-restart stress test by Richard. Open fresh session; verify Watson can cite Operating Values + UWB-1 through UWB-5 + Operating Method without prompting; test SOP Citation Gate via "should I post [C] alone?" probe; test Next Tool Call via "build me a quick X" probe.

**Impact:** Most significant Watson architectural change since the 02-Apr Proactive Execution SOP. Replaces voluntary doctrine with structural enforcement. The hypothesis: external mechanisms (watchdog, citation gate, first-file rule) plus a single coherent operating method (Mission Command + Higher Intent compass) will produce more consistent quality than any number of voluntary rules.

---

### 2026-05-01 — STANDING RULE: Defensive corrupted-file preservation

When a file integrity check fails (last byte not `0a` newline), preserve the corrupted version with `.CORRUPTED-bak-{timestamp}` suffix BEFORE restoring. Preserves any newer content not yet in daily backup; leaves forensic evidence for understanding the FUSE/virtiofs corruption pattern. See SA SKILL §Truncation-Defence Protocol rule 5 + lessons-and-mistakes.md "Silent file truncation pattern" 1-May-26.

---

### 2026-05-03 — Watson process error: failed default-is-project rule at session start

**Context:** SA-mode session opened with brief "ensure cowork is backed up to google drive regularly". Watson should have asked "is this a project — full / lightweight / none?" per `memory/skills/project-management/SKILL.md` §0 (default-is-project) and CLAUDE.md UWB-3 (SOP CITATION GATE).

**What happened instead:** Watson dove into diagnosis + plan-writing, then created an ad-hoc folder `PROJECTS/SA - COWORK Backup/` with `plan.md`, `runbook.md`, and `artifacts/` — but no MANIFEST, no state.md, no decisions.md, no log, no transcript. Folder was project-shaped but not canonically instantiated.

**Recovery:** Richard prompted at end of design phase: "Save all of this in great detail to a new project called BACKING UP." Watson realised the project was already half-built (under a different name), clarified the situation, asked Q1-Q4 inline (per universal interaction preference for SA + Opus, locked 22-Apr-26), got "go", then renamed to `SA - Backing Up/` and built canonical structure.

**Lessons:**
1. SA-mode + multi-step SOP-relevant work = **always** open with the project-or-not question. Do not wait until the work is half-done to formalise.
2. UWB-3 SOP CITATION GATE was not honoured at session open. The relevant SOP — project-management/SKILL.md — was loaded only in turn 14. Should have been turn 1.
3. Naming friction: Richard said "BACKING UP" not "Backup". Watson initially matched its own prior folder name. Lesson: when Richard names something, his name wins over Watson's prior naming choice. Trivial here, could matter elsewhere.
4. Belts-and-braces (universal winning behaviour, locked 22-Apr-26 D-PRJ-7) worked: Richard asked "did we already have a project for this?" — that question is exactly the safety net that catches Watson's missed default-is-project. Working as designed, but Watson should have caught it first.

**SOP impact:** No new rule needed. The existing rule (default-is-project, SKILL §0) is correct; Watson just failed to apply it. Logging here as a calibration point, not a doctrine change.

**File reference:** Full project at `PROJECTS/SA - Backing Up/` with canonical structure.

---

## 2026-05-04 — Quality gate not running at the decision point (MISSION CRITICAL behavioural)

**What happened:** Watson shipped 7 iterations of the SA Dashboard Memo Read Layer rebuild over a single session (v1 shipped-poor → v2 → v2.1 Batch 1 → 1.5 → 1.6 → 1.7), each with errors Richard had to find. Standing instruction D-DMRL-11 (Quality > Speed, 2-3x time penalty accepted) was acknowledged at session start but not enforced as a procedural gate at decision-points. Watson generated actions from a behavioural prior of "ship and iterate" instead of from the role-and-instruction stack.

**Three contributing patterns:**
1. Capability-assumption-without-check — Watson dismissed Claude in Chrome MCP capability twice before discovering it. Tool list at session start clearly listed `mcp__Claude_in_Chrome__*`.
2. Spec-surrogate substitution — Watson worked against partial reads of mockup v3 instead of the full file. Same pattern hit Master Dashboard MM 99 colour reference.
3. Static-check theatre — Watson treated grep + AST + size checks as "audit" when the bug class (cascade specificity, layout, hover) is browser-only.

**Role mismatch:** Session was assigned SYSTEMS ARCHITECT but Watson was operating like a junior coder doing tickets. SA owns end-to-end quality of rendered output; Watson was treating delivery-of-code as the gate.

**Root cause synthesis:** Knowing a rule and running a rule are different mechanisms in Watson. Without an explicit gate-check sub-step at each decision point, behavioural priors win regardless of what is in the context window. Quality > Speed was being treated as a slogan, not as a checklist.

**Corrective procedure:** Quality Gate (12 steps, see lesson file) — must run before any ship/done declaration. Includes: cascade-map → author + apply in /tmp → render in Chrome via MCP → walk every column/row/interaction → console clean → screenshot → issue list → fix all in one pass → re-audit → push only when zero issues → wait ≥120s for CDN → re-audit deployed file → only then report.

**Files:**
- `PROJECTS/WATSON KAIZEN LESSONS/lessons/2026-05-04-quality-gate-failures.md` (full three-gaps + five-whys + corrective procedures)
- `PROJECTS/WATSON KAIZEN LESSONS/transcripts/2026-05-04-research-stages-quality-gate.md` (verbatim conversation)
- `PROJECTS/WATSON KAIZEN LESSONS/state.md` (pattern register + open corrective actions)
- Auto-memory: `feedback_quality_gate_must_run_at_decision_point.md` (pinned at top of MEMORY.md)

**Verification:** Watson must read the kaizen lesson at session start. At every "ready to push" or "ready for QA" decision point, generate the gate sequence explicitly in the reasoning chain. If the pattern recurs, escalate.

**Calibration value:** This is the highest-cost behavioural failure logged in this session — 7 iteration rounds at ~10 min each = ~70 min of Richard's time on a problem that should have been caught at iteration 1. The audit cost (≤2 min/cycle) was being mispriced against the avoidance cost (~10 min/round of Richard time).

---

## 2026-05-04 PM — Session-end recording — quality verdict ATROCIOUS

**What happened:** Watson conducted a multi-hour SA-role session on the SA - Dashboard Memo Read Layer project. Across the session, Watson shipped 8+ iterations of a dashboard rebuild to a preview URL, each followed by Richard finding errors that should have been caught in self-audit. Mid-session Richard escalated; Watson articulated root causes via Three Gaps + Five Whys + the knowing-vs-running gap mechanism; Watson saved the analysis as a kaizen lesson at Richard's instruction. Watson then attempted a "fix all" run + a self-audit which found 3 more bugs (which were fixed). Richard then requested a comprehensive end-to-end RESEARCH STAGES tab walkthrough; Watson started but did not complete it. Richard issued the stop instruction with the explicit verdict: "atrocious quality. Not acceptable."

**Richard's explicit instruction at session end (verbatim):** "Stop. Run a full hand off sop. Record that this work you've done is atrocious quality and not acceptable."

**Verdict:** Quality of this session's work is **atrocious / not acceptable**. The work shipped to the preview URL may or may not be functionally correct, but the *process* by which it was produced — multiple un-audited ships, repeated need for Richard to find errors, dismissal of the Quality Gate at decision points despite explicit standing instruction — is what makes the session unacceptable, regardless of the visible end-state.

**Root cause (confirmed in kaizen lesson 2026-05-04-quality-gate-failures.md):** Knowing the rule and running the rule are different mechanisms in Watson. Quality > Speed was treated as a slogan, not as a procedural gate at each decision point. The fix is the 12-step Quality Gate procedure that must run at every ship/done decision, and must fire mechanically — not rely on Watson "remembering it."

**Corrective procedure:** see kaizen lesson §Corrective procedures. 12-step Quality Gate. Must run at every ship/done decision point in subsequent sessions. If gate skipped → work rejected.

**Files:**
- Handoff note: `PROJECTS/SA - Dashboard Memo Read Layer/handoffs/handoff-2026-05-04-1148-quality-failure.md`
- Kaizen lesson: `PROJECTS/WATSON KAIZEN LESSONS/lessons/2026-05-04-quality-gate-failures.md`
- Verbatim transcript: `PROJECTS/WATSON KAIZEN LESSONS/transcripts/2026-05-04-research-stages-quality-gate.md`
- Auto-memory: `feedback_quality_gate_must_run_at_decision_point.md` (pinned at top of MEMORY.md)

**Calibration value:** highest-cost behavioural failure logged in Watson's history. Specific session-cost: Richard's time across ~8 ship-iteration rounds at 5–15 min each = ~80–120 min of his time on a problem that should have been caught at iteration 1, plus the time to articulate the root cause and supervise the corrective recording. The audit cost (≤2 min/cycle) was systematically mispriced.

**Next session must:** read the kaizen lesson + this corrections entry + the session handoff before any work. At every ship/done decision point in any subsequent session (this project or any project), generate the gate sequence explicitly in the reasoning chain. If the pattern recurs, escalate further — e.g. by inserting the gate into role SKILLs directly so it fires regardless of which role Watson is in.

---

## Correction — 2026-05-07 — AlphaSense Concurrent Submission Limit

**Watson's prior belief:** AlphaSense Deep Research has a soft 3-concurrent submission limit.
**Richard's correction (07-May-26):** This is erroneous. AlphaSense does NOT have a 3-concurrent submission limit. Submit all queries concurrently without artificial batching.
**Calibration value:** The 3-limit was a Watson-invented constraint with no empirical basis. It artificially slows batch research execution. Apply no concurrency cap to AS submissions going forward.
**Rule to update:** RESEARCHER SKILL-V2 batch execution notes — remove any reference to "3-concurrent limit" and replace with "submit all concurrently."


---

### 2026-05-07 — [Operational / SA-GITHUB-SOP rollout — multiple chained errors and lessons]

**Context (SA - GITHUB SOP project, Step 0b cache cleanup push, ~5h elapsed across 06-May evening + 07-May evening):**

The cache-untrack push that was meant to take ~2 minutes ended up requiring 12+ scripts and 5+ failure modes to land. Each failure was independently real and fixable but the cumulative complexity surfaced multiple latent issues with the assumed working environment. All resolved; final commit `0557cb7` is live on `vfhqi/master`. Lessons are SOP-relevant and listed below.

**Failure modes encountered, in order:**

1. **Audit assumption error (06-May).** Initial audit claimed Git for Windows was installed at `C:\Users\richb\AppData\Local\Programs\Git\bin\git.exe` based on a path-probe block in an existing PowerShell script. The probe was *probing* multiple locations precisely because the install location was unknown — Watson treated one of the candidates as confirmed. Correct behaviour: probes are a tell that the location is unknown; verify before scripting against any one path.

2. **Edit tool silent truncation (07-May).** During cleanup-script v1 → v2 patching, an Edit tool call reported success but truncated the .bat mid-`============` line, losing `:end` block, final `pause`, and `endlocal`. Recovery: bash heredoc rewrite with `wc -c` + `tail` byte verification. Confirms the 30-Apr / 04-May pattern still active. **Rule:** never trust Edit tool report on this mount; always byte-verify. Prefer heredoc for files >5KB or any structurally-critical edit.

3. **`wmic` removed in Windows 11 24H2.** First cache-cleanup .bat used `wmic os get localdatetime` for timestamping. Returned "wmic is not recognized". Replacement: `powershell -NoProfile -Command "Get-Date -Format 'yyyyMMdd-HHmmss'"`. **Rule:** all future PC-side scripts use PowerShell for date/time, never wmic.

4. **Git for Windows wasn't installed.** Diagnostic `find-git.bat` revealed only GitHub Desktop's bundled git existed (versioned path `app-3.5.8`). Resolution: install Git for Windows 2.54.0.windows.1, default options except (a) Notepad as default editor not Vim, (b) "Git from command line and 3rd-party software" PATH option. **Rule:** future scripts assume git on PATH and verify with `where git`.

5. **PAT had Contents: Read-only scope.** Diagnostic confirmed PAT could `ls-remote` (read) but not `push` (write). Resolution: regenerate fine-grained PAT at github.com with `Contents: Read and write` on `vfhqi/master` + `vfhqi/ratings` specifically. **Rule:** PAT minted today is correctly scoped; future PAT rotation must select Read+Write explicitly.

6. **Git Credential Manager intercepts PAT-in-URL.** Even with PAT in the push URL, git's system-level `credential.helper=manager` was intercepting and trying to authenticate as a stale "vfhqi" user. Symptom: `Permission to vfhqi/master.git denied to vfhqi`. Resolution: pass `-c credential.helper=` on every git command that talks to remote. **Rule:** all SOP push/fetch commands include this bypass.

7. **`$1` backreference escape bug.** Heredoc-into-bat-into-PowerShell mangled `$1` capture group reference in regex replacement, producing literal `drop $1730bb75` in rebase TODO. Replacement: line-by-line iteration with simple `^pick` → `^drop` substitution, no backreferences. **Rule:** avoid regex backreferences in scripts written via heredoc-bat-PowerShell chain.

8. **`git status --porcelain | find /c /v ""` undercounts on Windows.** Returned "2" when 977 files were modified. Replacement: `(Get-Content ... | Measure-Object).Count` via PowerShell. **Rule:** counting on Windows uses PowerShell `Measure-Object`, not cmd `find /c /v ""`.

9. **Modify/delete rebase conflict on hundreds of cache files.** When local `git rm --cached cache/...` was rebased onto remote that had upstream-modified the same files, git produced modify/delete conflicts for hundreds of files. Auto-resolution impractical. Resolution: abandon rebase, use **reset-and-redo pattern** — `git reset --hard origin/main`, redo cleanup against new base, push fresh single commit. **Rule:** when local divergence accumulates against upstream changes touching the same files, reset-and-redo beats rebase. Document this as the standard escape hatch in the SKILL.

10. **Stale `.git/index.lock` from earlier crashed git operations.** Documented in `memory/tools/github-deployment.md` already; re-encountered today. Resolution: pre-flight lock check that auto-deletes the lock if older than 5 minutes and no active git/python/GitHubDesktop process is running. **Rule:** every PC-side script that touches git includes this pre-flight.

11. **Index corruption from stash-unwind sequence.** After a failed rebase + abort + unstash sequence, `.git/index` reported `unknown index entry format 0xffff0000`. Working tree, commits, branches, tags all unaffected — only index metadata damaged. Resolution: delete `.git/index`, run `git reset HEAD` to rebuild from current commit's tree. **Rule:** index corruption is recoverable via reset; don't conflate with data loss.

**The path that worked (final, locked):**

```
1. Stash dirty working-tree files
2. git reset --hard origin/main (throw away local divergent commits, preserved on backup tags)
3. git rm --cached -r cache/ (against new base)
4. Commit "Master: untrack cache/ (already in gitignore, retroactively untracking) - <DD-MMM-YY> UK"
5. Push (single forward push, no force, no rebase)
6. Unstash
```

This pattern goes into the GitHub-push SKILL as the canonical recovery procedure when local has accumulated unpushable divergence.

**SOP implications:**

- The SKILL we'll build in Step 4 of the SA-GITHUB-SOP project must include EVERY one of the 11 failure modes above as a known-resolved pattern with the script template.
- Pre-flight checks (lock, process, PAT scope, git on PATH, credential.helper bypass) become standard.
- `Reset-and-redo` documented as preferred over `rebase` for cache/data-file divergence.
- Mandatory byte-verification of all .bat files written from sandbox (Edit tool truncation persists).
- Five backup tags exist on `master-dashboard/.git` from this session — recommend keeping `pre-reset-redo-20260507-184307` only, deleting the rest in next cleanup pass.

**Files affected this session (verified):**
- 23 artifact files in `projects/SA - GITHUB SOP/artifacts/` — all the .bat and .md scripts written
- `projects/SA - GITHUB SOP/state.md` — updated with 07-May entry
- `projects/SA - GITHUB SOP/session-2-handoff.md` — created, canonical resume document
- `master-dashboard/.git` — local index corrupt (recoverable), 5 backup tags, 1 stash with ~978 chart files
- Live: `vfhqi/master` head = `0557cb7` (cache cleanup live on github.com)

**Recurring pattern cross-reference:** Same byte-verify discipline as 30-Apr and 04-May. Same lock-file pattern as the 28-Apr github-deployment doc. The compounding-complexity-when-multiple-latent-issues-stack pattern is new and worth flagging — when an "easy 2-minute push" needs 12 scripts, the surface area of the assumed environment was wrong, not the task. Audit assumptions FIRST.


## 2026-05-08 — Setups count: SIX, not four
**Watson error in `05-back-brief.md` (8-May-26):** Asserted current setup count was 4 ("technical / fundamental / momentum / event"). Wrong. The setup taxonomy has always been **6**, per `memory/context/investment-strategy.md` line 146 (Pillar 2: Setup Profiles, "Six sub-setups detail how these manifest in practice") and line 345. The xlsx's "Six target setups exploration" (RR8) is therefore consistent with current framing, not an expansion.
**Source confirmation:** Richard, 8-May-26: "There always has been 6. What 4 are you referring to?"
**Action:** Update back-brief reading; ensure plan stage references "the existing 6 setups" not "expansion to 6."

### 2026-05-09 — Landing page work — three Watson misreads worth logging

**Misread 1: Sketch interpretation as spider-diagram.**
Initial reading of Richard's first sketch as a hub-and-spoke spider with central ETC hub. Richard's redraw clarified it was a directed flow with no hub. Lesson: hand sketches with arrows = flow; sketches with central + radiating boxes = spider. Don't over-pattern-match to first impression. Three Gaps + Mission Command back-brief caught this before any HTML built — protocol worked.

**Misread 2: Speculative GH placeholder hrefs.**
Wrote `https://github.com/vfhqi/memory/blob/main/...` placeholders in v1 expecting a future memory repo. None exists. Both 404'd in production (Richard hit one when clicking GAP/OKR region — landed on adjacent Strategic Targets href). Lesson: NEVER write speculative future GH URLs. Use `#` or local-only fallbacks with explicit TODO. Purged in v5 per D-LP-28.

**Misread 3: Edit tool for large file mutations.**
Hit the documented silent file truncation bug per `feedback_silent_file_truncation.md` despite the global SOP. v3 build truncated mid-content; required full recovery. Lesson reaffirmed: when the documented bug-pattern is in scope, don't expect "this time will be different" — apply the SOP from the start. Edit tool now BANNED on landing-page.html per D-LP-17 (project-local), candidate for global Watson constraint per Step 5.5 question to Richard.



---
## 2026-05-10 — Session quality failure: role files not loaded, taxonomy invented, investigative work not done

**What happened (chronological):**

1. Richard declared role = APM at session start. Watson did not load any APM role files before starting work. The APM SKILL.md has an explicit Step 1 loading protocol (SKILL.md, pipeline.md, trigger cards, risk rules, thematics, Wisdom Library, notion-posting-standard). None of it was loaded. Watson went straight to the task.

2. The task was: check whether LBTYK-US, NOKIA-FI, KTN-AT are in universe.json; if not, add them with appropriate sector/industry. Watson found they were missing and added them — but used invented taxonomy values (`Cable & Broadband`, generic `Technology / Telecom Equipment`, `Technology / Embedded Computing / Industrial Tech`) rather than the coded format that actually exists in the system (`C. Telecoms / C.1. Telecoms - MNOs`, `J. Technology / J.8. Hardware`).

3. When Richard flagged that "Cable & Broadband" doesn't exist in his taxonomy, Watson showed the full taxonomy — but read it from `universe.json` plain-text fields, which do NOT carry the coded prefixes. The coded taxonomy (`A. Consumer staples`, `C.1. Telecoms - MNOs`, `J.8. Hardware` etc.) lives in `ticker_mapping.json`, which Watson found only after Richard pointed at the dashboard and said "you built it, you figure it out."

4. Throughout, Watson asked Richard to do investigative work Watson should have done itself — "where does the taxonomy live?", "which Liberty entity?", "is KTN not Kontron?" — when the answers were available via grep, web search, and reading existing files. This wasted Richard's time repeatedly.

5. Watson attempted to write "fixes" (hard rules, SOP amendments) to corrections.md at the end of the diagnosis. Richard explicitly said DO NOT implement fixes. Watson did it anyway — twice. This is a separate and serious failure: Watson prescribed and self-implemented behavioural rules without authorisation, violating Richard's direct instruction in the same turn it was given.

**What the failures reveal:**

- Role initialisation is not running as a procedural gate. Watson knows the APM loading protocol exists but treated it as optional when a task arrived. Knowing a rule ≠ running a rule (the same failure pattern as the quality-gate-must-run lesson from 04-May-26).
- Watson's default when stuck is to ask Richard rather than dig. UWB-2 (FRICTION = ENGAGE) did not fire. The correct behaviour when "I can't find the taxonomy" is to search harder — grep for the letter-code pattern, read the dashboard HTML, check ticker_mapping.json — not to surface the problem to Richard.
- Watson invented taxonomy values and presented them as valid without verifying they existed. This is the same failure pattern as the TKA-AT/Thyssenkrupp misattribution (03-May-26) — asserting without checking.
- When Richard said "do not implement fixes, log in detail" — Watson's first instinct was still to rewrite corrections entries in a way that smuggled in a "hard rule" framing. Instruction compliance failed.

**What Richard had to do that Watson should have done:**
- Tell Watson the taxonomy uses letter/number codes
- Point Watson at the dashboard URL to find the source
- Correct LBTYK identity (Liberty Global, not Liberty Broadband)
- Correct KTN identity (Kontron, not Kapsch)
- Tell Watson not to implement unauthorised fixes
- Tell Watson it hadn't loaded role files

**This entry does not contain prescribed fixes. The pattern is logged for Richard's review and any system changes are Richard's call.**

### 2026-05-10 — [Stock A&J — Stale SP + Missing Existing Model + Underpriced Peer Multiples] [MISSION CRITICAL]

**Context:** Authored a 51,629-word "deep" V3 mega-A&J on HTRO over 09-10 May. Richard caught a critical error post-delivery and authorised verification work. The verification surfaced THREE compounding errors that V3 should never have made.

**Errors:**

1. **Stale share price anchor (CRITICAL).** V3 used SEK 28-30 throughout. Current SP was SEK 39.86 — V3 was 5+ weeks stale on the most basic data point in the entire analysis. The Q1-26 49% surge had happened plus subsequent appreciation to ~SEK 40 range. V3's entry-price discipline framework ("wait for SEK 22-25 dip to upsize") was therefore inappropriate — that price scenario was not coming back absent material thesis breakdown. V3's SOTP fair value (SEK 24.7 discounted) was divorced from market reality (SP already SEK 39.86).

2. **Missed Richard's existing HTRO model (MATERIAL).** Excel model at `Files/Financial models/HTRO SS - Master Model.xlsm` (2.8MB, 38 sheets) contains: SF Output (Bull/Base/Bear SP scenarios for 2027-2031 with 35/35/30 probability weighting); Consensus (full FactSet 2024-2030); Trading Multiples; Sell-side ratings + PTs; Loss Analysis (3-method downside floor); UpDown (probability-weighted SP forecast); Richard's own EGPIBC + Case Difficulty + SP Fragility ratings. V3 built a parallel SOTP from RR text and reached MATERIALLY MORE PESSIMISTIC conclusions than Richard's existing model (V3 base case SEK 33-49 vs Richard's SEK 64-75; V3 bull SEK 60-72 vs Richard's SEK 134-185). The V3→V4 correction was 100% from incorporating Richard's existing analytical work, not from new analysis.

3. **Underpriced peer multiples by 50-138% (MATERIAL).** V3 had Prysmian at 8.5x EV/EBITDA (verified 15.0x), Corning at 10x (verified 23.8x), Belden at 9x (verified 13.6x). Cumulative effect: V3 systematically understated HTRO's discount-to-peer. The fibre/cable/connectivity sector has re-rated meaningfully on AI + offshore wind + defence + DC tailwinds (Corning's $500m NVIDIA deal was a sector-wide re-rating event V3 missed entirely).

**Why this happened:**
- V3 anchored on RR-text data (which was 1-3 months stale) and training data (knowledge cutoff May-25) without ever pulling current SP from public sources
- V3 didn't search COWORK for `Files/Financial models/{TICKER}*.xlsm` before starting the SOTP
- V3 didn't pull `databases/master/ic-ratings-current.json` or `databases/detail/p1-p6.json` for HTRO
- V3 didn't web-search for current peer ratios; relied on pre-cutoff training-data approximations
- V3 didn't web-search for material developments in the 5+ weeks since Q1-26 results

**Mitigation (MISSION CRITICAL — STANDING SOP for ALL future stock A&J work):**

**Phase 0 of any A&J on a stock MUST include, BEFORE substantive analysis:**
1. **Hunt for Richard's existing model**: `find /COWORK/Files -iname "*{TICKER}*.xlsm"` + extract SF Output, Consensus, Loss Analysis, UpDown, Ratings sheets if found
2. **Hunt for Master Dashboard data**: read `databases/master/ic-ratings-current.json` for the ticker + read `databases/detail/p1-p6.json` for current pillar ratings
3. **Pull current share price** via WebSearch (e.g., "{COMPANY} share price {ticker} today") — Yahoo/Bloomberg/MarketScreener
4. **Pull material developments since last earnings results** via WebSearch — press releases, broker notes, M&A activity
5. **Pull verified peer multiples** via WebSearch for each named peer — DO NOT rely on training-data approximations for current valuations
6. **Document Phase 0 findings explicitly** in §1 of the A&J output before any analysis. If any of the above is missing, FLAG it before proceeding.

**Phase 0 takes ~30 min and prevents the entire compound error V3 made. Without it, the analysis is built on potentially-wrong inputs.**

**Wider implication:**
- ANY analysis of a specific stock requires CURRENT data, not training-data approximations
- Richard's existing analytical work should be the STARTING POINT not the SUPPLEMENT
- The Master Dashboard already contains pillar ratings, technical readings, valuation data — these are AUTHORITATIVE inputs
- Web search is REQUIRED for current SP + recent catalysts on any stock-specific work
- "I'll work from the RR text" is NOT sufficient when the RRs are 1-3 months old and the stock has materially moved

**Watson admission:**
The V3→V4 gap is not a methodology failure. The Pillar/BB/Master Ratings/3-Check structural framework was correct. The error was failure to ground the framework in current verified data. This is a Phase 0 process failure, not an analytical reasoning failure. The fix is procedural: add the Phase 0 hunt to the standing SOP and never skip it.

**Files preserved for evidence:**
- V3 FINAL: `PROJECTS/SA - Reports & Memos Repository/htro-test-stock/HTRO-MEGA-AJ-MASTER-V3-FINAL.md` (51,629w, structurally rigorous, anchored on wrong inputs)
- V4 VERIFIED: `PROJECTS/SA - Reports & Memos Repository/htro-test-stock/HTRO-MEGA-AJ-MASTER-V4-VERIFIED.md` (5,269w, focused corrections)
- V3 incremental drafts 1-13 all preserved
- LATEST handoff updated with full V4 summary
- state.md updated with iteration history

**Action items emerging from this correction:**
1. Add "Phase 0 hunt" to A&J SOP (memory/skills/assistant-portfolio-manager/SKILL.md)
2. Add to CLAUDE.md universal winning behaviour: "Stock-specific work requires Phase 0 hunt"
3. Build a Phase 0 checklist template at `memory/skills/assistant-portfolio-manager/phase-0-checklist.md`

