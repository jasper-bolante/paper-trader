# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 18:29 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,784.16** |
| Total return since inception | -1.08% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $18,527.54 |
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
| BAX | 28 | $27.27 | $27.20 | $761.60 | $-2.01 | $25.00 |
| BBY | 14 | $88.05 | $83.05 | $1,162.70 | $-70.05 | $79.24 |
| CSCO | 8 | $131.57 | $123.53 | $988.24 | $-64.35 | $110.34 |
| CSX | 17 | $50.29 | $50.03 | $850.59 | $-4.36 | $46.01 |
| DOC | 40 | $21.90 | $20.66 | $826.60 | $-49.47 | $18.97 |
| FTNT | 7 | $149.43 | $161.39 | $1,129.73 | $83.69 | $151.44 |
| HPQ | 31 | $28.20 | $28.80 | $892.96 | $18.72 | $27.04 |
| HUM | 2 | $398.00 | $385.42 | $770.83 | $-25.16 | $348.07 |
| MPC | 3 | $306.56 | $344.85 | $1,034.55 | $114.87 | $302.74 |
| NTAP | 5 | $161.48 | $201.99 | $1,009.93 | $202.55 | $178.85 |
| NUE | 2 | $269.82 | $270.51 | $541.03 | $1.39 | $242.71 |
| PSX | 5 | $215.50 | $226.31 | $1,131.53 | $54.05 | $201.92 |
| SPY | 5 | $743.10 | $773.11 | $3,865.55 | $150.05 | — |
| STT | 8 | $185.86 | $189.40 | $1,515.20 | $28.33 | $168.49 |
| VLO | 3 | $304.72 | $330.50 | $991.50 | $77.34 | $291.46 |
| WST | 3 | $336.32 | $351.67 | $1,055.01 | $46.05 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T18:29` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T18:29` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
