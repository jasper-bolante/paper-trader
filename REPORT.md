# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 18:25 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,317.41** |
| Total return since inception | -3.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,673.66 (3.37%) |
| Positions value | $16,659.38 |
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
| BAX | 28 | $27.27 | $27.58 | $772.24 | $8.63 | $24.54 |
| BBY | 14 | $88.05 | $81.71 | $1,143.94 | $-88.81 | $79.24 |
| CSCO | 8 | $131.57 | $120.66 | $965.28 | $-87.31 | $108.28 |
| CSX | 17 | $50.29 | $50.52 | $858.84 | $3.89 | $46.01 |
| DDOG | 3 | $268.94 | $235.78 | $707.33 | $-99.50 | $211.93 |
| FTNT | 7 | $149.43 | $159.03 | $1,113.21 | $67.17 | $151.44 |
| HPQ | 31 | $28.20 | $29.75 | $922.25 | $48.01 | $25.38 |
| MPC | 3 | $306.56 | $299.29 | $897.87 | $-21.81 | $287.83 |
| NTAP | 5 | $161.48 | $190.26 | $951.30 | $143.92 | $172.38 |
| PSX | 5 | $215.50 | $204.58 | $1,022.90 | $-54.58 | $191.32 |
| SPY | 5 | $743.10 | $771.61 | $3,858.05 | $142.55 | — |
| STT | 8 | $185.86 | $185.45 | $1,483.60 | $-3.27 | $168.31 |
| VLO | 3 | $304.72 | $299.31 | $897.93 | $-16.23 | $283.28 |
| WST | 3 | $336.32 | $354.88 | $1,064.64 | $55.68 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-819.48 | $0.00 | $324.57 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-06T16:00` entry buy **HPQ** — momentum entry: rank 5, mom 0.453, vol 44%
- `2026-08-06T16:00` entry buy **DDOG** — momentum entry: rank 1, mom 0.960, vol 46%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
