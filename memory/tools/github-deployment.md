# GitHub Deployment from Cowork/Watson
<!-- [W] Created 28-Apr-26. Procedure tested and confirmed working. -->

## Overview

Watson can push dashboard updates to GitHub Pages from the Cowork sandbox without Richard's involvement. Two repos, same PAT, same push pattern.

## Credentials

**PAT location:** `C:\Users\richb\Documents\COWORK\.secrets\github-pat.txt`
- Fine-grained token, 93 chars, starts `github_pat_11CC...`
- Org-level scope — works for both repos
- Bash path: `/sessions/*/mnt/COWORK/.secrets/github-pat.txt`

## Repos

| Repo | GitHub URL | Pages URL | What gets pushed |
|------|-----------|-----------|-----------------|
| `vfhqi/dashboards` | `github.com/vfhqi/dashboards` | `https://vfhqi.github.io/dashboards/ic-ratings-dashboard-v2.html` | IC ratings dashboard HTML (copied as both `ic-ratings-dashboard-v2.html` AND `index.html`) |
| `vfhqi/master-dashboard` | `github.com/vfhqi/master-dashboard` | `https://vfhqi.github.io/master-dashboard/` | Master dashboard `index.html` |

## Push Procedure

**CRITICAL:** Do NOT attempt git operations directly on the mounted COWORK directories. Windows automation scripts create `.git/index.lock` files that block sandbox operations. Always use the fresh-clone-to-/tmp pattern below.

**CRITICAL:** `api.github.com` is blocked by sandbox proxy (403). Only `github.com` HTTPS works.

### IC Ratings Dashboard

```bash
PAT=$(cat /sessions/*/mnt/COWORK/.secrets/github-pat.txt | tr -d '\r\n ')
cd /tmp && rm -rf dash-push
git clone --depth 1 "https://${PAT}@github.com/vfhqi/dashboards.git" dash-push
cp /sessions/*/mnt/COWORK/databases/ic-ratings-dashboard-v2.html /tmp/dash-push/ic-ratings-dashboard-v2.html
cp /sessions/*/mnt/COWORK/databases/ic-ratings-dashboard-v2.html /tmp/dash-push/index.html
cd /tmp/dash-push && git config user.name "Watson" && git config user.email "rich.black@gmail.com"
git add -A && git commit -m "Watson: <description of changes>" && git push origin main
rm -rf /tmp/dash-push
```

### Master Dashboard

```bash
PAT=$(cat /sessions/*/mnt/COWORK/.secrets/github-pat.txt | tr -d '\r\n ')
cd /tmp && rm -rf dash-push
git clone --depth 1 "https://${PAT}@github.com/vfhqi/master-dashboard.git" dash-push
cp /sessions/*/mnt/COWORK/master-dashboard/index.html /tmp/dash-push/index.html
cd /tmp/dash-push && git config user.name "Watson" && git config user.email "rich.black@gmail.com"
git add -A && git commit -m "Watson: <description of changes>" && git push origin main
rm -rf /tmp/dash-push
```

## Chrome Testing After Push

1. Push using procedure above
2. Wait ~30 seconds for GitHub Pages deployment
3. Navigate to the Pages URL (see table above)
4. Audit using Claude in Chrome tools (`read_page`, `get_page_text`, `javascript_tool`)

## Commit Conventions

- Author: `Watson` / `rich.black@gmail.com`
- Message format: `Watson: <brief description of what changed>`
- Always `--depth 1` clone (speed + minimal footprint)
- Always `rm -rf /tmp/dash-push` after push (cleanup)

## Pre-existing Windows-side Scripts (reference only)

These run on Richard's PC, not from the sandbox:
- `master-dashboard/scripts/push-to-github.ps1` — PowerShell script that clones `vfhqi/dashboards`, copies master dashboard as `master-dashboard.html`, pushes
- `master-dashboard/scripts/refresh-dashboard-silent.bat` — 4-step build+push: `generate_master_data.py` → `generate_chart_data.py` → `build_dashboard.py` → git commit+push to `vfhqi/master-dashboard`

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `403 Forbidden` on `api.github.com` | Sandbox proxy allowlist | Use `github.com` HTTPS (git clone/push), not REST API |
| `.git/index.lock` on mounted dir | Windows automation scripts | Never git-operate on mounted dirs; use `/tmp` clone |
| `Operation not permitted` on lock file | Cross-filesystem permissions | Use `/tmp` clone pattern instead |
| Push rejected (non-fast-forward) | Someone pushed between clone and push | Re-clone and retry |
| PAT expired | Token rotation | Richard regenerates at github.com/settings/tokens |

## Session History

- 28-Apr-26: Procedure established and tested. Two commits pushed to `vfhqi/dashboards` (coverage tab fixes). Chrome-tested on GitHub Pages — all PASS.
