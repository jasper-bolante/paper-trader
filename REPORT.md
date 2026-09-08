# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-08 20:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,616.81** |
| Total return since inception | -1.92% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,617.95 (3.09%) |
| Positions value | $16,465.01 |
| Settled cash | $1,012.13 |
| Unsettled cash (T+1) | $2,150.29 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.98% | 2.91% |
| Annualized volatility | 11.19% | 11.90% |
| Sharpe (rf 4%) | -1.35 | 1.13 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 44 | 44 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 24 | $27.11 | $24.87 | $596.88 | $-53.65 | $22.38 |
| CRL | 2 | $285.12 | $280.86 | $561.72 | $-8.52 | $268.70 |
| EXPE | 2 | $303.37 | $274.46 | $548.93 | $-57.81 | $249.03 |
| FDS | 2 | $299.76 | $288.91 | $577.82 | $-21.71 | $282.41 |
| HPE | 16 | $53.55 | $56.05 | $896.80 | $39.96 | $50.45 |
| HUM | 2 | $426.49 | $403.00 | $806.00 | $-46.97 | $371.57 |
| IQV | 2 | $255.46 | $259.31 | $518.62 | $7.71 | $244.26 |
| MPC | 3 | $306.56 | $398.07 | $1,194.21 | $274.53 | $358.26 |
| NTAP | 5 | $206.27 | $189.11 | $945.55 | $-85.80 | $170.20 |
| PSX | 5 | $215.50 | $259.17 | $1,295.85 | $218.37 | $233.25 |
| SPY | 5 | $743.10 | $766.06 | $3,830.30 | $114.80 | — |
| STT | 8 | $185.86 | $191.89 | $1,535.12 | $48.25 | $174.87 |
| TECH | 12 | $72.32 | $72.31 | $867.72 | $-0.12 | $65.20 |
| TGT | 7 | $162.82 | $162.78 | $1,139.49 | $-0.22 | $147.91 |
| VLO | 3 | $304.72 | $383.33 | $1,149.99 | $235.83 | $345.00 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,108.07 | $0.00 | $921.91 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-08T17:23` entry buy **BAX** — momentum entry: rank 13, mom 0.337, vol 42%
- `2026-09-08T17:23` entry buy **EXPE** — momentum entry: rank 5, mom 0.493, vol 49%
- `2026-09-08T17:23` no_trade skip_entry **DASH** — insufficient investable cash (size $615, need >= $500)
- `2026-09-08T17:23` exit sell **FTNT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-08T17:23` exit sell **DASH** — trailing stop 10%
- `2026-09-08T17:23` exit sell **BAX** — trailing stop 10%
- `2026-09-04T22:29` system — eod_complete
- `2026-09-04T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-04T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-09-04T16:59` entry buy **NTAP** — momentum entry: rank 3, mom 0.631, vol 35%
- `2026-09-03T20:04` system — eod_complete
- `2026-09-03T20:04` system — corporate_actions_synced
- `2026-09-03T17:08` entry buy **HUM** — momentum entry: rank 3, mom 0.749, vol 35%
- `2026-09-03T17:08` entry buy **HPE** — momentum entry: rank 1, mom 1.081, vol 49%
- `2026-09-03T17:08` exit sell **HPE** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
