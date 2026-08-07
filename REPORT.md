# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 17:26 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,347.81** |
| Total return since inception | -3.26% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,673.66 (3.37%) |
| Positions value | $16,689.78 |
| Settled cash | $1,218.43 |
| Unsettled cash (T+1) | $1,446.40 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -4.22% | 3.19% |
| Annualized volatility | 11.48% | 15.02% |
| Sharpe (rf 4%) | -4.79 | 2.31 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 22 | 22 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.57 | $772.10 | $8.49 | $24.54 |
| BBY | 14 | $88.05 | $81.81 | $1,145.27 | $-87.48 | $79.24 |
| CSCO | 8 | $131.57 | $121.36 | $970.84 | $-81.75 | $108.28 |
| CSX | 17 | $50.29 | $50.83 | $864.03 | $9.08 | $46.01 |
| DDOG | 3 | $268.94 | $236.14 | $708.42 | $-98.40 | $211.93 |
| FTNT | 7 | $149.43 | $159.41 | $1,115.87 | $69.83 | $151.44 |
| HPQ | 31 | $28.20 | $29.67 | $919.77 | $45.53 | $25.38 |
| MPC | 3 | $306.56 | $300.71 | $902.13 | $-17.55 | $287.83 |
| NTAP | 5 | $161.48 | $190.56 | $952.80 | $145.42 | $172.38 |
| PSX | 5 | $215.50 | $205.79 | $1,028.95 | $-48.53 | $191.32 |
| SPY | 5 | $743.10 | $771.97 | $3,859.85 | $144.35 | — |
| STT | 8 | $185.86 | $185.61 | $1,484.88 | $-1.99 | $168.31 |
| VLO | 3 | $304.72 | $300.45 | $901.35 | $-12.81 | $283.28 |
| WST | 3 | $336.32 | $354.51 | $1,063.53 | $54.57 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-819.48 | $0.00 | $324.57 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-06T16:00` entry buy **HPQ** — momentum entry: rank 5, mom 0.453, vol 44%
- `2026-08-06T16:00` entry buy **DDOG** — momentum entry: rank 1, mom 0.960, vol 46%
- `2026-08-06T15:59` exit sell **DDOG** — trailing stop 10%
- `2026-08-05T20:10` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
