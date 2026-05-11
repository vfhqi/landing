# Memo Signposting — Canonical Principles
<!-- [W] Created 21-Apr-26. Load-bearing reference document.
     Single source of truth for memo signposting rules.
     All SKILLs, validators, renderers, and downstream docs must reference this. -->

**Status:** v1.0 — locked 21-Apr-26
**Owner:** Richard Black (substance) · Watson/SA (maintenance)
**Supersedes:** nothing (new document)
**Downstream dependencies:**
- `memory/skills/memo-view-formatting/SKILL.md` v2.2 (operational extract)
- `memory/skills/assistant-portfolio-manager/SKILL.md` (Signposting Doctrine subsection)
- `memory/skills/researcher/SKILL.md` (CQ/RA/TC output conventions)
- `databases/scripts/validate-memo.py` (R15, R16 coverage rules)
- `databases/scripts/build-memos.py` + dashboard JS renderer (signpost field emission)
- Pillar detail JSONs at `databases/detail/*.json` (CQ/RA/TC labels & rich forms)

---

## 1. Higher Intent — the North Star

The memo is the operational surface of Richard's investment system. When Richard reads a bullet, he must know in **under one second**:

> "This bullet answers **which Core Question / Required Attribute / Target Condition**, under **which Required Attribute Family**, inside **which Pillar**."

If that traversal takes three seconds per bullet, a 7,500-word DD memo costs an hour of cognitive overhead before any actual judgement work begins. Signposting transfers that traversal cost from Richard (expensive reader) to the APM (cheap author who already knows which question the bullet addresses — because the APM just chose to write it).

**Without signposting, the APM's analytical work is wasted** — the surface fails to telegraph the analytical hierarchy, and Richard's reading mental model cannot lock onto the APM's thinking. This is not cosmetic. This is structural.

Secondary benefit: signposts create **machine-readable structural data**. Future tooling can build coverage matrices, run cross-stock CQ comparisons, query "show me every IC#2 CQ3 across the portfolio," and validate that every stage has exhausted its required coverage.

---

## 2. Two-Layer Fundamental Architecture

The memo's analytical engine works toward understanding **two layers**, both essential, neither sufficient.

### Layer 1 — WHAT'S CHANGING (Pillar III)

The **three change-oriented Required Attribute Families**. The memo must show that something significant is changing, in a direction that matters, at a magnitude that matters, on a timescale that matters.

| Family | Full name | Question it answers |
|--------|-----------|---------------------|
| **IC#2** | Required Case Inputs | What are the positive change forces driving the case? (tailwinds, capex cycles, structural shifts) |
| **IC#3** | Required Case Setups | Does the setup pattern-match something we've seen work before? (EPT, EPSU, SDC, NG, etc.) |
| **IC#1** | Required Case Outputs | How do those inputs translate into financial outputs? (revenue, margins, EPS, FCF — the "numbers we can bank") |

### Layer 2 — HOW BANKABLE (Pillar IV)

The **eight Building Block families**. The memo must show that the case described in Layer 1 is *trustworthy* — that the probability of it playing out is high enough, that it is durable and robust, that its outputs are predictable.

BB#1 through BB#8 each answer a distinct "how bankable" question (company strength, market structure, management, financial profile, balance sheet, ownership, cash returns, external validators — full detail in APM SKILL §Pillar IV).

### Supporting Pillars

Layers 1+2 are the centre of gravity, but four supporting pillars frame them:

- **I — Technical Momentum:** price/volume confirming the case
- **II — Market Paradigm Fit:** the case survives macro/regime fit
- **V — Sell-Side Earnings Momentum:** the consensus is catching up (leading indicator)
- **VI — Valuation:** upside is available at current price

### Richard's Priority Order (when time is short)

When Richard triages, he looks in this order:

**A** technical momentum → **B** market/paradigm fit → **C** P3 (WHAT'S CHANGING) → **D** P4 (HOW BANKABLE)

This ordering is stored in the APM SKILL as operational doctrine. Signposting applies to all pillars but the highest-stakes signposting work is in C.II.2 (P3+P4) where the analytical density is highest.

---

## 3. Three-Tier Analytical Hierarchy (inside each Required Attribute Family)

Inside every Required Attribute Family (IC#1, IC#2, IC#3, BB#1…BB#8), the APM works through three tiers:

```
REQUIRED ATTRIBUTE FAMILY (A–F rating)
  └─ CORE QUESTIONS (CQ1, CQ2, CQ3…) — A–F rating each
       │ The bedrock. "Is X / How much is X" form.
       │ Mostly Information + Analysis. Narrow scope per question.
       │ ALWAYS answered. ALWAYS signposted.
       │
  └─ REQUIRED ATTRIBUTES (RA1, RA2…) — A–F rating each
       │ "Does the case have sufficient X?" form.
       │ Analysis + Judgement. Often spans multiple CQs.
       │
  └─ TARGET CONDITIONS (TC1, TC2…) — A–F rating each
       │ "Does the case meet TC X?" form.
       │ Analysis + Judgement. Often spans multiple RAs and CQs.
       │ Pass/fail-bent — a threshold to clear.
```

**Ratings roll up:** CQs inform RAs inform TCs inform the Family rating inform the Pillar rating. Every tier has an A–F grade.

**CORE QUESTIONS are the bedrock.** They are the smallest, most specific, most factual units of analysis. Every memo, at every stage, must answer every active CQ. Skipping a CQ is a **defect**, not a style choice. (Exception: at Triaging, skipping a CQ whose answer would be vapid at that depth is permitted — but it must be consciously skipped, not forgotten.)

### Terminology (locked 21-Apr-26)

| Old term | New term | Abbreviation |
|---|---|---|
| QUESTIONS | **CORE QUESTIONS** | CQs |
| ATTRIBUTES | **REQUIRED ATTRIBUTES** | RAs |
| TARGET CONDITIONS | TARGET CONDITIONS (unchanged) | TCs |
| Attribute Families | **REQUIRED ATTRIBUTE FAMILIES** | IC#1/2/3, BB#1–BB#8 |

The "Required" prefix is deliberate and slightly redundant — it signals that these are *non-optional* questions the case must answer to pass.

### Why this hierarchy matters for signposting

Signposting exposes this hierarchy to the reader. A bullet labelled `IC#1 CQ1 — Three-year triple ratchet step-up` tells Richard instantly:

- **Which pillar:** P3 (IC#1 is a P3 family)
- **Which layer:** Layer 1 (WHAT'S CHANGING)
- **Which family:** IC#1 (Required Case Outputs — financial outputs)
- **Which tier:** CQ (bedrock factual analysis)
- **Which question:** CQ1 (the first, usually the most load-bearing)
- **What the question asks:** three-year triple-ratchet step-up in earnings

Without the signpost, Richard reads six sentences of prose and has to reverse-engineer all of the above from context.

---

## 4. Stage Discipline (Triaging / ESA / DD)

The **depth** of analysis is gated by stage. The **coverage** of CQs/RAs/TCs is exhaustive at every stage.

| Stage | APM minimum requirement | Coverage rule |
|-------|-------------------------|---------------|
| **Triaging** | High-level analysis on every CQ in every active family. Write it down. Rate A–F. Then attempt RA + TC analysis to whatever extent possible at this depth. Rate. | Every CQ must be referenced (warning if breached). RAs/TCs strongly preferred. |
| **ESA** | Ingest *all* RESEARCHER ESA-phase output. Re-run every CQ + every RA + every TC analysis. Higher resolution, more content, firmer judgements. | Every CQ + every RA + every TC must be referenced (hard fail). |
| **DD** | Same as ESA on DD-phase RESEARCHER output. Maximum depth. Cross-references between CQs/RAs/TCs expected. | Same as ESA, plus every parent bullet in C.II must carry a signpost (hard fail). |

**Depth scales with stage. Coverage is exhaustive at every stage.**

Skipping a CQ at Triaging is allowed only if the analysis would be vapid. Skipping at ESA or DD is a defect that the validator rejects.

---

## 5. Signposting SOP

### 5.1 Where signposts go

- **Parent bullet** (top-level item in `bullet_group.items`): **signpost is mandatory** at ESA and DD. **Strongly preferred** at Triaging.
- **Sub-bullet** (`item.sub[]`): sub-bullets **inherit** their parent's signpost context. Do NOT repeat the parent's signpost on sub-bullets. Add a signpost on a sub-bullet **only when it cross-references a different CQ/RA/TC** than the parent.
- **Non-C.II content** (BLUF callouts, kv_grids, summaries, prose blocks in A/B/D/E/F): signposting does not apply.
- **C.I.1 ratings table:** long-form CQ/RA/TC labels appear as table rows (not signposts). This is the only place the "long form" is used.

### 5.2 Two patterns (both legitimate; **one pattern per `bullet_group`, no mixing inside a single group**)

**Pattern 1 — Prefix.** Signpost label leads, em-dash separator, then the answer.

> **IC#2 CQ1 — External change forces / tailwinds:** Russian gas shut-in plus EU REPowerEU plus US LNG capex creating 4–5% volume tailwind through 2028.

**Pattern 2 — Embedded.** The label appears inline within the answer text, using bold markers.

> The Russian gas shut-in is a major **external change force (IC#2 CQ1)**, while EU REPowerEU and US LNG capex constitute additional tailwinds.

**Choosing between them:** Pattern 1 is the default. It maximises scanability and is the right choice when the bullet *is* the answer to the CQ. Pattern 2 is better when the bullet is a narrative/argument whose structure is better preserved inline than chopped with a prefix — common in synthesis bullets and some RA-level bullets.

**Rule:** a single `bullet_group` (i.e. one family or one topic) uses one pattern. Don't mix prefix and embedded within a single group — it looks inconsistent.

### 5.3 Label form — **rich form is the default**

Parent bullets use **rich form**:

> **`{Family} {Type}{Number}` — `{Short label}`**

Examples:

| Example | Notes |
|---|---|
| `IC#1 CQ1 — Three-year triple ratchet step-up` | CQ-level, P3/IC#1 |
| `IC#2 CQ3 — Management capex commitment` | CQ-level, P3/IC#2 |
| `IC#2 RA — Sufficient change forces` | RA-level synthesis across IC#2's CQs |
| `BB#2 TC1 — Strong company (internal)` | TC-level, P4/BB#2 |
| `IC#3 CQ2 — EPT pattern match` | CQ-level, P3/IC#3 |

**Short form** (e.g. `IC#1 CQ1`) is permitted **only as an in-line cross-reference** inside the body of another bullet. Example:

> Margins lift to 12% by 2028 ties directly to the capex cycle signposted under IC#2 CQ3.

**Long form** (e.g. `Required Case Outputs CQ1: Three-year triple ratchet step-up`) is used **only in the C.I.1 ratings table**. Nowhere else.

### 5.4 Visual treatment

The signpost label is rendered in:

- **Font-weight: 600 (demi-bold)**
- **Same colour as body text** (no hue change)
- CSS class: `.memo-signpost`

This places the signpost **above body 400 in visual weight, below structural labels 700** (pillar titles, family titles, section headings). The eye reads body text first at 400, sees the bold 600 callout clearly, and still treats the structural headings as dominant.

Read order on a parent bullet (Pattern 1):

```
[J] B — IC#1 CQ1 — Three-year triple ratchet step-up: Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path.
 │   │      │                                      │   │
 IAJA rating  signpost (family+type+number)         │   body text (font-weight 400)
 tag  badge   — short label                         body-text colon
                     (all of this: font-weight 600)
```

### 5.5 Compound signposts

When a single bullet's judgement integrates multiple CQs — typical of an RA-level or TC-level synthesis — the signpost compounds:

> **IC#2 TC — Sufficient change forces (synthesises CQ1 + CQ2):** External tailwinds plus internal capex acceleration both present, jointly satisfying the change-forces threshold at B.

In the JSON schema this is represented as:

```json
{
  "signpost": {
    "level": "tc",
    "ref": "IC#2.TC",
    "label": "Sufficient change forces",
    "synthesises": ["IC#2.CQ1", "IC#2.CQ2"],
    "style": "prefix"
  }
}
```

The renderer auto-builds the `(synthesises CQ1 + CQ2)` parenthetical from the `synthesises` array.

---

## 6. JSON Schema (locked)

Bullet items in memo JSON gain an **optional** `signpost` field:

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#1.CQ1",
    "label": "Three-year triple ratchet step-up",
    "style": "prefix",
    "synthesises": ["IC#1.CQ2"]
  },
  "text": "Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path."
}
```

### Field reference

| Field | Type | Required | Values | Notes |
|---|---|---|---|---|
| `level` | string | yes | `cq` · `ra` · `tc` | Which tier of the hierarchy this bullet addresses |
| `ref` | string | yes | `{Family}.{Type}{Number}` e.g. `IC#1.CQ1`, `BB#2.TC1`, `IC#2.RA` | Machine-readable anchor. No number on RA if only one RA in family. |
| `label` | string | yes (prefix) / optional (embedded) | Short descriptive label | Rendered after em-dash in prefix form. Ignored in embedded form (renderer reads `**…**` markers from `text` instead). |
| `style` | string | yes | `prefix` · `embedded` | Which of the two patterns. Must match the pattern of the containing `bullet_group`. |
| `synthesises` | array of strings | optional | e.g. `["IC#1.CQ1", "IC#1.CQ2"]` | Compound signposts only. Renderer auto-builds the `(synthesises …)` parenthetical. |

### Where `signpost` is **omitted**

- Sub-bullets (inherit from parent)
- Non-C.II content: `kv_grid`, `prose`, `callout`, `bluf`, `summary`, table rows in C.I.1, header/metadata blocks
- Family/pillar/section header items (these already carry structural labels at 700 weight)

### Validator consumption

`level` and `ref` always carry structural data even when the rendered output is embedded (and `label` is ignored). The validator uses `(level, ref)` pairs to build a **coverage matrix** per stage — verifying that every active CQ/RA/TC in every active family is represented by at least one signposted parent bullet.

### Renderer behaviour

**Prefix (style="prefix"):**

```html
<li>
  <span class="iaja-tag">J</span>
  <span class="rating-badge rating-b">B</span>
  —
  <span class="memo-signpost">IC#1 CQ1 — Three-year triple ratchet step-up:</span>
  <span class="memo-body">Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path.</span>
</li>
```

**Embedded (style="embedded"):**

Renderer takes `text` field, converts `**…**` markdown markers to `<span class="memo-signpost">…</span>`, then emits:

```html
<li>
  <span class="iaja-tag">J</span>
  <span class="rating-badge rating-b">B</span>
  —
  <span class="memo-body">
    The Russian gas shut-in is a major
    <span class="memo-signpost">external change force (IC#2 CQ1)</span>,
    while EU REPowerEU and US LNG capex constitute additional tailwinds.
  </span>
</li>
```

### Backward compatibility

Bullets **without** a `signpost` field continue to render as-is (no signpost span). This allows incremental adoption — existing Lorem-Ipsum or un-signposted legacy content continues to render, while the validator flags coverage gaps at the appropriate severity for the stage.

---

## 7. Coverage Matrix (R15, R16 — new validator rules)

### R15 — Parent bullets in C.II must carry signposts (stage-flexed)

| Stage | Requirement | Violation severity |
|---|---|---|
| Triaging | Strongly preferred | Warning |
| ESA | Required | Hard fail |
| DD | Required | Hard fail |

R15 applies **only to C.II** (C.II.1 through C.II.5) parent bullets. It does not apply to A, B, D, E, F sections, nor to sub-bullets, nor to non-bullet content.

### R16 — CQ/RA/TC coverage matrix (stage-flexed)

For each active Required Attribute Family (i.e. each family that has content in the current memo), the validator checks that every declared CQ/RA/TC is referenced by at least one parent bullet's `signpost.ref`.

| Stage | Coverage requirement | Violation severity |
|---|---|---|
| Triaging | Every CQ in every active family | Warning |
| ESA | Every CQ + every RA + every TC | Hard fail |
| DD | Every CQ + every RA + every TC | Hard fail |

**Source of truth for "declared CQ/RA/TC":** the per-pillar detail JSONs at `databases/detail/{P1,P2,P3,P4,P5,P6}-detail.json`. These files enumerate every family's CQs, RAs, TCs (with rich-form labels). The validator reads them to build the expected coverage set, then compares against the signposts present in the memo JSON.

### Why stage-flexed

The validator intentionally **warns** rather than fails at Triaging. Triaging is the stage where the APM is still forming views — the cost of a hard fail there would push the APM toward over-hedged boilerplate. ESA and DD, by contrast, are where coverage must be exhaustive; the stakes justify a hard fail.

---

## 8. Anti-Patterns — do not do these

| Anti-pattern | Why it's wrong |
|---|---|
| Writing a bullet without deciding which CQ/RA/TC it answers | If you can't name the question, the bullet doesn't exist. Every parent bullet answers a specific, namable question. |
| Using long form (`Required Case Outputs CQ1: Three-year triple ratchet step-up`) outside the C.I.1 ratings table | Long form is for tabular contexts only. In prose it bloats the signpost. |
| Mixing Pattern 1 prefix and Pattern 2 embedded within a single `bullet_group` | One pattern per group. Mixing looks inconsistent and breaks the reader's scanning rhythm. |
| Repeating the parent's signpost on every sub-bullet | Sub-bullets inherit. Repetition is noise. |
| Omitting the signpost because "the context makes it obvious" | Richard's reading mental model is the criterion, not the author's. If the author has to explain why the signpost is unnecessary, the signpost is necessary. |
| Inventing new CQ/RA/TC labels that don't match the pillar detail JSON | The labels in the detail JSONs are authoritative. If a label needs changing, change the detail JSON first (and run the relabel sweep), then update memos. |
| Using a different visual weight than 600 for `.memo-signpost` | 400 blends into body. 700 competes with structural headings. 600 is the sweet spot. Do not override. |
| Signposting on BLUF, kv_grid, prose, or non-C.II bullet content | Signposting is a C.II discipline. Other registers have their own conventions. |
| Letting Triaging content skip "awkward" CQs silently | If a CQ is genuinely vapid at Triaging depth, write one sentence acknowledging that. Silent omission looks identical to oversight. |

---

## 9. Worked examples

### 9.1 Pattern 1 prefix — CQ-level (most common)

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#1.CQ1",
    "label": "Three-year triple ratchet step-up",
    "style": "prefix"
  },
  "text": "Order intake +34% YoY YTD and capex-driven margin trajectory to 12% by 2028 underwrite a credible EPS path from €4.20 (2025e) to €7.80 (2028e) — a 3x on earnings in three years consistent with the triple-ratchet setup."
}
```

Rendered:
> [J] **B** — **IC#1 CQ1 — Three-year triple ratchet step-up:** Order intake +34% YoY YTD and capex-driven margin trajectory to 12% by 2028 underwrite a credible EPS path from €4.20 (2025e) to €7.80 (2028e) — a 3x on earnings in three years consistent with the triple-ratchet setup.

### 9.2 Pattern 2 embedded — narrative bullet

```json
{
  "iaja": "A",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#2.CQ1",
    "style": "embedded"
  },
  "text": "The dominant change vector is supply-side: the Russian gas shut-in has removed ~150 bcm of European supply, and **the REPowerEU response plus US LNG capex (IC#2 CQ1)** is re-plumbing flows in a way that creates a 4–5% volume tailwind for NVTK's own LNG exports through 2028."
}
```

Rendered:
> [A] **B** — The dominant change vector is supply-side: the Russian gas shut-in has removed ~150 bcm of European supply, and **the REPowerEU response plus US LNG capex (IC#2 CQ1)** is re-plumbing flows in a way that creates a 4–5% volume tailwind for NVTK's own LNG exports through 2028.

### 9.3 Compound signpost — TC-level synthesis

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "tc",
    "ref": "IC#2.TC",
    "label": "Sufficient change forces",
    "synthesises": ["IC#2.CQ1", "IC#2.CQ2"],
    "style": "prefix"
  },
  "text": "External tailwinds (REPowerEU + LNG demand pull) plus internal capex acceleration (Arctic LNG-2 train 3 commissioning 1H27) are both present at sufficient magnitude to clear the threshold — TC passes at B."
}
```

Rendered:
> [J] **B** — **IC#2 TC — Sufficient change forces (synthesises CQ1 + CQ2):** External tailwinds (REPowerEU + LNG demand pull) plus internal capex acceleration (Arctic LNG-2 train 3 commissioning 1H27) are both present at sufficient magnitude to clear the threshold — TC passes at B.

### 9.4 Sub-bullets inherit — no signpost needed

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#1.CQ1",
    "label": "Three-year triple ratchet step-up",
    "style": "prefix"
  },
  "text": "Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path.",
  "sub": [
    { "iaja": "I", "text": "Order intake €3.2bn YTD vs €2.4bn prior year (+34%)." },
    { "iaja": "I", "text": "Q3-25 EBIT margin 9.8% vs 7.1% prior year; management guiding 11–12% by 2028." },
    { "iaja": "A", "text": "Ratchet mechanic: revenue growth + margin expansion + modest multiple hold → 3x EPS, 2x–2.5x share price." }
  ]
}
```

All three sub-bullets inherit the `IC#1 CQ1` context. No signposts on sub-bullets.

### 9.5 Cross-reference in body text — short form allowed

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#1.CQ2",
    "label": "Margin resilience through cycle",
    "style": "prefix"
  },
  "text": "Even under a -10% volume stress the capex backlog flagged in IC#2 CQ3 holds the margin floor above 8%, keeping the EPS ratchet (IC#1 CQ1) intact."
}
```

Here the parent signpost is `IC#1 CQ2`. Two in-line cross-refs (short form): `IC#2 CQ3` and `IC#1 CQ1`. Neither of those cross-refs creates a signposting obligation — they are just narrative pointers for the reader.

---

## 10. Implementation Plan (from `signposting-proposal.md`)

For the operational sequencing, see `signposting-proposal.md` §Implementation plan. The canonical rules in *this* document are the substance; the proposal captures the *ordering* of how we roll them into SKILLs, renderer, validator, and live content. Summary:

| # | Step | Reference |
|---|------|-----------|
| 1 | Save proposal + decisions + auto-memory | ✅ done 21-Apr-26 |
| 2 | Write this canonical principles doc | ✅ in progress (you are here) |
| 3 | Imprint signposting SOP into `memo-view-formatting/SKILL.md` v2.2 | pending |
| 4 | Imprint signposting doctrine into APM `SKILL.md` | pending |
| 5 | Patch dashboard CSS+JS renderer for `.memo-signpost` | pending |
| 6 | Global relabel QUESTIONS→CORE QUESTIONS, ATTRIBUTES→REQUIRED ATTRIBUTES | pending |
| 7 | Author NVTK C.II.2 IC#1 signposted (proof-of-concept) | pending |
| 8 | Extend `validate-memo.py` with R15 + R16 | pending |

Step 8 last: we don't want to hard-fail existing un-signposted memos before the SOP has bedded in.

---

## 11. Why This Matters (the load-bearing reason)

Richard's judgement quality is a function of **how quickly and cleanly he can traverse from "here is a bullet" to "this answers Core Question X about Required Attribute Y in the IC#2 family of Pillar III."**

If that traversal costs:

- **0.5 seconds per bullet** → signposting is working. The memo is a tool.
- **3 seconds per bullet** → the memo is a puzzle. At ~250 bullets in a DD memo that is ~12 minutes of puzzle-solving before any judgement. Over a year of DD memos that is hours.
- **5+ seconds per bullet** → the memo is actively obscuring the APM's thinking. Richard will either skim (missing signal) or abandon (wasting the APM's work entirely).

Signposting also creates **structural data** — machine-readable `(level, ref)` tuples that let future tooling build coverage dashboards, cross-stock comparisons, and CQ-by-CQ audit trails. Every signpost is simultaneously a human affordance and a machine hook.

Finally, signposting is a **forcing function on the author**. The APM cannot write a signpost it doesn't believe in. Writing `IC#1 CQ1 — Three-year triple ratchet step-up:` forces the APM to confront: *is this really about CQ1? Is it really about a three-year step-up? Have I actually answered it?* The label is a commitment device. Loose thinking cannot survive rigorous signposting.

---

## 12. Change Log

| Date | Version | Change |
|---|---|---|
| 21-Apr-26 | 1.0 | Document created from Richard's higher-intent brief. Locks terminology relabel, two-layer architecture, three-tier hierarchy, stage discipline, signposting SOP (two patterns), rich form labels, demi-bold visual, JSON schema, R15/R16 coverage, anti-patterns. |

---

## 13. Cross-references

- `signposting-proposal.md` — proposal + 8-step implementation plan
- `decisions.md` S1–S9 — locked decisions underpinning this doc
- `memo-view-formatting/SKILL.md` v2.2 (pending) — operational extract
- `assistant-portfolio-manager/SKILL.md` (pending) — APM doctrine integration
- `databases/detail/*-detail.json` — authoritative CQ/RA/TC labels
- `databases/scripts/validate-memo.py` (pending R15/R16) — mechanical enforcement
- `databases/scripts/patch-signpost-renderer.py` (pending) — CSS+JS patcher
- `.auto-memory/feedback_memo_signposting_doctrine.md` — cross-session doctrine note
