# state.md — SA - LANDING PAGE

**Last updated:** 2026-05-11 (v6r5)

## Where we are

- **v6r5 SHIPPED LIVE at https://vfhqi.github.io/landing/** — Chrome QA complete, every link click-tested and verified to land on real content.
- **All R1-R6 visual changes + 7 follow-up Chrome QA fixes complete:**
  - r1 → R1-R6 visuals shipped
  - r2 → Three reminder-block destinations re-pointed (skills INDEX, pre-write-backup, working-preferences)
  - r3 → Arrow routing through cluster-free corridors (D-LP-45); GAP card moved away from cyan + widened (D-LP-47); OKRs wrap to 2 lines no truncation (D-LP-46); OKRs ALSO listed in Strategic Targets (D-LP-48); Notes Repo→Ratings arrow drops below cyan body
  - r4 → All .md GH links route via github.com/blob/main/ for rendered markdown (D-LP-49)
  - r5 → Master Dashboard hrefs repointed to vfhqi/master/ (was 404 vfhqi/master-dashboard); Notes/Ratings to vfhqi/ratings/; Position Manager synced into vfhqi/landing/ (D-LP-50); pullback watchlist HTML viewer built and substrate href updated (D-LP-51)
- **D-LP-34 → D-LP-51 added** (18 new decisions across r1→r5).
- **51 decisions locked total** D-LP-01 → D-LP-51.
- **D-LP-16 superseded** (reminder block was non-clickable; now clickable).
- **D-LP-24 partially superseded** (Strategic Targets title now sits above 3 rows; rows still equal-weight relative to each other).
- **Memory mirror published:** ~7.8MB / 432 files at vfhqi.github.io/landing/memory/, /wisdom-library/, /PROJECTS/, /auto-memory/, /claude/. Sync via manual rerun for now; auto-sync future SA-GITHUB-SOP item.
- **v5 baseline preserved:** v5 LIVE prior state at https://vfhqi.github.io/landing/ (32,725 → 36,725 bytes), 33 decisions still locked.
- **Snapshots:** v5 → v6, all preserved.
- Standing rule: **Edit tool BANNED on landing-page.html** per D-LP-17. (Hit it again 11-May during build script edit — recovered via /tmp heredoc rebuild.)
- Standing rule: **Watson SKILL operationalisation of OKRs DEFERRED** per D-LP-26.
- Standing rule: **`.nojekyll` must remain at GH repo root** per D-LP-33.

## v5 (still recorded for audit)

- **v5 SHIPPED LIVE at https://vfhqi.github.io/landing/** (HTTP 200, 31,850 bytes byte-identical, 20 anchors, all v5 features verified).
- **Thematics dashboard LIVE at https://vfhqi.github.io/landing/thematics-dashboard.html** (HTTP 200, 16,705 bytes, schema v2 with A&J / Source Research / Raw Research sections rendering correctly).
- **All deep links verified** — brief.md / delta-report.md / AS-Q[1-4]-extract.md / 2026-05.json / iran-war + bear-market raw feeders all 200 OK after `.nojekyll` push.
- **33 decisions locked** D-LP-01 → D-LP-33; noise list parked.
- **Manifest schema v2** — each thematic carries aj_memo[] + source_research[] + raw_research[]. AI populated with 2 memos + 14 source files; iran-oil + recession-rollover have raw feeders only (await first APM memo).
- **Portfolio OKR archive** at `databases/portfolio-okrs/`: `2026-05.json` (real data) + `current.json` (pointer) + README.md (schema docs).
- **GAP card** clickable → `2026-05.json` (real data, not pointer).
- **Stocks Universe substrate** shows real counts: 973 stocks · 24 industries · 154 sectors.
- **5 versions snapshotted** v1 → v5, all pre