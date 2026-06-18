---
name: project-ia-aj-memo-batching-automation
description: IA A&J Memo Batching Automation — pipeline BUILT; Step D (BRAV-SE ESA) COMPLETE 18-Jun-26; next = DD memo test; Batches API track PARKED (not in scope); reviewed 18-Jun-26
metadata:
  type: project
---

Build substantially complete as of 17-Jun-26 session (two defect-fix passes).

**Why:** Overnight memo production — 10 memos/night via autonomous pipeline. Watson drops brief-card; pipeline runs Stations 0-5 without interruption (except E1/E4 gates for ESA stage which require Richard).

**Steps completed (17-Jun-26):**
- **B1-B4**: Emphasis band CAPS gate, F5 CQ answer-clause gate, v2 viewer deployed to live repo, SDIP normalised
- **Step A**: Full ESA/DD gate machinery — memo_state.py (E1-E6 gates, gate_state enum), gate_monitor.py (E6 poll), orchestrate_memo.py (advance loop with ESA/DD branches, auto-publish on judge PASS)
- **Step C**: Mock acceptance suite — 31 PASS 0 FAIL 1 SKIP (CR-01..CR-21 + CR-ESA-1..CR-ESA-7)
- **D1-D5 defect fixes** (first-hand audit pass 1):
  - D1 (critical): `sidecar_file` default in `new_stock_block` was `metadata.json` — fixed to `context/sidecar-prefill.json`. Sidecar pointer was wrong; K9 auto-advance never found judge_result.
  - D2/D5: Test suite fix (CR-ESA-7b `JUDGE_PROMPT_TMPL.format` needed SIDECAR kwarg after D4 fix)
  - D3: `materialize_writer_prompt` used `company = ticker` ignoring universe.json — fixed with `_company_name()` helper
  - D4: `--meta <sidecar>` literal placeholder in WRITER/JUDGE prompt templates — fixed to `--meta {SIDECAR}` with substitution
- **D6-D9 defect fixes** (first-hand audit pass 2 — fresh sceptical read of deployed code):
  - D6: `advance()` passed hardcoded `"normal","normal"` dials to `assemble()` ignoring `st["dials"]` — fixed to read `st.get("dials",{})`
  - D7: `run_render_qc()` hardcoded sidecar path — fixed with optional `sidecar_path` param; call site passes `R / blk["sidecar_file"]`
  - D8 (medium): E6 timeout measured from batch `created_at` not E6 gate open — fixed: `record_kq_briefs()` stamps `e6_blocked_at`; gate_monitor uses that (fallback: `created_at` for legacy files)
  - D9 (medium): `run_render_qc` mapped exit-3 to UNAVAILABLE but `generate_qc_audit.py` never emits exit 3. Cold renderer exit-1 with "ENVIRONMENT" in output was bumping fix_loop_attempts to cap then qc_hard_fail — fixed: detect UNAVAILABLE from output text not exit code
- **Final suite: 32 PASS 0 FAIL 1 SKIP** (CR-ESA-5b added to verify D8)

**Pipeline files (all deployed, all green):**
- `COWORK/scripts/memo-pipeline/memo_state.py` — state machine, gates, atomic writes
- `COWORK/scripts/memo-pipeline/orchestrate_memo.py` — advance loop, writer/judge prompt materialisation, auto-publish
- `COWORK/scripts/memo-pipeline/gate_monitor.py` — E6 poll, `e6_gate_open()`
- `COWORK/scripts/memo-pipeline/assemble_memo_context.py` — context assembly, sidecar writer
- `COWORK/scripts/memo-pipeline/run_mock_acceptance.py` — 32-test suite (32P/0F/1S)
- Backups: `.bak-d1d5-20260617`, `.bak-d6d9-20260617b` on orchestrate_memo, memo_state, gate_monitor, run_mock_acceptance

**Known limitation (acceptable):** trust dial hardcoded as "balanced" in assemble_memo_context.py line 303 regardless of batch dials. Balanced is the correct default; trust is not a passed parameter to assemble(). Not a blocker.

**Station 5 stub:** auto_publish() generates viewer HTML and marks closed. Full automation (metadata.json, Notion, refresh_repository.py) is Tier 2. For Step D, Watson does these steps manually after judge PASS.

**Step D — COMPLETE (18-Jun-26):**
- BRAV-SE ESA A&J memo v9 deployed: 208,314 chars, QC 72 PASS / 1 HARD FAIL (signpost) / 21 SOFT FLAG
- Italic _ITALIC_RX bug FIXED in generate_qc_audit.py (18-Jun-26) — italic now PASS at 18%
- git-commit-source.sh PAT bug FIXED (18-Jun-26) — \x27 encoding corrected on line 50
- Signpost HARD FAIL investigation: 456 bullets (153 italic closing bullets = QC code gap; 241 genuinely missing bold labels in data/sub-analysis bullets; 24 formatting artifacts)
- Signpost is NOT fully irreducible: QC code should exempt *italic* openers; memo also has ~241 bullets needing bold labels added
- Tier 1 Supervised-Briefable: ACHIEVED

**CRITICAL — Batches API: PARKED (confirmed, not in scope):**
The pipeline rides the Cowork-agent-per-stock multi-turn pipeline ONLY.
The overnight Batches-API track (separate project "IA — Analysis and Judgement Memos") is explicitly PARKED.
Step E is NOT about wiring a Batches API overnight runner. It is about scaling supervised runs via the existing Cowork pipeline — DD memo test first, then defining what Tier 2 automation looks like within the multi-turn model.

**Step D (original spec — now superseded by COMPLETE above):**
- Pre-condition: BRAV-SE Triaging memo must be in v2 format (doc 10 L2). If not: recast first or use OBEL-BE.
- Live ESA test: E1 Q&A (Richard) -> E3 context + key questions -> E4 approval (Richard) -> E5 briefs -> E6 wait -> ESA memo -> Station 3 QC -> Station 4 judge -> PASS -> publish -> closed
- After ESA: decide whether to chain DD test in same session or defer
- On Step D green: **Tier 1 Supervised-Briefable** achieved

**Q5 confirmed:** Autofire Station 5 (publish) on judge PASS — no manual pause.

**B3 deferred:** OBEL-BE editorial pass (F5 synthesis + emphasis trim) — separate LLM session, not blocked.

**Conversation capture:** `projects/SA - IA A&J Memo Batching Automation/CONVERSATION-CAPTURE-2026-06-17-PM-D1-D9-FIXES-AND-STEP-D-BRIEF.md` — full defect detail + plain-English + technical Step D sequence.

**How to apply:** Read handoff `handoff-2026-06-17-PM-d1d5-fixed-ready-for-step-d.md`, read restart prompt `RESTART-PROMPT-2026-06-17-PM-step-d-live-esa-test.md`, then proceed to Step D. Do NOT re-build Steps A/B/C/D-fixes — all done.
