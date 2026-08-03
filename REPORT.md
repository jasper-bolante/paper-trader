# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-03 20:14 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,538.13** |
| Total return since inception | -2.31% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,388.37 (1.94%) |
| Positions value | $17,435.98 |
| Settled cash | $990.39 |
| Unsettled cash (T+1) | $1,118.56 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.38% | 1.76% |
| Annualized volatility | 9.38% | 14.88% |
| Sharpe (rf 4%) | -3.97 | 1.45 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 19 | 19 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $85.25 | $1,193.57 | $-39.18 | $79.24 |
| CSX | 17 | $50.29 | $49.82 | $846.94 | $-8.01 | $45.34 |
| DDOG | 3 | $260.67 | $273.54 | $820.62 | $38.62 | $246.19 |
| DOC | 32 | $22.25 | $21.65 | $692.80 | $-19.22 | $20.55 |
| DVA | 6 | $227.39 | $233.61 | $1,401.66 | $37.30 | $216.78 |
| FTNT | 7 | $149.43 | $163.14 | $1,141.98 | $95.94 | $146.83 |
| MPC | 3 | $306.56 | $307.30 | $921.90 | $2.22 | $287.83 |
| NTAP | 5 | $161.48 | $182.95 | $914.75 | $107.37 | $164.66 |
| PSX | 5 | $215.50 | $206.22 | $1,031.10 | $-46.38 | $191.32 |
| SPY | 5 | $743.10 | $757.53 | $3,787.65 | $72.15 | — |
| STT | 8 | $185.86 | $183.77 | $1,470.16 | $-16.71 | $168.04 |
| UNH | 3 | $425.21 | $415.38 | $1,246.14 | $-29.48 | $393.25 |
| VLO | 3 | $304.72 | $307.51 | $922.53 | $8.37 | $283.28 |
| WST | 3 | $336.32 | $348.06 | $1,044.18 | $35.22 | $313.25 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-738.62 | $0.00 | $95.51 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-03T20:14` system — corporate_actions_synced
- `2026-08-03T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-03T18:18` no_trade skip_entry **ALL** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **NUE** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **HPQ** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **WELL** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **TRGP** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **TRV** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **CVS** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **FFIV** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **ALL** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **NUE** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **HPQ** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **WELL** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **TRGP** — insufficient investable cash (size $2, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
