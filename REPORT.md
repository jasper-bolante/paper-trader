# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 20:04 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,913.49** |
| Total return since inception | -0.43% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,705.08 |
| Settled cash | $1,318.75 |
| Unsettled cash (T+1) | $896.63 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.50% | 4.25% |
| Annualized volatility | 12.72% | 13.52% |
| Sharpe (rf 4%) | -0.62 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 28 | 28 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.73 | $748.44 | $-15.17 | $25.00 |
| BBY | 14 | $88.05 | $86.44 | $1,210.09 | $-22.66 | $79.24 |
| CSX | 17 | $50.29 | $50.17 | $852.89 | $-2.06 | $46.01 |
| FTNT | 7 | $149.43 | $159.97 | $1,119.79 | $73.75 | $151.44 |
| HPQ | 31 | $28.20 | $30.10 | $933.10 | $58.86 | $28.19 |
| HUM | 2 | $398.00 | $389.25 | $778.50 | $-17.49 | $350.32 |
| MPC | 3 | $306.56 | $355.48 | $1,066.44 | $146.76 | $321.00 |
| NTAP | 5 | $161.48 | $207.10 | $1,035.52 | $228.14 | $186.39 |
| NUE | 2 | $269.82 | $268.55 | $537.10 | $-2.54 | $245.24 |
| PANW | 2 | $388.28 | $384.24 | $768.48 | $-8.08 | $349.27 |
| PSX | 5 | $215.50 | $233.62 | $1,168.08 | $90.60 | $210.25 |
| SPY | 5 | $743.10 | $776.03 | $3,880.15 | $164.65 | — |
| STT | 8 | $185.86 | $191.80 | $1,534.40 | $47.53 | $172.62 |
| VLO | 3 | $304.72 | $341.55 | $1,024.65 | $110.49 | $308.51 |
| WST | 3 | $336.32 | $349.15 | $1,047.45 | $38.49 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T19:30` no_trade skip_entry **URI** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **TRV** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **ALL** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **GEN** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **FFIV** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CNC** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CRL** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T18:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T18:27` no_trade skip_entry **URI** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **TRV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **ALL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **CPAY** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T18:27` no_trade skip_entry **GEN** — insufficient investable cash (size $317, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
