# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-22 18:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,335.16** |
| Total return since inception | 1.68% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,810.66 (4.05%) |
| Positions value | $19,239.01 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $16.79 |
| Tax reserve | $15.57 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.89% | 3.87% |
| Annualized volatility | 11.19% | 11.01% |
| Sharpe (rf 4%) | 0.57 | 0.87 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 75 | 75 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.37 | $938.03 | $99.14 | $44.90 |
| CRL | 3 | $296.67 | $344.57 | $1,033.71 | $143.69 | $310.35 |
| EL | 10 | $105.95 | $106.37 | $1,063.70 | $4.22 | $95.47 |
| FFIV | 2 | $448.44 | $447.11 | $894.22 | $-2.67 | $431.75 |
| FTNT | 5 | $183.53 | $172.20 | $861.00 | $-56.66 | $154.98 |
| IQV | 2 | $255.46 | $274.62 | $549.23 | $38.32 | $248.73 |
| MPC | 3 | $399.06 | $459.43 | $1,378.29 | $181.12 | $436.32 |
| NTAP | 4 | $214.92 | $211.51 | $846.06 | $-13.61 | $195.57 |
| PLTR | 5 | $194.57 | $196.69 | $983.47 | $10.61 | $181.53 |
| PSX | 5 | $215.50 | $281.93 | $1,409.65 | $332.17 | $267.61 |
| RVTY | 9 | $122.75 | $156.43 | $1,407.83 | $303.11 | $141.67 |
| SPY | 5 | $743.10 | $762.27 | $3,811.35 | $95.85 | — |
| TECH | 12 | $72.32 | $72.64 | $871.62 | $3.78 | $65.38 |
| VLO | 3 | $392.61 | $423.15 | $1,269.45 | $91.63 | $413.91 |
| WST | 2 | $370.69 | $392.55 | $785.09 | $43.71 | $354.35 |
| ZBRA | 3 | $345.13 | $378.77 | $1,136.31 | $100.93 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,128.42 | $0.00 | $1,257.19 |

Dividends received: $103.80. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-22T18:08` entry buy **FTNT** — momentum entry: rank 4, mom 0.728, vol 43%
- `2026-10-22T18:07` system **APA** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-21T21:55` system — eod_complete
- `2026-10-21T18:12` no_trade skip_entry **IT** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CRM** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CNC** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **WDAY** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **NOW** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **HUM** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **VEEV** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **FTNT** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` exit sell **DDOG** — momentum rank decayed (None > 150 or ineligible: volatility 0.5136731923759654 above cap 0.5)
- `2026-10-20T21:48` system — eod_complete
- `2026-10-20T21:48` system — corporate_actions_synced
- `2026-10-20T18:05` entry buy **EL** — momentum entry: rank 20, mom 0.290, vol 36%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
