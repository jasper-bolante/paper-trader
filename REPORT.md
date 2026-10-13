# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-13 19:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,690.83** |
| Total return since inception | 3.45% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,938.23 (4.69%) |
| Positions value | $18,947.44 |
| Settled cash | $1,168.93 |
| Unsettled cash (T+1) | $589.33 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.61% | 4.51% |
| Annualized volatility | 10.85% | 11.01% |
| Sharpe (rf 4%) | 0.58 | 1.20 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 68 | 68 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $204.14 | $816.56 | $49.44 | $195.06 |
| APA | 19 | $44.15 | $47.95 | $911.05 | $72.16 | $42.17 |
| CRL | 3 | $296.67 | $299.18 | $897.54 | $7.52 | $279.86 |
| DDOG | 2 | $283.76 | $283.61 | $567.22 | $-0.30 | $255.25 |
| FFIV | 2 | $448.44 | $476.06 | $952.11 | $55.22 | $431.75 |
| IQV | 2 | $255.46 | $260.58 | $521.16 | $10.25 | $247.54 |
| META | 1 | $723.49 | $763.29 | $763.29 | $39.80 | $668.72 |
| MPC | 3 | $399.06 | $476.95 | $1,430.85 | $233.68 | $417.31 |
| NTAP | 5 | $206.27 | $238.85 | $1,194.25 | $162.90 | $215.29 |
| PSX | 5 | $215.50 | $292.42 | $1,462.10 | $384.62 | $253.62 |
| RVTY | 9 | $122.75 | $155.28 | $1,397.52 | $292.80 | $141.67 |
| SPY | 5 | $743.10 | $777.89 | $3,889.45 | $173.95 | — |
| TECH | 12 | $72.32 | $72.48 | $869.76 | $1.92 | $65.36 |
| VLO | 3 | $392.61 | $456.95 | $1,370.85 | $193.03 | $399.71 |
| WST | 2 | $370.69 | $371.73 | $743.46 | $2.08 | $339.09 |
| ZBRA | 3 | $345.13 | $386.75 | $1,160.26 | $124.88 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,197.33 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-07T23:43` system — eod_complete
- `2026-10-07T19:28` entry buy **META** — momentum entry: rank 20, mom 0.344, vol 47%
- `2026-10-07T19:28` entry buy **AMD** — momentum entry: rank 2, mom 1.073, vol 49%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
