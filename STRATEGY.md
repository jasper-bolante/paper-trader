# Strategy & Account Mechanics

Objective: **maximum gains under medium risk** — implemented as the
"conservative-medium" profile confirmed on 2026-07-07. Simulated $20,000
cash account, decisions once per hour during US regular sessions.

## Medium risk, operationally defined

| Constraint | Value |
|---|---|
| Permanent broad-index ballast | ~20% in SPY (rebalanced outside a 15–25% band) |
| Stock positions | 10–15 targets (12 nominal) |
| Max single position | 10% of equity at purchase; trimmed if it grows past 14% |
| Max sector concentration | 25% of equity (GICS sector, at purchase) |
| Cash buffer | ≥5% settled cash never deployed |
| Per-position stop | 10% trailing off the highest close since entry |
| Portfolio drawdown brakes | −7% from high-water mark: no new buys · −12%: halve the stock sleeve · −15%: liquidate everything and halt until manual resume |
| Churn limits | max 2 new positions/day; 3-trading-day minimum hold (stop-outs exempt) |
| Out of scope | shorting, options, margin/leverage, crypto, leveraged/inverse ETFs, stocks under $10, stocks with >50% annualized 30-day volatility, stocks trading <$10M/day |

## Signal model

- **Universe**: S&P 500 constituents (snapshot in `data/universe.csv`).
- **Momentum score**: 0.5 × 3-month return + 0.5 × 6-month return, skipping
  the most recent 5 trading days (short-term reversal noise). Computed daily
  from split-adjusted daily bars through the previous close — no lookahead.
- **Trend filter**: price above a rising 50-day moving average to enter.
- **Entry**: top-50 momentum rank, all filters pass, capacity and risk
  limits allow. Sizing is volatility-scaled (reference 30% annualized vol,
  scaling clamped to 0.6–1.2×) around an equal-weight base of
  (80% sleeve ÷ 12 positions).
- **Exit**: momentum rank decays past 150, close below the 100-day average,
  or the trailing stop triggers. Exits except stops respect the minimum hold.

The hourly cadence is deliberately mostly idle: signals update daily;
intra-day runs monitor stops, settle cash, process corporate actions, and
log a reasoned "no trade" decision when nothing crosses a threshold.

## Execution / fill model (no instant mid-price fills)

- Buys pay the **ask**, sells receive the **bid** (live IEX quotes); if no
  sane quote exists, a 5 bps half-spread is synthesized around the last
  trade. Quoted spreads wider than 75 bps are treated as unusable.
- **Market impact**: `k · daily_vol · sqrt(order_value / ADV$)` added on
  top — negligible for small orders in liquid names, grows with order size
  and volatility.
- **Entries** are marketable limit orders capped at ask × 1.001.
- **Limit orders** fill only when price trades *through* the limit
  (touch ≠ fill: models queue position).
- **Stops** are working orders evaluated each run against minute bars since
  the last check; a gap through the stop fills off the gap open, not the
  stop price.
- Fills are capped at 10% of observed traded volume in the evaluation
  window; the rest stays working.

## Account mechanics

- **Settlement**: T+1. Sale proceeds and dividends are tracked with settle
  dates; **buys only ever spend settled cash** (stricter than a real cash
  account, and good-faith violations are impossible by construction).
- **No margin, no leverage, no shorting.**
- **PDT**: not modeled. FINRA eliminated the pattern-day-trader rule
  effective 2026-06-04 (Regulatory Notice 26-10), and it never applied to
  cash accounts. The settlement rules above are what actually binds this
  account, plus the strategy's own churn limits.
- **Lots**: FIFO. Term is long if held >365 days (holding period can be
  tacked back by wash-sale adjustments).
- **Wash sales**: losses matched share-for-share against purchases within
  ±30 days (both directions); disallowed losses raise the replacement lot's
  basis and tack its holding period. Each replacement share absorbs at most
  one wash.
- **Tax drag** (assumed rates, applied as a standing reserve that reduces
  both reported equity and investable cash): **24%** short-term, **15%**
  long-term, **15%** dividends, no state tax. ST/LT net per IRS ordering
  with loss carryforward; the $3k ordinary-income offset is ignored.
- **Corporate actions**: splits rescale lots/stops on the ex-date with
  cash-in-lieu for fractionals; dividends accrue at the ex-date holding and
  settle on the pay date.

## Benchmark & metrics

- Benchmark: **$20,000 of SPY bought at inception** at the ask, dividends
  reinvested net of the 15% dividend tax, never sold. Fractional shares
  allowed (it's a yardstick, not a tradable account).
- Metrics from EOD snapshots: total return, annualized volatility, Sharpe
  (flat 4% risk-free assumption), max drawdown — portfolio vs. benchmark.

## Known approximations (accepted, by design)

- IEX quotes only (free feed): ~2–3% of consolidated volume; spreads can
  read slightly wider than NBBO. Conservative rather than flattering.
- Stops are monitored hourly; same-day triggers between runs fill using the
  minute-bar history, but a trigger in the last ~25 minutes of a session is
  handled at the next morning's prices (gap logic applies).
- Dividend entitlement uses holdings at the moment the ex-date is first
  processed, not the exact ex-date open.
- The universe is a periodic snapshot; index changes lag until refreshed.
- Taxes are reserved continuously rather than paid each April.
