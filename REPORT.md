# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-23 17:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,496.70** |
| Total return since inception | 2.48% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,563.05 (2.82%) |
| Positions value | $19,400.01 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $17.42 |
| Tax reserve | $15.66 |

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
| APA | 19 | $44.15 | $51.87 | $985.53 | $146.64 | $44.90 |
| CRL | 3 | $296.67 | $344.94 | $1,034.82 | $144.80 | $310.35 |
| EL | 10 | $105.95 | $107.94 | $1,079.35 | $19.87 | $96.93 |
| FFIV | 2 | $448.44 | $452.96 | $905.92 | $9.03 | $431.75 |
| FTNT | 5 | $183.53 | $177.76 | $888.80 | $-28.86 | $155.68 |
| IQV | 2 | $255.46 | $278.49 | $556.98 | $46.07 | $250.41 |
| MPC | 3 | $399.06 | $459.52 | $1,378.56 | $181.39 | $436.32 |
| NTAP | 4 | $214.92 | $215.54 | $862.16 | $2.49 | $195.57 |
| PLTR | 5 | $194.57 | $195.72 | $978.62 | $5.76 | $181.53 |
| PSX | 5 | $215.50 | $284.32 | $1,421.60 | $344.12 | $267.61 |
| RVTY | 9 | $122.75 | $158.21 | $1,423.89 | $319.17 | $141.67 |
| SPY | 5 | $743.10 | $760.68 | $3,803.40 | $87.90 | — |
| TECH | 12 | $72.32 | $72.58 | $870.90 | $3.06 | $65.38 |
| VLO | 3 | $392.61 | $423.45 | $1,270.37 | $92.55 | $413.91 |
| WST | 2 | $370.69 | $391.23 | $782.46 | $41.08 | $354.76 |
| ZBRA | 3 | $345.13 | $385.55 | $1,156.65 | $121.27 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,128.42 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-23T17:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-23T17:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T17:56` system **RVTY** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-22T21:52` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
