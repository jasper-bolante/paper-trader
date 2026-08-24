# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 19:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,679.71** |
| Total return since inception | -1.60% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,164.24 |
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
| BAX | 28 | $27.27 | $26.34 | $737.66 | $-25.95 | $25.00 |
| BBY | 14 | $88.05 | $87.65 | $1,227.10 | $-5.65 | $80.33 |
| CRL | 2 | $285.12 | $295.17 | $590.34 | $20.10 | $265.83 |
| CSX | 17 | $50.29 | $51.62 | $877.46 | $22.50 | $46.44 |
| EXPE | 2 | $331.47 | $336.56 | $673.11 | $10.17 | $298.17 |
| FDS | 2 | $299.76 | $303.35 | $606.70 | $7.17 | $269.64 |
| IQV | 2 | $255.46 | $259.65 | $519.31 | $8.40 | $234.04 |
| MPC | 3 | $306.56 | $361.26 | $1,083.80 | $164.12 | $330.10 |
| NTAP | 4 | $187.95 | $187.76 | $751.04 | $-0.75 | $169.07 |
| PANW | 2 | $388.17 | $350.49 | $700.98 | $-75.36 | $322.11 |
| PSX | 5 | $215.50 | $241.58 | $1,207.90 | $130.42 | $219.13 |
| SPY | 5 | $743.10 | $763.92 | $3,819.60 | $104.10 | — |
| STT | 8 | $185.86 | $191.21 | $1,529.64 | $42.77 | $173.64 |
| VEEV | 3 | $250.82 | $248.70 | $746.10 | $-6.37 | $225.63 |
| VLO | 3 | $304.72 | $347.88 | $1,043.64 | $129.48 | $315.01 |
| WST | 3 | $336.32 | $349.95 | $1,049.87 | $40.90 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T19:10` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:10` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
