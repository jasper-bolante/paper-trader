# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-30 18:31 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,835.69** |
| Total return since inception | -0.82% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,572.74 (2.86%) |
| Positions value | $18,491.12 |
| Settled cash | $1,333.14 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 2.68% |
| Annualized volatility | 11.05% | 11.53% |
| Sharpe (rf 4%) | -1.01 | 0.71 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 59 | 59 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $204.30 | $817.20 | $50.08 | $185.84 |
| APA | 19 | $44.15 | $42.25 | $802.75 | $-36.14 | $39.73 |
| BBY | 8 | $101.21 | $88.58 | $708.64 | $-101.04 | $85.36 |
| CRL | 3 | $296.67 | $297.35 | $892.05 | $2.03 | $266.50 |
| FFIV | 2 | $448.44 | $447.50 | $895.00 | $-1.89 | $403.38 |
| IQV | 2 | $255.46 | $270.72 | $541.44 | $30.53 | $247.54 |
| MPC | 3 | $399.06 | $403.41 | $1,210.23 | $13.06 | $358.97 |
| NTAP | 5 | $206.27 | $210.97 | $1,054.88 | $23.53 | $188.31 |
| PSX | 5 | $215.50 | $260.16 | $1,300.80 | $223.32 | $246.58 |
| RVTY | 9 | $122.75 | $155.99 | $1,403.91 | $299.19 | $137.49 |
| SPY | 5 | $743.10 | $766.45 | $3,832.25 | $116.75 | — |
| TECH | 12 | $72.32 | $72.49 | $869.88 | $2.04 | $65.36 |
| TGT | 7 | $162.82 | $156.50 | $1,095.50 | $-44.21 | $147.91 |
| VLO | 3 | $392.61 | $397.22 | $1,191.66 | $13.84 | $352.71 |
| WST | 2 | $370.69 | $373.38 | $746.76 | $5.38 | $338.99 |
| ZBRA | 3 | $345.13 | $376.06 | $1,128.18 | $92.80 | $338.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-30T18:31` no_trade — no signals crossed action thresholds this hour
- `2026-09-30T18:31` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-29T23:08` system — eod_complete
- `2026-09-29T23:08` system — corporate_actions_synced
- `2026-09-29T18:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-29T18:49` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-28T20:12` system — eod_complete
- `2026-09-25T21:46` system — eod_complete
- `2026-09-25T18:03` entry buy **WST** — momentum entry: rank 15, mom 0.333, vol 21%
- `2026-09-25T18:03` entry buy **FFIV** — momentum entry: rank 14, mom 0.335, vol 38%
- `2026-09-25T18:03` no_trade skip_entry **INCY** — sector cap: Health Care would exceed 25% of equity
- `2026-09-25T18:03` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-09-24T21:43` system — eod_complete
- `2026-09-24T17:55` entry buy **VLO** — momentum entry: rank 2, mom 0.681, vol 32%
- `2026-09-24T17:55` entry buy **MPC** — momentum entry: rank 1, mom 0.714, vol 30%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
