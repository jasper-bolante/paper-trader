# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 20:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,537.53** |
| Total return since inception | -2.31% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $15,904.31 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $2,284.80 |
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
| BAX | 28 | $27.27 | $26.41 | $739.34 | $-24.27 | $25.00 |
| BBY | 14 | $88.05 | $85.75 | $1,200.57 | $-32.18 | $80.33 |
| CRL | 2 | $285.12 | $291.45 | $582.90 | $12.66 | $262.31 |
| CSX | 17 | $50.29 | $50.97 | $866.41 | $11.46 | $46.01 |
| EXPE | 2 | $331.47 | $324.40 | $648.80 | $-14.14 | $298.17 |
| IQV | 2 | $255.46 | $256.14 | $512.28 | $1.37 | $230.53 |
| MPC | 3 | $306.56 | $358.16 | $1,074.48 | $154.80 | $330.10 |
| NTAP | 5 | $161.48 | $192.74 | $963.70 | $156.32 | $186.39 |
| PSX | 5 | $215.50 | $240.01 | $1,200.05 | $122.57 | $219.13 |
| SPY | 5 | $743.10 | $762.72 | $3,813.60 | $98.10 | — |
| STT | 8 | $185.86 | $183.01 | $1,464.12 | $-22.75 | $173.64 |
| VEEV | 3 | $250.82 | $250.69 | $752.09 | $-0.38 | $225.63 |
| VLO | 3 | $304.72 | $341.45 | $1,024.35 | $110.19 | $315.01 |
| WST | 3 | $336.32 | $353.88 | $1,061.62 | $52.66 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,136.32 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T19:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
