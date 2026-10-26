# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-26 19:30 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,730.34** |
| Total return since inception | 3.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,457.54 (2.29%) |
| Positions value | $19,633.65 |
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
| APA | 19 | $44.15 | $51.87 | $985.53 | $146.64 | $46.71 |
| CRL | 3 | $296.67 | $353.46 | $1,060.38 | $170.36 | $310.58 |
| EL | 10 | $105.95 | $108.72 | $1,087.25 | $27.77 | $97.82 |
| FFIV | 2 | $448.44 | $460.88 | $921.76 | $24.87 | $431.75 |
| FTNT | 5 | $183.53 | $183.28 | $916.40 | $-1.26 | $161.98 |
| IQV | 2 | $255.46 | $273.06 | $546.11 | $35.20 | $251.42 |
| MPC | 3 | $399.06 | $470.49 | $1,411.47 | $214.30 | $436.32 |
| NTAP | 4 | $214.92 | $223.64 | $894.56 | $34.89 | $195.57 |
| PLTR | 5 | $194.57 | $199.17 | $995.85 | $22.99 | $181.53 |
| PSX | 5 | $215.50 | $288.95 | $1,444.75 | $367.27 | $267.61 |
| RVTY | 9 | $122.75 | $160.11 | $1,440.99 | $336.27 | $142.86 |
| SPY | 5 | $743.10 | $765.21 | $3,826.05 | $110.55 | — |
| TECH | 12 | $72.32 | $72.67 | $871.98 | $4.14 | $65.38 |
| VLO | 3 | $392.61 | $427.03 | $1,281.09 | $103.27 | $413.91 |
| WST | 2 | $370.69 | $392.86 | $785.72 | $44.34 | $354.76 |
| ZBRA | 3 | $345.13 | $387.92 | $1,163.76 | $128.38 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,128.42 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-26T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-10-26T19:30` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T21:35` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
