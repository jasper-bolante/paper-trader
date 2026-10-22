# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-22 21:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,412.53** |
| Total return since inception | 2.06% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,563.05 (2.82%) |
| Positions value | $19,316.38 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $16.79 |
| Tax reserve | $15.57 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.99% | 2.63% |
| Annualized volatility | 11.24% | 11.17% |
| Sharpe (rf 4%) | 0.29 | 0.48 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 76 | 76 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.45 | $939.55 | $100.66 | $44.90 |
| CRL | 3 | $296.67 | $339.91 | $1,019.73 | $129.71 | $310.35 |
| EL | 10 | $105.95 | $107.70 | $1,077.00 | $17.52 | $96.93 |
| FFIV | 2 | $448.44 | $449.89 | $899.78 | $2.89 | $431.75 |
| FTNT | 5 | $183.53 | $172.97 | $864.88 | $-52.78 | $155.68 |
| IQV | 2 | $255.46 | $278.23 | $556.46 | $45.55 | $250.41 |
| MPC | 3 | $399.06 | $459.39 | $1,378.17 | $181.00 | $436.32 |
| NTAP | 4 | $214.92 | $212.51 | $850.04 | $-9.63 | $195.57 |
| PLTR | 5 | $194.57 | $196.18 | $980.90 | $8.04 | $181.53 |
| PSX | 5 | $215.50 | $284.55 | $1,422.73 | $345.25 | $267.61 |
| RVTY | 9 | $122.75 | $157.38 | $1,416.38 | $311.65 | $141.67 |
| SPY | 5 | $743.10 | $764.02 | $3,820.10 | $104.60 | — |
| TECH | 12 | $72.32 | $72.64 | $871.68 | $3.84 | $65.38 |
| VLO | 3 | $392.61 | $426.31 | $1,278.93 | $101.11 | $413.91 |
| WST | 2 | $370.69 | $394.18 | $788.36 | $46.98 | $354.76 |
| ZBRA | 3 | $345.13 | $383.90 | $1,151.70 | $116.32 | $352.09 |

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
