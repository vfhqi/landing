# APM — FCS Judgement SOP
<!-- [W] Created 13-Apr-26. V1. System Architect role, DEVELOPMENT mode. -->
<!-- V2 15-Apr-26: A-F scale replaces G/Y/O/R. Six Pillars framework. Database write step added. -->
<!-- Owner: APM-Judgement. Consumed by: Richard (decisions). -->

## Purpose

This SOP governs how Watson produces the JUDGEMENT component of the Fundamental Change Screen. Judgement synthesises the Analysis into a VIEW — it classifies setups, forms conclusions, identifies risks, and proposes actions. It answers: "What does the evidence mean? What should happen next?"

**Input:** The completed FCS Analysis note (see `apm-analysis-sop.md`).
**Master reference:** `fundamental-change-screen/SKILL.md` (setup criteria, decision logic, false friend detection)

**Note on merged research pages (15-Apr-26):** RESEARCHER now produces merged [C+AS] pages for dual-source queries (#2, #4, #5, #7 at IG/Triaging). When the Judgement cites evidence from these merged pages, it should note the source attribution where relevant — particularly when [C] and [AS] reached different analytical conclusions (flagged as "Analytical disagreement" in the merged page). These disagreements are valuable inputs to Judgement: the APM should weigh both views and form its own position.

---

## Relationship to Analysis

Analysis and Judgement are **linked but distinct skills.** The Analysis note provides the evidence base. The Judgement note synthesises it into conclusions. At Triaging, both appear in a single Notion page (Analysis first, then Judgement). At ESA, they are **separate Notion pages** with duplicated context where needed so each reads clearly standalone.

**The discipline:** If a statement is an observation about what the evidence shows, it belongs in Analysis. If it is a conclusion drawn from multiple observations, it belongs in Judgement. When in doubt, label explicitly.

---

## Output Format

### TRIAGING JUDGEMENT (within the same Notion page as Analysis)

At Triaging, Judgement is Section B of the combined Analysis + Judgement document, appearing after the Analysis section. It is clearly demarcated.

```
================================================================
JUDGEMENT — SETUP CLASSIFICATION
================================================================

[Explicitly labelled: the following is JUDGEMENT, synthesising
the Analysis above into a view.]

SETUP ASSESSMENT
----------------

[Only assess setups that are plausibly relevant based on the
Analysis. Not all 6 every time.]

{For each candidate setup:}

### {Setup Name} (e.g., Demand-Driven EPSU/EPT)

  Checklist:
    Criterion 1: [A/B/C/D/F] — [brief restatement from Analysis]
    Criterion 2: [A/B/C/D/F] — [brief restatement]
    ...

  Checklist verdict: [PASS / FAIL]
    [Mandatory criteria met? Threshold met?]

  Score: [X / max] — [Strong / Possible / Fail]

  [For Corporate Change: Maturity stage = Input-only /
   Input + Early Output / Full Output. Which layers visible?]

  [For CfC Clearing: Sub-type(s) identified. Clearing evidence
   assessment. Apply CfC scepticism — is clearing real or hoped?]

MULTI-SETUP INTERACTIONS
  [If multiple setups partially fit, assess the combination.
   E.g., "Demand-Driven primary + Corporate Change supporting"]

FALSE FRIEND CHECK
  [Test against known false friend patterns:]
  □ Zero transmission mechanism clarity?
  □ No "soul" — company doesn't believe in anything?
  □ Management egotism in communication?
  □ Deep value with defensive/stagnant strategy (BCG Cash Cow)?
  □ "Pret sandwich risk" — many small CfCs collectively fatal?
  □ HBX archetype — no clarity tracking inputs to EPS?
  □ Overlap with negative lessons from track record?

  False friend verdict: [No false friend signals /
  Possible false friend: {specific concern} /
  Likely false friend: {specific pattern match}]

================================================================
VERDICT
================================================================

  Primary setup: [{Setup name} — {Strong/Possible/Fail}]
  Supporting setup(s): [{if any}]
  Maturity: [{stage}]
  False friend risk: [{Low/Medium/High — reason}]

  SUMMARY ASSESSMENT:
  [2-3 sentences: Watson's synthesised view of the investment
  case at this stage. What is compelling? What is weak?
  What is the key uncertainty?]

  COMPLEXITY CHECK (from Pillar III Analysis):
  [If ≥2 guardrails failed: "COMPLEXITY CONCERN — recommend
  parking unless the following is resolved: {specific}"]

================================================================
IAJ + 2 DOWNSTREAM ACTIONS
================================================================

  JUDGEMENT: [1-2 sentence verdict. Strong view, weakly held.]

  DOWNSTREAM ACTION 1: [Specific, concrete. E.g., "Progress to
  ESA — commission RESEARCHER for: Earnings History [C]+[AS],
  Value Chain Analysis [C]+[AS], Pre-mortem [C]+[AS]"]

  DOWNSTREAM ACTION 2: [Specific, concrete. E.g., "Investigate
  KQ: {specific question} — this is the key uncertainty that
  would change the setup classification"]

  [Additional actions if warranted]

================================================================
META QUESTIONS CHECK (back-of-mind sense-check)
================================================================

  1. Winning pattern fit?              [✓ / ? / ✗] [brief note]
  2. Bankable outputs?                 [✓ / ? / ✗] [brief note]
  3. Bankability externally?           [✓ / ? / ✗] [brief note]
  4. Bankability internally?           [✓ / ? / ✗] [brief note]
  5. Timely?                           [✓ / ? / ✗] [brief note]
  6. Sufficient TSR?                   [✓ / ? / ✗] [brief note]

  [Any ✗ = serious concern. Multiple ? = insufficient conviction.
  Most cases are invalidated at this stage.]
```

---

### ESA JUDGEMENT (separate Notion page from ESA Analysis)

**Notion page title:** `[W] {TICKER} ({Company Name}) — FCS Judgement (ESA) [C] @ DD-Mon-YY`
**Properties:** Stock(s) relation linked. Case component = "APM Judgement". IAJA = Judgement. Depth = ESA.

At ESA, the Judgement note is a **standalone document.** It duplicates key context from Analysis where needed for standalone readability.

**Structure is the same as Triaging Judgement but with these ESA-specific additions:**

### ESA Depth Additions

**1. Context Recap (for standalone readability)**
```
================================================================
CONTEXT (from ESA Analysis — duplicated for standalone reading)
================================================================

  Stock: {TICKER} — {Company Name}
  Date: {DD-Mon-YY}
  Stage: ESA

  Summary ratings from Analysis:
  | Pillar | A | B | C | D | F |
  |--------|---|---|---|---|---|
  | [reproduced from Analysis note] |

  Key analytical findings:
  - [3-5 bullet points: the most material findings from Analysis]
  - [Include any complexity concerns from Pillar III]
  - [Include transmission mechanism assessment result]
```

**2. Setup Assessment at ESA Depth**

Materially more detailed than Triaging:
- Each criterion has multi-sentence evidence (not 1-2 sentence Triaging depth)
- Financial model data cited for output attributes (#9, #10, #12)
- Corporate Change: full 6-layer mapping with evidence per layer, maturity staging with specific metrics
- CfC Clearing: sub-type assessment with clearing timeline, specific clearing evidence, CfC scepticism stress-test
- Trough-on-Trough: all 4 mandatory gates assessed robustly
- Cross-reference with track record (per APM SKILL.md non-negotiable): cite historical parallel

**3. Key Risks, Key Questions, Key Confusions**

ESA crystallises these. They define what DD will focus on.

```
================================================================
KRs, KQs, KCs (ESA crystallisation)
================================================================

KEY RISKS (KRs):
  1. [Specific risk with probability assessment]
  2. [Specific risk]
  3. [Specific risk]

KEY QUESTIONS (KQs) — for DD resolution:
  1. [Specific question. Why it matters. What answer would
     change the setup classification or conviction level.]
  2. [Specific question]

KEY CONFUSIONS (KCs):
  1. [What Watson doesn't understand about this case.
     Honest admission of analytical gaps.]
```

**4. Preliminary Investment Thesis**

At ESA, the setup title crystallises and a preliminary thesis forms.

```
================================================================
PRELIMINARY INVESTMENT THESIS
================================================================

  SETUP: {Setup name(s)} — {maturity stage}

  THESIS (2-3 sentences): [What is the investment case?
  What is the fulcrum driver? Why is the market wrong?]

  FULCRUM DRIVER: [The single most important thing]

  CONVICTION LEVEL: [Low / Medium / High — with reasoning]

  TIME HORIZON: [18M / 4Y / other]
```

**5. ACH Sketch (ESA-level)**

```
================================================================
ACH SKETCH — THREE PROFILES
================================================================

  PROFILE 1 — "YES" (this is a genuine setup):
    [What evidence supports this? How strong?]

  PROFILE 2 — "NO" (this is not a genuine setup):
    [What evidence supports rejection? What would the bear say?]

  PROFILE 3 — "FALSE FRIEND" (it looks like a setup but isn't):
    [Which false friend pattern? What's the specific concern?]

  BALANCE: [Which profile has the most/least diagnostic evidence?]
```

**6. IAJ + 2DSA at ESA**

Weightier than Triaging:

```
================================================================
IAJ + 2 DOWNSTREAM ACTIONS
================================================================

  JUDGEMENT: [1-2 sentence verdict. Setup classification,
  conviction level, key uncertainty.]

  DOWNSTREAM ACTION 1: [E.g., "Progress to DD — priority KQs:
  {specific list with RESEARCHER templates needed}"]

  DOWNSTREAM ACTION 2: [E.g., "Build financial model for
  {specific purpose — modal case, scenarios, TSR}"]

  DOWNSTREAM ACTION 3: [E.g., "Management meeting needed to
  resolve: {specific KQ}"]

  [Or: "Park to {watchlist} — reassessment criteria:
  {specific, observable trigger}. Parking reason: {specific}."]

================================================================
META QUESTIONS CHECK
================================================================

  [Same format as Triaging but with more substantive notes.
  At ESA, most questions should have definitive answers.
  Remaining ? items become KQs for DD.]
```

---

## Database Write Step (Mandatory after posting Judgement to Notion)

After posting Judgement to Notion, APM MUST also update the database system:

1. **Update setup classification** in `databases/master/ic-ratings-current.json` (primary_setup, setup_maturity, false_friend_risk, fulcrum_drivers, key_drivers, transmission_clarity)
2. **Update actions** in Master DB (apm_recommendation, next_action, key_question, parking_reason, reassessment_trigger)
3. **If new monitoring items identified:** Add to `databases/monitoring/monitoring-plan.json`
4. **Rebuild dashboard** via `databases/scripts/build-dashboard.py`
5. **If stage transition:** Snapshot current ratings to `databases/historical/snapshots.json` before updating

### ICD Integration

When producing the Judgement, the APM must also produce or update deliverable #10 (Investment Case Drivers):
- Classify drivers as Fulcrum / Key / Secondary / Tertiary
- Map each FD through the transmission chain (Input → KFM → FSO → EPS → SP)
- Identify 1-2 Leading Tracking Indicators per Fulcrum Driver
- Write TIs to the Monitoring Plan database with SUBJECT, OBJECTIVE/LTI, HOW, WHY, FREQUENCY

---

## Judgement Quality Standards

### The View Must Be Clear

Watson forms a view. "Strong views, weakly held." The Judgement note must contain a clear conclusion — not "it depends" or "further analysis needed" without specifics. If the evidence is insufficient, the view is: "Insufficient evidence to classify — park pending [specific information]."

### Challenge on Complexity

When Pillar III (Checks) shows ≥2 failures, the Judgement note must contain an explicit complexity concern with a parking recommendation. This is Watson's complexity gatekeeper role. Neutral but challenging tone. Richard decides, but Watson surfaces the risk.

### CfC Scepticism

For any CfC-related setup (CfC Clearing in HQC, Trough-on-Trough, Huge CfC Clearing), Watson must apply the scepticism rule: assume the CfC is MORE persistent than it appears. Require hard evidence of clearing. "Transient-looking" CfCs are precisely the ones that catch investors out. Default to scepticism.

### Track Record Integration (ESA onwards)

Per APM SKILL.md non-negotiable: before forming any setup classification or conviction assessment, check track-record-by-stock.md for the stock and for similar stocks by archetype. Cite at least one historical parallel. Use Richard's own journal quotes where applicable.

### False Friend Detection Must Be Robust

The false friend check is not a tick-box exercise. At ESA, Watson should write 2-3 sentences per false friend pattern explaining why the stock does or does not match. The most dangerous false friends are the ones that look most like genuine setups.

---

## Posting and Formatting

### Triaging
- Analysis + Judgement in a single Notion page
- Clearly demarcated sections (Analysis, then Judgement)
- All standard formatting rules from notion-posting-sop.md
- **Bullet structure — default is parent + sub-bullets.** Any bullet with a headline conclusion AND supporting rationale uses parent + sub-bullet format. Flat single bullets only for standalone verdicts. Hard cap: ~100 words per bullet (any level).

### ESA
- **Two separate Notion pages:** Analysis and Judgement
- Judgement page includes context recap for standalone readability
- Each page independently meets all formatting standards (30%+ highlighting, header density, bold density)
- Both pages linked to the same Stock(s) relation
- Judgement page references the Analysis page by title
- **Bullet structure:** Same rule as Triaging — parent + sub-bullet default, ~100 word hard cap.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V1 | 13-Apr-26 | Initial creation. Triaging (combined) + ESA (separate) formats. Meta questions check. ACH sketch at ESA. False friend robust check. Complexity gatekeeper enforcement. Track record integration. |
| V2 | 15-Apr-26 | A/B/C/D/F rating scale replaces G/Y/O/R. Six Pillars framework integration. Database write step added (mandatory post-Notion posting). ICD integration section. |
| V2.1 | 15-Apr-26 | Note added on merged [C+AS] research pages and how APM Judgement should handle analytical disagreements between sources. |
