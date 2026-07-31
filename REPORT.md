# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-31 18:06 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,530.54** |
| Total return since inception | -2.35% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,986.27 (-0.07%) |
| Positions value | $18,542.69 |
| Settled cash | $990.39 |
| Unsettled cash (T+1) | $4.26 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.79% | -0.24% |
| Annualized volatility | 9.70% | 14.62% |
| Sharpe (rf 4%) | -4.96 | -0.47 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 17 | 17 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $86.48 | $1,210.72 | $-22.03 | $79.24 |
| CSX | 17 | $50.29 | $50.41 | $856.97 | $2.02 | $45.25 |
| DDOG | 3 | $260.67 | $271.22 | $813.66 | $31.66 | $241.84 |
| DOC | 32 | $22.25 | $21.86 | $699.68 | $-12.34 | $20.55 |
| DVA | 6 | $227.39 | $239.46 | $1,436.76 | $72.40 | $216.78 |
| FTNT | 7 | $149.43 | $161.37 | $1,129.56 | $83.52 | $138.79 |
| HUM | 3 | $391.16 | $365.84 | $1,097.52 | $-75.95 | $330.02 |
| MPC | 3 | $306.56 | $313.60 | $940.80 | $21.12 | $287.83 |
| NTAP | 5 | $161.48 | $178.13 | $890.65 | $83.27 | $157.11 |
| PSX | 5 | $215.50 | $211.41 | $1,057.05 | $-20.43 | $191.32 |
| SPY | 5 | $743.10 | $745.67 | $3,728.38 | $12.88 | — |
| STT | 8 | $185.86 | $184.29 | $1,474.32 | $-12.55 | $168.04 |
| UNH | 3 | $425.21 | $418.27 | $1,254.81 | $-20.81 | $393.25 |
| VLO | 3 | $304.72 | $309.79 | $929.37 | $15.21 | $283.28 |
| WST | 3 | $336.32 | $340.81 | $1,022.44 | $13.48 | $305.31 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-31T18:06` no_trade — no signals crossed action thresholds this hour
- `2026-07-31T18:06` no_trade skip_entry **VTRS** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **BNY** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **ADM** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **UNP** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **WELL** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **TRV** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **URI** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **CVS** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T15:38` entry buy **CSX** — momentum entry: rank 11, mom 0.334, vol 26%
- `2026-07-31T15:38` no_trade skip_entry **VTRS** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **BNY** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **ADM** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **UNP** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **WELL** — insufficient investable cash (size $10, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
