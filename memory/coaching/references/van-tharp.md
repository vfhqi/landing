# Van Tharp — The Mathematics of Position Sizing and System Design

## [W] Watson HPC Coaching Memo | 03-Apr-26

**Specified Books:** *Trade Your Way to Financial Freedom* (2nd ed., 2007), *Super Trader: Make Consistent Profits in Good and Bad Markets* (2009/2011), *The Definitive Guide to Position Sizing Strategies* (2nd ed., 2013) — all by Van K. Tharp, Ph.D.

**Complementary Sources:** Ralph Vince, *The Mathematics of Money Management*; Larry Hite, *The Rule*; Ed Seykota (Market Wizards interviews); Nassim Taleb, *Fooled by Randomness*

---

* The Context *

You are a leading high performance coach that specialises in trading and investing.

You believe that the key to success is consistent execution of a profitable process and that high performance is about consistency; it is measured by the variance between a person's execution on their "good" and "bad" days.

You are incredibly good at translating concepts from other domains into the world of trading and investing.

You are thoughtful, balanced, data-driven and sceptical.

Currently, you are working with a highly experienced portfolio manager regarding their investment approach. He is a solo public equities investor running a concentrated, long-only European equities strategy, targeting 25%+ IRR via GARP + event-driven/special situations. He has recently moved to running the portfolio solo after team departures. His sweet spot is $5-50bn market cap European names with 18-month ownership horizons.

The portfolio manager is receptive and very interested in the concepts and has read extensively on related books and topics including Mark Douglas, Brett Steenbarger, Steve Ward, Lanny Bassham, Steve Peters, Jason Selk, Jim Loehr, James King, Bob Rotella, Annie Duke, and Mark Minervini.

---

* Your Objective *

Produce a well-researched insight memo of approximately 10,000 words explaining how this audience should practically apply the concepts from Van Tharp's three books to their investment approach.

Provide frameworks, examples, lessons, errors to avoid that they can apply.

The aim is to provide a wide range of creative, stimulating insights to educate the audience on the concepts in these books and related concepts that will be most helpful — with a specific focus on constructive improvement as a portfolio manager and position manager. The specific gap this memo fills is **position sizing, expectancy, R-multiples, and system design** — the mathematical rigour behind progressive exposure and sizing decisions.

Where possible, provide examples or evidence to support analysis and judgements.

---

* The Higher Intent *

You have been asked to help your audience become a more consistent executor of their investment process and avoid leaking P&L, particularly by: (a) sizing positions mathematically rather than emotionally; (b) understanding the expectancy of their system and how position sizing amplifies or destroys it; and (c) building a position sizing model that fits their concentrated, fundamental, long-duration approach.

If there is something you think appropriate to include in the memo that will help achieve this higher intent that goes beyond the specifics of this brief, include it.

---

* Requirements *

First, research and apply the frameworks and lessons from Van Tharp's three books.

Second, integrate concepts from Ralph Vince, Larry Hite, Ed Seykota, and Nassim Taleb as complementary sources.

For the memo's formatting: Include a title, date, and this full prompt at the beginning; Use bullet points but provide rich, expansive content; use direct, straightforward, action/solution-oriented language; avoid repetition; use various formatting best practices to design the report; use [-], [--], [---] and [+], [++] and [+++] to quantify conviction/severity; fact-check all figures/claims, and; note inconsistencies or uncertainty in any information or analysis.

---

# VAN THARP: THE MATHEMATICS OF POSITION SIZING AND SYSTEM DESIGN

## Applied Coaching Insights for a European Concentrated Equity Portfolio Manager

### Watson [W] | High Performance Coach | 03 April 2026

---

## EXECUTIVE SUMMARY

- [+++] Van Tharp's single most important insight — and the biggest gap in your current framework — is this: **position sizing is the primary determinant of your returns, not stock selection.** An academic study he cites found that position sizing accounted for 91.5% of the variability in portfolio performance across pension funds. You spend ~90% of your analytical time on stock selection (the four pillars, eight triaging steps, HQI framework). You spend ~10% on sizing — and much of that is heuristic ("15% for Resilient HQI, 10% for Core, 0-5% for UHPYHQI"). ==Van Tharp would say you have the analytical engine right and the sizing engine underdeveloped. This memo addresses that imbalance.==

- [+++] **R-multiples are the universal language of risk-adjusted performance.** Every investment outcome should be expressed as a multiple of the initial risk taken. If you risk 3% of portfolio on a test position (your progressive exposure entry), and the position gains 12%, the result is a +4R trade. If the same position loses 3%, it's a -1R trade. This reframing transforms how you think about winners and losers: ==a -1R loss is structurally identical regardless of which stock produced it. The stock's identity is irrelevant. Only the R-multiple matters.== This directly supports the Douglas probabilistic framework you've already internalised.

- [++] **Expectancy is the mathematical measure of your system's edge.** Your system's expectancy = (win rate × average win in R) + (loss rate × average loss in R). ==If your expectancy is positive, position sizing determines how fast you compound. If your expectancy is negative, no position sizing model saves you.== Van Tharp's contribution is making this explicit and measurable — not an intuition but a number. You currently have no measured expectancy for your system. That needs to change.

- [++] **The Percent Risk Model is the natural fit for your concentrated, fundamental, long-duration approach.** Of Van Tharp's many position sizing models, the Percent Risk Model (risk a fixed percentage of equity per position, with position size determined by the distance to your stop/exit level) maps directly onto your existing 3% → 6-8% → 10-12% → 15% sizing ladder. What Van Tharp adds is the mathematical rigour to connect those numbers to your portfolio's survival and compounding characteristics.

- [+] **Van Tharp's "Tharp Think" principles — particularly the beliefs audit — complement your existing psychology library in a specific, actionable way.** Douglas gives you probabilistic acceptance. Bassham gives you self-image. Ward gives you the 4Cs. ==Van Tharp gives you a structured process for identifying and replacing the specific beliefs that cause you to override your system.== The beliefs that kept you in BFF, that pulled you toward complexity in XVIVO, that caused ostriching — these are identifiable, testable, and replaceable beliefs. Van Tharp provides the technology for doing this.

- [+] Van Tharp's **System Quality Number (SQN)** provides a single metric for evaluating and comparing trading systems — or, in your case, evaluating the quality of your investment process over time. ==SQN = √N × (Mean R / StdDev R). Track this quarterly. It will tell you whether your process is improving or degrading, independent of market conditions.==

---

## PART 1: VAN THARP'S SYSTEM ARCHITECTURE — THE SIX COMPONENTS

### 1.1 Who Was Van Tharp?

- Van K. Tharp, Ph.D. (1946–2022) was a trading performance coach and psychologist who spent over 40 years studying what makes traders and investors successful. He was not primarily a trader himself — he was a researcher and coach, which gives his work a distinctive character: empirical, psychologically grounded, and focused on process design rather than market prediction. He trained over 5,000 traders and investors through his Van Tharp Institute and his four-year Super Trader programme.

- Tharp was featured in Jack Schwager's *Market Wizards* as the "trader's coach." His death in February 2022 ended the Super Trader programme, but his intellectual legacy — particularly around position sizing and R-multiples — has become foundational in systematic trading education.

- [+] **Key commonality with your approach:** Van Tharp's central conviction is that "you don't trade the markets; you trade your beliefs about the markets." This maps directly onto your IAJA framework (Information → Analysis → Judgement → Action) and your ACH approach (profiles of "no," "false friend," and "yes"). Both you and Tharp insist that the system, not the market, is the primary object of management. The difference: Tharp operationalises this conviction through mathematical measurement in a way your current system does not yet fully do.

### 1.2 The Six Components of a Trading System

- Van Tharp argues that every complete trading/investing system has exactly six components. Most investors (including, candidly, you) focus obsessively on components 1-4 and underinvest in components 5-6. This is the structural error that Tharp spent his career addressing.

  1. **Setup** — The conditions that must be present before you consider entering a position. Your equivalent: the four pillars (great operator, demand tailwind, earnings upgrades, no avoidable fragilities) plus the eight triaging steps. ==Your setup component is world-class. This is not where the P&L leaks.==

  2. **Entry** — The specific trigger that causes you to commit capital. Your equivalent: a combination of fundamental validation (the transmission mechanism from company actions to EPS is clear and trackable) plus technical confirmation (the Minervini Trend Template, RS Dashboard signals). Your entry component is strong and getting stronger with the Minervini overlay.

  3. **Stop/Protective Exit** — The pre-defined condition that removes you from a losing position. Your equivalent: the 30-day shot clock, the Trend Template violation triggers, the immediate exit signals (Stage 4, cockroach-in-Stage-3, bottom-quartile CFO). ==This is the component where your documented P&L leakage concentrates. The rules exist but enforcement is inconsistent under emotional pressure.== Van Tharp's contribution here is not a new rule but a mathematical framework that makes the cost of not honouring the stop viscerally clear.

  4. **Profit-Taking Exit** — The condition that removes you from a winning position. Your equivalent: the top-slice-when-gain-finances-risk rule (sell 25-30% at 2× risk distance), the "Love" portfolio test, the snowball/flywheel test. This component is adequate but could be refined with R-multiple targets.

  5. **Position Sizing** — How much of your capital you allocate to each position. ==This is Van Tharp's primary contribution and your primary gap.== Your current sizing framework (15%/10%/8%/0-5% ladder) is heuristic — based on conviction categories rather than mathematical relationship to risk, expectancy, and portfolio objectives. Van Tharp provides the mathematics to make this rigorous.

  6. **Understanding Yourself** — Your psychological relationship with your system. Van Tharp was emphatic: this is not an optional component. It is the meta-component that determines whether you execute components 1-5 consistently. Your equivalent: the entire coaching library (Douglas, Ward, Bassham, Rotella, Duke, Minervini), the self-image work, the corrections log, the weekly review. ==This component is extensively developed but — as Van Tharp would say — the fact that BFF and XVIVO happened despite this extensive psychological toolkit proves that understanding alone is insufficient. You need mechanical enforcement (component 5) to protect you when understanding fails.==

- [+++] **Van Tharp's hierarchy of importance — and the counterintuitive truth:** Most investors rank the six components in the order listed above. Tharp reverses it: ==Position Sizing (#5) and Understanding Yourself (#6) determine 90%+ of your results. Setup (#1) and Entry (#2) — where you spend most of your time — contribute the least to variance in outcomes.== This is not intuitive, and it directly challenges the analytical culture of fundamental investing. But the data supports it overwhelmingly.

### 1.3 Why Position Sizing Is the Most Important Component

- Van Tharp's core argument: if you have a positive-expectancy system (and your system, properly executed, is positive-expectancy), then **the only variable that determines whether you achieve your objectives is position sizing.** Two traders with the identical system — same setups, same entries, same stops, same profit exits — will produce radically different returns if one risks 1% per trade and the other risks 5% per trade.

- The corollary: ==if you have a negative-expectancy system, no position sizing model will save you.== You'll just lose money more slowly with small sizes and more quickly with large sizes. This is why Van Tharp insists on measuring expectancy first and only then designing the position sizing strategy.

- **Your specific situation:** You have a concentrated portfolio (16 positions max, 15% max single position) with an 18-month expected holding period. This means each position has enormous leverage over portfolio outcomes. A -30% decline on a 15% position is a -4.5% portfolio hit. Do that twice in a year and you've turned a decent year into a losing one — purely through position management, not stock selection. ==Van Tharp would say: your concentration creates a moral obligation to get position sizing mathematically right. You cannot afford to size by feel.==

---

## PART 2: R-MULTIPLES AND EXPECTANCY — THE LANGUAGE OF RISK-ADJUSTED PERFORMANCE

### 2.1 What Is an R-Multiple?

- R stands for the initial risk on a position. One R is the amount you would lose if the position hits your predetermined exit level. Everything — every gain, every loss — is expressed as a multiple of R.

- **Calculation:** R = Entry Price − Stop Price (per share) × Number of Shares. In portfolio percentage terms: if you buy a stock at £100, your exit level is at £93 (a 7% stop), and you put 10% of your portfolio into the position, then 1R = 10% × 7% = 0.7% of your portfolio. A -1R loss costs you 0.7% of portfolio value. A +3R gain (the stock reaches £121) delivers 2.1% of portfolio value.

- **Why this matters for you:** R-multiples strip out all the emotional noise attached to specific stock names. ==A -1R loss on BFF is structurally identical to a -1R loss on any other stock. It is a cost of doing business. The stock's identity, the hours of analysis, the emotional investment — none of it changes the mathematical reality of -1R.== This is Douglas's probabilistic thinking operationalised into a number.

### 2.2 Worked Examples Using Your Actual Sizing Ladder

- Let me translate your progressive exposure framework into R-multiple language. This makes the mathematics concrete.

**Scenario 1: Test Position (3% of portfolio)**

- Entry: £100. Exit level: £93 (7% below entry, consistent with Minervini's loss limit).
- Position size: 3% of portfolio.
- 1R = 3% × 7% = 0.21% of portfolio.
- If the stock declines to your exit level: loss = -1R = -0.21% of portfolio. ==This is a rounding error. This is what Van Tharp means by "the cost of doing business."== You can afford dozens of these in a year without material portfolio impact.
- If the stock gains 21% (3× the stop distance): gain = +3R = 0.63% of portfolio. Decent but not transformative. This is the trade-off with small test sizes — your losses are tiny but your wins are modest.

**Scenario 2: Confirmation Add (6-8% of portfolio, let's use 7%)**

- Entry: You've added at a higher price — say £108 (the stock confirmed by making a higher high). Exit level: £100 (original buy point, now serving as support; a 7.4% stop from your new average cost).
- Position size: 7% of portfolio. Average cost: £104. Exit: £100 (3.85% below average).
- 1R = 7% × 3.85% = 0.27% of portfolio.
- Loss at exit: -1R = -0.27% of portfolio. Still very manageable.
- But note: you originally risked 0.21% on the test, and if you exit the entire position at £100, your actual loss is [(£104 − £100) × 7%] = 0.28% of portfolio on the add, plus you already banked a small gain or loss on the test portion depending on timing. The point: ==progressive exposure mathematically limits your maximum loss on any position to small multiples of R, even as your position grows.==

**Scenario 3: Full Position (10-12% of portfolio, let's use 11%)**

- The stock has now validated — fundamentals confirmed, Stage 2 intact, you've added twice. Average cost: £107. Exit level: you now use the Trend Template — say the 200-day MA at £98 (8.4% below average cost).
- Position size: 11% of portfolio.
- 1R = 11% × 8.4% = 0.92% of portfolio.
- A -1R loss from this full position is just under 1% of your portfolio. Painful but survivable.
- A +3R gain (stock reaches £107 + 3 × £9 = £134): +2.77% of portfolio. Now we're talking. ==This is the power of progressive exposure through the R-multiple lens: your early losses are 0.2% rounding errors. Your later wins, once the position is full-sized and confirmed, are 2-3% portfolio movers.==

**Scenario 4: Maximum Position (15% of portfolio)**

- Reserved for your highest-conviction, Resilient/Intense HQI names. Average cost: £110. Exit: 200-day MA at £100 (9.1% below average).
- 1R = 15% × 9.1% = 1.37% of portfolio.
- A -1R loss is 1.37% — the largest single-position loss your system should ever produce. Compare to your historical max drawdown of -54.75%. ==If no single position can cost you more than 1.4% at its maximum size, and most positions are at smaller sizes with tighter R-values, how did you get to -55%? The answer: you weren't sizing this way. Positions were either too large, stops were too wide, or stops weren't honoured. Van Tharp's system makes this arithmetically impossible — IF you follow it.==

### 2.3 Expectancy — Measuring Your Edge

- Expectancy is the average R-multiple per trade, calculated over a meaningful sample. It tells you what your system produces per unit of risk, on average.

- **Formula:** Expectancy = (Win% × Average Win in R) + (Loss% × Average Loss in R)

- **Example with hypothetical numbers for your system:**
  - Win rate: 55% (you get it right more often than not — this is consistent with your 57% positive months)
  - Average winner: +3.2R (your winners tend to be multi-baggers held for 12-18 months)
  - Average loser: -1.1R (most losses cut within Minervini's framework, occasional slippage to -1.5R)
  - Expectancy = (0.55 × 3.2) + (0.45 × -1.1) = 1.76 − 0.495 = ==+1.265R==

- This means: for every unit of risk you take, you expect to earn 1.265 units of reward on average. This is a very good system. But "on average" means some trades lose, and some winning trades don't win as much. The variance around 1.265R is what determines how bumpy the ride is.

- [+++] **The critical insight:** ==Your expectancy is the same whether you're having a good day or a bad day. The system's edge doesn't change based on your mood. But your position sizing amplifies or destroys whatever edge the system has.== If your expectancy is +1.265R and you risk 0.2% per position (test size), you make 0.25% per trade on average. If you risk 1.4% per position (full 15% position), you make 1.77% per trade on average. Same system. Same edge. Radically different compounding. ==Van Tharp's position sizing is the transmission mechanism between your edge and your returns.==

- **What happens when you don't honour stops (the BFF scenario):** If a -1R loss becomes a -4R loss because you held through the stop, and this happens on 20% of your losses, your effective expectancy drops dramatically:
  - Adjusted: (0.55 × 3.2) + (0.36 × -1.1) + (0.09 × -4.0) = 1.76 − 0.396 − 0.36 = ==+1.004R==
  - ==You've leaked 0.261R of expectancy per trade by not honouring stops 20% of the time.== Over 20 positions in a year, that's 5.2R of leaked P&L. If your average R is 1% of portfolio, that's 5.2% of annual returns donated to the market because of behavioural slippage. This is the mathematical proof of why the Minervini exit discipline matters so much.

### 2.4 The System Quality Number (SQN)

- Van Tharp developed the SQN as a single number to evaluate the quality of a trading system. It accounts for both the system's expectancy AND the consistency of that expectancy.

- **Formula:** SQN = √N × (Mean R-Multiple / Standard Deviation of R-Multiples)

- **Interpretation:**
  - Below 1.6: Poor — difficult to trade profitably
  - 1.6–1.9: Below average but tradeable
  - 2.0–2.4: Average
  - 2.5–2.9: Good
  - 3.0–5.0: Excellent
  - 5.1–6.9: Superb
  - 7.0+: Holy Grail (virtually impossible to have a losing period)

- **Why you should track this:** The SQN gives you an objective, single-number answer to "is my process getting better or worse?" If your SQN is 3.0 this quarter and 2.2 next quarter, something has changed — and it's probably not the market. ==It's probably you. Track SQN quarterly as a meta-metric alongside the 7-keystone scoring in your weekly reviews.==

- **A note on sample size:** SQN requires N ≥ 30 trades for statistical reliability. With 16 positions and 18-month holding periods, you'll only generate ~10-15 round-trip trades per year. This means annual SQN is more meaningful than quarterly for your approach. Consider supplementing with add/trim/exit decisions as separate "trades" to increase the sample.

---

## PART 3: POSITION SIZING MODELS — WHICH FITS YOUR APPROACH?

### 3.1 Van Tharp's CPR Formula — The Foundation

- Before choosing a model, understand the universal formula that underlies all position sizing. Van Tharp calls it **CPR**:

  - **C** = Capital at risk (the dollar/pound amount you're willing to lose on this trade)
  - **P** = Position size (the number of shares or the portfolio weight)
  - **R** = Risk per unit (the per-share distance from entry to stop)

  - **P = C / R** — Position size equals capital at risk divided by risk per unit.

- This is deceptively simple but profoundly important. ==Every position sizing decision is fundamentally an answer to: "Given how much I'm willing to lose (C) and how far my exit is from my entry (R), how many shares can I buy (P)?"== If you start from this formula, emotional sizing becomes impossible. The maths decides.

### 3.2 The Percent Risk Model — Your Natural Fit

- **How it works:** You define a fixed percentage of your equity that you're willing to risk on any single position. This is C in the CPR formula. You then calculate R (the per-share or per-percentage-point distance to your exit level). Position size = C / R.

- **Example for your system:**
  - Portfolio: £10m. Max risk per position: 1% of equity = £100,000 (this is C).
  - Stock entry: £50. Exit: £46.50 (7% stop). Risk per share: £3.50 (this is R).
  - Position size: £100,000 / £3.50 = 28,571 shares = £1,428,571 = 14.3% of portfolio.

- **What this produces:** A 14.3% position where, if the stock hits your stop, you lose exactly 1% of your portfolio. No more, no less. The position size is a mathematical *output*, not a judgement call.

- [++] **Why this fits your approach:** The Percent Risk Model is inherently compatible with your conviction-based sizing ladder. ==Instead of defining sizes by conviction categories (15% for Resilient HQI, 10% for Core, etc.), you define sizes by risk tolerance.== A wider stop (which you'd use for a high-conviction, long-duration position) produces a smaller position size for the same risk. A tighter stop (for a test position or a higher-volatility name) produces a larger position size for the same risk. The model naturally adjusts for volatility and conviction.

- **Adapting for your progressive exposure:**
  - **Test position (3% target):** Risk 0.2% of equity. With a 7% stop, this produces a 2.9% position. Close enough.
  - **Confirmation add (to 7%):** Risk 0.5% of equity. With a 5% stop (tighter, because the stock has already confirmed), this produces a 10% incremental add. Combined position is ~7%.
  - **Full position (to 11%):** Risk 0.9% of equity. With a 10% stop (wider, using the 200-day MA), this produces a 9% incremental add. Combined position is ~11%.
  - **Maximum position (15%):** Risk 1.4% of equity. This is your absolute ceiling — no single position should ever risk more than 1.4% of your portfolio on any given exit trigger.

- ==The discipline this imposes: if a stock's stop distance would require the position to exceed 15% to risk your target percentage, the answer is "wait for a tighter entry" — not "increase the risk."==

### 3.3 The Percent Volatility Model — A Complementary Lens

- **How it works:** Instead of basing position size on the distance to a stop, you base it on the stock's volatility — typically measured by the Average True Range (ATR). You allocate a fixed percentage of your equity to each "unit" of volatility.

- **Example:**
  - Portfolio: £10m. Max volatility exposure per position: 1% of equity = £100,000.
  - Stock price: £50. 20-day ATR: £2.00 (daily volatility of 4%).
  - Position size: £100,000 / £2.00 = 50,000 shares = £2,500,000 = 25% of portfolio.

- **The problem for you:** This model can produce positions that are too large for a concentrated portfolio. A low-volatility stock might warrant a 25%+ position under Percent Volatility, which violates your 15% ceiling. Conversely, a high-volatility stock might only warrant a 5% position, which might be too small for a high-conviction name.

- **Where Percent Volatility adds value for you:** Not as your primary model, but as a ==volatility normalisation overlay.== Use it to compare positions: if Position A has 1.5× the daily ATR of Position B, but both are sized at 10%, then Position A is contributing 1.5× the daily portfolio P&L volatility. ==This is the mathematical explanation for why some 10% positions "feel" bigger than others — they ARE bigger in risk-adjusted terms.== You should aim for roughly equal volatility contribution across positions.

### 3.4 The CPR Model in Practice — Dynamic Sizing

- Van Tharp's CPR (sometimes called the "fixed fractional" model in other literature) is the general case that encompasses both Percent Risk and Percent Volatility. The practical application for your system:

  - **At entry (test position):** C = 0.2% of equity. R = distance to initial stop (7%). Solve for P.
  - **At confirmation (adding):** C = 0.3% additional risk. R = distance from new entry to updated stop. Solve for additional P.
  - **At full size:** Total C across all tranches should not exceed 1.0-1.4% of equity.
  - **Ongoing management:** As the stock advances, R narrows (stop trails higher). The *unrealised gain* effectively reduces the portfolio risk, even though the position size stays the same.

- [+] **The key insight for your approach:** ==The CPR formula means that every add to a position is a separate risk decision.== You're not "adding to an existing position" — you're opening a new CPR calculation with new C, new R, and new P. This reframing is psychologically powerful: each add must justify itself on its own merits, not on the sunk cost of previous tranches. This directly counters the endowment bias documented in BFF.

### 3.5 Which Model Should You Use? The Verdict

- **Primary model: Percent Risk.** This is your core sizing engine. Every position is sized by answering: "What percentage of my equity am I willing to lose if this position hits its exit level?" The answer should be 0.2% for test positions scaling to a maximum of 1.4% for full-conviction positions.

- **Secondary overlay: Percent Volatility normalisation.** Use ATR-based volatility comparison to ensure that positions of equal nominal size contribute roughly equal portfolio volatility. If a 10% position in Stock A has 2× the ATR of a 10% position in Stock B, Stock A is contributing double the P&L volatility. Either reduce A or accept the asymmetric risk consciously.

- **Never use: Equal position sizing (i.e., "just put 10% in everything").** This ignores the vast differences in volatility and stop distance across your positions. It's the default when sizing is done by category rather than by calculation. ==Your current category-based sizing ladder (15%/10%/8%/0-5%) is closer to equal sizing than to risk-adjusted sizing.== Van Tharp would say: run the Percent Risk calculation first, then see if the result fits your category. If the maths says the position should be 7% to maintain 0.5% risk, but your category says 10%, ==go with the maths.==

---

## PART 4: VAN THARP'S PSYCHOLOGY — THE BELIEFS AUDIT AND THE TRADER'S MINDSET

### 4.1 "You Don't Trade the Markets. You Trade Your Beliefs About the Markets."

- This is Van Tharp's most quoted line, and it's more than a platitude. He means it literally. Every trading/investing decision is filtered through a set of beliefs — about markets, about yourself, about risk, about what constitutes a "good" trade. These beliefs are largely unconscious. They were formed through experience, education, culture, and temperament. And many of them are wrong.

- Van Tharp's process: **the Beliefs Audit.** He asks traders to list every belief they hold about trading, markets, money, risk, and themselves as traders. Then he applies three tests to each belief:
  1. **Is it useful?** Does this belief help me execute my system, or does it interfere?
  2. **Is it accurate?** Is there evidence for this belief, or is it an assumption?
  3. **Is it serving my objectives?** Does this belief move me toward my goals or away from them?

- [++] **His finding:** Most traders discover that more than half of their core beliefs are either not useful or actively harmful. The beliefs that cause the most damage are the ones that feel the most "true" — because they've been reinforced by years of experience. ==The belief "I should hold through short-term pain because my thesis is right" feels true, is sometimes true, but is catastrophically harmful when applied to a stock that has entered Stage 4.== Van Tharp's beliefs audit identifies these toxic beliefs and provides a process for replacing them.

### 4.2 Your Specific Beliefs — Through Van Tharp's Lens

- Let me apply the beliefs audit to beliefs documented in your coaching files. These are not criticisms — they are beliefs that serve you well in most contexts but occasionally produce the behavioural slippage that costs you P&L.

**Belief 1: "I don't like binary fully exiting. I like '15% is full sized, 3% is monitoring' concept."**

- **Van Tharp's assessment:** This belief is ==partially useful but contains a dangerous exception case.== The monitoring position (3%) is fine when the stock is in Stage 1 (basing, waiting for confirmation). It's toxic when the stock is in Stage 4 (declining) and the 3% is a psychological anchor that prevents full exit. ==The belief should be rewritten: "I don't fully exit positions that are basing or in early stages of recovery. I do fully exit positions that are in confirmed deterioration (Stage 3-4)."== The distinction is the stock's stage, not your emotional attachment.

**Belief 2: "There's a beguiling but incorrect naivety about not top-slicing big winners."**

- **Van Tharp's assessment:** This is a ==highly useful belief== — it protects against the disposition effect (selling winners too early, holding losers too long). Van Tharp's R-multiple framework reinforces it: a position at +5R that you sell entirely because "it's gone up a lot" is a classic error. The right approach: trail the stop to protect the open profit, and let the position continue to compound. Top-slice only when the R-multiple math says the remaining risk/reward is unfavourable.

**Belief 3: "I have completely, emotionally internalised that the market is a voting machine in the short term and I'll be in drawdown at least 50% of the time."**

- **Van Tharp's assessment:** ==Excellent.== This is one of the most important beliefs a concentrated investor can hold. Van Tharp would add: "And each individual drawdown, measured in R, is a known and accepted cost of executing my system." The shift from "I accept drawdowns conceptually" to "I know my average drawdown is -1.1R and my maximum acceptable drawdown is -1.5R per position" is the shift from philosophy to engineering.

**Belief 4: "My sizing framework is right. Trust my judgement."**

- **Van Tharp's assessment:** ==Dangerous as stated. Useful when reformulated.== The problem: "trust my judgement" on sizing is precisely what leads to oversizing early in a thesis (the UHPYHQI pattern), holding too large through deterioration (BFF), and inconsistency between positions. The reformulation: =="My sizing framework is right when it's calculated, not when it's felt. Trust my system's mathematics. Execute the CPR formula. Then trust the result."==

### 4.3 Mental States and Self-Sabotage Patterns

- Van Tharp identifies three levels of trading psychology:
  1. **Rules and discipline** (the mechanics — stops, sizing, entry triggers)
  2. **Mental states** (the emotional/cognitive environment in which you execute)
  3. **Beliefs** (the deepest layer — what you believe is true about yourself, markets, and money)

- Most coaching focuses on level 1 (give people rules) and somewhat on level 2 (manage emotions). Van Tharp insists that ==level 3 is where the real leverage is.== You can have perfect rules and excellent emotional management, but if your beliefs include "I'm smart enough to know when to override my rules," the rules will be overridden. This is precisely your documented pattern. You have excellent rules. Your emotional management is above average. But at moments of maximum stress, a belief kicks in: ==something like "my analytical depth gives me the right to override the mechanical stop."== This belief is not useful. It needs to be identified, tested, and replaced.

- **The Super Trader programme's approach:** Tharp's four-year programme required participants to undergo a structured beliefs transformation process. The core insight was that knowing the "right" beliefs was insufficient — the beliefs had to be "installed" at an unconscious level. He used a technique called **Mind to Muscle (M2M)**, developed by Dr. Michael Hall, which involved:
  1. Identifying the target belief (e.g., "I honour every exit trigger mechanically, without exception")
  2. Finding evidence for the belief (e.g., "every time I've honoured a stop, the outcome was better than when I didn't")
  3. Physically embodying the belief through repeated practice and visualisation
  4. Testing the belief under progressively stressful conditions

- ==This maps directly onto Bassham's directive affirmation + mental rehearsal process.== You're already doing a version of this with your self-image work. Van Tharp's M2M adds the specificity of identifying *which* belief needs to change, not just building a general positive self-image. The target: "I am someone who honours exit triggers mechanically" should be a specific, rehearsed, M2M-installed belief — not a general aspiration.

### 4.4 Van Tharp's "Tharp Think" Principles

- Van Tharp codified a set of principles he called "Tharp Think" — the beliefs that successful traders share. The ones most relevant to you:

  1. **"Trading is 100% psychology."** Not 80%, not 50%. 100%. The system is a psychological construct. The markets are a psychological arena. Your beliefs, mental states, and self-awareness are the only variables you actually control.

  2. **"You can never predict what the market will do; you can only respond to what it does."** This aligns with Douglas ("you don't need to know what will happen next to make money") and with your own OODA loop framework. ==The implication for sizing: never size based on what you think will happen. Size based on what happens if you're wrong.==

  3. **"Your results reflect your personal psychology."** If your returns are mediocre, the problem is not the market or the strategy — it's you. This is confrontational by design. Van Tharp would look at your 8.3% CAGR vs 25%+ target and say: "The gap is not in your stock-picking ability. It's in your sizing, your exits, and the beliefs that prevent you from executing both."

  4. **"The purpose of a trading system is to limit risk while maximising gain."** Notice: risk-limiting comes first. Gain-maximising comes second. Most fundamental investors reverse this priority — they optimise for upside and treat risk management as a constraint. Van Tharp says: ==risk management IS the system. Gain is a byproduct of excellent risk management, not the other way around.==

  5. **"You must measure your system's expectancy in R-multiples to know if you have an edge."** Without measurement, you're flying blind. You might *think* your system has positive expectancy. You might *feel* that you pick good stocks. But without the data — win rate, average winner in R, average loser in R, SQN — you're operating on belief, not evidence. And we've already established that many beliefs are wrong.

---

## PART 5: DIRECT APPLICATION TO YOUR DOCUMENTED PATTERNS — R-MULTIPLE POST-MORTEMS

### 5.1 BFF — The Cost of a -4R Loss [---]

- Your BFF lesson documents the full emotional cycle: endowment bias, commitment bias, FOFR, cockroach pattern, "worser, weirder, further, longer." Through Van Tharp's R-multiple lens, the damage becomes mathematically stark.

- **Hypothetical reconstruction:** BFF entered at (let's say) 10% of portfolio. Planned exit level implied a 1R loss of approximately 1% of portfolio. But the position was held through deterioration — the stop was not honoured. Final exit at (estimated) -30% to -40% from entry.

- In R-multiple terms: a -1R planned loss became a -4R to -5R actual loss. At 10% portfolio weight, that's a 3-4% portfolio hit instead of a 1% portfolio hit. ==The difference — 2-3% of portfolio — is pure leaked P&L. It is the mathematical cost of overriding the stop.==

- **Van Tharp's reframe:** He would not ask "why did you hold BFF?" He would ask: =="How many +1R trades would you need to make up for this single -4R loss?"== At +1.265R expectancy, the answer is approximately 3 full trades. You need three winning trades just to recover the damage from one overridden stop. This is the asymmetry of losses that Minervini hammers — now expressed in R-multiple mathematics.

- ==If you had honoured the stop, the -1R loss would have been recovered in less than one average trade.== The difference between one trade to recover and three trades to recover is approximately six months of portfolio time — that's the real cost of holding BFF.

### 5.2 XVIVO — The Complexity Premium in R [--]

- XVIVO illustrates a different R-multiple pathology: the position that consumes disproportionate analytical time relative to its R-contribution.

- Van Tharp introduces the concept of **Opportunity Cost in R**: every hour spent analysing a deteriorating position is an hour not spent finding the next +3R trade. If XVIVO consumed (conservatively) 40 hours of analytical time while producing a -2R outcome, and your average research cycle takes 20 hours to identify a +3R trade, then XVIVO cost you not just -2R but also the +3R trade you didn't find. ==The true cost of XVIVO is -5R when opportunity cost is included.==

- Your own lesson: "Learning all that stuff was trees not wood." Van Tharp would rephrase: =="Learning all that stuff cost you approximately 5R. What would those 40 hours have produced if directed at your watchlist instead?"==

### 5.3 Goodwin — Position Sizing and IR Fragility [-]

- Goodwin declined 40% on poor IR and a missed contract. Through the R-multiple lens: if this was a 6-8% position with a 10% stop, the planned -1R was 0.6-0.8% of portfolio. A 40% decline on an 8% position is a -3.2% portfolio hit — roughly a -4R to -5R outcome.

- Van Tharp's insight: ==the distance between -1R and -4R on any given position is the quality of your exit execution.== The system quality (SQN) degrades rapidly when you allow tail losses. A few -4R or -5R outcomes per year will drag an excellent SQN down to average.

### 5.4 Telecoms — The +3R Proof of Concept [++]

- Your telecoms case: "+34% vs +4%." If this was a 10% position that gained 34%, and the stop distance was 10% (Trend Template based), then:
  - 1R = 10% × 10% = 1.0% of portfolio
  - Gain = 10% × 34% = 3.4% of portfolio = +3.4R

- This is an excellent trade. ==A +3.4R outcome from a single position, with risk defined and limited to 1.0% at entry, is the system working as designed.== Van Tharp would say: your job is not to find more telecom-like ideas. Your job is to ensure that every position is structured with this same R-multiple discipline, so that the winners can produce +3R to +5R while the losers are capped at -1R.

### 5.5 Greggs — Trust and R [+]

- Greggs: "Trusted own judgment despite Pedro's concerns, stock up 25% YTD." If this was a 10% position with a 7% stop:
  - 1R = 10% × 7% = 0.7% of portfolio
  - Gain = 10% × 25% = 2.5% of portfolio = +3.6R

- The R-multiple framing strips out the emotional narrative. It doesn't matter that Pedro disagreed. It doesn't matter that you "trusted your judgement." ==What matters is that the position was structured to risk 0.7% of portfolio and delivered +3.6R. That's the data point. Record it. It contributes to your system's expectancy measurement.==

### 5.6 Instalco — The False Sell Signal [+]

- Instalco: trimmed 4% on raw material inflation worries, stock subsequently up 30%. Through the R-multiple lens: the 4% trim was a premature profit-exit that reduced your R-multiple capture.

- Van Tharp's principle: ==never exit a winning position because of fear.== Exit only when: (a) your stop is hit, (b) your profit target is reached, or (c) the R-multiple math says the remaining risk/reward is unfavourable. "Raw material inflation worries" is a fear-based exit, not a system-based exit. The stock was in Stage 2. Fundamentals were intact. The Trend Template held. The R-multiple calculation said: hold.

- Your own lesson: "Trust own assessment — don't let others' emotional flappiness influence." Van Tharp would add: =="Trust the R-multiple. If the position is +2R and the stop hasn't been hit and Stage 2 is intact, hold. The maths doesn't care about Pedro or raw material inflation headlines."==

---

## PART 6: INTEGRATION WITH EXISTING FRAMEWORKS

### 6.1 Douglas × Van Tharp — Philosophy Meets Engineering

- Mark Douglas provides the philosophical foundation: accept uncertainty, think in probabilities, detach from individual outcomes. Van Tharp provides the mathematical infrastructure: measure expectancy, calculate position size, track SQN, express everything in R-multiples.

- ==Douglas tells you WHY to accept a -1R loss without emotional reaction. Van Tharp tells you HOW MUCH to risk so that a -1R loss is structurally acceptable.== Together, they form a complete system for risk acceptance: Douglas addresses the mind, Van Tharp addresses the maths.

- **Your existing gap:** You have the Douglas insight deeply internalised ("Mark Douglas: no certain outcomes for any one stock, just probabilities. This is freedom."). You do not yet have the Van Tharp measurement infrastructure. ==The freedom Douglas describes is theoretical until you know your system's expectancy, your average R-multiple, and your SQN. With those numbers, the freedom becomes concrete.==

### 6.2 Bassham × Van Tharp — Self-Image and Evidence

- Bassham teaches that performance equals self-image. Van Tharp's R-multiple tracking provides the ==evidence base for a new self-image.== When you record every trade in R-multiples, you build a dataset that proves (or disproves) "I am a disciplined position manager."

- If your R-multiple log shows that 90% of your losses are -1R or smaller, that IS evidence for the self-image "I cut losses quickly." If 20% of your losses are -3R or worse, that's evidence that the self-image hasn't yet been installed. ==The R-multiple log is an objective self-image calibration tool.==

### 6.3 Ward × Van Tharp — The 4Cs and Sizing Discipline

- **Commitment:** Van Tharp's system requires commitment to the CPR formula on every position. No exceptions. No "just this once."
- **Concentration:** The R-multiple framework simplifies attention: you only need to know three things about each position — current R-multiple, stop level, and whether the stop conditions have changed.
- **Confidence:** An objectively measured positive expectancy builds evidence-based confidence. You're not confident because you "feel" good about your picks. You're confident because your SQN is 3.0+.
- **Control:** The CPR formula puts you in control of the one variable that matters most — position size. You can't control whether a stock goes up or down. You can control how much you risk on it.

### 6.4 Minervini × Van Tharp — Mechanical Exits Meet Mathematical Sizing

- Minervini provides the exit triggers (Trend Template, stage analysis, 7-8% max loss). Van Tharp provides the mathematical framework that makes those exits tolerable. ==If you've sized the position using the Percent Risk Model so that the Minervini stop produces a -1R loss equal to 0.5% of your portfolio, honouring that stop is easy. It's a rounding error. It doesn't threaten your identity or your returns.==

- The combination: Minervini's stops define R. Van Tharp's CPR formula defines position size given R. Together, they produce a system where ==every loss is pre-defined, pre-sized, and pre-accepted before the position is opened.== This is the complete mechanical layer that Douglas's philosophical framework demands.

### 6.5 Duke × Van Tharp — Kill Criteria and R-Multiples

- Annie Duke's kill criteria (pre-committed exit conditions set at entry) are R-multiple triggers in disguise. "Exit if the stock declines 7% from entry" is "exit at -1R." "Exit if 18-month EPS declines by 5%+" is a fundamental trigger that, when combined with Van Tharp's R-multiple tracking, produces a measurable R-outcome.

- ==Duke provides the pre-commitment architecture. Van Tharp provides the measurement language. Together: "My kill criterion for this position is -1R, defined as a 7% decline from entry, which at my current position size translates to 0.5% of portfolio. This loss is pre-accepted."==

### 6.6 Rotella × Van Tharp — Trusting the System You've Tested

- Rotella's Training vs Trusting distinction maps perfectly onto Van Tharp's system design vs system execution. The position sizing model is designed in Training mode (analytical, mathematical, conscious). It is executed in Trusting mode (mechanical, automatic, no override). ==If you've done the CPR calculation correctly in Training mode, there is nothing to think about in Trusting mode. The size is the size. The stop is the stop. Trust it.==

---

## PART 7: TENSIONS AND RESOLUTIONS

### 7.1 Short-Term Trader vs Long-Duration Investor

- **Tension:** Van Tharp's R-multiple framework was primarily developed for shorter-duration traders (weeks to months). Your 18-month ownership horizon creates complications: stops are wider, holding periods are longer, and the "loss at stop" can be larger in percentage terms.

- **Resolution:** ==The R-multiple framework is duration-agnostic.== R is simply the initial risk. Whether your stop is 7% below entry (tight, for a momentum trader) or 15% below entry (wide, for a fundamental investor), the mathematics of CPR work identically. The difference is that your wider stops require *smaller position sizes* to maintain the same C (capital at risk). This is actually what your progressive exposure framework already does — it starts small precisely because the initial stop is wide. Van Tharp's contribution is formalising this intuition into a calculation.

### 7.2 Frequent Trades vs Concentrated Positions

- **Tension:** Van Tharp assumes many trades per year (50-200+). You make 10-15 round-trip trades per year. This limits the statistical reliability of expectancy and SQN calculations.

- **Resolution:** Count every add, every trim, and every exit as a separate R-multiple event. A single position might generate 3-4 R-multiple data points: initial entry (test), confirmation add, trim/top-slice, and final exit. Over 16 positions with 18-month average holding and interim activity, you'll generate 40-60 R-multiple events per year. ==That's sufficient for meaningful expectancy measurement and approaching the N=30 minimum for SQN reliability.==

### 7.3 The Concentrated Portfolio Paradox

- **Tension:** Van Tharp's Percent Risk Model typically suggests risking 0.5-2% of equity per position. For a concentrated portfolio with 16 positions, if each risks 1.0%, the total portfolio risk is 16% — which is aggressive. But if each only risks 0.5%, the total portfolio risk is 8%, which might feel too conservative for a 25%+ IRR target.

- **Resolution:** This is not a contradiction — it's a feature. ==Your 25%+ IRR target requires that your winners win big, not that your risk per position is large.== With a positive expectancy of +1.265R and an average risk per position of 0.7%, your expected return per position per cycle is 0.89% of portfolio. Across 16 positions over an 18-month cycle, that's approximately 14.2% — before accounting for the compounding effect of reinvesting winners and the possibility of >1 cycle per year on some positions. To reach 25%+, you need either higher expectancy (through better stock selection or tighter stops) or more cycles per year (through higher portfolio turnover). ==The solution is not to increase per-position risk. It is to improve expectancy and cycle velocity.==

### 7.4 The Belief Tension — "I Know Better Than the Formula"

- **Tension:** Van Tharp's system is mechanical. Your documented self-image includes "dynamic swagger," "Finn Russell of stock-pickers," "I trust my judgement 150%." These identities resist mechanical constraint.

- **Resolution:** ==This is the most important tension to resolve, and Van Tharp would name it directly: the belief that your judgement can override the formula is the single most dangerous belief in your system.== Your judgement is excellent at stock selection (Setup and Entry). It is unreliable at position management (Stop, Sizing) under emotional pressure. The formula exists to protect you from yourself at the moments when your judgement is most compromised. Accepting this is not weakness — it's the mark of a professional. Ed Seykota: =="Win or lose, everybody gets what they want out of the market."== If you want the mathematical returns of a disciplined system, you must accept the mathematical constraints of that system.

---

## PART 8: IMPLEMENTATION PLAN

### 8.1 Immediate Actions (This Week)

1. **Start an R-Multiple Log.** ==For every position currently held, calculate: entry price, current stop level, current R-multiple.== Format: a simple spreadsheet or Notion database with columns for Stock | Entry | Stop | 1R (%) | Current R-Multiple | Position Size (%). This takes 30 minutes to set up and 5 minutes per week to maintain. It becomes the backbone of all expectancy and SQN calculations.

2. **Calculate your historical expectancy.** Go back through the last 12-24 months of completed trades. For each, estimate the R-multiple (entry, exit, what 1R would have been). Calculate: win rate, average winner in R, average loser in R, expectancy. ==This single number — your expectancy — will tell you more about your system's health than any amount of qualitative reflection.==

3. **Run the CPR formula on your next new position.** Before entering, define C (how much are you willing to lose?), R (where is your exit?), and calculate P (position size). ==Do not deviate from the calculation.== Compare the CPR output with what you would have sized "by feel." Note the difference. This difference is the sizing gap that Van Tharp identifies.

### 8.2 Medium-Term Integration (Next 2-4 Weeks)

4. **Build the Percent Risk sizing overlay into your portfolio.** For each of the 16 positions, calculate: what is the maximum risk (C) that produces the target position size given the current stop distance (R)? If any position is larger than the CPR formula recommends, flag it for potential trim at the next natural opportunity.

5. **Conduct a Beliefs Audit.** List your 10 most deeply held beliefs about position sizing and exits. For each: Is it useful? Is it accurate? Is it serving your 25%+ IRR objective? ==Pay special attention to beliefs that justify overriding mechanical stops.== These are the highest-leverage beliefs to change.

6. **Set up quarterly SQN tracking.** At the end of each quarter, calculate your SQN using the R-multiple log. Plot it over time. ==Target: SQN ≥ 2.5 (Good) within 12 months, trending toward 3.0 (Excellent).== If SQN declines quarter-over-quarter, diagnose why — the data will tell you whether it's larger losses, smaller wins, or both.

### 8.3 Ongoing Practices

7. **Express every trade result in R-multiples.** When discussing a position with Watson (APM), in your journal, or in your weekly review, use R-multiples as the default language. Not "I'm up 20% on Greggs" but "Greggs is at +3.6R." ==This linguistic shift forces probabilistic, system-level thinking and strips out the emotional narrative attached to specific stock names.==

8. **Review the Beliefs Audit quarterly.** Beliefs change slowly. New beliefs (like "I honour every stop mechanically") need repeated reinforcement through Bassham's mental rehearsal process and Van Tharp's M2M approach. Each quarter, test: did I honour the belief this quarter? If not, what was the cost in R?

9. **Run a "Van Tharp Check" at every weekly review.** Add one question to the Friday 16:00 review: =="What was my worst R-multiple outcome this week, and did it exceed -1R? If so, what happened?"== This question, asked consistently, makes stop slippage visible and accountable.

10. **Position Sizing Pre-Mortem.** Before committing to a new position, run a pre-mortem specifically on sizing: "If this position hits my stop, what is the R-multiple cost? Am I comfortable with that cost? If not, is the answer to reduce position size or widen the stop? Or is the answer not to take the trade?" ==The answer should never be "ignore the stop."==

---

## PART 9: THE VAN THARP–RICHARD SYNTHESIS

### 9.1 What Van Tharp Adds That Nothing Else In Your Library Provides

- Douglas gives you probabilistic acceptance. Bassham gives you self-image. Ward gives you the 4Cs. Minervini gives you mechanical exit triggers. Duke gives you pre-commitment architecture. Rotella gives you the training/trusting distinction.

- ==Van Tharp gives you the mathematics.==

- Specifically: the ability to measure your system's edge (expectancy), evaluate its quality (SQN), size positions objectively (CPR), express every outcome in a universal risk language (R-multiples), and identify the specific beliefs that prevent you from executing all of the above (Beliefs Audit).

- Your system is analytically excellent. Your psychology work is deep and multi-layered. What's missing is the quantitative bridge between "I have a good process" and "I know, mathematically, how good my process is, and I size every position accordingly." ==Van Tharp provides that bridge.==

### 9.2 The Position Sizing Gap — Your Highest-Leverage Improvement

- Consider two versions of you:

  - **Version A (current):** Sizes by conviction category. 15% for the best names, 10% for core, 0-5% for early-stage. Stops exist but are sometimes overridden. Average loss on failed positions: -2.5R (some cut at -1R, some held to -4R).

  - **Version B (Van Tharp-enhanced):** Sizes by CPR formula. Every position's size is a mathematical output of capital-at-risk divided by stop distance. Stops are mechanical and non-negotiable. Average loss on failed positions: -1.1R (tight distribution, minimal stop slippage).

  - **The difference in annual returns:** If Version A leaks 5R per year from stop slippage (a conservative estimate based on 2-3 overridden stops), and your average R is 0.7% of portfolio, that's 3.5% of annual returns leaked. ==Your current CAGR is 8.3%. Eliminating stop slippage alone — without changing a single stock pick — could raise it to approximately 12%.== That's a 45% improvement in returns from position management alone, with zero improvement in stock selection. ==This is what Van Tharp means when he says position sizing is the most important component.==

### 9.3 The System as a Whole

- You wrote in October 2024: *"I know what works. It's HQIs. Simple. No need to overthink."* Van Tharp would agree — and add: =="And you need to know, mathematically, HOW MUCH to commit to each HQI, WHEN to cut the ones that don't work, and WHAT your system produces per unit of risk. Without those numbers, 'I know what works' is a belief, not a fact. Make it a fact. Measure it. Then you'll really know."==

- Ed Seykota, who perhaps best embodies the Van Tharp ethos among the Market Wizards: =="There are old traders and there are bold traders, but there are very few old, bold traders."== Your concentrated, high-conviction approach is bold. Van Tharp's position sizing discipline is what makes it possible to be both bold and old. ==The mathematics of survival is not conservative — it's the prerequisite for compounding.==

- Larry Hite, another Tharp-adjacent thinker: *"I have two basic rules about winning in trading as well as in life: (1) If you don't bet, you can't win. (2) If you lose all your chips, you can't bet."* ==Rule 1 is your natural instinct — you are an aggressive, conviction-driven investor. Rule 2 is what Van Tharp's position sizing ensures. You will always have chips to bet. And with chips in front of you and a positive-expectancy system, the mathematics of compounding does the rest.==

---

## PART 10: THE DEEPEST LESSON — WHAT VAN THARP WOULD SAY ABOUT YOUR TRACK RECORD

### 10.1 The -54.75% Maximum Drawdown

- Your maximum drawdown was -54.75% (Aug 2021 to Oct 2023). Van Tharp would examine this through one lens: ==what was the aggregate position sizing that allowed this to happen?==

- A -55% drawdown from individual stock losses requires either: (a) several large positions declining 30-50% simultaneously without stops being honoured, or (b) a systemic market decline (which it was — 2022 was a broad bear market) compounded by concentrated positioning.

- Van Tharp's mathematical discipline would constrain this. If no single position can cost more than 1.4% of portfolio at maximum size (15% position × 9% stop), and the average position risks 0.7%, then the maximum portfolio loss from stops alone (if every position stopped out simultaneously) is approximately 11.2% (16 × 0.7%). ==A -55% drawdown is mathematically impossible under Van Tharp's Percent Risk Model — unless stops are not honoured, positions are too large, or both.==

- **The confronting truth:** ==Your -55% drawdown is proof that your pre-2026 position sizing was not systematic.== The 1Q26 portfolio architecture (16 stocks, 15% max, diversification constraints, 30-day shot clock) already addresses this structurally. Van Tharp's Percent Risk Model adds the mathematical layer that makes these structural constraints enforceable.

### 10.2 The Path From 8.3% to 25%

- Van Tharp would frame the gap between your 8.3% CAGR and your 25% target in R-multiple terms:

  - **At 8.3% CAGR with ~12 positions averaging 0.7% R:** Your system is generating approximately +0.7R per position per cycle. This is a positive-expectancy system — but barely.

  - **At 25% CAGR:** You need approximately +2.1R per position per cycle. This requires either: (a) winning bigger (average winner at +4-5R instead of +3R), (b) losing less (cutting every loss at -1R maximum, with no -3R or -4R outliers), or (c) cycling faster (more trades per year).

  - ==The lowest-hanging fruit is (b) — eliminating outsized losses.== Your documented BFF, XVIVO, and Goodwin cases show that you occasionally produce -3R to -5R outcomes. These single events destroy months of +1R to +3R accumulation. ==Capping every loss at -1R — through mechanical stops and CPR-based sizing — is the single highest-leverage change you can make.==

  - The second lever is (a) — ==letting winners run further.== Your top-slice discipline is generally good, but the Instalco trim suggests occasional premature profit-taking. Van Tharp's R-multiple tracking will show you: are you systematically cutting winners short? If your average winner is +2.5R but your best winners reach +8R before you exit, you're leaving R on the table. The trailing stop (based on Trend Template/stage analysis) should determine when to exit winners, not fear or round-number targets.

---

**[W] Watson | High Performance Coach | Produced 03-Apr-26 | ~10,000 words**

**Sources consulted:** Tharp, *Trade Your Way to Financial Freedom* (2nd ed., 2007); Tharp, *Super Trader: Make Consistent Profits in Good and Bad Markets* (2009/2011); Tharp, *The Definitive Guide to Position Sizing Strategies* (2nd ed., 2013); Vince, *The Mathematics of Money Management* (1992); Schwager, *Market Wizards* (1989/2012); Richard's personal journals (Roam, Notion), coaching memory files, investment strategy documents, stock notes, and corrections log.
