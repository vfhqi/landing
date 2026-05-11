# Memo Signposting — Proposal & Decisions
<!-- [W] Created 21-Apr-26. Captures Richard's higher-intent brief on memo signposting and the agreed implementation plan. -->

## Higher intent (Richard's brief, 21-Apr-26)

The memo's job is to make every analytical statement instantly traceable to the **Core Question / Required Attribute / Target Condition** it answers. Richard reads a bullet and must know, in under a second, *why* he is reading it here-and-now.

This is structural. Not cosmetic. The memo is the surface where the APM's analytical hierarchy meets Richard's reading mental model — if the surface fails to telegraph the hierarchy, the analytical work behind it is wasted.

## Two-layer architecture (re-affirmed)

The memo works toward understanding two layers, both essential:

**Layer 1 — The fundamental investment case (Pillar III).**
The 3× "change AFs": positive change inputs (IC#2), setup pattern match (IC#3), translating to financial outputs (IC#1). Magnitude and direction of change.

**Layer 2 — Bankability of the case (Pillar IV).**
Eight families of building blocks (BB#1–BB#8). Probability, durability, robustness, predictability — is the case trustworthy.

Both alongside: **I Technical Momentum**, **II Market Paradigm Fit**, **V SS Earnings Momentum**, **VI Valuation**.

Richard's stated priority order: **A** technical momentum, **B** market/environment fit, **C** investment case (P3), **D** investment case predictability/quality (P4).

## Terminology change (locked)

| Old name | New name | Notes |
|---|---|---|
| QUESTIONS | **CORE QUESTIONS** (CQs) | Bedrock. "Is X" / "How much is X." Mostly Information + Analysis, narrow scope per question. ALWAYS answered, ALWAYS signposted. |
| ATTRIBUTES | **REQUIRED ATTRIBUTES** (RAs) | "Does the case have sufficient X?" Analysis + Judgement, often spans multiple CQs and references other RAs/TCs. |
| TARGET CONDITIONS | **TARGET CONDITIONS** (TCs) | Unchanged. "Does the case meet TC X?" Analysis + Judgement, often spans multiple RAs and CQs. |
| ATTRIBUTE FAMILIES | **REQUIRED ATTRIBUTE FAMILIES** | Unchanged in shape (IC#1/IC#2/IC#3/BB#1–BB#8). Slightly redundant naming acknowledged but accepted. |

This relabel sweeps across: APM SKILL, RESEARCHER SKILL, FCS SKILL, memo formatting SKILL, the 6 pillar detail JSONs in `databases/detail/`, the C.I.1 ratings table, the validator, the dashboard column headers, RESEARCHER query templates, and any project decision/spec docs that mention the old terms.

## Stage discipline (re-affirmed for memo)

| Stage | APM minimum requirement |
|---|---|
| **Triaging** | High-level analysis on every CQ in every active family. Write it down. Rate A–F. Then attempt RA + TC analysis to whatever extent possible at this depth. Rate. |
| **ESA** | Ingest *all* RESEARCHER ESA-phase output. Re-run every CQ + every RA + every TC analysis and judgement. More content, higher resolution. Coverage = exhaustive at ESA depth. |
| **DD** | Same as ESA but on DD-phase RESEARCHER output. Maximum depth. Coverage = exhaustive at DD depth. Cross-references between CQs/RAs/TCs expected and welcomed. |

The depth is gated by stage; the coverage is not. Skipping a CQ at Triaging is allowed only if the analysis would be vapid; skipping at ESA/DD is a defect.

## Signposting SOP (locked)

### Where signposts go

- **Parent bullet (top level of `bullet_group.items`):** signpost is mandatory at ESA/DD, strongly preferred at Triaging.
- **Sub-bullets (`item.sub[]`):** signposts NOT required. They inherit context from their parent. Adding a signpost to a sub-bullet is permitted only when it cross-references a different CQ/RA/TC than the parent.

### Two patterns (both legitimate; one per sub-section, no mixing within a single `bullet_group`)

**Pattern 1 — Prefix.** Signpost label leads, em-dash separator, then the answer.

> **IC#2 CQ1 — External change forces / tailwinds:** Russian gas shut-in plus EU REPowerEU plus US LNG capex creating 4–5% volume tailwind through 2028.

**Pattern 2 — Embedded.** Label appears inline within the answer text.

> The Russian gas shut-in is a major **external change force (IC#2 CQ1)**, while EU REPowerEU and US LNG capex constitute additional tailwinds.

### Label form (Q1 answered: rich form)

Rich form is the default for parent bullets:

> **`{Family}.{Type}{Number}` — `{Short label}`**
> e.g. `IC#1 CQ1 — Three-year triple ratchet step-up`
> e.g. `IC#2 RA — Sufficient change forces`
> e.g. `BB#2 TC1 — Strong company (internal)`

Short form (`IC#1 CQ1`) is permitted only for in-line cross-references inside the body of another bullet.

Long form (`Required Case Outputs CQ1: Three-year triple ratchet step-up`) appears only in the C.I.1 ratings table.

### Visual treatment (Q2 answered: demi-bold = font-weight 600)

- Signpost label rendered in **demi-bold (font-weight: 600)**, same colour as body text.
- Sits above body 400 in visual weight, below the 700 used for structural labels (pillar/family titles).
- Read order on a parent bullet: `[J] B — IC#1 CQ1 — Three-year triple ratchet step-up: Order intake +34% YoY...`
  (IAJA tag → rating badge → em-dash → signpost label demi-bold → signpost short label demi-bold → colon → body text 400)
- For pattern 2 (embedded), bold-marked spans inside the bullet text. Author writes `**…**` markdown markers; renderer converts to `<span class="memo-signpost">…</span>`.

### Compound signposts

Where a single bullet's judgement integrates multiple CQs (typical of an RA-level or TC-level synthesis), the signpost can compound:

> **IC#2 TC — Sufficient change forces (synthesises CQ1 + CQ2):** External tailwinds plus internal capex acceleration both present, jointly satisfying the change-forces threshold at B.

## JSON schema (locked)

Bullet items gain an optional `signpost` field:

```json
{
  "iaja": "J",
  "rating": "B",
  "signpost": {
    "level": "cq",                 // "cq" | "ra" | "tc"
    "ref": "IC#1.CQ1",             // family.type+number
    "label": "Three-year triple ratchet step-up",
    "style": "prefix",             // "prefix" | "embedded"
    "synthesises": ["IC#1.CQ2"]    // optional, for compound signposts
  },
  "text": "Order intake +34% YoY and margin trajectory to 2028 underwrite a credible triple-ratchet EPS path."
}
```

`signpost` is omitted for sub-bullets and for non-C.II content where signposting doesn't apply (kv_grid, prose, callout, bluf, summary).

For embedded pattern, the renderer ignores `label` and uses `**…**` markers in `text` instead. `level` and `ref` still carry the structural data (drives validator coverage tracking).

## Stage-flexed coverage requirement (locked)

The validator (R16, new) enforces:

| Stage | Coverage rule | Enforcement |
|---|---|---|
| **Triaging** | Every CQ in every active family is referenced by at least one parent bullet's signpost | **Warning** if breached |
| **ESA** | Every CQ + every RA + every TC in every active family is referenced | **Hard fail** if breached |
| **DD** | Same as ESA, with the additional rule that no parent bullet exists *without* a signpost | **Hard fail** if breached |

This sounds heavy but most C.II.2 work already covers most CQs implicitly — the fail mode is omission, not over-asking.

## Implementation plan (priority order)

| # | Step | File(s) touched | State |
|---|------|-----------------|-------|
| 1 | Save proposal + decisions doc, auto-memory note | this file, decisions.md, auto-memory | in progress |
| 2 | Write `memo-signposting-principles.md` (canonical) | new file at project root | pending |
| 3 | Update `memo-view-formatting/SKILL.md` to v2.2 | the SKILL file | pending |
| 4 | Update APM `SKILL.md` with Signposting Doctrine | APM SKILL | pending |
| 5 | Patch dashboard CSS+JS for `.memo-signpost` rendering | `databases/scripts/patch-signpost-renderer.py` (new) | pending |
| 6 | Global relabel: QUESTIONS→CORE QUESTIONS, ATTRIBUTES→REQUIRED ATTRIBUTES | SOPs, pillar JSONs, validator | pending |
| 7 | Author NVTK C.II.2 IC#1 with signposts (proof-of-concept) | `NVTK/Triaging.json`, ESA, DD | pending |
| 8 | Extend `validate-memo.py` with R15 + R16 coverage matrix | validator + per-pillar JSON inputs | pending |

Step 8 (validator) intentionally last — we don't want to fail-build existing un-signposted memos until the SOP has had time to bed in.

## Why this matters

The memo is the operational surface of the entire investment system. Richard's judgement quality depends on the speed and clarity with which he can move from "here is a bullet" to "this answers Core Question X about Required Attribute Y in the IC#2 family of Pillar III." If that traversal costs even three seconds per bullet, a 7,500-word DD memo costs an hour of cognitive overhead before any actual judgement happens.

Signposting transfers that traversal cost from Richard (the reader, expensive) to the APM (the author, cheap, and the entity that already knows the answer because it just chose which CQ to address).

It also creates structural data that future tooling can exploit — coverage matrices, cross-stock CQ comparisons, "show me every IC#2 CQ3 across the portfolio" queries.

## Cross-references

- `decisions.md` — locked decisions S1–S5
- `memo-signposting-principles.md` — canonical principles (to be written)
- `memo-view-formatting/SKILL.md` — operational extract (to be updated to v2.2)
- `assistant-portfolio-manager/SKILL.md` — APM doctrine (to be updated)
- `databases/scripts/validate-memo.py` — mechanical enforcement (R15, R16 to be added)
- `databases/scripts/patch-signpost-renderer.py` — CSS+JS patcher (to be written)
