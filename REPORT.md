# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-29 23:31 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,206.93** |
| Total return since inception | 1.03% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,596.42 (2.98%) |
| Positions value | $16,876.44 |
| Settled cash | $2,692.46 |
| Unsettled cash (T+1) | $653.69 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.97% | 2.80% |
| Annualized volatility | 11.48% | 11.01% |
| Sharpe (rf 4%) | -0.03 | 0.48 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 81 | 81 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $51.50 | $978.50 | $139.61 | $46.71 |
| CRL | 3 | $296.67 | $376.09 | $1,128.27 | $238.25 | $338.48 |
| EL | 10 | $105.95 | $108.87 | $1,088.70 | $29.22 | $98.41 |
| IQV | 2 | $255.46 | $274.67 | $549.34 | $38.43 | $251.42 |
| MPC | 2 | $442.06 | $432.52 | $865.04 | $-19.08 | $397.53 |
| NTAP | 4 | $214.92 | $218.37 | $873.48 | $13.81 | $204.78 |
| PLTR | 5 | $194.57 | $194.17 | $970.85 | $-2.01 | $181.53 |
| PSX | 4 | $270.63 | $273.66 | $1,094.64 | $12.11 | $246.29 |
| RVTY | 9 | $122.75 | $165.74 | $1,491.66 | $386.94 | $149.17 |
| SPY | 5 | $743.10 | $765.26 | $3,826.30 | $110.80 | — |
| TECH | 12 | $72.32 | $72.71 | $872.52 | $4.68 | $65.44 |
| WDAY | 6 | $194.97 | $195.43 | $1,172.58 | $2.78 | $175.89 |
| WST | 2 | $370.69 | $416.21 | $832.42 | $91.04 | $374.59 |
| ZBRA | 3 | $345.13 | $377.38 | $1,132.14 | $96.76 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,025.20 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-29T23:31` system — corporate_actions_synced
- `2026-10-29T19:09` entry buy **WDAY** — momentum entry: rank 7, mom 0.595, vol 34%
- `2026-10-29T19:09` entry buy **PSX** — momentum entry: rank 6, mom 0.604, vol 37%
- `2026-10-29T19:09` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-29T19:09` exit sell **FTNT** — trailing stop 10%
- `2026-10-28T23:27` system — eod_complete
- `2026-10-28T19:02` entry buy **MPC** — momentum entry: rank 1, mom 0.830, vol 42%
- `2026-10-28T19:02` no_trade skip_entry **CRM** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **CNC** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **HUM** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **IT** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **NOW** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **WDAY** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **PSX** — insufficient investable cash (size $413, need >= $500)
- `2026-10-28T19:02` no_trade skip_entry **VEEV** — insufficient investable cash (size $413, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
