# UPDATING OLD RESEARCH MEMOS SOP

**Role:** RESEARCHER  
**Version:** 2.1 (06-May-26)  
**Status:** LIVE  
**Model:** Sonnet (recommended) or Opus

---

## Purpose

Take an existing researcher memo (raw markdown source) and **format it for readability** — add HTML structure, section headings, signpost labels, highlights, and split long text into scannable bullets. Deploy to GitHub Pages so it's clickable from the ratings dashboard.

**THIS IS A FORMATTING PASS, NOT A REWRITE.** The source content is preserved using the source's own words. You are adding structure and visual aids, not creating new analytical content.

---

## THE CARDINAL RULES

Read these before doing anything. Every rule below serves these three principles:

**1. DO NOT REWORD.** Use the source's exact words and phrases. If the source says "demand recovery is real but fragile," the output says "demand recovery is real but fragile" — not "cycle is turning" or "recovery remains uncertain." If the source says "catastrophically exposed," the output says "catastrophically exposed." You are formatting, not editing.

**2. DO NOT DROP CONTENT.** Every sentence, fact, number, rating, verdict, and analytical phrase in the source must appear in the output. The output word count must be >= 90% of the source word count. If anything, the output should be LONGER than the source (you're adding signpost labels, section headings, and a Key Findings block).

**3. DO NOT CHANGE THE ANALYTICAL TEMPERATURE.** If the source is bearish, the formatted memo reads bearish. If the source rates something ORANGE-RED, the output contains "ORANGE-RED." If the source says "hold pending evidence," the output says "hold pending evidence." Do not soften, neutralise, or rearrange content to lead with positives when the source verdict is negative.

---

## CRITICAL LESSONS FROM PRIOR FAILURES

1. **CONTENT LOSS + REWORDING (v1.0 disaster):** Watson summarised and reworded instead of formatting. AUTO Q1 BD lost 78% of words. BRAV Q7 KD had its ORANGE-RED verdict removed entirely and the memo reframed as positive. **Root cause:** SOP gave too much licence to "restructure." THIS version limits the task to formatting only.

2. **"FALLING OFF":** Formatting quality degraded in the second half of long memos. **Root cause:** attention drift. **FIX:** signpost consistency check (first half vs second half).

3. **FUSE SILENT TRUNCATION:** Files >28KB may truncate on the COWORK mount. **FIX:** write body HTML to sandbox first, verify byte count, then copy to COWORK.

---

## INPUT: What You Need Before Starting

| Item | Where to find it | Example |
|------|------------------|---------|
| **Source markdown** | `Files/{TICKER}/{STAGE}/{NN-CODE}/` | `Files/DCC/IG/02-CF/DCC-CF-AS-highlighted.md` |
| **Ticker index** | `Files/{TICKER}/index.json` | Gives query name, source, stage, query number |
| **Wrapper script** | `databases/scripts/wrap-memo-html.py` | Adds header, tags, QC footer |
| **CSS stylesheet** | `databases/memos/memo-style-v2.css` | Already deployed to GitHub |

### Source file naming patterns

- `*-highlighted.md` — PREFER this if it exists
- `*-cleaned.md` — next preference
- `raw-AS.md` / `raw-C.md` / `raw.md` — fallback
- If BOTH [AS] and [C] sources exist for the same query, **MERGE them into a single memo**. Include ALL content from both sources. Do not drop anything from either. Rules for merging:
  - Where both sources have an obviously matching section (same topic, similar keywords), combine them into one section. Place the longer source's content first, then append the other source's additional points below
  - Where a section exists in one source but not the other, include it as its own section
  - Tag each bullet with its source using a small suffix: `[AS]` or `[C]` at the end of the bullet text. This is additive (a few characters per bullet)
  - Do NOT try to synthesise, reconcile, or de-duplicate overlapping content. If both sources say similar things in different words, include both — each tagged with its source. Slight redundancy is fine; lost content is not
  - The merged memo's word count floor (90%) applies against the COMBINED word count of both sources

---

## THE 6 STEPS

### Step 1: Load and Count

1. Read the ticker's `Files/{TICKER}/index.json` for metadata (query name, source, stage, query number).
2. Read the source markdown file(s). If both [AS] and [C] sources exist, read BOTH.
3. Count source words (plain text, strip markdown). If merging two sources, count BOTH and sum them. Record this number — you need it at Step 5.
4. Read this SOP again if you haven't already this session. Do not rely on memory.

### Step 2: Plan Sections

Group the source content into H2 sections. This is the ONLY re-ordering you do.

1. **Keep existing sections if the source has them.** If the source already has numbered sections or headings, use those (give them descriptive names if the source uses "Section 1" etc.).
2. **If the source is unstructured prose:** group by analytical dimension. Typical sections: the source's own topic areas. Give each a descriptive name.
3. **When merging [AS] + [C]:** Use the LONGER source's section structure as the backbone. Slot the shorter source's content into matching sections (match by topic/keywords). Any sections from the shorter source that have no match in the longer source go at the end as additional sections.
4. **Identify 5-10 Key Findings** for the BLUF block. These are the most important sentences from the source, pulled out and listed at the top. Use the source's own words for these — do not rephrase. When merging, draw Key Findings from BOTH sources. Tag each with [AS] or [C].
5. **Every sentence in the source(s) must be allocated to a section.** Nothing left behind.

### Step 3: Format as HTML

Convert the source content into HTML. This is where the formatting happens.

**What you ARE doing:**
- Wrapping content in HTML tags with CSS classes
- Splitting long paragraphs/bullets into shorter ones (see splitting rule below)
- Adding signpost labels to bullets
- Adding highlight colours to bullets
- Adding underline emphasis to key phrases
- Bolding key terms on first occurrence
- Adding an italic summary sentence under each H2
- Creating the Key Findings BLUF block (additive — new content drawn from source)
- Replacing em-dashes with colons/commas/parentheses
- Removing trailing periods from bullets

**What you are NOT doing:**
- Rewording any sentence or phrase
- Dropping any content
- Compressing or summarising
- Creating sub-bullet hierarchies
- Adding IAJA tags (#J/#A/#I)
- Synthesising or reconciling content across sources (when merging [AS]+[C], include both — do not blend into new wording)
- Changing the analytical tone or verdict

### THE SPLITTING RULE

**Any bullet point or paragraph that spans more than 2 sentences AND more than 25 words total MUST be split into separate bullet points.** Apply this recursively — a 100-word paragraph becomes ~4 bullets, not 2.

How to split:
- Each sentence becomes its own bullet point
- Each new bullet must also meet the rule (if still > 2 sentences and > 25 words, split again)
- Use the source's exact words — splitting means putting a `</li><li>` between sentences, not rewriting them
- Add a signpost label to each new bullet where appropriate

**Example:**

Source:
```
Revenue grew 12.3% to €4.2bn driven by pricing and volume gains. Organic growth was 8.1% with acquisitions contributing 3.2% and FX a 1.0% headwind. Management upgraded full-year guidance to €4.5bn from €4.3bn, citing stronger-than-expected order intake in Q3.
```

Output (3 bullets, not 1):
```html
<li class="m-parent m-hl-green"><span class="m-signpost">Revenue:</span> Revenue grew <u>12.3% to €4.2bn</u> driven by pricing and volume gains</li>
<li class="m-parent"><span class="m-signpost">Organic growth:</span> Organic growth was <u>8.1%</u> with acquisitions contributing 3.2% and FX a 1.0% headwind</li>
<li class="m-parent m-hl-green"><span class="m-signpost">Guidance:</span> Management upgraded full-year guidance to <u>€4.5bn from €4.3bn</u>, citing stronger-than-expected order intake in Q3</li>
```

Note: the words are identical to the source. Only structure and formatting changed.

### HTML STRUCTURE TEMPLATE

```html
<!-- BLUF — this is ADDITIVE (new block, content drawn from source) -->
<section class="m-bluf">
  <h2 class="m-h2">Key Findings</h2>
  <ul class="m-bluf-list">
    <li class="m-hl-green"><span class="m-signpost">Label:</span> Key finding using <u>source's own words</u></li>
    <!-- 5-10 bullets, drawn from the most important sentences in the source -->
  </ul>
</section>

<!-- Body sections — content from source, formatted -->
<hr class="m-section-hr">
<section class="m-section">
  <h2 class="m-h2">Descriptive Section Name</h2>
  <p class="m-italic-summary"><em>One italic sentence summarising this section's main point.</em></p>
  
  <ul class="m-bullets">
    <li class="m-parent m-hl-green"><span class="m-signpost">Label:</span> Source sentence with <u>key phrase underlined</u></li>
    <li class="m-parent"><span class="m-signpost">Label:</span> Next source sentence with <u>key phrase underlined</u></li>
    <!-- Flat list — NO sub-bullets, NO nesting -->
  </ul>
</section>
```

### FORMATTING RULES CHECKLIST

| # | Rule | Notes |
|---|------|-------|
| F1 | H2 = descriptive section names | Keep source's own section names where they exist |
| F2 | H3 = sub-sections within H2 blocks (optional) | Only if source already has sub-sections |
| F3 | HR between H2 sections | `<hr class="m-section-hr">` |
| F4 | Key Findings BLUF: 5-10 bullets drawn from source | Additive. Use source's own words. |
| F5 | Italic summary under every H2 | One sentence. Can be your own words — it's additive. |
| F6 | Signpost labels on every bullet | `<span class="m-signpost">Label:</span>` |
| F7 | Highlights: green/yellow/red on `<li>` | Green = positive. Yellow = notable/neutral. Red = risk/concern. 30%+ of bullets. |
| F8 | Underline key phrases in bullets | `<u>key phrase</u>`. Target the number, verb, or pivoting phrase. |
| F9 | Bold key terms on first occurrence | Company names, financial figures, key terms. |
| F10 | No em-dashes | Replace with colons, commas, or parentheses. |
| F11 | No trailing periods on bullets | Bullets are fragments. |
| F12 | Split long text per the splitting rule | > 2 sentences AND > 25 words → split into separate bullets. |
| F13 | Flat bullet structure — NO sub-bullets | Every bullet is a `<li class="m-parent">`. No `<ul class="m-sub-bullets">`. |

### CSS CLASSES REFERENCE

| Element | Class(es) |
|---------|-----------|
| BLUF section | `<section class="m-bluf">` |
| BLUF bullet list | `<ul class="m-bluf-list">` |
| Body section | `<section class="m-section">` |
| H2 heading | `<h2 class="m-h2">` |
| H3 heading | `<h3 class="m-h3">` |
| Italic summary | `<p class="m-italic-summary"><em>...</em></p>` |
| Horizontal rule | `<hr class="m-section-hr">` |
| Bullet list | `<ul class="m-bullets">` |
| Bullet | `<li class="m-parent">` (add `m-hl-green/yellow/red` for highlight) |
| Signpost label | `<span class="m-signpost">Label:</span>` |
| Underline | `<u>key phrase</u>` |

### Step 4: Wrap with Header/Footer

Run the wrapper script:

```bash
cd /sessions/*/mnt/COWORK/

python databases/scripts/wrap-memo-html.py \
  /absolute/path/to/body.html \
  /absolute/path/to/output.html \
  --ticker TICKER \
  --stage STAGE \
  --query-name "Query Name" \
  --query-num NN \
  --source SOURCE \
  --date DD-Mon-YY
```

**Post-wrap fix (mandatory):**

```bash
sed -i 's|href="../memo-style-v2.css"|href="memo-style-v2.css"|g' /path/to/output.html
```

**Source flag for merged memos:** If the memo merges [AS] and [C] sources, pass `--source "AS+C"` to the wrapper script.

**Filename convention:** `{TICKER}-{NN}-{CODE}.html` (e.g. `AENA-01-BD.html`, `DCC-02-CF.html`)

### Step 5: VALIDATION GATE (MANDATORY — DO NOT SKIP)

Run the validation script:

```bash
# Single source:
python /sessions/*/mnt/COWORK/databases/scripts/validate-memo.py \
  /path/to/source.md \
  /path/to/body.html \
  /path/to/wrapped.html

# Merged [AS] + [C] sources — pass BOTH source files:
python /sessions/*/mnt/COWORK/databases/scripts/validate-memo.py \
  /path/to/source-AS.md \
  /path/to/source-C.md \
  /path/to/body.html \
  /path/to/wrapped.html
```

The validator sums word counts across all source files. The last two arguments are always body.html and wrapped.html; everything before them is treated as source files. [AS] and [C] source tags in the output are excluded from the word count.

**Hard gates (MUST pass or go back to Step 3):**

| Check | Threshold | Why |
|-------|-----------|-----|
| **Word ratio >= 90%** | Output words / source words >= 0.90 | You are formatting, not compressing. Output should be SAME LENGTH or LONGER. |
| **H2 sections >= 3** | Key Findings + 2+ body sections | Basic structure requirement. |
| **Signpost consistency** | Second half >= 40% of first half density | Catches "falling off" in long memos. |
| **Em-dashes = 0** | Zero `—` or `&mdash;` in content | Clean formatting. |
| **Structure sanity** | DOCTYPE, `</html>`, CSS link, QC footer, `data-ticker` | Valid HTML document. |

**Warning checks (fix if possible, flag for review):**

| Check | Threshold |
|-------|-----------|
| Signpost labels | 80%+ of bullets |
| Highlight density | 25%+ of bullets |
| Underlines | 50%+ of bullets |
| Trailing periods | Should be 0 |

**If the word ratio is below 90%, you have dropped content. Go back to Step 3 and find what you missed.**

### Step 6: Deploy to GitHub Pages

```bash
cd /tmp
rm -rf dashboards_deploy
git clone https://$(cat /sessions/*/mnt/COWORK/.secrets/github-pat.txt)@github.com/vfhqi/dashboards.git dashboards_deploy

cp /path/to/TICKER-NN-CODE.html dashboards_deploy/memos/
cd dashboards_deploy
git add memos/TICKER-NN-CODE.html
git commit -m "Add formatted memo: TICKER NN-CODE (v2.0 SOP)"
git push origin main
```

Save the body HTML to `databases/memos/{TICKER}-{CODE}-body.html` as an intermediate artifact.

---

## BATCH WORKFLOW

1. Read this SOP ONCE at the start of the session
2. For each memo: Steps 1-5, accumulate in the git clone
3. Clone GitHub repo ONCE, deploy all memos in a single commit, push once
4. Present all deployed URLs to Richard at the end

**Batch size:** 3-5 memos per session.
**Commit message:** `Add {N} formatted memos (v2.0 SOP): TICKER1-CODE, TICKER2-CODE, ...`

---

## MEMO MANIFEST INTEGRATION

The dashboard uses `covMemoManifest` to make cells clickable. This SOP focuses on rendering + deploying the memo HTML. Manifest integration is handled by the dashboard update pipeline separately.

---

## QUALITY STANDARDS SUMMARY

| Metric | Target | Hard Floor |
|--------|--------|------------|
| Word ratio (output/source) | >= 100% (formatting adds words) | 90% |
| H2 sections | 4-8 | 3 |
| Signpost labels | Every bullet | 80% |
| Highlight density | 30%+ of bullets | 25% |
| Underlines | Every bullet | 50% of bullets |
| Bullet length | ≤25 words per sentence-bullet | — |
| Em-dashes | 0 | 0 |
| Trailing periods | 0 | 0 |
| Sub-bullet nesting | NONE (flat structure) | NONE |

---

## TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| Word ratio < 90% | Content dropped | Go back to Step 3. Check source sentence by sentence — find what's missing. |
| Word ratio < 50% | Rewrote instead of formatted | Start over. Re-read the Cardinal Rules. Use the source's own words. |
| Signposts drop off in second half | Attention drift | Re-scan second half specifically. |
| Highlights all one colour | Lazy classification | Re-evaluate: green=positive, yellow=notable, red=risk. Mix expected. |
| Source has no clear sections | Unstructured prose | Group by topic yourself. But do not reword the content within sections. |
| File truncated after write | FUSE mount bug | Write to sandbox first, verify size, copy to COWORK. |
| wrap-memo-html.py fails | Relative paths | Always use ABSOLUTE paths. |
| CSS path wrong in wrapped HTML | Wrapper bug | Run the sed fix command in Step 4. |

---

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 05-May-26 | Initial SOP. Content restructure approach with IAJA, sub-bullets, dimension splitting. |
| 2.0 | 06-May-26 | **Major rewrite.** Reduced scope to FORMATTING ONLY. Removed IAJA tags, sub-bullet hierarchy, dimension splitting, judgement surfacing, J→A→I ordering, source attribution tagging, communication principles. Added Cardinal Rules (do not reword, do not drop, do not change temperature). Raised word floor from 35% to 90%. Added splitting rule (>2 sentences + >25 words → split). Flat bullet structure only (no nesting). |
| 2.1 | 06-May-26 | **Pre-mortem fixes (5 issues).** (1) Validator now accepts multiple source files for merged memos — sums word counts. (2) Removed "Merging multiple source files" contradiction from NOT-doing list. (3) Added `--source "AS+C"` guidance for wrapper script on merged memos. (4) Added merge-specific Step 2 rule: longer source = section backbone, shorter source slotted in. (5) BLUF draws from both sources when merging, tagged [AS]/[C]. Also: [AS]/[C] bracket tags excluded from validator output word count. |
