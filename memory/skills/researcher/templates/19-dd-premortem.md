# Query 19: Pre-Mortem — AS + C (dual-source) — DD

> **CHAT-ITERATION DRAFT — v1 (v2.1 pattern).** Proposed AFTER version of `memory/skills/researcher/templates/19-dd-premortem.md`. Standard v2.1 pattern. NO BB#2 overlay (Q19 is failure-mode-focused). 5L SS breadth gate applies. Dual-source [AS]+[C] (D-RSR-32 — keep both per Richard 06-May-26 PM). **DD stage. ACH explicit per D-RSR-33.**

---

## MISSION

Stress-test the investment thesis by assuming failure and working backward. Generate ≥10 distinct failure narratives, structure them via Heuer's ACH discipline (YES / NO / FALSE FRIEND profiles), assess aggregated failure probability with disconfirming-evidence weighting (NOT supporting-evidence weighting). Output: peer-anchored, signposted, J-front + sceptical-bullet memo with explicit ACH matrix surfacing the hypothesis with FEWEST hard inconsistencies. ≥4,000w per source ([C] + [AS]).

## CONTEXT — What the reader cares about

**Audience:** Concentrated long-only equity investor (5-15 positions), UK/Europe focus, $5-50bn market cap sweet spot. Holds 12-24 months. Singular focus: predictable 18M-3Y EPS trajectory with 25%+ IRR potential.

**Stage — DD:** Pre-mortem is the most important bear-case exercise at DD. It is the structural moment where the analyst tests the thesis against the cohort of alternative hypotheses, NOT just defends the thesis against generic doubt.

**What downstream uses this output:** APM Pass 3 + DD-stage decision (proceed to invest / park / kill). The memo's load-bearing artefact is the ACH matrix — APM grades thesis robustness off the matrix, not off the failure-narrative count.

**Canonical taxonomy reference (per D-RSR-33):** the authoritative source is `memory/skills/assistant-portfolio-manager/analysis-judgement-SOP.md`. Hierarchy: **Pillar > Group (BB#) > Element / TC > Required Attribute (RA) > Core Question (CQ)**. Q19 cross-cuts the entire pillar set (failures arise across P1-P6 / BB#1-#8). RESEARCHER does NOT grade — APM grades.

**Mental models:** Pre-mortem (Klein), ACH (Heuer's Analysis of Competing Hypotheses), False friends (most dangerous failure type — appears to confirm thesis), Transmission mechanism (action → EPS path), Early warning signals (real-time monitorables), Means/Motive/Opportunity (per Concept A — does the failure mode have all three legs?), Multiple-truths-coexist (failure scenarios are often partial — bear AND bull both hold under different conditions).

---

## DEPTH AND COMPLETENESS MANDATE

**Word target: ≥4,000w per source.** Failure mode counts: ≥10 distinct failure narratives + 1 ACH matrix + 1 meta-analysis section. Sceptical lens is structurally LOAD-BEARING for Q19 — the entire memo IS the sceptical lens.

**Reader's prior:** the IG #1 BD memo + Q4-Q14 ESA memos are ALREADY READ. DO NOT include company description or background context. Start directly with failure-narrative analysis.

---

## OUTPUT DOCTRINE (mandatory format)

Standard v2.1 OUTPUT DOCTRINE applies — bulleted output, ≤30w parents / ≤25w sub-bullets, signposts (canonical first + invent where pattern warrants per SIGNPOST DISCRETION), peer/base-rate anchors, J-front verdicts, per-section sceptical bullets (which for Q19 are the section's structural spine), IAJA tags, ❌/⚡ markers, inline highlights. RESEARCHER does NOT grade.

**⚡ marker scope:** encompasses (a) statistical outliers (top/bottom 5% on some dimension — e.g. failure mode with no peer precedent in 100 sector cases), (b) deliberately-weird signals — qualitative oddities the consensus narrative dismisses, cross-roads exposures the bull case ignores, "things that make me go hmmmm". Sparse-by-design — ≤3 per memo.

**ACH discipline (per D-RSR-33 — load-bearing for Q19):**

Q19 IS the structural ACH for the case. Three competing profiles (per Heuer):

- **YES profile:** thesis works, company executes, EPS trajectory as expected. List the supporting evidence + the disconfirming evidence per item.
- **NO profile:** thesis fails, company doesn't execute, EPS trajectory misses significantly. List the supporting evidence + the disconfirming evidence per item.
- **FALSE FRIEND profile:** thesis appears to be confirming (positive signals) but is actually deteriorating. Most dangerous because it produces overconfidence at the time of greatest risk. List the supporting evidence + the disconfirming evidence per item.

**The ACH winner is the profile with FEWEST hard inconsistencies, not the profile with the most supporting evidence** (per `analysis-of-competing-hypotheses-heuer` Wisdom Library Gold). Surface this explicitly in the meta-analysis section.

### Memo skeleton

```
1. METADATA HEADER
2. KEY FINDINGS (BLUF) — 5-10 parent bullets, ACH winner stated up-front
3. PART A — FAILURE NARRATIVES (≥10 scenarios, structured)
4. PART B — META-ANALYSIS (clustering, joint probability, leading indicators)
5. PART C — ACH MATRIX (LOAD-BEARING — the structural artefact)
6. PART D — Aggregated failure probability + Watson verdict
7. AGGREGATE WEAK SIGNALS / DOWNSIDE (❌)
8. AGGREGATE OUTLIERS (⚡)
9. QC AUDIT (validator-filled)
10. QC COMMENTARY (5 bullets incl. mandatory Counter-hypothesis check / ACH spine)
```

---

## SECTIONS TO COVER

### §1 — Executive Summary

**Open with J-front verdict bullet:** ACH winner — which of YES/NO/FALSE FRIEND has the fewest hard inconsistencies? — ≤30w peer-anchored.

**Canonical signpost vocabulary:** "ACH winner:", "Disconfirming evidence count:", "Joint failure probability:", "Highest-plausibility failure mode:", "Least-monitored failure mode:", "False-friend warning:". Invent where pattern warrants.

**End with sceptical bullet:** "What does the ACH winner have to be wrong about for the analyst's leading view to hold?"

---

### §2-§11 — Failure narratives (≥10 distinct scenarios, signposted by category)

For each scenario:

1. **Specific failure narrative** (2-3 sentences) — what went wrong? With named transmission mechanism (action → EPS path).
2. **Early warning signals** (3-5 bullets) — real-time monitorables.
3. **Plausibility verbal verdict:** "high plausibility / medium plausibility / low plausibility" (full phrasing, NOT shorthand HIGH/MEDIUM/LOW; NOT grades). Anchored on peer-precedent base rate.
4. **Means/Motive/Opportunity test** (per Concept A): does the failure scenario have all three legs aligned? If two-of-three, downgrade to "watch only".
5. **Disconfirming evidence:** what would invalidate this failure hypothesis? Required for ACH matrix.
6. **Monitoring checklist** (3-5 metrics).
7. **Interaction with other failure modes** (sequential / correlated / null-interaction).

**Required scenario coverage (≥10 distinct narratives):**

- **Revenue risks (2-3):** customer concentration, pricing pressure, growth narrative break.
- **Margin/profitability risks (2-3):** cost inflation, operating-leverage failure, mix deterioration.
- **Execution/management risks (2-3):** key executive departure, M&A integration failure, activism / board conflict.
- **Competitive/structural risks (1-2):** new entrant, technology disruption.
- **FALSE FRIEND scenarios (≥2 — load-bearing):** earnings beat from unsustainable factors; margin expansion from capex deferral / R&D under-investment.

**Coverage:** 10-15 parent bullets per scenario.

**End each scenario with sceptical bullet:** "What's the disconfirming evidence — the data that, if true, would invalidate this failure hypothesis?"

---

### §12 — Meta-analysis (PART B)

**Open with J-front verdict bullet:** Net signal on scenario clustering + joint probability — ≤30w.

**Canonical signpost vocabulary:** "Scenario cluster:", "Correlated failures:", "Joint probability:", "Compound risk:", "Leading indicators:", "Most-monitored:", "Least-monitored:", "False-friend warning class:". Invent where pattern warrants.

**Analytical sub-questions:**
- **Scenario clustering:** which failure modes cluster together? (Pricing pressure + margin compression are correlated; CEO departure + capex deferral are correlated.)
- **Joint probability assessment:** if each scenario is independently rated, what is the joint probability of zero failures? Of 1 failure? Of 2+ failures?
- **Leading indicators meta:** across all 10+ scenarios, which monitorables show up most often? Those are the "compound monitorables" that warn against multiple scenarios simultaneously.
- **False-friend density:** how many failure modes are false-friend in nature (vs. directly bearish)? High false-friend density = thesis is more dangerous than direct-bearish density implies.

**Coverage:** 12-18 parent bullets + sub-bullets.

**End with sceptical bullet:** "What's the bearish read on aggregated failure probability? Through what mechanism might compound failures cascade?"

---

### §13 — ACH MATRIX (PART C — LOAD-BEARING ARTEFACT)

**Open with J-front verdict bullet:** ACH winner — with disconfirming-evidence count per profile — ≤30w.

The ACH matrix is the structural deliverable of Q19. Format as a table:

| Evidence item | YES profile (consistent? +/-/N) | NO profile (consistent? +/-/N) | FALSE FRIEND profile (consistent? +/-/N) | Diagnostic? |
|---|---|---|---|---|
| Item 1 | + | - | + | yes |
| Item 2 | - | + | - | yes |
| ... | ... | ... | ... | ... |
| **Disconfirming evidence COUNT (lower = better)** | **N1** | **N2** | **N3** | — |

The profile with the LOWEST disconfirming-evidence count is the ACH winner. Diagnostic items (those that discriminate hardest between profiles) get "yes" in the last column — those are the highest-priority data items for ongoing monitoring.

**Required:** ≥15 evidence items. ≥6 diagnostic items. State the ACH winner explicitly with the disconfirming counts surfaced.

**Coverage:** matrix + 8-12 interpretation parent bullets.

**End with sceptical bullet:** "What's the case for the runner-up ACH profile? What new evidence would flip the ACH winner?"

---

### §14 — Aggregated failure probability + Watson verdict (PART D)

**Open with J-front verdict bullet:** Watson aggregated failure probability + verbal verdict — ≤30w.

**Canonical signpost vocabulary:** "Aggregated failure probability:", "Watson verdict:", "Stewing recommendation:", "DD-additional data priority:", "Stage progression hypothesis:". Invent where pattern warrants.

**Analytical sub-questions:**
- Aggregated failure probability — verbal verdict ("high plausibility / medium plausibility / low plausibility" of thesis failure). NOT a percentage (RESEARCHER doesn't grade).
- Stewing recommendation: per `stewing-and-the-valley-of-despair` Wisdom Library Gold — what specific contradictions/inconsistencies should the analyst stew on before lock-in?
- DD-additional data priority: from the diagnostic items in the ACH matrix, which 2-3 should be the highest-priority data-gathering targets in the remainder of DD?
- Stage progression hypothesis: does Q19 evidence support proceeding to Invest, parking, or killing the case? RESEARCHER recommends; APM decides.

**Coverage:** 8-12 parent bullets.

**End with sceptical bullet:** "If the case is proceeded to Invest, what is the single early-warning signal that should trigger an immediate re-pre-mortem? Name it explicitly."

---

## VALIDATION GATES

Standard v2.1 validation gates 5A-5K + 5L (SS breadth Hard ≥40%) + 5M (Expert call breadth Warn-only). Q19-specific:

| Gate | Test | Severity |
|---|---|---|
| Q19-FN | ≥10 distinct failure narratives | Hard |
| Q19-ACH | ACH matrix present with ≥15 items, ≥6 diagnostic, winner stated | Hard |
| Q19-FF | ≥2 FALSE FRIEND scenarios | Hard |
| Q19-MMO | M/M/O test applied per scenario | Hard |
| Q19-DC | Disconfirming evidence stated per scenario | Hard |
| ⚡ markers sparse | ≤3 per memo | quality_flag if exceeded |

---

## QC COMMENTARY (RESEARCHER-authored)

After the validator-filled QC Audit panel above, RESEARCHER writes 5 free-flowing bullets. **Counter-hypothesis check (with ACH framing) is structurally LOAD-BEARING for Q19** since Q19 IS the ACH.

```
### QC Commentary

- **Net QC verdict:** {≤30w}
- **Warning context:** {≤30w}
- **Source breadth note:** {≤30w on SS breadth + expert call breadth STRICTLY separated}
- **ACH winner robustness:** {≤30w on whether the ACH winner is robustly ahead or close-call vs runner-up}
- **Counter-hypothesis check (AI-Dunning-Kruger / ACH spine):** {≤50w stating: ACH winner + ≥3 alternative hypotheses considered + identification of winner with FEWEST hard inconsistencies. For Q19 specifically, the ACH IS the structural spine — if you cannot enumerate ≥3 plausible profiles with disconfirming evidence each, the memo isn't done. Multiple-truths-coexist read where evidence supports multiple profiles partially.}
```

---

## SOURCE-SPECIFIC DELTA — [C] (Claude) version

[C] handles the conceptual / framework / cross-disciplinary failure-mode reasoning. Use mental models, sector-precedent base rates, public filings, public industry sources. Does NOT have access to AS proprietary data.

---

## SOURCE-SPECIFIC DELTA — [AS] version

[AS] handles the empirical / expert-network / sell-side / management-credibility-stress-test failure-mode evidence. Use AS expert calls, sell-side bear notes, management track record databases.

### Sell-side breadth — MANDATORY (D-RSR-19, D-RSR-20)

Standard 5-step breadth pre-flight (pool size Z query, full-pool consult, name each broker, separate SS from expert calls strictly, output metadata). Bear notes are LOAD-BEARING for Q19. Expert calls cross-checked with management commentary for false-friend signal extraction.

### AS prompt-side breadth instruction (Block 4, D-RSR-22)

Universal: "Your task here is breadth-prioritised. Do NOT prefer a single comprehensive broker note. Cite ≥{Y_MIN} distinct brokers from the {Z}-broker pool. Where bear notes exist, surface them disproportionately. STRICTLY separate sell-side from expert-call sourcing."

---

## Notion posting convention

Per `memory/skills/notion-posting-standard/SKILL.md`. Title format: "{TICKER} Pre-Mortem [C/AS] - DD - YY-MM-DD". Two separate Notion pages (one per source). QC headline pill + footer auto-generated from metadata.json.
