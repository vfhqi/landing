# SKILL — Memo View Formatting

<!-- SOP CITATION REQUIRED — added 28-Apr-26 per CLAUDE.md UWB-3 -->
> **SOP Citation Required.** Per CLAUDE.md Universal Winning Behaviour 3 (SOP CITATION GATE), any proposal involving the workflow described in this file must include an in-turn citation to the specific §X.Y of this file. No citation = proposal not allowed.


**Purpose:** Ensure every memo JSON authored for the MEMO view conforms to the formatting principles agreed 20-Apr-26. This skill is load-bearing — read it **before** authoring or editing ANY memo sub-section.

**Version:** 2.8 (1-May-26 PM) — V13 mini-bump per principles v3.8. Adds §IV.H entry #11 Plain sight risks RA → DOUBLE (no slowing of core engine / no mediocre CEOs / no big Hmmms screen). Joins #7 Lessons check, #8 Negative earnings momentum, #10 Crash through stops as an RA-level double inside G4 Case riskiness. v2.7 (1-May-26 PM) — V12 mini-bump per principles v3.7. (a) §IV.H entry #9 General ACHs ESCALATED double → QUADRUPLE (now Q2 alongside Q1 Sector strength). (b) §IV.J.1 BQ summary-only element reorder added (Row 1 = great operator + value chain + high secular growth; Row 2 = advantaged business + industry structure + paradigm fit). Main pane + nav unchanged. R26b validator added. v2.6 (1-May-26) — adds QUADRUPLE weight tier (4.0×) per principles v3.6 §IV.F. Adds §IV.H entries #9-10 (General ACHs + Crash through stops → DOUBLE), entry N1 (Conservative IR → NORMAL defensive restatement), entry Q1 (Sector strength → QUADRUPLE). Adds §IV.J group summary 2-row layout, §IV.K G5 Optionality 3-column override, §IV.L element summary cols 2-4 only. Adds R26/R27/R28 validator rows. v2.5 (30-Apr-26 PM) — recalibrates DD multiplier from 5× to 3.75× (= ESA × 1.25) per principles v3.5 §IV.G. Narrows §IV.H entry #4: G2 "Case simplicity" group double-weight removed; "Required simplicity guardrails" element only is now double. v2.4 (30-Apr-26 PM) — substantial reform. Adds **weight system + stage scaling 3×/5×** mirroring principles §IV.F-H. Adds R22 (≥25% over floor, SOFT), R23 (per-CQ floor, SOFT), R24 (stage scaling band, SOFT), R25 (weight-tag consistency, SOFT). **Supersedes** v2.x stage-gated-depth (Triaging=TC only) — every CQ is now answered at every stage. v2.3 (30-Apr-26 AM) added R20 (no em-dashes) + R21 (no trailing periods). v2.2 (21-Apr-26 noon) — added signposting doctrine: every parent bullet in C.II must signpost the **Core Question / Required Attribute / Target Condition** it answers; new R15 (signpost present) and R16 (CQ/RA/TC coverage matrix) validator rules; relabel `QUESTIONS → CORE QUESTIONS (CQs)`, `ATTRIBUTES → REQUIRED ATTRIBUTES (RAs)`. v2.1 (20-Apr-26 evening) added bullet-length discipline (R14), R5 raise (3 → 6), per-family floor overrides for IC#1/2/3 and BB#2, and stage-gated anchor count for the flat-shape sub-sections. v2.0 added the C.II two-shape rule and stage-gated depth-of-disclosure; v1.0 (deprecated) over-banned all nesting outside C.I.

**Governing documents:**
- `databases/memo-view-formatting-principles.md` v3.8 — formatting/shape rules + weight system (half/normal/double/quadruple; #11 Plain sight risks added 1-May-26 PM) + stage scaling 3×/3.75× + group summary multi-row + BQ summary-only element reorder + G5 override + element summary cols 2-4 (the operational substance of v2.8).

**Cross-ref to STAGE PROGRESSION SOP (NEW 1-May-26):** This SKILL governs the OUTPUT SPEC for memos authored in Step 2 (APM A&J) of the STAGE PROGRESSION SOP (`memory/skills/stage-progression/SKILL.md`). The memo template here is the canonical render; the APM A&J SOP governs the analytical work that produces it. Both must be cited together when authoring or critiquing a memo.
- `memory/projects/ratings-dashboard/memo-signposting-principles.md` v1.0 — **signposting doctrine** (the operational substance of v2.2). **READ THIS BEFORE AUTHORING ANY C.II CONTENT.**

This skill is the operational extract of both.

**Validator:** `databases/scripts/validate-memo.py` — runs inside `build-memos.py` and fails the build on hard violation. A passing validator is necessary but not sufficient — read this skill too.

**Canonical references:**
- HTRO `databases/memos/HTRO/Triaging.json` Section D — the approved D.I shape (flat `bullet_group`).
- NVTK `databases/memos/NVTK/Triaging.json` Section C.II — the approved C.II two-shape pattern (re-authored 20-Apr-26 PM).

---

## The rule in one paragraph

Most memo sub-sections (D, E, B, A, F, and C.II.1/3/4/5) use the **flat shape**: optional italic BLUF, then one or more `bullet_group` blocks with flat items (`iaja` + `text` + optional 1-level `sub[]`), optional italic SUMMARY. Only **C.II.2** uses the **deep shape**: `pillar_block` containers wrap `family_block` containers wrap one `bullet_group` each — because P3 and P4 carry case trees that need to be mirrored in prose. C.I.1 has its own special block type (`ratings_table`) for the full Pillar→AF→TC→A→Q hierarchy.

---

## Block types

### Permitted anywhere
- `kv_grid` — key/value metadata (e.g., A.I stock header)
- `prose` — short paragraph copy (≤120w per block)
- `bullet_group` — the workhorse block for judgements + evidence
- `callout` — highlighted framing note (use sparingly, ≤60w)
- `bluf` — italic 1-sentence top-of-sub-section judgement frame
- `summary` — italic 1-sentence bottom-of-sub-section restatement

### Permitted ONLY in `C.I`
- `ratings_table` — the 283-row pillar/AF/TC/A/Q table. The ONLY place the full Excel LIST hierarchy is allowed to appear.

### Permitted ONLY in `C.II` (any sub-section)
- `pillar_block` — wraps content for one of the 6 pillars. Carries `pillar_id`, `label`, `rating`, and `blocks`.

### Permitted ONLY in `C.II.2` (deep-shape sub-section)
- `family_block` — wraps content for one of the 11 P3+P4 families (IC#1, IC#2, IC#3, BB#1...BB#8). Carries `badge`, `label`, `rating`, and `blocks`.

### FORBIDDEN everywhere
- `topic` — lifted from Excel LIST view. Do not use.
- `sub_topic` — same.
- `sub_sub_topic` — same.

---

## C.II two-shape rule

C.II is the only sub-section in the entire memo where two shapes legitimately coexist.

### Shape 1 — Flat (P1, P2, P5, P6 — i.e., C.II.1, C.II.3, C.II.4, C.II.5)

```
sub-section
├── bluf (italic prose)
└── pillar_block (one — the pillar itself)
    └── bullet_group
        ├── parent J item (the dimension/paradigm/metric/cut)
        │   └── 0-3 sub items (A/I)
        └── ... (3-10 items, see Miller cap)
```

These pillars carry flat arrays of metrics in the case ratings, not trees. Forcing them into `family_block` containers would create empty container chrome.

### Shape 2 — Deep (P3 + P4, only inside C.II.2)

```
C.II.2
├── bluf (italic prose, sub-section level)
├── pillar_block P3
│   ├── pillar BLUF (italic prose)
│   ├── family_block IC#1
│   │   ├── family BLUF (italic prose, ≤20w)
│   │   └── bullet_group
│   │       ├── family-summary J item (~30-50w)
│   │       ├── TC item J (parent)
│   │       │   └── 0-3 attribute children (A/I)
│   │       └── ... (capped at 7 items including family-summary)
│   ├── family_block IC#2 ...
│   └── family_block IC#3 ...
└── pillar_block P4
    └── family_block BB#1 ... BB#8 (all 8, always)
```

P3 and P4 carry trees (Pillar→Family→TC→Attribute→Question). The C.II.2 prose mirrors them as nested `pillar_block`+`family_block` containers, each holding one `bullet_group`.

### Hard rules

- **All 11 families render at every stage** (3 in P3 + 8 in P4). Triaging carries lighter content per family; DD descends fully.
- **`family_block` is permitted ONLY inside C.II.2.** C.II.1, C.II.3, C.II.4, C.II.5 use one `pillar_block` + one `bullet_group` only.
- **`pillar_block` is permitted ONLY inside C.II.** Never in D, E, A, B, F.
- **Items per `bullet_group` cap is 7 (Miller).** Inside `family_block`, this means 1 family-summary J + up to 6 TC bullets. Overflow collapses into one trailing "Plus N further target conditions covered in C.I.1 ratings table" item.
- **Family floor:** each family carries ≥95w (Triaging) / ≥195w (ESA) / ≥295w (DD). Sparse families (with no/few TCs) are topped up with synthetic family-level bullets, not skipped. The validator emits a soft warning if breached.

---

## Stage-gated depth-of-disclosure

The memo's job is different at each stage. Encode this in the JSON:

| Stage | C.II.2 descent | Per-family content density |
|-------|----------------|----------------------------|
| **Triaging** | Family → TC | Family-summary J + 2-3 TC bullets, no children. ~95w/family. |
| **ESA** | Family → TC → Attribute | Family-summary J + 3-5 TC bullets + 1-2 A/I attribute children per TC. ~195w/family. |
| **DD** | Family → TC → Attribute → Question | Family-summary J + 4-6 TC bullets + 2-3 attribute children + 1-3 question children. ~295w/family. |

The descent is **gated**, not declared. Shallower stages simply don't include the deeper layers.

### Word budgets (locked, v3.1)

| Sub-section | Triaging | ESA | DD |
|---|---|---|---|
| C.II.1 Technical Strength (P1) | 600w | 900w | 900w |
| C.II.2 Fundamental Case (P3+P4) | 2,100w | 4,250w | 7,000w |
| C.II.3 Fit for Paradigm (P2) | 600w | 900w | 1,200w |
| C.II.4 SS Momentum (P5) | 300w | 600w | 600w |
| C.II.5 Upside (P6) | 300w | 300w | 300w |
| **Total C.II** | **3,900w** | **6,950w** | **10,000w** |

C.II.2 was lifted in v3.1 because IC#1/2/3 floors doubled and BB#2 quadrupled (see per-family overrides below).

Green target band: 0.85×–1.15× of target. Out-of-band counts trip a validator warning (not failure).

C.II.1 (P1 Technical) does NOT scale beyond ESA — at 900w the 10 dimensions are fully covered; DD does not add new dimensions, only deeper sub-bullets.

C.II.5 (P6 Upside) is fixed at 300w across all stages. Upside is reported, not re-derived.

---

## `bullet_group` shape (universal)

```json
{
  "type": "bullet_group",
  "items": [
    {
      "iaja": "J",
      "rating": "B",
      "text": "Parent judgement — single sentence, 15-25 words"
    },
    {
      "iaja": "J",
      "rating": "A",
      "text": "Another parent judgement",
      "sub": [
        {"iaja": "A", "rating": "B", "text": "Evidence/analysis child — 10-20 words"},
        {"iaja": "I", "rating": "C", "text": "Context/information child — 10-20 words"}
      ]
    }
  ]
}
```

Rules (v3.1):
- **Items per `bullet_group`:** 1-7 (target 3-6). Never more than 7 (Miller's Law / P6).
- **Parent `iaja`:** `J` is the default. `I`/`A` parents are permitted but rare.
- **Children per parent:** 0-6 (raised from 3 in v2.0). Never more than 6 (still inside Miller).
- **Depth:** Parent + `sub` = two disclosure levels. NO grandchildren. A child's `sub[]` is forbidden.
- **Length (R14):** Parent **15-25w, hard cap 30w**; sub-bullet **10-20w, hard cap 30w**. Longer → split into more sub-bullets, OR add another parent anchor. Never let a single bullet bloat to "absorb" word budget. (See §IV.C of principles doc.)

### Rating prefix convention

Every bullet item carries an inline `rating` field rendered as `[J] B — text...`:
- `[J]` = IAJA tag (purple/green/blue badge)
- `B` = rating badge (A=green, B=blue, C=amber, D=orange, "—"=muted)
- em-dash separator
- bullet text

### Other legal `iaja` tags
- `J` — Judgement (purple #d2a8ff, semi-bold)
- `A` — Analysis / Action (green #7ee787)
- `I` — Information (blue #79c0ff)
- `ACT` — Action item (green, treat as A for layout)
- `OQ` — Open question (purple, shown with `?` marker)
- `KR` — Key risk (red accent)

---

## Sub-section shape (general)

A sub-section is an array of `blocks`:

1. Optional **`bluf`** — 1 sentence, 15-30 words, sets the judgement frame. ONE per sub-section, at the top.
2. **Body blocks** — `bullet_group` (flat shape) OR `pillar_block`+`family_block` (deep shape, C.II.2 only).
3. Optional **`summary`** — 1 sentence, 15-30 words, restates the take-away. ONE per sub-section, at the bottom.

**No** BLUF at the bullet-item level. **No** repeated BLUF at multiple structural levels (the family-level BLUF inside `family_block` is allowed and is NOT the sub-section BLUF).

If you find yourself writing the same judgement twice at two structural levels, you are building `sub_topic` in disguise. Stop and refactor.

---

## Per-family floor overrides (v3.1, C.II.2 only)

Default floor is 95w / 195w / 295w. Three families earn double, one earns quadruple.

| Family | Triaging | ESA | DD | Why the override |
|---|---|---|---|---|
| **IC#1** Required Case Drivers | 190w | 390w | 590w | The IC families ARE the case. |
| **IC#2** Required Case Outputs | 190w | 390w | 590w | The IC families ARE the case. |
| **IC#3** Required Case Setups | 190w | 390w | 590w | The IC families ARE the case. |
| **BB#2** Required Foundation Quality | 380w | 780w | 1,180w | Asymmetric-risk gate. |
| All other BBs (BB#1, BB#3-8) | 95w | 195w | 295w | Default. |

The validator carries these overrides in `FAMILY_FLOOR_OVERRIDES_TRI/ESA/DD` dicts in `validate-memo.py`. Floor breaches are SOFT (R12 warnings), not hard fails — but they signal "needs more thought," not "silence the warning."

---

## Stage-gated anchor count (v3.1, flat-shape sub-sections)

Parallel to stage-gated **depth** (§IV.B principles doc, deep-shape C.II.2), the flat-shape sub-sections flex their **anchor count** with stage. Reason: R14 caps each parent + 6 subs at 145w, so reaching higher word budgets requires more parent anchors, not longer bullets.

| Sub-section | Triaging anchors | ESA anchors | DD anchors |
|---|---|---|---|
| C.II.1 Technical (P1) | 7 dimensions | 7 dimensions | 7 dimensions (constant — depth grows) |
| C.II.3 Paradigm (P2) | 3 paradigms | 5 paradigms | 7 paradigms |
| C.II.4 SS Momentum (P5) | 5 metrics | 5 metrics | 5 metrics (constant — depth grows) |
| C.II.5 Upside (P6) | 3 cuts | 4 cuts | 5 cuts |

Where the anchor list grows, the *additional* anchors are higher-cost-of-acquisition dimensions (e.g., for paradigms: ESA adds energy-security and sanctions; DD adds capital-cycle and FX-regime). They wouldn't earn the time at Triaging.

---

## Signposting doctrine (v2.2 — the load-bearing discipline)

**Higher intent:** Every analytical statement in the memo must be instantly traceable to the **Core Question / Required Attribute / Target Condition** it answers. When Richard reads a bullet, he must know in **<1 second** *why* he is reading it here-and-now. Without signposting, the APM's analytical work is wasted because the surface fails to telegraph the hierarchy to the reader.

**Single source of truth:** `memory/projects/ratings-dashboard/memo-signposting-principles.md`. This section is the operational extract. If any detail below conflicts with the principles doc, the principles doc wins.

### The three-tier analytical hierarchy

Inside each Required Attribute Family (IC#1/IC#2/IC#3 in P3; BB#1–BB#8 in P4), the APM works three tiers:

- **CORE QUESTIONS (CQs)** — bedrock. "Is X / How much is X" form. Mostly Information + Analysis. **ALWAYS answered. ALWAYS signposted.**
- **REQUIRED ATTRIBUTES (RAs)** — "Does the case have sufficient X?" Analysis + Judgement. Often spans multiple CQs.
- **TARGET CONDITIONS (TCs)** — "Does the case meet TC X?" Pass/fail-bent threshold. Analysis + Judgement. Often spans multiple RAs.

Ratings roll up: CQs → RAs → TCs → Family rating → Pillar rating.

### Terminology (locked 21-Apr-26)

| Old term | New term (use this) |
|---|---|
| QUESTIONS | **CORE QUESTIONS** (CQs) |
| ATTRIBUTES | **REQUIRED ATTRIBUTES** (RAs) |
| TARGET CONDITIONS | TARGET CONDITIONS (TCs) — unchanged |
| Attribute Families | **REQUIRED ATTRIBUTE FAMILIES** (IC#1/2/3, BB#1–BB#8) |

### Signposting rules

1. **Every parent bullet in C.II must signpost its CQ/RA/TC** at ESA/DD; strongly preferred at Triaging.
2. **Sub-bullets inherit context** from their parent. Do NOT repeat the parent's signpost. Add a signpost on a sub-bullet only when it cross-references a *different* CQ/RA/TC.
3. **Label form: rich form is default.** `{Family} {Type}{Number} — {Short label}` (e.g. `IC#1 CQ1 — Three-year triple ratchet step-up`). Short form (`IC#1 CQ1`) only for in-line cross-references. Long form only in the C.I.1 ratings table.
4. **Two visual patterns, one per `bullet_group`, no mixing.**
   - **Pattern 1 prefix:** `**IC#2 CQ1 — External change forces / tailwinds:** Russian gas shut-in plus EU REPowerEU creating 4–5% volume tailwind…`
   - **Pattern 2 embedded:** `The Russian gas shut-in is a major **external change force (IC#2 CQ1)**, while EU REPowerEU constitutes an additional tailwind.`
5. **Visual treatment: demi-bold, font-weight 600.** Same colour as body. Above body 400, below structural labels 700. CSS class `.memo-signpost`.
6. **Compound signposts** for synthesis bullets: `**IC#2 TC — Sufficient change forces (synthesises CQ1 + CQ2):** …` (renderer auto-builds the parenthetical from the `synthesises` array).

### JSON schema — bullet item with signpost

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",                 // "cq" | "ra" | "tc"
    "ref": "IC#1.CQ1",             // family.type+number
    "label": "Three-year triple ratchet step-up",
    "style": "prefix",             // "prefix" | "embedded"
    "synthesises": ["IC#1.CQ2"]    // optional, compound only
  },
  "text": "Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path."
}
```

- `signpost` is **omitted** on sub-bullets and on non-C.II content.
- `signpost` is **optional structurally** so un-signposted legacy content continues to render — but the validator enforces coverage per the stage-flexed matrix below.
- For `style: "embedded"`, renderer ignores `label` and uses `**…**` markers from `text`. `level` and `ref` still populate the validator's coverage matrix.

### Stage discipline — coverage matrix (R15 + R16)

| Stage | R15 — signpost on parent bullet | R16 — CQ/RA/TC coverage |
|-------|-------------------------------|-------------------------|
| **Triaging** | Strongly preferred → **warning** if breached | Every CQ referenced → **warning** if breached |
| **ESA** | Required → **hard fail** | Every CQ + every RA + every TC referenced → **hard fail** |
| **DD** | Required → **hard fail** | Every CQ + every RA + every TC referenced → **hard fail** |

Validator source-of-truth for "declared CQ/RA/TC per family" is the per-pillar detail JSONs at `databases/detail/{P1,P2,P3,P4,P5,P6}-detail.json`.

### Signposting anti-patterns

- Writing a bullet **without deciding which CQ/RA/TC it answers**. If you can't name the question, the bullet doesn't exist.
- Using long form outside C.I.1 ratings table. Bloats prose.
- Mixing Pattern 1 and Pattern 2 inside a single `bullet_group`. Breaks reader's scanning rhythm.
- Repeating parent's signpost on every sub-bullet. Sub-bullets inherit — repetition is noise.
- Omitting signpost because "context makes it obvious." Richard's reading mental model is the criterion, not the author's.
- Inventing CQ/RA/TC labels not present in the pillar detail JSONs. Update the detail JSON first.
- Overriding `.memo-signpost` weight. 600 is locked. 400 disappears, 700 competes with structural headings.

### Worked example — Pattern 1 prefix (default)

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
  "text": "Order intake +34% YoY YTD and capex-driven margin trajectory to 12% by 2028 underwrite a credible EPS path from €4.20 (2025e) to €7.80 (2028e) — 3x on earnings in three years consistent with the triple-ratchet setup.",
  "sub": [
    { "iaja": "I", "text": "Order intake €3.2bn YTD vs €2.4bn prior year (+34%)." },
    { "iaja": "I", "text": "Q3-25 EBIT margin 9.8% vs 7.1% prior year; management guiding 11–12% by 2028." },
    { "iaja": "A", "text": "Ratchet mechanic: revenue growth + margin expansion + modest multiple hold → 3x EPS, 2x–2.5x share price." }
  ]
}
```

Sub-bullets inherit `IC#1 CQ1` context; no per-sub signpost.

### Worked example — Pattern 2 embedded (narrative)

```json
{
  "iaja": "A",
  "rating": "B",
  "signpost": {
    "level": "cq",
    "ref": "IC#2.CQ1",
    "style": "embedded"
  },
  "text": "The dominant change vector is supply-side: the Russian gas shut-in has removed ~150 bcm of European supply, and **the REPowerEU response plus US LNG capex (IC#2 CQ1)** is re-plumbing flows to create a 4–5% volume tailwind for NVTK's own LNG exports through 2028."
}
```

---

## Pre-flight checklist (read before every memo authoring task)

1. [ ] Have I read this SKILL file this session?
2. [ ] Am I about to use `topic`, `sub_topic`, or `sub_sub_topic`? → STOP. Use `pillar_block`/`family_block` (C.II only) or `bullet_group`.
3. [ ] Am I about to use `family_block` outside C.II.2? → STOP. R11 violation.
4. [ ] Am I about to use `pillar_block` outside C.II? → STOP. R10 violation.
5. [ ] Is any bullet_group >7 items? → split or cut. R4.
6. [ ] Is any parent carrying >6 children? → split. R5.
7. [ ] Is any child bullet carrying its own `sub[]`? → STOP. Flatten. R3.
8. [ ] **Is any single bullet >30w?** → STOP. Split into more sub-bullets, or add another parent anchor. NEVER lengthen the bullet to absorb word budget. R14.
9. [ ] Am I writing a sparse family below its floor (default 95/195/295w; IC#1-3 doubled; BB#2 quadrupled)? → top it up with synthetic family-level bullets. R12.
10. [ ] Does my flat-shape sub-section have enough parent anchors to hit the word target without fat bullets? See "stage-gated anchor count" above.
11. [ ] **Signposting — every C.II parent bullet:** have I decided which CQ/RA/TC this bullet answers *before* writing the answer? If I can't name the question, the bullet doesn't exist yet. R15.
12. [ ] **Signposting — coverage:** have I touched every active CQ (Triaging+) and every RA+TC (ESA/DD)? Cross-check against the pillar detail JSON at `databases/detail/{Pillar}-detail.json`. R16.
13. [ ] **Signposting — pattern consistency:** does each `bullet_group` use ONE pattern (prefix OR embedded), not mixed? Rule 4.
14. [ ] **Signposting — terminology:** am I using CORE QUESTIONS / REQUIRED ATTRIBUTES (not the old QUESTIONS / ATTRIBUTES)? Lock 21-Apr-26.
15. [ ] **No em-dashes in bullets:** does any bullet `text` contain `—` (em-dash, U+2014)? If yes, replace with `: ` (colon-space). R20. Locked 30-Apr-26.
16. [ ] **No trailing periods on bullets:** does any bullet `text` end in `.`? If yes, strip. `?` and `!` kept. R21. Locked 30-Apr-26.
17. [ ] **Weight tagging (v3.4):** is the item's `weight` (`half` / `normal` / `double`) consistent with §IV.H of principles? Default `normal` if absent. Inherits down the taxonomy. Locked 30-Apr-26.
18. [ ] **Per-CQ floor (v3.4):** does this CQ have at least `target_bullets × stage_multiplier × weight_multiplier` bullets? Triaging normal = 3-5; ESA normal = 9-15; DD normal = 15-25; double-weight scales 2×. R23. Locked 30-Apr-26.
19. [ ] **≥25% over floor (v3.4):** am I hugging the floor everywhere or genuinely writing more where content earns it? R22 (SOFT). Locked 30-Apr-26.
20. [ ] **Stage scaling (v3.5):** if this is ESA or DD, is each CQ scaled by stage_multiplier (1× / 3× / 3.75×)? Note: DD reduced from 5× to 3.75× in v3.5; stage-gated-depth rule SUPERSEDED 30-Apr-26 — every CQ is answered at every stage.
21. [ ] **Quadruple-weight (v3.6):** if I'm authoring under a `quadruple`-weight RA (4.0×), are bullet counts visibly heavier than `double`? ESA × quadruple = 36-60 bullets per CQ (~6-10 anchor groups). Reserved for peer-quality canary RAs. R25b (SOFT).
22. [ ] **Element summary cols 2-4 (v3.6):** is the element summary row leaving col 1 (CQ) empty and spanning cols 2-4 only? colspan=3, not 4. R28 (HARD). Locked 1-May-26.
23. [ ] **Group summary multi-row (v3.6):** for groups with >3 elements (currently BQ only), is the summary rendered as 2 rows × max 3 element columns? R26 (SOFT).
24. [ ] **G5 Optionality 3-column override (v3.6):** is G5 Case Optionality rendering a 3-column group summary (1 general + 2 RA), not skipped per V9 single-element rule? R27 (SOFT).
21. [ ] Will the validator pass? Run `python databases/scripts/validate-memo.py <path>` before baking.

---

## Known anti-patterns (do not reintroduce)

- **Excel LIST taxonomy lifted into prose.** The Excel Pillar→AF→TC→A→Q hierarchy is LEGITIMATE for the ratings table (C.I.1) and for the deep-shape C.II.2 only. Do not replicate it as `topic → sub_topic → bullet`. Use `pillar_block`+`family_block`+`bullet_group` instead.
- **`family_block` in flat-shape sub-sections.** C.II.1/3/4/5 use one `pillar_block` + one `bullet_group`. No families.
- **`pillar_block`/`family_block` outside C.II.** They simply don't exist anywhere else.
- **Per-item chrome.** Do not attach IDs or chips to individual bullets. Chrome belongs to section/sub-section/pillar/family headers only.
- **Grandchild bullets.** A child's `sub[]` is forbidden. R3.
- **10-item bullet_groups.** The Miller bound is 7. R4.
- **Nested BLUFs at the same logical level.** One sub-section BLUF, one pillar BLUF (in C.II.2), one family BLUF (in C.II.2). Don't repeat the same judgement.
- **Skipping sparse families in C.II.2.** All 11 families render at every stage. Top up with synthetic content; don't omit.
- **Fat bullets.** (Added v2.1.) A bullet over 30w is a paragraph in disguise. The failure mode is lazily allocating a sub-section's word target across a fixed parent list and letting per-bullet length blow out. Flex *count* (sub-bullets per parent OR parent anchors), not *length*. R14 catches this; pre-flight #8 prevents it.
- **Un-signposted C.II parent bullets at ESA/DD.** (Added v2.2.) Every parent bullet in C.II at ESA/DD must carry a `signpost` — this is the load-bearing discipline. The author already knows which CQ they're answering; declining to say so imposes that discovery cost on Richard. R15/R16 enforce.
- **Signposting drift.** (Added v2.2.) Inventing CQ/RA/TC labels that don't match `databases/detail/{Pillar}-detail.json`. The detail JSONs are authoritative; update those first if a label needs changing, then update memos.
- **Hollow signposts.** (Added v2.2.) A signpost that doesn't actually match the bullet body. Worse than no signpost — it misleads Richard's scanning. If the bullet answers CQ2 but you labelled it CQ1, fix the label.
- **Em-dashes in bullets.** (Added v2.3, 30-Apr-26.) The `—` separator creates a visual stutter that competes with the SemiBold anchor weight. Use `: ` (colon-space) for verdict→evidence joins. R20 enforces. Em-dashes in signposts and prose outside bullets are still permitted.
- **Trailing periods on bullets.** (Added v2.3, 30-Apr-26.) Bullets are fragments, not sentences. Trailing `.` is visual noise. Strip the last character if `.`. Internal periods kept. `?` and `!` carry tone, kept. R21 enforces.
- **Weight-system ignorance.** (Added v2.4, 30-Apr-26.) Treating every CQ as equal-importance in length and depth. Per §IV.F of principles, items have explicit `weight` attributes (half/normal/double) that propagate DOWN the taxonomy. Watson should consult the weight tag and scale length + analytical depth accordingly, not default to a flat distribution.
- **Stage-skipping CQs.** (Added v2.4, 30-Apr-26.) Following the now-DEPRECATED v3.0/v3.1 stage-gated-depth rule (Triaging = TC-only). Per §IV.G, every CQ is answered at every stage; what scales is per-CQ length (3× ESA / 5× DD). Skipping CQs at Triaging is no longer permitted.
- **Floor-hugging.** (Added v2.4, 30-Apr-26.) Writing exactly the floor on every CQ to satisfy a count check. Per R22, ≥25% of CQs in any memo should be over their floor — driven by content interest, not gaming. Surface the over-spend as a deliberate choice tied to higher intent.

---

## Cross-references

- `memory/projects/ratings-dashboard/memo-signposting-principles.md` v1.0 — **canonical signposting doctrine** (load-bearing; v2.2 substance lives there).
- `memory/projects/ratings-dashboard/signposting-proposal.md` — proposal + 8-step implementation plan.
- `memory/projects/ratings-dashboard/decisions.md` S1–S9 — locked signposting decisions.
- `databases/memo-view-formatting-principles.md` v3.1 — the 10 governing principles + §IV.A two-shape rule + §IV.B stage-gated depth.
- `databases/memos/HTRO/Triaging.json` — flat-shape reference (Section D).
- `databases/memos/NVTK/Triaging.json` — two-shape reference (Section C.II), as of 20-Apr-26 PM.
- `databases/scripts/validate-memo.py` — mechanical enforcement (R15/R16 coverage to be added).
- `databases/scripts/build-cii-mockup.py` — Lorem-Ipsum mockup generator with locked word budgets.
- `databases/detail/{P1…P6}-detail.json` — authoritative CQ/RA/TC labels per family.
- `databases/mockups/nvtk-cii-comparison.html` — 3-stage comparison mockup for visual reference.
- `.auto-memory/feedback_memo_c_ii_formatting.md` — durable memory pointer (v3.1 formatting).
- `.auto-memory/feedback_memo_signposting_doctrine.md` — durable memory pointer (v2.2 signposting).
- `memory/session-handoffs/SA-dashboard-opus47-HANDOFF-20-Apr-26.md` — origin failure.

---

*Skill v2.2 authored 21-Apr-26 noon after Richard's higher-intent brief on memo signposting. Adds signposting doctrine (R15 parent-bullet signpost, R16 CQ/RA/TC coverage matrix), terminology relabel (QUESTIONS→CORE QUESTIONS, ATTRIBUTES→REQUIRED ATTRIBUTES), `signpost` JSON field, two patterns (prefix/embedded), rich-form labels, demi-bold visual treatment. Owner: Richard (investor) / Watson (executor).*

*Skill v2.1 authored 20-Apr-26 evening after fat-bullet bug discovered in C.II.1/3/4/5 mockups. Adds R14 (bullet word cap), R5 raise (3 → 6), per-family floor overrides, stage-gated anchor count.*

*Skill v2.0 authored 20-Apr-26 PM after v1.0 was discovered to have over-codified the wrong rule (banning all C.II nesting).*
