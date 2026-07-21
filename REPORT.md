# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-21 16:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,961.20** |
| Total return since inception | -0.19% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,966.36 (-0.17%) |
| Positions value | $16,085.18 |
| Settled cash | $1,486.06 |
| Unsettled cash (T+1) | $2,395.63 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.11% | -0.34% |
| Annualized volatility | 7.60% | 10.92% |
| Sharpe (rf 4%) | -5.11 | -1.31 |
| Max drawdown | 1.74% | 1.73% |
| EOD observations | 9 | 9 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $67.28 | $874.70 | $4.46 | $61.84 |
| DDOG | 3 | $260.67 | $255.49 | $766.47 | $-15.53 | $236.93 |
| DVA | 6 | $227.39 | $236.97 | $1,421.79 | $57.43 | $213.37 |
| FFIV | 3 | $430.59 | $411.33 | $1,234.00 | $-57.77 | $388.22 |
| FTNT | 5 | $155.14 | $157.72 | $788.60 | $12.92 | $150.16 |
| HUM | 2 | $401.64 | $406.77 | $813.54 | $10.26 | $366.83 |
| IBKR | 10 | $95.61 | $95.46 | $954.60 | $-1.46 | $87.64 |
| MPC | 3 | $306.56 | $316.28 | $948.84 | $29.16 | $283.79 |
| NTAP | 5 | $161.48 | $164.82 | $824.12 | $16.75 | $147.36 |
| SPY | 5 | $743.10 | $748.90 | $3,744.50 | $29.00 | — |
| STT | 8 | $185.86 | $184.82 | $1,478.60 | $-8.27 | $168.04 |
| UNH | 3 | $425.21 | $434.31 | $1,302.91 | $27.30 | $383.45 |
| VLO | 3 | $304.72 | $310.83 | $932.49 | $18.33 | $282.05 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-21T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T16:57` no_trade skip_entry **DOC** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **CSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **MGM** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **PSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **JBHT** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **CVS** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **WST** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **TRGP** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **DOC** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **CSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **MGM** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **PSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **JBHT** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **CVS** — insufficient investable cash (size $485, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
