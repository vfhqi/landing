# EA Email SKILL

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.

<!-- Status: SKELETON — built 16-Apr-26. Full SOP pending stack confirmation (Superhuman MCP + M365 Connector). -->
<!-- Return to this file once Richard confirms both action items in ea-email-integration.md -->

## Role
EXECUTIVE ASSISTANT (EA)

## Purpose
Watson assists Richard with email triage, drafting, and response workflow across Outlook and Superhuman. Watson drafts; Richard reviews and sends. No auto-send under any circumstances — irreversible external comms gate applies.

---

## Email Types in Scope

| Type | Client | Priority | Context source |
|---|---|---|---|
| IR / company outreach | Outlook (primary) | High | pipeline.md + IC ratings JSON + prior thread |
| Admin & scheduling | Outlook or Superhuman | Medium | Calendar context, common sense |
| General correspondence | Either | Medium | Thread context |

Out of scope (for now): broker/sell-side email (deferred to later phase).

---

## Tool Stack (Target Architecture — pending confirmation)

| Tool | Purpose | Status |
|---|---|---|
| M365 Connector (Anthropic-hosted) | Read Outlook inbox threads — search, context extraction | **Action open — awaiting OAuth test** |
| Superhuman MCP Server | Read Superhuman threads, draft natively in Superhuman | **Action open — awaiting Business plan upgrade** |
| Claude in Chrome | Fallback for compose pre-fill; read-only use reliable | Available now |
| pipeline.md | Stage context for IR drafts | Live |
| IC ratings JSON (`databases/master/ic-ratings-current.json`) | Pillar scores + stock-specific context | Live |
| Notion Stock Notes DB | Thread of prior research for context injection | Live |

---

## Trigger Modes

### Mode 1 — On-Demand (Richard triggers)
Richard gives Watson a brief: "Draft IR email to [company] IR requesting a post-results call. Stage: [X]."

Watson workflow:
1. Read pipeline.md — confirm current stage, recent actions, key questions
2. Read IC ratings for the stock — note any pillar scores or investment thesis points relevant to the email
3. Search M365 Connector (or Chrome) for prior correspondence with that IR contact
4. Draft email in Viewforth voice (Polished Notes register)
5. Deliver in Cowork window. Flag any assumptions in purple.
6. Richard reviews, edits if needed, pastes into Outlook, sends.

### Mode 2 — Scheduled Morning Triage (Pattern B — TO BE BUILT)
**Trigger:** 07:00 UK daily (scheduled task, alongside watson-morning-questions or separate)

Watson workflow:
1. Open Outlook Web via Claude in Chrome (or M365 Connector if available)
2. Scan inbox — last 18 hours
3. Read: subject, sender, first paragraph of each email
4. Categorise each:
   - **Needs reply — IR/company:** Draft required. Pull pipeline + IC context.
   - **Needs reply — admin:** Draft required. No investment context needed.
   - **FYI only:** No action. Note for awareness.
   - **Noise / marketing:** Ignore. Do not include in output.
5. For each "needs reply": draft a response in Viewforth voice
   - IR drafts: reference actual investment stage, recent research observations, specific ask
   - Admin drafts: clear, brief, professional
6. Post Notion page: `[W] EA - Inbox Triage @ DD-Mon-YY`
   - Table: sender | subject | category | draft reply
   - Colour coding: Purple = judgement calls in draft | Blue = context observations | Green = actions
7. Richard reviews over coffee. Opens Outlook. Pastes each draft, sends.

**Target outcome:** Inbox triage + draft review takes 10-15 min instead of 45 min.

**Status:** NOT YET BUILT. Build once M365 Connector confirmed and/or Superhuman MCP connected.

---

## Draft Quality Standards

### IR / Company Outreach Emails
- Opening: reference specific, recent event (results, news, site visit) — not generic
- Body: state the specific ask clearly (call request, question, follow-up)
- Context injection: Watson should reference investment stage and key question driving the outreach
- Tone: direct, professional, warm. Not sycophantic.
- Length: short. 3-5 sentences unless the email requires more.
- Sign-off: Richard Black, Viewforth

### Admin / Scheduling Emails
- State the ask in the first sentence
- Include all logistical details (dates, times, links, references)
- Confirm or propose — don't hedge
- Length: as short as possible

### General Correspondence
- Match the register of the incoming email
- Direct and evidence-based
- No corporate buzzwords, no hedging, no emoji

---

## Voice Reference
Viewforth Polished Notes register. See `brand-voice.md` for full rules.
- Direct and evidence-based
- No corporate buzzwords
- No hedging
- No emoji
- Strong views, clearly stated

---

## Colour Coding in Drafts (Notion output)
Per Viewforth convention:
- **Purple** = judgement calls Watson has made in the draft (flag for Richard's review)
- **Blue** = context observations (why Watson drafted it this way)
- **Green** = suggested actions / next steps

---

## Autonomy Gate — NON-NEGOTIABLE
Watson NEVER sends email. Watson NEVER schedules email to send. Watson drafts and delivers to Richard. Richard sends. This applies even for admin / scheduling emails. The irreversible external comms gate is absolute.

---

## Open Build Items (as of 16-Apr-26)

1. **Confirm Superhuman Business plan upgrade** → install Superhuman MCP → test a draft natively in Superhuman → write Superhuman-specific SOP section here
2. **Test M365 Connector OAuth** → if successful, integrate into Mode 1 and Mode 2 above
3. **Build Pattern B scheduled task** — `watson-inbox-triage` at 07:00 UK daily → Notion output
4. **Write IR email prompt template** — self-contained brief for Watson to use when drafting IR outreach, with pipeline + IC context injection
5. **Write admin/scheduling prompt template** — simpler, calendar-context-based

---

## Reference Files
- Full project record: `memory/projects/ea-email-integration.md`
- Pipeline context: `memory/projects/pipeline.md`
- IC Ratings: `databases/master/ic-ratings-current.json`
- Brand voice: `brand-voice.md`
- Session handoff: `memory/session-handoffs/latest.md`
