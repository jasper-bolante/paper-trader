# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 19:40 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,800.52** |
| Total return since inception | -1.00% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,739.34 (3.70%) |
| Positions value | $18,543.90 |
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
| BAX | 28 | $27.27 | $27.21 | $762.02 | $-1.59 | $25.00 |
| BBY | 14 | $88.05 | $83.07 | $1,162.98 | $-69.77 | $79.24 |
| CSCO | 8 | $131.57 | $123.62 | $988.96 | $-63.63 | $110.34 |
| CSX | 17 | $50.29 | $50.21 | $853.57 | $-1.38 | $46.01 |
| DOC | 40 | $21.90 | $20.73 | $829.40 | $-46.67 | $18.97 |
| FTNT | 7 | $149.43 | $160.34 | $1,122.38 | $76.34 | $151.44 |
| HPQ | 31 | $28.20 | $29.27 | $907.37 | $33.13 | $27.04 |
| HUM | 2 | $398.00 | $387.32 | $774.64 | $-21.35 | $348.07 |
| MPC | 3 | $306.56 | $345.27 | $1,035.81 | $116.13 | $302.74 |
| NTAP | 5 | $161.48 | $201.71 | $1,008.55 | $201.17 | $178.85 |
| NUE | 2 | $269.82 | $271.89 | $543.78 | $4.14 | $242.71 |
| PSX | 5 | $215.50 | $225.14 | $1,125.70 | $48.22 | $201.92 |
| SPY | 5 | $743.10 | $772.73 | $3,863.65 | $148.15 | — |
| STT | 8 | $185.86 | $189.76 | $1,518.08 | $31.21 | $168.49 |
| VLO | 3 | $304.72 | $329.66 | $988.98 | $74.82 | $291.46 |
| WST | 3 | $336.32 | $352.68 | $1,058.03 | $49.07 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T19:40` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T19:40` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
