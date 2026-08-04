# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-04 20:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,730.52** |
| Total return since inception | -1.35% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,753.87 (3.77%) |
| Positions value | $18,356.51 |
| Settled cash | $1,376.55 |
| Unsettled cash (T+1) | $4.26 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.41% | 3.59% |
| Annualized volatility | 9.99% | 15.72% |
| Sharpe (rf 4%) | -2.24 | 2.80 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 20 | 20 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $86.34 | $1,208.76 | $-23.99 | $79.24 |
| CSX | 17 | $50.29 | $51.02 | $867.34 | $12.39 | $45.92 |
| DDOG | 3 | $260.67 | $288.17 | $864.51 | $82.51 | $259.35 |
| DOC | 32 | $22.25 | $21.62 | $691.84 | $-20.18 | $20.55 |
| DVA | 6 | $227.39 | $227.93 | $1,367.58 | $3.22 | $216.78 |
| FTNT | 7 | $149.43 | $168.27 | $1,177.89 | $131.85 | $151.44 |
| HUM | 2 | $383.80 | $362.33 | $724.66 | $-42.93 | $327.49 |
| MPC | 3 | $306.56 | $312.60 | $937.80 | $18.12 | $287.83 |
| NTAP | 5 | $161.48 | $190.47 | $952.35 | $144.97 | $171.42 |
| PSX | 5 | $215.50 | $205.99 | $1,029.95 | $-47.53 | $191.32 |
| SPY | 5 | $743.10 | $771.11 | $3,855.55 | $140.05 | — |
| STT | 8 | $185.86 | $185.23 | $1,481.84 | $-5.03 | $168.04 |
| UNH | 3 | $425.21 | $407.73 | $1,223.19 | $-52.43 | $393.25 |
| VLO | 3 | $304.72 | $308.61 | $925.83 | $11.67 | $283.28 |
| WST | 3 | $336.32 | $349.14 | $1,047.42 | $38.46 | $314.23 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-699.17 | $0.00 | $134.95 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-04T18:12` no_trade — no signals crossed action thresholds this hour
- `2026-08-04T18:12` no_trade skip_entry **WELL** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **VTRS** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **ALL** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **CVS** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **TRV** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **HPQ** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **FFIV** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **CNC** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T15:58` entry buy **HUM** — momentum entry: rank 5, mom 0.601, vol 37%
- `2026-08-04T15:58` no_trade skip_entry **WELL** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **VTRS** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **ALL** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **CVS** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **TRV** — insufficient investable cash (size $385, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
