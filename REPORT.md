# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 21:24 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,982.23** |
| Total return since inception | -0.09% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,890.29 |
| Settled cash | $1,260.94 |
| Unsettled cash (T+1) | $837.97 |
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
| BAX | 28 | $27.27 | $27.05 | $757.40 | $-6.21 | $25.00 |
| BBY | 14 | $88.05 | $85.37 | $1,195.18 | $-37.57 | $79.24 |
| CSCO | 8 | $131.57 | $113.48 | $907.88 | $-144.71 | $110.34 |
| CSX | 17 | $50.29 | $50.13 | $852.21 | $-2.74 | $46.01 |
| FTNT | 7 | $149.43 | $165.47 | $1,158.29 | $112.25 | $151.44 |
| HPQ | 31 | $28.20 | $31.32 | $970.92 | $96.68 | $28.19 |
| HUM | 2 | $398.00 | $384.81 | $769.62 | $-26.37 | $349.89 |
| MPC | 3 | $306.56 | $356.67 | $1,070.01 | $150.33 | $321.00 |
| NTAP | 5 | $161.48 | $205.00 | $1,025.00 | $217.62 | $184.50 |
| NUE | 2 | $269.82 | $272.49 | $544.98 | $5.34 | $245.24 |
| PSX | 5 | $215.50 | $232.64 | $1,163.20 | $85.72 | $209.38 |
| SPY | 5 | $743.10 | $777.86 | $3,889.30 | $173.80 | — |
| STT | 8 | $185.86 | $189.89 | $1,519.12 | $32.25 | $171.10 |
| VLO | 3 | $304.72 | $342.79 | $1,028.37 | $114.21 | $308.51 |
| WST | 3 | $336.32 | $346.27 | $1,038.81 | $29.85 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-857.70 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-13T19:37` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T19:37` no_trade skip_entry **EXPE** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **CPAY** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **GEN** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **XYZ** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **CRL** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **FFIV** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **URI** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T19:37` no_trade skip_entry **CNC** — insufficient investable cash (size $256, need >= $500)
- `2026-08-13T18:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T18:30` no_trade skip_entry **EXPE** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **GEN** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **XYZ** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **CRL** — insufficient investable cash (size $258, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
