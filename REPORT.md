# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 20:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,562.22** |
| Total return since inception | -2.19% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,612.30 (3.06%) |
| Positions value | $17,046.74 |
| Settled cash | $2,510.89 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.26% | 2.88% |
| Annualized volatility | 12.03% | 12.65% |
| Sharpe (rf 4%) | -1.68 | 1.41 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 35 | 35 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.29 | $736.12 | $-27.49 | $25.00 |
| BBY | 14 | $88.05 | $85.34 | $1,194.76 | $-37.99 | $80.33 |
| CRL | 2 | $285.12 | $297.55 | $595.10 | $24.86 | $268.70 |
| CSX | 17 | $50.29 | $51.50 | $875.50 | $20.55 | $46.44 |
| EXPE | 2 | $331.47 | $338.14 | $676.28 | $13.34 | $305.24 |
| FDS | 2 | $299.76 | $295.93 | $591.85 | $-7.68 | $274.51 |
| IQV | 2 | $255.46 | $259.48 | $518.96 | $8.05 | $234.27 |
| MPC | 3 | $306.56 | $354.86 | $1,064.57 | $144.89 | $330.10 |
| NTAP | 4 | $187.95 | $187.45 | $749.80 | $-1.99 | $169.07 |
| PANW | 2 | $388.17 | $339.93 | $679.86 | $-96.48 | $322.11 |
| PSX | 5 | $215.50 | $236.68 | $1,183.40 | $105.92 | $219.13 |
| SPY | 5 | $743.10 | $765.85 | $3,829.25 | $113.75 | — |
| STT | 8 | $185.86 | $193.04 | $1,544.32 | $57.45 | $173.74 |
| VEEV | 3 | $250.82 | $246.74 | $740.22 | $-12.25 | $225.63 |
| VLO | 3 | $304.72 | $340.42 | $1,021.26 | $107.10 | $315.01 |
| WST | 3 | $336.32 | $348.50 | $1,045.50 | $36.54 | $318.49 |

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
