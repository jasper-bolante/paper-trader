# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-03 20:04 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,735.72** |
| Total return since inception | -1.32% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,807.83 (4.04%) |
| Positions value | $16,648.02 |
| Settled cash | $1,130.86 |
| Unsettled cash (T+1) | $1,967.46 |
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
| BAX | 28 | $27.27 | $25.56 | $715.68 | $-47.93 | $25.00 |
| CRL | 2 | $285.12 | $293.29 | $586.58 | $16.34 | $268.70 |
| DASH | 4 | $228.34 | $221.96 | $887.84 | $-25.50 | $205.31 |
| FDS | 2 | $299.76 | $312.82 | $625.64 | $26.11 | $282.41 |
| FTNT | 4 | $170.05 | $156.40 | $625.60 | $-54.59 | $140.76 |
| HPE | 16 | $53.55 | $54.43 | $870.88 | $14.04 | $48.99 |
| HUM | 2 | $426.49 | $406.49 | $812.98 | $-39.99 | $371.57 |
| IQV | 2 | $255.46 | $271.40 | $542.80 | $31.89 | $244.26 |
| MPC | 3 | $306.56 | $387.50 | $1,162.50 | $242.82 | $348.75 |
| PSX | 5 | $215.50 | $254.31 | $1,271.55 | $194.07 | $230.41 |
| SPY | 5 | $743.10 | $773.12 | $3,865.57 | $150.07 | — |
| STT | 8 | $185.86 | $193.93 | $1,551.44 | $64.57 | $174.54 |
| TECH | 12 | $72.32 | $72.45 | $869.40 | $1.56 | $65.20 |
| TGT | 7 | $162.82 | $163.97 | $1,147.76 | $8.05 | $147.57 |
| VLO | 3 | $304.72 | $370.60 | $1,111.80 | $197.64 | $333.54 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,103.64 | $0.00 | $710.55 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-01T20:07` system **TGT** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T20:07` system — corporate_actions_synced

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
