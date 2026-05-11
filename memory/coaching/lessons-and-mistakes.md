---
name: Lessons and Mistakes
description: Specific lessons and mistakes Richard has documented — high-value for preventing repetition
type: user
---

# Lessons and Mistakes — Extracted from Personal Journal and Stock Notes (Pre-Nov-25 through Mar-26)

## WATSON / SYSTEM LESSONS

### Scheduled Task COWORK Mount Failure — Root Cause and Fix (28-Apr-26)

**Incident:** The gym-trio overnight RESEARCHER task (00:30 UK, 28-Apr-26) failed to run AS submissions. The task correctly ran all [C] research (20 Notion pages posted) but skipped all AlphaSense submissions. Initial diagnosis (from Watson) was incorrect — blamed "Chrome browser unavailable overnight." Chrome was in fact open.

**True root cause:** The scheduled task called `mcp__cowork__request_cowork_directory` as its first pre-flight step to mount the COWORK folder. This tool presents a folder-access **permission dialog** in the Cowork UI that requires Richard's physical approval. At 00:30, Richard was asleep. The session stalled on the very first step and never reached the AS submission phase. The [C] research that completed was produced by the session eventually proceeding with some native work, but the AS submissions (which require Claude in Chrome, a later step) were never attempted.

**Why the initial diagnosis was wrong:** Watson looked at the completion report's own statement ("browser agent unavailable") rather than reading the actual session transcript. The transcript showed the stall point clearly: the session's second tool call was `mcp__cowork__request_cowork_directory`, and no further AS-related activity followed.

**Lesson 1 — Diagnose from evidence, not from reports written by the thing that failed.** The completion report was written by the same session that failed. It contained a self-serving mis-diagnosis. The correct diagnostic approach is to read the raw session transcript, which shows exactly where execution stopped. Watson should have done this immediately rather than reasoning from the report.

**Lesson 2 — The COWORK mount step must be removed from scheduled task prompts.** COWORK is mounted persistently in live Cowork sessions. Scheduled tasks that include a `request_cowork_directory` call will always fail unattended because that tool requires UI approval. The fix: remove the mount step from all scheduled task prompts entirely. The COWORK folder is available via its mount path without re-requesting.

**Solution implemented:** Remove `request_cowork_directory` pre-flight from scheduled task templates. Rely on the standing COWORK mount (`/sessions/*/mnt/COWORK/` in bash, `C:\Users\richb\Documents\COWORK\` via file tools). This is already how successful overnight batches (e.g. cables/grid 25-26 Apr) operated.

**Secondary fix — Solution 2:** For tasks that do need a live session context (e.g. AS submissions via Chrome), schedule them during waking hours rather than 00:30. AS submissions don't benefit from running at midnight — the 45-min wait means extraction would happen at ~01:15 anyway. A 07:30 schedule gives the same overnight production with none of the permission-dialog risk.

---

### Overnight Research — Planned Future Start Requires a Scheduled Task (28-Apr-26, MTRS)

**Incident:** Richard asked Watson to run the full IG + Triaging RESEARCHER SOP for Munters Group (MTRS-SE). He specified "do not start research until 04:15 UK time on 28-Apr-26." Watson agreed to this timing, completed the back-brief, received confirmation — and then did nothing. No scheduled task was created. The research did not run at 04:15. When Richard checked in the next morning, nothing had been done.

**Root cause — no mechanism to action the agreed start time:**
Watson treated "start at 04:15" as a conversational acknowledgement rather than a binding operational commitment requiring a mechanism. The instruction implied autonomy and an unattended start. But without a scheduled task, Watson has no way to initiate work after a session ends. Live sessions are not persistent — Watson cannot "wake up" at a future time. The only way to honour a future timed start is to create a scheduled task before the session closes.

**Lesson 1 — Planned future starts require a scheduled task. Full stop.**
If Richard specifies a future time for Watson to begin work ("start at 04:15", "run this overnight", "do this while I sleep"), Watson must create a scheduled task in that same session before the conversation ends. If Watson cannot create the task for any reason, it must flag this explicitly: "I cannot guarantee this will run without a scheduled task — shall I create one now?" Verbal agreement to a future time is not execution.

**Lesson 2 — Close the loop before closing the session.**
When a commitment has been made for future autonomous execution, the last action before session close must be: confirm the scheduled task exists, confirm the trigger time, confirm the prompt is correct. If no task has been created, the loop is open. Open loops are failures waiting to happen.

**Lesson 3 — Don't diagnose from self-written reports.**
When reviewing what happened (or didn't happen), read the raw evidence — transcripts, file timestamps, task lists — not summary reports written by the session that failed. A failing session's self-diagnosis is unreliable. This mirrors the COMET lesson from the same date.

**Compound lesson — the pattern across three same-day failures (28-Apr-26):**
Three separate overnight failures occurred on the same date (gym-trio, COMET, MTRS) each with a distinct but related root cause: (1) COWORK mount dialog stalled an unattended session; (2) scheduling collision consumed context before AS phase; (3) no scheduled task created at all. The common thread: Watson agreed to autonomous future execution without confirming the mechanism. The fix in all cases is the same: before session close, confirm the execution mechanism exists and is operational.

**Corrective action:** Research executed immediately in live session on 28-Apr-26 when failure discovered.

---

### 28-Apr-26 — Overnight Watchdog 03:30 Retry — out-of-cycle fire and Task B premature fires

**Incident:** The standing `watson-overnight-watchdog-0330` (cron `30 3 * * *`) fired at **14:08 BST on 28-Apr** instead of 03:30. On the same day, `vod-ig-triaging-task-b-28apr` (scheduled fireAt `2026-04-29T02:30:00+01:00`) fired twice prematurely — at 13:04 BST and 14:05 BST on 28-Apr — roughly 12 hours before its scheduled time. Both Task B fires correctly took the STOP path (Task A had not produced any inputs) and no work was corrupted.

**What was missing:** Nothing was actually missing in terms of overnight outputs — Tasks A and B for VOD-GB are scheduled for tonight (29-Apr 01:00/02:30 BST) and have not yet been due. The "miss" was schedule discipline: the watchdog and Task B both fired at times wildly different from their stated schedules.

**Why (best inference):** The scheduled-task system either (a) accepted ad-hoc/manual triggers as if they were the canonical fire, or (b) has a fireAt/cron parsing or tz issue. Two separate tasks misfiring on the same day in similar magnitude (~12h early) suggests a system-level issue rather than a per-task config error. A previous bash-heredoc-induced JSON corruption of `overnight-status-2026-04-29.json` (truncated to 1440 bytes) was also discovered and repaired during this run.

**Retry outcome:** No retry was attempted. The 03:30 watchdog SOP says retries should defer to overnight scheduling, and firing Task A at 14:08 BST would have (i) defeated overnight scheduling, (ii) risked colliding with the genuine 29-Apr 01:00 Task A fire. Diagnosis written to `overnight-status-2026-04-29.json` (`watchdog_03_30` block, run_history entry) and to `morning-briefing-flag.md`. Two anomalies surfaced for Richard's attention.

**Lessons:**
- **Watchdogs must verify their own clock alignment before retrying.** If a watchdog fires outside its expected window relative to the work it's meant to retry, the safe action is to log and exit, not to fire speculative work.
- **Self-written completion flags can lie.** The pre-existing `overnight-status-2026-04-29.json` claimed Task B "completed" at 02:30 BST on 29-Apr, but its file mtime was 13:04 BST on 28-Apr — written ~13 hours before the timestamp it asserted. Trust mtime over self-reported timestamps when diagnosing.
- **bash heredoc + Python `-c` quoting can silently corrupt files** (per existing memory `feedback_bash_heredoc_bang_escape.md`). When updating JSON files, write the script via the Write tool first and execute the file — never embed long Python in a heredoc.

---

### 29-Apr-26 — Overnight Research Failed Despite Watchdog Retries — AS Rendering Blocked All Night

**What was supposed to run:**

Three separate research briefs were live for the night of 28/29-Apr-26:

1. **BGN (Banca Generali) Task B** — Extract 6 AS threads (Q1 BD, Q2 CF, Q4 ET, Q5 ED, Q6 SS, Q9 EH) generated overnight 27/28-Apr. Post 6 Notion pages. AS threads confirmed present at session close on 28-Apr.
2. **VOD-GB (Vodafone) Task A + B** — [C] research + 5 AS thread submissions (Q1/Q2/Q4/Q5/Q6) + extract + post 7 Notion pages.
3. **ESA Block — EKTA / HTRO / HTWS-GB Task E + F** — 7 [C] files + 9 AS thread submissions (Task E, 05:45 BST) + extraction + ~15 Notion pages (Task F, 07:30 BST).

**What ran:**

- **VOD-GB Task A** — Completed ~00:14–00:32 BST. All [C] files written to disk. 5 AS threads submitted (Q1/Q2/Q4/Q5/Q6). VOD-GB Q3 [C]-only posted (1 page, Notion: 35135e909b0b813b9001d7dee9919002).
- **ESA Task E** — Completed ~07:30–08:35 BST. 7 [C] files written (all passing word-count gates). 9 AS threads submitted and verified (EKTA Q10/Q14, HTRO Q14, HTWS Q8/Q9/Q10/Q12/Q13/Q14).
- **BGN Task B** — Never ran. The overnight task only executed VOD-GB; BGN brief was not picked up.

**What was missing after both 03:30 and 06:30 watchdog checks:**

- **BGN:** 0 of 6 pages. All 6 AS threads (generated 27/28-Apr) blank at both watchdog passes.
- **VOD-GB:** 5 of 6 AS-dependent pages. All 5 STILL-RUNNING threads blank at both passes. Q7 [C]-only also not posted.
- **EKTA:** 0 of 4 pages. Both ESA threads (submitted ~07:30 BST) blank at 06:30 check.
- **HTRO:** 0 of 2 pages. Q10 re-post (no AS needed) not executed; Q14 thread blank.
- **HTWS-GB:** 0 of 9 pages. Q11 [C]-only not executed; all 6 AS threads blank.
- **Total: 1 of ~22 expected pages posted.**

**Hypothesised cause:**

AlphaSense content panels rendered blank in Chrome across ALL threads — including BGN Q7 KD (a known-complete thread successfully extracted in a live session on 28-Apr used as a control test). This rules out content availability as the cause. The rendering failure is an AS interface/session issue: the authenticated Chrome session in the scheduled task context is either (a) experiencing a stale auth/cookie state that prevents content rendering, or (b) the AS gensearch UI is requiring a user interaction (click, scroll, focus event) that the unattended Chrome context cannot provide. The Copy-to-Clipboard button was absent on every thread tested at 03:30 and 06:30. The blank-pane pattern is structurally identical to the "false negative" known pattern (JS DOM check returns 'Generative Search') documented in SKILL-V2.7, except that in prior successful unattended runs the Copy button eventually appeared after sidebar navigation. On this occasion it did not appear after multiple sidebar interactions.

**What Richard needs to do manually in a live session:**

1. Open AlphaSense in Chrome — check if threads now render (Copy button visible).
2. If rendering restored: run extraction protocol per brief-cards in order (BGN first, then VOD-GB, then EKTA/HTRO/HTWS-GB).
3. Three pages can be posted immediately without AS (VOD-GB Q7 KD, HTRO Q10, HTWS-GB Q11) — priority quick wins.
4. If threads still blank: test resubmitting one thread manually to confirm AS is not down.

**Pattern / structural observation:**

This is the second overnight cycle (27/28-Apr first observed) in which AS interface rendering failed for extraction in unattended context. The 28-Apr live session succeeded in extracting (BGN Q7 KD) using an identical protocol. The differentiating factor appears to be: live session = Richard present, Chrome in active use = content renders. Unattended = Chrome not actively used = content pane blank. The unattended extraction protocol may require a "warmup" interaction (navigate to AS home, click around briefly) before navigating to a specific thread URL.

**Follow-up investigation for Systems Architect:** Consider whether a Chrome warmup step (navigate to AS home, brief interaction, then navigate to thread) before each extraction would resolve the blank-pane issue in unattended context.

---

## STOCK-SPECIFIC LESSONS

### BFF — The Cockroach Lesson (Feb-26, HIGH PRIORITY)
1. **Endowment bias, commitment bias** — held too long despite mounting evidence
2. **ACH threshold breached = EXIT; don't wait until getting closer** ("walking towards fire")
3. **Don't let fallen SP stop right action** — fear of future regret (FOFR) paralysed him when SP fell 10-15% on SS downgrade
4. **Cockroaches lesson** — problems are never isolated; first cockroach implies more
5. **"Worser, weirder, further, longer"** — problems compound and extend beyond initial expectations
6. **Trust my gut** — "felt IR was diagnostic and was super weird in Jan-26 call"
7. Bad hiring, no respect for great people, bad IR — red flags he should have weighted more heavily

### XVIVO — The Complexity Trap (Jan-26, HIGH PRIORITY)
1. **Execution not potential** — judge companies on what they DO, not what they COULD do
2. **"Do the basics"** — errors took too long to solve, seemed silly (kidney in US)
3. **Errors in one organ were first cockroach** — same cockroach pattern as BFF
4. **Too much detail, no simple ACH invalidation guide** — got lost in trees, missed forest
5. **"Learning all that stuff was trees not wood. Narrow frame distraction"**
6. **Legacy moat, not reinvestment or execution moat** — critical distinction
7. **Got to meet management teams + assess quality vs. product** — process reminder
8. **"Not hell yeah" = don't invest** — Xvivo was too complex, too many moving parts
9. **"Too complex"** — explicit invalidation reason
10. **CFO assessed as "poor — bottom quartile"** — this alone should invalidate

### Goodwin — The IR Fragility Lesson (24-Mar-26)
- Share price down 40% on earnings because expected contract didn't come through
- "Cause — poor investor support and lack of IR"
- **Lesson: "Reiterate the lesson and standard re. helpful and conservative investor relations"**
- Small cap businesses are fundamentally more fragile to IR failures

### Avanza — The Vague Numbers Lesson (27-Mar-26)
- "Not my Avanza with CEO meeting — vague, because I was vague on the numbers"
- **Lesson: Keep IR calls very financial-centric. Must have a model ready (at minimum sell-side)**
- Made into formal SOP

### Adyen — Predictability and Timing (18-Mar-26)
- "Growth reset in Feb. Share price from 1400 to 850"
- **Lesson: predictability, waiting for bottom, concentration risk**

## PROCESS AND BEHAVIOURAL LESSONS

### Invalidation — The Master Lesson (appears 5+ times)
- "ACH threshold breached = exit. Don't wait" (BFF)
- "Deterioration in TIs: exit, not reduce" (22-Feb-26)
- Three reasons to exit on deterioration: (1) sentiment support gone, (2) fundamental skew down, (3) return on time falls 90%
- "Hence invalidation on deterioration in KD TIs. Even when it seems early."
- **The mistake pattern:** Richard knows the stock should be exited but delays because of FOFR, endowment bias, or hope

### The Ostriching Mistake (Nov-25)
- "Avoided looking at prices. Still ostriching. Should be checking at 1000h. It is ostriching" (09-Nov-25)
- "Didn't see BFF earnings!" (09-Nov-25)
- **Lesson:** Not monitoring positions is not risk management — it's avoidance

### The Complexity Creep Mistake (recurring)
- "Too much detail, no simple ACH invalidation guide fails" (XVIVO)
- "Solving for 'perfect' not 'alpha test' simple version" (Steve Ward)
- "Over-complication" (Steve Ward)
- **Pattern:** Richard's natural depth of analysis becomes counter-productive when it delays action

### The "Not Finishing Insights" Mistake (recurring)
- Multiple journal entries contain "FINISH THIS" or "FINISH WRITING UP THIS INSIGHT"
- Insights are generated but not completed, embedded, or actioned
- **Cost:** Insights get lost, lessons not embedded, same mistakes repeat

### The Listening Mistake (Mar-26)
- "Good preparation for what I wanted to say — but not for what I didn't want to hear" (16-Mar-26)
- "Tried to convince him rather than listen — silly"
- **Lesson:** In negotiations and difficult conversations, listen first

### Morning Routine Slippage (recurring)
- "No morning routine done — for a long time now" (26-Mar-26)
- "Ditto meditation" (26-Mar-26)
- **Cost:** Loss of the mental/emotional energy and clarity that the routine provides

## MARKET/MACRO LESSONS

### The Big Waves Lesson (23-Mar-26)
- "There have been a few big, simple, obvious mega trends to have ridden — AI, gold, oil"
- "These are the simple, obvious themes to OWN rather than trying to navigate around them"
- **Lesson:** Be thematically agnostic, watch all sectors, ride 2-3Y waves

### Telecoms Lesson (Feb-26)
- "Learning from the SPs all going up 50-100%"
- Reminder: "+34% vs +4% and could've been another 10-20% easily" (Feb-26 playbook)
- **Lesson:** The playbook works when executed. Trust it.

---

## Roam Journal Content (Pre-Nov-25)

### Biggest Portfolio Management Lesson (Life to Date)
- "The need to make the early, big decisions and get them right."
- "Getting those wrongs/missing them/not making them cleanly/decisively leads to five much smaller, more myopic/minor decisions that aren't important."
- "I knew it was all about system in balance, looking three steps ahead, but wasn't making it happen—struggling with management/interpersonal friction."

### Insider Ownership ≠ Alignment
- MasMovil/Orange: valued at 2-3x equity at takeout. "Large insider ownership is great but NOT the exact same as alignment of interests."
- Exasol and anecdotes from Andrew Hollingsworth reinforce this.

### Growth Sweet Spot Quantified
- "20-30% revenue/earnings growth is the sweet spot."
- "10% growth = inflection unlikely. 50-70% = too hard to forecast, stumbles likely."
- "It's like driving a car through London at 75mph vs 30mph. Sexy isn't always smart."
- Negative examples: Medartis, Xvivo, Delivery Hero, Wise plc, Cazoo.

### Top-Slicing Discipline
- Don't hold stretched positions sentimentally. Must see better R/R at current price.
- Need positive optionality emerging + cone of uncertainty narrowing to justify bigger size at higher SP.
- Snowball/flywheel test: is the business and case getting STRONGER with time? If not, top-slice.

---

### Overnight Scheduled Task — AS Unavailable: Root Cause & Solutions (28-Apr-26, COMET Research Review)

**Context:** COMET Holding AG (COTN-CH) IG + Triaging research was scheduled overnight (03:30 UK, 28-Apr-26). The [C] research agents completed and saved to disk (5 files, 22,468 words total). All 6 AS submissions were logged with valid URLs. But no AS extraction, no merging, no Notion posting occurred. Task appeared complete but was only ~40% done.

**Observed symptoms:**
- Folder structure `COWORK/Files/COTN-CH/` existed with [C] raw and formatted files
- 6 AS URLs present in `research-queue.md` with status PENDING
- No `metadata.json` files anywhere
- No Notion page IDs
- No completion report
- `lastRunAt` timestamp matched `watson-morning-routine` (06:03 BST) — not the 03:30 fire time

**Root cause — scheduling collision consumed task context:**
The `comet-ig-triaging-research` task (fireAt 03:30) and `gym-trio-ig-triaging-esa` (fireAt 00:30) both showed identical `lastRunAt: 2026-04-28T06:03:57` — the same timestamp as `watson-morning-routine`. All three tasks were absorbed and executed within the single morning-routine session at 06:03, not at their individual scheduled fire times. The morning-routine session ran three substantial research workstreams simultaneously. Context exhausted. The [C] work completed (fast — native Sonnet agents, minutes each). The AS extraction phase — which requires: wait 45+ min → Chrome browser → PDF download → pdfplumber extraction → merge → highlight → post — never executed before the session ended.

**Secondary factor — COWORK mount request in scheduled task prompts:**
As documented in the gym-trio incident (same date, same file), scheduled tasks that call `request_cowork_directory` as a pre-flight step will stall on a UI permission dialog when Richard is asleep. This was also present in the COMET task prompt. Combined with the scheduling collision, this created a double failure mode.

**Why Watson's first status report was incomplete:**
Watson checked file existence and word counts (correct), checked the scheduled task list (correct), but did not check for Notion page IDs or metadata.json files — which would have immediately revealed that nothing had been posted. The status report described the [C] outputs as "complete" without confirming the end-to-end pipeline (save → merge → post → verify) had finished. Lesson: completion = Notion pages posted + page IDs confirmed, not just raw files on disk.

**Solution 1 — Time-stagger overnight research tasks (procedural fix):**
Schedule each research task at a different time with sufficient separation that each gets its own dedicated session context. E.g. COMET at 01:00, gym-trio at 03:30. The morning routine at 06:00 then finds no research tasks left to absorb. Each task runs in isolation with a full context window, and the 45-min AS wait falls naturally within the task's own session. Low engineering overhead — just scheduling discipline.

**Solution 2 — Split [C] and [AS] into two separate tasks (structural fix):**
Architect overnight research as a two-task pipeline:
- Task A (fires at 01:00): runs all [C] agents + submits all [AS] prompts → saves URLs → exits immediately. Fast: completes in ~15 min.
- Task B (fires at 02:00, 60 min later): picks up the saved URLs → extracts all AS PDFs → runs merges → highlights → posts to Notion → verifies. No waiting required — reports are already ready.

Each task is short, focused, and has a clear completion boundary. No single task needs to hold a 45-min wait open. More robust to context pressure, session drops, and tool approval delays. Higher setup cost but eliminates the class of failure entirely.

**Recommendation:** Solution 2 for any research stock where unattended overnight completion is required. Solution 1 as a quick fix for ad-hoc scheduling.

**Corrective action taken:**
AS extraction, merging, and Notion posting for COMET completed manually in a live session on 28-Apr-26 (this session). All 7 pages posted. See `COWORK/Files/COTN-CH/completion-report-28Apr26.md` for full details.

---

### MTRS-SE Live Session — AS Submission URL Verification (28-Apr-26)

**Context:** MTRS-SE IG + Triaging research (queries #1-7) was run in a live session on 28-Apr-26. All 5 [C] memos had been produced and saved to disk. Six concurrent Haiku agents were dispatched to submit [AS] prompts for queries #1, #2, #4, #5, #6, #7.

**Issue 1 — Duplicate thread URLs across agents:**
Two of the six Haiku agents returned the same thread URL (`409385__1777369650790`). This is almost certainly because both agents were operating in the same browser session and one agent navigated to a URL that the other had already created — i.e., the second agent's "new submission" was actually the first agent's thread. AlphaSense's SPA (single-page application) doesn't isolate tabs from each other's sidebar state, so multiple Haiku agents running simultaneously can see and navigate to each other's newly-created threads.

**Issue 2 — Generic URL on first Haiku return (#5 Earnings Delivery):**
One agent returned `https://research.alpha-sense.com/gensearch?mode=deep` without a thread ID, indicating the submission either (a) didn't create a new thread, or (b) the agent reported the URL before the thread ID appeared in the address bar. The sidebar text later showed a thread corresponding to the correct query title, suggesting submission likely succeeded.

**Issue 3 — SPA rendering made JS DOM verification unreliable:**
All standard JS approaches to enumerate sidebar thread links returned empty results. AlphaSense uses React Router with dynamic rendering — anchor tags with `gensearch/` hrefs are not present in the static DOM. Th
### 1-May-26 — BRIGHT SPOT: Mission Command + 3 Gaps back-briefing produced 27 brief items in one morning with 0 misunderstandings (Memo specimen V11→V20)

**Incident (positive):** Across V11→V20 of the Sheet 3 visual style memo specimen (1-May-26 ~05:30 → ~06:40 UK), Watson took 27 brief items through Mission Command parse + Three Gaps diagnostic + back-brief BEFORE writing any code, on every single round. Result: zero round-trips for misunderstanding, zero deliveries Richard had to bounce back as wrong, and 10 versions shipped live in ~70 minutes.

**Richard's feedback (2026-05-01 ~07:00 UK):** *"The way we have worked on this specific part of the project over last 12-24 hours is great. You backbriefing in mission command and 3 gaps style has been superb to help us avoid misunderstandings."*

**Five whys — why did this work so well?**

**Why 1 — Why was there zero misunderstanding across 27 brief items?**
Because every brief was parsed, ambiguities surfaced as questions BEFORE Watson touched files, and the back-brief made Richard's intent legible to both parties before execution started.

**Why 2 — Why did parsing first prevent misunderstanding?**
Because Richard's briefs are dense and often compress multiple changes into single sentences (e.g. "make rating pills smaller" — does that mean nav, main, both, all sizes, or summary-only?). Without parse, Watson would have made one of two failure choices: (a) execute the most-permissive interpretation and waste effort, or (b) execute the most-restrictive interpretation and under-deliver. Parse forces the disambiguating question into the back-brief.

**Why 3 — Why does parsing surface those questions reliably?**
Because Mission Command has a fixed schema (Context / Objective / Higher Intent / Specific Requests / Constraints) and Three Gaps has a fixed schema (Understanding / Alignment / How-to). The schemas force Watson to fill every box. Empty boxes are visible — they ARE the questions Watson must ask. There's no place to hide an unexamined assumption.

**Why 4 — Why do schemas catch what intuition misses?**
Because intuitive parsing falls into the trap of pattern-matching to similar past briefs and assuming the same answer. Schema parsing forces Watson to re-derive each component from THIS brief's content, not from cached pattern-match. The schema is a forcing function for fresh thinking.

**Why 5 — Why is fresh thinking so much higher-quality than pattern-match?**
Because Richard iterates fast and changes course often. Each brief is a slightly-different problem. Pattern-match to "last similar brief" produces stale solutions. Fresh derivation produces solutions that fit THIS brief specifically. Over 27 items in one morning, the cumulative drift between pattern-match-Watson and fresh-derivation-Watson is enormous. The schemas keep Watson honest at the start of each brief.

**Lesson (durable, universal):** **Schema-driven parsing > intuitive parsing for high-density, fast-iteration work.** The Mission Command + Three Gaps frame is not ceremony — it's a forcing function that prevents pattern-match shortcuts. Apply it ALWAYS for non-trivial briefs. Skip only on truly trivial commands (single tool call, no judgement required).

**Corrective action / how to compound:**
1. Codified in CLAUDE.md Operating Method already (added 28-Apr-26 in Agency Under Friction reform). This morning's V11→V20 arc was the largest-N validation to date.
2. Make this a self-reinforcing pattern: every successful arc like this should produce a bright-spot entry that names the mechanism (back-briefing) so Watson can trace the cause-effect chain in future sessions.
3. Watch for the failure mode: a brief that "feels obvious" is exactly when pattern-match shortcuts try to skip the parse. Use the FRICTION = ENGAGE rule (UWB-2) — when Watson feels it could just dive in, that's the signal to back-brief instead.

---

### 1-May-26 — BRIGHT SPOT: Persistent file-saving discipline eliminated session-compaction loss across 10-version morning arc

**Incident (positive):** Across V11→V20, Watson wrote 10 FULL-BACKUP folders, 40+ pre-write `.bak-pre-vN` files, continuously updated state.md after every version, and ran the GitHub push immediately after every build. When session compaction risk was raised by Richard at 07:00, the answer was "no exposure — every artefact is on durable COWORK disk and on GitHub." Zero context loss this morning.

**Richard's feedback (2026-05-01 ~07:00 UK):** *"You are also saving files to the project regularly — we are not suffering from session compaction in the same way as the past. This is great."*

**Five whys — why did persistent file-saving prevent compaction loss?**

**Why 1 — Why was there no compaction loss across 10 versions?**
Because every meaningful state change was written to a file in COWORK durable storage immediately. Session context could compact freely without losing any work product.

**Why 2 — Why did writing immediately matter?**
Because session context is unreliable. Watson cannot predict when compaction will occur. The only way to guarantee survival is to externalise state to the filesystem before context might shrink. Anything held in conversational memory only is at risk.

**Why 3 — Why is the filesystem more reliable than conversational memory?**
Because the filesystem has an explicit lifecycle: files persist until explicitly deleted. Conversational memory has an implicit lifecycle: tokens are evicted on a schedule Watson doesn't control. The mismatch in reliability is enormous — filesystem ~ 100% reliable until deletion; conversational memory ~ 0% reliable past compaction threshold.

**Why 4 — Why did Watson learn to do this consistently this morning when past sessions had compaction loss?**
Three structural changes had landed in CLAUDE.md before this morning that combined to enforce the discipline:
- (a) **Operating Values: Quality > Speed** (28-Apr-26) — removed the "save fast / write to chat" temptation by making accuracy paramount over throughput.
- (b) **UWB-1: NEXT TOOL CALL** (28-Apr-26) — turns "I should save state" intent into immediate tool call, no delay.
- (c) **CONTEXT WINDOWS + SOP feedback memory** (mission critical) — explicit doctrine "never lose knowledge in session memory; default to durable COWORK files; save every ≤5min."
Together these three made it psychologically and procedurally "wrong" to leave state in conversation only.

**Why 5 — Why did those three changes finally stick when prior reminders hadn't?**
Because they're at HEADLINE level in CLAUDE.md (always loaded in context) AND they're framed as IDENTITY rather than RULES. Quality > Speed is "who Watson is", not "what Watson follows." UWB-1 is a Universal Winning Behaviour — one of FIVE non-negotiables. Context-windows-SOP is mission-critical memory. The combined gravity of these three placements made deviation feel like character violation, not rule violation. Identity-level discipline is durable; rule-level discipline drifts.

**Lesson (durable, universal):** **Externalise state to durable storage before you might need to recover it, not after you find you can't.** The cost of a save is small (1 file write); the cost of a lost session is enormous (re-derive everything from broken pointers). Save aggressively, save eagerly, save by default. The save threshold should be "any non-trivial state change" — not "when I think I might lose context."

**Corrective action / how to compound:**
1. Continue the practice on EVERY non-trivial work session, not just when Richard reminds.
2. The three structural pillars (Operating Values + UWB-1 + Context Windows SOP) work as a package. Don't soften any one of them; they reinforce each other.
3. Watch for the failure mode: micro-optimisation thinking ("I'll save when this batch is done"). The optimisation is false — saving is cheap. Save now.
4. When Richard runs an "anti-compaction protocol" check, the answer should always be "fully covered, here are the durable artefacts" — not "let me write things down now." If we ever have to write things down at the protocol-check moment, we've already failed.

---


### 1-May-26 — STAGE PROGRESSION SOP rolled out in TRIAL MODE — 8 open issues catalogued

**Context:** STAGE PROGRESSION SOP v1.0 + APM AJ SOP review authored 1-May-26 morning. Rolled out in TRIAL MODE through ~mid-May-26. 8 open issues catalogued at `memory/apm/open-issues-stage-progression.md` — each with a "lily pad" cross-ref in the role/file most likely to encounter it.

**Lesson — emergence-driven processing over pre-emptive build.** Richard's instruction: *"Make sure all this is saved into the relevant roles, the lessons, the ratings dashboard, so somehow when it emerges as an issue we can process it then."* The lesson is: when SOP changes are non-trivial, RESIST the temptation to pre-emptively action every downstream item. Instead, document the open issues + scatter lily pads + let real work surface them. This protects against (a) pre-mature optimisation in the abstract, (b) over-engineering before evidence, and (c) burning Richard's time on items that may resolve themselves through actual practice.

**Compound principle:** TRIAL MODE + LILY PAD pattern is reusable. For any new SOP rollout: trial first (set re-assessment date); document open issues with lily pads; iterate based on evidence, not anticipation.

---

### 1-May-26 — APM SKILL.md silently corrupted by linter modification mid-byte

**Incident:** Sometime during the morning's edits to APM SKILL.md, the file was silently truncated mid-UTF-8 byte (offset 135,135). Truncation was NOT discovered for several hours because Read tool returned partial content without erroring. Discovered when bash + python tried to read the file — UnicodeDecodeError surfaced. Both my pre-bcdef backup AND the AM-FULL-BACKUP-COMPLETE folder copy have the same corruption — meaning the truncation predates my edits today.

**Root cause (best inference):** Linter modification (system-reminder noted "modified by a linter") rewrote the file with content of identical byte length but ending mid-byte. The corruption was invisible to Read tool because it streams content and truncates at malformed UTF-8 silently.

**Recovery:** Restored from `memory/backups/2026-04-28/memory/skills/assistant-portfolio-manager/SKILL.md` (134,040 bytes, ends cleanly at "Ready for Richard review and enhancement.\n"). Re-applied the 1-May-26 STAGE PROGRESSION cross-ref I had added earlier. Lost any linter-introduced content from this morning (was likely formatting changes, not new substance — but unknown for certain).

**Lesson — daily backups saved us.** Without `memory/backups/2026-04-28/` we would have lost the APM SKILL substantively. Anti-compaction discipline working as designed at the daily layer.

**Lesson — file-integrity validation must be a pre-write check.** Read tool returned a partial-content silent truncation — a SILENT failure mode. The fix: when about to edit any file, first validate it's parseable end-to-end (e.g., `python3 -c "open(path).read()"`). If reads fail, repair from backup BEFORE edit. This pattern was used reactively today; should be proactive going forward.

**Lesson — preserve corrupted files for forensic review.** Defensive backup of `SKILL.md.CORRUPTED-bak-20260501-091500` taken before restore. The CORRUPTED file is 32 lines longer than the 28-Apr backup — meaning some content from this morning is preserved in it (just truncated mid-byte at the end). If those 32 lines turn out to matter, they can be salvaged from the .CORRUPTED-bak.

**Corrective actions:**
1. APM SKILL restored from 28-Apr daily backup (1-May-26 09:15 UK).
2. STAGE PROGRESSION cross-ref re-applied to restored file.
3. Defensive CORRUPTED-bak preserved for forensic review.
4. Pattern flagged: pre-write file integrity validation should be standard before any role-SKILL edit.

---


### 1-May-26 — Silent file truncation pattern: ten SOP additions to defend against it

**Incident:** Discovered today that 14 of 50 critical files (28% of SKILL.md, key context files, project doctrine files) on the COWORK filesystem mount were silently truncated mid-content. Files end with non-newline final byte; Read tool returns partial content without erroring; bash and Python error on read. Includes APM SKILL.md (corrupted twice), memo doctrine principles.md (mid-§IV.E), corrections.md, and several others. Same FUSE/virtiofs/linter pattern discovered yesterday for D-DMRL-14 (decisions.md truncated reproducibly to 6,289 bytes by Write tool) but at much wider scope.

**Root cause (5-whys; details in feedback_silent_file_truncation.md):** The Cowork environment runs a Linux container connected to the user's Windows host via a FUSE/virtiofs filesystem layer. Large writes that span buffer-flush points appear to report success at the application level while persisting only partial content to disk. Both the Write tool (Linux-side) and the linter (Windows-side, judging from "modified by a linter" system-reminder messages) trigger this failure mode. Filesystem reports the truncated size as the file's actual size, so reads do not surface the corruption.

**Ten SOP additions filed today** to defend against this going forward:
1. Read-side integrity validation before relying on any SKILL/SOP file (last byte must be `0a`)
2. Write-side default to bash heredoc for files >5KB
3. Defensive `.CORRUPTED-bak-{ts}` preservation when corruption found
4. Treat every "modified by a linter" system-reminder as a re-validation cue
5. Pre-write backup before any non-trivial mutation, taken via bash `cp` (SA-specific)
6. Multi-source redundancy for critical doctrine (doctrine file + SKILL mirror + code implementation)
7. Daily backup as recovery contract (memory/backups/{date}/, preserved 30+ days)
8. Daily integrity check as morning-routine task (COS-specific)
9. State.md write protocol — append-only, ≤4KB chunks, byte-verify after each (SA-specific)
10. Cross-project paranoia (D-DMRL-13 generalised to all SA projects)

**Filed across:** CLAUDE.md (rules 1, 2, 3, 4, 7), COS SKILL Daily Cadence (rule 8), SA SKILL (rules 5, 6, 9, 10), corrections.md (rule 3 standing reference), feedback_silent_file_truncation.md (5-whys + this lesson summary mirrored to auto-memory).

**Compound principle:** This is an infrastructure-level issue Watson cannot fix at root. The realistic mitigations are layered: detect on read; minimise via bash heredoc on write; recover from daily backup; preserve evidence when corruption found. Together these make the failure recoverable but not preventable.

---

