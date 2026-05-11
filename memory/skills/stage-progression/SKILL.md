# STAGE PROGRESSION SOP — Cross-Role Skill

**Status:** MISSION CRITICAL — governs how Richard, APM, COS, and RES coordinate to move investment ideas through the 6-stage research process (IG → Triaging → ESA → DD → Capital).
**Created:** 1-May-26 | **Owner:** Cross-role (skills layer)
**Locked by:** Richard, 1-May-26 morning

> ## ★ TRIAL MODE (1-May-26 → ~mid-May-26) ★
>
> **Status:** TRIAL. Use this SOP as-written for the next 2-3 weekly review meetings (i.e. ~3 cycles). DO NOT rewrite the AJ SOP to v2.2 yet — wait for trial outcomes. Capture friction in `memory/apm/open-issues-stage-progression.md` as it surfaces. Iterate based on real evidence, not anticipation.
>
> **Trial success criteria (informal):**
> - Step 4 weekly review meetings happen on cadence (Friday PM UK)
> - Decisions get made and filed (no open loops)
> - GNG CHECKS prove useful as agenda driver
> - APM-Richard alignment improves (fewer surprise disagreements)
> - COS scribe + APM proposal pattern works
>
> **Re-assessment:** ~mid-May-26 (3rd weekly meeting). Decide whether to (a) lock as v1.1 with friction-driven refinements, (b) v2.2 rewrite of AJ SOP using trial evidence, (c) revise scope.

<!-- SOP CITATION REQUIRED — per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

---

## Higher intent

Richard's higher intent (verbatim, 1-May-26 morning):

> *"For me to skim your judgement, analysis, and information clearly (in that order), and decide where I disagree (hopefully rarely), enabling us to drive rapid/huge movement of investment ideas through our RESEARCH PROCESS (from IG to TRIAGING to ESA to DD to CAPITAL)."*
>
> *"Just like I do with human colleagues."*

The system this SOP describes is the **operational discipline that makes that higher intent achievable.** Without it: APM produces memos in isolation, Richard reads them ad-hoc, decisions drift, ideas pile up unparked. With it: every stock has a clear path from one stage to the next, governed by a brief → analysis → review → decision rhythm.

---

## What this SOP governs

This SOP governs the **stage transitions** within the 6-stage research process:

```
IG → Triaging → ESA → DD → Capital → (Live monitoring → Exit)
```

A stage transition is not a passive event. It requires:
1. A clear brief (Step 1)
2. APM A&J work (Step 2)
3. Richard's review (Step 3)
4. A weekly review meeting (Step 4)

The transition decision (progress / park / kill) is made at Step 4, NEVER at Step 2 unilaterally.

---

## Scope by stage

| Stage transition | Heavyweight | Memo authored | Weekly review meeting |
|---|---|---|---|
| **IG → Triaging** | **EXEMPT** (light pipeline only) | Triaging memo (light) | Optional — quick chat, not formal meeting |
| **Triaging → ESA** | **Full heavyweight** | **ESA memo (deep)** | **Required — formal weekly review meeting** |
| **ESA → DD** | **Full heavyweight** | **DD memo (deepest)** | **Required — formal weekly review meeting** |
| **DD → Capital** | **Maximal** | DD memo final + position sizing | **Required — formal weekly review meeting + entry sizing decision** |
| Live → Exit | Conditional | Exit proposal memo | Required if exit triggered |

The heavyweight 4-step pipeline (Brief → APM A&J → Richard review → Review meeting) applies in full from **Triaging→ESA onward**. IG→Triaging is **EXEMPT** from the heavyweight version (per Richard, 1-May-26). 

### Light pipeline for IG→Triaging (NEW 1-May-26)

For the IG→Triaging transition only:
- RESEARCHER does most of the work (IG-stage queries: Business Description + Change Forces dual-source, scanner triage, etc.)
- APM produces a 2-line judgement (NOT a full memo; NO GNG CHECKS; NO formal review meeting)
- Decision (progress to Triaging / park) made by APM with light Richard sign-off (chat-only, ad-hoc OK)
- Pipeline.md updated; no Step 4 weekly meeting required for IG→Triaging
- Rationale: heavyweight at this stage would burn time on stocks that obviously fail the first screen; light triage is the right tool

The heavyweight pipeline kicks in from Triaging→ESA onward — that is when APM authors a full memo, produces GNG CHECKS, Richard reviews, and the weekly meeting decides progression.

---

## The 4 Steps

### Step 1 — Brief

**Owner:** Richard (originator) → APM (recipient).
**Mediator (optional):** COS, when Richard delegates briefing or batches multiple briefs.

**What happens:**
- Richard briefs APM (or COS briefs APM on Richard's behalf, if pre-agreed) on the stock at the stage.
- APM back-briefs via **Mission Command parse** (Context / Objective / Higher Intent / Specific Requests / Constraints) + **Three Gaps diagnostic** (Understanding / Alignment / How-to). See `CLAUDE.md` Operating Method.
- APM surfaces clarifying questions BEFORE starting analytical work. Empty back-brief diagnostic = suspicious.
- Alignment locked when Richard confirms the back-brief.

**Output:** Brief acknowledged + understood, gaps surfaced, alignment locked. Stored as a 3-line summary at the top of the stock's APM working file (`memory/staging/apm-active/{TICKER}-{stage}.md` — append-only working log).

**Quality gate:** APM must have an explicit back-brief artefact (not just a chat acknowledgement) BEFORE starting Step 2.

**Cross-ref:** `CLAUDE.md` Operating Method (Mission Command + Three Gaps + Back-brief).

---

### Step 2 — APM A&J

**Owner:** APM role.

**What happens:**
- APM executes the **APM A&J SOP** (`memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md`) at the relevant stage (Triaging / ESA / DD).
- Produces memo per V20 template (memo doctrine v3.8 + SKILL v2.8) with all weight tiers, signposting, summary blocks, content scaffolds.
- Produces **GNG CHECKS** artefact (formerly called "GO/NO GO ACTION QUESTIONS"; renamed 1-May-26) — 6-10 questions, stack-ranked, varied form, direct/challenging tone — separate Notion page, linkable from Ratings Dashboard RESEARCH STAGES tab.
- Logs uncertainty per the **judgement-importance-weighted escalation** rule (more important judgement = more checking with Richard; case-level NEVER finalised unilaterally).

**Output:**
- Memo posted to Notion Stock Notes DB + baked into Ratings Dashboard
- GNG CHECKS posted to Notion (separate page, linkable)
- 3-line handoff written to `memory/staging/apm-output-queue.md` so COS knows there's review-pending work
- Pipeline.md updated: stock state = "Stage X memo shipped, awaiting Richard review"

**Quality gate:** APM cannot ship without 12 quality gates passing per AJ SOP §Quality Gates + new G13 (GNG CHECKS posted, 6-10 questions).

**Cross-ref:** `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` (governs the analytical work) + `databases/memo-view-formatting-principles.md` v3.8 (governs memo output spec).

---

### Step 3 — Richard's review

**Owner:** Richard (reviewer).
**Chase / accountability:** COS role.

**What happens:**
- Richard skims memo: judgement → analysis → information ordering. If he agrees with the judgement layer, he's done — no need to drop deeper.
- Richard reviews the GNG CHECKS to surface his disagreements / additions / probes BEFORE the weekly meeting.
- COS chases Richard via the morning routine to ensure review happens within 24-48 hours of APM ship (avoid memo backlog).

**COS responsibilities (from `chief-of-staff/SKILL.md` Daily Cadence):**
- Morning routine surfaces "APM memos pending Richard review" queue from `memory/staging/apm-output-queue.md`
- If a memo has been pending review for >48 hours: COS escalates ("APM shipped HTRO ESA memo on 1-May-26, still pending your review — aiming for review meeting Friday")
- COS is NOT a passive reminder system. Richard expects to be chased.

**Output:** Richard's review notes — captured either as inline annotations in the GO/NO GO ACTION QUESTIONS Notion page, or in chat with APM. Stored at `memory/apm/richard-review-notes/{TICKER}-{stage}-{date}.md` if formalised.

**Quality gate:** Richard review COMPLETE before weekly review meeting (not concurrent — separation matters so meeting is for debate, not for first-read).

**Cross-ref:** `memory/skills/chief-of-staff/SKILL.md` §Daily Cadence + COS→APM handoff triggers + `memory/skills/morning-routine/SKILL.md`.

---

### Step 4 — Weekly review meeting

**Owner:** Richard (chair) + APM (defendant/adapter).
**Optional attendees:** COS (scribe — verifies + files decisions), RES (contextualises information layer if disputed).

**Cadence:** **Weekly batch** (multiple stocks per meeting). Establishes regular weekly rhythm. Default day: Friday afternoon UK (after EOD routine, before WFP meeting). If multiple stocks awaiting review, prioritise by: (a) Triaging→ESA decisions due, (b) DD→Capital decisions due (highest stakes), (c) ESA→DD decisions due.

**No upper-bound on batch size (NEW 1-May-26):** Weekly batch is OPEN-ENDED — no cap on number of stocks per meeting. Meeting closes when each stock has a decision. If a meeting runs unusually long, that is a SIGNAL TO APM to brief better in future cycles (reduce open questions per stock; surface uncertainty earlier in GNG CHECKS) — NOT a signal to cap stocks. Capping would create open loops; the higher intent (rapid/huge movement of ideas through research process) requires every stock to exit with a decision.

**Format:** **Chat-async first, voice escalation optional.**
- Default mode: Richard + APM debate in chat (e.g., Cowork session, or Slack-equivalent). APM is in APM mode (Opus model required).
- Open-ended duration — meeting closes when each stock has a decision.
- Voice escalation if a single stock's debate is too dense for chat (rare).

**Meeting agenda (default — driven by GNG CHECKS):**
- Per stock, walk through the 6-10 GNG CHECKS in stack-ranked order.
- For each question, Richard responds; APM defends or adapts.
- After all questions resolved, Richard makes the case-level decision: **progress to next stage / park / kill**.
- COS captures the decision; APM logs any rating revisions to calibration log (`memory/apm/calibration-log.md`).

**Decision logic at meeting:**

| Decision | Trigger | Downstream action |
|---|---|---|
| **Progress to next stage** | Case-level judgement = A or B; majority of GO/NO GO ACTION QUESTIONS resolved positively; no live invalidation ACH triggered | APM produces case components (Phase 5 of AJ SOP) for the stock; RESEARCHER briefed on next-stage research queue; pipeline.md updated to next stage |
| **Park** | Case-level judgement = C or borderline; key questions unresolved; awaiting external trigger (earnings, catalyst) | Pipeline.md updated to "parked at Stage X with re-activation trigger Y"; COS adds re-check date to monitoring |
| **Kill** | Case-level judgement = D or F; thesis broken; multiple invalidation ACHs triggered | Pipeline.md removes; APM logs final lesson to `memory/coaching/lessons-and-mistakes.md`; track-record updated |

**Output capture mechanism:**
- **APM proposes capture** — at meeting close, APM writes a 5-line summary per stock to a draft `memory/apm/stage-decisions-log.md` entry.
- **COS verifies + files** — COS reviews the draft within 4 hours, confirms accuracy with Richard if any ambiguity, then commits to the canonical log + propagates updates to pipeline.md, monitoring-plan.json, and (if progress decision) RESEARCHER queue.
- **Calibration log** — APM separately logs any rating revisions Richard made to `memory/apm/calibration-log.md` per AJ SOP v2.2 §Calibration log.

**Quality gate:** Every stock that enters a weekly review meeting EXITS with a decision. No "we'll revisit next week" allowed unless explicitly parked.

**Cross-ref:** `memory/apm/stage-decisions-log.md` (NEW — to be created) + `memory/apm/calibration-log.md` (NEW — to be created) + `memory/skills/chief-of-staff/SKILL.md` §Weekly Cadence.

---

## Per-step ownership matrix

| Step | Richard | APM | COS | RES |
|---|---|---|---|---|
| 1. Brief | **Originator** | Recipient + back-briefer | Mediator (optional) | — |
| 2. APM A&J | — | **Owner — produces memo + questions** | — | Provides info layer (briefed by APM if gaps) |
| 3. Richard's review | **Reviewer** | — | **Chaser — enforces 24-48h SLA** | — |
| 4. Review meeting | **Chair + decision-maker** | **Defendant + adapter + capture-proposer** | **Scribe — verifies + files** | Optional — contextualises disputes |
| 5. Post-meeting (if progress) | — | **Owner — produces case components** | Updates pipeline + monitoring | Briefed for next-stage research |

---

## Per-step quality gates summary

1. **Step 1:** Back-brief artefact exists (not just chat acknowledgement). Mission Command parse + Three Gaps diagnostic complete.
2. **Step 2:** All 13 quality gates pass (12 from AJ SOP v2.1 + new G13 GO/NO GO ACTION QUESTIONS posted).
3. **Step 3:** Richard review complete BEFORE meeting (not concurrent). COS chases enforced 24-48h SLA.
4. **Step 4:** Every stock exits meeting with a decision. APM proposes capture; COS verifies + files within 4h.
5. **Post-meeting (if progress):** Case components artefact produced by APM. Pipeline + monitoring updated.

---

## Anti-patterns (what we are NOT doing)

1. **Slide-it-under-the-door publishing.** APM does NOT ship memo + walk away. Memo + GNG CHECKS form a unit. The questions are the bridge to the meeting.
2. **APM unilateral case-level decision.** Even if APM rates a stock A or F, the case-level decision (progress / park / kill) is Richard's at the weekly meeting. APM RECOMMENDS, never decides.
3. **Ad-hoc reviews.** No "let's do this stock now" mid-week reviews unless Richard explicitly requests. Weekly batch maintains rhythm + protects Richard's deep-work time.
4. **Open loops.** Every stock entering a meeting MUST exit with a decision. No "park for further thought" without an explicit re-activation trigger and a re-check date.
5. **Capture by Richard.** Richard chairs; he does NOT scribe. APM proposes capture; COS verifies + files. If COS is absent, APM files solo and flags for COS verification.
6. **Skipping the back-brief.** Step 1 is non-negotiable even on "obvious" briefs. The schema-driven parse is what catches misalignment before 30 min of memo work goes wrong.

---

## Cross-references

- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` — Step 2 SOP (governing APM A&J work)
- `memory/skills/assistant-portfolio-manager/SKILL.md` — APM role definition + Six Pillars framework
- `memory/skills/chief-of-staff/SKILL.md` — Step 3 chase + Step 4 scribe responsibilities
- `memory/skills/researcher/SKILL-V2.md` — RES role; Step 1 (briefed by APM if Step 2 needs more info) + Step 4 (optional attendance)
- `memory/skills/morning-routine/SKILL.md` — COS surfaces APM memos pending review
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 — memo template (output spec for Step 2)
- `databases/memo-view-formatting-principles.md` v3.8 — memo doctrine SSoT (weight tiers, signposting, summary blocks)
- `memory/skills/communication-principles/SKILL.md` — cross-role communication doctrine (4 principles)
- `memory/context/investment-process.md` — 6-stage research process (this SOP governs the GATE TRANSITIONS within that process)
- `memory/context/investment-strategy.md` — 4-pillar framework (case-level decision criteria)
- `memory/projects/ratings-dashboard/v11-v20-summary.md` — V20 memo template informs Step 2 output spec
- `wisdom-library/general/decision-making/judgement-analysis-information-ordering.md` — Gold tier model (J→A→I)
- `wisdom-library/general/decision-making/mission-command.md` — Step 1 back-brief discipline
- `wisdom-library/general/decision-making/three-gaps-art-of-action.md` — Step 1 diagnostic

---

## Files this SOP creates / requires (NEW today)

| File | Owner | Purpose | Status |
|---|---|---|---|
| `memory/staging/apm-active/{TICKER}-{stage}.md` | APM | Step 1 back-brief artefact + Step 2 working log | Per-stock as needed |
| `memory/staging/apm-output-queue.md` | APM writes; COS reads | Step 2→3 handoff queue | NEW — to be created on first APM ship under v2.2 |
| `memory/apm/richard-review-notes/{TICKER}-{stage}-{date}.md` | Richard or APM | Step 3 review notes (formalised) | Per-stock as needed |
| `memory/apm/stage-decisions-log.md` | APM proposes; COS verifies + files | Step 4 meeting decisions canonical log | NEW — to be created at first weekly review meeting |
| `memory/apm/calibration-log.md` | APM | APM rating vs Richard revision tracking | NEW — to be created at first weekly review meeting where any rating revision happens |

---

## Versioning

- **v1.0 (1-May-26)** — Initial creation. 4-step pipeline locked. Cross-refs to AJ SOP v2.1 (pre-v2.2 rewrite), memo doctrine v3.8, COS SKILL.

---

*[W] Created 1-May-26 ~07:35 UK by SA role at Richard's instruction. Step 4 weekly review meeting cadence + chat-async format + open-ended duration confirmed by Richard. Heavyweight scope from Triaging→ESA onward confirmed by Richard.*
