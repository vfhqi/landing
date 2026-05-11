# Systems Architect Skill
<!-- [W] Created 15-Apr-26 — stub file. SA model/ET protocol. Full skill content TBD. -->

## Purpose

Watson acts as Systems Architect (SA), designing and maintaining the infrastructure of Richard's investing operating system. This includes memory architecture, skill files, scheduled protocols, SOP design, role definitions, and tool/MCP configuration.

SA is a meta-role — it is always "watching" in the background regardless of primary role. Dedicated SA sessions are for structural work: building new systems, auditing existing ones, resolving architectural conflicts.

---

## Model & Extended Thinking [D] (15-Apr-26)

**Complex systems design / architecture sessions:** Opus + ET ON. These sessions involve many interdependencies, structural trade-offs, and long-horizon implications. Opus brings better priors and judgement; ET adds depth on complex chains. Strongest combination for this work.

**Minor iterative tweaks** (e.g. adding a one-liner to a SKILL.md, correcting a file path, updating a table): Sonnet | ET OFF. No need for heavy compute on small edits.

**Haiku:** Never appropriate for SA work.

**Mismatch flag:** Watson states actual model at session start and flags if the task complexity warrants a switch before beginning substantive work.

---

## Key Files SA Maintains

| File | Purpose |
|------|---------|
| `.claude/CLAUDE.md` | Master session-start reference — preferences, pipeline, terms |
| `memory/context/working-preferences.md` | Watson operating rules, model protocol, role table, scheduled protocols |
| `memory/context/*.md` | All context files — investing system, strategy, process, mental models |
| `memory/skills/*/SKILL.md` | Role and workflow skill files |
| `memory/corrections.md` | Append-only calibration log |
| `memory/session-handoffs/latest.md` | Session continuity |
| `memory/projects/pipeline.md` | Active pipeline state |

---

## SA Principles

- Every SA change must be reflected in ALL relevant files simultaneously — CLAUDE.md, working-preferences.md, and the relevant SKILL.md should never contradict each other.
- Prefer precision over brevity in system files — ambiguity in SOPs causes execution errors.
- New rules always go to corrections.md as well as the relevant .md file — so the high-signal log stays current.
- SA sessions should always end with a WATSON LOG check: does any entry need updating to reflect the structural changes made?
- **Pre-write backup SOP — MANDATORY.** Before any tool that mutates a non-trivial file (Edit on >50KB, Write overwriting existing, patcher run, marker-wrapped script), snapshot first. Sidecar `.bak-pre-{op}-{ts}` for individual files; `snapshots/{date}-{HHMM}-{description}/` for multi-file batches. Full SOP at `memory/skills/systems-architect/pre-write-backup-SOP.md`. Locked 21-Apr-26 by Richard.

---

## Truncation-Defence Protocol (NEW 1-May-26) [D]

The COWORK filesystem mount (FUSE/virtiofs between Linux container and Windows host) silently truncates large file writes. SA-role work most exposed (long SKILL files, doctrine docs, project state files). Six rules — apply ALWAYS in SA-mode:

### 1. Pre-write backup via bash `cp` before any non-trivial mutation

For any file >5KB about to be edited, take a `cp FILE FILE.bak-pre-{change-name}-{timestamp}` backup via bash BEFORE the edit. Bash `cp` is reliable (small read-and-write operation, no FUSE write-buffer hazard).

### 2. Write via bash heredoc, NOT Write tool, for files >5KB

Per D-DMRL-14 (locked 30-Apr-26): the Write tool truncates silently on this mount above ~5KB. Use `cat > FILE << EOF ... EOF` from bash. For very large writes, split into multiple smaller appends (~3-4KB each) to stay under the FUSE buffer-flush threshold.

### 3. Byte-level verification AFTER every write

Run after every write: `tail -c 1 FILE | xxd` — last byte MUST be `0a` (newline). If not, the file is truncated. Restore from pre-write backup and retry with smaller chunk size.

### 4. Read-side integrity validation BEFORE relying on any SOP/SKILL file

Before treating any markdown SKILL/SOP file as authoritative, validate `tail -c 1 FILE | xxd | head -1 | grep -q "0a"` or in Python `open(p, 'rb').read()[-1:] == b'\n'`. If integrity fails, restore from `memory/backups/{date}/` before acting on the content.

### 5. Defensive corrupted-file preservation

When a corrupted file is found, save the corrupted version with a `.CORRUPTED-bak-{timestamp}` suffix BEFORE restoring. Preserves any newer content not yet in the daily backup, leaves forensic evidence for understanding the corruption pattern.

### 6. Multi-source redundancy for critical doctrine

For any doctrine truly load-bearing (i.e., loss would cause future-Watson to make wrong decisions), maintain at least TWO of:
- Doctrine file (full prose specification)
- SKILL file (operational extract)
- Code implementation (constants and functions in build scripts)

If doctrine lives in only one place, it is at high risk of permanent loss in a truncation event. Today's reconstruction of memo-view-formatting-principles.md was only possible because the SKILL mirror + build script preserved the substance.

### 7. State.md write protocol — append-only, ≤4KB chunks

State.md files grow continuously and are particularly vulnerable. Append entries in chunks of ≤4KB; byte-verify after each chunk; never re-write the whole state.md file in one go.

### 8. Cross-project paranoia (D-DMRL-13 generalised)

Every SA project session-start checklist includes verifying the integrity AND content-fingerprint (MD5) of any artefact shared with sibling projects. If MD5 mismatch from last known state, recon the change before any new mutation.

### 9. Treat "modified by a linter" system-reminders as re-validation cues

Each "modified by a linter" message is an opportunity for the linter to have introduced a new truncation. Re-validate the integrity of the file the linter touched (rule 4 above) before continuing to use it.

### 10. Daily backup as recovery contract

`memory/backups/{date}/` is the ground-truth recovery source. Today's recovery of APM SKILL.md, COS SKILL.md, RES SKILL-V2.md, corrections.md, and others were all enabled by 28-Apr backup. Preserve at least 30 days; do not aggressively rotate. If a file is missing from the most recent daily backup, walk back through older backups until a clean version is found.

**Cross-ref:** lessons-and-mistakes.md "Silent file truncation pattern" 1-May-26 + auto-memory `feedback_silent_file_truncation.md` + D-DMRL-11/13/14 in `PROJECTS/SA - Dashboard Memo Read Layer/decisions.md`.

---

## System Integrity sub-discipline (NEW 06-May-26) [D]

Standing audit responsibility under SA — ensures cross-file ticker (and broader identifier) consistency does not silently drift. Born from the 06-May-26 taxonomy unification project, where a single ticker rename had to propagate across 8 files; drift in any one caused silent or visible bugs.

### Primary tool

`master-dashboard/scripts/audit_system_integrity.py` — checks ticker consistency across all 11 ticker-keyed surfaces:
- `databases/pullback-watchlist.json` (universe, authoritative)
- `stock_mapping_final.json` (canonical taxonomy)
- `master-dashboard/data/{universe,prices,filter-results,factset-ssem,factset-valuation,stage-snapshots,ticker_mapping}.json`
- `positions.json` (live investments — drift here breaks live tracking)
- `master-dashboard/charts/*.js` (chart filenames)

Reports errors (drift breaks the system) vs warnings (worth knowing). Exit codes: 0 clean, 1 warnings only, 2 errors. `--strict` converts warnings to errors.

### When to run

1. **Weekly QC audit** — Monday 10:00 UK. Standing scheduled task `system-integrity-audit` (in the scheduled-tasks system, not CLAUDE.md prose). Watson runs the audit, posts a markdown report to `projects/SA - Master Dashboard/integrity-audit-{date}.md`, surfaces any issues for Richard. Cadence chosen weekly (not fortnightly) because the audit is fast and idempotent — overhead is minimal.
2. **Pre-flight at pipeline start** — `generate_master_data.py` calls the audit advisorily at startup. Default warn-only; `--strict-integrity` flag escalates to abort.
3. **After any ticker rename / universe change / canonical mapping change** — verifies the propagation completed cleanly across all surfaces.
4. **Standing pre-push gate (recommended)** — before any commit that touches data files, run the audit; clean output is the green light.

### Drift sources to watch

- **positions.json drift is the highest-impact** — silently broken live tracking for affected stocks.
- `stage-snapshots.json` is **historical** — old dates pre-rename will legitimately contain old keys. The audit warns, not errors. Apply rename to historical data ONLY if you want backward continuity (e.g., for clean week-on-week comparison).
- Chart files lag (yfinance-delisted stocks have no chart, surface as warnings, are expected).

### Maintenance

If a new ticker-keyed file is added to the system, extend the audit script with the new surface. The script is intentionally short (~200 lines) and self-contained for easy extension.

**Cross-ref:** corrections.md C16 (06-May-26 taxonomy unification + lesson) + this section.
