# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-04 22:29 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,612.57** |
| Total return since inception | -1.94% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,728.84 (3.64%) |
| Positions value | $17,452.71 |
| Settled cash | $2,161.54 |
| Unsettled cash (T+1) | $8.94 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.00% | 3.46% |
| Annualized volatility | 11.33% | 11.95% |
| Sharpe (rf 4%) | -1.37 | 1.43 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 43 | 43 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.80 | $722.40 | $-41.21 | $25.00 |
| CRL | 2 | $285.12 | $288.84 | $577.68 | $7.44 | $268.70 |
| DASH | 4 | $228.34 | $211.67 | $846.68 | $-66.66 | $205.31 |
| FDS | 2 | $299.76 | $302.07 | $604.14 | $4.61 | $282.41 |
| FTNT | 4 | $170.05 | $156.25 | $625.00 | $-55.19 | $140.76 |
| HPE | 16 | $53.55 | $52.00 | $832.00 | $-24.84 | $48.99 |
| HUM | 2 | $426.49 | $401.22 | $802.44 | $-50.53 | $371.57 |
| IQV | 2 | $255.46 | $267.67 | $535.34 | $24.43 | $244.26 |
| MPC | 3 | $306.56 | $389.28 | $1,167.84 | $248.16 | $350.35 |
| NTAP | 5 | $206.27 | $185.59 | $927.95 | $-103.40 | $167.03 |
| PSX | 5 | $215.50 | $254.97 | $1,274.85 | $197.37 | $230.41 |
| SPY | 5 | $743.10 | $770.18 | $3,850.90 | $135.40 | — |
| STT | 8 | $185.86 | $194.31 | $1,554.44 | $67.57 | $174.87 |
| TECH | 12 | $72.32 | $72.42 | $869.10 | $1.26 | $65.20 |
| TGT | 7 | $162.82 | $164.35 | $1,150.45 | $10.74 | $147.91 |
| VLO | 3 | $304.72 | $370.50 | $1,111.50 | $197.34 | $333.54 |

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
