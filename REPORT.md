# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 19:49 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,687.00** |
| Total return since inception | -1.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,351.21 |
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
| BAX | 28 | $27.27 | $26.18 | $733.04 | $-30.57 | $25.00 |
| BBY | 14 | $88.05 | $86.41 | $1,209.74 | $-23.01 | $80.33 |
| CRL | 2 | $285.12 | $296.17 | $592.34 | $22.10 | $262.31 |
| CSX | 17 | $50.29 | $51.55 | $876.35 | $21.40 | $46.01 |
| EXPE | 2 | $331.47 | $324.00 | $648.00 | $-14.94 | $298.17 |
| FDS | 2 | $299.76 | $299.79 | $599.58 | $0.05 | $269.64 |
| IQV | 2 | $255.46 | $260.10 | $520.19 | $9.28 | $230.53 |
| MPC | 3 | $306.56 | $362.85 | $1,088.55 | $168.87 | $330.10 |
| NTAP | 5 | $161.48 | $192.88 | $964.40 | $157.02 | $186.39 |
| PANW | 2 | $388.17 | $360.02 | $720.04 | $-56.30 | $313.89 |
| PSX | 5 | $215.50 | $243.81 | $1,219.08 | $141.60 | $219.13 |
| SPY | 5 | $743.10 | $766.74 | $3,833.70 | $118.20 | — |
| STT | 8 | $185.86 | $186.68 | $1,493.40 | $6.53 | $173.64 |
| VEEV | 3 | $250.82 | $248.93 | $746.79 | $-5.68 | $225.63 |
| VLO | 3 | $304.72 | $349.50 | $1,048.50 | $134.34 | $315.01 |
| WST | 3 | $336.32 | $352.50 | $1,057.51 | $48.55 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-21T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
