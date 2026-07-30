# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-30 15:34 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,367.43** |
| Total return since inception | -3.16% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,593.59 (-2.03%) |
| Positions value | $17,528.25 |
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
| BBY | 14 | $88.05 | $88.04 | $1,232.56 | $-0.19 | $79.24 |
| DDOG | 3 | $260.67 | $266.51 | $799.53 | $17.53 | $237.94 |
| DOC | 32 | $22.25 | $21.97 | $703.04 | $-8.98 | $20.55 |
| DVA | 6 | $227.39 | $240.58 | $1,443.48 | $79.12 | $216.78 |
| FTNT | 7 | $149.43 | $155.50 | $1,088.47 | $42.43 | $138.10 |
| HUM | 3 | $391.16 | $371.29 | $1,113.87 | $-59.60 | $329.83 |
| MPC | 3 | $306.56 | $312.03 | $936.09 | $16.41 | $287.83 |
| NTAP | 5 | $161.48 | $172.03 | $860.15 | $52.77 | $157.11 |
| PSX | 5 | $215.50 | $209.35 | $1,046.75 | $-30.73 | $191.32 |
| SPY | 5 | $743.10 | $735.37 | $3,676.82 | $-38.68 | — |
| STT | 8 | $185.86 | $178.72 | $1,429.76 | $-57.11 | $168.04 |
| UNH | 3 | $425.21 | $421.66 | $1,264.98 | $-10.64 | $393.25 |
| VLO | 3 | $304.72 | $308.02 | $924.06 | $9.90 | $283.28 |
| WST | 3 | $336.32 | $336.23 | $1,008.69 | $-0.27 | $302.61 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-29T15:31` exit sell **IBKR** — trailing stop 10%
- `2026-07-29T15:31` exit sell **HUM** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
