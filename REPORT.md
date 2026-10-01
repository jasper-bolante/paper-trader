# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-01 18:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,849.45** |
| Total return since inception | -0.75% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,552.01 (2.76%) |
| Positions value | $18,504.88 |
| Settled cash | $1,333.42 |
| Unsettled cash (T+1) | $25.62 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.72% | 2.58% |
| Annualized volatility | 10.96% | 11.43% |
| Sharpe (rf 4%) | -0.99 | 0.66 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 60 | 60 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $205.88 | $823.50 | $56.38 | $185.84 |
| APA | 19 | $44.15 | $43.30 | $822.61 | $-16.28 | $39.73 |
| BBY | 8 | $101.21 | $87.96 | $703.68 | $-106.00 | $85.36 |
| CRL | 3 | $296.67 | $288.17 | $864.51 | $-25.51 | $266.50 |
| FFIV | 2 | $448.44 | $448.29 | $896.58 | $-0.31 | $403.38 |
| IQV | 2 | $255.46 | $261.91 | $523.82 | $12.91 | $247.54 |
| MPC | 3 | $399.06 | $417.86 | $1,253.58 | $56.41 | $358.97 |
| NTAP | 5 | $206.27 | $214.22 | $1,071.12 | $39.78 | $189.08 |
| PSX | 5 | $215.50 | $263.54 | $1,317.70 | $240.22 | $246.58 |
| RVTY | 9 | $122.75 | $151.17 | $1,360.53 | $255.81 | $137.66 |
| SPY | 5 | $743.10 | $764.78 | $3,823.90 | $108.40 | — |
| TECH | 12 | $72.32 | $72.44 | $869.28 | $1.44 | $65.36 |
| TGT | 7 | $162.82 | $156.73 | $1,097.11 | $-42.60 | $147.91 |
| VLO | 3 | $392.61 | $405.97 | $1,217.91 | $40.09 | $352.71 |
| WST | 2 | $370.69 | $366.73 | $733.45 | $-7.93 | $338.99 |
| ZBRA | 3 | $345.13 | $375.20 | $1,125.60 | $90.22 | $338.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-01T18:59` no_trade — no signals crossed action thresholds this hour
- `2026-10-01T18:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-30T22:32` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
