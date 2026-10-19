# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-19 23:01 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,180.22** |
| Total return since inception | 0.90% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,635.98 (3.18%) |
| Positions value | $17,993.40 |
| Settled cash | $1,486.55 |
| Unsettled cash (T+1) | $715.13 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.83% | 3.00% |
| Annualized volatility | 11.02% | 11.12% |
| Sharpe (rf 4%) | -0.05 | 0.63 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 73 | 73 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.76 | $945.44 | $106.55 | $44.78 |
| CRL | 3 | $296.67 | $299.98 | $899.94 | $9.92 | $279.86 |
| DDOG | 3 | $264.28 | $260.27 | $780.81 | $-12.04 | $234.24 |
| FFIV | 2 | $448.44 | $450.88 | $901.76 | $4.87 | $431.75 |
| IQV | 2 | $255.46 | $265.78 | $531.56 | $20.65 | $247.54 |
| MPC | 3 | $399.06 | $474.40 | $1,423.20 | $226.03 | $436.32 |
| NTAP | 4 | $214.92 | $207.49 | $829.94 | $-29.73 | $193.37 |
| PLTR | 5 | $194.57 | $194.16 | $970.77 | $-2.09 | $175.08 |
| PSX | 5 | $215.50 | $290.60 | $1,453.00 | $375.52 | $267.61 |
| RVTY | 9 | $122.75 | $150.83 | $1,357.47 | $252.75 | $141.67 |
| SPY | 5 | $743.10 | $766.73 | $3,833.65 | $118.15 | — |
| TECH | 12 | $72.32 | $72.47 | $869.64 | $1.80 | $65.36 |
| VLO | 3 | $392.61 | $433.23 | $1,299.68 | $121.86 | $413.91 |
| WST | 2 | $370.69 | $384.06 | $768.12 | $26.74 | $345.65 |
| ZBRA | 3 | $345.13 | $376.14 | $1,128.42 | $93.04 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,218.01 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-19T23:01` system — corporate_actions_synced
- `2026-10-19T19:26` entry buy **PLTR** — momentum entry: rank 7, mom 0.620, vol 39%
- `2026-10-19T19:26` no_trade skip_entry **TMO** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CNC** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CRM** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **A** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **MSFT** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **NOW** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **HUM** — insufficient investable cash (size $867, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-19T19:26` exit sell **META** — momentum rank decayed (None > 150 or ineligible: volatility 0.5053586052163451 above cap 0.5)
- `2026-10-16T21:36` system — eod_complete
- `2026-10-16T17:39` entry buy **DDOG** — momentum entry: rank 3, mom 0.788, vol 44%
- `2026-10-16T17:39` no_trade skip_entry **CRM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **MSFT** — insufficient investable cash (size $384, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
