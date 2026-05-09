# databases/portfolio-okrs/

Period-stamped JSON archive of Richard's portfolio OKRs (Target Conditions + monthly OKRs).

## Schema (v1)

- `{YYYY-MM}.json` — one file per period (typically monthly).
- `current.json` — pointer to active period.
- `index.json` — (optional, future) full chronological index.

## Files

- **`{YYYY-MM}.json`** — period file. Schema:
  ```json
  {
    "schema_version": "1",
    "period": "2026-05",
    "period_label": "May 2026",
    "generated_at": "2026-05-09",
    "portfolio_target_conditions": [ {id, name, type, target, current, delta, note} ],
    "portfolio_okrs": [ {id, description, target_count, filled_count, filled_with, filter_type, filter_value, rationale} ],
    "summary": {total_targets, total_filled, remaining},
    "future_tc_placeholders": [ ... ]
  }
  ```
- **`current.json`** — `{"current_period": "2026-05", "current_file": "2026-05.json"}`. Update at start of each new period.

## Consumers

- `landing-page.html` — embeds the current period's OKRs inline (in a `<script type="application/json" id="okrs">`) and renders them in the GAP card. Manual two-step: edit JSON file here AND inline copy in landing page until automated.
- **Future Watson APM workflow** — read `current.json` → `current_file` → load OKRs → use as screening filters. Operational hook-up DEFERRED to separate Richard-led pass per D-LP-26.
- **Future scripts** — same pattern.

## Rules

- Append-only: never overwrite a period file once the period closes.
- When OKR is filled, append the ticker to the corresponding `filled_with` array and increment `filled_count`. Update `summary`. Don't mutate `target_count` retroactively.
- Period transitions: copy the open targets from previous period if they roll forward; create new OKRs for period-specific gaps.
