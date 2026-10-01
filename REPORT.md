# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-01 23:22 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,822.60** |
| Total return since inception | -0.89% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,565.20 (2.83%) |
| Positions value | $18,478.03 |
| Settled cash | $1,333.42 |
| Unsettled cash (T+1) | $25.62 |
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
| ANET | 4 | $191.78 | $204.44 | $817.76 | $50.64 | $185.84 |
| APA | 19 | $44.15 | $43.34 | $823.46 | $-15.43 | $39.73 |
| BBY | 8 | $101.21 | $87.65 | $701.20 | $-108.48 | $85.36 |
| CRL | 3 | $296.67 | $286.77 | $860.31 | $-29.71 | $266.50 |
| FFIV | 2 | $448.44 | $443.48 | $886.96 | $-9.93 | $403.38 |
| IQV | 2 | $255.46 | $260.83 | $521.66 | $10.75 | $247.54 |
| MPC | 3 | $399.06 | $419.94 | $1,259.82 | $62.65 | $377.95 |
| NTAP | 5 | $206.27 | $215.15 | $1,075.75 | $44.40 | $193.64 |
| PSX | 5 | $215.50 | $263.94 | $1,319.70 | $242.22 | $246.58 |
| RVTY | 9 | $122.75 | $149.19 | $1,342.71 | $237.99 | $137.66 |
| SPY | 5 | $743.10 | $764.10 | $3,820.50 | $105.00 | — |
| TECH | 12 | $72.32 | $72.42 | $869.04 | $1.20 | $65.36 |
| TGT | 7 | $162.82 | $156.75 | $1,097.28 | $-42.43 | $147.91 |
| VLO | 3 | $392.61 | $408.23 | $1,224.69 | $46.87 | $367.41 |
| WST | 2 | $370.69 | $365.18 | $730.36 | $-11.02 | $338.99 |
| ZBRA | 3 | $345.13 | $375.61 | $1,126.83 | $91.45 | $338.27 |

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
