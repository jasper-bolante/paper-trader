# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 16:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,690.14** |
| Total return since inception | -1.55% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,354.35 |
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
| BAX | 28 | $27.27 | $26.43 | $739.90 | $-23.71 | $25.00 |
| BBY | 14 | $88.05 | $87.48 | $1,224.79 | $-7.96 | $80.33 |
| CRL | 2 | $285.12 | $297.04 | $594.07 | $23.83 | $262.31 |
| CSX | 17 | $50.29 | $51.37 | $873.29 | $18.34 | $46.01 |
| EXPE | 2 | $331.47 | $323.46 | $646.92 | $-16.02 | $298.17 |
| FDS | 2 | $299.76 | $301.15 | $602.31 | $2.78 | $269.64 |
| IQV | 2 | $255.46 | $258.73 | $517.46 | $6.55 | $230.53 |
| MPC | 3 | $306.56 | $362.20 | $1,086.62 | $166.94 | $330.10 |
| NTAP | 5 | $161.48 | $194.17 | $970.85 | $163.47 | $186.39 |
| PANW | 2 | $388.17 | $356.13 | $712.27 | $-64.07 | $313.89 |
| PSX | 5 | $215.50 | $242.38 | $1,211.88 | $134.39 | $219.13 |
| SPY | 5 | $743.10 | $767.18 | $3,835.92 | $120.42 | — |
| STT | 8 | $185.86 | $186.18 | $1,489.44 | $2.57 | $173.64 |
| VEEV | 3 | $250.82 | $249.76 | $749.28 | $-3.19 | $225.63 |
| VLO | 3 | $304.72 | $347.70 | $1,043.12 | $128.96 | $315.01 |
| WST | 3 | $336.32 | $352.08 | $1,056.24 | $47.28 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-21T16:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T16:00` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T15:05` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T15:05` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T14:08` entry buy **FDS** — momentum entry: rank 8, mom 0.452, vol 50%
- `2026-08-21T14:08` entry buy **PANW** — momentum entry: rank 1, mom 1.067, vol 45%
- `2026-08-20T20:58` system — eod_complete
- `2026-08-20T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T19:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
