# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 18:27 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,903.44** |
| Total return since inception | -0.48% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,695.03 |
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
| BAX | 28 | $27.27 | $26.68 | $746.90 | $-16.71 | $25.00 |
| BBY | 14 | $88.05 | $86.42 | $1,209.95 | $-22.80 | $79.24 |
| CSX | 17 | $50.29 | $50.32 | $855.44 | $0.49 | $46.01 |
| FTNT | 7 | $149.43 | $161.57 | $1,130.99 | $84.95 | $151.44 |
| HPQ | 31 | $28.20 | $30.04 | $931.24 | $57.00 | $28.19 |
| HUM | 2 | $398.00 | $387.98 | $775.96 | $-20.03 | $349.89 |
| MPC | 3 | $306.56 | $353.77 | $1,061.31 | $141.63 | $321.00 |
| NTAP | 5 | $161.48 | $207.37 | $1,036.83 | $229.45 | $184.50 |
| NUE | 2 | $269.82 | $270.38 | $540.76 | $1.12 | $245.24 |
| PANW | 2 | $388.28 | $385.05 | $770.10 | $-6.46 | $349.27 |
| PSX | 5 | $215.50 | $231.62 | $1,158.10 | $80.62 | $209.38 |
| SPY | 5 | $743.10 | $776.09 | $3,880.45 | $164.95 | — |
| STT | 8 | $185.86 | $191.25 | $1,530.00 | $43.13 | $171.10 |
| VLO | 3 | $304.72 | $340.65 | $1,021.95 | $107.79 | $308.51 |
| WST | 3 | $336.32 | $348.35 | $1,045.05 | $36.09 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T18:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T18:27` no_trade skip_entry **URI** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **TRV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **ALL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **CPAY** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **GEN** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **FFIV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **CNC** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **CRL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T17:30` no_trade skip_entry **URI** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **TRV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **ALL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **GEN** — insufficient investable cash (size $317, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
