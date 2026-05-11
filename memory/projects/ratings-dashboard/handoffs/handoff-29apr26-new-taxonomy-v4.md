# Handoff — 29-Apr-26 EVE — New Taxonomy Pillar Tree V4
<!-- [W] Anti-compaction save. Full restart context. -->

```text
RESTART PROMPT — New Taxonomy Pillar Tree V4 (29-Apr-26)

Role: SYSTEMS ARCHITECT. Mode: EXECUTION. Project: RATINGS DASHBOARD.

WHAT WE BUILT THIS SESSION:
A standalone HTML pillar tree visualisation (`databases/pillar-tree-new-taxonomy.html`, 28KB) from Richard's new workbook taxonomy (`For Watson - Families - 29-Apr.xlsx`, NEW tab). This is a DIFFERENT taxonomy from the existing dashboard pillar tree — 3-tier (Element → Required Attribute → Core Question), NOT the old 4-tier schema.

CURRENT STATE OF THE FILE:
- Two pillars stacked vertically: Investment Case Elements (IC, top) and Investment Case Building Blocks (BB, below)
- IC: 4 elements run horizontally via h-spread. Attrs/CQs drop vertically below each element.
- BB: 5 groups run horizontally (equal-width columns, flex:1 1 0, no wrapping). Elements drop vertically below each group. Attrs/CQs drop vertically below each element. Long text wraps within columns.
- Numbering badges: G1-G5 (green), E1-En (brown, restart per parent), RA1-RAn (blue, per element), CQ1-CQn (grey, per attr)
- Connector lines: pillar-stem (1.5px, #bbb) connects pillar pill to h-spread. H-spread-bar drawn by JS between actual child positions (no dangling lines). V-drop rails end exactly at last child via CSS variable --vd-rail-bottom set by fixVDropRails().
- Depth controls: Groups only / + Elements / + Attributes / + Core Questions
- Totals: 18 elements / 63 RAs / 175 CQs
- All </ escaped as <\/ inside <script> block. Closing </script></body></html> NOT escaped.

V4 CHANGE (most recent):
E1 "Required input forces?" was restructured:
- Old: RA1 "Change forces?" with 2 CQs (external, internal)
- New: RA1 "Strong external change forces / tailwinds?" (7 CQs: Demand, Competition, Disruption, Political/regulatory, Supply side, Revenue/demand cycle, Macroeconomic) + RA2 "Strong internal change forces?" (5 CQs: Leadership, Strategy/structure, Priorities/ambition, Financial profile, Track record) + RA3 "Robust base?" (5 CQs, unchanged)
Source: researched from AI Prompts/Watson - IG - Change forces - REFV04_RB.docx. Section C "Key components summary" excluded (synthesis layer, agreed with Richard).

KEY FILES:
- databases/pillar-tree-new-taxonomy.html — the deliverable (28KB, V4)
- databases/new_tree_data.json — the data source (updated with V4 changes)
- databases/scripts/build_tree_v3.py — builds HTML from JSON (reads new_tree_data.json, writes pillar-tree-new-taxonomy.html)
- databases/pillar-tree-canonical.json — also updated from workbook earlier this session (12 families, 41 TCs, 62 RAs, 165 CQs — NOTE: this is the OLD canonical format, not updated with V4 CF split)
- AI Prompts/Watson - IG - Change forces - REFV04_RB.docx — CF prompt template (source for V4 CQs)

TECHNICAL LESSONS (hard-won this session):
1. </ inside <script> breaks HTML parsing — escape as <\/ (44+ occurrences)
2. Blanket </ → <\/ must NOT touch </script> closing tag — escape JS body BEFORE assembling into template
3. Edit tool truncates files >800KB — use Python Write
4. Minified JS (no linebreaks) causes statement boundary loss — always use formatted JS
5. h-spread horizontal bar must be drawn by JS (measuring actual child positions), not CSS ::before (which extends beyond children = dangling lines)
6. v-drop rail height must be set by JS (CSS variable) to end at last child's arm, not overshoot

RICHARD'S QUALITY FEEDBACK THIS SESSION:
- "It doesn't work. Really poor quality control from you." (after minified JS broke rendering)
- "Atrocious. Not working. Check your work better." (earlier iteration)
- "Great." (multiple times after fixes)
- Always test before delivering. Always verify JS executes. Always check closing tags.

PENDING:
- Richard may brief further CQ corrections
- Integration into live Ratings Dashboard (patch-pillar-tree-tab-v2.py will need to use new taxonomy data)
- GitHub push
- pillar-tree-canonical.json NOT yet updated with V4 CF split (only new_tree_data.json has it)
```

## Session Timeline

1. Richard provided workbook, asked for standalone pillar tree using NEW taxonomy
2. Updated `pillar-tree-canonical.json` from workbook (rebuild_pillar_tree.py)
3. Built initial HTML — failed (minified JS). Fixed.
4. Wrong taxonomy (forced into old 4-tier). Richard: "Do NOT force it into the old schema." Rebuilt with faithful 3-tier.
5. Iterative layout: vertical-drop connectors for all tiers (3 rounds of refinement)
6. Richard: horizontal elements + vertical pillars. Done. Then: "Roll back." Rolled back.
7. Comprehensive rebuild: numbering + IC horizontal + BB horizontal + pillars stacked. Failed (</script> escaping). Fixed.
8. V2: removed dangling lines, connected pillar pills, enabled text wrapping.
9. V3: locked 5 BB groups on one row with equal-width columns, text wraps within columns. Richard: "Great."
10. V4: researched CF prompt, split E1.RA1 into external (7 CQs) + internal (5 CQs). Richard confirmed approach.

## Decisions Made

| # | Decision | Richard's words |
|---|----------|-----------------|
| 1 | Faithful 3-tier, NOT forced into old 4-tier | "Do NOT force it into the old schema" |
| 2 | All connector lines from bottom of pills, not right side | Multiple requests |
| 3 | IC elements horizontal, BB groups horizontal, pillars stacked | Final comprehensive request |
| 4 | 5 BB groups always on one row, text wraps within columns | "keep all the 5 groups in the building blocks section on one horizontal row" |
| 5 | Financial profile + track record included as internal CQs despite E2 overlap | "Include them as new CQs" |
| 6 | Section C "Key components summary" excluded from CQs | "Agreed with the Section C Q" |
