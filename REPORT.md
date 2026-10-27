# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-27 23:05 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,526.94** |
| Total return since inception | 2.63% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,712.69 (3.56%) |
| Positions value | $18,189.17 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $1,258.50 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.56% | 3.38% |
| Annualized volatility | 11.35% | 11.10% |
| Sharpe (rf 4%) | 0.42 | 0.66 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 79 | 79 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $50.80 | $965.11 | $126.22 | $46.71 |
| CRL | 3 | $296.67 | $358.96 | $1,076.89 | $186.88 | $323.07 |
| EL | 10 | $105.95 | $108.34 | $1,083.45 | $23.97 | $97.97 |
| FFIV | 2 | $448.44 | $461.38 | $922.76 | $25.87 | $431.75 |
| FTNT | 5 | $183.53 | $184.93 | $924.65 | $6.99 | $166.44 |
| IQV | 2 | $255.46 | $271.44 | $542.88 | $31.97 | $251.42 |
| MPC | 3 | $399.06 | $435.92 | $1,307.76 | $110.59 | $436.32 |
| NTAP | 4 | $214.92 | $227.53 | $910.12 | $50.45 | $204.78 |
| PLTR | 5 | $194.57 | $198.73 | $993.65 | $20.79 | $181.53 |
| PSX | 5 | $215.50 | $268.39 | $1,341.95 | $264.47 | $267.61 |
| RVTY | 9 | $122.75 | $161.98 | $1,457.82 | $353.10 | $145.78 |
| SPY | 5 | $743.10 | $769.58 | $3,847.90 | $132.40 | — |
| TECH | 12 | $72.32 | $72.61 | $871.32 | $3.48 | $65.43 |
| WST | 2 | $370.69 | $398.12 | $796.25 | $54.87 | $358.31 |
| ZBRA | 3 | $345.13 | $382.22 | $1,146.66 | $111.28 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,065.16 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-27T18:52` no_trade skip_entry **HPQ** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **CNC** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **IT** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **NOW** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **WDAY** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **HUM** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **VLO** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **VEEV** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` exit sell **VLO** — trailing stop 10%
- `2026-10-26T23:16` system — eod_complete
- `2026-10-26T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-10-26T19:30` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T21:35` system — eod_complete
- `2026-10-23T17:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-23T17:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
