# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 14:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,723.41** |
| Total return since inception | -1.38% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $16,788.31 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $1,586.68 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.50% | 3.32% |
| Annualized volatility | 12.28% | 13.14% |
| Sharpe (rf 4%) | -1.30 | 1.85 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 31 | 31 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.62 | $745.36 | $-18.25 | $25.00 |
| BBY | 14 | $88.05 | $87.17 | $1,220.45 | $-12.30 | $80.33 |
| CRL | 2 | $285.12 | $292.31 | $584.61 | $14.37 | $260.98 |
| CSX | 17 | $50.29 | $50.97 | $866.41 | $11.46 | $46.01 |
| EXPE | 2 | $331.47 | $324.92 | $649.84 | $-13.10 | $298.17 |
| IQV | 2 | $255.46 | $255.32 | $510.64 | $-0.27 | $229.79 |
| MPC | 3 | $306.56 | $367.38 | $1,102.12 | $182.45 | $330.10 |
| NTAP | 5 | $161.48 | $194.75 | $973.75 | $166.37 | $186.39 |
| PANW | 2 | $388.28 | $357.50 | $715.00 | $-61.56 | $349.27 |
| PSX | 5 | $215.50 | $246.20 | $1,231.00 | $153.52 | $219.13 |
| SPY | 5 | $743.10 | $766.42 | $3,832.10 | $116.60 | — |
| STT | 8 | $185.86 | $186.65 | $1,493.20 | $6.33 | $173.64 |
| VEEV | 3 | $250.82 | $250.69 | $752.07 | $-0.40 | $225.62 |
| VLO | 3 | $304.72 | $350.10 | $1,050.30 | $136.14 | $315.01 |
| WST | 3 | $336.32 | $353.82 | $1,061.46 | $52.50 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-20T14:09` exit sell **FTNT** — trailing stop 10%
- `2026-08-19T20:56` system — eod_complete
- `2026-08-19T20:56` system — corporate_actions_synced
- `2026-08-19T19:51` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T19:51` no_trade skip_entry **WSM** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **NUE** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **APA** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TGT** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **BKNG** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TECH** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **IQV** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **VEEV** — insufficient investable cash (size $374, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
