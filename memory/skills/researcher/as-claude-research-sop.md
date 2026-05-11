# Research Execution SOP — V1 ⛔ DEPRECATED
<!-- [W] Created 02-Apr-26. DEPRECATED 15-Apr-26 — superseded by as-claude-research-sop-v2.md -->
<!-- DO NOT USE. Retained for historical reference only. All active execution uses V2. -->
<!-- Key changes in V2: Haiku AS submission agent; self-contained templates; PDF download extraction (AS interface changed 15-Apr-26); concurrent limit 3→10. -->

## Purpose

This SOP governs how Watson executes research through two sources: **Claude [C]** (native execution) and **AlphaSense [AS]** (browser-based Deep Research). It is the single source of truth for research execution mechanics. All research types (IG, KQ, ESA, monitoring, info flow) use this SOP.

---

## Core Principle: Dual-Source, Different Execution Models

- **Claude [C]:** Watson executes research **natively** — using its own web search, analysis, and writing capabilities. No browser needed. No waiting. Parallel execution via sub-agents.
- **AlphaSense [AS]:** Watson submits prompts via **Chrome browser** to AlphaSense Deep Research. Fire-and-forget with URL bookmarking. 45-minute wait.

The optimal workflow is:
1. Launch all [C] research as parallel native agents (immediate execution)
2. While [C] agents run, submit [AS] prompts to AlphaSense via Chrome (fire-and-forget)
3. Post [C] outputs to Notion as they complete
4. After 45+ minutes, return to AlphaSense URLs, extract [AS] results
5. Post [AS] outputs to Notion

---

## Step 1: Receive Brief & Create Prompts

Watson receives a research brief from Richard (or from a pipeline trigger). Watson creates the appropriate prompts by adapting the relevant templates from `AI Prompts/`.

### Prompt Adaptation for Claude vs AlphaSense

The same base prompt goes to both sources, with one systematic difference:

| Element | Claude [C] | AlphaSense [AS] |
|---|---|---|
| Sell-side research references | **REMOVE** — Watson searches the public web; no access to sell-side reports | **KEEP** — AlphaSense searches proprietary broker research, expert calls, filings |
| Expert/insider interview references | **REMOVE** — same reason | **KEEP** — AlphaSense indexes expert network transcripts |
| Everything else | Keep as-is | Keep as-is |

This is the ONLY difference between [C] and [AS] prompt versions. Watson applies this automatically when adapting prompts.

---

## Step 2: Execute Claude [C] Research — NATIVE

### Method

Watson executes [C] research directly using its own capabilities:
1. Read the adapted [C] prompt (sell-side/expert references removed)
2. Use **WebSearch** extensively to research each topic in the prompt
3. Write the complete memo (~7,000 words for BD/CF) with full analysis, tables, and judgement
4. Save output to a local file (e.g., `/tmp/{ticker}_bd_c.md`)

### Parallel Execution

- Launch multiple [C] research tasks as **parallel sub-agents** — no concurrency limit
- Each agent handles one prompt (e.g., one BD or one CF for one stock/batch)
- For a batch of 4 stocks × 2 prompts = 8 agents running simultaneously
- All agents write to separate output files

### Quality Standards

- Output must be ~7,000 words (BD and CF templates)
- Must follow the section structure from the prompt template
- Include tables, financial data, peer comparisons as specified
- Include judgement and analysis, not just description
- If WebSearch results are thin for a company, flag this and note which sections may be less comprehensive

### Advantages Over Browser Submission

- **No waiting:** Results available in minutes, not 45+ minutes
- **No prompt complexity ceiling:** Full templates can be used as-is (no 6-section limit)
- **No stalling risk:** No dependency on Claude Research mode infrastructure
- **Higher throughput:** Unlimited parallel agents vs. 5-concurrent browser limit
- **Direct quality control:** Watson can judge quality in real-time and supplement research as needed

---

## Step 3: Submit to AlphaSense Deep Research

**CRITICAL: Deep Research mode must be VERIFIED, not assumed. See `memory/skills/diligence-checks/SKILL.md` Check Type 1 + Check Type 4.**

### Submission Protocol (with mandatory verification gates)

1. Navigate to `https://research.alpha-sense.com/gensearch`
2. **BEFORE pasting prompt:** Click "Deep Research" in the mode selector
3. **VERIFY mode selection** (both methods required):
   - **Visual:** Screenshot the mode selector area — "Deep Research" must appear bold/selected
   - **Programmatic:** Run JS check: `aria-pressed` must be `true` on Deep Research button, `Mui-selected` class must be present
   - **Log the result** in conversation: "Deep Research: aria-pressed=true, selected=true"
4. Paste the adapted [AS] prompt into the editor
5. **PRE-SUBMIT CHECKPOINT:**
   - [ ] Deep Research still selected (re-verify via JS — pasting can sometimes reset mode)
   - [ ] Prompt contains correct company/ticker
   - [ ] Screenshot taken showing prompt + mode selector
6. Submit (Enter key)
7. **POST-SUBMIT VERIFICATION:**
   - [ ] URL changed (new thread ID in address bar)
   - [ ] Page shows "Deep Research Report" progress bar
   - [ ] **Sidebar label** shows "Deep Research" under thread title (zoom screenshot to confirm)
   - If ANY of these fail: do NOT proceed. The submission was not in Deep Research mode. Start over.
8. **Copy the browser URL** from the address bar
9. Log URL to `memory/research-queue.md` with "Deep Research verified" status
10. Close the window/tab
11. Repeat for additional prompts

### Sub-Agent Delegation Rule [D] (09-Apr-26)

**If delegating AlphaSense submission to a sub-agent:** The sub-agent prompt MUST include:
- Explicit instruction to click Deep Research before pasting
- Explicit instruction to verify via JS (`aria-pressed=true`)
- Explicit instruction to screenshot sidebar label post-submission
- Explicit instruction to report all three verification results

The parent agent MUST validate the sub-agent's reported verification on return. If the sub-agent doesn't report verification evidence, treat the submission as failed.

### Concurrent Submissions

- **AlphaSense concurrent limit: 3 Deep Research searches at a time**
- For batch submissions exceeding 3, submit in waves of 3
- Submit first wave → copy URLs → close → wait 45 minutes → check first wave → submit next wave if slots are available

### No Project Equivalent

AlphaSense does not have a project/folder system. Each Deep Research query is a standalone thread accessible via its URL.

---

## Step 4: Wait & Do Other Work (AlphaSense only)

- **Minimum wait: 45 minutes** from [AS] submission
- Do NOT monitor progress. Do NOT keep tabs open.
- Watson stores the URLs (see URL Storage below) and moves to other tasks
- Use waiting time productively: post [C] outputs to Notion, run posting verification, work on other tasks
- Do not leave [AS] results uncollected for hours — the aim is to complete the research cycle promptly

---

## Step 5: Return & Retrieve AlphaSense Results

After 45+ minutes:

1. Navigate to each saved [AS] URL
2. Check if research is complete:
   - **AlphaSense:** Complete when the progress bar is gone and full content is visible with section headings. If still generating (Stop button visible), wait longer or click "Show Results" for partial output.

Note: Claude [C] results do not require retrieval — Watson writes them directly and they are immediately available.

---

## Step 6: Extract AlphaSense Results

### AlphaSense [AS] Extraction — Clipboard Intercept Method (tested 03-Apr-26)

**Primary method:** Intercept the AlphaSense "Copy to Clipboard" button via JavaScript, then trigger a blob download to COWORK/Files/. This captures both **plain text** and **rich HTML** (with bold, headers, tables, links — ideal for Notion posting).

#### Pre-requisite: FULL SCREEN

**The browser window MUST be full screen (1920x1080 minimum) before any extraction.** The AlphaSense SPA does not render report content into the `.css-x73re6` container when the window is too small — the container exists but stays empty. Always resize to full screen first. [D] (05-Apr-26)

#### Workflow per report:

1. **Navigate** to the saved [AS] URL
2. **Install clipboard interceptor** via JavaScript (one-time per page load):
   ```javascript
   const origWrite = navigator.clipboard.write;
   navigator.clipboard.write = async function(data) {
     for (const item of data) {
       for (const type of item.types) {
         const blob = await item.getType(type);
         const text = await blob.text();
         if (type === 'text/plain') window._copiedPlain = text;
         if (type === 'text/html') window._copiedHtml = text;
       }
     }
     return origWrite.call(navigator.clipboard, data);
   };
   ```
3. **Scroll to bottom** of report (the response container is `.css-x73re6`):
   ```javascript
   document.querySelector('.css-x73re6').scrollTop = 999999;
   ```
4. **Click "Copy to Clipboard" button** — first icon in the action bar after "Show Results"
5. **Wait 2-3 seconds** for the async clipboard write to complete
6. **Download both formats** as blob files to COWORK/Files/:
   ```javascript
   // Plain text
   const blob1 = new Blob([window._copiedPlain], {type: 'text/plain'});
   const a1 = document.createElement('a'); a1.href = URL.createObjectURL(blob1);
   a1.download = '{TICKER}-{TYPE}-AS.txt'; document.body.appendChild(a1); a1.click();
   // Rich HTML
   const blob2 = new Blob([window._copiedHtml], {type: 'text/html'});
   const a2 = document.createElement('a'); a2.href = URL.createObjectURL(blob2);
   a2.download = '{TICKER}-{TYPE}-AS.html'; document.body.appendChild(a2); a2.click();
   ```
7. **Read files from disk** at `/sessions/*/mnt/COWORK/Files/`
8. **Strip endnotes** (last ~10% of text — everything after `\n\[\d+\]\s+[A-Z]` pattern)
9. **Strip inline footnote markers** (`[1]`, `[2]`, etc.) via regex: `\[\d+\]`
10. **Strip prompt echo** (the "Question" / "REQUEST" block at the top of Copy to Clipboard output)

#### Content characteristics (Copy to Clipboard button):
- **Clean text** — no kerning/spacing artifacts (unlike PDF download)
- **Rich HTML available** — preserves bold, headers, tables, links (854KB for a typical BD report)
- **Includes footnotes** (474 markers in a typical BD) — easy to strip with regex
- **Includes endnotes section** (~10% of total text) — easy to strip by finding boundary
- **Includes prompt echo** at top — strip the "Question" block
- **Does NOT include sidebar/UI** — clean report content only

#### Why this method, not the alternatives:
| Method | Verdict | Reason |
|---|---|---|
| **Copy to Clipboard + intercept** | **PRIMARY** | Clean text, rich HTML, no kerning, automatable |
| PDF Download | Backup | Has kerning artifacts ("r esear ch"), no rich formatting, but works as fallback |
| Ctrl+A + Ctrl+C | Rejected | Includes sidebar junk, excludes footnotes (useful for manual but messy for automation) |
| DOM JS extraction | Rejected | JS tool output truncated at ~1000 chars — fundamentally broken for large texts |
| get_page_text | Rejected | "Page body too large" error on AlphaSense pages |
| read_page accessibility | Rejected | Truncates element text to ~100 chars per element |

#### Alternative Primary Method: Direct DOM Extraction (tested 05-Apr-26, used for 22-report batch)

When the clipboard intercept method is unavailable or unreliable, direct DOM extraction works well for bulk processing. This was the method used successfully for the entire 03-Apr batch (22 reports).

**Workflow per report:**

1. **FULL SCREEN FIRST** — `resize_window(1920, 1080)` before anything else
2. **Navigate** to the saved [AS] URL in an existing or new tab
3. **Wait 25 seconds** for full page load
4. **Take a screenshot** to verify the page state (content visible, not loading)
5. **Close the Results panel** — click the X button at approximately (636, 63) on the page. The Results panel (centre panel showing source documents) squeezes the content container and prevents rendering
6. **Wait 5 seconds** for content to re-render in the expanded container
7. **Scroll to bottom** to trigger lazy-loaded content:
   ```javascript
   document.querySelector('.css-x73re6').scrollTop = document.querySelector('.css-x73re6').scrollHeight;
   ```
8. **Extract text:**
   ```javascript
   document.querySelector('.css-x73re6').innerText
   ```
9. **Download via Blob:**
   ```javascript
   const text = document.querySelector('.css-x73re6').innerText;
   const blob = new Blob([text], {type: 'text/plain'});
   const a = document.createElement('a');
   a.href = URL.createObjectURL(blob);
   a.download = '{TICKER}-{TYPE}-clipboard-copy.txt';
   document.body.appendChild(a); a.click();
   ```
10. **Verify file on disk** — check file size is >0 bytes. If the Blob download saved 0 bytes, retry with **data URI fallback**:
    ```javascript
    const text = document.querySelector('.css-x73re6').innerText;
    const a = document.createElement('a');
    a.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(text);
    a.download = '{TICKER}-{TYPE}-clipboard-copy2.txt';
    document.body.appendChild(a); a.click();
    ```
11. **Read file from disk** and process through the Python pipeline

**Why this works:** The `.css-x73re6` container holds the full report text once the browser viewport is large enough (1920x1080+) and the Results panel is closed. No clipboard interceptor setup needed.

**When to use which method:**
- **Clipboard Intercept** — best for single reports where you want both plain text AND rich HTML
- **Direct DOM Extraction** — best for bulk processing (faster setup, no per-page interceptor installation)
- Both require full-screen viewport and closed Results panel

#### Fallback: PDF Download
If both DOM extraction and clipboard intercept fail (page reload, JS error), use the Download button instead:
1. Scroll to bottom, click Download icon (arrow-down, in action bar)
2. PDF saves to COWORK/Files/ as `DR-Report-by-Alphasense-{date}-{time}.pdf`
3. Read via pypdf: `from pypdf import PdfReader; reader = PdfReader(path)`
4. **Post-process required:** Fix kerning artifacts (regex: `r'(\w) (\w)'` patterns like "r esear ch" → "research"). This is lossy — DOM/clipboard methods are strongly preferred.

#### If Nothing Renders (0 chars in container)
Recovery protocol (confirmed 05-Apr-26):
1. Check viewport — must be 1920x1080. `resize_window(1920, 1080)` and retry
2. Check Results panel — must be closed. Click X at (636, 63) and retry
3. If still 0 chars — restart Chrome entirely and retry from step 1
4. If still 0 chars after Chrome restart — escalate to Richard immediately. Do NOT grind for >10 minutes

Save extracted output locally before posting.

Note: Claude [C] outputs are already in local files — no extraction step needed.

---

## Step 6b: Post-Extraction Processing Pipeline

After extraction, run the Python processing pipeline before posting to Notion.

**Script location:** `COWORK/scripts/process_report.py`

**Usage:** `python3 process_report.py {TICKER} {BD|CF} {input_file_path}`

**Pipeline steps:**
1. **Clean** — strips prompt echo, footnote markers (`[1]`, `[2]`), source annotations, UI artifacts
2. **Highlight** — keyword-based paragraph-level sentiment classification (green/red/yellow, ~40 green keywords, ~50 red, ~35 yellow). Minimum 2 keyword hits per paragraph. Target: 30%+ coverage
3. **Chunk** — splits into 14,500-character chunks at paragraph boundaries (Notion has ~15K char limit per API call)

**Output:** Creates `{TICKER}-{TYPE}-chunk-{N}.md` files in `COWORK/Files/`

**Posting from chunks:**
1. Create page with chunk 1 content via `create-pages` (include all properties)
2. Append chunks 2-N sequentially via `update-page` with `update_content` command
3. Match the last unique line of existing content as `old_str`, append new content as `new_str`
4. Verify each append succeeded before moving to the next chunk

---

## URL Storage

Watson stores submitted research URLs in `memory/research-queue.md`. Format:

```markdown
## Active Research Queue

| Submitted | Source | Stock/Topic | Prompt Type | URL | Status |
|---|---|---|---|---|---|
| 2026-04-02 09:15 | Claude | DHER | BD [C] | https://claude.ai/chat/... | Pending |
| 2026-04-02 09:16 | AS | DHER | BD [AS] | https://research.alpha-sense.com/... | Pending |

## Completed (last 7 days)
[Moved here after extraction. Pruned weekly.]
```

Watson creates this file if it doesn't exist. Updates it when submitting, when extracting, and at session handoff. This provides an audit trail and makes it easy to resume if a session is interrupted.

---

## Batch Execution Planning

For multi-stock or multi-prompt batches, Watson plans execution as follows:

**Claude [C]:** All prompts launch simultaneously as parallel sub-agents. No wave planning needed — there is no concurrency limit for native execution.

**AlphaSense [AS]:** Wave planning required due to 3-concurrent-search limit.

**Example: 3 stocks x 2 prompts each = 6 Claude + 6 AlphaSense = 12 total**

| Phase | Claude [C] (parallel, no limit) | AlphaSense [AS] (limit 3) |
|---|---|---|
| T+0 | All 6 [C] agents launch simultaneously | Wave 1: Stock A BD, Stock A CF, Stock B BD |
| T+5-15min | [C] outputs complete, begin Notion posting + verification | (waiting) |
| T+45min | [C] posting complete, verification passed | Wave 1 extraction + Wave 2: Stock B CF, Stock C BD, Stock C CF |
| T+90min | All [C] done | Wave 2 extraction, all [AS] posting + verification |

Watson calculates [AS] waves before starting and logs the plan in the research queue.

---

## Quality Checks (Pre-Posting)

Before handing output to the Notion Posting SOP:

### Claude [C] Outputs (Native)
- Word count: BD should be >3,000 words; CF should be >4,000 words; KQ should be >3,000 words
- Structure: All sections from the prompt template covered?
- Quality: Tables present? Peer comparisons included? Judgement in each section?
- If thin on a particular section due to limited web search results, flag for Richard

### AlphaSense [AS] Outputs (Browser)
- Is the output complete? (Not truncated, not a partial/stalled result)
- Does it match the prompt? (Correct stock, correct research type)
- Is it substantial? (Same word count thresholds as above)
- If output is too short or clearly incomplete, retry with the same or modified prompt

---

## References

- Prompt templates: `AI Prompts/` directory
- Notion posting: `memory/skills/researcher/notion-posting-sop.md`
- Research pipeline logic: `memory/skills/researcher/SKILL.md`
- Corrections log: `memory/corrections.md` (search for "Claude Research" and "AlphaSense" entries)
