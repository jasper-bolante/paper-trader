# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-25 21:46 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,677.78** |
| Total return since inception | -1.61% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,756.56 (3.78%) |
| Positions value | $18,333.21 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.68% | 3.60% |
| Annualized volatility | 11.24% | 11.60% |
| Sharpe (rf 4%) | -0.98 | 1.08 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 57 | 57 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $206.49 | $825.96 | $58.84 | $185.84 |
| APA | 19 | $44.15 | $42.73 | $811.87 | $-27.02 | $39.73 |
| BBY | 8 | $101.21 | $90.51 | $724.08 | $-85.60 | $85.36 |
| CRL | 3 | $296.67 | $292.78 | $878.34 | $-11.68 | $265.03 |
| FFIV | 2 | $448.44 | $443.00 | $886.01 | $-10.88 | $403.38 |
| IQV | 2 | $255.46 | $270.26 | $540.52 | $29.61 | $247.54 |
| MPC | 3 | $399.06 | $393.26 | $1,179.78 | $-17.39 | $358.97 |
| NTAP | 5 | $206.27 | $201.23 | $1,006.15 | $-25.20 | $181.11 |
| PSX | 5 | $215.50 | $255.70 | $1,278.50 | $201.02 | $246.58 |
| RVTY | 9 | $122.75 | $151.11 | $1,359.99 | $255.27 | $136.00 |
| SPY | 5 | $743.10 | $771.21 | $3,856.05 | $140.55 | — |
| TECH | 12 | $72.32 | $72.62 | $871.44 | $3.60 | $65.36 |
| TGT | 7 | $162.82 | $157.43 | $1,102.01 | $-37.70 | $147.91 |
| VLO | 3 | $392.61 | $387.10 | $1,161.29 | $-16.53 | $352.71 |
| WST | 2 | $370.69 | $370.58 | $741.16 | $-0.22 | $333.52 |
| ZBRA | 3 | $345.13 | $370.02 | $1,110.06 | $74.68 | $333.97 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-23T17:56` no_trade skip_entry **WAT** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **FFIV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **TMO** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **VLO** — insufficient investable cash (size $37, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
