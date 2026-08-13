# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 19:37 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,952.32** |
| Total return since inception | -0.24% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $17,860.38 |
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
| BAX | 28 | $27.27 | $27.02 | $756.70 | $-6.91 | $25.00 |
| BBY | 14 | $88.05 | $85.56 | $1,197.84 | $-34.91 | $79.24 |
| CSCO | 8 | $131.57 | $112.94 | $903.48 | $-149.11 | $110.34 |
| CSX | 17 | $50.29 | $50.13 | $852.29 | $-2.66 | $46.01 |
| FTNT | 7 | $149.43 | $165.25 | $1,156.75 | $110.71 | $151.44 |
| HPQ | 31 | $28.20 | $30.93 | $958.68 | $84.44 | $27.04 |
| HUM | 2 | $398.00 | $383.31 | $766.62 | $-29.37 | $349.89 |
| MPC | 3 | $306.56 | $355.36 | $1,066.08 | $146.40 | $313.38 |
| NTAP | 5 | $161.48 | $205.87 | $1,029.35 | $221.97 | $181.81 |
| NUE | 2 | $269.82 | $272.48 | $544.96 | $5.32 | $244.43 |
| PSX | 5 | $215.50 | $231.04 | $1,155.20 | $77.72 | $202.98 |
| SPY | 5 | $743.10 | $777.78 | $3,888.90 | $173.40 | — |
| STT | 8 | $185.86 | $189.74 | $1,517.88 | $31.01 | $171.10 |
| VLO | 3 | $304.72 | $341.48 | $1,024.44 | $110.28 | $297.31 |
| WST | 3 | $336.32 | $347.07 | $1,041.21 | $32.25 | $318.26 |

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
