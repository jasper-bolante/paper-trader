# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-30 23:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,942.62** |
| Total return since inception | -0.29% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,390.41 (1.95%) |
| Positions value | $16,209.79 |
| Settled cash | $1,872.72 |
| Unsettled cash (T+1) | $1,875.77 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.35% | 1.77% |
| Annualized volatility | 11.64% | 11.10% |
| Sharpe (rf 4%) | -0.38 | 0.19 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 82 | 82 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $52.83 | $1,003.77 | $164.88 | $47.55 |
| CRL | 3 | $296.67 | $359.50 | $1,078.51 | $188.49 | $338.48 |
| EL | 10 | $105.95 | $109.23 | $1,092.30 | $32.82 | $98.41 |
| IQV | 2 | $255.46 | $267.33 | $534.66 | $23.75 | $251.42 |
| IT | 3 | $226.78 | $228.67 | $686.01 | $5.67 | $205.80 |
| MPC | 2 | $442.06 | $444.64 | $889.28 | $5.16 | $400.18 |
| NTAP | 4 | $207.54 | $199.19 | $796.78 | $-33.40 | $179.28 |
| PLTR | 5 | $194.57 | $184.10 | $920.50 | $-52.36 | $181.53 |
| PSX | 4 | $270.63 | $282.83 | $1,131.32 | $48.79 | $254.55 |
| RVTY | 9 | $122.75 | $156.91 | $1,412.23 | $307.51 | $149.17 |
| SPY | 5 | $743.10 | $756.00 | $3,780.00 | $64.50 | — |
| TECH | 12 | $72.32 | $72.69 | $872.28 | $4.44 | $65.44 |
| WDAY | 6 | $194.97 | $197.81 | $1,186.86 | $17.06 | $178.03 |
| WST | 2 | $370.69 | $412.64 | $825.28 | $83.90 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,007.39 | $0.00 | $1,299.66 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-10-28T19:02` no_trade skip_entry **CRM** — insufficient investable cash (size $413, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
