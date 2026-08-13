# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 17:32 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,889.44** |
| Total return since inception | -0.55% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $17,797.51 |
| Settled cash | $1,260.94 |
| Unsettled cash (T+1) | $837.97 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.21% | 3.77% |
| Annualized volatility | 12.71% | 13.90% |
| Sharpe (rf 4%) | -1.22 | 2.47 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 26 | 26 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.95 | $754.60 | $-9.01 | $25.00 |
| BBY | 14 | $88.05 | $85.44 | $1,196.09 | $-36.66 | $79.24 |
| CSCO | 8 | $131.57 | $112.80 | $902.36 | $-150.23 | $110.34 |
| CSX | 17 | $50.29 | $50.54 | $859.18 | $4.23 | $46.01 |
| FTNT | 7 | $149.43 | $163.41 | $1,143.87 | $97.83 | $151.44 |
| HPQ | 31 | $28.20 | $30.30 | $939.15 | $64.91 | $27.04 |
| HUM | 2 | $398.00 | $384.46 | $768.92 | $-27.07 | $349.89 |
| MPC | 3 | $306.56 | $351.89 | $1,055.67 | $135.99 | $313.38 |
| NTAP | 5 | $161.48 | $204.69 | $1,023.47 | $216.09 | $181.81 |
| NUE | 2 | $269.82 | $272.63 | $545.27 | $5.63 | $244.43 |
| PSX | 5 | $215.50 | $229.73 | $1,148.65 | $71.17 | $202.98 |
| SPY | 5 | $743.10 | $777.09 | $3,885.43 | $169.93 | — |
| STT | 8 | $185.86 | $189.88 | $1,519.04 | $32.17 | $171.10 |
| VLO | 3 | $304.72 | $337.50 | $1,012.50 | $98.34 | $297.31 |
| WST | 3 | $336.32 | $347.77 | $1,043.31 | $34.35 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-857.70 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-13T17:32` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T17:32` no_trade skip_entry **EXPE** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **CPAY** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **GEN** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **XYZ** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **CRL** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **FFIV** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **URI** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **CNC** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T16:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T16:27` no_trade skip_entry **EXPE** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **CPAY** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **GEN** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **XYZ** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **CRL** — insufficient investable cash (size $261, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
