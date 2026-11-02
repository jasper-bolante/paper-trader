# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-02 22:26 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,549.39** |
| Total return since inception | -2.25% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.08 (1.57%) |
| Positions value | $15,816.56 |
| Settled cash | $3,743.11 |
| Unsettled cash (T+1) | $5.38 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.32% | 1.39% |
| Annualized volatility | 12.07% | 11.05% |
| Sharpe (rf 4%) | -0.87 | 0.08 |
| Max drawdown | 5.68% | 3.57% |
| EOD observations | 83 | 83 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $48.82 | $927.58 | $88.69 | $47.55 |
| CRL | 3 | $296.67 | $338.42 | $1,015.26 | $125.24 | $338.48 |
| EL | 10 | $105.95 | $104.74 | $1,047.40 | $-12.08 | $98.41 |
| IQV | 2 | $255.46 | $258.43 | $516.86 | $5.95 | $251.42 |
| IT | 3 | $226.78 | $235.34 | $706.02 | $25.68 | $211.81 |
| MPC | 2 | $442.06 | $430.48 | $860.96 | $-23.16 | $400.18 |
| NTAP | 4 | $207.54 | $185.21 | $740.82 | $-89.36 | $179.28 |
| PLTR | 5 | $194.57 | $178.88 | $894.40 | $-78.46 | $181.53 |
| PSX | 4 | $270.63 | $275.08 | $1,100.32 | $17.79 | $254.55 |
| RVTY | 9 | $122.75 | $151.70 | $1,365.30 | $260.58 | $149.17 |
| SPY | 5 | $743.10 | $753.17 | $3,765.85 | $50.35 | — |
| TECH | 12 | $72.32 | $72.67 | $872.04 | $4.20 | $65.44 |
| WDAY | 6 | $194.97 | $198.05 | $1,188.30 | $18.50 | $178.25 |
| WST | 2 | $370.69 | $407.73 | $815.45 | $74.07 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,007.39 | $0.00 | $1,299.66 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-30T23:07` system — eod_complete
- `2026-10-30T23:07` system **SPY** — benchmark_dividend
- `2026-10-30T18:47` entry buy **NTAP** — momentum entry: rank 7, mom 0.614, vol 42%
- `2026-10-30T18:47` entry buy **IT** — momentum entry: rank 5, mom 0.623, vol 45%
- `2026-10-30T18:47` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-30T18:47` exit sell **NTAP** — trailing stop 10%
- `2026-10-30T18:47` exit sell **ZBRA** — trailing stop 10%
- `2026-10-29T23:31` system — eod_complete
- `2026-10-29T23:31` system — corporate_actions_synced
- `2026-10-29T19:09` entry buy **WDAY** — momentum entry: rank 7, mom 0.595, vol 34%
- `2026-10-29T19:09` entry buy **PSX** — momentum entry: rank 6, mom 0.604, vol 37%
- `2026-10-29T19:09` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-29T19:09` exit sell **FTNT** — trailing stop 10%
- `2026-10-28T23:27` system — eod_complete
- `2026-10-28T19:02` entry buy **MPC** — momentum entry: rank 1, mom 0.830, vol 42%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
