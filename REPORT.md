# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-13 23:49 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,688.91** |
| Total return since inception | 3.44% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,940.12 (4.70%) |
| Positions value | $18,945.51 |
| Settled cash | $1,168.93 |
| Unsettled cash (T+1) | $589.33 |
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
| ANET | 4 | $191.78 | $204.50 | $818.00 | $50.88 | $195.06 |
| APA | 19 | $44.15 | $48.01 | $912.19 | $73.30 | $43.21 |
| CRL | 3 | $296.67 | $299.04 | $897.12 | $7.10 | $279.86 |
| DDOG | 2 | $283.76 | $282.37 | $564.74 | $-2.78 | $255.25 |
| FFIV | 2 | $448.44 | $476.20 | $952.40 | $55.51 | $431.75 |
| IQV | 2 | $255.46 | $260.49 | $520.97 | $10.06 | $247.54 |
| META | 1 | $723.49 | $762.51 | $762.51 | $39.02 | $686.26 |
| MPC | 3 | $399.06 | $477.22 | $1,431.66 | $234.49 | $429.50 |
| NTAP | 5 | $206.27 | $238.89 | $1,194.45 | $163.10 | $215.29 |
| PSX | 5 | $215.50 | $292.68 | $1,463.40 | $385.92 | $263.41 |
| RVTY | 9 | $122.75 | $155.08 | $1,395.72 | $291.00 | $141.67 |
| SPY | 5 | $743.10 | $778.03 | $3,890.15 | $174.65 | — |
| TECH | 12 | $72.32 | $72.50 | $869.94 | $2.10 | $65.36 |
| VLO | 3 | $392.61 | $456.37 | $1,369.11 | $191.29 | $410.73 |
| WST | 2 | $370.69 | $371.52 | $743.05 | $1.67 | $339.09 |
| ZBRA | 3 | $345.13 | $386.70 | $1,160.10 | $124.72 | $349.27 |

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
