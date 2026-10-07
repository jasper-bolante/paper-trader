# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-07 19:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,319.69** |
| Total return since inception | 1.60% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,973.22 (4.87%) |
| Positions value | $18,588.27 |
| Settled cash | $1,728.77 |
| Unsettled cash (T+1) | $17.12 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.30% | 4.68% |
| Annualized volatility | 11.13% | 11.25% |
| Sharpe (rf 4%) | 0.16 | 1.33 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 64 | 64 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $642.90 | $642.90 | $-7.10 | $578.61 |
| ANET | 4 | $191.78 | $215.94 | $863.78 | $96.66 | $193.89 |
| APA | 19 | $44.15 | $43.84 | $833.05 | $-5.84 | $39.73 |
| CRL | 3 | $296.67 | $301.87 | $905.61 | $15.59 | $279.86 |
| FFIV | 2 | $448.44 | $468.72 | $937.44 | $40.55 | $423.09 |
| IQV | 2 | $255.46 | $258.26 | $516.52 | $5.61 | $247.54 |
| META | 1 | $723.49 | $722.90 | $722.90 | $-0.59 | $650.61 |
| MPC | 3 | $399.06 | $440.80 | $1,322.40 | $125.23 | $390.17 |
| NTAP | 5 | $206.27 | $236.59 | $1,182.95 | $151.60 | $205.60 |
| PSX | 5 | $215.50 | $271.32 | $1,356.60 | $279.12 | $246.58 |
| RVTY | 9 | $122.75 | $153.77 | $1,383.93 | $279.21 | $141.67 |
| SPY | 5 | $743.10 | $777.15 | $3,885.77 | $170.27 | — |
| TECH | 12 | $72.32 | $72.52 | $870.18 | $2.34 | $65.36 |
| VLO | 3 | $392.61 | $422.36 | $1,267.08 | $89.26 | $377.45 |
| WST | 2 | $370.69 | $368.69 | $737.38 | $-4.00 | $339.09 |
| ZBRA | 3 | $345.13 | $386.59 | $1,159.77 | $124.39 | $346.80 |

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
