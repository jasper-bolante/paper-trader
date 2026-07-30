# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-30 17:06 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,442.60** |
| Total return since inception | -2.79% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,593.59 (-2.03%) |
| Positions value | $17,603.42 |
| Settled cash | $1,035.89 |
| Unsettled cash (T+1) | $809.45 |
| Tax reserve | $6.16 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.63% | -2.20% |
| Annualized volatility | 8.94% | 12.30% |
| Sharpe (rf 4%) | -7.35 | -3.31 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 16 | 16 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $88.43 | $1,238.02 | $5.27 | $79.24 |
| DDOG | 3 | $260.67 | $265.99 | $797.97 | $15.97 | $237.94 |
| DOC | 32 | $22.25 | $22.08 | $706.56 | $-5.46 | $20.55 |
| DVA | 6 | $227.39 | $240.09 | $1,440.54 | $76.18 | $216.78 |
| FTNT | 7 | $149.43 | $152.96 | $1,070.72 | $24.68 | $138.10 |
| HUM | 3 | $391.16 | $375.46 | $1,126.38 | $-47.09 | $329.83 |
| MPC | 3 | $306.56 | $314.06 | $942.18 | $22.50 | $287.83 |
| NTAP | 5 | $161.48 | $173.34 | $866.70 | $59.32 | $157.11 |
| PSX | 5 | $215.50 | $209.86 | $1,049.30 | $-28.18 | $191.32 |
| SPY | 5 | $743.10 | $740.00 | $3,700.00 | $-15.50 | — |
| STT | 8 | $185.86 | $181.26 | $1,450.08 | $-36.79 | $168.04 |
| UNH | 3 | $425.21 | $425.68 | $1,277.03 | $1.41 | $393.25 |
| VLO | 3 | $304.72 | $308.14 | $924.42 | $10.26 | $283.28 |
| WST | 3 | $336.32 | $337.84 | $1,013.52 | $4.56 | $302.61 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-30T17:06` no_trade — no signals crossed action thresholds this hour
- `2026-07-30T17:06` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-07-30T15:34` entry buy **BBY** — momentum entry: rank 12, mom 0.316, vol 29%
- `2026-07-30T15:34` entry buy **WST** — momentum entry: rank 10, mom 0.368, vol 30%
- `2026-07-30T15:34` no_trade skip_entry **CVS** — sector cap: Health Care would exceed 25% of equity
- `2026-07-30T15:34` exit sell **JBHT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-07-29T21:28` system — eod_complete
- `2026-07-29T19:54` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T19:54` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T18:33` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T18:33` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T16:52` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T16:52` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T15:32` entry buy **HUM** — momentum entry: rank 4, mom 0.701, vol 33%
- `2026-07-29T15:32` entry buy **FTNT** — momentum entry: rank 2, mom 1.006, vol 35%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
