# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-11 19:38 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,661.93** |
| Total return since inception | -1.69% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,799.89 (4.00%) |
| Positions value | $17,865.67 |
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
| BBY | 14 | $88.05 | $83.83 | $1,173.62 | $-59.13 | $79.24 |
| CSCO | 8 | $131.57 | $120.89 | $967.12 | $-85.47 | $110.34 |
| CSX | 17 | $50.29 | $50.12 | $851.96 | $-3.00 | $46.01 |
| DOC | 40 | $21.90 | $20.57 | $823.00 | $-53.07 | $18.97 |
| FTNT | 7 | $149.43 | $161.72 | $1,132.04 | $86.00 | $151.44 |
| HPQ | 31 | $28.20 | $29.05 | $900.55 | $26.31 | $27.04 |
| HUM | 2 | $398.00 | $374.90 | $749.80 | $-46.19 | $348.07 |
| MPC | 3 | $306.56 | $333.77 | $1,001.31 | $81.63 | $288.24 |
| NTAP | 5 | $161.48 | $198.52 | $992.60 | $185.22 | $178.85 |
| PSX | 5 | $215.50 | $223.89 | $1,119.45 | $41.97 | $193.81 |
| SPY | 5 | $743.10 | $771.00 | $3,855.00 | $139.50 | — |
| STT | 8 | $185.86 | $187.10 | $1,496.80 | $9.93 | $168.31 |
| VLO | 3 | $304.72 | $322.88 | $968.62 | $54.47 | $283.47 |
| WST | 3 | $336.32 | $352.64 | $1,057.92 | $48.96 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-11T19:38` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T19:38` no_trade skip_entry **TGT** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **URI** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **NUE** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **GEN** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **UAL** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **CNC** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **DAL** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T19:38` no_trade skip_entry **FFIV** — insufficient investable cash (size $53, need >= $500)
- `2026-08-11T18:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T18:28` no_trade skip_entry **TGT** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **URI** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **NUE** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **GEN** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **UAL** — insufficient investable cash (size $55, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
