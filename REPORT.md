# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 16:26 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,916.62** |
| Total return since inception | -0.42% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,708.21 |
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
| BAX | 28 | $27.27 | $26.82 | $750.82 | $-12.79 | $25.00 |
| BBY | 14 | $88.05 | $86.33 | $1,208.62 | $-24.13 | $79.24 |
| CSX | 17 | $50.29 | $50.48 | $858.16 | $3.21 | $46.01 |
| FTNT | 7 | $149.43 | $161.76 | $1,132.32 | $86.28 | $151.44 |
| HPQ | 31 | $28.20 | $30.29 | $938.99 | $64.75 | $28.19 |
| HUM | 2 | $398.00 | $386.64 | $773.28 | $-22.71 | $349.89 |
| MPC | 3 | $306.56 | $354.36 | $1,063.08 | $143.40 | $321.00 |
| NTAP | 5 | $161.48 | $205.43 | $1,027.12 | $219.75 | $184.50 |
| NUE | 2 | $269.82 | $270.00 | $540.00 | $0.36 | $245.24 |
| PANW | 2 | $388.28 | $386.25 | $772.50 | $-4.06 | $349.27 |
| PSX | 5 | $215.50 | $232.91 | $1,164.55 | $87.07 | $209.38 |
| SPY | 5 | $743.10 | $776.71 | $3,883.53 | $168.03 | — |
| STT | 8 | $185.86 | $190.97 | $1,527.76 | $40.89 | $171.10 |
| VLO | 3 | $304.72 | $341.48 | $1,024.44 | $110.28 | $308.51 |
| WST | 3 | $336.32 | $347.68 | $1,043.04 | $34.08 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T16:26` no_trade skip_entry **URI** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **TRV** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **ALL** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **CPAY** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **GEN** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **FFIV** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **CNC** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **CRL** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T15:24` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T15:24` no_trade skip_entry **URI** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **TRV** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **ALL** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **CPAY** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **GEN** — insufficient investable cash (size $315, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
