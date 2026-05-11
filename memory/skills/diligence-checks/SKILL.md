# Verification Reference — How to Test Things
<!-- [W] V3 28-Apr-26. Browser Self-Test seven-step detail relocated here from working-preferences.md (R3). -->
<!-- [W] V2 simplified 24-Apr-26. Was "Diligence Checks — Cross-Role Verification Framework" (6 check types, 10 winning behaviours). -->
<!-- This file = how-to reference. Standing orders live in CLAUDE.md (Operating Values + Universal Winning Behaviours). -->

## Core Principle

Verify at the point of no return — before the error becomes costly, not after. Validate outputs, not intentions.

The standing order is **Universal Winning Behaviour 1 (NEXT TOOL CALL)** in CLAUDE.md: every claim of "I have built / posted / verified X" must be accompanied in the same turn by the verification tool call producing the evidence. This file tells you WHICH evidence to gather for which workflow.

---

## How to Test: HTML/JS/CSS Builds (Browser Self-Test)

**This is where Watson has historically failed most.** Syntactic checks (AST parse, brace count, grep for functions) catch malformed code but not broken functionality. The real test: open it in a browser and look at it.

**The seven-step Browser Self-Test (relocated from working-preferences.md, R3):**

1. Push to GitHub Pages (via `push-dashboard.sh` or equivalent) or serve locally
2. Use Claude in Chrome to navigate to the live URL
3. Take a screenshot — verify layout, elements, no visual breaks
4. Read the console — check for JS errors
5. Click key interactive elements — verify they work
6. If anything is wrong, fix and repeat
7. Present to Richard with screenshot evidence

If browser testing is genuinely impossible (sandbox network limits, Chrome unavailable): state this explicitly and provide Richard a numbered test plan — what to open, what to click, what to look for. Never present a build as "done" with only syntactic checks.

**Fallback minimum if browser unavailable:**
- [ ] Every onclick handler references a defined function (grep cross-check)
- [ ] Every variable reference has a corresponding definition (grep for removed vars)
- [ ] colspan sums equal actual column counts (count manually)
- [ ] CSS top/z-index values are in expected ranges
- [ ] No dead code (functions defined but never called)
- [ ] After removing/renaming anything, grep the entire file for remaining references

These catch the class of bugs that have historically reached Richard: dead function calls, stale variable references, misaligned colspans, CSS positioning errors.

---

## How to Test: Browser Interactions (AlphaSense, Forms, UI)

For any critical UI interaction via Chrome:
1. Screenshot before the action, zoom on the target element
2. Verify state programmatically (JS: `aria-pressed`, `classList`, `Mui-selected`) — don't rely on visual alone
3. Screenshot after the action to confirm state change
4. Log the verified state ("aria-pressed=true") — not a claim ("I selected it")

**AlphaSense submission checklist:**
- [ ] Deep Research mode verified via JS
- [ ] Prompt text visible in input field (screenshot)
- [ ] Correct company/ticker in prompt
- [ ] Screenshot captured before pressing Enter
- [ ] After submission: URL changes, progress bar visible, sidebar shows "Deep Research"

---

## How to Test: Sub-Agent Output

When a sub-agent returns work:
1. **Word count:** BD/CF minimum 3,000-4,000 words. Below 50% of expected → don't post, escalate. Below minimum → flag.
2. **Structure:** Grep for expected section headers — are all sections present?
3. **Source integrity:** Does the output reference the correct company, ticker, date?
4. **Match to brief:** Does the output accomplish what RICHARD asked for (not what Watson asked the sub-agent for)?

Watson owns sub-agent output. The sub-agent did the work; Watson checks the work. No exceptions.

---

## How to Test: Notion Postings

Before any create-pages call:
- [ ] H2 count: 8-15 present
- [ ] H3 count: 15-25 present
- [ ] Bold density: financial metrics, analyst names, ratings bolded
- [ ] Highlight coverage: 30%+ at sentence level (not paragraph level)
- [ ] Zero artifact contamination (no source annotations, date stamps, broken spans)
- [ ] Properties: Stock(s) relation set, title format correct, date/case component/source tag correct
- [ ] Content completeness: word count matches source within 90%

After posting: fetch the page and verify content is present and correctly formatted.

---

## How to Test: Data Pipelines

When data moves through stages (extract → clean → highlight → chunk → post):
- Track character/word count at each stage
- Cleaning should retain 85-100% of source
- Highlighting adds span tags (count increases)
- Chunks should sum to total ± 5%
- Posted word count should match source within 20% — investigate any larger gap

---

## When to Escalate

If verification fails twice on the same issue, or if Watson has been grinding on a problem for 10+ minutes without progress: stop and flag it to Richard. He often has practical shortcuts Watson wouldn't think of.

---

## Cross-References

- **CLAUDE.md** — Operating Values + Universal Winning Behaviours (the standing orders this file supports)
- **working-preferences.md** — Proactive Execution gates, Model protocol, Daily rhythm
- **CLAUDE.md UWB-3 (SOP CITATION GATE)** — for any proposal touching an SOP-governed workflow, cite the specific SOP §X.Y in-turn. Failure to cite = proposal not allowed.
