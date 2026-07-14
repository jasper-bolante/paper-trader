# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-14 20:40 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,142.10** |
| Total return since inception | 0.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,240.88 (1.20%) |
| Positions value | $14,614.78 |
| Settled cash | $5,516.95 |
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
| BEN | 42 | $33.14 | $33.13 | $1,391.67 | $-0.29 | $29.82 |
| CNC | 13 | $66.94 | $68.72 | $893.30 | $23.06 | $61.84 |
| CSCO | 8 | $120.26 | $117.10 | $936.80 | $-25.29 | $109.12 |
| DVA | 6 | $227.39 | $232.35 | $1,394.10 | $29.74 | $211.95 |
| FFIV | 3 | $430.59 | $431.35 | $1,294.05 | $2.28 | $388.22 |
| FTNT | 5 | $155.14 | $166.84 | $834.20 | $58.52 | $150.16 |
| HUM | 2 | $401.64 | $406.54 | $813.08 | $9.80 | $365.89 |
| IBKR | 10 | $95.61 | $95.61 | $956.10 | $0.04 | $86.05 |
| SPY | 5 | $743.10 | $752.05 | $3,760.25 | $44.75 | — |
| UNH | 3 | $425.21 | $425.32 | $1,275.97 | $0.36 | $382.79 |
| URI | 1 | $1,090.35 | $1,065.26 | $1,065.26 | $-25.09 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-13T18:18` no_trade skip_entry — no entry slots (positions 8/15, new today 2/2)
- `2026-07-13T16:06` entry buy **URI** — momentum entry: rank 8, mom 0.423, vol 35%
- `2026-07-13T16:06` entry buy **BEN** — momentum entry: rank 7, mom 0.438, vol 28%
- `2026-07-10T20:00` system — eod_complete
- `2026-07-10T20:00` system **CSCO** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
