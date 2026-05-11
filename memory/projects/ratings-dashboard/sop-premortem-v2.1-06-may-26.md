# Updating Old Research Memos SOP — Pre-Mortem & Version History

**Date:** 06-May-26
**Context:** SOP v2.0 written after v1.0 catastrophically failed in Sonnet testing. v2.1 written after pre-mortem identified 7 issues before second Sonnet test run.

---

## SOP Version History

| Version | File | Date | Summary |
|---------|------|------|---------|
| 1.0 | `.bak-pre-v21-premortem-20260506` contains v2.0; v1.0 was overwritten in-place | 05-May-26 | Content restructure approach. IAJA, sub-bullets, dimension splitting. 35% word floor. |
| 2.0 | Overwritten by v2.1 (backup at `.bak-pre-v21-premortem-20260506`) | 06-May-26 | Major rewrite: formatting only, Cardinal Rules, 90% word floor, flat bullets, splitting rule. |
| 2.1 | `updating-old-research-memos-SOP.md` (LIVE) | 06-May-26 | Pre-mortem fixes: multi-source merge, validator multi-file, bracket-tag exclusion. |

**Backup files:**
- `memory/skills/researcher/updating-old-research-memos-SOP.md.bak-pre-v21-premortem-20260506` — v2.0 before pre-mortem fixes

---

## v1.0 Test Results (7 memos, Sonnet mode)

| Memo | Word ratio | Failure mode |
|------|------------|--------------|
| AUTO-01-BD | 21.6% | Catastrophic content loss + rewording |
| AUTO-02-CF | 15.9% | Catastrophic content loss + rewording |
| AUTO-03-TM | 21.8% | Catastrophic content loss + rewording |
| BRAV-02-CF | 107% | OK ratio, wrong highlight style |
| BRAV-06-SS | 36% | Content loss |
| BRAV-07-KD | 116% | OK ratio but ORANGE-RED verdict removed entirely |
| BRAV-09-EH | 122% | OK ratio, wrong metadata (Q5 Triaging rendered as Q9 ESA) |

**Root cause:** SOP v1.0 gave Sonnet editorial licence via instructions to "restructure", "surface judgements", "dimension splitting". Sonnet treated 35% word floor as a target. Three failure modes: (1) content loss, (2) systematic rewording/softening, (3) verdict removal.

---

## v2.0 → v2.1 Pre-Mortem (06-May-26)

Richard instructed a pre-mortem before second Sonnet test. Seven issues found, five fixed:

### Issue 1 (CRITICAL): Validator only accepts one source file
**Problem:** SOP says merge [AS]+[C] into one memo, but validator takes single `<source.md>`. Would measure 90% ratio against one source only — Sonnet could drop entire second source and still pass.
**Fix:** Validator now accepts `source1.md source2.md ... body.html wrapped.html`. Sums word counts across all source files.

### Issue 2 (CRITICAL): "Merging multiple source files" in NOT-doing list
**Problem:** Line 103 said "Merging multiple source files" under "What you are NOT doing" — directly contradicts the merge instructions at line 54.
**Fix:** Changed to "Synthesising or reconciling content across sources (when merging [AS]+[C], include both — do not blend into new wording)".

### Issue 3 (MEDIUM): Wrapper script --source flag
**Problem:** Wrapper takes `--source AS` or `--source C`. No guidance for merged memos.
**Fix:** Added SOP instruction: pass `--source "AS+C"` for merged memos.

### Issue 4 (MEDIUM): No merge-specific section planning
**Problem:** Step 2 says "keep existing sections" but two sources may have different structures. No guidance on which takes precedence.
**Fix:** Added Step 2 rule: "Use the LONGER source's section structure as backbone. Slot shorter source's content into matching sections. Orphan sections from shorter source go at end."

### Issue 5 (MEDIUM): BLUF Key Findings — which source?
**Problem:** No guidance on drawing BLUF from merged sources.
**Fix:** Added: "When merging, draw Key Findings from BOTH sources. Tag each with [AS] or [C]."

### Issue 6 (NOTED): Context window pressure on long merged memos
**Problem:** AUTO Q1 BD (AS ~9,700w) + C source (~6,800w) = ~16,500w input → ~17,000w+ output = 33,000+ words in a single memo pass. May cause "falling off" in second half.
**Status:** Noted. Not an SOP fix. May need to reduce batch size for long merged memos.

### Issue 7 (FIXED): [AS]/[C] tags inflate word count
**Problem:** Source tags add ~200 words on a 200-bullet memo. Inflates output word count.
**Fix:** Validator now strips `[AS]`, `[C]`, `[AS+C]` from output text before word counting. Richard requested: exclude anything in brackets from word count.

---

## Key Design Decisions

1. **Merge, don't pick one source.** Richard wants both [AS] and [C] perspectives in one memo. The divergence between sources IS analytical signal. Merge = additive (include all), not editorial (blend/reconcile).

2. **Simple merge rule.** Combine by section proximity, tag each bullet with source. Don't de-duplicate. Slight redundancy is acceptable; content loss is not.

3. **90% word floor against COMBINED sources.** If AS is 9,700w and C is 6,800w, the floor is 90% of 16,500w = 14,850w. This is the hard gate.

4. **Formatting only, not rewrite.** v2.0 Cardinal Rules remain the foundation. The merge instructions are additive — they don't override the "do not reword" principle.
