# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-11 16:27 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,649.62** |
| Total return since inception | -1.75% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,799.89 (4.00%) |
| Positions value | $17,853.36 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $759.75 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 3.82% |
| Annualized volatility | 13.07% | 14.44% |
| Sharpe (rf 4%) | -1.75 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 24 | 24 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.71 | $775.88 | $12.27 | $25.00 |
| BBY | 14 | $88.05 | $83.61 | $1,170.54 | $-62.21 | $79.24 |
| CSCO | 8 | $131.57 | $120.38 | $963.04 | $-89.55 | $110.34 |
| CSX | 17 | $50.29 | $49.81 | $846.77 | $-8.18 | $46.01 |
| DOC | 40 | $21.90 | $20.72 | $828.80 | $-47.27 | $18.97 |
| FTNT | 7 | $149.43 | $161.89 | $1,133.23 | $87.19 | $151.44 |
| HPQ | 31 | $28.20 | $29.09 | $901.94 | $27.70 | $27.04 |
| HUM | 2 | $398.00 | $376.75 | $753.50 | $-42.49 | $348.07 |
| MPC | 3 | $306.56 | $332.50 | $997.50 | $77.82 | $288.24 |
| NTAP | 5 | $161.48 | $197.71 | $988.55 | $181.17 | $178.85 |
| PSX | 5 | $215.50 | $222.34 | $1,111.72 | $34.24 | $193.81 |
| SPY | 5 | $743.10 | $771.74 | $3,858.70 | $143.20 | — |
| STT | 8 | $185.86 | $187.67 | $1,501.36 | $14.49 | $168.31 |
| VLO | 3 | $304.72 | $322.81 | $968.43 | $54.27 | $283.47 |
| WST | 3 | $336.32 | $351.13 | $1,053.39 | $44.43 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-11T16:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T16:27` no_trade skip_entry **TGT** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **URI** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **NUE** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **GEN** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **UAL** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **CNC** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **DAL** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **FFIV** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **TGT** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **URI** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **NUE** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **GEN** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **UAL** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T14:38` no_trade skip_entry **CNC** — insufficient investable cash (size $55, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
