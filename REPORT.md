# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-29 18:49 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,646.52** |
| Total return since inception | -1.77% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,603.96 (3.02%) |
| Positions value | $18,301.95 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.85% | 2.84% |
| Annualized volatility | 11.15% | 11.62% |
| Sharpe (rf 4%) | -1.05 | 0.78 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 58 | 58 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $203.29 | $813.18 | $46.06 | $185.84 |
| APA | 19 | $44.15 | $41.99 | $797.81 | $-41.08 | $39.73 |
| BBY | 8 | $101.21 | $89.02 | $712.16 | $-97.52 | $85.36 |
| CRL | 3 | $296.67 | $293.64 | $880.92 | $-9.10 | $265.10 |
| FFIV | 2 | $448.44 | $440.68 | $881.36 | $-15.53 | $403.38 |
| IQV | 2 | $255.46 | $269.19 | $538.38 | $27.47 | $247.54 |
| MPC | 3 | $399.06 | $392.80 | $1,178.40 | $-18.77 | $358.97 |
| NTAP | 5 | $206.27 | $208.65 | $1,043.23 | $11.88 | $184.04 |
| PSX | 5 | $215.50 | $251.82 | $1,259.10 | $181.62 | $246.58 |
| RVTY | 9 | $122.75 | $152.19 | $1,369.66 | $264.94 | $136.00 |
| SPY | 5 | $743.10 | $764.72 | $3,823.60 | $108.10 | — |
| TECH | 12 | $72.32 | $72.41 | $868.86 | $1.02 | $65.36 |
| TGT | 7 | $162.82 | $157.09 | $1,099.63 | $-40.08 | $147.91 |
| VLO | 3 | $392.61 | $388.03 | $1,164.09 | $-13.73 | $352.71 |
| WST | 2 | $370.69 | $375.52 | $751.04 | $9.66 | $338.27 |
| ZBRA | 3 | $345.13 | $373.51 | $1,120.53 | $85.15 | $334.58 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-23T17:56` no_trade skip_entry **ADP** — insufficient investable cash (size $37, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
