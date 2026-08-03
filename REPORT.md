# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-03 18:18 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,569.20** |
| Total return since inception | -2.15% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,099.31 (0.50%) |
| Positions value | $17,467.05 |
| Settled cash | $990.39 |
| Unsettled cash (T+1) | $1,118.56 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.41% | 0.32% |
| Annualized volatility | 9.65% | 14.33% |
| Sharpe (rf 4%) | -4.11 | 0.12 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 18 | 18 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $84.02 | $1,176.21 | $-56.54 | $79.24 |
| CSX | 17 | $50.29 | $49.74 | $845.66 | $-9.29 | $45.34 |
| DDOG | 3 | $260.67 | $276.77 | $830.31 | $48.31 | $241.84 |
| DOC | 32 | $22.25 | $21.73 | $695.20 | $-16.82 | $20.55 |
| DVA | 6 | $227.39 | $235.10 | $1,410.60 | $46.24 | $216.78 |
| FTNT | 7 | $149.43 | $163.97 | $1,147.76 | $101.72 | $145.70 |
| MPC | 3 | $306.56 | $310.60 | $931.80 | $12.12 | $287.83 |
| NTAP | 5 | $161.48 | $183.96 | $919.80 | $112.42 | $160.74 |
| PSX | 5 | $215.50 | $207.69 | $1,038.45 | $-39.03 | $191.32 |
| SPY | 5 | $743.10 | $758.08 | $3,790.38 | $74.88 | — |
| STT | 8 | $185.86 | $182.96 | $1,463.68 | $-23.19 | $168.04 |
| UNH | 3 | $425.21 | $416.22 | $1,248.66 | $-26.96 | $393.25 |
| VLO | 3 | $304.72 | $308.89 | $926.67 | $12.51 | $283.28 |
| WST | 3 | $336.32 | $347.29 | $1,041.87 | $32.91 | $306.91 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-738.62 | $0.00 | $95.51 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-03T16:04` no_trade skip_entry **TRV** — insufficient investable cash (size $2, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
