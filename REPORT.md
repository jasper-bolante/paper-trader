# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 19:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,700.03** |
| Total return since inception | -1.50% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,184.56 |
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
| BAX | 28 | $27.27 | $26.57 | $744.10 | $-19.51 | $25.00 |
| BBY | 14 | $88.05 | $87.41 | $1,223.67 | $-9.08 | $80.33 |
| CRL | 2 | $285.12 | $298.34 | $596.68 | $26.44 | $265.83 |
| CSX | 17 | $50.29 | $51.42 | $874.22 | $19.27 | $46.44 |
| EXPE | 2 | $331.47 | $338.77 | $677.54 | $14.60 | $298.17 |
| FDS | 2 | $299.76 | $305.87 | $611.74 | $12.21 | $269.64 |
| IQV | 2 | $255.46 | $260.06 | $520.12 | $9.21 | $234.04 |
| MPC | 3 | $306.56 | $361.96 | $1,085.89 | $166.22 | $330.10 |
| NTAP | 4 | $187.95 | $187.16 | $748.62 | $-3.17 | $169.07 |
| PANW | 2 | $388.17 | $350.19 | $700.38 | $-75.96 | $322.11 |
| PSX | 5 | $215.50 | $241.80 | $1,209.00 | $131.52 | $219.13 |
| SPY | 5 | $743.10 | $763.77 | $3,818.85 | $103.35 | — |
| STT | 8 | $185.86 | $191.07 | $1,528.56 | $41.69 | $173.64 |
| VEEV | 3 | $250.82 | $247.82 | $743.47 | $-9.00 | $225.63 |
| VLO | 3 | $304.72 | $346.91 | $1,040.73 | $126.57 | $315.01 |
| WST | 3 | $336.32 | $353.66 | $1,060.98 | $52.02 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T19:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:56` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
