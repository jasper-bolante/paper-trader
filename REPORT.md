# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-14 18:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,448.09** |
| Total return since inception | 2.24% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,940.12 (4.70%) |
| Positions value | $18,481.23 |
| Settled cash | $1,189.86 |
| Unsettled cash (T+1) | $791.86 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 3.37% | 4.52% |
| Annualized volatility | 10.86% | 10.93% |
| Sharpe (rf 4%) | 0.82 | 1.19 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 69 | 69 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $47.78 | $907.91 | $69.02 | $43.21 |
| CRL | 3 | $296.67 | $304.49 | $913.47 | $23.45 | $279.86 |
| DDOG | 2 | $283.76 | $273.40 | $546.80 | $-20.72 | $255.25 |
| FFIV | 2 | $448.44 | $458.81 | $917.61 | $20.72 | $431.75 |
| FTNT | 3 | $185.45 | $185.35 | $556.06 | $-0.30 | $166.82 |
| IQV | 2 | $255.46 | $262.39 | $524.78 | $13.87 | $247.54 |
| META | 1 | $723.49 | $736.38 | $736.38 | $12.89 | $686.26 |
| MPC | 3 | $399.06 | $479.15 | $1,437.45 | $240.28 | $429.50 |
| NTAP | 5 | $206.27 | $222.86 | $1,114.30 | $82.95 | $215.29 |
| PSX | 5 | $215.50 | $295.03 | $1,475.15 | $397.67 | $263.41 |
| RVTY | 9 | $122.75 | $153.61 | $1,382.49 | $277.77 | $141.67 |
| SPY | 5 | $743.10 | $767.90 | $3,839.50 | $124.00 | — |
| TECH | 12 | $72.32 | $72.53 | $870.36 | $2.52 | $65.36 |
| VLO | 3 | $392.61 | $458.51 | $1,375.53 | $197.71 | $410.73 |
| WST | 2 | $370.69 | $375.96 | $751.92 | $10.54 | $339.09 |
| ZBRA | 3 | $345.13 | $377.17 | $1,131.51 | $96.13 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,184.63 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-08T23:52` system — eod_complete
- `2026-10-08T19:23` no_trade — no signals crossed action thresholds this hour
- `2026-10-08T19:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
