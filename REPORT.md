# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-15 21:40 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,351.59** |
| Total return since inception | 1.76% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,769.21 (3.85%) |
| Positions value | $18,169.82 |
| Settled cash | $1,110.01 |
| Unsettled cash (T+1) | $1,086.62 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.69% | 3.66% |
| Annualized volatility | 11.00% | 11.04% |
| Sharpe (rf 4%) | 0.24 | 0.87 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 71 | 71 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $47.23 | $897.37 | $58.48 | $43.21 |
| CRL | 3 | $296.67 | $306.48 | $919.43 | $29.41 | $279.86 |
| DDOG | 2 | $283.76 | $264.00 | $528.00 | $-39.52 | $255.25 |
| FFIV | 2 | $448.44 | $456.49 | $912.98 | $16.09 | $431.75 |
| FTNT | 3 | $185.45 | $181.96 | $545.88 | $-10.48 | $166.82 |
| IQV | 2 | $255.46 | $271.19 | $542.38 | $31.47 | $247.54 |
| META | 1 | $723.49 | $736.58 | $736.58 | $13.09 | $686.26 |
| MPC | 3 | $399.06 | $476.59 | $1,429.77 | $232.60 | $436.32 |
| NTAP | 4 | $214.92 | $214.68 | $858.72 | $-0.95 | $193.37 |
| PSX | 5 | $215.50 | $289.10 | $1,445.50 | $368.02 | $267.61 |
| RVTY | 9 | $122.75 | $154.70 | $1,392.30 | $287.58 | $141.67 |
| SPY | 5 | $743.10 | $771.68 | $3,858.40 | $142.90 | — |
| TECH | 12 | $72.32 | $72.54 | $870.48 | $2.64 | $65.36 |
| VLO | 3 | $392.61 | $444.43 | $1,333.28 | $155.46 | $413.91 |
| WST | 2 | $370.69 | $383.13 | $766.26 | $24.88 | $344.82 |
| ZBRA | 3 | $345.13 | $377.50 | $1,132.50 | $97.12 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,141.40 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-15T17:51` entry buy **NTAP** — momentum entry: rank 1, mom 0.872, vol 46%
- `2026-10-15T17:51` exit sell **NTAP** — trailing stop 10%
- `2026-10-14T21:53` system — eod_complete
- `2026-10-14T18:08` entry buy **FTNT** — momentum entry: rank 2, mom 0.753, vol 41%
- `2026-10-14T18:08` exit sell **ANET** — trailing stop 10%
- `2026-10-13T23:49` system — eod_complete
- `2026-10-13T19:56` entry buy **DDOG** — momentum entry: rank 3, mom 0.725, vol 49%
- `2026-10-13T19:56` no_trade skip_entry **MU** — insufficient investable cash (size $687, need >= $500)
- `2026-10-13T19:56` exit sell **AMD** — trailing stop 10%
- `2026-10-12T21:49` system — eod_complete
- `2026-10-09T23:25` system — eod_complete
- `2026-10-09T23:25` system — corporate_actions_synced
- `2026-10-09T18:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-09T18:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-09T18:57` system **NTAP** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
