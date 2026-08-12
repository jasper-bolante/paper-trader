# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 16:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,774.23** |
| Total return since inception | -1.13% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $18,517.61 |
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
| BAX | 28 | $27.27 | $27.03 | $756.84 | $-6.77 | $25.00 |
| BBY | 14 | $88.05 | $83.30 | $1,166.20 | $-66.55 | $79.24 |
| CSCO | 8 | $131.57 | $122.78 | $982.24 | $-70.35 | $110.34 |
| CSX | 17 | $50.29 | $50.05 | $850.85 | $-4.10 | $46.01 |
| DOC | 40 | $21.90 | $20.74 | $829.60 | $-46.47 | $18.97 |
| FTNT | 7 | $149.43 | $164.10 | $1,148.70 | $102.66 | $151.44 |
| HPQ | 31 | $28.20 | $28.82 | $893.26 | $19.02 | $27.04 |
| HUM | 2 | $398.00 | $385.13 | $770.26 | $-25.73 | $348.07 |
| MPC | 3 | $306.56 | $342.49 | $1,027.47 | $107.79 | $302.74 |
| NTAP | 5 | $161.48 | $200.92 | $1,004.60 | $197.22 | $178.85 |
| NUE | 2 | $269.82 | $270.82 | $541.64 | $2.00 | $242.71 |
| PSX | 5 | $215.50 | $224.85 | $1,124.27 | $46.79 | $201.92 |
| SPY | 5 | $743.10 | $772.48 | $3,862.38 | $146.88 | — |
| STT | 8 | $185.86 | $189.62 | $1,516.96 | $30.09 | $168.49 |
| VLO | 3 | $304.72 | $328.09 | $984.27 | $70.11 | $291.46 |
| WST | 3 | $336.32 | $352.69 | $1,058.07 | $49.11 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T16:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T16:28` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
