# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-14 15:24 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,934.11** |
| Total return since inception | -0.33% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,935.54 (4.68%) |
| Positions value | $17,725.70 |
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
| BAX | 28 | $27.27 | $26.80 | $750.26 | $-13.35 | $25.00 |
| BBY | 14 | $88.05 | $86.60 | $1,212.40 | $-20.35 | $79.24 |
| CSX | 17 | $50.29 | $50.56 | $859.61 | $4.65 | $46.01 |
| FTNT | 7 | $149.43 | $161.32 | $1,129.24 | $83.20 | $151.44 |
| HPQ | 31 | $28.20 | $30.52 | $946.12 | $71.88 | $28.19 |
| HUM | 2 | $398.00 | $384.13 | $768.27 | $-27.72 | $349.89 |
| MPC | 3 | $306.56 | $358.12 | $1,074.36 | $154.68 | $321.00 |
| NTAP | 5 | $161.48 | $204.04 | $1,020.20 | $212.82 | $184.50 |
| NUE | 2 | $269.82 | $271.40 | $542.80 | $3.16 | $245.24 |
| PANW | 2 | $388.28 | $385.21 | $770.42 | $-6.14 | $349.27 |
| PSX | 5 | $215.50 | $234.38 | $1,171.88 | $94.39 | $209.38 |
| SPY | 5 | $743.10 | $776.04 | $3,880.20 | $164.70 | — |
| STT | 8 | $185.86 | $191.00 | $1,528.00 | $41.13 | $171.10 |
| VLO | 3 | $304.72 | $344.03 | $1,032.09 | $117.93 | $308.51 |
| WST | 3 | $336.32 | $346.62 | $1,039.86 | $30.90 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,017.26 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-14T15:24` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T15:24` no_trade skip_entry **URI** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **TRV** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **ALL** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **CPAY** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **GEN** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **FFIV** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **CNC** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T15:24` no_trade skip_entry **CRL** — insufficient investable cash (size $315, need >= $500)
- `2026-08-14T14:33` entry buy **PANW** — momentum entry: rank 1, mom 1.057, vol 50%
- `2026-08-14T14:33` no_trade skip_entry **URI** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **TRV** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **ALL** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **CPAY** — insufficient investable cash (size $314, need >= $500)
- `2026-08-14T14:33` no_trade skip_entry **GEN** — insufficient investable cash (size $314, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
