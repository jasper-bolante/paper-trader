# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-06 01:29 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,121.63** |
| Total return since inception | -4.39% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,703.17 (-1.48%) |
| Positions value | $12,721.75 |
| Settled cash | $6,410.16 |
| Unsettled cash (T+1) | $5.38 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -4.46% | -1.66% |
| Annualized volatility | 12.52% | 13.92% |
| Sharpe (rf 4%) | -1.34 | -0.57 |
| Max drawdown | 7.74% | 6.06% |
| EOD observations | 86 | 86 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $107.87 | $1,078.70 | $19.22 | $100.89 |
| IT | 4 | $220.40 | $197.79 | $791.16 | $-90.43 | $186.37 |
| MPC | 2 | $428.77 | $377.44 | $754.88 | $-102.67 | $351.03 |
| PSX | 4 | $274.37 | $246.97 | $987.88 | $-109.58 | $233.77 |
| RVTY | 9 | $122.75 | $150.85 | $1,357.65 | $252.93 | $149.17 |
| SPY | 5 | $743.10 | $730.52 | $3,652.60 | $-62.90 | — |
| TECH | 12 | $72.32 | $72.67 | $872.10 | $4.26 | $65.47 |
| VEEV | 4 | $305.03 | $310.07 | $1,240.28 | $20.16 | $279.52 |
| WDAY | 6 | $194.97 | $200.34 | $1,202.04 | $32.24 | $181.66 |
| WST | 2 | $370.69 | $392.23 | $784.46 | $43.08 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-973.47 | $0.00 | $1,512.22 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-06T01:29` system — corporate_actions_synced
- `2026-11-05T20:47` no_trade — no signals crossed action thresholds this hour
- `2026-11-05T20:47` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-05T20:47` system — drawdown_state
- `2026-11-05T01:00` system — eod_complete
- `2026-11-04T20:31` entry buy **PSX** — momentum entry: rank 5, mom 0.462, vol 35%
- `2026-11-04T20:31` entry buy **MPC** — momentum entry: rank 3, mom 0.643, vol 40%
- `2026-11-04T20:31` no_trade skip_entry **HUM** — insufficient investable cash (size $870, need >= $500)
- `2026-11-04T20:31` exit sell **NTAP** — momentum rank decayed (None > 150 or ineligible: volatility 0.5383352861062571 above cap 0.5)
- `2026-11-04T20:31` exit sell **PSX** — trailing stop 10%
- `2026-11-04T20:31` exit sell **MPC** — trailing stop 10%
- `2026-11-04T00:48` system — eod_complete
- `2026-11-04T00:48` system — corporate_actions_synced
- `2026-11-03T20:14` entry buy **IT** — momentum entry: rank 6, mom 0.518, vol 44%
- `2026-11-03T20:14` entry buy **VEEV** — momentum entry: rank 2, mom 0.782, vol 31%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
