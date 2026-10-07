# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-07 23:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,309.76** |
| Total return since inception | 1.55% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,920.47 (4.60%) |
| Positions value | $18,578.34 |
| Settled cash | $1,728.77 |
| Unsettled cash (T+1) | $17.12 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.48% | 4.42% |
| Annualized volatility | 11.05% | 11.18% |
| Sharpe (rf 4%) | 0.22 | 1.22 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 65 | 65 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $645.90 | $645.90 | $-4.10 | $581.31 |
| ANET | 4 | $191.78 | $215.78 | $863.12 | $96.00 | $194.20 |
| APA | 19 | $44.15 | $43.81 | $832.48 | $-6.41 | $39.73 |
| CRL | 3 | $296.67 | $300.19 | $900.57 | $10.55 | $279.86 |
| FFIV | 2 | $448.44 | $466.48 | $932.96 | $36.07 | $423.09 |
| IQV | 2 | $255.46 | $258.25 | $516.50 | $5.59 | $247.54 |
| META | 1 | $723.49 | $721.08 | $721.08 | $-2.41 | $650.61 |
| MPC | 3 | $399.06 | $442.36 | $1,327.07 | $129.89 | $398.12 |
| NTAP | 5 | $206.27 | $235.84 | $1,179.17 | $147.83 | $212.25 |
| PSX | 5 | $215.50 | $271.57 | $1,357.85 | $280.37 | $246.58 |
| RVTY | 9 | $122.75 | $153.49 | $1,381.41 | $276.69 | $141.67 |
| SPY | 5 | $743.10 | $777.30 | $3,886.50 | $171.00 | — |
| TECH | 12 | $72.32 | $72.53 | $870.30 | $2.46 | $65.36 |
| VLO | 3 | $392.61 | $424.12 | $1,272.36 | $94.54 | $381.71 |
| WST | 2 | $370.69 | $366.41 | $732.82 | $-8.56 | $339.09 |
| ZBRA | 3 | $345.13 | $386.08 | $1,158.24 | $122.86 | $347.47 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-07T19:28` entry buy **META** — momentum entry: rank 20, mom 0.344, vol 47%
- `2026-10-07T19:28` entry buy **AMD** — momentum entry: rank 2, mom 1.073, vol 49%
- `2026-10-07T19:28` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **A** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **PLTR** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **HPQ** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **DDOG** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **FTNT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **MU** — insufficient investable cash (size $929, need >= $500)
- `2026-10-06T23:11` system — eod_complete
- `2026-10-06T19:00` no_trade skip_entry **WAT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **TMO** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **MSFT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **A** — insufficient investable cash (size $311, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
