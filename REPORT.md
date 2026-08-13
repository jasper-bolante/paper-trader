# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 18:30 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,918.43** |
| Total return since inception | -0.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $17,826.49 |
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
| BAX | 28 | $27.27 | $27.07 | $758.10 | $-5.51 | $25.00 |
| BBY | 14 | $88.05 | $85.36 | $1,195.04 | $-37.71 | $79.24 |
| CSCO | 8 | $131.57 | $112.04 | $896.32 | $-156.27 | $110.34 |
| CSX | 17 | $50.29 | $50.51 | $858.67 | $3.72 | $46.01 |
| FTNT | 7 | $149.43 | $164.35 | $1,150.45 | $104.41 | $151.44 |
| HPQ | 31 | $28.20 | $30.36 | $941.31 | $67.07 | $27.04 |
| HUM | 2 | $398.00 | $384.34 | $768.68 | $-27.31 | $349.89 |
| MPC | 3 | $306.56 | $354.13 | $1,062.40 | $142.73 | $313.38 |
| NTAP | 5 | $161.48 | $204.64 | $1,023.20 | $215.82 | $181.81 |
| NUE | 2 | $269.82 | $273.29 | $546.58 | $6.94 | $244.43 |
| PSX | 5 | $215.50 | $230.88 | $1,154.40 | $76.92 | $202.98 |
| SPY | 5 | $743.10 | $777.15 | $3,885.77 | $170.27 | — |
| STT | 8 | $185.86 | $190.33 | $1,522.64 | $35.77 | $171.10 |
| VLO | 3 | $304.72 | $339.92 | $1,019.76 | $105.60 | $297.31 |
| WST | 3 | $336.32 | $347.72 | $1,043.16 | $34.20 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-857.70 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-13T18:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T18:30` no_trade skip_entry **EXPE** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **GEN** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **XYZ** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **CRL** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **FFIV** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **URI** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T18:30` no_trade skip_entry **CNC** — insufficient investable cash (size $258, need >= $500)
- `2026-08-13T17:32` no_trade — no signals crossed action thresholds this hour
- `2026-08-13T17:32` no_trade skip_entry **EXPE** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **CPAY** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **GEN** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **XYZ** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T17:32` no_trade skip_entry **CRL** — insufficient investable cash (size $259, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
