# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 20:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,312.84** |
| Total return since inception | -3.44% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $16,654.81 |
| Settled cash | $1,218.43 |
| Unsettled cash (T+1) | $1,446.40 |
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
| BAX | 28 | $27.27 | $27.54 | $771.12 | $7.51 | $24.79 |
| BBY | 14 | $88.05 | $81.95 | $1,147.30 | $-85.45 | $79.24 |
| CSCO | 8 | $131.57 | $121.42 | $971.40 | $-81.19 | $109.28 |
| CSX | 17 | $50.29 | $50.25 | $854.25 | $-0.70 | $46.01 |
| DDOG | 3 | $268.94 | $233.84 | $701.52 | $-105.30 | $211.93 |
| FTNT | 7 | $149.43 | $159.58 | $1,117.06 | $71.02 | $151.44 |
| HPQ | 31 | $28.20 | $30.05 | $931.40 | $57.16 | $27.04 |
| MPC | 3 | $306.56 | $298.02 | $894.07 | $-25.61 | $287.83 |
| NTAP | 5 | $161.48 | $189.60 | $948.00 | $140.62 | $172.38 |
| PSX | 5 | $215.50 | $203.91 | $1,019.52 | $-57.96 | $191.32 |
| SPY | 5 | $743.10 | $773.16 | $3,865.80 | $150.30 | — |
| STT | 8 | $185.86 | $184.70 | $1,477.60 | $-9.27 | $168.31 |
| VLO | 3 | $304.72 | $298.30 | $894.90 | $-19.26 | $283.28 |
| WST | 3 | $336.32 | $353.62 | $1,060.86 | $51.90 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-819.48 | $0.00 | $324.57 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-07T14:34` entry buy **CSCO** — momentum entry: rank 8, mom 0.353, vol 36%
- `2026-08-07T14:34` entry buy **BAX** — momentum entry: rank 4, mom 0.473, vol 50%
- `2026-08-07T14:34` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T14:34` exit sell **DOC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T00:25` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
