# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 19:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,601.71** |
| Total return since inception | -1.99% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,086.24 |
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
| BAX | 28 | $27.27 | $26.32 | $737.10 | $-26.51 | $25.00 |
| BBY | 14 | $88.05 | $85.62 | $1,198.75 | $-34.00 | $80.33 |
| CRL | 2 | $285.12 | $299.61 | $599.22 | $28.98 | $268.70 |
| CSX | 17 | $50.29 | $51.56 | $876.61 | $21.65 | $46.44 |
| EXPE | 2 | $331.47 | $336.98 | $673.96 | $11.02 | $305.24 |
| FDS | 2 | $299.76 | $300.58 | $601.16 | $1.63 | $274.51 |
| IQV | 2 | $255.46 | $259.00 | $518.00 | $7.09 | $234.27 |
| MPC | 3 | $306.56 | $357.38 | $1,072.12 | $152.45 | $330.10 |
| NTAP | 4 | $187.95 | $187.23 | $748.92 | $-2.87 | $169.07 |
| PANW | 2 | $388.17 | $338.83 | $677.66 | $-98.68 | $322.11 |
| PSX | 5 | $215.50 | $239.14 | $1,195.70 | $118.22 | $219.13 |
| SPY | 5 | $743.10 | $765.37 | $3,826.85 | $111.35 | — |
| STT | 8 | $185.86 | $192.88 | $1,543.04 | $56.17 | $173.64 |
| VEEV | 3 | $250.82 | $245.86 | $737.58 | $-14.89 | $225.63 |
| VLO | 3 | $304.72 | $342.55 | $1,027.65 | $113.49 | $315.01 |
| WST | 3 | $336.32 | $350.64 | $1,051.92 | $42.96 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-24T19:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:56` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
