# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-04 16:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,673.03** |
| Total return since inception | -1.63% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,807.83 (4.04%) |
| Positions value | $17,513.17 |
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
| BAX | 28 | $27.27 | $26.04 | $728.98 | $-34.63 | $25.00 |
| CRL | 2 | $285.12 | $290.51 | $581.02 | $10.78 | $268.70 |
| DASH | 4 | $228.34 | $214.90 | $859.58 | $-53.76 | $205.31 |
| FDS | 2 | $299.76 | $303.20 | $606.40 | $6.87 | $282.41 |
| FTNT | 4 | $170.05 | $156.42 | $625.68 | $-54.51 | $140.76 |
| HPE | 16 | $53.55 | $52.81 | $844.96 | $-11.88 | $48.99 |
| HUM | 2 | $426.49 | $403.67 | $807.34 | $-45.63 | $371.57 |
| IQV | 2 | $255.46 | $268.11 | $536.22 | $25.31 | $244.26 |
| MPC | 3 | $306.56 | $389.21 | $1,167.63 | $247.95 | $348.75 |
| NTAP | 5 | $206.27 | $185.47 | $927.35 | $-104.00 | $166.92 |
| PSX | 5 | $215.50 | $256.46 | $1,282.30 | $204.82 | $230.41 |
| SPY | 5 | $743.10 | $770.95 | $3,854.75 | $139.25 | — |
| STT | 8 | $185.86 | $194.52 | $1,556.16 | $69.29 | $174.54 |
| TECH | 12 | $72.32 | $72.42 | $869.04 | $1.20 | $65.20 |
| TGT | 7 | $162.82 | $164.26 | $1,149.82 | $10.11 | $147.57 |
| VLO | 3 | $304.72 | $371.98 | $1,115.94 | $201.78 | $333.54 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,000.13 | $0.00 | $814.06 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-02T17:16` exit sell **FTNT** — trailing stop 10%
- `2026-09-01T20:07` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
