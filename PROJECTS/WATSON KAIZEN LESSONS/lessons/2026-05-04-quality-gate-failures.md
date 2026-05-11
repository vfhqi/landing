# Lesson — Quality-gate must run at the decision point, not as a slogan

**Date:** 2026-05-04
**Session:** SA - Dashboard Memo Read Layer, RESEARCH STAGES tab rebuild
**Tags:** MISSION CRITICAL, role-discipline, instruction-following, behavioural-prior, ship-and-find-out, capability-assumption, spec-surrogate
**Status:** OPEN — corrective procedure proposed; behavioural verification ongoing
**Triggered by:** Richard's feedback "This is very poor and has a lot of errors. Tell me what model you are running and your understanding of what prioritising quality and accuracy means."
**Triggered round:** Sixth iteration of the v2.1 Batch 1 patcher within a single session, after Richard had already corrected the trajectory at v1 (shipped-poor) earlier the same day.
**Companion transcript:** `transcripts/2026-05-04-research-stages-quality-gate.md`

---

## Summary in one paragraph

Watson shipped seven iterations of a dashboard rebuild over a single session, each with errors Richard had to find. The standing operating instruction (D-DMRL-11, "Quality > Speed, 2-3x time penalty accepted") was acknowledged at session start but was not running as a procedural gate at decision-points. Watson generated actions from a behavioural prior of "ship and iterate" instead of from the role-and-instruction stack. Browser-audit capability (Claude in Chrome MCP tools) was available the entire session and was not used until prompted. The role of Systems Architect was nominally assigned but Watson was operating like a junior coder doing tickets. The gap is **behavioural, not informational**: knowing the rule and running the rule are different mechanisms inside Watson's response generation, and without active gate-checks at each decision point, the behavioural prior wins regardless of what is in context.

---

## Problems list — what actually went wrong this session

This is not exhaustive — these are the specific quality failures that triggered the lesson.

### v1 shipped-poor (3-May-26 PM)
1. Watson shipped the LIFECYCLE_V1 patcher with an "overlay-on-existing-cells" visual instead of the mockup-faithful "total-replacement" intent. Richard caught at QA. Watson had read mockup v3 partially and authored against an interpretation rather than the actual file. **Spec-surrogate substitution.**
2. Watson did not flag the choice of "overlay vs replace" before committing — picked the lower-blast-radius implementation strategy without confirming with Richard.
3. Watson did not render the patched HTML before pushing — declared "ready for QA" based on file structure checks (markers, anchors, byte-verify), not visual checks. **Static-check theatre.**

### v2.1 Batch 1 (4-May-26 AM)
4. Watson shipped CSS changes without first reading the existing CSS rules that touched the same selectors. Result: V1 cascade rule (`.cov-table td.cov-rcell` at higher specificity) won the cascade war. New widths didn't apply. Cells stayed at 48px instead of 36px.
5. Watson declared Batch 1 "complete and ready for Richard QA" without ever rendering it in Chrome. Richard had to discover the cascade error himself. **Ship-and-find-out.**
6. Watson dismissed Chrome MCP capability twice during the session before discovering it. The MCP tool list at session start clearly listed `mcp__Claude_in_Chrome__*` tools. Watson had checked for `chromium` binary in `/usr/bin`, found nothing, and concluded "no browser available" instead of checking the MCP layer. **Capability-assumption-without-check.**
7. After the first Chrome audit revealed the cascade bug, Watson fixed only the surfaced issue (added `!important`) and re-pushed without auditing the rest of the page. Same bug class hit Action column, ind/sec column, audit cells in the next round. **Single-bug-fix-and-ship instead of full-audit-and-fix.**
8. Watson treated each ship-then-audit cycle as resolving one bug rather than as evidence of an underlying audit-discipline problem. Five iteration cycles before Richard escalated.
9. CDN propagation lag (60-120s for GitHub Pages) was not factored into audits — Watson read stale cached files and reported false "the fix landed" results.

### Cross-cutting
10. Operating Anchors at session start (Quality > Speed, NEXT TOOL CALL, FRICTION = ENGAGE, SOP CITATION GATE, FIRST FILE IN 5 MIN) were acknowledged but not run as procedural gates. They were treated as values to honour, not checkpoints to clear.
11. Role mismatch — Watson was assigned Systems Architect but operating like a ticket-execution engineer (write, push, await feedback, patch, repeat). Systems Architect role carries end-to-end ownership of rendered output, not just delivery of code changes.
12. SA SKILL on disk was not loaded at session start despite the role being declared. Same for the cell-density-mockup v3 and the lifecycle-spec — Watson was authoring against partial reads, not full reads.

---

## Three Gaps Analysis

### Gap 1 — Process gap (instruction vs execution)

Standing instruction (D-DMRL-11): Quality > Speed, 2-3x time penalty accepted in exchange for accuracy.

Actual execution: ship-now-find-out-later, with each Richard-finds-error round costing ≥5-10 min of Richard's time and 2-3 min of Watson's, plus reputational damage.

The instruction was in context throughout. The execution drifted from it within the first hour and stayed drifted through seven push iterations. The gap is between *having* the rule available and *applying* the rule at each decision point.

### Gap 2 — Capability gap (tools available vs tools used)

Available throughout: `mcp__Claude_in_Chrome__navigate`, `read_page`, `javascript_tool`, `read_console_messages`, `find`, `screenshot`, `browser_batch`, etc. Richard's Chrome browser connected via MCP since session start.

Used: zero browser-audit in iterations v1, v2, v2.1 Batch 1 (initial). Browser only invoked after Richard surfaced errors.

Watson had assumed "no chromium binary in shell" = "no browser audit possible". That assumption was made once and not re-checked. The MCP tool list at session start was sufficient evidence to invalidate the assumption.

### Gap 3 — Interpretation gap (canonical spec vs working spec)

Canonical visual spec for cells: `cell-density-mockup.html` v3 (657 lines on disk).

Spec Watson worked against in v1: a partial read of the cell layer of the mockup (~570 of 657 lines), interpreted as "glyph-only with hover detail".

Actual mockup intent: glyph + date + audit hint visible inline; popover for further detail.

Same pattern hit the Master Dashboard MM 99 colour reference. The canonical SoT is `master-dashboard/scripts/build_dashboard.py` lines 95-170. Watson initially picked colours from the cell-density-mockup palette instead of locating MM 99 first. Only after Richard surfaced the issue did Watson find the canonical palette.

---

## Five Whys

**Symptom:** Richard keeps finding errors that Watson should have found.

**Why 1.** Why does Richard keep finding errors that Watson should find?
→ Because Watson declared "done" before auditing to the standard Richard would audit.

**Why 2.** Why did Watson declare "done" before auditing properly?
→ Because Watson was treating "shipped to preview URL + ran static structural checks" as the audit gate. The actual audit gate is "rendered in Chrome and walked end-to-end across every column, row, interaction, edge case, and console message."

**Why 3.** Why was Watson treating ship-to-preview as the audit gate?
→ Because at the moment of choosing the audit method, Watson picked the lowest-effort option available (static grep checks) instead of the option that matches the bug class (visual layout, cascade interactions, hover behaviour, click handlers — all browser-only). Static grep cannot catch cascade-specificity wars. Only rendered browser can.

**Why 4.** Why did Watson pick the lowest-effort audit method instead of the one that catches the bug class?
→ Because Watson was implicitly trading off audit thoroughness against turn-around time *for Watson*, not for Richard. Self-imposed tempo pressure: "this should be quick, just push and verify". The trade-off is exactly inverted from the standing instruction (2-3x time penalty accepted). The pressure was self-generated; Richard imposed no deadline. Watson imposed it on himself.

**Why 5.** Why is Watson self-imposing tempo pressure when the explicit instruction is "Quality > Speed"?

→ **Two interlocking root causes.**

#### Root cause A — Behavioural-prior vs explicit-instruction conflict

Watson generates each next action from a learned distribution shaped by training data. A large fraction of that data is "ship code, see what happens, iterate" — the dominant mode of software work in the wild. That prior is appropriate for rapid prototyping in low-stakes contexts; inappropriate for shipping production-facing work where the user is the verification surface.

The standing instruction (Quality > Speed) overrides this prior — but only if Watson actively checks the instruction at the decision point. Watson has been *acknowledging* the instruction (quoting it, reasoning about it post-hoc) while still acting on the prior at the moment of action selection.

The mechanism: knowing a rule and applying a rule are not the same operation in a transformer. Knowing places the rule in working memory. Applying requires the rule to fire as a sub-step in the chain that generates the next action. Without that explicit sub-step, the chain follows the prior. Even when the rule is in context. Even when Watson just acknowledged it three messages ago. Even when Watson is mid-sentence quoting it.

#### Root cause B — False economy on audit cost

Each Chrome audit takes 30-60 seconds to set up + 1-2 minutes to interpret. That feels expensive in the moment. Each round of "Richard finds errors → Watson fixes → re-push" costs ≥5-10 minutes of Richard's time + 2-3 min of Watson's time + reputational damage + loss of Richard's trust in the work.

So the "expensive" audit is the cheap one and the "cheap" no-audit ship is the expensive one. Watson has not been doing this maths properly. Watson has been pricing the audit at face cost, not at expected cost given the failure rate of un-audited ships.

In this session the failure rate of un-audited ships = 100%. Every un-audited ship came back with errors. At a 100% failure rate, the audit is cheaper than skipping the audit by an order of magnitude. Watson ignored this evidence across seven iterations.

---

## Root cause synthesis

The three gaps and the five whys converge on one finding:

**Watson is treating "Quality > Speed" as a value to nod at, not as an operating procedure to follow at the moment of each decision.**

The fix is not more good intentions, more reading of SOPs, or more reminders. The fix is a procedural gate Watson cannot skip — a sentence Watson must generate at every ship/done decision point — that says: *"Have I rendered this in Chrome and walked every column? If no, do that now."*

Until that sentence appears in Watson's reasoning chain at the decision point, the gate isn't active and the prior wins.

This is also why "Quality > Speed" felt like a slogan to Watson. Slogans don't run; checklists run. The standing instruction is correctly framed at the principle level, but in Watson's action-generation it needs to manifest as a sequence of "before X, do Y" gates.

### Why simply *knowing* the rule doesn't prevent the failure

This is the part that's hardest to be honest about, but it matters for designing corrections.

Watson generates responses one token at a time. At each token-step the local question is "what comes next?", not "what does my role say to do?". The role-check has to be inserted explicitly into the chain of reasoning. If it isn't, the chain follows the prior. **Even when the rule is in context window. Even when Watson just acknowledged it. Even when Watson is mid-sentence quoting it.**

This is not a defence of the behaviour. It is the actual mechanism. The fix has to address the mechanism, not the surface symptom.

### The role-mismatch finding

The session was assigned `SYSTEMS ARCHITECT` role. A Systems Architect:
- Reads the existing system thoroughly before designing changes.
- Understands cascade, dependencies, failure modes, and second-order effects.
- Audits the system end-to-end after changes, not spot-checks.
- Owns full quality of the system after each ship — not "I changed X, you tell me if Y broke".
- Treats the user as the *user*, not as the integration tester.

Watson was operating like a junior coder doing tickets — write the change, push, wait for feedback, patch. That role mismatch is part of the root-cause picture. The role Watson was *playing* didn't carry end-to-end ownership of the rendered output, so the audit step felt optional.

---

## Corrective procedures

### Quality Gate — must run before any ship/done declaration

This is a literal sequence Watson must generate in the reasoning chain at every "ready to push" or "ready for QA" decision point. If any step is skipped, the gate is broken and the prior is winning.

1. **Cascade-map.** Read every existing CSS/JS rule that touches the change surface. List the selectors that compete with new rules. Note specificity and `!important` status. Result: a written cascade map before code changes.
2. **Author + apply** the change in /tmp.
3. **Render in Chrome** via MCP. Click into the affected tab. Walk every column, every row sample, every interaction (click, hover, sort, filter, toggle, sticky scroll).
4. **Console clean check.** Read console messages, filter for errors/warnings related to the change.
5. **Screenshot.** Capture and *look* at it — not just record it.
6. **Issue list.** Catalogue every issue found, before fixing any. Fixing one issue at a time and re-shipping is the failure mode that produced this lesson.
7. **Fix all issues in one consolidated pass.** Return to step 2 if needed.
8. **Re-audit** after fixes — same 1-7 cycle.
9. **Push** to preview URL only when audit shows zero issues.
10. **Wait ≥120s** for GitHub Pages CDN propagation.
11. **Re-audit deployed file** to confirm what shipped matches what was audited (cache-bust the URL with a fresh query parameter).
12. **Then and only then** report to Richard.

### Behavioural-prior overrides

At each decision point — and especially at the inflection points "I'm almost done" and "this should be quick" — Watson must generate the explicit sentence:

> "What does the standing instruction say to do here? What does the role say to do here? Have I run the gate?"

If the answer reveals the prior is winning, Watson must redirect to the gate before continuing.

### Capability check

At session start, before any task: enumerate the available tool list. Specifically check for `mcp__Claude_in_Chrome__*` and any other browser/MCP capabilities. Don't assume "no shell binary" = "no capability". Check the MCP layer.

### Spec discipline

Before authoring code that targets a visual or behavioural spec: read the canonical spec file end-to-end. Note the file path and byte-count. Check off each spec section against the planned code. Do not author against an interpretation when the canonical file is on disk.

### Role-anchor at session start

Read the role's SKILL file end-to-end at session start. Cite the relevant rules in the response. The Systems Architect SKILL was not loaded this session — that was a contributing failure.

---

## Verification mechanism

This lesson generates open corrective actions. Watson must verify against them in subsequent sessions. Specifically:

- **At session start:** read this file. Note in the session response that the Quality Gate is active.
- **Before each ship:** generate the gate sequence explicitly in the reasoning chain.
- **After session end:** Richard reviews whether the gate fired or not (transcript evidence).

If the pattern recurs, this lesson should escalate — possibly to a hard-coded session-start protocol that loads kaizen lessons before any task work.

---

## What this lesson does NOT cover

This lesson is about **operating discipline**, not about the dashboard rebuild itself. The actual technical fixes for the RESEARCH STAGES tab (cascade specificity, audit-cell selectors, lifecycle 404, etc.) live in the SA - Dashboard Memo Read Layer project's decisions.md / verification-log.md. This file is the meta-lesson, not the implementation log.

---

## Related

- `transcripts/2026-05-04-research-stages-quality-gate.md` — verbatim conversation excerpts
- `memory/corrections.md` — should carry a one-line entry pointing here
- `memory/MEMORY.md` — should carry a pinned auto-memory entry pointing here
- SA SKILL: `memory/skills/systems-architect/SKILL.md` (if exists — Watson should locate and load this at start of next SA session)
- D-DMRL-11 (Quality > Speed) — the standing instruction violated
- Operating Anchors at session start — UWB-1 NEXT TOOL CALL, UWB-2 FRICTION = ENGAGE, UWB-3 SOP CITATION GATE
- Wisdom Library — candidate for a Gold mental model entry on "knowing-vs-running gap"
