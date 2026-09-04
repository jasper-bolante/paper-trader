# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-04 19:49 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,605.70** |
| Total return since inception | -1.97% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,807.83 (4.04%) |
| Positions value | $17,445.84 |
| Settled cash | $2,161.54 |
| Unsettled cash (T+1) | $8.94 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.39% | 3.86% |
| Annualized volatility | 11.37% | 12.04% |
| Sharpe (rf 4%) | -1.05 | 1.66 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 42 | 42 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.93 | $725.90 | $-37.71 | $25.00 |
| CRL | 2 | $285.12 | $289.02 | $578.04 | $7.80 | $268.70 |
| DASH | 4 | $228.34 | $212.24 | $848.96 | $-64.38 | $205.31 |
| FDS | 2 | $299.76 | $300.26 | $600.52 | $0.99 | $282.41 |
| FTNT | 4 | $170.05 | $156.06 | $624.24 | $-55.95 | $140.76 |
| HPE | 16 | $53.55 | $52.03 | $832.48 | $-24.36 | $48.99 |
| HUM | 2 | $426.49 | $400.35 | $800.70 | $-52.27 | $371.57 |
| IQV | 2 | $255.46 | $267.76 | $535.52 | $24.61 | $244.26 |
| MPC | 3 | $306.56 | $388.97 | $1,166.91 | $247.23 | $348.75 |
| NTAP | 5 | $206.27 | $185.56 | $927.80 | $-103.55 | $166.92 |
| PSX | 5 | $215.50 | $254.65 | $1,273.23 | $195.75 | $230.41 |
| SPY | 5 | $743.10 | $770.10 | $3,850.50 | $135.00 | — |
| STT | 8 | $185.86 | $194.25 | $1,554.00 | $67.13 | $174.54 |
| TECH | 12 | $72.32 | $72.42 | $868.98 | $1.14 | $65.20 |
| TGT | 7 | $162.82 | $164.22 | $1,149.51 | $9.80 | $147.57 |
| VLO | 3 | $304.72 | $369.52 | $1,108.56 | $194.40 | $333.54 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,000.13 | $0.00 | $814.06 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-04T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-04T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-09-04T16:59` entry buy **NTAP** — momentum entry: rank 3, mom 0.631, vol 35%
- `2026-09-03T20:04` system — eod_complete
- `2026-09-03T20:04` system — corporate_actions_synced
- `2026-09-03T17:08` entry buy **HUM** — momentum entry: rank 3, mom 0.749, vol 35%
- `2026-09-03T17:08` entry buy **HPE** — momentum entry: rank 1, mom 1.081, vol 49%
- `2026-09-03T17:08` exit sell **HPE** — trailing stop 10%
- `2026-09-03T17:08` exit sell **NTAP** — trailing stop 10%
- `2026-09-03T17:08` exit sell **EXPE** — trailing stop 10%
- `2026-09-02T20:03` system — eod_complete
- `2026-09-02T17:16` entry buy **FTNT** — momentum entry: rank 7, mom 0.595, vol 48%
- `2026-09-02T17:16` entry buy **HPE** — momentum entry: rank 1, mom 1.022, vol 50%
- `2026-09-02T17:16` no_trade skip_entry **HUM** — insufficient investable cash (size $771, need >= $500)
- `2026-09-02T17:16` exit sell **CSX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
