# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 17:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,698.55** |
| Total return since inception | -1.51% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $16,763.45 |
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
| BAX | 28 | $27.27 | $26.34 | $737.66 | $-25.95 | $25.00 |
| BBY | 14 | $88.05 | $86.33 | $1,208.55 | $-24.20 | $80.33 |
| CRL | 2 | $285.12 | $295.13 | $590.27 | $20.03 | $260.98 |
| CSX | 17 | $50.29 | $51.26 | $871.34 | $16.38 | $46.01 |
| EXPE | 2 | $331.47 | $327.50 | $655.00 | $-7.94 | $298.17 |
| IQV | 2 | $255.46 | $259.33 | $518.66 | $7.75 | $229.79 |
| MPC | 3 | $306.56 | $364.02 | $1,092.06 | $172.38 | $330.10 |
| NTAP | 5 | $161.48 | $195.80 | $979.00 | $171.62 | $186.39 |
| PANW | 2 | $388.28 | $354.12 | $708.24 | $-68.32 | $349.27 |
| PSX | 5 | $215.50 | $243.93 | $1,219.65 | $142.17 | $219.13 |
| SPY | 5 | $743.10 | $766.08 | $3,830.38 | $114.88 | — |
| STT | 8 | $185.86 | $185.91 | $1,487.32 | $0.45 | $173.64 |
| VEEV | 3 | $250.82 | $252.12 | $756.36 | $3.89 | $225.62 |
| VLO | 3 | $304.72 | $346.09 | $1,038.27 | $124.11 | $315.01 |
| WST | 3 | $336.32 | $356.90 | $1,070.70 | $61.74 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-20T14:09` exit sell **FTNT** — trailing stop 10%
- `2026-08-19T20:56` system — eod_complete
- `2026-08-19T20:56` system — corporate_actions_synced
- `2026-08-19T19:51` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T19:51` no_trade skip_entry **WSM** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **NUE** — insufficient investable cash (size $374, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
