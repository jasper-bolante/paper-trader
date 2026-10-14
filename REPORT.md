# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-14 21:53 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,435.53** |
| Total return since inception | 2.18% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,692.77 (3.46%) |
| Positions value | $18,468.67 |
| Settled cash | $1,189.86 |
| Unsettled cash (T+1) | $791.86 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.11% | 3.28% |
| Annualized volatility | 11.05% | 11.10% |
| Sharpe (rf 4%) | 0.38 | 0.76 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 70 | 70 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $47.38 | $900.22 | $61.33 | $43.21 |
| CRL | 3 | $296.67 | $301.90 | $905.70 | $15.68 | $279.86 |
| DDOG | 2 | $283.76 | $269.29 | $538.58 | $-28.94 | $255.25 |
| FFIV | 2 | $448.44 | $457.18 | $914.35 | $17.46 | $431.75 |
| FTNT | 3 | $185.45 | $184.11 | $552.33 | $-4.03 | $166.82 |
| IQV | 2 | $255.46 | $262.10 | $524.20 | $13.29 | $247.54 |
| META | 1 | $723.49 | $737.46 | $737.46 | $13.97 | $686.26 |
| MPC | 3 | $399.06 | $484.80 | $1,454.40 | $257.23 | $436.32 |
| NTAP | 5 | $206.27 | $222.25 | $1,111.25 | $79.90 | $215.29 |
| PSX | 5 | $215.50 | $297.35 | $1,486.73 | $409.25 | $267.61 |
| RVTY | 9 | $122.75 | $152.17 | $1,369.53 | $264.81 | $141.67 |
| SPY | 5 | $743.10 | $768.84 | $3,844.20 | $128.70 | — |
| TECH | 12 | $72.32 | $72.52 | $870.24 | $2.40 | $65.36 |
| VLO | 3 | $392.61 | $459.90 | $1,379.70 | $201.88 | $413.91 |
| WST | 2 | $370.69 | $374.83 | $749.66 | $8.28 | $339.09 |
| ZBRA | 3 | $345.13 | $376.71 | $1,130.13 | $94.75 | $349.27 |

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
