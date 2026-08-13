# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 16:27 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,854.79** |
| Total return since inception | -0.73% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $17,762.85 |
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
| BAX | 28 | $27.27 | $26.89 | $753.06 | $-10.55 | $25.00 |
| BBY | 14 | $88.05 | $85.56 | $1,197.84 | $-34.91 | $79.24 |
| CSCO | 8 | $131.57 | $112.35 | $898.80 | $-153.79 | $110.34 |
| CSX | 17 | $50.29 | $50.42 | $857.14 | $2.19 | $46.01 |
| FTNT | 7 | $149.43 | $163.19 | $1,142.33 | $96.29 | $151.44 |
| HPQ | 31 | $28.20 | $30.12 | $933.88 | $59.63 | $27.04 |
| HUM | 2 | $398.00 | $384.20 | $768.40 | $-27.59 | $349.89 |
| MPC | 3 | $306.56 | $350.88 | $1,052.64 | $132.96 | $313.38 |
| NTAP | 5 | $161.48 | $204.02 | $1,020.10 | $212.72 | $181.81 |
| NUE | 2 | $269.82 | $273.14 | $546.28 | $6.64 | $244.43 |
| PSX | 5 | $215.50 | $228.56 | $1,142.80 | $65.32 | $202.98 |
| SPY | 5 | $743.10 | $776.43 | $3,882.17 | $166.67 | — |
| STT | 8 | $185.86 | $189.67 | $1,517.36 | $30.49 | $171.10 |
| VLO | 3 | $304.72 | $335.17 | $1,005.51 | $91.35 | $297.31 |
| WST | 3 | $336.32 | $348.18 | $1,044.54 | $35.58 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-857.70 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-13T16:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T16:27` no_trade skip_entry **EXPE** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **CPAY** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **GEN** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **XYZ** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **CRL** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **FFIV** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **URI** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T16:27` no_trade skip_entry **CNC** — insufficient investable cash (size $261, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **EXPE** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **CPAY** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **GEN** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **XYZ** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **CRL** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **FFIV** — insufficient investable cash (size $259, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
