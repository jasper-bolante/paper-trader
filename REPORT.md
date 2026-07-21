# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-21 15:23 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,915.64** |
| Total return since inception | -0.42% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,966.36 (-0.17%) |
| Positions value | $16,039.62 |
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
| CNC | 13 | $66.94 | $66.71 | $867.23 | $-3.01 | $61.84 |
| DDOG | 3 | $260.67 | $257.13 | $771.39 | $-10.61 | $236.93 |
| DVA | 6 | $227.39 | $235.72 | $1,414.32 | $49.96 | $213.37 |
| FFIV | 3 | $430.59 | $411.05 | $1,233.15 | $-58.62 | $388.22 |
| FTNT | 5 | $155.14 | $157.35 | $786.75 | $11.07 | $150.16 |
| HUM | 2 | $401.64 | $405.76 | $811.52 | $8.24 | $366.83 |
| IBKR | 10 | $95.61 | $94.70 | $947.05 | $-9.01 | $87.64 |
| MPC | 3 | $306.56 | $316.37 | $949.11 | $29.43 | $283.79 |
| NTAP | 5 | $161.48 | $163.99 | $819.95 | $12.57 | $147.36 |
| SPY | 5 | $743.10 | $747.52 | $3,737.60 | $22.10 | — |
| STT | 8 | $185.86 | $183.56 | $1,468.44 | $-18.43 | $168.04 |
| UNH | 3 | $425.21 | $433.11 | $1,299.33 | $23.71 | $383.45 |
| VLO | 3 | $304.72 | $311.26 | $933.78 | $19.62 | $282.05 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-21T15:23` no_trade skip_entry **DOC** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **CSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **MGM** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **PSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **JBHT** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **CVS** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **WST** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` no_trade skip_entry **TRGP** — insufficient investable cash (size $485, need >= $500)
- `2026-07-21T15:23` exit sell **URI** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-07-21T15:23` exit sell **BEN** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-07-20T20:50` system — eod_complete
- `2026-07-20T19:14` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T19:14` no_trade skip_entry **MNST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **CSX** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **DOC** — insufficient investable cash (size $488, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
