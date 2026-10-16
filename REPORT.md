# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-16 17:39 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,166.64** |
| Total return since inception | 0.83% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,769.21 (3.85%) |
| Positions value | $17,710.05 |
| Settled cash | $1,450.37 |
| Unsettled cash (T+1) | $1,021.08 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.69% | 3.66% |
| Annualized volatility | 11.00% | 11.04% |
| Sharpe (rf 4%) | 0.24 | 0.87 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 71 | 71 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $48.88 | $928.72 | $89.83 | $43.21 |
| CRL | 3 | $296.67 | $299.52 | $898.57 | $8.55 | $279.86 |
| DDOG | 3 | $264.28 | $244.61 | $733.83 | $-59.02 | $220.15 |
| FFIV | 2 | $448.44 | $442.13 | $884.26 | $-12.63 | $431.75 |
| IQV | 2 | $255.46 | $264.89 | $529.79 | $18.88 | $247.54 |
| META | 1 | $723.49 | $711.39 | $711.39 | $-12.10 | $686.26 |
| MPC | 3 | $399.06 | $478.80 | $1,436.38 | $239.21 | $436.32 |
| NTAP | 4 | $214.92 | $205.94 | $823.76 | $-35.91 | $193.37 |
| PSX | 5 | $215.50 | $293.71 | $1,468.55 | $391.07 | $267.61 |
| RVTY | 9 | $122.75 | $153.17 | $1,378.53 | $273.81 | $141.67 |
| SPY | 5 | $743.10 | $764.60 | $3,823.00 | $107.50 | — |
| TECH | 12 | $72.32 | $72.50 | $870.06 | $2.22 | $65.36 |
| VLO | 3 | $392.61 | $447.19 | $1,341.56 | $163.74 | $413.91 |
| WST | 2 | $370.69 | $380.96 | $761.92 | $20.54 | $344.82 |
| ZBRA | 3 | $345.13 | $373.24 | $1,119.72 | $84.34 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,197.61 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-16T17:39` entry buy **DDOG** — momentum entry: rank 3, mom 0.788, vol 44%
- `2026-10-16T17:39` no_trade skip_entry **CRM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **MSFT** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **NOW** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **HUM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **WDAY** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **PLTR** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **VEEV** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **FTNT** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` exit sell **FTNT** — trailing stop 10%
- `2026-10-16T17:39` exit sell **DDOG** — trailing stop 10%
- `2026-10-15T21:40` system — eod_complete
- `2026-10-15T17:51` entry buy **NTAP** — momentum entry: rank 1, mom 0.872, vol 46%
- `2026-10-15T17:51` exit sell **NTAP** — trailing stop 10%
- `2026-10-14T21:53` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
