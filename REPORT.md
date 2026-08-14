# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 19:30 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,873.58** |
| Total return since inception | -0.63% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,665.17 |
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
| BAX | 28 | $27.27 | $26.82 | $751.10 | $-12.51 | $25.00 |
| BBY | 14 | $88.05 | $86.05 | $1,204.70 | $-28.05 | $79.24 |
| CSX | 17 | $50.29 | $50.17 | $852.89 | $-2.06 | $46.01 |
| FTNT | 7 | $149.43 | $160.37 | $1,122.59 | $76.55 | $151.44 |
| HPQ | 31 | $28.20 | $30.02 | $930.77 | $56.53 | $28.19 |
| HUM | 2 | $398.00 | $387.67 | $775.34 | $-20.65 | $349.89 |
| MPC | 3 | $306.56 | $354.07 | $1,062.21 | $142.53 | $321.00 |
| NTAP | 5 | $161.48 | $204.90 | $1,024.50 | $217.12 | $184.50 |
| NUE | 2 | $269.82 | $268.33 | $536.66 | $-2.98 | $245.24 |
| PANW | 2 | $388.28 | $381.85 | $763.70 | $-12.86 | $349.27 |
| PSX | 5 | $215.50 | $231.86 | $1,159.30 | $81.82 | $209.38 |
| SPY | 5 | $743.10 | $776.17 | $3,880.85 | $165.35 | — |
| STT | 8 | $185.86 | $191.61 | $1,532.88 | $46.01 | $171.10 |
| VLO | 3 | $304.72 | $340.36 | $1,021.07 | $106.91 | $308.51 |
| WST | 3 | $336.32 | $348.87 | $1,046.61 | $37.65 | $318.26 |

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
