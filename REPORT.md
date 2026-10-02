# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-02 18:39 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,971.75** |
| Total return since inception | -0.14% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,565.20 (2.83%) |
| Positions value | $18,627.18 |
| Settled cash | $1,341.92 |
| Unsettled cash (T+1) | $17.12 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.95% | 2.65% |
| Annualized volatility | 10.99% | 11.34% |
| Sharpe (rf 4%) | -0.68 | 0.67 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 61 | 61 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $206.67 | $826.68 | $59.56 | $185.84 |
| APA | 19 | $44.15 | $43.33 | $823.27 | $-15.62 | $39.73 |
| BBY | 8 | $101.21 | $88.08 | $704.60 | $-105.08 | $85.36 |
| CRL | 3 | $296.67 | $289.04 | $867.12 | $-22.90 | $266.50 |
| FFIV | 2 | $448.44 | $456.06 | $912.11 | $15.22 | $403.38 |
| IQV | 2 | $255.46 | $258.45 | $516.90 | $5.99 | $247.54 |
| MPC | 3 | $399.06 | $422.97 | $1,268.91 | $71.74 | $377.95 |
| NTAP | 5 | $206.27 | $226.50 | $1,132.47 | $101.12 | $193.64 |
| PSX | 5 | $215.50 | $265.83 | $1,329.15 | $251.67 | $246.58 |
| RVTY | 9 | $122.75 | $151.13 | $1,360.17 | $255.45 | $137.66 |
| SPY | 5 | $743.10 | $768.95 | $3,844.73 | $129.23 | — |
| TECH | 12 | $72.32 | $72.42 | $868.98 | $1.14 | $65.36 |
| TGT | 7 | $162.82 | $155.00 | $1,085.00 | $-54.71 | $147.91 |
| VLO | 3 | $392.61 | $407.50 | $1,222.50 | $44.68 | $367.41 |
| WST | 2 | $370.69 | $365.85 | $731.70 | $-9.68 | $338.99 |
| ZBRA | 3 | $345.13 | $377.63 | $1,132.89 | $97.51 | $338.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-02T18:39` no_trade — no signals crossed action thresholds this hour
- `2026-10-02T18:39` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-01T23:22` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
