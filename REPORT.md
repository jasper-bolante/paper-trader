# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-11 17:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,637.39** |
| Total return since inception | -1.81% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,397.52 (1.99%) |
| Positions value | $17,466.32 |
| Settled cash | $1,043.36 |
| Unsettled cash (T+1) | $1,138.33 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.12% | 1.81% |
| Annualized volatility | 11.13% | 11.80% |
| Sharpe (rf 4%) | -1.90 | 0.57 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 46 | 46 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CRL | 2 | $285.12 | $277.52 | $555.04 | $-15.20 | $268.70 |
| FDS | 3 | $293.49 | $259.34 | $778.02 | $-102.44 | $253.30 |
| HUM | 2 | $426.49 | $408.96 | $817.92 | $-35.05 | $371.57 |
| INCY | 6 | $122.55 | $122.42 | $734.52 | $-0.75 | $110.18 |
| IQV | 2 | $255.46 | $261.87 | $523.73 | $12.82 | $244.26 |
| MPC | 3 | $306.56 | $403.07 | $1,209.21 | $289.53 | $359.56 |
| NTAP | 5 | $206.27 | $194.75 | $973.75 | $-57.60 | $170.20 |
| PAYX | 8 | $115.18 | $115.29 | $922.32 | $0.87 | $103.66 |
| PSX | 5 | $215.50 | $262.04 | $1,310.20 | $232.72 | $234.77 |
| RVTY | 9 | $122.75 | $123.69 | $1,113.21 | $8.49 | $111.51 |
| SPY | 5 | $743.10 | $765.73 | $3,828.65 | $113.15 | — |
| STT | 8 | $185.86 | $193.80 | $1,550.40 | $63.53 | $174.87 |
| TECH | 12 | $72.32 | $72.34 | $868.08 | $0.24 | $65.20 |
| TGT | 7 | $162.82 | $156.49 | $1,095.43 | $-44.28 | $147.91 |
| VLO | 3 | $304.72 | $395.28 | $1,185.84 | $271.68 | $350.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,160.54 | $0.00 | $957.59 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-11T17:08` entry buy **INCY** — momentum entry: rank 12, mom 0.309, vol 27%
- `2026-09-11T17:08` no_trade skip_entry **NUE** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **CF** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **ADP** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **GEN** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **GPN** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **GPC** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **MRK** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **APA** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` exit sell **EXPE** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-11T17:08` exit sell **BAX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-10T22:44` system — eod_complete
- `2026-09-10T19:59` no_trade — no signals crossed action thresholds this hour
- `2026-09-10T19:59` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-09-10T17:07` entry buy **FDS** — momentum entry: rank 13, mom 0.282, vol 42%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
