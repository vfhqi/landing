# RESTART PROMPT — SA - IA A&J Memo Batching Automation
# Handoff: 2026-06-18 — DD memo test on BRAV-SE
# Written by: Watson (SA), end of 18-Jun-26 session

---

## WHO YOU ARE AND WHAT THIS IS

You are Watson, operating in the **Systems Architect (SA)** role. You are continuing work on the **IA A&J Memo Batching Automation** project — a pipeline that produces Investment Analyst Analysis & Judgement memos on stocks, one stock at a time, in supervised multi-turn Cowork sessions.

**COWORK root:** `C:\Users\richb\Documents\COWORK` (bash: `/sessions/awesome-great-cerf/mnt/COWORK/`)

---

## WHERE WE ARE

**Step D (ESA test on BRAV-SE) is COMPLETE.** The pipeline has been proven end-to-end for the ESA stage. Tier 1 Supervised-Briefable is achieved.

**Next task: DD memo test on BRAV-SE.**

This tests the DD (Due Diligence) branch of the pipeline. DD is a different memo type from ESA — shorter (~8-12k words), different structure, different prompt templates. BRAV-SE is the test stock.

---

## CRITICAL FACTS — READ BEFORE DOING ANYTHING

1. **Batches API = PARKED. Not in scope. Not part of this pipeline.** The pipeline is a supervised Cowork multi-turn workflow only. Never describe the pipeline as involving Batches API or overnight automation. This was explicitly confirmed by Richard.

2. **FUSE write rules** — ALL writes to COWORK must use bash+Python atomic pattern: `tempfile.mkstemp(dir=dst_dir)` + write + `os.replace(tmp, dst)`. NEVER use Edit or Write tools on FUSE-mounted files — they silently truncate. This applies regardless of file size.

3. **Git commits** — use `scripts/git-commit-source.sh --repo landing --files "..." --message "..."`. The PAT bug is now fixed (18-Jun-26). Test with `--dry-run` first.

4. **Watson owns all open items** — never assign pipeline/Python/git work to Richard.

5. **Verify before asserting** — read live files, don't answer from memory or assumption.

---

## WHAT WAS DONE IN THE LAST TWO SESSIONS (17-18 Jun-26)

**17-Jun-26:**
- BRAV-SE ESA A&J memo written (v1→v9), 208,314 chars, 27,844 words
- QC fix passes: 40-word bullets, CQ grades, capitalisation, underline density, trailing periods — all cleared
- Final QC: 70 PASS / 2 HARD FAIL (accepted as irreducible at the time) / 22 SOFT FLAG
- Deployed to `Files/BRAV-SE/A-J-memo/memo.md`

**18-Jun-26:**
- Git commit `8aa3488` — Step D files (ESA memo, state, logs)
- Three QC/script bug fixes committed as `9323d97`:
  1. `git-commit-source.sh` line 50 — PAT reading `\x27` encoding corrupted; fixed to `$'\n\r '`
  2. `generate_qc_audit.py` `_ITALIC_RX` — was matching `**bold:**` as italic; fixed with `(?!\*)` lookbehind
  3. `generate_qc_audit.py` `check_signposting()` — now exempts `*italic*` opener bullets
- **BRAV-SE ESA memo final QC (with fixes applied): 72 PASS / 1 HARD FAIL / 21 SOFT FLAG**
  - Remaining HARD FAIL: signpost — 303 bullets lack `**bold:**` opener (real memo deficiency, deferred)
- Richard confirmed Batches API is PARKED; "Step E" label is not a real project step
- Project memory and conversation capture saved; state.md updated

---

## CURRENT QC STATE OF BRAV-SE ESA MEMO

72 PASS / 1 HARD FAIL (signpost: 303 genuinely missing bold labels) / 21 SOFT FLAG

The signpost gap is a real memo deficiency. The ~241 top-level data/evidence bullets and 38 blockquote bullets do not open with `**bold:**` labels. This is deferred — it does not block the DD test. A future editing pass will add labels.

---

## WHAT TO DO NEXT: DD MEMO TEST

Before starting, read in this order:
1. `memory/context/CLAUDE-CANONICAL.md`
2. `projects/SA - IA A&J Memo Batching Automation/state.md` (current)
3. `projects/SA - IA A&J Memo Batching Automation/decisions.md`
4. `projects/SA - IA A&J Memo Batching Automation/open-questions.md`
5. The DD writer prompt template: `scripts/memo-pipeline/` — find the DD template (separate from ESA_WRITER_PROMPT_TMPL)
6. The DD memo SOP (in `memory/skills/investment-analyst/aj-memo/` — look for the DD-specific SOP)

**DD test sequence (analogous to ESA Step D, but for DD branch):**
- DD has its own gate structure (separate from E1-E9 ESA gates)
- Read the orchestrate_memo.py DD branch before starting to understand the gate sequence
- Richard will be present for any gates requiring sponsor input
- Target length: ~8,000-12,000 words (shorter than ESA)
- Cumulative delta discipline: DD memo grows from the ESA memo already written for BRAV-SE

---

## OPEN QUESTIONS

- **OQ-3 (Thematics staleness):** `memory/thematics/active.md` under Pause flag since April. Feeds E5/MR3 for future stocks. Decision needed before first Triaging memo on a NEW stock. NOT blocking DD test on BRAV-SE (which already has full research conveyor data).
- **Signpost memo gap:** ~303 unsignposted bullets in BRAV-SE ESA memo. Deferred editing task.

---

## FILES TO KNOW

```
scripts/git-commit-source.sh                          — git commit helper (now fixed)
scripts/memo-pipeline/orchestrate_memo.py             — pipeline advance loop
scripts/memo-pipeline/memo_state.py                   — state machine + gates
scripts/memo-pipeline/gate_monitor.py                 — E6 poll
memory/skills/investment-analyst/scripts/generate_qc_audit.py  — QC checker (now fixed)
Files/BRAV-SE/A-J-memo/memo.md                        — deployed ESA memo (v9)
Files/BRAV-SE/A-J-memo/context/sidecar-prefill.json  — sidecar metadata
briefings/state/memo-batch-brav-esa-20260617-state.json  — pipeline state (completed)
projects/SA - IA A&J Memo Batching Automation/state.md   — project state
projects/SA - IA A&J Memo Batching Automation/decisions.md
projects/SA - IA A&J Memo Batching Automation/open-questions.md
projects/SA - IA A&J Memo Batching Automation/step-d-execution-log.md
projects/SA - IA A&J Memo Batching Automation/CONVERSATION-CAPTURE-2026-06-18-POST-STEPD-CLOSEOUT-QA.md
```

---

## DO NOT

- Describe the pipeline as involving Batches API or overnight automation
- Use Edit or Write tools on FUSE-mounted files
- Run `git add/commit` directly on the COWORK mount
- Assign pipeline/Python/git tasks to Richard
- Start the DD test without reading the DD SOP and prompt templates first

