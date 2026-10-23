# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-23 21:35 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,508.66** |
| Total return since inception | 2.54% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,457.54 (2.29%) |
| Positions value | $19,411.97 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $17.42 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.47% | 2.11% |
| Annualized volatility | 11.20% | 11.14% |
| Sharpe (rf 4%) | 0.42 | 0.32 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 77 | 77 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $51.90 | $986.01 | $147.12 | $46.71 |
| CRL | 3 | $296.67 | $345.09 | $1,035.27 | $145.25 | $310.58 |
| EL | 10 | $105.95 | $108.69 | $1,086.85 | $27.37 | $97.82 |
| FFIV | 2 | $448.44 | $455.26 | $910.52 | $13.63 | $431.75 |
| FTNT | 5 | $183.53 | $179.98 | $899.90 | $-17.76 | $161.98 |
| IQV | 2 | $255.46 | $279.35 | $558.70 | $47.79 | $251.42 |
| MPC | 3 | $399.06 | $457.27 | $1,371.81 | $174.64 | $436.32 |
| NTAP | 4 | $214.92 | $215.65 | $862.60 | $2.93 | $195.57 |
| PLTR | 5 | $194.57 | $196.74 | $983.70 | $10.84 | $181.53 |
| PSX | 5 | $215.50 | $283.10 | $1,415.50 | $338.02 | $267.61 |
| RVTY | 9 | $122.75 | $158.73 | $1,428.57 | $323.85 | $142.86 |
| SPY | 5 | $743.10 | $760.10 | $3,800.50 | $85.00 | — |
| TECH | 12 | $72.32 | $72.57 | $870.84 | $3.00 | $65.38 |
| VLO | 3 | $392.61 | $419.35 | $1,258.05 | $80.23 | $413.91 |
| WST | 2 | $370.69 | $391.74 | $783.48 | $42.10 | $354.76 |
| ZBRA | 3 | $345.13 | $386.56 | $1,159.68 | $124.30 | $352.09 |

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
