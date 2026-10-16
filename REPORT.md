# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-16 21:36 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,145.38** |
| Total return since inception | 0.73% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,543.94 (2.72%) |
| Positions value | $17,688.78 |
| Settled cash | $1,450.37 |
| Unsettled cash (T+1) | $1,021.08 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.66% | 2.54% |
| Annualized volatility | 11.10% | 11.17% |
| Sharpe (rf 4%) | -0.10 | 0.49 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 72 | 72 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.16 | $934.04 | $95.15 | $44.24 |
| CRL | 3 | $296.67 | $300.23 | $900.69 | $10.67 | $279.86 |
| DDOG | 3 | $264.28 | $247.03 | $741.11 | $-51.75 | $222.33 |
| FFIV | 2 | $448.44 | $441.80 | $883.60 | $-13.29 | $431.75 |
| IQV | 2 | $255.46 | $266.89 | $533.78 | $22.87 | $247.54 |
| META | 1 | $723.49 | $709.42 | $709.42 | $-14.07 | $686.26 |
| MPC | 3 | $399.06 | $478.21 | $1,434.63 | $237.46 | $436.32 |
| NTAP | 4 | $214.92 | $203.79 | $815.18 | $-44.49 | $193.37 |
| PSX | 5 | $215.50 | $293.39 | $1,466.95 | $389.47 | $267.61 |
| RVTY | 9 | $122.75 | $152.62 | $1,373.58 | $268.86 | $141.67 |
| SPY | 5 | $743.10 | $763.31 | $3,816.55 | $101.05 | — |
| TECH | 12 | $72.32 | $72.56 | $870.66 | $2.82 | $65.36 |
| VLO | 3 | $392.61 | $444.70 | $1,334.10 | $156.28 | $413.91 |
| WST | 2 | $370.69 | $383.81 | $767.62 | $26.24 | $345.43 |
| ZBRA | 3 | $345.13 | $368.96 | $1,106.88 | $71.50 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,197.61 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-16T17:39` entry buy **DDOG** — momentum entry: rank 3, mom 0.788, vol 44%
- `2026-10-16T17:39` no_trade skip_entry **CRM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **MSFT** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **NOW** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **HUM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **WDAY** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **PLTR** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **VEEV** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **FTNT** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` exit sell **FTNT** — trailing stop 10%
- `2026-10-16T17:39` exit sell **DDOG** — trailing stop 10%
- `2026-10-15T21:40` system — eod_complete
- `2026-10-15T17:51` entry buy **NTAP** — momentum entry: rank 1, mom 0.872, vol 46%
- `2026-10-15T17:51` exit sell **NTAP** — trailing stop 10%
- `2026-10-14T21:53` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
