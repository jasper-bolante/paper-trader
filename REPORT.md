# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-23 17:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,564.94** |
| Total return since inception | -2.18% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.58 (4.05%) |
| Positions value | $14,207.11 |
| Settled cash | $1,029.50 |
| Unsettled cash (T+1) | $4,342.80 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.58% | 3.86% |
| Annualized volatility | 11.41% | 11.77% |
| Sharpe (rf 4%) | -0.96 | 1.25 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 54 | 54 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $202.47 | $809.88 | $42.76 | $185.09 |
| APA | 19 | $44.15 | $43.59 | $828.21 | $-10.68 | $39.73 |
| BBY | 8 | $101.21 | $92.09 | $736.76 | $-72.92 | $85.36 |
| CRL | 3 | $296.67 | $277.88 | $833.64 | $-56.38 | $256.69 |
| IQV | 2 | $255.46 | $268.41 | $536.82 | $25.91 | $244.26 |
| NTAP | 5 | $206.27 | $197.35 | $986.75 | $-44.60 | $179.40 |
| PSX | 5 | $215.50 | $253.43 | $1,267.12 | $189.64 | $246.58 |
| RVTY | 9 | $122.75 | $141.70 | $1,275.30 | $170.58 | $132.06 |
| SPY | 5 | $743.10 | $768.38 | $3,841.90 | $126.40 | — |
| TECH | 12 | $72.32 | $72.54 | $870.48 | $2.64 | $65.30 |
| TGT | 7 | $162.82 | $156.94 | $1,098.58 | $-41.13 | $147.91 |
| ZBRA | 3 | $345.13 | $373.89 | $1,121.67 | $86.29 | $325.24 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-23T17:56` no_trade skip_entry **SOLV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **EXPD** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **ADP** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **WAT** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **FFIV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **TMO** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **VLO** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **MPC** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` exit sell **GEN** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **VLO** — trailing stop 10%
- `2026-09-23T17:56` exit sell **MPC** — trailing stop 10%
- `2026-09-22T21:36` system — eod_complete
- `2026-09-22T17:43` no_trade — no signals crossed action thresholds this hour
- `2026-09-22T17:43` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
