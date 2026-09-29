# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-29 23:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,657.85** |
| Total return since inception | -1.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,572.74 (2.86%) |
| Positions value | $18,313.28 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 2.68% |
| Annualized volatility | 11.05% | 11.53% |
| Sharpe (rf 4%) | -1.01 | 0.71 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 59 | 59 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $202.88 | $811.52 | $44.40 | $185.84 |
| APA | 19 | $44.15 | $42.21 | $801.99 | $-36.90 | $39.73 |
| BBY | 8 | $101.21 | $88.74 | $709.92 | $-99.76 | $85.36 |
| CRL | 3 | $296.67 | $296.11 | $888.33 | $-1.69 | $266.50 |
| FFIV | 2 | $448.44 | $438.01 | $876.02 | $-20.87 | $403.38 |
| IQV | 2 | $255.46 | $269.22 | $538.44 | $27.53 | $247.54 |
| MPC | 3 | $399.06 | $391.93 | $1,175.79 | $-21.38 | $358.97 |
| NTAP | 5 | $206.27 | $209.23 | $1,046.15 | $14.80 | $188.31 |
| PSX | 5 | $215.50 | $252.05 | $1,260.25 | $182.77 | $246.58 |
| RVTY | 9 | $122.75 | $152.76 | $1,374.88 | $270.16 | $137.49 |
| SPY | 5 | $743.10 | $764.38 | $3,821.90 | $106.40 | — |
| TECH | 12 | $72.32 | $72.37 | $868.44 | $0.60 | $65.36 |
| TGT | 7 | $162.82 | $156.41 | $1,094.87 | $-44.84 | $147.91 |
| VLO | 3 | $392.61 | $387.96 | $1,163.89 | $-13.92 | $352.71 |
| WST | 2 | $370.69 | $376.66 | $753.32 | $11.94 | $338.99 |
| ZBRA | 3 | $345.13 | $375.86 | $1,127.57 | $92.18 | $338.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-29T23:08` system — corporate_actions_synced
- `2026-09-29T18:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-29T18:49` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-28T20:12` system — eod_complete
- `2026-09-25T21:46` system — eod_complete
- `2026-09-25T18:03` entry buy **WST** — momentum entry: rank 15, mom 0.333, vol 21%
- `2026-09-25T18:03` entry buy **FFIV** — momentum entry: rank 14, mom 0.335, vol 38%
- `2026-09-25T18:03` no_trade skip_entry **INCY** — sector cap: Health Care would exceed 25% of equity
- `2026-09-25T18:03` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-09-24T21:43` system — eod_complete
- `2026-09-24T17:55` entry buy **VLO** — momentum entry: rank 2, mom 0.681, vol 32%
- `2026-09-24T17:55` entry buy **MPC** — momentum entry: rank 1, mom 0.714, vol 30%
- `2026-09-23T21:42` system — eod_complete
- `2026-09-23T17:56` no_trade skip_entry **SOLV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **EXPD** — insufficient investable cash (size $37, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
