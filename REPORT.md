# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-24 17:55 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,689.93** |
| Total return since inception | -1.55% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,661.82 (3.31%) |
| Positions value | $16,707.09 |
| Settled cash | $2,971.41 |
| Unsettled cash (T+1) | $25.90 |
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
| ANET | 4 | $191.78 | $204.36 | $817.44 | $50.32 | $185.09 |
| APA | 19 | $44.15 | $44.17 | $839.23 | $0.34 | $39.73 |
| BBY | 8 | $101.21 | $91.18 | $729.44 | $-80.24 | $85.36 |
| CRL | 3 | $296.67 | $294.50 | $883.50 | $-6.52 | $256.69 |
| IQV | 2 | $255.46 | $272.05 | $544.10 | $33.19 | $244.26 |
| MPC | 3 | $399.06 | $398.85 | $1,196.55 | $-0.62 | $358.97 |
| NTAP | 5 | $206.27 | $197.98 | $989.90 | $-41.45 | $179.40 |
| PSX | 5 | $215.50 | $262.69 | $1,313.45 | $235.97 | $246.58 |
| RVTY | 9 | $122.75 | $146.30 | $1,316.70 | $211.98 | $132.06 |
| SPY | 5 | $743.10 | $766.53 | $3,832.65 | $117.15 | — |
| TECH | 12 | $72.32 | $72.58 | $870.96 | $3.12 | $65.30 |
| TGT | 7 | $162.82 | $156.85 | $1,097.98 | $-41.73 | $147.91 |
| VLO | 3 | $392.61 | $391.90 | $1,175.71 | $-2.11 | $352.71 |
| ZBRA | 3 | $345.13 | $366.49 | $1,099.47 | $64.09 | $333.97 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-23T17:56` no_trade skip_entry **MPC** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` exit sell **GEN** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **VLO** — trailing stop 10%
- `2026-09-23T17:56` exit sell **MPC** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
