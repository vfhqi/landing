#!/usr/bin/env python3
"""
generate_qc_audit.py - Investment Analyst A&J memo Quality Control Audit generator.

Counterpart to the RESEARCHER role's generate_qc_footer.py. Produces section 7
of the A&J memo self-review debrief file: a structured, machine-checkable
compliance audit table PLUS an auto-generated plain-English narrative
explaining it.

Governing SOP: memory/skills/investment-analyst/aj-memo/05-IA-EXECUTION-DISCIPLINE.md section 6

WHY THIS IS A SCRIPT, NOT IA SELF-REPORT
----------------------------------------
A self-written completion flag can lie. An Investment Analyst that has just
spent hours on a memo is the worst-placed party to audit it objectively. This
script reads the actual bytes on disk and counts what is actually there. The IA
cannot argue with the word count.

USAGE
-----
    python3 generate_qc_audit.py --memo <memo.md> --stage <triaging|esa|dd> \
        --meta <metadata.json> [--out <section7.md>]

  --memo   path to the memo markdown file
  --stage  one of: triaging | esa | dd  (also accepts: early-stage-assessment, deep-dive)
  --meta   path to the JSON sidecar metadata block (see METADATA SCHEMA below)
  --out    optional output path for the section 7 block; if omitted, prints to stdout

EXIT CODE
---------
  0  audit clean of HARD FAILs   -> Phase 4 may proceed
  1  one or more HARD FAILs      -> gate: fix the memo and re-run
  2  usage / input error

RENDER-QC GATE (added 2026-06-15)
---------------------------------
Unless --render-qc off is passed, this script also triggers the Station-3
Render + Visual QC gate (render_qc_gate.py, same directory): it builds the
memo's real repository viewer and renders it headless, and a broken/blank/
unrenderable viewer becomes a HARD FAIL row here. This reconciles the
SOP-vs-script divergence (SOP 05 section 6 demanded a visual HARD gate; the
script never enforced one), so an unattended run can no longer ship a
visually-broken memo. The Writer's intermediate floor-QC fix iterations may
pass --render-qc off for speed; the FINAL pre-publish audit and every
unattended run leave it ON (the default).

METADATA SCHEMA (the JSON sidecar the IA assembles during the memo)
-------------------------------------------------------------------
{
  "ticker": "EKTA.B-SE",
  "stage": "triaging",
  "memo_date": "2026-05-14",
  "debrief_filename": "ekta-triaging-self-review-debrief-2026-05-14.md",
  "research_reports": [
      {"family": "Change Forces", "kind": "family", "source": "AS",
       "date": "2026-05-30", "identity_confirmed": true},
      {"family": "Business Foundation", "kind": "family", "source": "AS",
       "date": "2026-05-30", "identity_confirmed": true},
      {"name": "pricing-power-vs-two-largest-peers", "kind": "ia-initiated",
       "source": "C/AS", "date": "2026-06-01"}
  ],
  "wisdom_library_models": [
      {"name": "false-friends", "shaped_judgement": true},
      {"name": "operator-validation-horizon", "shaped_judgement": true}
  ],
  "self_initiated_queries": [
      {"type": "Q21", "gap": "E1 RA2 - leverage figure", "dual_source": true,
       "report": "EKTA-Triaging-IA-initiated-net-debt-ebitda-reconciliation-2026-05-14.md"}
  ],
  "midflight_consults": [
      {"what": "Q4-gate threshold scope", "richard_response": "Proceed - we are aligned."}
  ],
  "validator": {
      "ran": true,
      "gates": [
          {"name": "signpost-label coverage", "result": "PASS"},
          {"name": "bullet-nesting depth", "result": "PASS"}
      ]
  },
  "go_no_go": {"present": true, "paired": true, "question_count": 8},
  "data_discrepancies": [
      "Net debt/EBITDA: ~3.0x (one [C] report) vs ~1.3-1.5x (other sources)"
  ],
  "render_target_supports_sentiment": true
}

Any metadata key may be omitted; the script degrades gracefully and records the
gap in the "Known limitations" row rather than crashing.

SYNC DISCIPLINE
---------------
FLOORS are now loaded at runtime from memo-floors-v1.json (same directory as
this script), which is the SINGLE SOURCE OF TRUTH for all floor numbers.
The hardcoded tables below are fallback defaults only and should stay in sync
with the JSON. To change a floor: edit memo-floors-v1.json only.
Phase-A hardening 2026-06-14. ESA/DD per-RA enforcement added 2026-06-02.
DD floors: present in memo-floors-v1.json and the hardcoded fallback below; synced with 02-THINKING Procedure 3 (Session 21, 16-Jun-26).
"""

import argparse
import os
import json
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# FLOORS TABLE  -  mirror of 02-THINKING-SOP.md. KEEP IN SYNC.
# --------------------------------------------------------------------------
# Whole-memo word floors (exclude Section A and Section F).
WHOLE_MEMO_WORD_FLOOR = {
    "triaging": 9000,
    "esa": 21000,
    "dd": 28000,
}

# Per-section word floors that the Thinking SOP states explicitly.
# Sections without an explicit floor are reported informational-only.
SECTION_WORD_FLOOR = {
    "triaging": {"B": 700, "E": 850},
    "esa": {"B": 1400, "E": 1000},
    "dd": {"B": 2000, "E": 1400},
}

# Per-Element word floors the Thinking SOP states explicitly (Triaging only -
# ESA/DD give element bullet multipliers but not explicit per-element word
# floors, so those are reported informational-only at ESA/DD).
ELEMENT_WORD_FLOOR = {
    "triaging": {"E1": 1200, "E5": 1400, "E7": 1300, "E8": 3500, "E11": 1600},
    "esa": {},
    "dd": {},
}

# Per-Element minimum bullet floors (per RA / per CQ), AFTER multipliers.
# Triaging: E1 x2 -> 6, E5 x2 -> 6, E7 x2 -> 6, E8 carve-out -> 3, E11 light -> 4.
ELEMENT_BULLET_FLOOR = {
    "triaging": {"E1": 6, "E5": 6, "E7": 6, "E8": 3, "E11": 4},
    # ESA/DD floors populated 2026-06-02 (D-IA-4RR refinement R1) from the
    # 02-THINKING-SOP Procedure 2/3 floors, post-multiplier, per RA and per CQ.
    # These are the BASE per-RA/CQ floors; RA-specific overrides (E12 RA1 x4,
    # E15 RA1 x4 / RA2 x2) live in RA_FLOOR_OVERRIDE below. For the two carve-out
    # Elements (E8, E10) the base is the lower "others" floor; the elevated
    # fit-setup / material-CQ floor is reported INFO because the script cannot
    # know which setups/CQs the IA elected to deepen (KNOWN LIMITATION).
    "esa": {"E1": 8, "E2": 6, "E3": 3, "E4": 4, "E5": 10, "E7": 8, "E8": 3,
            "E9": 3, "E10": 3, "E11": 4, "E12": 3, "E13": 3,
            "E18": 3, "E19": 3, "E20": 3},
    "dd": {"E1": 10, "E2": 8, "E3": 4, "E5": 10, "E6": 3, "E7": 10, "E8": 3,
           "E9": 4, "E10": 3, "E11": 4, "E12": 3, "E13": 4, "E15": 3,
           "E16": 3, "E17": 3, "E18": 4, "E19": 4, "E20": 4},
}

# RA-specific bullet floor overrides (the quadruple/double weighted RAs). Applied
# to the RA summary AND each Core Question inside that RA. Source: 02-THINKING-SOP.
RA_FLOOR_OVERRIDE = {
    "esa": {"E12": {"RA1": 12}},
    "dd": {"E12": {"RA1": 16}, "E15": {"RA1": 12, "RA2": 6}},
}

# Carve-out Elements: only 1-2 setups (E8) or 6-10 Core Questions (E10) deepen to
# the elevated floor; the rest stay at the base. The script enforces the base on
# every RA and reports the elevated expectation as INFO (it cannot identify which
# units the IA elected to deepen). The IA self-checks the elevated units.
CARVE_OUT_ELEVATED = {
    "esa": {"E8": 4, "E10": 6},
    "dd": {"E8": 5, "E10": 8},
}

# Which Elements should be substantively present at each stage (scope check).
# Triaging in-scope: E1, E5, E7, E8, E11. Everything else must be explicitly
# marked "not applicable at this stage".
IN_SCOPE_ELEMENTS = {
    "triaging": ["E1", "E5", "E7", "E8", "E11"],
    "esa": ["E1", "E2", "E3", "E4", "E5", "E7", "E8", "E9", "E10",
            "E11", "E12", "E13", "E18", "E19", "E20"],
    "dd": ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10",
           "E11", "E12", "E13", "E15", "E16", "E17", "E18", "E19", "E20"],
}

# Section D presence by stage: zero at Triaging, light at ESA, solid at DD.
SECTION_D_EXPECTED = {"triaging": "zero", "esa": "light", "dd": "solid"}

# Banned phrases (Communicating SOP Guideline 13 + 16). Lower-cased substring match.
BANNED_PHRASES = [
    "synergies", "ecosystem", "unlock value", "holistic approach",
    "double-down", "low-hanging fruit", "leverage value",
    "it could be argued", "may potentially", "in some respects",
    "a neutral fact", "neutral fact worth knowing", "to be honest",
    "in fairness", "interesting to note that", "as an ai",
    "i'd be happy to", "i appreciate you",
]

STAGE_ALIASES = {
    "triaging": "triaging", "triage": "triaging",
    "esa": "esa", "early-stage-assessment": "esa", "early stage assessment": "esa",
    "dd": "dd", "deep-dive": "dd", "deep dive": "dd",
}

STAGE_LABEL = {"triaging": "Triaging", "esa": "Early-Stage Assessment", "dd": "Deep Dive"}

# Verdict constants.
PASS = "PASS"
HARD = "HARD FAIL"
SOFT = "SOFT FLAG"
INFO = "INFO"

# Format reform v2 emphasis BANDS (D-AJ-24 floors; D-AJ-29 caps added 2026-06-17).
# All measured over body BULLET text only (Sections B-E). Units differ: underline
# is % of WORDS; highlight + italic are % of BULLETS.
UNDERLINE_FLOOR_PCT = 0.15    # >=15% of bullet words underlined (__text__)
UNDERLINE_CAP_PCT   = 0.25    # <=25% of bullet words underlined (D-AJ-29 hard cap)
HIGHLIGHT_FLOOR_PCT = 0.30    # >=30% of bullets carry a ==sentiment== highlight
HIGHLIGHT_CAP_PCT   = 0.40    # <=40% of bullets highlighted (D-AJ-29 hard cap)
ITALIC_FLOOR_PCT    = 0.15    # >=15% of bullets carry an italic span (*text*) (D-AJ-29: was 20%)
ITALIC_CAP_PCT      = 0.25    # <=25% of bullets italicised (D-AJ-29 hard cap)

# A section/element within ~THIN_MARGIN of its floor passes but earns a soft flag.
THIN_MARGIN = 0.10


# --------------------------------------------------------------------------
# Single-source floors JSON loader (Phase A, 2026-06-14)
# --------------------------------------------------------------------------
def _load_floors_json():
    """Load memo-floors-v1.json from the same directory as this script and
    override the hardcoded floor tables at module load time.
    Falls back silently to the hardcoded constants if the file is absent."""
    floors_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "memo-floors-v1.json")
    if not os.path.isfile(floors_path):
        return  # fallback: keep hardcoded tables
    try:
        data = json.loads(open(floors_path, encoding="utf-8").read())
    except Exception as exc:
        sys.stderr.write(
            "WARNING: memo-floors-v1.json found but could not be parsed (%s); "
            "using hardcoded fallback floors.\n" % exc)
        return
    global WHOLE_MEMO_WORD_FLOOR, SECTION_WORD_FLOOR, ELEMENT_WORD_FLOOR
    global ELEMENT_BULLET_FLOOR, RA_FLOOR_OVERRIDE, CARVE_OUT_ELEVATED, IN_SCOPE_ELEMENTS
    if "whole_memo_word_floor" in data:
        WHOLE_MEMO_WORD_FLOOR = data["whole_memo_word_floor"]
    if "section_word_floor" in data:
        SECTION_WORD_FLOOR = data["section_word_floor"]
    if "element_word_floor" in data:
        ELEMENT_WORD_FLOOR = data["element_word_floor"]
    if "element_bullet_floor" in data:
        ELEMENT_BULLET_FLOOR = data["element_bullet_floor"]
    if "ra_floor_override" in data:
        RA_FLOOR_OVERRIDE = data["ra_floor_override"]
    if "carve_out_elevated" in data:
        CARVE_OUT_ELEVATED = data["carve_out_elevated"]
    if "in_scope_elements" in data:
        IN_SCOPE_ELEMENTS = data["in_scope_elements"]


_load_floors_json()


# --------------------------------------------------------------------------
# Memo parsing
# --------------------------------------------------------------------------
def normalise_stage(raw):
    key = (raw or "").strip().lower()
    if key not in STAGE_ALIASES:
        sys.stderr.write("ERROR: unknown stage '%s'. "
                         "Use one of: triaging | esa | dd\n" % raw)
        sys.exit(2)
    return STAGE_ALIASES[key]


def word_count(text):
    return len(re.findall(r"\b[\w'-]+\b", text))


def split_sections(memo_text):
    """Split the memo into Sections A-F by '## Section X' or '# Section X' headers.
    Returns {section_letter: body_text}. Tolerant of '## Section C - ...' etc."""
    sections = {}
    header_re = re.compile(r"^#{1,3}\s*Section\s+([A-F])\b.*$", re.MULTILINE | re.IGNORECASE)
    matches = list(header_re.finditer(memo_text))
    for i, m in enumerate(matches):
        letter = m.group(1).upper()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(memo_text)
        sections[letter] = memo_text[start:end]
    return sections


def find_elements(memo_text):
    """Return {element_id: body_text} for every E# section heading found.
    BOUNDARY FIX (2026-06-13): bound each element at the next heading whose level
    is <= the element heading level (next Group/Pillar/Section or same-level
    Element), not just the next E# heading. Old logic ran the LAST element to EOF
    and over-counted its word floor (the 1U1-DE E11 under-floor mask)."""
    elements = {}
    head_re = re.compile(r"^(#{1,6})[ \t]*(.*)$", re.MULTILINE)
    heads = [(mm.start(), mm.end(), len(mm.group(1)), mm.group(0))
             for mm in head_re.finditer(memo_text)]
    elem_re = re.compile(r"^#{2,6}\s*(?:Element\s+)?(E\d{1,2})\b", re.IGNORECASE)
    for idx, (hstart, hend, level, line) in enumerate(heads):
        em = elem_re.match(line)
        if not em:
            continue
        eid = em.group(1).upper()
        if eid in elements:
            continue
        end = len(memo_text)
        for (h2start, _e, level2, _l) in heads[idx + 1:]:
            if level2 <= level:
                end = h2start
                break
        elements[eid] = memo_text[hend:end]
    return elements


def count_bullets(text):
    """Count markdown bullet lines (-, *, +) at any indent level."""
    return len(re.findall(r"^\s*[-*+]\s+\S", text, re.MULTILINE))


def mentions_not_applicable(memo_text, eid):
    """True if the memo explicitly marks an Element 'not applicable at this stage'."""
    pat = re.compile(re.escape(eid) + r"\b[^\n]{0,120}not applicable", re.IGNORECASE)
    if pat.search(memo_text):
        return True
    pat2 = re.compile(r"not applicable[^\n]{0,120}\b" + re.escape(eid) + r"\b",
                      re.IGNORECASE)
    return bool(pat2.search(memo_text))


# --------------------------------------------------------------------------
# Discipline checks (mechanically checkable subset of COMMUNICATING + PRESENTING)
# --------------------------------------------------------------------------
def check_three_layer_bluf(memo_text):
    """Page-level BLUF (after title), section-level BLUF, section-closing summary.
    Heuristic: page-level = a 'BLUF' or 'Bottom Line Up Front' marker near the top;
    section-level/closing = italic lines as a proxy."""
    has_page = bool(re.search(r"\b(BLUF|Bottom Line Up Front)\b",
                              memo_text[:4000], re.IGNORECASE))
    italic_lines = re.findall(r"^[*_][^*_\n].*[*_]\s*$", memo_text, re.MULTILINE)
    has_italic_layers = len(italic_lines) >= 2
    return has_page and has_italic_layers, {
        "page_bluf": has_page,
        "italic_layer_count": len(italic_lines),
    }


def check_grades_present(memo_text):
    """A-F grades present. Looks for [A]/[B]/[C]/[D]/[F] tokens or pill markup."""
    grade_tokens = re.findall(r"\[(?:A|B|C|D|F)\]", memo_text)
    pill_tokens = re.findall(r"\bp-(?:A|B|C|D|F)\b", memo_text)
    total = len(grade_tokens) + len(pill_tokens)
    return total, grade_tokens


def check_counter_view(elements, in_scope):
    """Every IN-SCOPE, substantively-present Element should carry a
    'Counter-view considered' block. Out-of-scope Elements that are present
    only as a 'not applicable' note are NOT required to carry one."""
    missing = []
    for eid in in_scope:
        body = elements.get(eid)
        if body is None:
            continue  # absence is caught by the scope-completeness check
        if not re.search(r"counter[- ]view", body, re.IGNORECASE):
            missing.append(eid)
    return missing


# --------------------------------------------------------------------------
# Format reform checks (D-AJ-21, 2026-06-16): no prose paragraphs; 40-word
# bullet ceiling (HARD); CQ ratings on judgement-bearing Core Questions (HARD);
# acronym / shorthand without a plain-English description (SOFT).
# --------------------------------------------------------------------------
_SENT_END_RX = re.compile(r'[.!?](?:\s|$)')

def _strip_md(text):
    t = re.sub(r'`[^`]*`', '', text)
    t = re.sub(r'[*_>#]+', '', t)
    return t.strip()

def _iter_body_blocks(section_text):
    """Yield (kind, text, raw_lines) blocks, skipping HTML comments. kind in
    {heading, bullet, numlist, blockquote, table, hr, prose}."""
    lines = section_text.split("\n")
    i, n = 0, len(lines)
    in_comment = False
    while i < n:
        ln = lines[i]; s = ln.strip()
        if in_comment:
            if "-->" in s:
                in_comment = False
            i += 1; continue
        if s.startswith("<!--"):
            if "-->" not in s:
                in_comment = True
            i += 1; continue
        if not s:
            i += 1; continue
        if re.match(r'^#{1,6}\s', s):
            yield ("heading", s, [ln]); i += 1; continue
        if re.match(r'^-{3,}$', s):
            yield ("hr", s, [ln]); i += 1; continue
        if s.startswith(">"):
            blk = []
            while i < n and lines[i].strip().startswith(">"):
                blk.append(lines[i]); i += 1
            yield ("blockquote", "\n".join(blk), blk); continue
        if s.startswith("|"):
            blk = []
            while i < n and lines[i].strip().startswith("|"):
                blk.append(lines[i]); i += 1
            yield ("table", "\n".join(blk), blk); continue
        if re.match(r'^[-*+]\s', s):
            yield ("bullet", s, [ln]); i += 1; continue
        if re.match(r'^\d+\.\s', s):
            yield ("numlist", s, [ln]); i += 1; continue
        para = [ln]; i += 1
        while i < n:
            s2 = lines[i].strip()
            if (not s2 or re.match(r'^#{1,6}\s', s2) or s2.startswith(">")
                    or s2.startswith("|") or re.match(r'^[-*+]\s', s2)
                    or re.match(r'^\d+\.\s', s2) or s2.startswith("<!--")
                    or re.match(r'^-{3,}$', s2)):
                break
            para.append(lines[i]); i += 1
        yield ("prose", " ".join(x.strip() for x in para), para)

def check_no_prose(sections):
    """HARD (D-AJ-21): no prose paragraphs in body Sections B-E. A non-bullet,
    non-heading, non-table, non-list body block of >1 sentence OR >40 words is a
    banned prose paragraph; a blockquote summary that is prose (not bullets) and
    exceeds that bound is also flagged. Carve-outs: headings, tables, lists,
    short single-sentence lead-ins/notes, Section A hero fields, Section F."""
    violations = []
    for L in ("B", "C", "D", "E"):
        body = sections.get(L)
        if not body:
            continue
        for kind, text, raw in _iter_body_blocks(body):
            if kind == "prose":
                plain = _strip_md(text)
                w = word_count(plain); sents = len(_SENT_END_RX.findall(plain))
                if w > 40 or sents > 1:
                    violations.append("%s: prose para (%dw,%dsent): %s"
                                      % (L, w, sents, plain[:48]))
            elif kind == "blockquote":
                has_bullets = any(re.match(r'^\s*>\s*[-*+]\s', x) for x in raw)
                if not has_bullets:
                    inner = " ".join(re.sub(r'^\s*>\s?', '', x) for x in raw)
                    plain = _strip_md(inner)
                    w = word_count(plain); sents = len(_SENT_END_RX.findall(plain))
                    if w > 40 or sents > 1:
                        violations.append("%s: prose summary in colour block (%dw,%dsent): %s"
                                          % (L, w, sents, plain[:48]))
    return violations

def check_bullet_ceiling(sections):
    """HARD (D-AJ-21 / Communicating C1): no body bullet over 40 words. Applies
    to markdown bullets incl. blockquote bullets (> - ). Numbered lists (the
    locked invalidation thresholds) and tables are excluded; so are Sections A/F."""
    over = []
    for L in ("B", "C", "D", "E"):
        body = sections.get(L)
        if not body:
            continue
        for ln in body.split("\n"):
            m = re.match(r'^\s*(?:>\s*)?[-*+]\s+(.*)$', ln)
            if not m:
                continue
            plain = _strip_md(m.group(1))
            w = word_count(plain)
            if w > 40:
                over.append("%s (%dw): %s" % (L, w, plain[:48]))
    return over

def check_cq_ratings(memo_text):
    """HARD (D-AJ-21): every Core Question unit (a bullet or heading whose label
    carries a CQ token) must carry an [A]-[F] grade (judgement-bearing) OR a
    [factual] tag (intended-ungraded). Missing both = HARD."""
    missing = []
    for ln in memo_text.split("\n"):
        s = ln.strip()
        is_bullet_cq = re.match(r'^(?:>\s*)?[-*+]\s+\**[^\n]*\bCQ\d+\b', s)
        is_head_cq = re.match(r'^#{3,6}\s+[^\n]*\bCQ\d+\b', s)
        if not (is_bullet_cq or is_head_cq):
            continue
        # read the grade from the bold label (between the first **...**), so a colon
        # INSIDE the question does not hide a grade that follows it (v2 fix).
        _mlab = re.match(r'^(?:>\s*)?[-*+]\s+\*\*(.+?)\*\*', s)
        label = _mlab.group(1) if _mlab else s.split(":", 1)[0]
        if re.search(r'\[[ABCDF]\]', label) or re.search(r'\[factual\]', label, re.I):
            continue
        if is_head_cq and (re.search(r'\[[ABCDF]\]', s)
                           or re.search(r'\[factual\]', s, re.I)):
            continue
        m = re.search(r'\bCQ\d+\b', s)
        missing.append((m.group(0) if m else "CQ") + ": " + _strip_md(s)[:44])
    return missing

def check_cq_answer_clauses(memo_text):
    """HARD (F5, D-AJ-27 2026-06-17): every in-scope judgement Core Question MAIN
    bullet must carry a one-line answer clause after the closing **label** bold span.
    Pattern: - **E# RA# CQ<n> ... [GRADE]** <answer clause (>=3 words)>
    Factual CQs ([factual] tagged) are exempt (they may carry only the tag).
    Heading-style CQs are exempt (no trailing prose expected in a heading).
    Returns list of (cq_id, line_excerpt) tuples for any failing lines.
    """
    missing = []
    for ln in memo_text.split("\n"):
        s = ln.strip()
        # Must be a bullet that carries a CQ token
        if not re.match(r'^(?:>\s*)?[-*+]\s+\**[^\n]*\bCQ\d+\b', s):
            continue
        # Exempt factual CQs
        _lab_m = re.match(r'^(?:>\s*)?[-*+]\s+\*\*(.+?)\*\*', s)
        label = _lab_m.group(1) if _lab_m else ""
        if re.search(r'\[factual\]', label, re.I) or re.search(r'\[factual\]', s, re.I):
            continue
        # Judgement CQs must have an [A-F] grade in the label
        if not re.search(r'\[[ABCDF]\]', label):
            continue  # not a graded CQ bullet — let check_cq_ratings catch it
        # Extract text after the closing ** of the bold label
        after_label = re.sub(r'^(?:>\s*)?[-*+]\s+\*\*.*?\*\*\s*', '', s)
        # Strip any trailing inline codes / brackets / whitespace
        answer_words = re.findall(r'[A-Za-z\d]+', after_label)
        if len(answer_words) < 3:
            cq_m = re.search(r'\bCQ(\d+)\b', s)
            cq_id = "CQ" + cq_m.group(1) if cq_m else "CQ?"
            missing.append((cq_id, _strip_md(s)[:60]))
    return missing


def check_acronym_descriptions(memo_text):
    """SOFT (D-AJ-21): flag source-borrowed shorthand and bare codes that should
    carry a plain-English description: L<n> (last-n shorthand), E<n>/E<n> element
    slash-runs, and bare cohort codes TCM<n> not written inside parentheses."""
    hits = []
    for m in re.finditer(r'\bL\d+\b', memo_text):
        hits.append(m.group(0))
    for m in re.finditer(r'\bE\d+(?:/E\d+)+\b', memo_text):
        hits.append(m.group(0))
    for m in re.finditer(r'(?<!\()\bTCM\d+\b(?!\))', memo_text):
        hits.append(m.group(0))
    uniq = sorted(set(hits))
    return uniq, len(hits)


def _body_bullets(sections):
    """All body bullet texts (Sections B-E), HTML comments stripped."""
    chunks = []
    for L in ("B", "C", "D", "E"):
        body = sections.get(L) or ""
        body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
        for ln in body.split("\n"):
            m = re.match(r"^\s*(?:>\s*)?[-*+]\s+(.*)$", ln)
            if m:
                chunks.append(m.group(1))
    return chunks

_ITALIC_RX = re.compile(r"(?<!\*)\*(?!\*)(?!\s)(.+?)(?<!\s)\*(?!\*)")  # fix: (?!\*) after opening * prevents matching **bold:** as italic (18-Jun-26)

def check_underline_hard(sections):
    """HARD (F1, D-AJ-24): >=20% of body-bullet words underlined (__text__)."""
    chunks = _body_bullets(sections)
    total = sum(word_count(_strip_md(c)) for c in chunks)
    ul = 0
    for c in chunks:
        for m in re.findall(r"__(.+?)__", c):
            ul += word_count(m)
    pct = (ul / total) if total else 0.0
    return pct, ul, total

def check_highlight_hard(sections):
    """HARD (F2, D-AJ-24): >=30% of body bullets carry a ==sentiment== highlight."""
    chunks = _body_bullets(sections)
    n = len(chunks)
    hl = sum(1 for c in chunks if re.search(r"==[^=]", c))
    pct = (hl / n) if n else 0.0
    return pct, hl, n

def check_italic_hard(sections):
    """HARD (F3, D-AJ-24): >=20% of body bullets carry an italic (*text*) span."""
    chunks = _body_bullets(sections)
    n = len(chunks)
    it = sum(1 for c in chunks if _ITALIC_RX.search(c))
    pct = (it / n) if n else 0.0
    return pct, it, n

def check_signposting(sections):
    """HARD (F13, D-AJ-24): every body bullet (incl. sub-bullets) opens with a
    bold signpost label (**...**).
    Exemption (18-Jun-26): bullets opening with *italic* are valid closing/summary
    bullets required by the BLUF spec — they are not unsignposted."""
    bad = []
    for L in ("B", "C", "D", "E"):
        body = sections.get(L) or ""
        body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
        for ln in body.split("\n"):
            m = re.match(r"^\s*(?:>\s*)?[-*+]\s+(.*)$", ln)
            if not m:
                continue
            txt = m.group(1).lstrip()
            if txt.startswith("**"):
                continue  # correctly signposted
            if txt.startswith("*") and not txt.startswith("**"):
                continue  # italic closing/summary bullet — valid, exempt from signpost
            bad.append("%s: %s" % (L, _strip_md(m.group(1))[:44]))
    return bad

def check_bullet_capitalisation(sections):
    """HARD (F11, D-AJ-24): each body bullet's first letter is capitalised."""
    bad = []
    for L in ("B", "C", "D", "E"):
        body = sections.get(L) or ""
        body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
        for ln in body.split("\n"):
            m = re.match(r"^\s*(?:>\s*)?[-*+]\s+(.*)$", ln)
            if not m:
                continue
            t = re.sub(r"^\**\s*", "", m.group(1))
            first = next((ch for ch in t if ch.isalpha()), "")
            if first and first.islower():
                bad.append("%s: %s" % (L, _strip_md(m.group(1))[:44]))
    return bad

def check_spellout_hard(memo_text):
    """HARD (F14, D-AJ-24): bare element-code shorthand standing in for meaning
    (e.g. 'E8 verdict', 'E9/E10', 'L4') must be spelled out with the element name."""
    hits = []
    for m in re.finditer(r"\bE\d+\s+(verdict|answer|grade|summary|fit|setup|score)\b",
                         memo_text, re.I):
        hits.append(m.group(0))
    for m in re.finditer(r"\bE\d+(?:/E\d+)+\b", memo_text):
        hits.append(m.group(0))
    for m in re.finditer(r"\bL\d+\b", memo_text):
        hits.append(m.group(0))
    return sorted(set(hits)), len(hits)



def check_banned_phrases(memo_text):
    lower = memo_text.lower()
    hits = []
    for phrase in BANNED_PHRASES:
        for m in re.finditer(re.escape(phrase), lower):
            s = max(0, m.start() - 25)
            e = min(len(lower), m.end() + 25)
            hits.append((phrase, memo_text[s:e].replace("\n", " ").strip()))
    return hits


def check_emdash_in_bullets(memo_text):
    """Em-dashes are banned inside bullets (Presenting SOP Group 6)."""
    bad = []
    for line in memo_text.splitlines():
        if re.match(r"^\s*[-*+]\s+", line):
            test = re.sub(r"\*\*[^*]*\*\*", "", line)  # drop bold signpost labels
            if "—" in test:
                bad.append(line.strip()[:90])
    return bad


def check_trailing_period_bullets(memo_text):
    """Bullets should not end in a period (Presenting SOP Group 6)."""
    bad = []
    for line in memo_text.splitlines():
        if re.match(r"^\s*[-*+]\s+", line):
            stripped = line.rstrip()
            core = re.sub(r"(==|\*\*|__|\*|`)+$", "", stripped).rstrip()
            if core.endswith(".") and not core.endswith("..."):
                bad.append(stripped[:90])
    return bad


def check_html_tables(memo_text):
    """Pipe tables only - no HTML tables (Presenting SOP)."""
    return bool(re.search(r"<(table|tr|td|th)\b", memo_text, re.IGNORECASE))


def check_header_descent(memo_text):
    """Headers should descend without GROSS jumps.

    Note: the Presenting SOP's 6-tier hierarchy is not strictly sequential in
    practice - a memo can legitimately go '## Section C' straight to a tier-4
    or tier-6 Element heading. So this check only flags a GROSS skip (a jump of
    3+ levels at once), and the result is treated as a SOFT FLAG, not a hard
    fail - header rendering is partly judgement-dependent.
    Returns list of offending transitions (line snippets)."""
    offenders = []
    prev_level = None
    for line in memo_text.splitlines():
        m = re.match(r"^(#{1,6})\s+\S", line)
        if not m:
            continue
        level = len(m.group(1))
        if prev_level is not None and level > prev_level + 2:
            offenders.append("%s -> %s" % ("#" * prev_level, line.strip()[:70]))
        prev_level = level
    return offenders


def check_sentiment_highlight(memo_text, render_supports):
    """>= 30% of sentences sentiment-highlighted using ==+text==, ==-text==,
    ==~text== or ==text== (neutral) syntax.
    Phase-A rewrite 2026-06-14: replaces the prior Notion colour-wrapper heuristic
    which always reported 0% because memos use == not Notion colour markup."""
    if not render_supports:
        return None, 0, 0  # judgement-dependent; not checkable here
    # Count ==+text==, ==-text==, ==~text==, ==text== spans
    spans = len(re.findall(r'==[+~-]?[^=\n]+==', memo_text))
    # Approximate sentence count (strip code blocks and pipe-table rows first)
    body = re.sub(r'```[\s\S]*?```', '', memo_text)
    body = re.sub(r'^\|.*\|.*$', '', body, flags=re.MULTILINE)
    sentences = len(re.findall(r'[.!?](?:\s|$)', body))
    pct = (spans / sentences) if sentences else 0.0
    return pct, spans, sentences


def check_invalidation_thresholds(memo_text):
    """The 10 Invalidation thresholds should appear verbatim at D.II (ESA/DD).
    Heuristic: a D.II heading plus a 10-item numbered list near it."""
    has_dii = bool(re.search(r"\bD\.?\s?II\b|D\.II", memo_text))
    numbered = re.findall(r"^\s*(\d{1,2})[.)]\s+\S", memo_text, re.MULTILINE)
    has_ten = numbered.count("10") >= 1 and numbered.count("1") >= 1
    return has_dii, has_ten


def check_driver_tables(memo_text):
    """7-column upstream/downstream driver tables present (ESA/DD)."""
    for line in memo_text.splitlines():
        if line.count("|") >= 7 and re.search(
                r"\b(LTI|leading tracking|invalidation)\b", line, re.IGNORECASE):
            return True
    for line in memo_text.splitlines():
        cells = [c for c in line.split("|") if c.strip()]
        if len(cells) >= 7 and "-" not in line.replace("|", "").strip()[:3]:
            return True
    return False


def check_sensitivity_scenario(memo_text):
    """DD only: D.IV sensitivity + scenario tables present (SOFT presence check).
    Numbers are IA/FA content; this verifies the scaffold exists, not its values."""
    has_sens = bool(re.search(r"sensitivit", memo_text, re.IGNORECASE))
    has_scen = bool(re.search(r"\bscenario", memo_text, re.IGNORECASE))
    return has_sens, has_scen


# --------------------------------------------------------------------------
# Required-Attribute / Core-Question parsing (per-RA bullet enforcement, R1/R2)
# --------------------------------------------------------------------------
# RA heading: a bold line beginning '**RA<n>' (both memo eras render it this way).
_RA_HEAD_RE = re.compile(
    r"^\s*(?:#{2,6}\s*(?:E\d+\s*[-\u2013\u2014]?\s*)?|\*\*)RA(\d+)\b",
    re.MULTILINE)
# CQ marker: standalone bold '**CQ<n>' (14-May era) OR inline bold bullet
# '- **E# RA# CQ<n>,' / '**...CQ<n>' (Jun era). Count distinct occurrences.
_CQ_MARK_RE = re.compile(r"\*\*(?:[^*\n]*?)?CQ(\d+)\b", re.IGNORECASE)
# Markers that end an Element's RA content (trailing blocks that must not be
# counted toward the last RA's bullet tally).
_RA_END_RE = re.compile(
    r"(?im)^\s*(?:[-*+]\s+)?(?:\*\*)?(?:Element rating|Counter[- ]view|Downstream action|"
    r"Element-closing|\*Element-closing)")


def split_required_attributes(element_body):
    """Split an Element body into [(ra_id, ra_block_text), ...].
    Each block runs from its '**RA<n>' marker to the next RA marker, trimmed at
    the first trailing-block marker (Element rating / Counter-view / Downstream
    action / Element-closing). Returns [] if no RA markers found."""
    heads = list(_RA_HEAD_RE.finditer(element_body))
    if not heads:
        return []
    blocks = []
    for i, m in enumerate(heads):
        ra_id = "RA" + m.group(1)
        start = m.start()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(element_body)
        block = element_body[start:end]
        # trim at the first trailing-block marker inside this block
        tm = _RA_END_RE.search(block)
        if tm:
            block = block[:tm.start()]
        blocks.append((ra_id, block))
    return blocks


def count_core_questions(ra_block):
    """Distinct Core Questions referenced inside an RA block."""
    nums = set(_CQ_MARK_RE.findall(ra_block))
    return len(nums)


def per_ra_bullet_rows(eid, body, stage, base_floor):
    """Build per-RA bullet-floor rows for one Element at ESA/DD.
    Returns (rows, element_total_bullets, parsed_ok)."""
    rows = []
    ra_blocks = split_required_attributes(body)
    overrides = RA_FLOOR_OVERRIDE.get(stage, {}).get(eid, {})
    if not ra_blocks:
        # parser could not find RA structure: fall back to a lenient element-total
        # check and SOFT-flag the fallback so it is visible.
        n = count_bullets(body)
        # element-total fallback floor: base x 2 (summary + at least one CQ band)
        fb = base_floor * 2
        v = SOFT if n < fb else PASS
        rows.append(Row("%s bullet floor (RA parse fallback)" % eid,
                        ">= %d (element total, base x2)" % fb,
                        "%d bullets; RA markers not parsed" % n, v,
                        "RA structure not detected - relied on element-total check"))
        return rows, n, False
    element_total = 0
    for ra_id, block in ra_blocks:
        n = count_bullets(block)
        element_total += n
        floor = overrides.get(ra_id, base_floor)
        n_cq = count_core_questions(block)
        expected = floor * (1 + n_cq)
        if n < expected:
            v = HARD
        elif n < expected * (1 + THIN_MARGIN):
            v = SOFT
        else:
            v = PASS
        ovr = " (x-weight override)" if ra_id in overrides else ""
        rows.append(Row("%s %s bullet floor%s" % (eid, ra_id, ovr),
                        ">= %d (=%d x [1 summary + %d CQ])" % (expected, floor, n_cq),
                        "%d bullets" % n, v))
    return rows, element_total, True


# --------------------------------------------------------------------------
# New discipline checks (R3): downstream actions, cohort anchor, D/F-before-A/B
# --------------------------------------------------------------------------
def check_downstream_actions(elements, in_scope, stage="triaging", sections=None):
    """Stage-aware downstream-actions check (Communicating SOP G19).
    Triaging: each in-scope Element must carry a per-element actions block (>= 2).
    ESA/DD: PASS if a consolidated E.III block with >= 2 actions exists; falls
    back to per-element check if no E.III found (Phase-A rewrite 2026-06-14)."""
    if stage in ("esa", "dd"):
        # Check for consolidated E.III downstream-actions block in Section E
        e_body = (sections.get("E", "") if sections else "") or ""
        if not e_body:
            # fallback: search across all element text
            e_body = "\n".join(elements.get(eid, "") for eid in in_scope)
        eiii_m = re.search(r"(?i)E\.?\s*III\b", e_body)
        if eiii_m:
            after_eiii = e_body[eiii_m.end():eiii_m.end() + 3000]
            n_consol = len(re.findall(r"^\s*[-*+]\s+\S", after_eiii, re.MULTILINE))
            if n_consol >= 2:
                return []  # consolidated E.III block present and sufficient
        # Fall back: per-element check (some ESA memos use per-element structure)
        per_fails = []
        for eid in in_scope:
            body = elements.get(eid)
            if body is None:
                continue
            m = re.search(r"(?i)downstream action", body)
            if not m:
                per_fails.append("%s (no block)" % eid)
            else:
                tail = body[m.end():]
                n = len(re.findall(r"^\s*[-*+]\s+\S", tail, re.MULTILINE))
                if n < 2:
                    per_fails.append("%s (%d)" % (eid, n))
        if not per_fails:
            return []  # per-element structure satisfies
        eiii_note = (" (no E.III block)" if not eiii_m
                     else " (E.III block has < 2 actions)")
        return [", ".join(per_fails[:4]) + eiii_note]
    else:
        # Triaging: original per-element check
        fails = []
        for eid in in_scope:
            body = elements.get(eid)
            if body is None:
                continue
            m = re.search(r"(?i)downstream action", body)
            if not m:
                fails.append("%s (no actions block)" % eid)
                continue
            tail = body[m.end():]
            n_actions = len(re.findall(r"^\s*[-*+]\s+\S", tail, re.MULTILINE))
            if n_actions < 2:
                fails.append("%s (%d)" % (eid, n_actions))
        return fails


def check_cohort_anchor(elements, in_scope):
    """Each in-scope Element grade should be struck against a cohort/peer/base-rate
    anchor (D-IA-4RR-09 cohort grading)."""
    anchor_re = re.compile(
        r"(?i)(cohort|vs\.?\s+peers?|peer set|peer group|base rate|"
        r"versus the|against the (live )?cohort|relative to (the )?peers)")
    missing = []
    for eid in in_scope:
        body = elements.get(eid)
        if body is None:
            continue
        if not anchor_re.search(body):
            missing.append(eid)
    return missing


def _element_headline_grade(body):
    """Best-effort headline A-F grade for an Element block."""
    m = re.search(r"Element rating[^\n]*?\[([ABCDF])\]", body)
    if m:
        return m.group(1)
    m = re.search(r"\[([ABCDF])\]", body)
    return m.group(1) if m else None


def check_df_before_ab_bluf(sections, elements, in_scope):
    """If any in-scope Element headline grades D/F, the BLUF (Section B) should
    surface a D/F before the first A/B (Communicating SOP G8). Heuristic, SOFT."""
    headline_grades = [_element_headline_grade(elements.get(e, "")) for e in in_scope]
    has_df = any(g in ("D", "F") for g in headline_grades if g)
    if not has_df:
        return True, "no D/F element-headline grades to order"
    b = sections.get("B", "")
    ab = re.search(r"\[(?:A|B)\]", b)
    df = re.search(r"\[(?:D|F)\]", b)
    if df is None:
        return False, "D/F finding(s) exist but none surfaced in the BLUF"
    if ab is not None and ab.start() < df.start():
        return False, "first A/B appears before first D/F in the BLUF"
    return True, "D/F surfaced before A/B in the BLUF"


_GRADE_VAL = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}


def check_grade_rollup(elements, in_scope):
    """Flag Elements whose headline grade sits >1 notch above the mean of their
    own sub-grades (grade-inflation heuristic, R4)."""
    flagged = []
    for eid in in_scope:
        body = elements.get(eid)
        if body is None:
            continue
        headline = _element_headline_grade(body)
        if headline is None:
            continue
        subs = re.findall(r"\[([ABCDF])\]", body)
        # drop the headline grade occurrences (count it once as headline)
        sub_vals = [_GRADE_VAL[g] for g in subs]
        # remove one instance of the headline value (the headline token itself)
        if headline in [s for s in subs]:
            sub_vals_wo = list(sub_vals)
            try:
                sub_vals_wo.remove(_GRADE_VAL[headline])
            except ValueError:
                sub_vals_wo = sub_vals
        else:
            sub_vals_wo = sub_vals
        if len(sub_vals_wo) < 2:
            continue
        mean = sum(sub_vals_wo) / float(len(sub_vals_wo))
        if _GRADE_VAL[headline] - mean > 1.0:
            flagged.append("%s headline [%s] vs sub-grade mean %.1f" % (
                eid, headline, mean))
    return flagged


# --------------------------------------------------------------------------
# Row builder
# --------------------------------------------------------------------------
class Row(object):
    __slots__ = ("dimension", "standard", "actual", "verdict", "note")

    def __init__(self, dimension, standard, actual, verdict, note=""):
        self.dimension = dimension
        self.standard = standard
        self.actual = actual
        self.verdict = verdict
        self.note = note



# --------------------------------------------------------------------------
# V4.3 redesign structural compliance checks (Opus 2026-06-12).
# These catch a memo written to a PRE-redesign skeleton (the 1U1-DE failure
# mode) and the "stopped at B.3" failure (the AALB-NL B.4/5/6 gap) -- both of
# which the prior gate was blind to, so both passed IA self-QC wrongly.
# --------------------------------------------------------------------------
def check_section_a_heading(memo_text):
    """SOP-04 R3: Section A heading must be 'Section A - Summary Snapshot'."""
    return bool(re.search(r"^#{1,3}\s*Section\s+A\s*[\u2014\-]\s*Summary\s+Snapshot\b",
                          memo_text, re.MULTILINE | re.IGNORECASE))

def check_b_subsections(memo_text):
    """SOP-04 B4-B6: B.1-B.6 must ALL be present as Section B subsections."""
    present, missing = [], []
    for n in range(1, 7):
        if re.search(r"^#{2,4}\s*B\.%d\b" % n, memo_text, re.MULTILINE):
            present.append("B.%d" % n)
        else:
            missing.append("B.%d" % n)
    return present, missing

def check_mr_headings(memo_text):
    """SOP-04 B2/B3: six Master-Rating headings MR1-MR6."""
    return sorted(set(re.findall(r"^#{3,5}\s*(MR[1-6])\b", memo_text, re.MULTILINE)))

def check_blockquote_summaries(memo_text, sections, stage):
    """SOP-03 C6 / SOP-04 R8: every major Section must open with a '> ' summary.
    Zero blockquotes = no summary mechanism at all (the 1U1-DE case)."""
    total = len(re.findall(r"^\s*>\s+\S", memo_text, re.MULTILINE))
    expected = ["B", "C", "E"] + (["D"] if stage in ("esa", "dd") else [])
    missing = [L for L in expected if L in sections
               and not re.search(r"^\s*>\s+\S", sections[L], re.MULTILINE)]
    return total, missing

def check_judgement_summary_labels(memo_text):
    """SOP-03 C6 / SOP-04 R8: '**JUDGEMENT SUMMARY' bold labels are BANNED
    (deprecated). Matches the bold label only, never the words in a checklist line."""
    return len(re.findall(r"\*\*\s*JUDGEMENT\s+SUMMARY", memo_text, re.IGNORECASE))

def check_gng_present(meta):
    """SOP-04: a Go-No-Go Checks one-pager must be paired with every memo."""
    mp = meta.get("__memo_path")
    if not mp:
        return None, "memo path not supplied to the audit"
    import glob as _glob
    d = os.path.dirname(mp)
    hits = [os.path.basename(x) for x in _glob.glob(os.path.join(d, "*"))
            if re.search(r"gng|go-?no-?go", os.path.basename(x), re.IGNORECASE)
            and not re.search(r"superseded|archived", os.path.basename(x), re.IGNORECASE)]
    return (len(hits) > 0), (", ".join(hits[:2]) if hits else "no Go-No-Go file in memo folder")


# --------------------------------------------------------------------------
# Phase-A gate hardening checks (2026-06-14)
# --------------------------------------------------------------------------

def check_invalid_grades(memo_text):
    """HARD: any bracketed grade token outside {A,B,C,D,F,NR} is a defect.
    Catches [E] (letter E is not in the A/B/C/D/F grading system) and grade
    tokens with +/- modifiers like [B+], [A-] (banned everywhere in the system)."""
    invalid = []
    # Grade-with-modifier: [B+], [A-], [C-], [D+] etc. — always wrong
    for m in re.finditer(r'\[([A-F][+\-])\]', memo_text):
        invalid.append(m.group(0))
    # [E] used as a grade: E is not in the grading system (A/B/C/D/F)
    for m in re.finditer(r'\[E\]', memo_text):
        invalid.append('[E]')
    unique = sorted(set(invalid))
    return unique, len(invalid)


def check_ratings_json(meta):
    """HARD: ratings.json must exist in the memo folder, be parseable JSON,
    and contain the correct ticker key (so the viewer can populate nav chips)."""
    mp = meta.get("__memo_path")
    ticker = meta.get("ticker", "")
    if not mp:
        return None, None, "memo path not supplied to the audit"
    memo_dir = os.path.dirname(mp)
    ratings_path = os.path.join(memo_dir, "ratings.json")
    # Also accept legacy {TICKER}-{Stage}-ratings.json naming — gen_memo_viewer
    # already produces this for some stacks. Glob if canonical name absent.
    if not os.path.isfile(ratings_path):
        import glob as _glob
        legacy = _glob.glob(os.path.join(memo_dir, "*-ratings.json"))
        if legacy:
            ratings_path = max(legacy, key=os.path.getmtime)
        else:
            return False, False, "ratings.json NOT found in memo folder"
    try:
        data = json.loads(open(ratings_path, encoding="utf-8").read())
    except Exception as exc:
        return True, False, "ratings.json found but JSON parse error: %s" % exc
    if not ticker:
        return True, None, "ratings.json found and parseable; ticker not in meta, key check skipped"
    # Two canonical ratings.json schemas exist in the toolchain and BOTH are valid;
    # accept either so a correctly-authored memo is never hard-failed (2026-06-15 fix
    # after the field-only check regressed and blocked the geo-key-nested schema that
    # the Memo Writer authors per first-hand diligence amendment A / SESSION-CAPTURE 7):
    #   (1) renderer-written FLAT: {"ticker": "{TICKER-EX}", "ratings": {...}, ...}
    #   (2) writer-authored GEO-KEY-NESTED: {"{TICKER-EX}": {"ticker": "{TICKER-EX}", ...}}
    if data.get("ticker") == ticker:
        return True, True, "ratings.json present; flat ticker field '%s' matched" % ticker
    nested = data.get(ticker)
    if isinstance(nested, dict):
        return True, True, ("ratings.json present; ticker key '%s' found "
                            "(geo-key-nested writer schema)" % ticker)
    actual = data.get("ticker", "<not present>")
    return True, False, (
        "ratings.json found but neither schema matched: no top-level '%s' key, and "
        "top-level ticker field = '%s'" % (ticker, actual))


def check_internal_codes(memo_text):
    """SOFT: Watson-coined workstream codes (e.g. SA05, TCM06) must not appear
    in memo body text visible to Richard (internal-code firewall). Pattern:
    2-5 uppercase letters immediately followed by 2-3 digits (no space).
    SAFE_PREFIX_SET excludes standard financial abbreviations (FY, IFRS, IAS,
    Q-codes, RA, CQ, MR, LT/NTM/LTM multiples) that are not Watson codes."""
    WHITELIST = {"MR10", "MR11", "MR12", "MR13", "MR14", "MR15"}
    SAFE_PREFIX_SET = {
        "FY",   # fiscal year: FY24, FY25, FY26
        "IFRS", # accounting standard: IFRS16, IFRS15, IFRS17
        "IAS",  # accounting standard: IAS36, IAS38, IAS19
        "MR",   # master rating headings: MR10+
        "RA",   # research-area headings: RA10+ (edge)
        "CQ",   # cross-question headings: CQ10+ (edge)
        "LT",   # long-term multiple: LT12, LT24
        "NTM",  # next-twelve-months: NTM12
        "LTM",  # last-twelve-months: LTM12
        "EV",   # enterprise value: EV12, EV24
        "PE",   # price/earnings: PE12, PE24
        "MA",   # moving average: MA50, MA200
        "RS",   # relative strength: RS200
        "ROE",  # return on equity: ROE15
        "ROA",  # return on assets: ROA10
        "ROI",  # return on investment: ROI12
    }
    hits = re.findall(r'\b([A-Z]{2,5}\d{2,3})\b', memo_text)
    flagged = [
        h for h in hits
        if h not in WHITELIST
        and not any(h.startswith(p) for p in SAFE_PREFIX_SET)
    ]
    return sorted(set(flagged)), len(flagged)


def check_section_a_brevity(sections, char_limit=80):
    """SOFT: Section A field values must be <= char_limit characters (SOP R3,
    80-char limit locked by Richard 2026-06-14). Checks pipe-table cells and
    bold **Key:** Value lines."""
    a_body = sections.get("A", "")
    violations = []
    HEADER_WORDS = {"value", "field", "---", ":---", "---:", ":---:"}
    # Pipe table cells (second column = value column)
    for m in re.finditer(r'^\|([^|\n]+)\|([^|\n]+)\|', a_body, re.MULTILINE):
        cell = m.group(2).strip()
        if not cell or cell.lower().strip("-: ") in HEADER_WORDS:
            continue
        if len(cell) > char_limit:
            violations.append("%s... [%d chars]" % (cell[:40], len(cell)))
    # Bold key-value lines: **Key:** Value
    for m in re.finditer(r'^\*\*[^*\n]+\*\*[:\s]+(.+)$', a_body, re.MULTILINE):
        val = m.group(1).strip()
        if len(val) > char_limit:
            violations.append("%s... [%d chars]" % (val[:40], len(val)))
    return violations


def check_underline_density(sections):
    """SOFT: underline coverage target ~20% per section (SOP Presenting R5).
    Flag if < 12% (too thin) or > 30% (over-underlined).
    Uses __text__ markdown underline syntax. Skips stub sections (< 100 words)."""
    results = []
    MIN_PCT = 0.12
    MAX_PCT = 0.30
    MIN_WORDS = 100
    for sec in sorted(k for k in sections.keys() if k not in ("A", "F")):
        body = sections[sec]
        total_words = word_count(body)
        if total_words < MIN_WORDS:
            continue
        underlined = re.findall(r'__(.+?)__', body, re.DOTALL)
        ul_words = sum(len(re.findall(r'\S+', u)) for u in underlined)
        pct = ul_words / float(total_words) if total_words else 0.0
        if pct < MIN_PCT:
            results.append(("Section %s" % sec, pct, "low (<12%)", total_words, ul_words))
        elif pct > MAX_PCT:
            results.append(("Section %s" % sec, pct, "high (>30%)", total_words, ul_words))
    return results


def check_cross_artefact(memo_text, meta):
    """SOFT: MR1-MR6 grades in the memo body must agree with ratings.json.
    Catches silent memo-vs-artefact divergence before shipping (Phase-A, 2026-06-14)."""
    ticker = meta.get("ticker", "")
    mp = meta.get("__memo_path")
    if not mp or not ticker:
        return None, "memo path or ticker not in meta"
    ratings_path = os.path.join(os.path.dirname(mp), "ratings.json")
    if not os.path.isfile(ratings_path):
        return None, "ratings.json not found (see ratings.json gate above)"
    try:
        ratings = json.loads(open(ratings_path, encoding="utf-8").read())
    except Exception as exc:
        return None, "ratings.json parse error: %s" % exc
    stock_ratings = ratings.get(ticker, {})
    if not stock_ratings:
        return None, "ticker '%s' not in ratings.json (see ratings.json gate)" % ticker
    # Extract MR1-MR6 from memo body: heading line then grade token (same or next line)
    memo_mr = {}
    for i in range(1, 7):
        m = re.search(
            r'MR%d\b[^\n]{0,80}\[([ABCDF])\]|MR%d\b\n[^\n]{0,80}\[([ABCDF])\]' % (i, i),
            memo_text)
        if m:
            memo_mr["MR%d" % i] = m.group(1) or m.group(2)
    conflicts = []
    for key, memo_grade in memo_mr.items():
        json_grade = stock_ratings.get(key)
        if json_grade and json_grade != memo_grade:
            conflicts.append("%s: memo=[%s] vs json=[%s]" % (key, memo_grade, json_grade))
    if conflicts:
        return False, "grade conflict(s): %s" % "; ".join(conflicts)
    if memo_mr:
        return True, "MR grades consistent (%d MR keys checked)" % len(memo_mr)
    return None, "no MR grade tokens found in memo body to compare"


def check_decimal_advisory(memo_text):
    """INFO: flag numbers with 3+ decimal places as potential precision excess.
    Advisory only — IA to review whether the precision is warranted."""
    hits = re.findall(r'\b\d+\.\d{3,}\b', memo_text)
    return hits


def build_rows(memo_text, stage, meta):
    rows = []
    sections = split_sections(memo_text)
    elements = find_elements(memo_text)
    in_scope = IN_SCOPE_ELEMENTS.get(stage, [])

    # ---- 1. Word-count floors: whole-memo + per-section ----
    body_sections = {k: v for k, v in sections.items() if k not in ("A", "F")}
    whole_words = sum(word_count(v) for v in body_sections.values())
    floor = WHOLE_MEMO_WORD_FLOOR.get(stage, 0)
    if floor:
        if whole_words < floor:
            v = HARD
        elif whole_words < floor * (1 + THIN_MARGIN):
            v = SOFT
        else:
            v = PASS
        rows.append(Row("Whole-memo word count (excl. A, F)", ">= %d" % floor,
                        "%d" % whole_words, v))
    else:
        rows.append(Row("Whole-memo word count (excl. A, F)", "no floor on record",
                        "%d" % whole_words, INFO))

    sec_floors = SECTION_WORD_FLOOR.get(stage, {})
    for letter in sorted(sections.keys()):
        w = word_count(sections[letter])
        sf = sec_floors.get(letter)
        if sf:
            if w < sf:
                v = HARD
            elif w < sf * (1 + THIN_MARGIN):
                v = SOFT
            else:
                v = PASS
            rows.append(Row("Section %s word count" % letter, ">= %d" % sf,
                            "%d" % w, v))
        else:
            rows.append(Row("Section %s word count" % letter, "no explicit floor",
                            "%d" % w, INFO,
                            "Thinking SOP states no explicit word floor for this section"))

    # ---- 2. Bullet-count floors: per in-scope Element ----
    bullet_floors = ELEMENT_BULLET_FLOOR.get(stage, {})
    if stage == "triaging":
        # Triaging keeps the proven element-aggregate check (>= base floor of
        # bullets in the Element block). Unchanged 2026-06-02.
        for eid in in_scope:
            body = elements.get(eid)
            bf = bullet_floors.get(eid)
            if body is None:
                continue  # absence caught by the scope check below
            n = count_bullets(body)
            if bf:
                if n < bf:
                    v = HARD
                elif n < bf + 1:  # exactly at floor -> thin
                    v = SOFT
                else:
                    v = PASS
                note = "exactly at floor - no margin" if v == SOFT else ""
                rows.append(Row("%s bullet count" % eid,
                                ">= %d per RA/CQ floor" % bf,
                                "%d bullets in Element block" % n, v, note))
            else:
                rows.append(Row("%s bullet count" % eid,
                                "floor not yet tabled for this stage",
                                "%d bullets in Element block" % n, INFO))
    else:
        # ESA / DD: per-Required-Attribute enforcement (R1/R2, 2026-06-02).
        carve = CARVE_OUT_ELEVATED.get(stage, {})
        for eid in in_scope:
            body = elements.get(eid)
            bf = bullet_floors.get(eid)
            if body is None:
                continue
            if not bf:
                rows.append(Row("%s bullet floor" % eid,
                                "floor not tabled for this stage",
                                "%d bullets in Element block" % count_bullets(body),
                                INFO))
                continue
            ra_rows, elem_total, parsed = per_ra_bullet_rows(eid, body, stage, bf)
            rows.extend(ra_rows)
            if eid in carve:
                rows.append(Row("%s carve-out elevated floor" % eid,
                                ">= %d on the fit-setup/material CQ unit(s)" % carve[eid],
                                "element total %d bullets; elevated units not "
                                "machine-identifiable" % elem_total, INFO,
                                "IA self-checks the deepened unit(s) at the elevated floor"))

    # element word floors (Triaging has explicit ones)
    elem_word_floors = ELEMENT_WORD_FLOOR.get(stage, {})
    for eid, ewf in elem_word_floors.items():
        body = elements.get(eid)
        if body is None:
            continue
        w = word_count(body)
        if w < ewf:
            v = HARD
        elif w < ewf * (1 + THIN_MARGIN):
            v = SOFT
        else:
            v = PASS
        rows.append(Row("%s word count" % eid, ">= %d" % ewf, "%d" % w, v))

    # ---- 3. Stage-scope completeness ----
    missing = [e for e in in_scope if e not in elements]
    if missing:
        rows.append(Row("Stage-scope completeness (in-scope Elements present)",
                        "all of: %s" % ", ".join(in_scope),
                        "MISSING: %s" % ", ".join(missing), HARD,
                        "in-scope Element(s) absent from the memo"))
    else:
        rows.append(Row("Stage-scope completeness (in-scope Elements present)",
                        "all of: %s" % ", ".join(in_scope),
                        "all present", PASS))
    # scope-creep: out-of-scope Elements written substantively
    out_of_scope_written = []
    for eid, body in elements.items():
        if eid not in in_scope:
            if word_count(body) > 120 and not mentions_not_applicable(memo_text, eid):
                out_of_scope_written.append(eid)
    if out_of_scope_written:
        rows.append(Row("Stage-scope discipline (no scope-creep)",
                        "out-of-stage Elements only as 'not applicable'",
                        "SUBSTANTIVE OUT-OF-SCOPE: %s" % ", ".join(out_of_scope_written),
                        HARD, "out-of-stage Element(s) written substantively"))
    else:
        rows.append(Row("Stage-scope discipline (no scope-creep)",
                        "out-of-stage Elements only as 'not applicable'",
                        "no scope-creep detected", PASS))

    # ---- 4. Validator gates ----
    validator = meta.get("validator", {})
    if validator.get("ran"):
        for gate in validator.get("gates", []):
            res = str(gate.get("result", "")).upper()
            v = PASS if res in ("PASS", "OK", "GREEN") else HARD
            rows.append(Row("Validator gate: %s" % gate.get("name", "?"),
                            "PASS", gate.get("result", "?"), v))
    else:
        rows.append(Row("Validator gates", "validator run on the memo",
                        "validator output not supplied", SOFT,
                        "validator metadata missing - supply validator output to the script"))

    # ---- 5. Communication-discipline compliance ----
    bluf_ok, bluf_detail = check_three_layer_bluf(memo_text)
    rows.append(Row("Three-layer BLUF present (page / section / closing)",
                    "all three layers",
                    "page=%s, italic-layer lines=%d" % (
                        bluf_detail["page_bluf"], bluf_detail["italic_layer_count"]),
                    PASS if bluf_ok else HARD))

    grade_total, _ = check_grades_present(memo_text)
    rows.append(Row("A-F grades present on rated units",
                    ">= one grade token per rated unit",
                    "%d grade tokens found" % grade_total,
                    PASS if grade_total >= len(in_scope) else HARD))

    inv_unique, inv_count = check_invalid_grades(memo_text)
    rows.append(Row("No invalid grade tokens (Phase-A R1)",
                    "only [A][B][C][D][F][NR]; no [E] or +/- modifiers",
                    "clean" if not inv_unique
                    else "%d token(s): %s" % (inv_count, ", ".join(inv_unique[:6])),
                    PASS if not inv_unique else HARD,
                    "" if not inv_unique
                    else "remove [E] (not in A-F system) and all [X+]/[X-] modifier variants"))

    cv_missing = check_counter_view(elements, in_scope)
    rows.append(Row("'Counter-view considered' on every in-scope Element",
                    "present on every in-scope Element",
                    "all present" if not cv_missing
                    else "MISSING on: %s" % ", ".join(cv_missing),
                    PASS if not cv_missing else HARD))

    banned = check_banned_phrases(memo_text)
    rows.append(Row("No banned buzzwords / hedging / meta-framing",
                    "zero hits",
                    "clean" if not banned
                    else "%d hit(s): %s" % (
                        len(banned), "; ".join(p for p, _ in banned[:4])),
                    PASS if not banned else HARD))

    ic_unique, ic_count = check_internal_codes(memo_text)
    rows.append(Row("No internal workstream codes in memo body (Phase-A R4)",
                    "zero Watson-coined codes (SA05, TCM06 etc.)",
                    "clean" if not ic_unique
                    else "%d code(s): %s" % (ic_count, ", ".join(ic_unique[:6])),
                    PASS if not ic_unique else SOFT,
                    "" if not ic_unique
                    else "remove internal codes; must not appear in text visible to Richard"))

    emdash = check_emdash_in_bullets(memo_text)
    rows.append(Row("No em-dashes inside bullets",
                    "zero",
                    "clean" if not emdash
                    else "%d bullet(s) with em-dash" % len(emdash),
                    PASS if not emdash else HARD))

    trailing = check_trailing_period_bullets(memo_text)
    rows.append(Row("No trailing periods on bullets",
                    "zero",
                    "clean" if not trailing
                    else "%d bullet(s) end in a period" % len(trailing),
                    PASS if not trailing else HARD))

    # ---- 5a-reform. Format reform checks (D-AJ-21, 2026-06-16) ----
    no_prose = check_no_prose(sections)
    rows.append(Row("No prose paragraphs (D-AJ-21)",
                    "every body block a bullet/heading/table/list; summaries bulleted",
                    "clean" if not no_prose
                    else "%d prose block(s): %s" % (len(no_prose), " | ".join(no_prose[:3])),
                    PASS if not no_prose else HARD,
                    "" if not no_prose else "convert prose to bullets + nested sub-bullets"))

    over_ceiling = check_bullet_ceiling(sections)
    rows.append(Row("40-word bullet ceiling (D-AJ-21 / C1)",
                    "every body bullet <= 40 words",
                    "clean" if not over_ceiling
                    else "%d bullet(s) over 40w: %s" % (len(over_ceiling), " | ".join(over_ceiling[:3])),
                    PASS if not over_ceiling else HARD,
                    "" if not over_ceiling else "split each over-length bullet into parent + sub-bullets"))

    cq_missing = check_cq_ratings(memo_text)
    rows.append(Row("CQ ratings on judgement-bearing Core Questions (D-AJ-21)",
                    "every CQ carries [A]-[F] or a [factual] tag",
                    "all CQs graded/tagged" if not cq_missing
                    else "%d CQ(s) missing grade/[factual]: %s" % (len(cq_missing), " | ".join(cq_missing[:3])),
                    PASS if not cq_missing else HARD,
                    "" if not cq_missing else "grade each judgement CQ [A]-[F]; tag factual CQs [factual]"))

    cq_no_answer = check_cq_answer_clauses(memo_text)
    rows.append(Row("CQ answer clause on every graded Core Question bullet (F5, D-AJ-27)",
                    ">=3-word answer clause after **label** on each graded CQ",
                    "all graded CQs carry an answer clause" if not cq_no_answer
                    else "%d CQ(s) missing answer clause: %s" % (
                        len(cq_no_answer), " | ".join(x[0] for x in cq_no_answer[:4])),
                    PASS if not cq_no_answer else HARD,
                    "" if not cq_no_answer else (
                        "add a one-line answer clause after **label**: "
                        "- **E# RA# CQ<n> — question? [X]** Net: answer here.")))

    acr_uniq, acr_n = check_acronym_descriptions(memo_text)
    rows.append(Row("Acronyms/shorthand carry a description (D-AJ-21)",
                    "no bare L<n>/element-slash/cohort-code shorthand",
                    "clean" if not acr_uniq
                    else "%d shorthand token(s): %s" % (acr_n, ", ".join(acr_uniq[:6])),
                    PASS if not acr_uniq else SOFT,
                    "" if not acr_uniq else "spell out shorthand with a plain-English description"))

    # ---- 5a-v2. Emphasis + signposting + spell-out HARD gates (D-AJ-24) ----
    ul_pct, ul_w, ul_tot = check_underline_hard(sections)
    _ul_ok = UNDERLINE_FLOOR_PCT <= ul_pct <= UNDERLINE_CAP_PCT
    rows.append(Row("Underline density 15-25%% of bullet words (F1, D-AJ-29)",
                    "15-25%%",
                    "%.0f%% (%d/%d words underlined)" % (ul_pct*100, ul_w, ul_tot),
                    PASS if _ul_ok else HARD,
                    "" if _ul_ok else (
                        "underline more: (__text__)" if ul_pct < UNDERLINE_FLOOR_PCT
                        else "over-underlined: reduce to <=25%% of bullet words")))

    hl_pct, hl_n, hl_tot = check_highlight_hard(sections)
    _hl_ok = HIGHLIGHT_FLOOR_PCT <= hl_pct <= HIGHLIGHT_CAP_PCT
    rows.append(Row("Sentiment highlight 30-40%% of bullets (F2, D-AJ-29)",
                    "30-40%%",
                    "%.0f%% (%d/%d bullets highlighted)" % (hl_pct*100, hl_n, hl_tot),
                    PASS if _hl_ok else HARD,
                    "" if _hl_ok else (
                        "add ==+pos==/==-neg== highlights" if hl_pct < HIGHLIGHT_FLOOR_PCT
                        else "too many highlights: reduce to <=40%% of bullets")))

    it_pct, it_n, it_tot = check_italic_hard(sections)
    _it_ok = ITALIC_FLOOR_PCT <= it_pct <= ITALIC_CAP_PCT
    rows.append(Row("Italic emphasis 15-25%% of bullets (F3, D-AJ-29)",
                    "15-25%%",
                    "%.0f%% (%d/%d bullets italicised)" % (it_pct*100, it_n, it_tot),
                    PASS if _it_ok else HARD,
                    "" if _it_ok else (
                        "italicise more: (*text*)" if it_pct < ITALIC_FLOOR_PCT
                        else "over-italicised: reduce to <=25%% of bullets")))

    sign_bad = check_signposting(sections)
    rows.append(Row("Every bullet signposted with a bold label (F13)",
                    "every body bullet opens with **label**",
                    "all signposted" if not sign_bad
                    else "%d unsignposted: %s" % (len(sign_bad), " | ".join(sign_bad[:3])),
                    PASS if not sign_bad else HARD,
                    "" if not sign_bad else "open every bullet (and sub-bullet) with a bold signpost label"))

    cap_bad = check_bullet_capitalisation(sections)
    rows.append(Row("Bullets start with a capital letter (F11)",
                    "every bullet capitalised",
                    "clean" if not cap_bad
                    else "%d lower-case: %s" % (len(cap_bad), " | ".join(cap_bad[:3])),
                    PASS if not cap_bad else HARD,
                    "" if not cap_bad else "capitalise the first word of each bullet; re-nest stray fragments"))

    spo_uniq, spo_n = check_spellout_hard(memo_text)
    rows.append(Row("Element codes spelled out, no bare shorthand (F14)",
                    "no 'E8 verdict'/'E9/E10'/'L4' shorthand",
                    "clean" if not spo_uniq
                    else "%d shorthand: %s" % (spo_n, ", ".join(spo_uniq[:6])),
                    PASS if not spo_uniq else HARD,
                    "" if not spo_uniq else "name the element every time, e.g. 'Element E8 (Fit with acceptable case setups) verdict'"))

    # ---- 5b. New discipline checks (R3/R4, 2026-06-02) ----
    da_fails = check_downstream_actions(elements, in_scope, stage=stage, sections=sections)
    rows.append(Row("Two downstream actions per in-scope Element (G19)",
                    ">= 2 actions per in-scope Element",
                    "all present" if not da_fails
                    else "short/absent on: %s" % ", ".join(da_fails),
                    PASS if not da_fails else SOFT,
                    "" if not da_fails else "add the two next-actions block"))

    anchor_missing = check_cohort_anchor(elements, in_scope)
    rows.append(Row("Cohort / peer anchor on each in-scope Element grade (D-IA-4RR-09)",
                    "cohort/peer/base-rate anchor present per in-scope Element",
                    "all anchored" if not anchor_missing
                    else "no anchor detected on: %s" % ", ".join(anchor_missing),
                    PASS if not anchor_missing else SOFT,
                    "" if not anchor_missing else "strike each grade vs the live cohort"))

    df_ok, df_note = check_df_before_ab_bluf(sections, elements, in_scope)
    rows.append(Row("D/F findings surfaced before A/B in the BLUF (G8)",
                    "worst news first in the executive summary",
                    df_note, PASS if df_ok else SOFT,
                    "" if df_ok else "re-order the BLUF to lead with D/F findings"))

    infl = check_grade_rollup(elements, in_scope)
    rows.append(Row("Grade roll-up sanity (headline vs sub-grade mean, R4)",
                    "headline grade within ~1 notch of its sub-grade mean",
                    "no inflation detected" if not infl
                    else "possible inflation: %s" % "; ".join(infl),
                    PASS if not infl else SOFT,
                    "" if not infl else "re-justify the headline grade or lower it"))

    # ---- 5c. V4.3 redesign structural compliance (Opus 2026-06-12) ----
    if check_section_a_heading(memo_text):
        rows.append(Row("Section A 'Summary Snapshot' heading (R3)",
                        "Section A - Summary Snapshot", "present", PASS))
    else:
        rows.append(Row("Section A 'Summary Snapshot' heading (R3)",
                        "Section A - Summary Snapshot",
                        "MISSING / non-canonical heading", HARD,
                        "Section A must use the exact redesign heading"))

    a_brevity_violations = check_section_a_brevity(sections)
    rows.append(Row("Section A field values <= 80 chars each (Phase-A R5)",
                    "every field value <= 80 characters",
                    "clean" if not a_brevity_violations
                    else "%d field(s) over 80 chars: %s" % (
                        len(a_brevity_violations),
                        "; ".join(a_brevity_violations[:3])),
                    PASS if not a_brevity_violations else SOFT,
                    "" if not a_brevity_violations
                    else "shorten Section A field values to <= 80 chars for clean hero tiles"))

    b_present, b_missing = check_b_subsections(memo_text)
    rows.append(Row("Executive Summary B.1-B.6 subsections (B4-B6)",
                    "all of B.1-B.6 present",
                    ("present: " + ", ".join(b_present)) if not b_missing
                    else ("MISSING: " + ", ".join(b_missing)),
                    PASS if not b_missing else HARD,
                    "" if not b_missing else "add the missing Executive-Summary subsections"))

    mr_found = check_mr_headings(memo_text)
    rows.append(Row("Six Master-Rating headings MR1-MR6 (B2/B3)",
                    "MR1-MR6 present",
                    ("found: " + ", ".join(mr_found)) if len(mr_found) >= 6
                    else ("only %d: %s" % (len(mr_found), ", ".join(mr_found))),
                    PASS if len(mr_found) >= 6 else HARD))

    bq_total, bq_missing = check_blockquote_summaries(memo_text, sections, stage)
    if bq_total == 0:
        rows.append(Row("Blockquote summary blocks (C6 / R8)",
                        "'> ' summary at every container",
                        "ZERO blockquotes - no summary mechanism present", HARD,
                        "every Section/Element must open with a '> ' summary"))
    elif bq_missing:
        rows.append(Row("Blockquote summary blocks (C6 / R8)",
                        "'> ' summary opening every major Section",
                        "%d total, Section(s) without one: %s" % (bq_total, ", ".join(bq_missing)),
                        HARD, "add a '> ' summary at the top of each flagged Section"))
    else:
        rows.append(Row("Blockquote summary blocks (C6 / R8)",
                        "'> ' summary opening every major Section",
                        "%d blockquotes, all major Sections covered" % bq_total, PASS))

    js_hits = check_judgement_summary_labels(memo_text)
    rows.append(Row("No '**JUDGEMENT SUMMARY' labels (C6 deprecation)",
                    "zero bold JUDGEMENT SUMMARY labels",
                    "clean" if not js_hits else "%d banned label(s)" % js_hits,
                    PASS if not js_hits else HARD,
                    "" if not js_hits else "remove the deprecated label; blockquote is the only summary"))

    gng_found, gng_detail = check_gng_present(meta)
    if gng_found is None:
        rows.append(Row("Go-No-Go Checks artefact paired (SOP-04)",
                        "GNG one-pager in the memo folder", gng_detail, INFO,
                        "pass the memo path so the audit can check"))
    else:
        rows.append(Row("Go-No-Go Checks artefact paired (SOP-04)",
                        "GNG one-pager in the memo folder", gng_detail,
                        PASS if gng_found else HARD,
                        "" if gng_found else "author the paired Go-No-Go Checks one-pager"))

    # --- ratings.json check (Phase-A R2) ---
    rj_exists, rj_key_ok, rj_detail = check_ratings_json(meta)
    if rj_exists is None:
        rows.append(Row("ratings.json present with correct ticker key (Phase-A R2)",
                        "ratings.json in folder, parseable, ticker key present",
                        rj_detail, INFO, "pass the memo path so the audit can check"))
    elif not rj_exists:
        rows.append(Row("ratings.json present with correct ticker key (Phase-A R2)",
                        "ratings.json in folder, parseable, ticker key present",
                        rj_detail, HARD, "create ratings.json in the memo folder"))
    elif rj_key_ok is None:
        rows.append(Row("ratings.json present with correct ticker key (Phase-A R2)",
                        "ratings.json in folder, parseable, ticker key present",
                        rj_detail, SOFT, "supply ticker in meta to validate the key"))
    elif not rj_key_ok:
        rows.append(Row("ratings.json present with correct ticker key (Phase-A R2)",
                        "ratings.json in folder, parseable, ticker key present",
                        rj_detail, HARD,
                        "fix the ticker key in ratings.json to match the meta ticker"))
    else:
        rows.append(Row("ratings.json present with correct ticker key (Phase-A R2)",
                        "ratings.json in folder, parseable, ticker key present",
                        rj_detail, PASS))

    # --- Cross-artefact consistency (Phase-A R3) ---
    xart_ok, xart_detail = check_cross_artefact(memo_text, meta)
    if xart_ok is None:
        rows.append(Row("Cross-artefact grade consistency memo vs ratings.json (Phase-A R3)",
                        "MR1-MR6 grades agree between memo body and ratings.json",
                        xart_detail, INFO,
                        "ensure memo path and ticker are in meta for this check"))
    elif xart_ok:
        rows.append(Row("Cross-artefact grade consistency memo vs ratings.json (Phase-A R3)",
                        "MR1-MR6 grades agree between memo body and ratings.json",
                        xart_detail, PASS))
    else:
        rows.append(Row("Cross-artefact grade consistency memo vs ratings.json (Phase-A R3)",
                        "MR1-MR6 grades agree between memo body and ratings.json",
                        xart_detail, SOFT,
                        "reconcile grade conflict between memo body and ratings.json before shipping"))

    # ---- 6. Presentation-discipline compliance ----
    html_tbl = check_html_tables(memo_text)
    rows.append(Row("Pipe tables only (no HTML tables)",
                    "zero HTML tables",
                    "HTML table found" if html_tbl else "clean",
                    HARD if html_tbl else PASS))

    descent = check_header_descent(memo_text)
    rows.append(Row("Header hierarchy - no gross skips",
                    "no jump of 3+ levels at once",
                    "clean" if not descent
                    else "%d gross-skip transition(s)" % len(descent),
                    PASS if not descent else SOFT,
                    "" if not descent
                    else "header rendering is partly judgement-dependent - soft flag, not a block"))

    ul_issues = check_underline_density(sections)
    if not ul_issues:
        rows.append(Row("Underline density ~20% per section (Phase-A R6)",
                        "12-30% of section words underlined (__text__)",
                        "all substantive sections in range", PASS))
    else:
        for (sec_label, pct_val, flag_desc, total_w, ul_w) in ul_issues:
            rows.append(Row(
                "Underline density ~20%% - %s (Phase-A R6)" % sec_label,
                "12-30% of section words underlined",
                "%s: %.0f%% (%d/%d words)" % (flag_desc, pct_val * 100, ul_w, total_w),
                SOFT,
                "adjust underline density toward ~20%%; "
                "add __text__ spans if low; reduce if high"))

    # Legacy sentence-level sentiment check RETIRED (doc 10 L4, D-AJ-24 supersedes):
    # the HARD bullet-level highlight gate (F2 above) now owns this check. Keeping
    # the call in case callers read it externally, but no row emitted here.
    # pct, spans, sents = check_sentiment_highlight(...)  # retired 2026-06-17

    if stage in ("esa", "dd"):
        has_dii, has_ten = check_invalidation_thresholds(memo_text)
        ok = has_dii and has_ten
        rows.append(Row("10 Invalidation thresholds verbatim at D.II",
                        "present, 10 items, verbatim",
                        "D.II heading=%s, ten-item list near it=%s" % (has_dii, has_ten),
                        PASS if ok else HARD))
        has_driver = check_driver_tables(memo_text)
        rows.append(Row("7-column driver tables (upstream + downstream)",
                        "present at ESA/DD",
                        "found" if has_driver else "NOT found",
                        PASS if has_driver else HARD))

    if stage == "dd":
        hs, hc = check_sensitivity_scenario(memo_text)
        rows.append(Row("Sensitivity + scenario tables (D.IV, Deep Dive)",
                        "both present (presence check; numbers are IA/FA content)",
                        "sensitivity=%s, scenario=%s" % (hs, hc),
                        PASS if (hs and hc) else SOFT,
                        "" if (hs and hc) else "add the D.IV sensitivity and/or scenario table"))

    # Section D presence by stage
    d_expected = SECTION_D_EXPECTED.get(stage)
    d_body = sections.get("D", "")
    d_words = word_count(d_body)
    if d_expected == "zero":
        if d_words > 150:
            rows.append(Row("Section D content level", "zero content at Triaging",
                            "%d words" % d_words, HARD,
                            "Section D should be zero-content at Triaging"))
        else:
            rows.append(Row("Section D content level", "zero content at Triaging",
                            "%d words (note-only)" % d_words, PASS))
    else:
        rows.append(Row("Section D content level",
                        "%s at %s" % (d_expected, STAGE_LABEL[stage]),
                        "%d words" % d_words, INFO,
                        "depth is judgement-dependent - deferred to the Investment Analyst"))

    # --- Decimal precision advisory (Phase-A R7) ---
    dec_hits = check_decimal_advisory(memo_text)
    rows.append(Row("Decimal precision advisory (Phase-A R7)",
                    "3+ decimal-place numbers flagged for IA review",
                    "none" if not dec_hits
                    else "%d number(s) with 3+ dp: %s" % (
                        len(dec_hits), ", ".join(dec_hits[:5])),
                    INFO,
                    "review whether 3+ decimal places are warranted; trim where not"))

    # ---- 7. Source provenance and vintage ----
    # 4-report era: research_reports[] may carry family bulk reports (kind="family",
    # AlphaSense-only by design) and IA-initiated follow-up queries (kind="ia-initiated").
    reports = meta.get("research_reports", [])
    family_reports = [r for r in reports
                      if r.get("kind") == "family" or r.get("family")]
    ia_reports = [r for r in reports if r.get("kind") == "ia-initiated"]
    # Backward-compat: if no kind/family markers at all, treat every entry as bulk.
    if reports and not family_reports and not ia_reports:
        family_reports = reports
    if reports:
        dates = [r.get("date") for r in reports if r.get("date")]
        dates_sorted = sorted(dates)
        spread = ("%s -> %s" % (dates_sorted[0], dates_sorted[-1])
                  if dates_sorted else "no dates supplied")
        unconfirmed = [r.get("family", r.get("name", "?")) for r in family_reports
                       if not r.get("identity_confirmed")]
        idnote = ("all family reports identity-confirmed"
                  if family_reports and not unconfirmed
                  else ("identity unconfirmed: %s" % ", ".join(unconfirmed[:4])
                        if unconfirmed else "no family reports listed"))
        rows.append(Row("Source provenance (research reports listed)",
                        "every in-scope report listed with source + date; family reports identity-confirmed",
                        "%d report(s) (%d family, %d IA-initiated); vintage %s; %s" % (
                            len(reports), len(family_reports), len(ia_reports),
                            spread, idnote),
                        PASS if (dates_sorted and not unconfirmed) else SOFT,
                        "" if (dates_sorted and not unconfirmed)
                        else "supply dates and identity_confirmed for each family report"))
    else:
        rows.append(Row("Source provenance (research reports listed)",
                        "every in-scope report listed",
                        "research report metadata not supplied", SOFT,
                        "supply research_reports[] to the script"))

    # ---- 8. Dual-source coverage (IA-initiated queries only) ----
    # The 4 bulk family reports are AlphaSense-only BY DESIGN (no Claude side), so the
    # DEFAULT-to-BOTH [C]+[AS] rule applies ONLY to IA-initiated follow-up research.
    if ia_reports:
        single_source = [r.get("name", "?") for r in ia_reports
                         if str(r.get("source", "")).upper() not in ("C/AS", "AS/C")]
        if single_source:
            rows.append(Row("Dual-source coverage (IA-initiated [C]+[AS])",
                            "DEFAULT-to-BOTH unless stated justification",
                            "%d single-source IA-initiated query(ies): %s" % (
                                len(single_source), ", ".join(single_source[:4])),
                            SOFT,
                            "single-source gaps - confirm each carries a stated justification"))
        else:
            rows.append(Row("Dual-source coverage (IA-initiated [C]+[AS])",
                            "DEFAULT-to-BOTH", "all IA-initiated queries dual-sourced", PASS))
    else:
        rows.append(Row("Dual-source coverage (IA-initiated [C]+[AS])",
                        "applies to IA-initiated queries only",
                        "no IA-initiated queries; bulk family reports AlphaSense-by-design",
                        PASS))

    # ---- 9. Wisdom Library models applied ----
    models = meta.get("wisdom_library_models", [])
    shaped = [m for m in models if m.get("shaped_judgement")]
    if not models:
        rows.append(Row("Wisdom Library models applied",
                        ">= 1 in a substantive memo",
                        "zero models recorded", SOFT,
                        "empty model list in a substantive memo is suspicious"))
    else:
        rows.append(Row("Wisdom Library models applied",
                        ">= 1 in a substantive memo",
                        "%d consulted, %d shaped a judgement" % (len(models), len(shaped)),
                        PASS))

    # ---- 10. Self-initiated research log ----
    queries = meta.get("self_initiated_queries", [])
    n_q = len(queries)
    if n_q > 5:
        rows.append(Row("Self-initiated research query count",
                        "1-5 expected; 6+ signals a section 2 consult",
                        "%d queries" % n_q, HARD,
                        "6+ queries - a section 2 mid-flight consult should have fired"))
    else:
        rows.append(Row("Self-initiated research query count",
                        "1-5 expected band", "%d queries" % n_q, PASS))
    if queries:
        ss_q = [q for q in queries if not q.get("dual_source")]
        if ss_q:
            rows.append(Row("Self-initiated queries dual-sourced",
                            "DEFAULT-to-BOTH unless justified",
                            "%d single-source quer(y/ies)" % len(ss_q), SOFT))
        else:
            rows.append(Row("Self-initiated queries dual-sourced",
                            "DEFAULT-to-BOTH", "all dual-sourced", PASS))

    # ---- 11. Mid-flight consults log ----
    consults = meta.get("midflight_consults", [])
    rows.append(Row("Mid-flight PM consults logged",
                    "every section 2 consult recorded with Richard's response",
                    "%d consult(s) logged" % len(consults), INFO,
                    "informational - consult frequency is loose by design"))

    # ---- 12. Data discrepancies flagged ----
    discrepancies = meta.get("data_discrepancies", [])
    rows.append(Row("Data discrepancies flagged (not silently resolved)",
                    "surfaced, not buried",
                    "%d discrepanc(y/ies) flagged" % len(discrepancies)
                    if discrepancies else "none recorded",
                    INFO, "informational record - never a fail"))

    # ---- 13. Go-No-Go Checks artefact -- question-count FORMAT only ----
    # Presence/pairing is gated authoritatively by the file-based check in 5c
    # above. This row validates the 6-10 question-count FORMAT, and only when the
    # IA supplies go_no_go metadata; absent metadata DEFERS (INFO), never HARD,
    # so it never double-counts or false-fails a memo whose GNG file is present.
    gng = meta.get("go_no_go", {})
    if not gng:
        rows.append(Row("Go-No-Go Checks - 6-10 question format",
                        "6-10 stack-ranked questions (checked when meta supplied)",
                        "go_no_go metadata not supplied (presence gated by file check above)",
                        INFO, "supply go_no_go metadata to validate the question count"))
    else:
        qc = gng.get("question_count", 0)
        paired = gng.get("paired", False)
        if paired and 6 <= qc <= 10:
            rows.append(Row("Go-No-Go Checks - 6-10 question format",
                            "present, paired, 6-10 questions",
                            "present, paired, %d questions" % qc, PASS))
        else:
            rows.append(Row("Go-No-Go Checks - 6-10 question format",
                            "present, paired, 6-10 questions",
                            "present=%s, paired=%s, questions=%s" % (
                                gng.get("present"), paired, qc), HARD,
                            "Go-No-Go present but outside the 6-10 stack-ranked format"))

    # ---- 14. Known limitations roll-up ----
    limitations = []
    if not validator.get("ran"):
        limitations.append("validator output not supplied to the script")
    if not reports:
        limitations.append("research report metadata not supplied")
    # render_target_supports_sentiment limitation retired (doc 10 L4, 2026-06-17):
    # the D-AJ-24 HARD highlight gate (F2) supersedes the sentence-level sentinel.
    if not models:
        limitations.append("Wisdom Library model list empty")
    limitations_txt = ("; ".join(limitations) if limitations
                       else "none - full metadata supplied")
    rows.append(Row("Known limitations (what the audit could not check)",
                    "full metadata supplied",
                    limitations_txt, SOFT if limitations else PASS,
                    "roll-up row - informational"))

    return rows, sections, elements


# --------------------------------------------------------------------------
# Narrative generation (deterministic, templated from the rows)
# --------------------------------------------------------------------------
def generate_narrative(rows, stage, meta):
    hard = [r for r in rows if r.verdict == HARD]
    soft = [r for r in rows if r.verdict == SOFT]
    passes = [r for r in rows if r.verdict == PASS]

    lines = []
    lines.append("### Quality Control Audit - narrative")
    lines.append("")

    # Headline verdict
    if hard:
        lines.append("**Headline verdict: GATED - %d HARD FAIL%s open.** "
                     "The memo does not yet clear the Quality Control Audit. "
                     "%d soft flag%s also recorded. "
                     "Phase 4 close-out cannot proceed until the hard fails are fixed "
                     "and the audit re-run clean." % (
                         len(hard), "s" if len(hard) != 1 else "",
                         len(soft), "s" if len(soft) != 1 else ""))
    else:
        lines.append("**Headline verdict: PASS - zero HARD FAILs.** "
                     "The memo clears the Quality Control Audit. "
                     "%d soft flag%s recorded for awareness; soft flags do not block "
                     "close-out." % (len(soft), "s" if len(soft) != 1 else ""))
    lines.append("")

    # What the audit checked
    lines.append("**What the audit checked.** "
                 "Word-count floors (whole-memo and per-section), per-Element bullet "
                 "and word floors, stage-scope completeness and scope-creep, validator "
                 "gates, the mechanically-checkable subset of the Communicating SOP "
                 "(three-layer BLUF, A-F grades, counter-view coverage, banned phrases, "
                 "em-dashes in bullets, trailing periods) and the Presenting SOP "
                 "(HTML tables, header descent, sentiment highlighting, Invalidation "
                 "thresholds, driver tables), source provenance and vintage, dual-source "
                 "coverage, Wisdom Library models applied, the self-initiated research "
                 "log, mid-flight consults, data discrepancies, and the Go-No-Go Checks "
                 "artefact. Stage audited: %s." % STAGE_LABEL.get(stage, stage))
    lines.append("")

    # Where the memo performed well
    if passes:
        lines.append("**Where the memo performed well.**")
        highlight = []
        for r in passes:
            if "word count" in r.dimension.lower() and r.standard.startswith(">="):
                highlight.append("- %s: %s against a %s floor - clear." % (
                    r.dimension, r.actual, r.standard))
            elif "bullet count" in r.dimension.lower() and r.standard.startswith(">="):
                highlight.append("- %s: %s, %s - clear." % (
                    r.dimension, r.actual, r.standard))
        discipline_passes = [r for r in passes
                             if "word count" not in r.dimension.lower()
                             and "bullet count" not in r.dimension.lower()]
        for r in discipline_passes[:6]:
            highlight.append("- %s: %s." % (r.dimension, r.actual))
        if not highlight:
            highlight.append("- (no quantitative pass rows to surface)")
        lines.extend(highlight)
        lines.append("")

    # Where the memo is light or borderline
    if soft:
        lines.append("**Where the memo is light or borderline.** "
                     "These passed or are inherent flags - none blocks close-out - "
                     "but each is worth Richard's eye:")
        for r in soft:
            note = " - %s" % r.note if r.note else ""
            lines.append("- %s: %s (standard: %s)%s." % (
                r.dimension, r.actual, r.standard, note))
        lines.append("")

    # Hard fails and the fix loop
    if hard:
        lines.append("**Hard fails and the fix loop.** "
                     "Each row below blocks Phase 4 close-out. The Investment Analyst "
                     "must go back and fix the underlying problem in the memo - fixing "
                     "the analysis, not gaming the check - then re-run the audit, and "
                     "repeat until the audit is clean of hard fails:")
        for r in hard:
            note = " - %s" % r.note if r.note else ""
            lines.append("- %s: actual %s vs standard %s%s." % (
                r.dimension, r.actual, r.standard, note))
        lines.append("")

    # Significance read
    if hard:
        sig = ("This memo has a structural compliance problem: %d hard fail%s "
               "against the SOP standards. It is not ready for close-out. The fix "
               "loop is mandatory - the hot wash and the self-review debrief proper "
               "are written against the fixed memo, not this one." % (
                   len(hard), "s" if len(hard) != 1 else ""))
    elif len(soft) >= 5:
        sig = ("This memo clears every hard check, but the number of soft flags "
               "(%d) says it is running close to its floors and standards in "
               "several places rather than comfortably clear. Worth a read of the "
               "soft-flag rows above before leaning hard on the memo." % len(soft))
    elif soft:
        sig = ("This is a comfortably-compliant memo. It clears every hard check "
               "and carries only %d soft flag%s - the kind of honest, inherent "
               "'flagged not papered over' item the self-review debrief is built "
               "to carry. No compliance concern." % (
                   len(soft), "s" if len(soft) != 1 else ""))
    else:
        sig = ("This is a cleanly-compliant memo - every hard check passes and "
               "there are no soft flags. The memo met its floors and disciplines "
               "with margin. No compliance concern.")
    lines.append("**Significance read.** " + sig)
    lines.append("")

    return "\n".join(lines)


# --------------------------------------------------------------------------
# Table rendering
# --------------------------------------------------------------------------
def render_table(rows):
    out = []
    out.append("### Quality Control Audit - table")
    out.append("")
    out.append("| Dimension | Standard | Actual | Verdict | Note |")
    out.append("|---|---|---|---|---|")
    for r in rows:
        note = r.note.replace("|", "/") if r.note else ""
        dim = r.dimension.replace("|", "/")
        std = r.standard.replace("|", "/")
        act = r.actual.replace("|", "/")
        out.append("| %s | %s | %s | **%s** | %s |" % (dim, std, act, r.verdict, note))
    out.append("")
    hard = sum(1 for r in rows if r.verdict == HARD)
    soft = sum(1 for r in rows if r.verdict == SOFT)
    pas = sum(1 for r in rows if r.verdict == PASS)
    info = sum(1 for r in rows if r.verdict == INFO)
    out.append("**Tally:** %d PASS - %d HARD FAIL - %d SOFT FLAG - %d INFO - "
               "%d rows total." % (pas, hard, soft, info, len(rows)))
    out.append("")
    return "\n".join(out)


def render_section7(rows, stage, meta):
    ticker = meta.get("ticker", "{ticker}")
    memo_date = meta.get("memo_date", "{date}")
    hard = sum(1 for r in rows if r.verdict == HARD)

    header = []
    header.append("## section 7 - Quality Control Audit")
    header.append("")
    header.append("*Auto-generated by `generate_qc_audit.py` from the memo's own "
                  "content and metadata - NOT Investment Analyst self-report. "
                  "Memo: %s %s A&J memo, %s.*" % (
                      ticker, STAGE_LABEL.get(stage, stage), memo_date))
    header.append("")
    status = ("GATED - fix loop required" if hard
              else "PASS - clear of hard fails")
    header.append("**Audit status: %s.**" % status)
    header.append("")
    body = render_table(rows) + "\n" + generate_narrative(rows, stage, meta)
    return "\n".join(header) + body + "\n"


# --------------------------------------------------------------------------
# Metadata type hardening (F3, 2026-06-15 — KPN test friction)
# --------------------------------------------------------------------------
def _coerce_meta_types(meta):
    """The metadata sidecar is agent-assembled JSON; it may be valid JSON but
    carry the wrong TYPE for a field (e.g. research_reports as a string, or
    go_no_go as a list). Before this guard such a type error crashed the audit
    mid-run. Coerce each expected field to its safe type so a malformed field
    degrades to an INFO/limitation row, never a crash."""
    for k in ("research_reports", "wisdom_library_models",
              "self_initiated_queries", "midflight_consults", "data_discrepancies"):
        if k in meta and not isinstance(meta[k], list):
            meta[k] = []
    for k in ("validator", "go_no_go"):
        if k in meta and not isinstance(meta[k], dict):
            meta[k] = {}
    v = meta.get("validator")
    if isinstance(v, dict) and "gates" in v and not isinstance(v["gates"], list):
        v["gates"] = []
    return meta


# --------------------------------------------------------------------------
# Render + Visual QC gate (Station 3) -- triggered from main(), folded into rows
# --------------------------------------------------------------------------
def append_render_qc_row(rows, memo_path, stage, meta, mode):
    """Trigger render_qc_gate.py and append its verdict as a Row so it counts in
    the HARD-fail tally and the exit code. mode is 'on' or 'off'.

    PASS        -> PASS row.
    FAIL        -> HARD row (the viewer is broken; fix the memo).
    UNAVAILABLE -> HARD row (render could not run; environment, re-run when warm).
                   We BLOCK rather than wave through, because the whole point of
                   the gate is that an unattended run cannot ship an unrendered
                   memo. The note flags it as an environment retry, not a rewrite.
    """
    dim = "Render + visual QC (headless viewer render)"
    std = "viewer builds, structure intact, paints clean with no errors"
    if mode == "off":
        rows.append(Row(dim, std,
                        "render-QC skipped (--render-qc off; intermediate fix-loop only)",
                        INFO,
                        "the FINAL pre-publish audit and every unattended run must "
                        "leave render-QC ON"))
        return

    gate = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "render_qc_gate.py")
    if not os.path.isfile(gate):
        rows.append(Row(dim, std,
                        "render_qc_gate.py not found next to this script", HARD,
                        "ENVIRONMENT: render-QC could not run; install the gate and "
                        "re-run. Do not ship unrendered."))
        return

    ticker = meta.get("ticker")
    if not ticker:
        rows.append(Row(dim, std,
                        "no 'ticker' in metadata - cannot build the viewer", HARD,
                        "supply the coverage-data ticker key (e.g. KPN-NL) in metadata"))
        return

    import subprocess as _sp
    try:
        proc = _sp.run([sys.executable, gate, "--memo", str(memo_path),
                        "--ticker", str(ticker), "--stage", stage],
                       capture_output=True, text=True, timeout=240)
        result = json.loads(proc.stdout)
        if "status" not in result:
            raise ValueError("gate result missing 'status'")
    except Exception as exc:
        rows.append(Row(dim, std,
                        "render-QC gate crashed: %s: %s" % (type(exc).__name__, exc),
                        HARD,
                        "ENVIRONMENT: render-QC could not complete; re-run when the "
                        "renderer is warm. Do not ship unrendered."))
        return

    status = result.get("status")
    reason = result.get("reason", "")
    shot = result.get("screenshot", "")
    actual = reason + (("  [proof: %s]" % shot) if shot else "")
    if status == "PASS":
        rows.append(Row(dim, std, actual, PASS))
    elif status == "FAIL":
        rows.append(Row(dim, std, actual, HARD,
                        "the memo's viewer is broken; fix the memo and re-run"))
    else:
        rows.append(Row(dim, std, actual or "render-QC unavailable", HARD,
                        "ENVIRONMENT: render-QC could not run (not a memo defect); "
                        "re-run when the renderer is warm. Do not ship unrendered."))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Generate the section 7 Quality Control Audit for an A&J memo.")
    ap.add_argument("--memo", required=True, help="path to the memo markdown file")
    ap.add_argument("--stage", required=True, help="triaging | esa | dd")
    ap.add_argument("--meta", required=True,
                    help="path to the JSON sidecar metadata block")
    ap.add_argument("--out", default=None,
                    help="optional output path for the section 7 block (else stdout)")
    ap.add_argument("--render-qc", dest="render_qc", choices=("on", "off"),
                    default="on",
                    help="trigger the headless Render+Visual QC gate (default on; "
                         "pass off only for intermediate fix-loop iterations)")
    args = ap.parse_args()

    stage = normalise_stage(args.stage)

    memo_path = Path(args.memo)
    if not memo_path.is_file():
        sys.stderr.write("ERROR: memo file not found: %s\n" % memo_path)
        sys.exit(2)
    memo_text = memo_path.read_text(encoding="utf-8")

    meta_path = Path(args.meta)
    if not meta_path.is_file():
        sys.stderr.write("ERROR: metadata file not found: %s\n" % meta_path)
        sys.exit(2)
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.stderr.write("ERROR: metadata JSON is invalid: %s\n" % e)
        sys.exit(2)
    if not isinstance(meta, dict):
        sys.stderr.write("ERROR: metadata JSON must be a top-level object/dict\n")
        sys.exit(2)
    _coerce_meta_types(meta)   # F3: tolerate valid-JSON-but-wrong-type sidecars

    meta["__memo_path"] = str(memo_path)
    rows, _sections, _elements = build_rows(memo_text, stage, meta)

    # Station-3 Render + Visual QC gate (added 2026-06-15). Folds a HARD row in
    # when the memo's rendered viewer is broken/blank/unrenderable, so an
    # unattended run cannot ship a visually-broken memo. ON by default.
    append_render_qc_row(rows, memo_path, stage, meta, args.render_qc)

    section7 = render_section7(rows, stage, meta)

    if args.out:
        Path(args.out).write_text(section7, encoding="utf-8")
        sys.stderr.write("wrote section 7 block to %s\n" % args.out)
    else:
        sys.stdout.write(section7)

    hard = sum(1 for r in rows if r.verdict == HARD)
    if hard:
        sys.stderr.write("\nAUDIT GATED: %d HARD FAIL row(s). "
                         "Fix the memo and re-run.\n" % hard)
        sys.exit(1)
    sys.stderr.write("\nAUDIT CLEAN: zero HARD FAIL rows. Phase 4 may proceed.\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
