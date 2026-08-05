# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-05 18:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,528.60** |
| Total return since inception | -2.36% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,753.87 (3.77%) |
| Positions value | $15,687.72 |
| Settled cash | $1,377.21 |
| Unsettled cash (T+1) | $2,470.47 |
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
| BBY | 14 | $88.05 | $84.42 | $1,181.88 | $-50.87 | $79.24 |
| CSX | 17 | $50.29 | $50.97 | $866.41 | $11.46 | $45.92 |
| DDOG | 3 | $260.67 | $287.91 | $863.73 | $81.73 | $259.35 |
| DOC | 32 | $22.25 | $21.86 | $699.36 | $-12.66 | $20.55 |
| FTNT | 7 | $149.43 | $165.26 | $1,156.86 | $110.82 | $151.44 |
| HUM | 2 | $383.80 | $364.57 | $729.15 | $-38.44 | $327.49 |
| MPC | 3 | $306.56 | $301.12 | $903.36 | $-16.32 | $287.83 |
| NTAP | 5 | $161.48 | $190.07 | $950.35 | $142.97 | $171.42 |
| PSX | 5 | $215.50 | $202.67 | $1,013.35 | $-64.13 | $191.32 |
| SPY | 5 | $743.10 | $771.84 | $3,859.18 | $143.68 | — |
| STT | 8 | $185.86 | $188.38 | $1,507.04 | $20.17 | $168.04 |
| VLO | 3 | $304.72 | $302.93 | $908.79 | $-5.37 | $283.28 |
| WST | 3 | $336.32 | $349.43 | $1,048.28 | $39.32 | $314.23 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-872.29 | $0.00 | $134.95 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-05T18:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-05T18:07` no_trade skip_entry **CVS** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **TRV** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **NUE** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CSCO** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CNC** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **FFIV** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **HPQ** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **DVA** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CVS** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **TRV** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **NUE** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CSCO** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CNC** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **FFIV** — insufficient investable cash (size $395, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
