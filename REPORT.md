# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 17:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,681.88** |
| Total return since inception | -1.59% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,346.08 |
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
| BAX | 28 | $27.27 | $26.34 | $737.38 | $-26.23 | $25.00 |
| BBY | 14 | $88.05 | $86.75 | $1,214.50 | $-18.25 | $80.33 |
| CRL | 2 | $285.12 | $297.63 | $595.27 | $25.03 | $262.31 |
| CSX | 17 | $50.29 | $51.44 | $874.39 | $19.44 | $46.01 |
| EXPE | 2 | $331.47 | $323.12 | $646.25 | $-16.69 | $298.17 |
| FDS | 2 | $299.76 | $298.99 | $597.98 | $-1.55 | $269.64 |
| IQV | 2 | $255.46 | $258.74 | $517.48 | $6.57 | $230.53 |
| MPC | 3 | $306.56 | $361.85 | $1,085.54 | $165.86 | $330.10 |
| NTAP | 5 | $161.48 | $193.64 | $968.20 | $160.82 | $186.39 |
| PANW | 2 | $388.17 | $357.13 | $714.26 | $-62.08 | $313.89 |
| PSX | 5 | $215.50 | $242.84 | $1,214.20 | $136.72 | $219.13 |
| SPY | 5 | $743.10 | $766.25 | $3,831.28 | $115.78 | — |
| STT | 8 | $185.86 | $186.18 | $1,489.40 | $2.53 | $173.64 |
| VEEV | 3 | $250.82 | $250.24 | $750.72 | $-1.75 | $225.63 |
| VLO | 3 | $304.72 | $349.52 | $1,048.56 | $134.40 | $315.01 |
| WST | 3 | $336.32 | $353.56 | $1,060.68 | $51.72 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
