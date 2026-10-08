# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-08 23:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,385.06** |
| Total return since inception | 1.93% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,839.73 (4.20%) |
| Positions value | $18,653.65 |
| Settled cash | $1,736.45 |
| Unsettled cash (T+1) | $9.44 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.86% | 4.02% |
| Annualized volatility | 10.98% | 11.13% |
| Sharpe (rf 4%) | 0.34 | 1.07 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 66 | 66 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $620.83 | $620.83 | $-29.17 | $581.31 |
| ANET | 4 | $191.78 | $210.96 | $843.82 | $76.70 | $194.20 |
| APA | 19 | $44.15 | $45.47 | $863.93 | $25.04 | $40.92 |
| CRL | 3 | $296.67 | $298.09 | $894.27 | $4.25 | $279.86 |
| FFIV | 2 | $448.44 | $461.56 | $923.12 | $26.23 | $423.09 |
| IQV | 2 | $255.46 | $259.10 | $518.19 | $7.28 | $247.54 |
| META | 1 | $723.49 | $720.98 | $720.98 | $-2.51 | $650.61 |
| MPC | 3 | $399.06 | $463.68 | $1,391.04 | $193.87 | $417.31 |
| NTAP | 5 | $206.27 | $230.89 | $1,154.45 | $123.10 | $212.25 |
| PSX | 5 | $215.50 | $281.55 | $1,407.75 | $330.27 | $253.40 |
| RVTY | 9 | $122.75 | $152.09 | $1,368.81 | $264.09 | $141.67 |
| SPY | 5 | $743.10 | $774.30 | $3,871.50 | $156.00 | — |
| TECH | 12 | $72.32 | $72.46 | $869.52 | $1.68 | $65.36 |
| VLO | 3 | $392.61 | $444.12 | $1,332.36 | $154.54 | $399.71 |
| WST | 2 | $370.69 | $363.17 | $726.34 | $-15.04 | $339.09 |
| ZBRA | 3 | $345.13 | $382.25 | $1,146.74 | $111.36 | $347.47 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-08T19:23` no_trade — no signals crossed action thresholds this hour
- `2026-10-08T19:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-07T23:43` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
