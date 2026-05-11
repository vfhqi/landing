# Research Execution SOP — V2

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- [W] V2 created 14-Apr-26. Major changes: Haiku AS submission agent, self-contained templates, source-specific execution paths. -->
<!-- [W] V2.1 updated 15-Apr-26: PDF download confirmed as primary extraction method (AS interface changed overnight 14-15 Apr); concurrent limit updated 3 → 10. -->
<!-- [W] V2.2 updated 15-Apr-26: Step 6c added — dual-source merge post-processing for queries #2, #4, #5, #7. Pre-merge validation gate, backbone selection, contradiction handling, thin-AS handling. -->
<!-- [W] V3.0.1 updated 06-May-26: Q1 (Business Description) added to Step 6c merge list per D-RSR-36. Backbone default: [AS]. -->
<!-- [W] V3.0.2 updated 06-May-26: ALL dual-source queries now merge to single page per D-RSR-37. Step 6c expanded from IG/Triaging-only to all stages: added Q8, Q10, Q14, Q19, Q20 with backbone defaults. Merge content-retention gate added (≥70% of combined raw). Richard's instruction: "1 longer memo is better than 2 separate memos." -->
<!-- [W] V2.3 updated 29-Apr-26: Pre-Submission Character Count Gate added before Haiku dispatch (§Step 3). Root cause: two SMWH AS submissions truncated (JS injection method pasted partial prompt before Submit clicked). Gate requires Sonnet to verify character count and JS-injection post-paste length before Haiku dispatches. -->
<!-- [W] V3.0 updated 30-Apr-26: FOUR-PHASE MODEL replaces continuous-Chrome workflow. Phase 1 = submit + verify + close window (live session). Phase 2 = cold reopen + extract (scheduled, ~02:00 UK). Phase 3 = merge. Phase 4 = publish. Auto-resubmit rule added (§Step 6, Rule #31): if extraction fails after 2-3 retries over 15 min AND original submission >120 min ago → assume thread is broken, resubmit fresh. Removes all Chrome-warmup engineering. Memory Saver / tab discard / renderer hang failure modes eliminated by closing Chrome between phases. Richard's instruction 30-Apr-26. -->
<!-- Referenced by: RESEARCHER role file (SKILL-V2.md) -->

## Purpose

This SOP governs how Watson executes research through two sources: **Claude [C]** (Sonnet native execution) and **AlphaSense [AS]** (Haiku browser submission + Sonnet extraction). It is the single source of truth for research execution mechanics. All 22 queries use this SOP.

---

## Core Architecture: Three Execution Roles

| Role | Model | Responsibility |
|------|-------|----------------|
| **Parent RESEARCHER** | Sonnet | Orchestration: reads templates, fills placeholders, dispatches agents, validates returns, posts to Notion, runs verification |
| **Claude [C] Research Agent** | Sonnet | Writes the research memo natively using web search. Receives only the self-contained template. Returns the completed memo. |
| **AlphaSense [AS] Submission Agent** | Haiku | Submits the prepared prompt to AlphaSense Deep Research via Chrome browser. Returns URL + verification evidence. Does NOT write research. |

**Sonnet handles all intellectual work.** Haiku handles only the mechanical browser submission protocol.

---

## Four-Phase Execution Model (v3.0, 30-Apr-26)

**The AS workflow is split into four discrete phases, each with its own context and lifecycle.** This replaces the prior continuous-session model that kept Chrome alive across submit→wait→extract. Locked 30-Apr-26 per Richard's instruction.

| Phase | When | Live or scheduled | Chrome state | Token cost |
|---|---|---|---|---|
| **Phase 1 — SUBMIT + VERIFY** | Live session, immediately on brief sign-off | Live (Richard at desk) | Open during; **CLOSED at end of phase** | Low — single focused context |
| **Phase 2 — EXTRACT** | Scheduled task, 02:00 UK (or ≥3h after submission, whichever later) | Scheduled / unattended | **Cold reopen** for each thread; closed at end | Low — short focused task |
| **Phase 3 — MERGE** | Scheduled task, ~02:30 UK (after Phase 2) | Scheduled / unattended | Not used | Low — local file ops only |
| **Phase 4 — PUBLISH** | Scheduled task, ~03:00 UK (after Phase 3) | Scheduled / unattended | Not used | Medium — Notion API + dashboard render |

**Why four phases instead of continuous flow:**

1. **Eliminates the blank-pane / tab-discard failure mode entirely.** Chrome is closed between Phase 1 and Phase 2. There is no "stale renderer," no "tab discarded," no Memory Saver consideration. Phase 2 cold-reopens a fresh Chrome window with fresh JS context and fresh auth cookies.
2. **Each phase has a clean context.** No "wait 45 minutes while doing other work" pattern (which is when context exhaustion repeatedly hit, e.g. COMET 28-Apr-26).
3. **Failures are isolated.** Phase 2 failure does not corrupt Phase 1 outputs. Phase 3 failure does not corrupt Phase 2 outputs. Each phase's outputs are a durable handoff artefact.
4. **The AS-FIRST GATE (Rule #29) becomes structural.** Phase 4 cannot fire until Phase 3 wrote `merged.md`. Phase 3 cannot fire until Phase 2 wrote `raw-AS.md`.
5. **Resubmission is cheap.** AlphaSense resubmissions are free. If a thread is "broken" (per Rule #31 below), Watson resubmits in a new window without any cost penalty.

**Phase boundaries map onto handoff artefacts:**

| End of phase | Artefact written | Next phase reads |
|---|---|---|
| Phase 1 | `as-thread.json` (URL, status=SUBMITTED, prompt char count, sidebar evidence) | Phase 2 reads URL list |
| Phase 2 | `raw-AS.md` + updated `as-thread.json` (status=EXTRACTED) | Phase 3 reads raw-AS.md |
| Phase 3 | `merged.md` + `qc-audit.md` + updated `metadata.json` | Phase 4 reads merged.md + metadata |
| Phase 4 | Notion page IDs in `metadata.json`, dashboard manifest updated | Watchdog reads completion flag |

**This four-phase model supersedes** the prior "all in one session" pattern documented in V2.x. Step 1 (Prepare Prompts), Step 2 (Execute [C]), Step 3 (Submit AS) all map to Phase 1. Step 6 (Extract) maps to Phase 2. Step 6c (Merge) maps to Phase 3. Step 7 (Post to Notion) maps to Phase 4.

---

## Step 1: Prepare Prompts from Templates

Parent RESEARCHER reads the relevant template file from `templates/` and fills in placeholders:

| Placeholder | Source |
|-------------|--------|
| `{TICKER}` | Stock ticker |
| `{COMPANY}` | Full company name |
| `{INDUSTRY}` | Industry/sector |
| `{PEERS}` | 2-4 comparable peers (ideally European-listed). RESEARCHER selects if Richard hasn't specified. |
| `{ANGLES}` | Any specific angles Richard flagged in the brief |
| `{KDs}` | Key drivers (for #14 only — from APM's posted Analysis + Judgement) |

### Source-Specific Prompt Adaptation

Each template contains clearly separated prompt versions:

- **[C] version:** Sell-side research and expert interview references REMOVED. Watson searches the public web; no access to proprietary sources.
- **[AS] version:** Sell-side and expert references KEPT. AlphaSense searches proprietary broker research, expert calls, filings.

This is the ONLY systematic difference. Templates encode this automatically.

---

## Step 2: Execute Claude [C] Research — Sonnet Native

### Method

1. Parent RESEARCHER extracts the [C] prompt section from the filled template
2. Dispatches a Sonnet sub-agent with the [C] prompt as the COMPLETE brief
3. Sub-agent uses **WebSearch** extensively to research each topic
4. Sub-agent writes the complete memo and returns it
5. Parent RESEARCHER validates on return (see Step 5)

### Parallel Execution

- Launch ALL [C] agents simultaneously — no concurrency limit
- Each agent handles one query (e.g., one CF [C] or one TM [C])
- For a batch of 3 stocks × 2 [C] queries each = 6 agents running simultaneously

### Quality Standards

- Output must meet the minimum word count specified in the Master Table
- Must follow the section structure from the template
- Include tables, financial data, peer comparisons as specified
- Include judgement and analysis, not just description
- If WebSearch results are thin, flag which sections may be less comprehensive

### What the [C] Sub-Agent Receives

ONLY the filled template. Nothing else. No SKILL.md, no posting SOP, no philosophy files. The template's CONTEXT section contains the investment system context this specific query needs. The template's PROMPT section is the complete research brief.

---

## Step 3: Submit to AlphaSense Deep Research — PHASE 1 (Live Session)

### Overview

Parent RESEARCHER (Sonnet) prepares the [AS] prompt. A Haiku-mode sub-agent executes the browser submission protocol. Haiku's job is purely mechanical: navigate, verify mode, paste, submit, capture URL, **verify health, close window**.

**This is Phase 1 of the four-phase model (v3.0, 30-Apr-26).** Phase 1 happens in a live session while Richard is at the desk and able to act on submission failures. Phase 1 ends with Chrome **closed** — no kept-alive monitoring, no warmup engineering, no tab-discard concerns. Phase 2 (extract) cold-reopens hours later.

### ⚠️ Pre-Submission Character Count Gate — MANDATORY (added 29-Apr-26)

Before dispatching the Haiku submission agent, **Sonnet must verify the prompt is fully populated.** Two SMWH submissions (29-Apr-26) failed because Haiku clicked Submit before the full prompt was in the text field — the JS injection method pre-filled only a short excerpt, not the full prompt.

**Mandatory check before every Haiku dispatch:**

1. Count the characters in `{THE_FILLED_AS_PROMPT}` — the actual text that will be pasted
2. Compare against the source template word count. Each prompt template specifies a minimum word count target. The submitted prompt should be ≥80% of the template's word count
3. **If the prompt is shorter than expected:** Stop. Do NOT dispatch Haiku. Re-examine how the placeholder was filled. Was the entire template section extracted, or only a fragment?
4. Log the character count in the SUBMISSION_REPORT field `prompt_char_count` (see Return Format below — add this field)
5. **If using JS injection method** (pasting via `document.querySelector('textarea').value = ...` or similar): always verify post-paste that the full content is present before submitting. Run: `document.querySelector('textarea').value.length` and compare against the pre-paste character count. If lengths don't match, the paste was truncated — do NOT submit.

**Minimum prompt length guidance by query type:**

| Query type | Typical template word count | Minimum acceptable submission |
|---|---|---|
| #1 BD, #6 SS, #9 Earnings delivery record | ~400-600 words | ≥350 words |
| #2 CF, #5 ED, #7 KD | ~600-900 words | ≥500 words |
| #21 KQ Analysis, #22 CEO/CFO Questions | ~800-1,200 words | ≥700 words |
| All others | Varies | ≥80% of template |

**Root cause (29-Apr-26):** Both #21 and #22 were submitted with only a short introductory paragraph — the JS injection wrote partial content before the submit button was clicked. Richard confirmed both: "Submit was pressed before the full prompt was entered." Two complete re-runs were required. This gate is structural prevention of that failure mode.

---

### Haiku AS Submission Agent — Prompt Template

The Haiku agent receives this prompt (filled in by Sonnet):

```
## TASK: Submit Research Prompt to AlphaSense Deep Research

You are submitting a research prompt to AlphaSense. Follow this protocol EXACTLY.

### PROMPT TO SUBMIT
{THE_FILLED_AS_PROMPT}

### PROTOCOL (follow every step — do not skip any)

1. Navigate to: https://research.alpha-sense.com/gensearch
2. Click "Deep Research" in the mode selector
3. VERIFY mode selection — run this JavaScript:
   ```javascript
   (() => {
     const btn = document.querySelector('[aria-pressed="true"]');
     const sel = document.querySelector('.Mui-selected');
     return JSON.stringify({
       ariaPressedTrue: btn ? btn.textContent : 'NOT FOUND',
       muiSelected: sel ? sel.textContent : 'NOT FOUND'
     });
   })()
   ```
   Record the result.
4. Take a SCREENSHOT showing the mode selector area
5. Paste the prompt into the editor
6. RE-VERIFY mode (pasting can reset it) — run the same JS check
7. Take a SCREENSHOT showing prompt + mode selector
8. Submit (Enter key)
9. Wait 5 seconds
10. VERIFY submission:
    - Check URL changed (new thread ID in address bar)
    - Check page shows "Deep Research Report" progress indicator
    - Take a SCREENSHOT of the sidebar label (zoom if needed) — must show "Deep Research"
11. Copy the browser URL from the address bar

### REQUIRED RETURN FORMAT

Report ALL of the following. If ANY field is empty, the submission is FAILED.

```
SUBMISSION_REPORT:
  url: {the AlphaSense URL}
  pre_paste_verify: {JS check result from step 3}
  post_paste_verify: {JS check result from step 6}
  url_changed: {yes/no}
  progress_indicator: {yes/no}
  sidebar_label: {Deep Research / other / not visible}
  screenshots_taken: {count}
  status: {VERIFIED / FAILED}
  failure_reason: {if FAILED, explain what went wrong}
```

### RULES
- Do NOT modify the prompt text
- Do NOT proceed past step 2 if Deep Research mode is not verified
- If anything fails, STOP and report the failure — do not retry
- Do NOT extract any results — extraction is handled separately
```

### Sonnet Validation on Return

Parent RESEARCHER checks the Haiku agent's SUBMISSION_REPORT:
1. `status` must be `VERIFIED`
2. `pre_paste_verify` and `post_paste_verify` must both show Deep Research selected
3. `url_changed` must be `yes`
4. `sidebar_label` must be `Deep Research`
5. URL must be a valid AlphaSense URL

**If ANY check fails:** Treat submission as failed. Log the failure. Re-submit via Haiku (or escalate to Richard if second attempt fails).

### Concurrent Submissions

- **AlphaSense concurrent limit: 10 Deep Research searches at a time** (confirmed 15-Apr-26 — increased from previous 3-report limit)
- Haiku submits in waves of up to 10
- Submit Wave 1 → copy URLs → wait 45 min → Sonnet extracts Wave 1 → Haiku submits Wave 2 if needed → repeat
- For typical IG batches (2 AS reports per stock, ≤5 stocks = ≤10 reports), a single wave is usually sufficient
- Parent RESEARCHER tracks waves in `memory/research-queue.md`

---

## Step 3a: Phase 1 Submission Health Check + Window Close — MANDATORY (v3.0, 30-Apr-26)

**This is the gate that closes Phase 1.** After every AS submission via Haiku, before declaring Phase 1 complete:

### Five-check verification (Sonnet, in live session)

For each submitted thread:

1. **Prompt length verified post-paste** — `document.querySelector('textarea').value.length` matches the source prompt within 95% (existing V2.3 char count gate, kept).
2. **Submit clicked successfully** — confirmed by URL change (new thread ID in address bar, not the generic `/gensearch` URL).
3. **Processing indicator visible** — screenshot shows the AS progress icon / "Generating Deep Research Report" status text. Not just "submitted" — *actively processing*.
4. **Sidebar entry present** — left sidebar shows the new thread title with "Deep Research" label.
5. **URL captured** — written to `as-thread.json` with `status: SUBMITTED`, ISO timestamp, thread title, prompt char count.

**If ANY check fails:** Resubmit immediately while still in live session. Do NOT defer to scheduled Phase 2 or watchdog. Phase 2 cannot fix a bad submission — it can only extract from a thread that is genuinely processing.

### Close the window

After the five-check verification passes for every submitted thread:

1. Sonnet writes `as-thread.json` with full provenance (URLs, statuses, char counts, sidebar evidence)
2. **Close the Chrome window entirely.** Use `mcp__Claude_in_Chrome__tabs_close_mcp` for the AS tab(s); if browser-managed, close the browser.
3. **Do NOT keep Chrome alive across the wait window.** Phase 2 will cold-reopen.

### Why "close the window" is mandatory

The blank-pane / tab-discard / Memory Saver / renderer-hang failure modes all require a kept-alive Chrome session to manifest. Closing Chrome between Phase 1 and Phase 2 eliminates all of them. Phase 2 lands a fresh window on the same authenticated AS session (cookie-based persistence), retrieves the thread, extracts, and closes again. Locked 30-Apr-26 per Richard's instruction.

### Output of Phase 1

- `as-thread.json` per query, with `status: SUBMITTED` and full provenance
- `raw-C.md` per [C]-side query (saved by Step 5)
- All Chrome windows closed
- Phase 1 complete — session can close

**Do not proceed to extraction in the same session.** Extraction is Phase 2 (scheduled task at 02:00 UK or ≥3h post-submission).

---

## Step 4: Inter-Phase Hand-off (Phase 1 → Phase 2)

**There is NO active wait phase in v3.0.** Watson does not "wait and do other work." Phase 1 ends, the live session closes, the scheduled Phase 2 task fires later.

- **Phase 2 fire time:** 02:00 UK (default) OR ≥3 hours after the latest Phase 1 submission, whichever is later.
- **Provenance handed across:** `as-thread.json` is the only handoff artefact. It contains all URLs Phase 2 needs.
- **Watson does NOT:** monitor progress, keep tabs open, return periodically, or "do other work while waiting." All those patterns are deprecated in v3.0.

---

## Step 5: Return & Validate Sub-Agent Outputs

### For [C] Sub-Agents (immediate return)

On return from each Sonnet [C] research agent:

1. **Word count check — two-tier gate (revised 24-Apr-26):**
   - **<50% of minimum:** Hard floor. Do NOT post. Save raw to local Files/. Log failure. Escalate to Richard. Regenerate.
   - **50-75% of minimum:** Quality gate. Read the template, count how many specified sections/sub-questions are present. If section coverage <80% → do not post, regenerate or escalate. If coverage ≥80% → post with `"quality_flag": "below_target"` in metadata.json.
   - **>75% of minimum:** Pass. Post normally.
2. **Ticker/company check:** Correct stock discussed throughout
3. **Section completeness:** All sections from the template present (this is also the quality gate check for 50-75% outputs)
4. **Quality spot-check:** Tables present? Peer comparisons? Judgement in each section?
5. If any check fails: flag to Richard with specific deficiency
6. **⚠️ SAVE TO STRUCTURED LOCAL STORAGE (18-Apr-26, v2) [D]:** Save to the folder-per-ticker structure per Rule #20 v2 (SKILL-V2.md). This replaces the old flat-file save. See Step 5b below for the full sequence. File first, post second. Rationale: context compaction can destroy unsaved agent outputs AND local files serve as Watson's cross-session working memory.

**⚠️ RESEARCHER OUTPUT FEEDS APM — NOT AN INVESTMENT DECISION (15-Apr-26) [D]:** RESEARCHER produces Information only. At session close, summarise findings and explicitly flag: "This now feeds the APM role for Analysis and Judgement." Never present research findings as PARK/PROCEED/ESA verdicts — that is the APM role's job. The correct chain: RESEARCHER → Information → APM (Analysis + Judgement) → Richard (final Judgement + Action). Never collapse RESEARCHER and APM into one step.

### For [AS] Submissions (after 45+ min wait)

Validation is of the submission itself (done in Step 3). Content validation happens after extraction (Step 6).

---

## Step 5b: Save to Structured Local Storage (Rule #20 v2, 18-Apr-26)

After validation passes and before Notion formatting:

1. **Determine paths:**
   - Ticker: from the query context
   - Stage: from query number (1-3=IG, 4-7=Triaging, 8-14=ESA, 15-19=DD, 20-21=KQ, 22=Monitoring, 23=Thematic)
   - Query folder: `{QUERY-NUM}-{QUERY-SHORT-NAME}/`

2. **Create directories:** `mkdir -p COWORK/Files/{TICKER}/{STAGE}/{QUERY-FOLDER}/`

3. **Save raw output:**
   - Single-source: `raw.md`
   - Dual-source: `raw-C.md` and `raw-AS.md`

4. **After formatting/highlighting, save formatted output:**
   - Single-source: `notion-formatted.md`
   - Dual-source: `merged.md` (the merged version that goes to Notion)

5. **Write metadata.json:** `{"ticker", "query_number", "query_name", "stage", "source", "word_count", "created", "notion_page_id" (null until posted), "notion_posted", "properties": {"title", "sentiment", "tags"}}`
   - Update `notion_page_id` and `notion_posted: true` after successful Notion posting.

6. **Update per-ticker index:** Read/write `COWORK/Files/{TICKER}/index.json`

7. **Update master index:** Read/write `COWORK/Files/index-master.json`

8. **Regenerate ticker README:** `COWORK/Files/{TICKER}/README.md`

9. Proceed to Notion posting (Step 6, unchanged).

---

## Step 6: Extract AlphaSense Results — PHASE 2 (Cold Reopen, Scheduled)

**Extraction is always done by Sonnet, not Haiku.** The extraction requires quality judgement and error recovery.

**This is Phase 2 of the four-phase model (v3.0, 30-Apr-26).** Phase 2 is a scheduled task that fires at 02:00 UK (default) or ≥3h post-submission. Chrome was **closed at the end of Phase 1**. Phase 2 cold-reopens a fresh window for each thread, extracts, then closes. There is no warmup, no kept-alive monitoring, no per-thread state carryover.

### Phase 2 Cold-Reopen Protocol — MANDATORY (v3.0, 30-Apr-26)

For each thread URL in `as-thread.json` with `status: SUBMITTED`:

1. **Open a fresh Chrome window** (or fresh tab in a freshly-launched browser session). Do NOT navigate from a stale tab.
2. **Resize to full screen** — `resize_window(1920, 1080)`.
3. **Navigate directly to the thread URL.** AS auth cookies persist across browser restarts; you land on the same authenticated session as Phase 1.
4. **Wait 60 seconds** for content to render (AS is a SPA — content streams in after load).
5. **Check for the PDF Download button.** If visible, proceed to extraction (PDF Download method, below).
6. **If Download button absent after 60s:** wait another 60s, recheck. Total wait per thread: up to 3 minutes from initial navigation. Do not wait longer.
7. **If still absent after 3 min:** apply **Auto-Resubmit Decision Tree** (Rule #31, below) — do NOT just defer.
8. **After successful extraction:** close the tab/window before opening the next thread URL. **Per-thread cold isolation prevents cross-thread contamination** (cf. 28-Apr Haiku concurrent-agent contamination — same root cause).

### Pre-requisite: FULL SCREEN

Browser window MUST be full screen (1920x1080 minimum) before any extraction. Always `resize_window(1920, 1080)` first (already specified in step 2 above).

---

## ⚠️ Rule #31 — Auto-Resubmit Decision Tree (v3.0, 30-Apr-26)

**Resubmission to AlphaSense is FREE.** There is no cost penalty for resubmitting a query. There is also no way to "fix" a broken AS thread — they cannot be edited or restarted; they must be resubmitted as a new thread. This rule operationalises that reality.

### Decision tree (apply per thread in Phase 2)

```
Try to extract thread.
│
├─ Extraction succeeded? → Done. Save raw-AS.md. Update as-thread.json status=EXTRACTED.
│
└─ Extraction failed (no Download button, blank pane, error)
    │
    ├─ Retry 2 more times over a 15-minute window
    │   - Wait 5 min, fresh tab, navigate, recheck
    │   - Wait 5 min, fresh tab, navigate, recheck
    │
    ├─ Still failing AFTER 15 min of retries?
    │   │
    │   ├─ Original submission >120 min ago?
    │   │   YES → Thread is "broken" per AS conventions. RESUBMIT FRESH.
    │   │       1. Re-read the original prompt from `as-thread.json` (`prompt_text` field)
    │   │       2. Open fresh Chrome window
    │   │       3. Submit per Phase 1 protocol (Step 3 + Step 3a five-check verification)
    │   │       4. Update as-thread.json:
    │   │          - Mark old thread: status=BROKEN_RESUBMITTED, broken_at=<ISO ts>
    │   │          - Add new thread: new_url, new_thread_id, status=SUBMITTED, resubmitted_from=<old_thread_id>
    │   │       5. Defer extraction of the NEW thread to next Phase 2 cycle (don't try to extract immediately — fresh threads need ≥45 min)
    │   │       6. Set `auto_resubmit_triggered: true` in metadata.json (surfaces in QC footer)
    │   │
    │   └─ Original submission <120 min ago?
    │       NO → Thread may genuinely still be processing. Mark status=STILL_RUNNING. Defer to next Phase 2 cycle (or 03:30 watchdog).
    │
    └─ Log all retry attempts in as-thread.json `retry_log` array (timestamp, attempt #, outcome)
```

### Why 120 minutes?

AS Deep Research typically completes in 45–60 min. 120 min is 2× the upper bound of typical generation time. Beyond this, a thread that hasn't rendered is overwhelmingly likely to be broken (queue stuck, AS-side error) rather than genuinely slow. Empirical evidence: BGN 29-Apr-26 overnight — 5/6 threads showed 0% progress 24h+ post-submission. They were broken; resubmission was the only path forward.

### Why retry 2-3 times over 15 min before resubmitting?

Distinguishes transient render issues (which clear with a fresh tab) from genuinely broken threads. 3 attempts over 15 min covers most transient issues without bleeding watchdog time.

### Escalation

If a SECOND auto-resubmission is needed (i.e. the auto-resubmitted thread itself fails 120 min later), STOP auto-resubmitting and surface to the morning briefing flag with `🚨 AS_REPEATED_FAILURE`. This indicates AS-side service degradation, not a per-thread issue — Richard should test manually before further automated submissions.

### Provenance

Every resubmission preserves the chain in `as-thread.json`:
```json
{
  "query": "Q5 ED",
  "ticker": "BGN",
  "threads": [
    {"thread_id": "1777368911831", "submitted": "...", "status": "BROKEN_RESUBMITTED", "broken_at": "...", "retry_log": [...]},
    {"thread_id": "1777999XXXXXX", "submitted": "...", "status": "EXTRACTED", "resubmitted_from": "1777368911831"}
  ]
}
```

The QC footer block (notion-posting-sop §Step 4.5) surfaces "Auto-resubmit triggered? (Rule #31): Yes (original X, new Y)" so Richard can see when this happened.

---

### ⚠️ Interface Change (15-Apr-26) — PDF Download is Now Primary

The AlphaSense Deep Research interface changed overnight ~14-15 Apr 2026. The old "Copy to Clipboard" button and DOM `.css-x73re6` content panel no longer work on saved URLs — the panel only renders during active generation. **PDF Download is now the confirmed, tested primary extraction method.**

### Primary Method: PDF Download ✅ CONFIRMED WORKING

1. Navigate to the saved [AS] URL
2. **Wait 15–60 seconds** for the page to fully render (AS is a SPA — content streams in after load)
3. Find the **Download button** — it is in the **top-right corner of the report**, outside the main viewport if screenshot width is <1920px. Use the `find` tool with query "Download" to locate it by ref, then `left_click` using the `ref` parameter (not coordinates). The button has `data-testid="ExportToPDFButtonWrapper"` and `aria-label="Download"`.
4. The PDF saves automatically to `COWORK/Files/NOT BACKED UP/Chrome downloads/` — filename format: `DR-Report-by-Alphasense-{MM-DD-YYYY}-{HH-MM}.pdf`
5. Read the PDF using **pdfplumber** (NOT pypdf — pypdf produces spaced-out text artefacts like "RESUL TS")
6. Extract text: take all content **after the line "RESULTS FOR QUERY"**
7. **Strip the following:**
   - Prompt echo block at the top (everything before and including "RESULTS FOR QUERY")
   - Citations / references section (block beginning "Citations" near end of main body)
   - Page number lines (e.g. "Page 1 of 12")
   - AlphaSense legal disclaimer (footer on each page — begins "© AlphaSense" or "AlphaSense is a service mark")
   - Inline footnote markers `[1]`, `[2]` etc. (replace with single space)
   - Table of contents block if present (numbered list of section headings at top)
8. Run cleaned text through `process_report.py` pipeline (Step 6b below)

**If the Download button is not visible:** The report is still generating. Wait longer — do not attempt DOM extraction. Check again after 15+ minutes.

**pdfplumber extraction snippet (confirmed working):**
```python
import pdfplumber, re

def extract_clean(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = [p.extract_text(layout=False) for p in pdf.pages if p.extract_text(layout=False)]
    full = '\n'.join(pages)
    # Strip boilerplate
    full = re.sub(r'©\d{4}.*?AlphaSense.*?\n', '\n', full)
    full = re.sub(r'Page \d+ of \d+\s*\n', '\n', full)
    full = re.sub(r'\s*\[\d+\]\s*', ' ', full)  # footnote markers
    full = re.sub(r'\n{3,}', '\n\n', full)
    # Start content after "RESULTS FOR QUERY"
    idx = full.upper().find('RESULTS FOR QUERY')
    if idx >= 0:
        full = full[idx + len('RESULTS FOR QUERY'):]
    return full.strip()
```

### Alternative: DOM Extraction (only works during active generation)

The `.css-x73re6` container only has content while a report is actively streaming/generating. If you are monitoring a submission in real-time:

1. FULL SCREEN FIRST (1920x1080)
2. Navigate to the AS URL immediately after submission
3. Wait for content to appear (check `document.querySelector('.css-x73re6').innerText.length > 0`)
4. Once content renders, extract: `document.querySelector('.css-x73re6').innerText`
5. Download via Blob to COWORK/Files/
6. Strip endnotes, footnote markers, prompt echo

**This method fails on saved URLs in a new session — content will be 0 chars.**

### Fallback: Clipboard Intercept (legacy — pre-15-Apr-26 interface)

_Only applicable if the old "Copy to Clipboard" button is visible:_

1. Install interceptor and click Copy to Clipboard
2. Download captured plain/HTML blobs
3. Strip artifacts as above

### If Nothing Renders (0 chars)

1. Try the PDF Download method — does not depend on DOM render
2. If PDF download button not visible → report is still generating (wait longer)
3. If PDF download button visible but content blank → escalate to Richard. Do NOT grind >10 minutes

---

## Step 6b: Post-Extraction Processing Pipeline

**Script:** `COWORK/scripts/process_report.py`
**Usage:** `python3 process_report.py {TICKER} {QUERY_TYPE} {input_file_path}`

Pipeline steps:
1. **Clean** — strips prompt echo, footnote markers, source annotations, UI artifacts
2. **Highlight** — keyword-based paragraph-level sentiment classification (green/red/yellow). Target: 30%+ coverage
3. **Chunk** — splits into 14,500-character chunks at paragraph boundaries

Output: `{TICKER}-{TYPE}-chunk-{N}.md` files in `COWORK/Files/` (root, Watson-created — backed up daily)

---

## Step 6c: Merge Dual-Source Outputs (all dual-source queries: #1, #2, #4, #5, #7, #8, #10, #14, #19, #20)

**When:** Both [C] and [AS] outputs are validated and ready for a dual-source query.
**Reference:** RESEARCHER SKILL-V2.md rules #13-18. D-RSR-37 (06-May-26): ALL dual-source queries merge to single page.
**Scope:** IG/Triaging (#1, #2, #4, #5, #7) + ESA (#8, #10, #14) + DD (#19, #20). Same protocol for all stages.

### Pre-Merge Validation Gate

Before merging, verify:
1. **Same query type:** [AS] output answers the same question as [C] (not a different query that drifted)
2. **Substance threshold (revised 24-Apr-26):** [AS] ≥ 3,500 words OR ≥ 40% of [C] word count
3. **Correct ticker:** Company/ticker consistent throughout [AS] output
4. **Same scope:** Same reporting period, same time horizon

**If ANY check fails:** Post [C]-only page. Save [AS] to `COWORK/outputs/{ticker}/raw/` as reference. Log the failure reason.

### Merge Execution

1. **Select backbone** per defaults in SKILL-V2.md rule #14:
   - **IG/Triaging:**
   - #1 (Business Description): [AS] backbone — broker initiation reports provide richest factual base; [C] enriches with analytical framing, cross-sector parallels, quality flags. Override: thin [AS] (<3,500 words) → [C] backbone. (D-RSR-36)
   - #2 (Change Forces): [AS] backbone (unless thin [AS] <3,500 words → [C] backbone)
   - #4 (Earnings trends vs. peers): [C] backbone
   - #5 (Most recent earnings delivery): [C] backbone (unless heavy-coverage stock with data-rich [AS])
   - #7 (KD Assessment — Triaging): [C] backbone (unless thin-coverage stock)
   - **ESA/DD (D-RSR-37):**
   - #8 (BM/Sector Primer): [AS] backbone — broker sector primers + expert calls provide richest industry structure + competitive analysis. Override: thin [AS] (<3,500 words) → [C] backbone.
   - #10 (Short-Sellers): [C] backbone — public bear-case material (short-seller reports, Substack, Reddit) is the unique value. Override: heavy-coverage stock with rich [AS] bear survey → [AS] backbone.
   - #14 (KD Assessment — ESA): [C] backbone — Watson's own driver synthesis is the intellectual spine. Override: thin-coverage stock → [AS] backbone.
   - #19 (Pre-mortem): [C] backbone — framework/conceptual failure-mode reasoning structures the narrative. Override: very rich [AS] expert evidence → [AS] backbone.
   - #20 (CEO/CFO Meeting Prep): [C] backbone — framework-driven question generation structures the document. Override: heavy-coverage stock with rich [AS] Q&A history → [AS] backbone.
   - **Proportional override (all queries, 24-Apr-26):** If [C] word count > 2x [AS] word count, always use [C] backbone regardless of query-specific defaults

2. **Structure the merged page:**
   - Copy backbone source's structure as the page skeleton
   - Weave in the other source's unique material at relevant section points
   - For broker/expert quotes from [AS], use: `**[AS·{broker}]:**` attribution per `notion-posting-standard/SKILL.md` §15 (e.g. `**[AS·Jefferies]:**`, `**[AS·Goldman]:**`, `**[AS·multiple]:**` when multiple brokers, `**[AS·company]:**` for primary docs, `**[AS·expert]:**` for expert calls)
   - For [C] analytical points added to an [AS] backbone, use: `**[C]:**` attribution
   - **Deprecated 30-Apr-26:** the prior `==Per [AS]/[broker]:==` syntax — `==text==` does NOT render in Notion. Do not use.
   - Every factual claim must be traceable to its source

3. **Handle interpretive contradictions** (rule #17):
   - When [C] and [AS] disagree on interpretation: present BOTH views, attributed
   - Do NOT resolve — flag with purple highlight for APM/Richard
   - Format: "**[Analytical disagreement]** [C] assessment: ... [AS] counter-view per [broker]: ..."

4. **Handle thin [AS]** (rule #18, thresholds revised 24-Apr-26):
   - If [AS] < 3,500 words but passes validation: fold unique insights as inline callouts/footnotes
   - Page reads as enriched [C], not a balanced dual-source document

5. **Save raw outputs:** Both raw [C] and raw [AS] texts saved to `COWORK/outputs/{ticker}/raw/{query#}-{source}.md`

6. **Merge content-retention gate (D-RSR-37):** After merge, verify merged word count ≥70% of (raw-C + raw-AS) combined word count. This ensures content was codified/organised into the merged document, not cut. Failure = flag for review before posting. The goal is to codify ALL content — eliminate duplication but preserve breadth, depth, colour, and variety of information and perspectives.

7. **Title the merged page (updated 16-Apr-26):** `[W] {TICKER} - {Stage} - {Query Name} - {5-15 word summary} [C+AS] @ DD-Mon-YY` — Company name NOT included. Summary = substantive descriptor of the merged page's central finding.

### Output

One merged `.md` file ready for Notion posting pipeline (Step 7).

---

## Step 7: Post to Notion

Hand processed output to the Notion Posting SOP (`notion-posting-sop.md`). The posting SOP handles:
- Final highlighting refinement (analytical layer on top of keyword-based)
- Formatting verification (headers, bold, bullets)
- Pre-flight quality gate
- Chunked posting (create page → append chunks)
- Property setting (date, IAJA, depth, case component, Stock(s) relation)
- Post-posting verification

---

## Batch Execution Planning

For multi-stock or multi-query batches:

**Claude [C]:** All prompts launch simultaneously as parallel Sonnet sub-agents. No wave planning needed.

**AlphaSense [AS]:** Haiku submits in waves of up to 10 (concurrent limit confirmed 15-Apr-26).

**Example: 3 stocks × IG (queries #1-3 = 2 AS + 2 C per stock = 6 AS total)**

| Phase | Sonnet [C] | Haiku [AS] |
|-------|-----------|-----------|
| T+0 | Launch 6 [C] agents (3 stocks × 2 [C] queries) | Single wave: all 6 AS reports submitted simultaneously (well within 10-limit) |
| T+5-15 min | [C] outputs return → validate → highlight → post | (waiting) |
| T+45-60 min | [C] posting + verification complete | Sonnet extracts all 6 AS reports → post to Notion |
| T+75 min | All done | All [AS] posted + verified |

**Example: 5 stocks × IG (10 AS reports) = exactly at the 10-concurrent limit → single wave.**

**Example: 6+ stocks = 12+ AS reports → two waves needed.** Wave 1: first 10 → extract → Wave 2: remainder.

Watson calculates [AS] waves before starting and logs the plan in `memory/research-queue.md`.

---

## URL Storage

Watson stores submitted research URLs in `memory/research-queue.md`. Format:

```markdown
## Active Research Queue

| Submitted | Source | Stock/Topic | Query # | URL | Status | Haiku Verified |
|---|---|---|---|---|---|---|
| 2026-04-14 09:15 | AS | DKSH | #1 BD | https://research.alpha-sense.com/... | Pending | Yes — DR verified |

## Completed (last 7 days)
[Moved here after extraction. Pruned weekly.]
```

---

## References

- Query templates: `memory/skills/researcher/templates/`
- Research pipeline logic: `memory/skills/researcher/SKILL-V2.md`
- Notion posting: `memory/skills/researcher/notion-posting-sop.md`
- Diligence checks: `memory/skills/diligence-checks/SKILL.md`
- Corrections log: `memory/corrections.md`
