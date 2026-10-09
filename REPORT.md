# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-09 23:25 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,467.58** |
| Total return since inception | 2.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,955.46 (4.78%) |
| Positions value | $18,733.94 |
| Settled cash | $1,736.45 |
| Unsettled cash (T+1) | $12.04 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.27% | 4.59% |
| Annualized volatility | 10.92% | 11.09% |
| Sharpe (rf 4%) | 0.47 | 1.24 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 67 | 67 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $607.29 | $607.29 | $-42.71 | $581.31 |
| ANET | 4 | $191.78 | $216.73 | $866.92 | $99.80 | $195.06 |
| APA | 19 | $44.15 | $45.87 | $871.53 | $32.64 | $41.28 |
| CRL | 3 | $296.67 | $302.13 | $906.39 | $16.37 | $279.86 |
| FFIV | 2 | $448.44 | $479.72 | $959.44 | $62.55 | $431.75 |
| IQV | 2 | $255.46 | $259.81 | $519.63 | $8.72 | $247.54 |
| META | 1 | $723.49 | $718.12 | $718.12 | $-5.37 | $650.61 |
| MPC | 3 | $399.06 | $454.96 | $1,364.88 | $167.71 | $417.31 |
| NTAP | 5 | $206.27 | $237.22 | $1,186.10 | $154.75 | $213.50 |
| PSX | 5 | $215.50 | $278.15 | $1,390.77 | $313.29 | $253.40 |
| RVTY | 9 | $122.75 | $154.12 | $1,387.08 | $282.36 | $141.67 |
| SPY | 5 | $743.10 | $778.60 | $3,893.00 | $177.50 | — |
| TECH | 12 | $72.32 | $72.47 | $869.64 | $1.80 | $65.36 |
| VLO | 3 | $392.61 | $433.74 | $1,301.22 | $123.40 | $399.71 |
| WST | 2 | $370.69 | $365.63 | $731.26 | $-10.12 | $339.09 |
| ZBRA | 3 | $345.13 | $386.89 | $1,160.67 | $125.29 | $348.20 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-09T23:25` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
