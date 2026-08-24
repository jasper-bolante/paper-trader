# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 18:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,631.00** |
| Total return since inception | -1.84% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,115.53 |
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
| BAX | 28 | $27.27 | $26.12 | $731.36 | $-32.25 | $25.00 |
| BBY | 14 | $88.05 | $87.70 | $1,227.80 | $-4.95 | $80.33 |
| CRL | 2 | $285.12 | $293.14 | $586.28 | $16.04 | $265.83 |
| CSX | 17 | $50.29 | $51.52 | $875.92 | $20.97 | $46.44 |
| EXPE | 2 | $331.47 | $333.61 | $667.22 | $4.28 | $298.17 |
| FDS | 2 | $299.76 | $304.13 | $608.26 | $8.73 | $269.64 |
| IQV | 2 | $255.46 | $258.86 | $517.72 | $6.81 | $234.04 |
| MPC | 3 | $306.56 | $359.51 | $1,078.55 | $158.87 | $330.10 |
| NTAP | 4 | $187.95 | $187.69 | $750.78 | $-1.01 | $169.07 |
| PANW | 2 | $388.17 | $350.44 | $700.88 | $-75.46 | $322.11 |
| PSX | 5 | $215.50 | $240.58 | $1,202.90 | $125.42 | $219.13 |
| SPY | 5 | $743.10 | $763.38 | $3,816.90 | $101.40 | — |
| STT | 8 | $185.86 | $190.32 | $1,522.56 | $35.69 | $173.64 |
| VEEV | 3 | $250.82 | $246.69 | $740.06 | $-12.41 | $225.63 |
| VLO | 3 | $304.72 | $346.23 | $1,038.68 | $124.52 | $315.01 |
| WST | 3 | $336.32 | $349.89 | $1,049.67 | $40.71 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T18:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T18:00` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
