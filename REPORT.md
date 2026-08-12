# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 14:38 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,707.38** |
| Total return since inception | -1.46% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $18,450.76 |
| Settled cash | $1,259.82 |
| Unsettled cash (T+1) | $3.60 |
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
| BAX | 28 | $27.27 | $26.64 | $746.06 | $-17.55 | $25.00 |
| BBY | 14 | $88.05 | $82.73 | $1,158.22 | $-74.53 | $79.24 |
| CSCO | 8 | $131.57 | $123.78 | $990.28 | $-62.31 | $110.34 |
| CSX | 17 | $50.29 | $49.81 | $846.86 | $-8.10 | $46.01 |
| DOC | 40 | $21.90 | $20.67 | $826.80 | $-49.27 | $18.97 |
| FTNT | 7 | $149.43 | $165.00 | $1,155.00 | $108.96 | $151.44 |
| HPQ | 31 | $28.20 | $28.37 | $879.47 | $5.23 | $27.04 |
| HUM | 2 | $398.00 | $379.46 | $758.92 | $-37.07 | $348.07 |
| MPC | 3 | $306.56 | $340.60 | $1,021.80 | $102.12 | $302.74 |
| NTAP | 5 | $161.48 | $200.10 | $1,000.50 | $193.12 | $178.85 |
| NUE | 2 | $269.82 | $269.68 | $539.36 | $-0.28 | $242.71 |
| PSX | 5 | $215.50 | $224.34 | $1,121.72 | $44.24 | $201.92 |
| SPY | 5 | $743.10 | $772.77 | $3,863.85 | $148.35 | — |
| STT | 8 | $185.86 | $189.37 | $1,514.92 | $28.05 | $168.49 |
| VLO | 3 | $304.72 | $325.59 | $976.77 | $62.61 | $291.46 |
| WST | 3 | $336.32 | $350.07 | $1,050.22 | $41.26 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T14:38` entry buy **NUE** — momentum entry: rank 9, mom 0.364, vol 34%
- `2026-08-11T21:24` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
