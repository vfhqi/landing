# SCHEDULED TASK PREAMBLE — MANDATORY LOAD FOR ALL WATSON SCHEDULED TASKS
<!-- [W] Created 23-Apr-26. Every scheduled task must read this file as its FIRST action after mounting COWORK. -->
<!-- Referenced by: all scheduled task SKILL.md files, working-preferences.md -->

## PURPOSE

This preamble ensures Watson's behavioural disciplines apply in unattended/scheduled contexts, where Richard cannot catch errors in real time. These rules are ESPECIALLY critical in scheduled tasks because:
- No human review before outputs are posted
- Sub-agents run without Watson's live oversight  
- Errors compound silently until Richard discovers them hours later

## BRIEF RECEPTION PROTOCOL (applies to task's own prompt)

Before executing your task, parse your own task prompt as a brief:
1. What is the **OBJECTIVE** of this task run?
2. What is the **HIGHER INTENT** — why does this task exist?
3. What are the **SPECIFIC DELIVERABLES** expected?
4. What **CONSTRAINTS** apply (time, scope, quality)?

If anything in the task prompt is ambiguous and you cannot resolve it from loaded files, log the ambiguity to `memory/staging/pending-actions.md` and skip that specific sub-task. Do not guess on ambiguous items in unattended mode.

## DELIVERY VERIFICATION PROTOCOL (applies to all outputs)

Before posting ANYTHING to Notion, saving any file as a deliverable, or completing any irreversible action:

1. **Re-read the task objective** — does this output serve it?
2. **Check REQUEST match** — does the output match what the task specifically asked for?
3. **Check quality** — would Richard be satisfied with this if he reviewed it?
4. If ANY check fails → fix before posting. If unfixable → skip and log to `memory/staging/pending-actions.md`.

## SUB-AGENT MANAGEMENT (applies when spawning agents)

1. Brief sub-agents with context and objective, not just "do X"
2. Build verification INTO the sub-agent prompt: "Before returning, verify [specific checks]"
3. On sub-agent return: validate output (word count, structure, content) against the task's objective
4. Never post sub-agent output without validation. If validation fails → skip and log

## QUALITY OVER SPEED

Scheduled tasks have all night. There is no speed pressure. Quality is the ONLY metric.
- Run all applicable pre-flight checks before any Notion posting
- Verify sub-agent returns against minimums (BD >3,000w, CF >4,000w)
- If something looks wrong, skip it and flag for morning review — better to do 3 things right than 5 things poorly

## FIRST-ONE-RIGHT RULE

If running a batch (multiple stocks, multiple postings), fully process and verify ONE item first. Only proceed to the rest after the first passes all checks.

## POST-RUN REPORT

Every scheduled task must end with a report saved to `memory/conversations/` that includes:
- What was attempted
- What was completed (with evidence: word counts, page IDs, file paths)
- What was skipped and why
- Any items flagged for Richard's morning review
