# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-28 23:27 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,481.65** |
| Total return since inception | 2.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,718.61 (3.59%) |
| Positions value | $15,537.70 |
| Settled cash | $1,454.49 |
| Unsettled cash (T+1) | $3,505.12 |
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
| APA | 19 | $44.15 | $51.12 | $971.28 | $132.39 | $46.71 |
| CRL | 3 | $296.67 | $374.00 | $1,122.00 | $231.98 | $336.60 |
| EL | 10 | $105.95 | $109.34 | $1,093.40 | $33.92 | $98.41 |
| FTNT | 5 | $183.53 | $174.21 | $871.03 | $-46.63 | $166.44 |
| IQV | 2 | $255.46 | $278.91 | $557.82 | $46.91 | $251.42 |
| MPC | 2 | $442.06 | $440.62 | $881.24 | $-2.88 | $397.53 |
| NTAP | 4 | $214.92 | $223.69 | $894.78 | $35.11 | $204.78 |
| PLTR | 5 | $194.57 | $195.13 | $975.65 | $2.79 | $181.53 |
| RVTY | 9 | $122.75 | $165.37 | $1,488.29 | $383.57 | $148.83 |
| SPY | 5 | $743.10 | $769.80 | $3,849.00 | $133.50 | — |
| TECH | 12 | $72.32 | $72.68 | $872.16 | $4.32 | $65.43 |
| WST | 2 | $370.69 | $403.90 | $807.80 | $66.42 | $363.51 |
| ZBRA | 3 | $345.13 | $384.42 | $1,153.26 | $117.88 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-746.41 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-28T19:02` exit sell **MPC** — trailing stop 10%
- `2026-10-28T19:02` exit sell **PSX** — trailing stop 10%
- `2026-10-27T23:05` system — eod_complete
- `2026-10-27T18:52` no_trade skip_entry **HPQ** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **CNC** — insufficient investable cash (size $53, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
