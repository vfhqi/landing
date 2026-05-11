---
name: EA Email Integration Project
description: Full research, proposals, and architecture decisions for getting Watson (EA role) involved in Richard's email workflow across Outlook and Superhuman
type: project
---

# EA Email Integration Project
<!-- Created: 16-Apr-26 | SA session -->

## Project Status
**PAUSED — 16-Apr-26.** Research complete. Proposals made. Two parallel action tracks open. Return here to resume.

## Context & Why This Exists

Richard uses **Outlook** (primary, business M365 account, Viewforth) and **Superhuman Mail** (AI writing, secondary). He also has Gmail connected but uses it as secondary.

Watson currently has no access to either email client. The EA role has no email capability. The gap: Watson holds all investment context (pipeline, IC ratings, Viewforth voice, stock theses) but can't reach email clients. Superhuman's own AI can reach the inbox but knows none of Richard's investment context. This project bridges that gap.

**Trigger for this session:** Richard asked how the EA role could be involved in emails, specifically given he uses Outlook + Superhuman. He wants Watson to help with:
- Drafting replies (biggest pain point — drafting + triage)
- Triage and prioritisation of incoming email
- Email types: IR/company outreach, admin & scheduling, general correspondence (NOT broker/sell-side — at least not initially)

**Autonomy constraint (firm, as of 16-Apr-26):** Watson drafts only. Richard approves and sends every email. No auto-send. This is non-negotiable for now — irreversible external comms gate applies.

**Preferred handoff mode:** Compose in browser (Claude in Chrome pre-filling the compose window) — however, research shows this is fragile (see below). Pattern B (scheduled triage with drafted replies) is the more robust equivalent.

---

## Research Findings (16-Apr-26)

### Claude in Chrome — Outlook Web / Superhuman
- Can navigate to `outlook.office.com` and `mail.superhuman.com`
- Can read email threads (subject, sender, full content) via DOM — fully reliable
- **Compose/pre-fill: FRAGILE.** Rich-text editors (contentEditable divs, iframe-based) in both Outlook Web and Superhuman are not standard `<textarea>` elements. Claude in Chrome's form_input tools work inconsistently with these. Reliability ~70%. Not production-grade for daily use.
- Read-only use of Chrome is reliable; write/compose is not.

### Superhuman — Native AI & MCP
- Superhuman has native AI features: Write with AI, Instant Reply, Ask AI, Auto-summarize
- **Superhuman MCP Server exists** — connects to Claude via Model Context Protocol
- Supports: read threads, draft replies in Richard's learned voice, queue for user review. Does NOT auto-send.
- Requires: **Superhuman Business plan** (or higher). Chrome must be open with Superhuman running.
- Richard confirmed he is happy to upgrade to Business plan to unlock this.
- Status: **ACTION OPEN — Richard to upgrade plan and check MCP settings in Superhuman.**

### Microsoft 365 Connector (Anthropic-hosted)
- Official connector via Anthropic — set up through Claude.ai Settings → Integrations
- **Read-only:** can search, read, analyse email threads via Microsoft Graph API
- Cannot draft, compose, or send emails
- Requires Microsoft 365 business account (Viewforth account likely qualifies)
- **Enterprise tenant risk:** If IT admin approval is required in Azure AD, may be blocked. Richard is likely his own admin (solo operator) so probably fine. Test confirms immediately — if blocked, message says "Your organisation requires admin approval."
- How to test: Claude.ai → Settings → Integrations → Microsoft 365 → Connect → Microsoft OAuth flow
- Status: **ACTION OPEN — Richard to attempt OAuth connection and report back.**

### Community Outlook MCP Servers (third-party)
- Several exist (`ryaker/outlook-mcp`, `littlebeanapps/outlook-mcp`, etc.)
- Some support draft creation and sending via Microsoft Graph API
- Variable maturity; require local server setup
- Not recommended as first step — too much friction for a non-developer setup

### Gmail MCP
- Most mature email MCP available
- Supports `create_draft()` — drafts without sending
- Gmail is connected to Richard's account but is secondary
- Not the priority given Outlook + Superhuman are primary

---

## Four Proposals Evaluated

### Proposal 1 — Claude in Chrome Read + Draft (Available Now, Zero Setup)
Watson opens email client in Chrome, reads thread context, writes draft in Cowork window. Richard copy-pastes into Outlook/Superhuman.
- **Pro:** Zero setup. Works today. Watson can pull IC ratings + pipeline before drafting.
- **Con:** Copy-paste step is manual. Compose pre-fill is fragile (~70%).
- **Verdict:** Good for immediate use on high-stakes IR emails. Not scalable for daily triage.

### Proposal 2 — Superhuman MCP Server (Best Near-Term for Superhuman emails)
Native MCP connection. Watson reads threads, drafts in Richard's learned voice, queues for review. Draft appears natively in Superhuman compose window.
- **Pro:** Cleanest integration. No copy-paste. Approve-before-send enforced by design. Superhuman voice learning + Watson context = better drafts than either alone.
- **Con:** Superhuman-only. Chrome must be open. Requires Business plan.
- **Verdict:** High priority once Business plan is confirmed. Install MCP, test this week.

### Proposal 3 — M365 Connector + Watson Drafts to Text (Robust Infrastructure Layer)
M365 Connector gives Watson read access to Outlook inbox. Watson searches thread history before drafting. Draft delivered as text in Cowork / Notion. Richard pastes and sends.
- **Pro:** Read reliability 95%+. Watson finds email context itself — no manual forwarding required. Enterprise-grade, Anthropic-hosted.
- **Con:** Read-only. Paste step remains manual.
- **Verdict:** Install regardless of other choices. This is the infrastructure layer. Eliminates the biggest friction (manually pasting context into Watson).

### Proposal 4 — Hybrid Architecture (RECOMMENDED FULL DESIGN)
Combines Proposals 2 + 3 as a coherent EA email system:

| Email type | Tool stack | Watson action |
|---|---|---|
| IR/company outreach (Outlook) | M365 reads thread → Watson drafts → Richard pastes | Watson pulls IC ratings + pipeline stage before drafting |
| Admin/scheduling (Outlook or Superhuman) | M365 reads context → Watson drafts as text | Short drafts, lower context dependency |
| Superhuman correspondence | Superhuman MCP drafts natively | Watson context injected via prompt |

Watson's IR drafts reference actual investment stage (e.g., "Following your Q4 results, I noted X in your commentary and wanted to discuss Y") — not generic outreach. Context injection is automatic from pipeline.md and IC ratings JSON.

---

## Proposed Pattern B — Scheduled Morning Inbox Triage (HIGH VALUE)

Richard's preferred model for "proactive response email work" — Watson monitors and proposes drafts, not just reacts to triggers.

**How it works:**
1. **07:00 scheduled task** (alongside or separate from watson-morning-questions)
2. Watson opens Outlook Web via Claude in Chrome → scans inbox last 18 hours
3. Reads subject, sender, first paragraph of each email
4. Categorises: IR/broker outreach → needs reply | admin → needs reply | FYI → no action | noise → ignore
5. For "needs reply": checks pipeline.md + IC ratings JSON for relevant context (e.g., email from MTU IR → Watson knows stage = Triage complete, 6 [C] pages posted)
6. Drafts reply for each in Viewforth voice (Polished Notes register), colour-coded per convention
7. Output: Notion page titled `[W] EA - Inbox Triage @ DD-Mon-YY` — table of emails + draft responses. Posted before Richard wakes up.
8. Richard reviews over coffee, edits drafts if needed, opens Outlook, pastes and sends. Target: 10-15 min vs. 45 min manual.

**Why this is the right design:** Separates context retrieval (M365 Connector, reliable) from draft delivery (Watson drafts → Richard sends). EA role has investment context, not just a faster typist. Fits existing morning cadence. Gate — approve before send — preserved by design.

**Note on limitations:** Watson cannot sit passively watching the inbox. All Watson actions start from either (a) Richard triggering, or (b) scheduled task at set time. True event-driven monitoring (triggered by incoming email) is not available today — would require webhook support from M365 or Superhuman, neither of which currently exists.

---

## Open Action Items (as of 16-Apr-26)

| # | Action | Owner | Status |
|---|---|---|---|
| 1 | Upgrade Superhuman to Business plan | Richard | Open |
| 2 | Check MCP section in Superhuman settings once upgraded | Richard → Watson | Open |
| 3 | Attempt M365 Connector OAuth in Claude.ai Settings → Integrations | Richard | Open |
| 4 | Report back on both — Watson will configure MCP and build SOP | Watson | Waiting on Richard |
| 5 | Once stack confirmed: build Pattern B morning triage scheduled task | Watson | Pending |
| 6 | Write full EA Email SOP into `memory/skills/ea-email/SKILL.md` | Watson | Skeleton done (see file) |

---

## Next Session — Resume Protocol

When returning to this project:
1. Read this file in full
2. Read `memory/skills/ea-email/SKILL.md`
3. Ask Richard: (a) Superhuman plan status, (b) M365 Connector result
4. If both confirmed → proceed to Pattern B scheduled task build + full SOP
5. If M365 blocked → proceed with Chrome-only triage workflow (less clean but functional)
6. If Superhuman MCP available → connect it, test a draft, write Superhuman-specific SOP section

---

## Key Decisions Made

- Autonomy level: **Draft-only. Richard approves and sends every email.** No exceptions for now.
- Email types in scope: IR/company outreach, admin/scheduling, general correspondence
- Email types out of scope (for now): broker/sell-side
- Preferred handoff: compose in browser (aspirational); Pattern B triage page (practical)
- M365 Connector: install regardless — read access is the infrastructure layer
- Superhuman MCP: high priority once Business plan confirmed
- Community Outlook MCP: deferred — too much setup friction
- Gmail MCP: not priority (Gmail is secondary)
