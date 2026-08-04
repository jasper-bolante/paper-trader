# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-04 18:12 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,771.84** |
| Total return since inception | -1.14% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,388.37 (1.94%) |
| Positions value | $18,397.83 |
| Settled cash | $1,376.55 |
| Unsettled cash (T+1) | $4.26 |
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
| BBY | 14 | $88.05 | $87.00 | $1,218.00 | $-14.75 | $79.24 |
| CSX | 17 | $50.29 | $50.66 | $861.13 | $6.18 | $45.34 |
| DDOG | 3 | $260.67 | $288.41 | $865.23 | $83.23 | $246.19 |
| DOC | 32 | $22.25 | $21.55 | $689.76 | $-22.26 | $20.55 |
| DVA | 6 | $227.39 | $228.89 | $1,373.34 | $8.98 | $216.78 |
| FTNT | 7 | $149.43 | $167.98 | $1,175.86 | $129.82 | $146.83 |
| HUM | 2 | $383.80 | $362.93 | $725.86 | $-41.73 | $327.49 |
| MPC | 3 | $306.56 | $312.50 | $937.50 | $17.82 | $287.83 |
| NTAP | 5 | $161.48 | $195.00 | $975.00 | $167.62 | $164.66 |
| PSX | 5 | $215.50 | $206.26 | $1,031.30 | $-46.18 | $191.32 |
| SPY | 5 | $743.10 | $771.81 | $3,859.05 | $143.55 | — |
| STT | 8 | $185.86 | $186.15 | $1,489.20 | $2.33 | $168.04 |
| UNH | 3 | $425.21 | $410.30 | $1,230.90 | $-44.72 | $393.25 |
| VLO | 3 | $304.72 | $307.89 | $923.67 | $9.51 | $283.28 |
| WST | 3 | $336.32 | $347.34 | $1,042.02 | $33.06 | $313.25 |

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
