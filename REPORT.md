# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-09 18:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,517.44** |
| Total return since inception | 2.59% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,839.73 (4.20%) |
| Positions value | $18,783.81 |
| Settled cash | $1,736.45 |
| Unsettled cash (T+1) | $12.04 |
| Tax reserve | $14.86 |

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
| AMD | 1 | $650.00 | $610.98 | $610.98 | $-39.02 | $581.31 |
| ANET | 4 | $191.78 | $216.79 | $867.18 | $100.06 | $194.20 |
| APA | 19 | $44.15 | $45.81 | $870.39 | $31.50 | $40.92 |
| CRL | 3 | $296.67 | $303.47 | $910.41 | $20.39 | $279.86 |
| FFIV | 2 | $448.44 | $480.38 | $960.76 | $63.87 | $423.09 |
| IQV | 2 | $255.46 | $261.85 | $523.70 | $12.79 | $247.54 |
| META | 1 | $723.49 | $718.96 | $718.96 | $-4.53 | $650.61 |
| MPC | 3 | $399.06 | $455.99 | $1,367.97 | $170.80 | $417.31 |
| NTAP | 5 | $206.27 | $237.02 | $1,185.10 | $153.75 | $212.25 |
| PSX | 5 | $215.50 | $279.95 | $1,399.75 | $322.27 | $253.40 |
| RVTY | 9 | $122.75 | $154.94 | $1,394.46 | $289.74 | $141.67 |
| SPY | 5 | $743.10 | $778.82 | $3,894.10 | $178.60 | — |
| TECH | 12 | $72.32 | $72.47 | $869.70 | $1.86 | $65.36 |
| VLO | 3 | $392.61 | $436.89 | $1,310.68 | $132.87 | $399.71 |
| WST | 2 | $370.69 | $370.20 | $740.40 | $-0.98 | $339.09 |
| ZBRA | 3 | $345.13 | $386.42 | $1,159.26 | $123.88 | $347.47 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-09T18:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-09T18:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-09T18:57` system **NTAP** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-08T23:52` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
