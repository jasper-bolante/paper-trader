# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 19:33 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,692.74** |
| Total return since inception | -1.54% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $18,652.63 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $3.60 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.50% | 3.86% |
| Annualized volatility | 11.65% | 14.76% |
| Sharpe (rf 4%) | -3.79 | 2.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 23 | 23 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.88 | $780.50 | $16.89 | $24.79 |
| BBY | 14 | $88.05 | $82.72 | $1,158.15 | $-74.60 | $79.24 |
| CSCO | 8 | $131.57 | $123.76 | $990.08 | $-62.51 | $109.28 |
| CSX | 17 | $50.29 | $50.12 | $852.04 | $-2.91 | $46.01 |
| DDOG | 3 | $268.94 | $259.15 | $777.45 | $-29.37 | $211.93 |
| DOC | 40 | $21.90 | $20.95 | $838.00 | $-38.07 | $18.97 |
| FTNT | 7 | $149.43 | $164.57 | $1,152.02 | $105.98 | $151.44 |
| HPQ | 31 | $28.20 | $30.18 | $935.43 | $61.19 | $27.04 |
| HUM | 2 | $398.00 | $385.01 | $770.02 | $-25.97 | $348.07 |
| MPC | 3 | $306.56 | $317.89 | $953.68 | $34.00 | $287.83 |
| NTAP | 5 | $161.48 | $201.06 | $1,005.30 | $197.92 | $172.38 |
| PSX | 5 | $215.50 | $215.05 | $1,075.25 | $-2.23 | $191.32 |
| SPY | 5 | $743.10 | $772.85 | $3,864.25 | $148.75 | — |
| STT | 8 | $185.86 | $186.69 | $1,493.52 | $6.65 | $168.31 |
| VLO | 3 | $304.72 | $314.60 | $943.80 | $29.64 | $283.28 |
| WST | 3 | $336.32 | $354.38 | $1,063.14 | $54.18 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-10T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T19:33` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T18:25` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T17:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T17:28` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T16:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T16:25` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T14:38` entry buy **DOC** — momentum entry: rank 11, mom 0.312, vol 21%
- `2026-08-10T14:38` entry buy **HUM** — momentum entry: rank 3, mom 0.695, vol 39%
- `2026-08-07T20:10` system — eod_complete
- `2026-08-07T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T19:33` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T18:25` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
