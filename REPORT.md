# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-05 15:41 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,501.36** |
| Total return since inception | -2.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,753.87 (3.77%) |
| Positions value | $15,660.48 |
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
| BBY | 14 | $88.05 | $84.50 | $1,183.00 | $-49.75 | $79.24 |
| CSX | 17 | $50.29 | $50.80 | $863.68 | $8.73 | $45.92 |
| DDOG | 3 | $260.67 | $284.51 | $853.53 | $71.53 | $259.35 |
| DOC | 32 | $22.25 | $21.80 | $697.44 | $-14.58 | $20.55 |
| FTNT | 7 | $149.43 | $165.78 | $1,160.46 | $114.42 | $151.44 |
| HUM | 2 | $383.80 | $361.95 | $723.90 | $-43.69 | $327.49 |
| MPC | 3 | $306.56 | $302.33 | $907.00 | $-12.68 | $287.83 |
| NTAP | 5 | $161.48 | $189.58 | $947.90 | $140.52 | $171.42 |
| PSX | 5 | $215.50 | $201.18 | $1,005.88 | $-71.61 | $191.32 |
| SPY | 5 | $743.10 | $772.10 | $3,860.50 | $145.00 | — |
| STT | 8 | $185.86 | $187.02 | $1,496.16 | $9.29 | $168.04 |
| VLO | 3 | $304.72 | $302.88 | $908.65 | $-5.50 | $283.28 |
| WST | 3 | $336.32 | $350.79 | $1,052.37 | $43.41 | $314.23 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-872.29 | $0.00 | $134.95 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-05T15:41` no_trade skip_entry **CVS** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **TRV** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **NUE** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CSCO** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CNC** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **FFIV** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **HPQ** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **DVA** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` exit sell **UNH** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-05T15:40` exit sell **DVA** — trailing stop 10%
- `2026-08-04T20:10` system — eod_complete
- `2026-08-04T18:12` no_trade — no signals crossed action thresholds this hour
- `2026-08-04T18:12` no_trade skip_entry **WELL** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **VTRS** — insufficient investable cash (size $381, need >= $500)
- `2026-08-04T18:12` no_trade skip_entry **ALL** — insufficient investable cash (size $381, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
