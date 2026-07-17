# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-17 16:42 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,837.55** |
| Total return since inception | -0.81% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,209.12 (1.05%) |
| Positions value | $18,339.90 |
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
| BEN | 42 | $33.14 | $32.83 | $1,378.65 | $-13.31 | $30.26 |
| CNC | 13 | $66.94 | $65.26 | $848.38 | $-21.86 | $61.84 |
| DDOG | 3 | $260.67 | $257.10 | $771.30 | $-10.70 | $236.06 |
| DVA | 6 | $227.39 | $236.22 | $1,417.29 | $52.93 | $211.95 |
| FFIV | 3 | $430.59 | $407.90 | $1,223.70 | $-68.07 | $388.22 |
| FTNT | 5 | $155.14 | $161.72 | $808.62 | $32.95 | $150.16 |
| HUM | 2 | $401.64 | $395.39 | $790.78 | $-12.50 | $366.83 |
| IBKR | 10 | $95.61 | $91.31 | $913.05 | $-43.01 | $87.64 |
| MPC | 3 | $306.56 | $307.28 | $921.84 | $2.16 | $275.76 |
| NTAP | 5 | $161.48 | $162.24 | $811.20 | $3.82 | $145.92 |
| SPY | 5 | $743.10 | $745.94 | $3,729.70 | $14.20 | — |
| STT | 8 | $185.86 | $183.02 | $1,464.16 | $-22.71 | $168.04 |
| UNH | 3 | $425.21 | $432.11 | $1,296.33 | $20.71 | $382.79 |
| URI | 1 | $1,090.35 | $1,053.83 | $1,053.83 | $-36.52 | $980.79 |
| VLO | 3 | $304.72 | $303.69 | $911.07 | $-3.09 | $274.10 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-17T16:42` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T16:42` no_trade skip_entry **DAL** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MGM** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MNST** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **CVS** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **DOC** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **WST** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **JBHT** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **TRGP** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T14:59` entry buy **VLO** — momentum entry: rank 9, mom 0.376, vol 40%
- `2026-07-17T14:59` no_trade skip_entry **DAL** — insufficient investable cash (size $435, need >= $500)
- `2026-07-17T14:59` no_trade skip_entry **MGM** — insufficient investable cash (size $435, need >= $500)
- `2026-07-17T14:59` no_trade skip_entry **MNST** — insufficient investable cash (size $435, need >= $500)
- `2026-07-17T14:59` no_trade skip_entry **CVS** — insufficient investable cash (size $435, need >= $500)
- `2026-07-17T14:59` no_trade skip_entry **DOC** — insufficient investable cash (size $435, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
