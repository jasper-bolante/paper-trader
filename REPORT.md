# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-30 20:44 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,454.50** |
| Total return since inception | -2.73% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,986.27 (-0.07%) |
| Positions value | $17,614.76 |
| Settled cash | $1,035.89 |
| Unsettled cash (T+1) | $810.11 |
| Tax reserve | $6.26 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.79% | -0.24% |
| Annualized volatility | 9.70% | 14.62% |
| Sharpe (rf 4%) | -4.96 | -0.47 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 17 | 17 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $87.79 | $1,229.06 | $-3.69 | $79.24 |
| DDOG | 3 | $260.67 | $268.71 | $806.13 | $24.13 | $241.84 |
| DOC | 32 | $22.25 | $22.05 | $705.60 | $-6.42 | $20.55 |
| DVA | 6 | $227.39 | $239.48 | $1,436.88 | $72.52 | $216.78 |
| FTNT | 7 | $149.43 | $154.21 | $1,079.47 | $33.43 | $138.79 |
| HUM | 3 | $391.16 | $366.69 | $1,100.07 | $-73.40 | $330.02 |
| MPC | 3 | $306.56 | $313.88 | $941.64 | $21.96 | $287.83 |
| NTAP | 5 | $161.48 | $174.02 | $870.10 | $62.72 | $157.11 |
| PSX | 5 | $215.50 | $210.58 | $1,052.90 | $-24.58 | $191.32 |
| SPY | 5 | $743.10 | $742.59 | $3,712.95 | $-2.55 | — |
| STT | 8 | $185.86 | $182.81 | $1,462.52 | $-24.35 | $168.04 |
| UNH | 3 | $425.21 | $421.62 | $1,264.86 | $-10.76 | $393.25 |
| VLO | 3 | $304.72 | $311.63 | $934.89 | $20.73 | $283.28 |
| WST | 3 | $336.32 | $339.23 | $1,017.69 | $8.73 | $305.31 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $41.74. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-30T20:44` system **WST** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-30T20:44` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
