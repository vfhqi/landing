# Daily Podcast SOP
<!-- [W] Created 03-Apr-26 by Systems Architect -->

## Purpose

Generate personalised daily podcast scripts on risk management, position management, portfolio construction, and exit discipline. The scripts are designed for Richard to paste into NotebookLM and listen to as audio — building a strong risk management mindset through daily osmosis.

---

## Trigger

- **When:** Every evening handoff (part of session-handoff protocol, Step 4c)
- **Frequency:** Daily (weekdays minimum, weekends optional)
- **Role:** HPC generates, session handoff delivers

---

## Output Spec

Every delivery includes **one script:**

| Version | Length | Word count (~150 wpm) | Use case |
|---------|--------|-----------------------|----------|
| **30-min** | ~4,500 words | Morning routine, evening wind-down, weekend, commute |

One 30-min script per episode. No 15-min versions.

---

## File Naming & Library

**Scripts saved to:** `memory/coaching/podcast-library/`

**Naming convention:**
```
YYYY-MM-DD-[theme-slug]-30.md
```

**Example:**
```
2026-04-04-exit-discipline-emotional-cycle-30.md
```

**Index file:** `memory/coaching/podcast-library/INDEX.md` — updated with every new episode. Tracks: date, theme, primary author(s), secondary authors, length, one-line summary, personalisation level.

---

## Canon — Approved Authors & Frameworks

Draw from any of these. Go wide. Rotate across authors to build breadth.

### Primary Canon (dedicated coaching memos exist)
| Author | Key concepts | Memo location |
|--------|-------------|---------------|
| **Mark Douglas** | 5 fundamental truths, 7 principles of consistency, probabilistic mindset, the zone, four trading fears | `coaching/references/mark-douglas.md` |
| **Mark Minervini** | Trend Template, progressive exposure, 7-8% rule, emotional cycle, VCP, stage analysis | `coaching/references/mark-minervini.md` |
| **Annie Duke** | Kill criteria, resulting, monkeys and pedestals, quitting frameworks, pre-commitment | `coaching/references/annie-duke.md` |
| **Van Tharp** | R-multiples, expectancy, position sizing models, beliefs audit, system design | `coaching/references/van-tharp.md` |

### Extended Canon (framework summaries in coaching-frameworks.md)
| Author | Key concepts |
|--------|-------------|
| **Lanny Bassham** | Self-image, mental rehearsal, directive affirmations, "that's like me" |
| **Steve Ward** | 4Cs (Commitment, Concentration, Confidence, Control), recovery, change drivers |
| **Bob Rotella** | Training vs Trusting mindset, 10 Commandments, pre-shot routine, accept imperfection |
| **Timothy Gallwey** | Performance = Potential - Interference, Self 1/Self 2, non-judgemental awareness |
| **James Clear** | Identity-based habits, environment design, habit stacking, compound improvement |
| **Jim Loehr** | Energy management, full engagement, recovery rituals, oscillation |
| **Steve Peters** | Chimp/Human/Computer model, emotional hijacking, Observer mode |
| **Brett Steenbarger** | Trading psychology, performance journals, solution-focused coaching |
| **James King** | Inner game of trading, focus and flow |
| **Jason Selk** | Mental toughness, relentless solution focus, 60-second mental workout |

### Supplementary (draw from training knowledge + web research)
- **William O'Neil** — CAN SLIM, sell rules, stock selection
- **Stan Weinstein** — 4-stage analysis, 30-week MA, sector rotation
- **Jack Schwager** — Market Wizards interviews, common traits of great traders
- **Howard Marks** — Second-level thinking, risk ≠ volatility, market cycles
- **Michael Mauboussin** — Skill vs luck, base rates, process journals
- **Ari Kiev** — Trading commitment, visualisation under pressure, trading larger
- **Nassim Taleb** — Antifragility, Black Swans, skin in the game
- **Daniel Kahneman** — System 1/2, loss aversion, anchoring, availability bias
- **Ray Dalio** — Pain + reflection = progress, radical transparency, principles

---

## Theme Rotation

### Core Themes (cycle through these)
1. **Exit discipline** — cutting losses, shot clock, emotional cycle, Stage 3/4 signals
2. **Progressive exposure** — test positions, scaling up on confirmation, protecting initial capital
3. **Monitoring discipline** — daily RS check, ostriching prevention, early warning signals
4. **Self-image and identity** — "I am a disciplined position manager," Bassham's mental rehearsal
5. **Probabilistic thinking** — Douglas's truths, accepting uncertainty, process over outcomes
6. **Energy and recovery** — Loehr's oscillation, Ward's recovery advocacy, decision quality under fatigue
7. **Simplicity and case clarity** — complexity as the enemy, "simple + completed > complicated + incomplete"
8. **Portfolio construction** — concentration discipline, diversification dimensions, sizing framework
9. **The knowing-doing gap** — why intellectual agreement isn't enough, bridging to embodiment
10. **Positive reinforcement** — Telecoms/Greggs/Instalco wins, evidence of capability, "that's like me"

### Rotation Logic
- Don't repeat the same theme within 5 episodes
- Don't repeat the same primary author within 3 episodes
- Weight themes 1-3 (exit, exposure, monitoring) slightly higher — these are the highest-leverage behaviours
- Every 5th episode should be a "positive evidence" episode (theme 10) to maintain self-image
- Cross-reference Richard's current pipeline state and recent coaching-log entries to make themes timely

---

## Personalisation Rules

Vary the personalisation level across episodes:

| Level | Description | Frequency |
|-------|-------------|-----------|
| **Heavy** | Specific stock post-mortems drawn from full 96-stock track record (NOT just BFF/XVIVO/Goodwin — use Instalco, Fasadgruppen, S4, Kainos, Keywords, Avanza, GVC, Entain, Greggs, Telecoms, etc.), journal quotes, R-multiple analysis | ~2x/week |
| **Medium** | References to Richard's strategy, portfolio architecture, current pipeline, general patterns | ~2x/week |
| **Light** | Framework-focused, author's own examples and stories, principles applied generally | ~1x/week |

**Always personalised regardless of level:**
- "You" throughout
- Coaching tone (direct, challenging, positive)
- Aligned to Richard's OKRs, ETCs, and strategy
- References to his specific investing system (HQI framework, 4 pillars, 6-stage process)

---

## Script Format Rules

- Solo narrator voice (Watson as coach speaking to Richard)
- No bullet points in spoken script — flowing speech only
- Short to medium sentences. Varied rhythm. Rhetorical questions.
- [PAUSE] markers for emphasis at key moments
- No hedging, no corporate language, no emoji
- Include stage directions in brackets where useful: [slower], [with emphasis], [beat]
- Journal quotes from Richard should be delivered slowly and given space
- End every episode with a single actionable takeaway

---

## Quality Checklist (before delivery)

- [ ] Word count within 10% of target (4,500 ±450)
- [ ] Reads well spoken aloud — no academic language, no bullet points in speech
- [ ] At least one author from the canon is the primary source
- [ ] Theme hasn't been repeated in last 5 episodes (check INDEX.md)
- [ ] Primary author hasn't been repeated in last 3 episodes (check INDEX.md)
- [ ] Aligned to current OKRs/ETCs/strategy (read relevant files if unsure)
- [ ] Ends with a single actionable takeaway
- [ ] 30-min script produced
- [ ] INDEX.md updated
- [ ] Scripts saved with correct naming convention
- [ ] **STOCK DEPTH CHECK (Non-Negotiable):** Minimum 5-6 different stocks referenced. No single stock referenced more than twice. At least 2 stocks must NOT be BFF, XVIVO, or Goodwin. If personalisation level is Heavy or Medium-Heavy, at least 3 direct journal quotes from track-record-by-stock.md must be included.
- [ ] **ARCHETYPE CHECK:** At least 2 different archetypes from stock-archetypes.md referenced (not just "delayed exit" repeatedly). Name the archetype explicitly in the script.
- [ ] **TRACK RECORD LOADING GATE COMPLETED:** Steps 3-5 of Preparation section were read before writing began. If delegating to sub-agents, the sub-agent prompt must include specific stock examples, journal quotes, and archetype references extracted from these files — do NOT rely on sub-agents to load the files themselves.

---

## Preparation (before generating) — MANDATORY LOADING GATE

**Non-Negotiable:** Steps 1-5 below MUST be completed before writing a single word of script. This gate exists because Watson defaulted to 3 "safe" stock examples (BFF/XVIVO/Goodwin) despite having a 96-stock track record with 17 deep narratives, 19 archetypes, and hundreds of journal quotes. That failure made the coaching generic instead of personal. See corrections.md entry 10-Apr-26.

1. Read `memory/coaching/podcast-library/INDEX.md` — check recent themes and authors
2. Read `memory/coaching-log.md` — any recent patterns or observations to address?
3. **Read `memory/coaching/track-record-by-stock.md`** — scan Tier 1 index (17 stocks) + read full entries for 3-4 stocks most relevant to this episode's theme. Pull specific journal quotes. This is the primary source of personalisation.
4. **Read `memory/coaching/stock-archetypes.md`** — identify which archetypes connect to this episode's theme. Use specific archetype examples (not just the behavioural patterns from HPC SKILL.md).
5. **Read `memory/coaching/risk-management-lessons.md`** — pull the relevant section(s) for the episode theme (e.g., §3 Exit for exit discipline episodes, §1 Sizing for sizing episodes). Use Watson Coaching Prompts and Richard's own journal quotes.
6. (Optional) Read `memory/coaching/stock-trigger-cards.md` — useful for quick-reference coaching hooks per stock.
3. Read `memory/projects/pipeline.md` — current portfolio state for timely references
4. Pick theme and primary author based on rotation logic
5. Read the relevant coaching reference file(s)
6. Generate both scripts
7. Update INDEX.md
8. Deliver via session handoff

---

## Integration Points

| System | How Daily Podcast connects |
|--------|---------------------------|
| **Session Handoff SOP** | Step 4c — generate and deliver scripts as part of evening handoff |
| **HPC Role Charter** | Listed under Daily responsibilities |
| **CLAUDE.md** | Listed under Scheduled Protocols |
| **Coaching Cadence** | New touchpoint in HPC SKILL.md cadence table |
| **Coaching-frameworks.md** | Canon source — all approved authors documented there |
| **Morning Questions** | Can reference yesterday's podcast theme: "You listened to X yesterday — did it land?" |

---

## Key Files

| File | Purpose |
|------|---------|
| `coaching/podcast-library/INDEX.md` | Episode index — date, theme, author, length, summary |
| `coaching/podcast-library/YYYY-MM-DD-*.md` | Individual scripts |
| `coaching/references/*.md` | Source coaching memos |
| `skills/high-performance-coach/references/coaching-frameworks.md` | Full canon reference |
| `coaching-log.md` | Recent coaching observations (for timely personalisation) |
| `projects/pipeline.md` | Current portfolio state |
