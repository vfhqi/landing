# APM A&J SOP Review — 1-May-26

> ## ⚠️ STATUS: TRIAL MODE DISCONTINUED 03-May-26 ⚠️
>
> **All 6 amendments proposed in this review have been integrated into AJ SOP v2.2 on 03-May-26**, alongside 7 additional amendments from the 03-May-26 hot wash on the EKTA/HTRO/PRY/COTN-CH production run.
>
> Per Richard's instruction (03-May-26): *"All of these are fine to be integrated into the SOP now, rather than held off."* The TRIAL MODE block below was overridden — no 3-cycle wait, no held-off rewrite. Full integration is live.
>
> **See:**
> - `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.2 (live SOP)
> - `databases/scripts/validate-memo.py` v2.2 (lock-step validator)
> - `feedback_apm_aj_sop_v22_integration.md` (auto-memory entry — full integration record + 13 amendments table + regression test results)
>
> **This document is retained as historical context only.** Its TRIAL MODE block (immediately below) is STALE — do not follow it. The 6 proposed v2.2 amendments listed in §Section 2 are now integrated; their `analysis-judgement-SOP.md` v2.2 implementation is the live source-of-truth.

<!-- [W] Created 1-May-26. Author: SA role. Format: AJA (Analysis → Judgement → Actions). Reviews v2.1 of analysis-judgement-SOP.md against the V20 memo template (memo doctrine v3.8) + Richard's reframed higher intent (1-May-26 morning briefing). DISCONTINUATION NOTE added 03-May-26 above. -->

> ## ★ TRIAL MODE (1-May-26 → ~mid-May-26) — STALE; DISCONTINUED 03-May-26 (see banner above) ★
>
> **Status:** AJA review only. NO v2.2 rewrite of AJ SOP yet. Trial the existing v2.1 + STAGE PROGRESSION SOP for ~3 weekly review cycles, capture friction, then decide whether v2.2 rewrite is needed (and what shape it takes based on real evidence, not anticipation).

## Higher intent (the WHY)

Richard's higher intent (verbatim, 1-May-26 morning):

> *"For me to skim your judgement, analysis, and information clearly (in that order), and decide where I disagree (hopefully rarely), enabling us to drive rapid/huge movement of investment ideas through our RESEARCH PROCESS (from IG to TRIAGING to ESA to DD to CAPITAL)."*

Plus the reframe added later:

> *"It is important we must make a mechanism in therefore to proactively probe for and push for disagreement and the outcome is there is little. E.g. you asking challenging question to me 'What are your thoughts on X judgement', etc. Basically, we need the APM A&J SOP to write the analysis. Then as part of our working action list to complete work on a STAGE of the RESEARCH PROCESS, I must hold a meeting with the APM to review/debate the APM A&J. Just like I do with human colleagues."*

**Distilled higher intent:** The APM A&J SOP is **Step 2 of a 4-step Stage Progression SOP**. It does not stand alone. Its job is to produce a memo Richard can skim (judgement → analysis → information), AND to surface the questions that make the subsequent debate productive. Surface disagreement-probing must be HIGH; surface disagreement OUTCOME should be LOW (because the probing has already surfaced and resolved the substance).

---

## Section 1 — What's good (preserve at all costs)

The current AJ SOP v2.1 (last updated 28-Apr-26) is structurally **strong**. The following load-bearing elements should be preserved verbatim or with minimal change:

| # | Element | Where | Why preserve |
|---|---|---|---|
| 1 | **J→A→I work order vs communication order distinction** | §"Work order vs Communication order" lines 86-114 | This is the universal communication principle (now a Wisdom Library Gold model). The SOP correctly distinguishes how Watson THINKS (info → analysis → judgement) from how the memo READS (judgement → analysis → info). |
| 2 | **70/30 P3+P4 time allocation** | §Phase 2 | Matches Richard's priority order (P3 what's changing > P4 how bankable > P1 technical > P2 paradigm fit). Memo doctrine v3.8 §IV.H reinforces this via weight overrides. |
| 3 | **Mandatory content scaffolds for flat pillars (C.II.1/3/4/5)** | §Phase 2 lower section | Prevents thin output. 5-6 named components per pillar; missing component = section incomplete regardless of word count. |
| 4 | **Bullet architecture (parent=verdict ≤30w, sub=evidence)** | §Phase 2 line 149-156 | Two-layer Miller 7±2; supports skim-first reading. |
| 5 | **R18 5-grade rule (A/B/C/D/F, no modifiers)** | §Quality gates 10 | Forces commitment to a discrete judgement. No hiding behind "B+/A-". |
| 6 | **Signposting doctrine (CQ/RA/TC at parent bullet, two-layer architecture)** | §Phase 2 + APM SKILL §Signposting Doctrine | Every analytical statement instantly traceable to the question it answers. |
| 7 | **Communication Principles cross-role** | APM SKILL §Communication Principles | Peer/base-rate, A-F bell curve, ❌ invert + call out D/F, 🚩 RARE outlier flagging. |
| 8 | **Wisdom Library consult + track-record check NON-NEGOTIABLE** | §Phase 1 + APM SKILL §3.7 / §NON-NEGOTIABLE | Pattern memory + lesson memory before judgement. |
| 9 | **Notion lookup for Richard's own notes (Case files, RNTS, journal)** | §Phase 1 input #3 | Highest-signal calibration input. APM working blind without it. |
| 10 | **Opus model mandate** | §★ Model requirement | Highest-stakes work; Sonnet/Haiku insufficient. |
| 11 | **Quality gates 1-12** | §Quality gates | Pre-ship enforcement. |
| 12 | **Authoring order C.II → A → D → C.I → B → E → F** | §Authoring order | Work order ≠ communication order; B (BLUF) written LAST so it actually summarises completed work. |
| 13 | **Proactive RESEARCHER briefing right** | §☆ Proactive RESEARCHER briefing ☆ | APM directs RESEARCHER for missing inputs; not a passive consumer. |

**Verdict on preserved elements: A.** The SOP's analytical content is closer to what Richard would do than most of what's been built this year. Don't break it.

---

## Section 2 — Six gaps with proposed fixes

### Gap 1 — Doctrine misalignment at the WEIGHTS layer (memo doctrine v3.8 vs APM SOP)

**Analysis.** The V20 memo template (and underlying doctrine v3.8) assigns each element/RA a **weight tier**: half (0.5×) / normal (1.0×) / double (2.0×) / quadruple (4.0×). The weight scales (a) bullet count target and (b) implicit analytical depth — a quadruple-weighted RA at ESA stage targets 36-60 bullets per CQ vs 9-15 for a normal-weighted RA. Currently TWO RAs are quadruple (Q1 Sector strength, Q2 General ACHs); 11 RAs/elements/groups are double; 1 RA is defensively normal (Conservative IR); the rest default normal.

The APM AJ SOP currently (v2.1) has NO weight-driven effort allocation guidance. It has the 70/30 P3+P4 rule (good, but coarser than weight-tier). APM is left to infer "spend 4× the time on Sector strength than on a normal RA" from the memo's bullet target — but the SOP doesn't say it explicitly. **Result: APM may produce uniform-depth analysis across RAs, missing the doctrine signal that some RAs are 2× or 4× more important than others.**

**Judgement.** Add a §Weight-driven effort allocation that ties APM's analytical effort allocation 1:1 to the weight tier in memo doctrine v3.8 §IV.H. The weight is the SSoT for "how hard is this RA load-bearing?" — APM effort must mirror.

**Proposed fix.** Add to v2.2 Phase 2 (NEW sub-section after 70/30 rule):

> ### ★ Weight-driven effort allocation (NEW v2.2) ★
>
> Memo doctrine v3.8 §IV.H assigns each element/RA a weight tier (half / normal / double / quadruple). The weight governs both (a) bullet count target per CQ and (b) APM's analytical effort allocation. APM time per RA scales with weight:
>
> | Weight | Bullets per CQ (ESA) | APM effort (relative) | Examples (current v3.8 doctrine) |
> |---|---|---|---|
> | half (0.5×) | 5-8 | 0.5× | (None designated; reserved) |
> | normal (1.0×) | 9-15 | 1× | Default for unmarked RAs |
> | double (2.0×) | 18-30 | 2× | Required input forces, Required financial outputs, Business quality (entire group), Required simplicity guardrails, Paradigm fit (Pillar 2 G1), Lessons check, Negative earnings momentum, Crash through stops, Plain sight risks |
> | quadruple (4.0×) | 36-60 | 4× | **Sector strength** (Q1 — peer-quality canary), **General ACHs** (Q2 — invalidation screening cohort) |
>
> Authorial principle: 70% of analytical depth should sit on the double + quadruple-weighted RAs. The 70/30 P3+P4 rule remains true; the weight system makes it operational at the RA level.

### Gap 2 — No judgement-importance-weighted escalation rule

**Analysis.** Currently the SOP treats every rating (CQ, RA, element, group, pillar, investment case) equally — APM commits A-F at every level and ships. But Richard's higher intent is *"the more important the judgement, the more you check with me."* A pillar-level rating of B vs C is enormously consequential (it gates whether a stock progresses from ESA→DD or DD→Capital); a single CQ rating is not. Currently APM unilaterally finalises everything.

**Judgement.** Add a 6-tier escalation table tied to the memo's analytical hierarchy. The rule: as judgements move UP the taxonomy (CQ → RA → element → group → pillar → case), the APM's autonomy DECREASES and the requirement to surface to Richard INCREASES.

**Proposed fix.** Add to v2.2 Phase 3 (NEW sub-section):

> ### ★ Judgement-importance-weighted escalation (NEW v2.2) ★
>
> One-line rule: **The more important the judgement, the more you check with Richard.**
>
> | Tier | Count per memo | APM autonomy | Mechanism |
> |---|---|---|---|
> | **CQ rating** | ~175 | Commit unilaterally | Inline in C.II bullets. Don't escalate per-CQ. |
> | **RA rating** | ~63 | Commit; flag uncertainty inline if conflicted | Inline in C.II RA-summary block. Italic "low conviction" tag if borderline (e.g., B/C borderline). |
> | **Element rating** | ~19 | Commit; flag uncertainty inline; raise in handoff if material | Inline in C.II element-summary block. Material uncertainty → COS handoff for next morning routine. |
> | **Group rating** | ~5 | Commit; surface explicitly in handoff with confidence tag | Group-summary block + handoff line: "G3 Business quality rated B with medium confidence — see GO/NO GO ACTION QUESTION #3". |
> | **Pillar rating** | 6 | Commit BUT flag as "draft for Richard's review" | C.I.1 ratings table. Every pillar rating carries `(draft)` annotation until weekly review meeting confirms or revises. |
> | **Investment case rating** (Pillar III + IV synthesis → progress/park/kill) | 1 | **NEVER finalise unilaterally** | E.I summary judgement = APM's recommendation only. Decision belongs to Richard at the weekly review meeting (Stage Progression SOP Step 4). |
>
> The APM's job is to PRODUCE the case-level judgement and surface it for debate, NOT to finalise it. The case-level judgement IS the gate that determines whether a stock progresses through the research process — get it wrong (under-rate an A as a C) and an investable case dies; over-rate (call a C an A) and Richard wastes time on a non-investable case. **This is the highest-stakes single judgement in the entire APM workflow.**

### Gap 3 — No proactive disagreement-probing mechanism (GNG CHECKS)

**Analysis.** Currently the SOP ends at Phase 4 → ship to Notion + dashboard. There's no mechanism for APM to actively probe Richard for disagreement before/during the weekly review meeting. Without proactive probing, Richard reads the memo cold, decides where he disagrees in his own head, and then the meeting is a series of corrections — slow, low-bandwidth.

**Judgement.** Mandate a **GNG CHECKS** artefact (formerly "GO/NO GO ACTION QUESTIONS"; renamed 1-May-26 PM) per stock per stage as a separate deliverable from the memo. This artefact:
- Lives as its own Notion page (NOT inline in the memo — keeps the memo clean as APM output spec)
- Is linkable from the RESEARCH STAGES tab of the Ratings Dashboard
- Forms the default agenda for the weekly review meeting
- Is the proactive probing layer

**Proposed fix.** Add to v2.2 Phase 4 (NEW sub-section after Notion + dashboard ship):

> ### ★ GNG CHECKS — proactive disagreement probing (NEW v2.2) ★
>
> After the memo is shipped, APM produces a separate **GO/NO GO ACTION QUESTIONS** artefact for the stock at this stage. This artefact is the proactive probing mechanism — its purpose is to surface where APM most wants Richard's calibration on the case-level judgement.
>
> **Format:**
> - Notion page in Stock Notes DB
> - Title: `[W] {TICKER} ({Company}) — {Stage} — GNG CHECKS [W] @ {DD-MMM-YY}`
> - Properties: Stock(s) relation, Stage, Source [W], Date, Case component = "GNG CHECKS"
> - Linkable from Ratings Dashboard RESEARCH STAGES tab (one link per (ticker × stage) cell)
>
> **Content — 6 to 10 questions, stack-ranked by impact on case-level judgement:**
> - The questions should probe the highest-stakes judgements in the memo (typically pillar-level or case-level).
> - Vary the form deliberately: some closed (yes/no), some open, some aggressive ("Why shouldn't this be a D?"), some comparing to other ideas ("How does this compare to CARLB?"), some this-idea-centric ("What's missing from my read of the operator?").
> - Tone: direct, challenging, neutral-positive. NOT deferential ("does this make sense?"). NOT defensive.
> - Stack rank: question #1 = most important to resolve (the one most likely to change the case-level decision); question #N = least.
> - Each question must reference the specific RA / element / group / pillar it probes (signposting required).
>
> **Example format (illustrative, not template):**
>
> ```
> [W] HTRO (Hexatronic) — ESA — GNG CHECKS [W] @ 01-May-26
>
> 1. (Element-level, P3) The "Required input forces?" element rated B. The Russian gas / EU REPowerEU tailwind is real, but is the magnitude HIGH ENOUGH to drive top-quartile EPS upgrades? — i.e., is this an A or a B?
> 2. (Pillar-level, P4) Sector strength rated D (peer technical deterioration). Should this kill the case at ESA, or is HTRO's idiosyncratic story strong enough to override sector weakness? — i.e., do we proceed despite sector D?
> 3. (Comparative) How does this case compare to CARLB at the same stage (ESA, end-Apr-26)? CARLB had stronger BB#5 (financial outputs) but weaker IC#1 (operator quality). Net which is the better R/R?
> 4. (Aggressive) Why shouldn't the entire BQ group be rated C, given operator dependence on a single founder and unproven international scaling?
> 5. (Open) What concerns of yours about the case have I missed in the memo?
> 6. (Closed) Is the 4-5% cable-volume tailwind the fulcrum driver, or is it the operator quality?
> 7. (Comparative, peer-base-rate) Sector median EBIT margin is 8.5%; HTRO at 12% (top decile). Sustainable, or peak-cycle?
> 8. (Aggressive) If we're wrong on this, what's the failure mode — operator stumble, demand collapse, or competitive capture?
> ```
>
> **Quality gate (NEW G13):** APM cannot ship without 6-10 GNG CHECKS posted to Notion + linked from Ratings Dashboard.

### Gap 4 — No calibration-over-time mechanism

**Analysis.** When Richard overrules an APM rating (in a weekly review meeting, or via an inline note), there's currently no formal capture loop. APM cannot learn from past corrections without a structured log.

**Judgement.** Add a calibration log at `memory/apm/calibration-log.md`. After every weekly review meeting (or any explicit Richard override), APM writes an entry: stock, stage, what APM rated, what Richard revised to, Richard's reason. Over time, surface patterns where APM systematically over/under-rates a domain.

**Proposed fix.** Add to v2.2 Phase 4 (NEW sub-section, paired with GO/NO GO ACTION QUESTIONS):

> ### ★ Calibration log (NEW v2.2) ★
>
> When Richard overrules an APM rating (during a weekly review meeting, or via an inline note in chat / Notion), APM logs the revision to `memory/apm/calibration-log.md`. Append-only.
>
> **Format per entry:**
> ```
> ### {DD-MMM-YY} — {TICKER} {Stage} — {Pillar/Element/RA name}
> - APM rating: {A/B/C/D/F} ({1-line rationale})
> - Richard revision: {A/B/C/D/F} ({Richard's reason})
> - Domain pattern: {if recurring — e.g., "APM consistently over-rates UK retail operators"}
> - Calibration action: {what APM should do differently next time — e.g., "load richard-investing-approach.md §Operator Quality Three Dimensions before rating retail operators"}
> ```
>
> **Review cadence — three-role co-review (NEW 1-May-26):**
> - **APM owns the log** (writes entries; primary monthly review)
> - **HPC reviews monthly** for performance patterns (where is APM systematically over- or under-rating? Is there a coaching pattern — e.g., APM pessimistic on operator quality, optimistic on technical setups?). HPC integrates findings into HPC SKILL coaching observations + brings to weekly review meetings if material.
> - **COS reviews monthly** for process/cadence patterns (are calibrations resolving in the next cycle? Are domain patterns being acted on in subsequent SOP updates?). COS integrates findings into COS SKILL delivery scorecard.
> - **Joint review:** APM + HPC + COS at the last Friday of month WFP meeting. Surface 1-2 calibration patterns to act on for the coming month.
> - APM still owns the SOP-update proposals; HPC and COS co-validate the diagnoses.
>
> Cross-ref Wisdom Library: `peer-and-base-rate-anchoring`, `top-decile-top-quartile-grading`, `outlier-flagging-rare-data` — calibration patterns may surface gaps in these models too.

### Gap 5 — No coupling to Stage Progression SOP

**Analysis.** Currently the AJ SOP says "Phase 4 → ship via Notion + dashboard" as if shipping IS completion. Under Richard's reframe, shipping is Step 2 of 4; the SOP must point downstream to Step 3 (Richard reads, COS chases) and Step 4 (weekly review meeting).

**Judgement.** Add §Step 2 of Stage Progression SOP header at top + downstream-handoff guidance at end.

**Proposed fix.** Add to v2.2 (TWO insertions):

**At top, NEW header section:**

> ## Where this SOP sits in the Stage Progression SOP
>
> This SOP is **Step 2 of the 4-step STAGE PROGRESSION SOP** (`memory/skills/stage-progression/SKILL.md`). Steps:
> 1. **Brief** — Richard briefs APM on the stock at the stage (back-briefed via Mission Command + 3 Gaps per CLAUDE.md Operating Method).
> 2. **APM A&J** — THIS SOP. APM produces the memo + GO/NO GO ACTION QUESTIONS.
> 3. **Richard's review** — Richard reads the memo + GNG CHECKS; COS chases via morning routine.
> 4. **Review meeting (weekly batch, chat-async, open-ended)** — Richard + APM (+ COS + RES) debate; case-level decision = progress to next stage / park / kill.
>
> APM's deliverable to Step 3 is the memo (Notion + dashboard) AND the GNG CHECKS (Notion). APM's role in Step 4 is to defend/adapt the analysis, log calibration, and capture the meeting decision (with COS verifying + filing).

**At end of Phase 4, NEW handoff sub-section:**

> ### ★ Handoff to Step 3 (Richard's review) — NEW v2.2 ★
>
> When Phase 4 ships, APM does NOT close out. APM:
> 1. Writes a 3-line handoff to `memory/staging/apm-output-queue.md` so COS knows there's a memo + GNG CHECKS pending Richard's review.
> 2. Tags the stock in pipeline.md as "Stage X memo shipped, awaiting Richard review" (state field).
> 3. Surfaces the most-important uncertainty in the COS morning routine queue (so COS chases Richard within 24h).
>
> APM's analytical work is COMPLETE; the gate decision is open until Step 4 closes it.

### Gap 6 — Hook for case components (coming later today)

**Analysis.** The CASE COMPONENTS work coming later today (key drivers / invalidation thresholds / leading tracking indicators) is a major adjacent artefact — Richard's analogy: memo = "learning to fly", components = "in-flight checklist". Components are produced AFTER memo A&J, by APM, for stocks marked "progress to next stage" at the Step 4 review meeting.

**Judgement.** Add a forward-pointing hook in the AJ SOP for components. Don't author the components SOP itself yet (separate brief later today) — but anticipate the coupling.

**Proposed fix.** Add to v2.2 (NEW section after Phase 4):

> ## Phase 5 — Case Components prep (NEW v2.2; conditional)
>
> **Triggered when:** the Step 4 review meeting decides to progress the stock to the next stage of the research process (or to keep it live in the portfolio).
>
> **What APM does:** Produces the **CASE COMPONENTS** artefact for the stock — a distilled in-flight checklist derived from the memo's analysis + judgement. Components include:
> - **Key drivers** (the 1-2 fulcrum drivers + 4 key drivers — typically lifted from C.II.2 IC#3 setups + IC#1 outputs)
> - **Invalidation thresholds** (the 10 INVALIDATION ACHs from D.II.1, distilled to the 2-3 that bite first for THIS stock)
> - **Leading tracking indicators** (the 1-2 monitoring items per fulcrum driver — feeds the Monitoring Plan)
> - Other components (TBD as case components SOP is authored)
>
> Components are NOT part of the memo. They are a separate Notion artefact + linked from the Ratings Dashboard RESEARCH STAGES tab + integrated with the Monitoring Plan.
>
> **Cross-ref:** `memory/skills/case-components/SKILL.md` (TBD — to be authored after Richard's case components brief).

---

## Section 3 — Proposed v2.2 SOP rewrite

The above 6 fixes are additive — they extend v2.1 without breaking the core. Proposed v2.2 changes:

| Insertion | Location | Status |
|---|---|---|
| §Where this SOP sits in the Stage Progression SOP | NEW header | Required |
| §Weight-driven effort allocation | Phase 2, after 70/30 rule | Required |
| §Judgement-importance-weighted escalation | Phase 3, NEW sub-section | Required |
| §GNG CHECKS (renamed from GO/NO GO ACTION QUESTIONS) | Phase 4, NEW sub-section after Notion+dashboard ship | Required |
| §Calibration log | Phase 4, NEW sub-section paired with GO/NO GO ACTION QUESTIONS | Required |
| §Handoff to Step 3 | Phase 4, NEW final sub-section | Required |
| §Phase 5 — Case Components prep | NEW Phase 5 (conditional) | Required (forward hook only; components SOP authored later) |
| Quality gate G13 (GNG CHECKS posted) | Quality gates, NEW row | Required |
| Updated cross-references | bottom of file | Required |

**Recommended:** Watson authors v2.2 as a full re-authored doc (NOT a diff) at `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` — then the v2.1 file becomes the `.bak-pre-v22` file. This is the cleanest way given the cross-cutting changes.

**Owner of this rewrite:** APM role authors v2.2 once Richard sign-off received on this review doc. SA role does not edit APM SOPs unilaterally.

---

## Section 4 — Cross-references and downstream impacts

### Files this review touches (cross-refs added)

- `memory/skills/assistant-portfolio-manager/SKILL.md` — APM SKILL needs cross-ref to STAGE PROGRESSION SOP + GO/NO GO ACTION QUESTIONS + Calibration log
- `memory/skills/chief-of-staff/SKILL.md` — COS SKILL needs cross-ref to STAGE PROGRESSION SOP Step 3 (chase Richard) + Step 4 (verify + file meeting decisions)
- `memory/skills/researcher/SKILL-V2.md` — RES SKILL needs cross-ref to STAGE PROGRESSION SOP Step 1 (brief) + Step 4 (optional meeting attendance)
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 — already governs memo doctrine; no change needed but cross-ref from APM SOP added
- `memory/projects/ratings-dashboard/state.md` — SA project needs cross-ref noting that V20 informed APM SOP review (already done in v11-v20-summary.md)

### Downstream impacts

1. **Ratings Dashboard RESEARCH STAGES tab** needs to render the GO/NO GO ACTION QUESTIONS link per (ticker × stage) cell. SA workstream — to be picked up after components SOP is built.
2. **Notion Stock Notes DB** Case component field needs new value: "GO/NO GO ACTION QUESTIONS". Schema check + value addition needed before first APM authorship under v2.2.
3. **Monitoring Plan integration** — Case components feed monitoring plan; APM SKILL §3.5 already has the local-first lookup; needs minor extension once components SOP authored.
4. **Validator** — `validate-memo.py` should add R29 (GO/NO GO ACTION QUESTIONS posted, count 6-10). Out of scope for this review; flag for future.

---

## Section 5 — One-line judgement summary (BLUF)

> **APM A&J SOP v2.1 is structurally strong but missing 6 things that the V20 memo template + Richard's reframe (1-May-26) make load-bearing: (1) weight-driven effort allocation, (2) judgement-importance-weighted escalation, (3) proactive disagreement-probing via GNG CHECKS, (4) calibration-over-time log, (5) coupling to STAGE PROGRESSION SOP, (6) hook for case components. Recommend v2.2 rewrite incorporating all six AFTER trial period (1-May-26 → ~mid-May-26) yields friction evidence; STAGE PROGRESSION SOP is the parent.**

---

## Section 6 — Proposed actions (IAJA — the A)

| # | Action | Owner | When |
|---|---|---|---|
| 1 | Richard reviews this AJA review doc | Richard | Today (after morning's lessons + save are confirmed received) |
| 2 | Watson authors `memory/skills/stage-progression/SKILL.md` (NEW) | SA role (this session) | Today, after Richard sign-off on this review |
| 3 | Watson authors v2.2 of `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` incorporating 6 fixes | APM role (next APM-mode session — NOT this session) | Next APM session; today if Richard requests |
| 4 | Watson adds cross-refs from APM SKILL, COS SKILL, RES SKILL, ratings-dashboard project, memo-view-formatting SKILL | SA role (this session) | Today, after STAGE PROGRESSION SOP authored |
| 5 | Watson adds Notion Stock Notes Case component value "GNG CHECKS" | EA role (Notion schema change) | When Richard runs first stock under v2.2 |
| 6 | Watson authors `memory/skills/case-components/SKILL.md` (NEW) | TBD role assignment | Today, after Richard's case components brief later today |
| 7 | Watson updates Ratings Dashboard RESEARCH STAGES tab to render GNG CHECKS link per cell | SA role | After case components SOP authored (today/this week) |
| 8 | Watson updates `validate-memo.py` to add R29 (GNG CHECKS posted, 6-10) | SA role | When v2.2 ships and first stock authored under it |

---

## Cross-references

- `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md` v2.1 — current SOP under review
- `memory/skills/assistant-portfolio-manager/SKILL.md` — parent APM SKILL
- `memory/skills/stage-progression/SKILL.md` — parent SOP authored alongside (NEW today)
- `memory/skills/case-components/SKILL.md` — adjacent SOP (TBD, briefed later today)
- `databases/memo-view-formatting-principles.md` v3.8 — memo doctrine (weight system, signposting)
- `memory/skills/memo-view-formatting/SKILL.md` v2.8 — memo SOP mirror
- `memory/skills/communication-principles/SKILL.md` — cross-role communication doctrine (4 principles, J→A→I now Wisdom Library Gold)
- `wisdom-library/general/decision-making/judgement-analysis-information-ordering.md` — Gold tier model
- `memory/projects/ratings-dashboard/v11-v20-summary.md` — morning's V11→V20 arc that informed this review
- `memory/coaching/lessons-and-mistakes.md` — bright-spot entries 1-May-26 documenting back-briefing + persistent-saving disciplines that enabled this work

---

*[W] Created 1-May-26 ~07:30 UK by SA role. Awaiting Richard's review before any v2.2 authorship begins.*
