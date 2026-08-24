# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 16:05 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,663.55** |
| Total return since inception | -1.68% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,148.08 |
| Settled cash | $1,579.42 |
| Unsettled cash (T+1) | $944.42 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.79% | 2.84% |
| Annualized volatility | 12.26% | 13.01% |
| Sharpe (rf 4%) | -1.43 | 1.45 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 33 | 33 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.22 | $734.16 | $-29.45 | $25.00 |
| BBY | 14 | $88.05 | $88.00 | $1,232.07 | $-0.68 | $80.33 |
| CRL | 2 | $285.12 | $296.88 | $593.76 | $23.52 | $265.83 |
| CSX | 17 | $50.29 | $51.53 | $876.09 | $21.14 | $46.44 |
| EXPE | 2 | $331.47 | $336.09 | $672.18 | $9.24 | $298.17 |
| FDS | 2 | $299.76 | $304.95 | $609.90 | $10.37 | $269.64 |
| IQV | 2 | $255.46 | $260.44 | $520.88 | $9.97 | $234.04 |
| MPC | 3 | $306.56 | $359.12 | $1,077.35 | $157.67 | $330.10 |
| NTAP | 4 | $187.95 | $187.86 | $751.44 | $-0.35 | $169.07 |
| PANW | 2 | $388.17 | $351.02 | $702.05 | $-74.29 | $322.11 |
| PSX | 5 | $215.50 | $240.84 | $1,204.20 | $126.72 | $219.13 |
| SPY | 5 | $743.10 | $764.95 | $3,824.75 | $109.25 | — |
| STT | 8 | $185.86 | $190.35 | $1,522.80 | $35.93 | $173.64 |
| VEEV | 3 | $250.82 | $248.32 | $744.96 | $-7.51 | $225.63 |
| VLO | 3 | $304.72 | $344.51 | $1,033.53 | $119.37 | $315.01 |
| WST | 3 | $336.32 | $349.32 | $1,047.96 | $39.00 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T16:05` entry buy **NTAP** — momentum entry: rank 2, mom 0.918, vol 44%
- `2026-08-24T16:05` exit sell **NTAP** — trailing stop 10%
- `2026-08-24T15:11` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T15:11` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T14:20` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T14:20` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-21T20:52` system — eod_complete
- `2026-08-21T20:52` system — corporate_actions_synced
- `2026-08-21T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T19:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:07` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:58` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:03` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
