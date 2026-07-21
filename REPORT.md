# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-21 18:51 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,940.50** |
| Total return since inception | -0.30% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,966.36 (-0.17%) |
| Positions value | $16,064.48 |
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
| CNC | 13 | $66.94 | $67.19 | $873.47 | $3.23 | $61.84 |
| DDOG | 3 | $260.67 | $253.66 | $761.00 | $-21.00 | $236.93 |
| DVA | 6 | $227.39 | $237.06 | $1,422.36 | $58.00 | $213.37 |
| FFIV | 3 | $430.59 | $410.51 | $1,231.53 | $-60.24 | $388.22 |
| FTNT | 5 | $155.14 | $157.12 | $785.60 | $9.92 | $150.16 |
| HUM | 2 | $401.64 | $405.46 | $810.92 | $7.64 | $366.83 |
| IBKR | 10 | $95.61 | $94.45 | $944.50 | $-11.56 | $87.64 |
| MPC | 3 | $306.56 | $319.02 | $957.06 | $37.38 | $283.79 |
| NTAP | 5 | $161.48 | $164.35 | $821.75 | $14.37 | $147.36 |
| SPY | 5 | $743.10 | $748.48 | $3,742.40 | $26.90 | — |
| STT | 8 | $185.86 | $184.32 | $1,474.56 | $-12.31 | $168.04 |
| UNH | 3 | $425.21 | $433.89 | $1,301.67 | $26.05 | $383.45 |
| VLO | 3 | $304.72 | $312.56 | $937.66 | $23.50 | $282.05 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-21T18:51` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T18:51` no_trade skip_entry **DOC** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **CSX** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **MGM** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **PSX** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **JBHT** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **CVS** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **WST** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **TRGP** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T16:57` no_trade skip_entry **DOC** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **CSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **MGM** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **PSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **JBHT** — insufficient investable cash (size $482, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
