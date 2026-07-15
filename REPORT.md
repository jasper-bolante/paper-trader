# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-15 16:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,995.83** |
| Total return since inception | -0.02% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,240.88 (1.20%) |
| Positions value | $16,762.76 |
| Settled cash | $3,222.70 |
| Unsettled cash (T+1) | $14.65 |
| Tax reserve | $4.28 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.64% | 1.03% |
| Annualized volatility | 3.63% | 11.60% |
| Sharpe (rf 4%) | 10.04 | 5.25 |
| Max drawdown | 0.03% | 0.77% |
| EOD observations | 5 | 5 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $33.74 | $1,417.08 | $25.12 | $29.82 |
| CNC | 13 | $66.94 | $66.93 | $870.09 | $-0.15 | $61.84 |
| CSCO | 8 | $120.26 | $111.61 | $892.88 | $-69.21 | $109.12 |
| DVA | 6 | $227.39 | $231.83 | $1,390.98 | $26.62 | $211.95 |
| FFIV | 3 | $430.59 | $414.92 | $1,244.76 | $-47.01 | $388.22 |
| FTNT | 5 | $155.14 | $164.54 | $822.72 | $47.04 | $150.16 |
| HUM | 2 | $401.64 | $411.08 | $822.17 | $18.89 | $365.89 |
| IBKR | 10 | $95.61 | $96.61 | $966.10 | $10.04 | $86.05 |
| NTAP | 5 | $161.48 | $157.87 | $789.35 | $-18.03 | $145.25 |
| SPY | 5 | $743.10 | $751.48 | $3,757.40 | $41.90 | — |
| STT | 8 | $185.86 | $185.53 | $1,484.24 | $-2.63 | $167.18 |
| UNH | 3 | $425.21 | $420.82 | $1,262.46 | $-13.16 | $382.79 |
| URI | 1 | $1,090.35 | $1,042.53 | $1,042.53 | $-47.82 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-15T16:52` no_trade — no signals crossed action thresholds this hour
- `2026-07-15T16:52` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-15T15:09` entry buy **STT** — momentum entry: rank 11, mom 0.388, vol 25%
- `2026-07-15T15:09` entry buy **NTAP** — momentum entry: rank 5, mom 0.600, vol 44%
- `2026-07-14T20:40` system — eod_complete
- `2026-07-14T18:42` no_trade — no signals crossed action thresholds this hour
- `2026-07-14T18:42` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T16:47` no_trade — no signals crossed action thresholds this hour
- `2026-07-14T16:47` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T15:09` entry buy **UNH** — momentum entry: rank 10, mom 0.387, vol 26%
- `2026-07-14T15:09` entry buy **IBKR** — momentum entry: rank 8, mom 0.455, vol 40%
- `2026-07-13T20:00` system — eod_complete
- `2026-07-13T20:00` system **BEN** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-13T20:00` system — corporate_actions_synced
- `2026-07-13T18:18` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
