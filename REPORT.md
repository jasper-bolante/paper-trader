# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 19:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,685.75** |
| Total return since inception | -1.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,349.96 |
| Settled cash | $2,331.21 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.38% | 2.46% |
| Annualized volatility | 12.31% | 13.20% |
| Sharpe (rf 4%) | -1.85 | 1.26 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 32 | 32 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.30 | $736.26 | $-27.35 | $25.00 |
| BBY | 14 | $88.05 | $86.39 | $1,209.46 | $-23.29 | $80.33 |
| CRL | 2 | $285.12 | $294.92 | $589.83 | $19.59 | $262.31 |
| CSX | 17 | $50.29 | $51.46 | $874.82 | $19.87 | $46.01 |
| EXPE | 2 | $331.47 | $323.18 | $646.35 | $-16.59 | $298.17 |
| FDS | 2 | $299.76 | $298.78 | $597.56 | $-1.97 | $269.64 |
| IQV | 2 | $255.46 | $258.60 | $517.19 | $6.28 | $230.53 |
| MPC | 3 | $306.56 | $363.67 | $1,091.01 | $171.33 | $330.10 |
| NTAP | 5 | $161.48 | $193.81 | $969.08 | $161.70 | $186.39 |
| PANW | 2 | $388.17 | $357.79 | $715.57 | $-60.77 | $313.89 |
| PSX | 5 | $215.50 | $244.22 | $1,221.08 | $143.60 | $219.13 |
| SPY | 5 | $743.10 | $766.21 | $3,831.05 | $115.55 | — |
| STT | 8 | $185.86 | $186.72 | $1,493.76 | $6.89 | $173.64 |
| VEEV | 3 | $250.82 | $248.59 | $745.78 | $-6.69 | $225.63 |
| VLO | 3 | $304.72 | $349.90 | $1,049.70 | $135.54 | $315.01 |
| WST | 3 | $336.32 | $353.82 | $1,061.46 | $52.50 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-21T19:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:07` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:58` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:03` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T16:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T16:00` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T15:05` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T15:05` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T14:08` entry buy **FDS** — momentum entry: rank 8, mom 0.452, vol 50%
- `2026-08-21T14:08` entry buy **PANW** — momentum entry: rank 1, mom 1.067, vol 45%
- `2026-08-20T20:58` system — eod_complete
- `2026-08-20T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T19:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
