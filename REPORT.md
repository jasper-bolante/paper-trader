# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 17:30 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,894.80** |
| Total return since inception | -0.53% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,686.39 |
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
| BAX | 28 | $27.27 | $26.70 | $747.60 | $-16.01 | $25.00 |
| BBY | 14 | $88.05 | $85.92 | $1,202.81 | $-29.94 | $79.24 |
| CSX | 17 | $50.29 | $50.36 | $856.12 | $1.17 | $46.01 |
| FTNT | 7 | $149.43 | $161.35 | $1,129.48 | $83.44 | $151.44 |
| HPQ | 31 | $28.20 | $30.24 | $937.44 | $63.20 | $28.19 |
| HUM | 2 | $398.00 | $386.55 | $773.09 | $-22.90 | $349.89 |
| MPC | 3 | $306.56 | $353.93 | $1,061.79 | $142.11 | $321.00 |
| NTAP | 5 | $161.48 | $206.25 | $1,031.28 | $223.90 | $184.50 |
| NUE | 2 | $269.82 | $270.30 | $540.60 | $0.96 | $245.24 |
| PANW | 2 | $388.28 | $384.80 | $769.60 | $-6.96 | $349.27 |
| PSX | 5 | $215.50 | $232.25 | $1,161.22 | $83.74 | $209.38 |
| SPY | 5 | $743.10 | $775.79 | $3,878.95 | $163.45 | — |
| STT | 8 | $185.86 | $190.81 | $1,526.48 | $39.61 | $171.10 |
| VLO | 3 | $304.72 | $340.99 | $1,022.96 | $108.80 | $308.51 |
| WST | 3 | $336.32 | $348.99 | $1,046.97 | $38.01 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T17:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T17:30` no_trade skip_entry **URI** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **TRV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **ALL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **GEN** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **FFIV** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **CNC** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T17:30` no_trade skip_entry **CRL** — insufficient investable cash (size $317, need >= $500)
- `2026-08-14T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T16:26` no_trade skip_entry **URI** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **TRV** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **ALL** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **CPAY** — insufficient investable cash (size $316, need >= $500)
- `2026-08-14T16:26` no_trade skip_entry **GEN** — insufficient investable cash (size $316, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
