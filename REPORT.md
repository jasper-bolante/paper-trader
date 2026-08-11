# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-11 21:24 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,648.57** |
| Total return since inception | -1.76% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $17,852.31 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $759.75 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.82% | 3.51% |
| Annualized volatility | 12.78% | 14.20% |
| Sharpe (rf 4%) | -1.76 | 2.34 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 25 | 25 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.61 | $772.94 | $9.33 | $25.00 |
| BBY | 14 | $88.05 | $83.27 | $1,165.78 | $-66.97 | $79.24 |
| CSCO | 8 | $131.57 | $120.44 | $963.52 | $-89.07 | $110.34 |
| CSX | 17 | $50.29 | $49.96 | $849.32 | $-5.63 | $46.01 |
| DOC | 40 | $21.90 | $20.50 | $820.00 | $-56.07 | $18.97 |
| FTNT | 7 | $149.43 | $161.91 | $1,133.37 | $87.33 | $151.44 |
| HPQ | 31 | $28.20 | $29.07 | $901.01 | $26.77 | $27.04 |
| HUM | 2 | $398.00 | $372.82 | $745.65 | $-50.34 | $348.07 |
| MPC | 3 | $306.56 | $336.38 | $1,009.12 | $89.45 | $302.74 |
| NTAP | 5 | $161.48 | $198.50 | $992.50 | $185.12 | $178.85 |
| PSX | 5 | $215.50 | $224.36 | $1,121.80 | $44.32 | $201.92 |
| SPY | 5 | $743.10 | $770.57 | $3,852.85 | $137.35 | — |
| STT | 8 | $185.86 | $187.21 | $1,497.68 | $10.81 | $168.49 |
| VLO | 3 | $304.72 | $323.85 | $971.54 | $57.38 | $291.46 |
| WST | 3 | $336.32 | $351.74 | $1,055.22 | $46.26 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-11T21:24` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
