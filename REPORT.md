# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 14:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,633.37** |
| Total return since inception | -1.83% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,297.58 |
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
| BAX | 28 | $27.27 | $26.31 | $736.68 | $-26.93 | $25.00 |
| BBY | 14 | $88.05 | $87.33 | $1,222.62 | $-10.13 | $80.33 |
| CRL | 2 | $285.12 | $291.18 | $582.36 | $12.12 | $262.31 |
| CSX | 17 | $50.29 | $51.53 | $876.01 | $21.06 | $46.01 |
| EXPE | 2 | $331.47 | $323.77 | $647.54 | $-15.40 | $298.17 |
| FDS | 2 | $299.76 | $299.60 | $599.20 | $-0.33 | $269.64 |
| IQV | 2 | $255.46 | $257.13 | $514.27 | $3.36 | $230.53 |
| MPC | 3 | $306.56 | $361.02 | $1,083.06 | $163.38 | $330.10 |
| NTAP | 5 | $161.48 | $193.97 | $969.88 | $162.50 | $186.39 |
| PANW | 2 | $388.17 | $348.77 | $697.54 | $-78.80 | $313.89 |
| PSX | 5 | $215.50 | $241.75 | $1,208.72 | $131.24 | $219.13 |
| SPY | 5 | $743.10 | $765.23 | $3,826.15 | $110.65 | — |
| STT | 8 | $185.86 | $186.94 | $1,495.56 | $8.69 | $173.64 |
| VEEV | 3 | $250.82 | $248.96 | $746.88 | $-5.59 | $225.63 |
| VLO | 3 | $304.72 | $344.71 | $1,034.13 | $119.97 | $315.01 |
| WST | 3 | $336.32 | $352.32 | $1,056.97 | $48.01 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
