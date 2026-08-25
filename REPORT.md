# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 15:23 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,614.24** |
| Total return since inception | -1.93% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,098.77 |
| Settled cash | $2,510.89 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.58% | 2.58% |
| Annualized volatility | 12.09% | 12.84% |
| Sharpe (rf 4%) | -1.28 | 1.27 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 34 | 34 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.19 | $733.32 | $-30.29 | $25.00 |
| BBY | 14 | $88.05 | $85.72 | $1,200.08 | $-32.67 | $80.33 |
| CRL | 2 | $285.12 | $296.85 | $593.70 | $23.46 | $268.70 |
| CSX | 17 | $50.29 | $51.79 | $880.43 | $25.48 | $46.44 |
| EXPE | 2 | $331.47 | $335.25 | $670.50 | $7.56 | $305.24 |
| FDS | 2 | $299.76 | $301.04 | $602.08 | $2.55 | $274.51 |
| IQV | 2 | $255.46 | $259.36 | $518.72 | $7.81 | $234.27 |
| MPC | 3 | $306.56 | $359.29 | $1,077.87 | $158.19 | $330.10 |
| NTAP | 4 | $187.95 | $187.86 | $751.44 | $-0.35 | $169.07 |
| PANW | 2 | $388.17 | $345.34 | $690.68 | $-85.66 | $322.11 |
| PSX | 5 | $215.50 | $240.15 | $1,200.75 | $123.27 | $219.13 |
| SPY | 5 | $743.10 | $764.97 | $3,824.85 | $109.35 | — |
| STT | 8 | $185.86 | $191.85 | $1,534.80 | $47.93 | $173.64 |
| VEEV | 3 | $250.82 | $246.45 | $739.35 | $-13.12 | $225.63 |
| VLO | 3 | $304.72 | $343.12 | $1,029.36 | $115.20 | $315.01 |
| WST | 3 | $336.32 | $350.28 | $1,050.84 | $41.88 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-25T15:23` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T15:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T14:22` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T14:22` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T21:00` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
