# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-25 18:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,602.32** |
| Total return since inception | -1.99% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,651.06 (3.26%) |
| Positions value | $18,257.75 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.88% | 3.07% |
| Annualized volatility | 11.34% | 11.67% |
| Sharpe (rf 4%) | -1.06 | 0.90 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 56 | 56 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $208.79 | $835.16 | $68.04 | $185.14 |
| APA | 19 | $44.15 | $42.47 | $806.93 | $-31.96 | $39.73 |
| BBY | 8 | $101.21 | $90.96 | $727.68 | $-82.00 | $85.36 |
| CRL | 3 | $296.67 | $292.24 | $876.72 | $-13.30 | $265.03 |
| FFIV | 2 | $448.44 | $448.20 | $896.40 | $-0.49 | $403.38 |
| IQV | 2 | $255.46 | $271.86 | $543.72 | $32.81 | $247.54 |
| MPC | 3 | $399.06 | $386.01 | $1,158.05 | $-39.12 | $358.97 |
| NTAP | 5 | $206.27 | $199.57 | $997.85 | $-33.50 | $179.40 |
| PSX | 5 | $215.50 | $251.95 | $1,259.75 | $182.27 | $246.58 |
| RVTY | 9 | $122.75 | $149.03 | $1,341.27 | $236.55 | $135.64 |
| SPY | 5 | $743.10 | $771.10 | $3,855.50 | $140.00 | — |
| TECH | 12 | $72.32 | $72.59 | $871.14 | $3.30 | $65.30 |
| TGT | 7 | $162.82 | $157.15 | $1,100.02 | $-39.69 | $147.91 |
| VLO | 3 | $392.61 | $377.20 | $1,131.60 | $-46.22 | $352.71 |
| WST | 2 | $370.69 | $370.50 | $740.99 | $-0.39 | $333.45 |
| ZBRA | 3 | $345.13 | $371.66 | $1,114.98 | $79.60 | $333.97 |

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
