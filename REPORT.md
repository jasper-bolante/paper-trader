# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-30 22:32 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,669.83** |
| Total return since inception | -1.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,552.01 (2.76%) |
| Positions value | $18,325.26 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.72% | 2.58% |
| Annualized volatility | 10.96% | 11.43% |
| Sharpe (rf 4%) | -0.99 | 0.66 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 60 | 60 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $203.67 | $814.68 | $47.56 | $185.84 |
| APA | 19 | $44.15 | $41.54 | $789.26 | $-49.63 | $39.73 |
| BBY | 8 | $101.21 | $88.22 | $705.72 | $-103.96 | $85.36 |
| CRL | 3 | $296.67 | $295.62 | $886.85 | $-3.17 | $266.50 |
| FFIV | 2 | $448.44 | $445.33 | $890.66 | $-6.23 | $403.38 |
| IQV | 2 | $255.46 | $268.92 | $537.84 | $26.93 | $247.54 |
| MPC | 3 | $399.06 | $395.71 | $1,187.13 | $-10.04 | $358.97 |
| NTAP | 5 | $206.27 | $210.09 | $1,050.42 | $19.08 | $189.08 |
| PSX | 5 | $215.50 | $255.25 | $1,276.25 | $198.77 | $246.58 |
| RVTY | 9 | $122.75 | $152.95 | $1,376.55 | $271.83 | $137.66 |
| SPY | 5 | $743.10 | $763.61 | $3,818.05 | $102.55 | — |
| TECH | 12 | $72.32 | $72.49 | $869.88 | $2.04 | $65.36 |
| TGT | 7 | $162.82 | $156.62 | $1,096.38 | $-43.34 | $147.91 |
| VLO | 3 | $392.61 | $387.83 | $1,163.49 | $-14.33 | $352.71 |
| WST | 2 | $370.69 | $370.69 | $741.37 | $-0.01 | $338.99 |
| ZBRA | 3 | $345.13 | $373.58 | $1,120.74 | $85.36 | $338.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-30T18:31` no_trade — no signals crossed action thresholds this hour
- `2026-09-30T18:31` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-29T23:08` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
