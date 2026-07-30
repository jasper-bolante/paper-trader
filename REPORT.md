# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-30 18:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,430.49** |
| Total return since inception | -2.85% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,593.59 (-2.03%) |
| Positions value | $17,591.31 |
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
| BBY | 14 | $88.05 | $88.31 | $1,236.34 | $3.59 | $79.24 |
| DDOG | 3 | $260.67 | $266.44 | $799.34 | $17.34 | $237.94 |
| DOC | 32 | $22.25 | $22.05 | $705.76 | $-6.26 | $20.55 |
| DVA | 6 | $227.39 | $239.30 | $1,435.80 | $71.44 | $216.78 |
| FTNT | 7 | $149.43 | $152.58 | $1,068.06 | $22.02 | $138.10 |
| HUM | 3 | $391.16 | $372.19 | $1,116.56 | $-56.91 | $329.83 |
| MPC | 3 | $306.56 | $314.98 | $944.94 | $25.26 | $287.83 |
| NTAP | 5 | $161.48 | $173.16 | $865.82 | $58.44 | $157.11 |
| PSX | 5 | $215.50 | $210.33 | $1,051.65 | $-25.83 | $191.32 |
| SPY | 5 | $743.10 | $740.60 | $3,703.00 | $-12.50 | — |
| STT | 8 | $185.86 | $182.01 | $1,456.08 | $-30.79 | $168.04 |
| UNH | 3 | $425.21 | $422.98 | $1,268.94 | $-6.68 | $393.25 |
| VLO | 3 | $304.72 | $309.16 | $927.48 | $13.32 | $283.28 |
| WST | 3 | $336.32 | $337.18 | $1,011.54 | $2.58 | $302.61 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-30T18:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-30T18:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
