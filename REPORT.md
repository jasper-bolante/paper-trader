# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 14:33 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,955.53** |
| Total return since inception | -0.22% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,747.12 |
| Settled cash | $1,318.75 |
| Unsettled cash (T+1) | $896.63 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.16% | 4.49% |
| Annualized volatility | 12.93% | 13.73% |
| Sharpe (rf 4%) | -0.36 | 2.88 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 27 | 27 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.84 | $751.52 | $-12.09 | $25.00 |
| BBY | 14 | $88.05 | $86.92 | $1,216.88 | $-15.87 | $79.24 |
| CSX | 17 | $50.29 | $50.70 | $861.90 | $6.95 | $46.01 |
| FTNT | 7 | $149.43 | $161.17 | $1,128.19 | $82.15 | $151.44 |
| HPQ | 31 | $28.20 | $30.64 | $949.84 | $75.60 | $28.19 |
| HUM | 2 | $398.00 | $383.61 | $767.22 | $-28.77 | $349.89 |
| MPC | 3 | $306.56 | $359.27 | $1,077.82 | $158.14 | $321.00 |
| NTAP | 5 | $161.48 | $203.56 | $1,017.78 | $210.40 | $184.50 |
| NUE | 2 | $269.82 | $272.74 | $545.48 | $5.84 | $245.24 |
| PANW | 2 | $388.28 | $388.08 | $776.16 | $-0.40 | $349.27 |
| PSX | 5 | $215.50 | $234.07 | $1,170.35 | $92.87 | $209.38 |
| SPY | 5 | $743.10 | $777.05 | $3,885.27 | $169.77 | — |
| STT | 8 | $185.86 | $190.35 | $1,522.80 | $35.93 | $171.10 |
| VLO | 3 | $304.72 | $345.20 | $1,035.60 | $121.44 | $308.51 |
| WST | 3 | $336.32 | $346.77 | $1,040.31 | $31.35 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T14:33` entry buy **PANW** — momentum entry: rank 1, mom 1.057, vol 50%
- `2026-08-14T14:33` no_trade skip_entry **URI** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **TRV** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **ALL** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **CPAY** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **GEN** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **FFIV** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **CNC** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **CRL** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` exit sell **CSCO** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-13T21:24` system — eod_complete
- `2026-08-13T19:37` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T19:37` no_trade skip_entry **EXPE** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **CPAY** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **GEN** — insufficient investable cash (size $256, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
