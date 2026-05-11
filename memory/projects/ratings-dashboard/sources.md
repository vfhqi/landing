# Ratings Dashboard — Canonical Source Paths
<!-- [W] Created 21-Apr-26. -->

## MEMO spec source

| Item | Path |
|------|------|
| Excel file (current) | `Files/NOT BACKED UP/RB downloads/RB excel tools/For Watson - APM Dashboard 4 views - 21_04_2026 0709.xlsx` |
| Sheet to read | `MEMO view MASTER CORRECT` |
| Other sheets | `TABLE view`, `MAP view`, `0522h 19_APR`, `0522h 19_APR alt1`, `0522h 19_APR alt2`, `LIST view` |

## Dashboard build pipeline

| Item | Path |
|------|------|
| Build script | `databases/scripts/build-memos.py` |
| Validator | `databases/scripts/validate-memo.py` |
| Markdown generator | `databases/scripts/generate-memo-md.py` |
| Live dashboard HTML | `databases/dashboard.html` (TBD — confirm exact filename in state.md) |
| Mockup (3-stage compare) | `databases/mockups/nvtk-cii-comparison.html` |

## Memo JSON sources

| Item | Path |
|------|------|
| NVTK Triaging (live) | `databases/memos/NVTK/Triaging.json` |
| NVTK ESA (to build) | `databases/memos/NVTK/ESA.json` |
| NVTK DD (to build) | `databases/memos/NVTK/DD.json` |
| HTRO Triaging (live) | `databases/memos/HTRO/Triaging.json` |

(Confirm exact paths in state.md when first touched.)

## Skill / SOP references

| Item | Path |
|------|------|
| Memo formatting v3.1 | `memory/skills/memo-view-formatting/SKILL.md` |
| Memo formatting principles | `memory/skills/memo-view-formatting/memo-view-formatting-principles.md` |
| FCS V7 (six pillars) | `memory/skills/fundamental-change-screen/SKILL.md` |
| Notion posting standard V2 | `memory/skills/notion-posting-standard/SKILL.md` |
| Diligence checks | `memory/skills/diligence-checks/SKILL.md` |
| Session handoff | `memory/skills/session-handoff/SKILL.md` |

## Backup / snapshot location

| Item | Path |
|------|------|
| Project snapshots | `memory/projects/ratings-dashboard/snapshots/{YYYY-MM-DD-HHMM}/` |
| Dashboard backups (separate) | `databases/backups/{timestamp}/` |
