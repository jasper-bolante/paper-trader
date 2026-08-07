# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 19:33 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,325.22** |
| Total return since inception | -3.37% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,673.66 (3.37%) |
| Positions value | $16,667.19 |
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
| BAX | 28 | $27.27 | $27.84 | $779.66 | $16.05 | $24.54 |
| BBY | 14 | $88.05 | $81.84 | $1,145.76 | $-86.99 | $79.24 |
| CSCO | 8 | $131.57 | $121.22 | $969.76 | $-82.83 | $108.28 |
| CSX | 17 | $50.29 | $50.41 | $856.97 | $2.02 | $46.01 |
| DDOG | 3 | $268.94 | $237.84 | $713.52 | $-93.30 | $211.93 |
| FTNT | 7 | $149.43 | $158.97 | $1,112.79 | $66.75 | $151.44 |
| HPQ | 31 | $28.20 | $29.91 | $927.06 | $52.82 | $25.38 |
| MPC | 3 | $306.56 | $296.46 | $889.38 | $-30.30 | $287.83 |
| NTAP | 5 | $161.48 | $190.13 | $950.67 | $143.29 | $172.38 |
| PSX | 5 | $215.50 | $203.41 | $1,017.07 | $-60.41 | $191.32 |
| SPY | 5 | $743.10 | $772.83 | $3,864.15 | $148.65 | — |
| STT | 8 | $185.86 | $185.20 | $1,481.60 | $-5.27 | $168.31 |
| VLO | 3 | $304.72 | $297.14 | $891.42 | $-22.74 | $283.28 |
| WST | 3 | $336.32 | $355.79 | $1,067.37 | $58.41 | $316.04 |

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
