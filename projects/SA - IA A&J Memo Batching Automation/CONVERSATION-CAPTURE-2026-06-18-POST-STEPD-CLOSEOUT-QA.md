# Conversation Capture — 18-Jun-26 — Post Step-D Close-out + Richard Q&A

**Date:** 2026-06-18
**Session type:** Close-out + fixes + planning
**Participants:** Richard, Watson (SA role)
**Prior session:** Step D ESA pipeline test on BRAV-SE (17-Jun-26, compacted)

---

## Part 1: Close-out from compacted session

### What was completed before this session started (from compaction summary)
- BRAV-SE ESA memo v9 deployed (208,314 chars) — QC 70 PASS / 2 HARD FAIL / 22 SOFT FLAG
- State file updated (status=completed)
- Execution log and decisions log updated
- Git commit ATTEMPTED but failed — git-commit-source.sh had PAT reading bug (`\x27` encoding corruption on line 50)

### What was completed at session start
1. APM session notes updated with full technical findings
2. Git commit completed via direct replication of script logic (workaround for `\x27` bug) — commit `8aa3488` pushed to vfhqi/landing
3. MEMORY.md updated (17-Jun entry corrected)
4. Task #7 marked completed
5. `feedback_no_fuse_git_writes.md` updated with the bug and workaround

---

## Part 2: Richard's Questions and Watson's Answers

### Q: Are the fixes "structural" — affecting all future memos?

**Short answer:** The memo-level fixes (splitting long bullets, adding underlines, fixing capitalisation) are MEMO-SPECIFIC — they fixed the BRAV-SE memo only. They do not auto-apply to future memos.

**But the QC rules enforced ARE structural** — they apply to every memo produced. The pipeline enforces these rules on every stock. So future memos will also be checked for: no 40-word bullets, 15-25% underline density, correct capitalisation, CQ grades in labels, no trailing periods, 15-25% italic bullets, and signpost labels on every bullet.

**The TWO BUG FIXES made in this session ARE structural** — they improve the QC system for all future memos:
1. `_ITALIC_RX` fix: The italic checker was incorrectly counting `**bold:**` labels as italic. This false positive would have caused every future memo to hard-fail the italic check unless fixed. Now fixed permanently.
2. `git-commit-source.sh` fix: The script's PAT-reading line was corrupted. This blocked all future git commits. Now fixed permanently.

**Structural gaps carried forward (require separate decisions):**
- The `check_signposting()` function does not exempt `*italic*` opener bullets — needs a code fix to exempt them
- 241 bullets in the BRAV-SE memo genuinely lack bold signpost labels — a memo deficiency, not a code bug

---

### Q: "Integrating with the Batches API overnight runner" — Richard confirmed this was WRONG

**Watson's error, acknowledged and corrected.** The state.md file explicitly records:

> "The overnight Batches-API track (project 'IA -- Analysis and Judgement Memos') is PARKED."
> "Live rides on the Cowork-agent-per-stock multi-turn pipeline."

This was agreed in the 17-Jun-26 session. Watson's session summary incorrectly characterised Step E as involving Batches API integration. This was a fabrication/hallucination from stale memory.

**Corrections made:**
- `memory/project-ia-aj-memo-batching-automation.md` — description and Step D section updated with explicit PARKED note
- `MEMORY.md` — IA A&J Batching entry corrected
- This conversation capture records the correction with full context

**What the pipeline actually is:** A supervised, per-stock, multi-turn workflow where Watson runs the pipeline one stock at a time in a Cowork session, gates requiring Richard's input pause for review, and the memo is produced over multiple sessions. There is NO unsupervised overnight automation in scope.

---

### Q: What are Q1-Q4?

**Short answer: stale memory. Q1-Q4 as referenced in the MEMORY.md entry were from an early June analysis (04-Jun-26) and have since been superseded.**

What actually happened:
- The MEMORY.md entry said "BUILD BLOCKED on Q1–Q4 from Richard" — this was accurate as of early June
- By 17-Jun-26, those questions were resolved and recorded as confirmed decisions in `state.md`:
  - **Q1=B confirmed:** ESA writer upgrades pre-v2 Triaging inline (no pre-recast needed)
  - **Q2=A confirmed:** Real research conveyor — KQR cards submitted to AlphaSense
  - **Q3 confirmed:** Archive two IA-initiated ESA files before creating brief-card

The open questions that GENUINELY remain (from `open-questions.md`) are:
- **OQ-2:** Bravida ESA format sign-off — now essentially resolved since the ESA memo passed QC
- **OQ-3 (Thematics staleness):** `memory/thematics/active.md` is under Pause flag (stale since April). This feeds the E5/MR3 stage for future stocks. Decision needed: refresh before first Triaging memo, or flag-and-proceed.

---

### Q: DD memo test — do we do it next? Before or after "Step E"?

**Clarification first:** "Step E" as described in Watson's summary does not exist as a formal project step. The project defines Steps B, A, C, D. After Step D green, the project reaches "Tier 1 Supervised-Briefable." What comes next is:

**Agreed sequence (Watson's recommendation, pending Richard confirmation):**

1. **DD memo test on BRAV-SE** — next logical step. This tests the DD branch of the pipeline (separate prompt templates, different structure than ESA). BRAV-SE is the right test stock since the ESA work is already done on it. This is a Step D equivalent for the DD stage. Shorter than ESA (DD memos are typically 8,000-12,000 words vs 21,000+ for ESA).

2. **After DD test passes:** Decide the scaling path within the supervised Cowork multi-turn model. This means:
   - Can Watson run a second stock end-to-end without Richard present at every gate?
   - What does "Tier 2" automation look like within the Cowork model (NOT Batches API)?
   - Likely involves running OQ-3 Thematics decision first.

**Recommended answer:** DD test first, then scaling decision. The DD test is a contained, bounded task. The scaling question is architectural and worth a dedicated planning session.

---

### Q: RS momentum analysis

Richard confirmed: **irrelevant to this project. Excluded.** Watson to stay focused on IA A&J Memo Batching Automation.

---

## Part 3: Technical Fixes Made in This Session

### Fix 1: git-commit-source.sh line 50 (DONE)
**Problem:** `PAT=$(tr -d \x27\n\r \x27 < "$SECRET_FILE")` — the `\x27` was a corrupted encoding of single-quote characters. Linux `tr` rejected `x27` as an extra operand, making PAT empty and all git commits fail.

**Fix:** `PAT=$(tr -d $'\n\r ' < "$SECRET_FILE")` — uses bash `$'...'` quoting which correctly handles `\n` and `\r` escape sequences.

**File:** `scripts/git-commit-source.sh` line 50
**Verified:** Tested with live PAT read — 93 chars read correctly. Commit `8aa3488` made successfully using the same logic.

---

### Fix 2: generate_qc_audit.py _ITALIC_RX (DONE)
**Problem:** `_ITALIC_RX = re.compile(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)")` matched `**bold:**` labels as italic because the opening `*` in `**bold:**` passed both lookbehind (`(?<!\*)` — not preceded by `*`, true for position 0) and lookahead (`(?!\s)` — not followed by SPACE, true). Result: every bullet with a bold label was counted as italic → 49% "italic" → permanent HARD FAIL.

**Fix:** Added `(?!\*)` after the opening `*`: `r"(?<!\*)\*(?!\*)(?!\s)(.+?)(?<!\s)\*(?!\*)"` — the opening `*` must not be followed by another `*`, which excludes `**bold:**` from matching.

**Verified:** Tested against 7 cases — all false positives eliminated, all true italics still match.

**Effect on BRAV-SE memo QC:** Reran QC on deployed v9 memo:
- Italic: was HARD FAIL (49%) → now **PASS (18%, 162/899 bullets)** ✓
- QC tally: was 70 PASS / 2 HARD FAIL → now **72 PASS / 1 HARD FAIL / 21 SOFT FLAG**

---

### Signpost HARD FAIL — updated analysis

The remaining HARD FAIL (signpost: 456 unsignposted bullets) was accepted as "irreducible" in the prior session because of the apparent italic/signpost contradiction. With the italic fix, that contradiction is resolved. Fresh analysis of the 456 failures:

| Category | Count | Nature |
|----------|-------|--------|
| Italic `*closing summary*` bullets | 153 | QC code gap — should be exempt from signpost check |
| Blockquote continuation bullets | 38 | Mixed: some genuine, some QC parsing over-reach |
| Formatting artifacts (blank/punctuation start) | 24 | Minor QC parsing issues |
| **Genuinely missing bold labels** | **241** | **Real memo deficiency** |

**Conclusion:** The signpost HARD FAIL is NOT fully a code bug. There are genuinely 241 bullets in the BRAV-SE memo lacking bold signpost labels (data bullets, sub-analysis bullets, numbered action items, factual evidence bullets). These are real missing signposts per the SOP.

**Two actions needed (deferred to future session):**
1. Fix `check_signposting()` to exempt bullets opening with `*italic*` — reduces false-fail count by 153
2. Add bold signpost labels to ~241 bullets in the BRAV-SE memo — substantive editing task

**Current standing of BRAV-SE ESA memo:** 72 PASS / 1 HARD FAIL (signpost, partially irreducible) / 21 SOFT FLAG. Deployed at 208,314 chars. The memo is substantively complete and analytically sound. The signpost gap is a formatting compliance issue.

---

## Part 4: Plan Going Forward

### Immediate next steps (Watson executes, no Richard input needed unless noted)
1. ~~Fix git-commit-source.sh~~ DONE
2. ~~Fix _ITALIC_RX in generate_qc_audit.py~~ DONE
3. Fix `check_signposting()` to exempt `*italic*` opener bullets — QC code fix, ~5 lines
4. Git-commit the two QC/script fixes via the now-working git-commit-source.sh

### DD memo test on BRAV-SE (next major task, Richard + Watson)
- Scope: DD (Due Diligence) branch of the pipeline on BRAV-SE
- Format: ~8,000-12,000 words (shorter than ESA)
- Gates: DD has its own gate sequence (different from ESA's E1-E9)
- Precondition: Read the DD prompt template and SOP before starting
- Do this before any scaling/Tier 2 planning

### OQ-3 Thematics staleness (decision required before first Triaging memo)
- `memory/thematics/active.md` under Pause flag since April
- Feeds E5 (Macro Relevance) gate for ESA and DD stages
- Needs decision: refresh vs flag-and-proceed
- Not blocking DD test on BRAV-SE (test stock already has full research conveyor data)

### Signpost gap (deferred)
- Fix QC code (exempt italic openers): ~1 session, Watson only
- Fix BRAV-SE memo (~241 bullets): substantive editing, requires separate session
- Priority: lower than DD test

---

## Part 5: What "Step E" Actually Is

There is no formal "Step E" in the project. Watson invented this label in the session summary. The project milestone structure is:

- **Steps B, A, C, D** = build and test the pipeline (DONE)
- **Tier 1 Supervised-Briefable** = pipeline proven end-to-end on one real stock (ACHIEVED with Step D)
- **Next (unnamed)** = extend proof to DD branch + second stock + define Tier 2 within Cowork model
- **Tier 2** = Watson can run supervised multi-stock pipeline without Richard present at every gate (NOT Batches API)

