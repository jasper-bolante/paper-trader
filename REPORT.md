# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-29 19:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,171.11** |
| Total return since inception | 0.86% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,718.61 (3.59%) |
| Positions value | $16,840.62 |
| Settled cash | $2,692.46 |
| Unsettled cash (T+1) | $653.69 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.34% | 3.41% |
| Annualized volatility | 11.29% | 11.03% |
| Sharpe (rf 4%) | 0.35 | 0.66 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 80 | 80 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $51.29 | $974.51 | $135.62 | $46.71 |
| CRL | 3 | $296.67 | $374.95 | $1,124.85 | $234.83 | $336.60 |
| EL | 10 | $105.95 | $109.19 | $1,091.90 | $32.42 | $98.41 |
| IQV | 2 | $255.46 | $273.48 | $546.95 | $36.04 | $251.42 |
| MPC | 2 | $442.06 | $423.68 | $847.36 | $-36.76 | $397.53 |
| NTAP | 4 | $214.92 | $218.07 | $872.28 | $12.61 | $204.78 |
| PLTR | 5 | $194.57 | $193.57 | $967.88 | $-4.99 | $181.53 |
| PSX | 4 | $270.63 | $270.49 | $1,081.96 | $-0.57 | $243.44 |
| RVTY | 9 | $122.75 | $165.20 | $1,486.80 | $382.08 | $148.83 |
| SPY | 5 | $743.10 | $767.63 | $3,838.18 | $122.68 | — |
| TECH | 12 | $72.32 | $72.70 | $872.40 | $4.56 | $65.43 |
| WDAY | 6 | $194.97 | $194.82 | $1,168.92 | $-0.88 | $175.34 |
| WST | 2 | $370.69 | $419.38 | $838.76 | $97.38 | $363.51 |
| ZBRA | 3 | $345.13 | $375.96 | $1,127.88 | $92.50 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,025.20 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-28T19:02` exit sell **FFIV** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
