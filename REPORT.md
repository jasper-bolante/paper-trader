# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-02 23:11 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,972.85** |
| Total return since inception | -0.14% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,716.46 (3.58%) |
| Positions value | $18,628.28 |
| Settled cash | $1,341.92 |
| Unsettled cash (T+1) | $17.12 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.20% | 3.40% |
| Annualized volatility | 11.01% | 11.33% |
| Sharpe (rf 4%) | -0.39 | 0.92 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 62 | 62 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $207.34 | $829.34 | $62.22 | $186.60 |
| APA | 19 | $44.15 | $43.67 | $829.73 | $-9.16 | $39.73 |
| BBY | 8 | $101.21 | $87.97 | $703.80 | $-105.88 | $85.36 |
| CRL | 3 | $296.67 | $290.15 | $870.45 | $-19.57 | $266.50 |
| FFIV | 2 | $448.44 | $454.00 | $908.01 | $11.12 | $408.60 |
| IQV | 2 | $255.46 | $258.31 | $516.63 | $5.72 | $247.54 |
| MPC | 3 | $399.06 | $422.36 | $1,267.08 | $69.91 | $380.12 |
| NTAP | 5 | $206.27 | $226.51 | $1,132.55 | $101.20 | $203.86 |
| PSX | 5 | $215.50 | $264.57 | $1,322.88 | $245.39 | $246.58 |
| RVTY | 9 | $122.75 | $151.43 | $1,362.87 | $258.15 | $137.66 |
| SPY | 5 | $743.10 | $769.72 | $3,848.60 | $133.10 | — |
| TECH | 12 | $72.32 | $72.41 | $868.92 | $1.08 | $65.36 |
| TGT | 7 | $162.82 | $155.95 | $1,091.65 | $-48.06 | $147.91 |
| VLO | 3 | $392.61 | $405.66 | $1,216.98 | $39.16 | $367.41 |
| WST | 2 | $370.69 | $365.52 | $731.04 | $-10.34 | $338.99 |
| ZBRA | 3 | $345.13 | $375.92 | $1,127.76 | $92.38 | $338.33 |

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
