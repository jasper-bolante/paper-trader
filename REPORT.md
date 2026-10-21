# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-21 21:55 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,592.76** |
| Total return since inception | 2.96% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,810.66 (4.05%) |
| Positions value | $18,639.19 |
| Settled cash | $1,130.16 |
| Unsettled cash (T+1) | $838.27 |
| Tax reserve | $14.86 |

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
| APA | 19 | $44.15 | $49.64 | $943.16 | $104.27 | $44.90 |
| CRL | 3 | $296.67 | $344.83 | $1,034.49 | $144.47 | $310.35 |
| EL | 10 | $105.95 | $103.70 | $1,037.00 | $-22.48 | $95.47 |
| FFIV | 2 | $448.44 | $458.32 | $916.64 | $19.75 | $431.75 |
| IQV | 2 | $255.46 | $276.37 | $552.74 | $41.83 | $248.73 |
| MPC | 3 | $399.06 | $469.06 | $1,407.18 | $210.01 | $436.32 |
| NTAP | 4 | $214.92 | $217.30 | $869.20 | $9.53 | $195.57 |
| PLTR | 5 | $194.57 | $201.71 | $1,008.53 | $35.67 | $181.53 |
| PSX | 5 | $215.50 | $290.22 | $1,451.10 | $373.62 | $267.61 |
| RVTY | 9 | $122.75 | $156.71 | $1,410.35 | $305.62 | $141.67 |
| SPY | 5 | $743.10 | $773.22 | $3,866.10 | $150.60 | — |
| TECH | 12 | $72.32 | $72.64 | $871.68 | $3.84 | $65.38 |
| VLO | 3 | $392.61 | $436.65 | $1,309.96 | $132.14 | $413.91 |
| WST | 2 | $370.69 | $393.72 | $787.44 | $46.06 | $354.35 |
| ZBRA | 3 | $345.13 | $391.21 | $1,173.63 | $138.25 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,184.63 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-20T18:05` no_trade skip_entry **CRM** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
