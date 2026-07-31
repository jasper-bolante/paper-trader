# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-31 20:05 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,531.44** |
| Total return since inception | -2.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,099.31 (0.50%) |
| Positions value | $18,543.59 |
| Settled cash | $990.39 |
| Unsettled cash (T+1) | $4.26 |
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
| BBY | 14 | $88.05 | $86.18 | $1,206.52 | $-26.23 | $79.24 |
| CSX | 17 | $50.29 | $50.38 | $856.46 | $1.51 | $45.34 |
| DDOG | 3 | $260.67 | $267.97 | $803.91 | $21.91 | $241.84 |
| DOC | 32 | $22.25 | $21.83 | $698.56 | $-13.46 | $20.55 |
| DVA | 6 | $227.39 | $240.04 | $1,440.27 | $75.91 | $216.78 |
| FTNT | 7 | $149.43 | $161.89 | $1,133.23 | $87.19 | $145.70 |
| HUM | 3 | $391.16 | $363.85 | $1,091.55 | $-81.92 | $330.02 |
| MPC | 3 | $306.56 | $316.34 | $949.02 | $29.34 | $287.83 |
| NTAP | 5 | $161.48 | $178.60 | $893.00 | $85.62 | $160.74 |
| PSX | 5 | $215.50 | $211.69 | $1,058.45 | $-19.03 | $191.32 |
| SPY | 5 | $743.10 | $746.79 | $3,733.95 | $18.45 | — |
| STT | 8 | $185.86 | $184.21 | $1,473.68 | $-13.19 | $168.04 |
| UNH | 3 | $425.21 | $414.43 | $1,243.29 | $-32.33 | $393.25 |
| VLO | 3 | $304.72 | $312.89 | $938.67 | $24.51 | $283.28 |
| WST | 3 | $336.32 | $341.01 | $1,023.03 | $14.07 | $306.91 |

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
