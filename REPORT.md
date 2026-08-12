# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 17:32 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,747.63** |
| Total return since inception | -1.26% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $18,491.01 |
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
| BAX | 28 | $27.27 | $27.10 | $758.80 | $-4.81 | $25.00 |
| BBY | 14 | $88.05 | $83.14 | $1,163.96 | $-68.79 | $79.24 |
| CSCO | 8 | $131.57 | $122.88 | $983.00 | $-69.59 | $110.34 |
| CSX | 17 | $50.29 | $50.01 | $850.09 | $-4.87 | $46.01 |
| DOC | 40 | $21.90 | $20.73 | $829.20 | $-46.87 | $18.97 |
| FTNT | 7 | $149.43 | $161.45 | $1,130.15 | $84.11 | $151.44 |
| HPQ | 31 | $28.20 | $28.79 | $892.49 | $18.25 | $27.04 |
| HUM | 2 | $398.00 | $385.09 | $770.18 | $-25.81 | $348.07 |
| MPC | 3 | $306.56 | $342.04 | $1,026.12 | $106.44 | $302.74 |
| NTAP | 5 | $161.48 | $201.15 | $1,005.73 | $198.35 | $178.85 |
| NUE | 2 | $269.82 | $270.54 | $541.08 | $1.44 | $242.71 |
| PSX | 5 | $215.50 | $224.80 | $1,124.00 | $46.52 | $201.92 |
| SPY | 5 | $743.10 | $772.88 | $3,864.43 | $148.93 | — |
| STT | 8 | $185.86 | $188.97 | $1,511.80 | $24.93 | $168.49 |
| VLO | 3 | $304.72 | $328.27 | $984.81 | $70.65 | $291.46 |
| WST | 3 | $336.32 | $351.73 | $1,055.19 | $46.23 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T17:32` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T17:32` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
