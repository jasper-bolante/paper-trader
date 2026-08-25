# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 19:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,578.42** |
| Total return since inception | -2.11% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,062.94 |
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
| BAX | 28 | $27.27 | $26.25 | $735.14 | $-28.47 | $25.00 |
| BBY | 14 | $88.05 | $85.33 | $1,194.62 | $-38.13 | $80.33 |
| CRL | 2 | $285.12 | $298.30 | $596.60 | $26.36 | $268.70 |
| CSX | 17 | $50.29 | $51.60 | $877.20 | $22.25 | $46.44 |
| EXPE | 2 | $331.47 | $337.12 | $674.24 | $11.30 | $305.24 |
| FDS | 2 | $299.76 | $296.43 | $592.86 | $-6.67 | $274.51 |
| IQV | 2 | $255.46 | $260.00 | $520.00 | $9.09 | $234.27 |
| MPC | 3 | $306.56 | $356.14 | $1,068.42 | $148.74 | $330.10 |
| NTAP | 4 | $187.95 | $187.19 | $748.76 | $-3.03 | $169.07 |
| PANW | 2 | $388.17 | $339.73 | $679.46 | $-96.88 | $322.11 |
| PSX | 5 | $215.50 | $237.69 | $1,188.47 | $110.99 | $219.13 |
| SPY | 5 | $743.10 | $765.99 | $3,829.95 | $114.45 | — |
| STT | 8 | $185.86 | $193.00 | $1,544.00 | $57.13 | $173.64 |
| VEEV | 3 | $250.82 | $246.86 | $740.58 | $-11.89 | $225.63 |
| VLO | 3 | $304.72 | $341.37 | $1,024.11 | $109.95 | $315.01 |
| WST | 3 | $336.32 | $349.51 | $1,048.53 | $39.57 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-25T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T19:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T16:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T16:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T15:23` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T15:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T14:22` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T14:22` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T21:00` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
