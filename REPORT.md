# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-03 16:04 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,625.78** |
| Total return since inception | -1.87% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,099.31 (0.50%) |
| Positions value | $17,523.63 |
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
| BBY | 14 | $88.05 | $83.80 | $1,173.20 | $-59.55 | $79.24 |
| CSX | 17 | $50.29 | $50.09 | $851.45 | $-3.50 | $45.34 |
| DDOG | 3 | $260.67 | $274.69 | $824.07 | $42.07 | $241.84 |
| DOC | 32 | $22.25 | $21.86 | $699.68 | $-12.34 | $20.55 |
| DVA | 6 | $227.39 | $241.08 | $1,446.48 | $82.12 | $216.78 |
| FTNT | 7 | $149.43 | $163.63 | $1,145.44 | $99.40 | $145.70 |
| MPC | 3 | $306.56 | $316.21 | $948.64 | $28.97 | $287.83 |
| NTAP | 5 | $161.48 | $182.52 | $912.60 | $105.22 | $160.74 |
| PSX | 5 | $215.50 | $210.15 | $1,050.75 | $-26.73 | $191.32 |
| SPY | 5 | $743.10 | $756.05 | $3,780.27 | $64.77 | — |
| STT | 8 | $185.86 | $182.53 | $1,460.24 | $-26.63 | $168.04 |
| UNH | 3 | $425.21 | $415.96 | $1,247.88 | $-27.74 | $393.25 |
| VLO | 3 | $304.72 | $313.25 | $939.75 | $25.59 | $283.28 |
| WST | 3 | $336.32 | $347.73 | $1,043.18 | $34.22 | $306.91 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-738.62 | $0.00 | $95.51 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-03T16:04` no_trade skip_entry **ALL** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **NUE** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **HPQ** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **WELL** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **TRGP** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **TRV** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **CVS** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` no_trade skip_entry **FFIV** — insufficient investable cash (size $2, need >= $500)
- `2026-08-03T16:04` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-07-31T20:05` system — eod_complete
- `2026-07-31T18:06` no_trade — no signals crossed action thresholds this hour
- `2026-07-31T18:06` no_trade skip_entry **VTRS** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **BNY** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **ADM** — insufficient investable cash (size $7, need >= $500)
- `2026-07-31T18:06` no_trade skip_entry **UNP** — insufficient investable cash (size $7, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
