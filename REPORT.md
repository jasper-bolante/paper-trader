# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 16:25 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,630.90** |
| Total return since inception | -1.85% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $18,590.79 |
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
| BAX | 28 | $27.27 | $27.84 | $779.52 | $15.91 | $24.79 |
| BBY | 14 | $88.05 | $82.47 | $1,154.51 | $-78.24 | $79.24 |
| CSCO | 8 | $131.57 | $123.67 | $989.36 | $-63.23 | $109.28 |
| CSX | 17 | $50.29 | $50.28 | $854.76 | $-0.19 | $46.01 |
| DDOG | 3 | $268.94 | $254.95 | $764.85 | $-41.97 | $211.93 |
| DOC | 40 | $21.90 | $21.02 | $840.80 | $-35.27 | $18.97 |
| FTNT | 7 | $149.43 | $163.90 | $1,147.30 | $101.26 | $151.44 |
| HPQ | 31 | $28.20 | $30.14 | $934.34 | $60.10 | $27.04 |
| HUM | 2 | $398.00 | $385.45 | $770.90 | $-25.09 | $348.07 |
| MPC | 3 | $306.56 | $312.82 | $938.47 | $18.79 | $287.83 |
| NTAP | 5 | $161.48 | $200.43 | $1,002.15 | $194.77 | $172.38 |
| PSX | 5 | $215.50 | $212.19 | $1,060.95 | $-16.53 | $191.32 |
| SPY | 5 | $743.10 | $773.71 | $3,868.55 | $153.05 | — |
| STT | 8 | $185.86 | $185.39 | $1,483.12 | $-3.75 | $168.31 |
| VLO | 3 | $304.72 | $311.69 | $935.07 | $20.91 | $283.28 |
| WST | 3 | $336.32 | $355.38 | $1,066.14 | $57.18 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-10T16:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T16:25` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T14:38` entry buy **DOC** — momentum entry: rank 11, mom 0.312, vol 21%
- `2026-08-10T14:38` entry buy **HUM** — momentum entry: rank 3, mom 0.695, vol 39%
- `2026-08-07T20:10` system — eod_complete
- `2026-08-07T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T19:33` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T18:25` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T17:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T17:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T16:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T15:29` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T15:29` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
