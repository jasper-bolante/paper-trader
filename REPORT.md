# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-28 19:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,513.38** |
| Total return since inception | 2.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,712.69 (3.56%) |
| Positions value | $15,569.42 |
| Settled cash | $1,454.49 |
| Unsettled cash (T+1) | $3,505.12 |
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
| APA | 19 | $44.15 | $51.72 | $982.68 | $143.79 | $46.71 |
| CRL | 3 | $296.67 | $371.45 | $1,114.35 | $224.33 | $323.07 |
| EL | 10 | $105.95 | $109.24 | $1,092.40 | $32.92 | $97.97 |
| FTNT | 5 | $183.53 | $178.22 | $891.10 | $-26.56 | $166.44 |
| IQV | 2 | $255.46 | $276.88 | $553.76 | $42.85 | $251.42 |
| MPC | 2 | $442.06 | $441.69 | $883.39 | $-0.73 | $397.53 |
| NTAP | 4 | $214.92 | $224.47 | $897.88 | $38.21 | $204.78 |
| PLTR | 5 | $194.57 | $194.26 | $971.30 | $-1.56 | $181.53 |
| RVTY | 9 | $122.75 | $165.90 | $1,493.06 | $388.34 | $145.78 |
| SPY | 5 | $743.10 | $771.98 | $3,859.90 | $144.40 | — |
| TECH | 12 | $72.32 | $72.63 | $871.56 | $3.72 | $65.43 |
| WST | 2 | $370.69 | $402.11 | $804.22 | $62.84 | $358.31 |
| ZBRA | 3 | $345.13 | $384.61 | $1,153.83 | $118.45 | $352.09 |

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
