# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-23 21:42 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,555.14** |
| Total return since inception | -2.22% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,661.82 (3.31%) |
| Positions value | $14,197.31 |
| Settled cash | $1,029.50 |
| Unsettled cash (T+1) | $4,342.80 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.29% | 3.13% |
| Annualized volatility | 11.40% | 11.78% |
| Sharpe (rf 4%) | -1.24 | 0.94 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 55 | 55 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $203.34 | $813.36 | $46.24 | $185.09 |
| APA | 19 | $44.15 | $43.70 | $830.30 | $-8.59 | $39.73 |
| BBY | 8 | $101.21 | $90.81 | $726.52 | $-83.16 | $85.36 |
| CRL | 3 | $296.67 | $277.50 | $832.50 | $-57.52 | $256.69 |
| IQV | 2 | $255.46 | $268.18 | $536.36 | $25.45 | $244.26 |
| NTAP | 5 | $206.27 | $196.32 | $981.60 | $-49.75 | $179.40 |
| PSX | 5 | $215.50 | $256.29 | $1,281.45 | $203.97 | $246.58 |
| RVTY | 9 | $122.75 | $142.13 | $1,279.21 | $174.49 | $132.06 |
| SPY | 5 | $743.10 | $767.69 | $3,838.45 | $122.95 | — |
| TECH | 12 | $72.32 | $72.53 | $870.30 | $2.46 | $65.30 |
| TGT | 7 | $162.82 | $156.29 | $1,094.03 | $-45.68 | $147.91 |
| ZBRA | 3 | $345.13 | $371.07 | $1,113.22 | $77.84 | $333.97 |

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
