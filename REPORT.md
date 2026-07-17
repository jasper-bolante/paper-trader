# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-17 18:36 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,857.01** |
| Total return since inception | -0.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,209.12 (1.05%) |
| Positions value | $18,359.36 |
| Settled cash | $1,486.06 |
| Unsettled cash (T+1) | $17.25 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.87% | 0.87% |
| Annualized volatility | 8.74% | 10.38% |
| Sharpe (rf 4%) | -4.62 | 3.16 |
| Max drawdown | 1.50% | 0.77% |
| EOD observations | 7 | 7 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $32.51 | $1,365.42 | $-26.54 | $30.26 |
| CNC | 13 | $66.94 | $65.92 | $857.02 | $-13.22 | $61.84 |
| DDOG | 3 | $260.67 | $258.37 | $775.11 | $-6.89 | $236.06 |
| DVA | 6 | $227.39 | $235.31 | $1,411.86 | $47.50 | $211.95 |
| FFIV | 3 | $430.59 | $411.49 | $1,234.47 | $-57.30 | $388.22 |
| FTNT | 5 | $155.14 | $162.30 | $811.50 | $35.82 | $150.16 |
| HUM | 2 | $401.64 | $397.65 | $795.31 | $-7.97 | $366.83 |
| IBKR | 10 | $95.61 | $90.50 | $905.05 | $-51.01 | $87.64 |
| MPC | 3 | $306.56 | $311.80 | $935.40 | $15.72 | $275.76 |
| NTAP | 5 | $161.48 | $163.55 | $817.75 | $10.37 | $145.92 |
| SPY | 5 | $743.10 | $743.79 | $3,718.95 | $3.45 | — |
| STT | 8 | $185.86 | $182.54 | $1,460.32 | $-26.55 | $168.04 |
| UNH | 3 | $425.21 | $434.32 | $1,302.96 | $27.34 | $382.79 |
| URI | 1 | $1,090.35 | $1,049.07 | $1,049.07 | $-41.28 | $980.79 |
| VLO | 3 | $304.72 | $306.39 | $919.17 | $5.01 | $274.10 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-17T18:36` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T18:36` no_trade skip_entry **DAL** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MGM** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MNST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **CVS** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **DOC** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **WST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **JBHT** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **TRGP** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T16:42` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T16:42` no_trade skip_entry **DAL** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MGM** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MNST** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **CVS** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **DOC** — insufficient investable cash (size $489, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
