# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-14 16:47 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,120.32** |
| Total return since inception | 0.60% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,162.29 (0.81%) |
| Positions value | $14,592.99 |
| Settled cash | $5,516.95 |
| Unsettled cash (T+1) | $14.65 |
| Tax reserve | $4.28 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.44% | 0.63% |
| Annualized volatility | 4.41% | 14.11% |
| Sharpe (rf 4%) | 7.47 | 3.53 |
| Max drawdown | 0.03% | 0.77% |
| EOD observations | 4 | 4 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $32.97 | $1,384.53 | $-7.43 | $29.81 |
| CNC | 13 | $66.94 | $68.78 | $894.14 | $23.90 | $61.46 |
| CSCO | 8 | $120.26 | $117.45 | $939.60 | $-22.49 | $109.12 |
| DVA | 6 | $227.39 | $233.47 | $1,400.82 | $36.46 | $211.95 |
| FFIV | 3 | $430.59 | $427.95 | $1,283.85 | $-7.92 | $387.13 |
| FTNT | 5 | $155.14 | $166.14 | $830.70 | $55.02 | $147.32 |
| HUM | 2 | $401.64 | $406.09 | $812.18 | $8.90 | $365.27 |
| IBKR | 10 | $95.61 | $94.83 | $948.30 | $-7.76 | $86.00 |
| SPY | 5 | $743.10 | $751.24 | $3,756.20 | $40.70 | — |
| UNH | 3 | $425.21 | $425.25 | $1,275.74 | $0.12 | $382.49 |
| URI | 1 | $1,090.35 | $1,066.94 | $1,066.94 | $-23.41 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-10T20:00` system — corporate_actions_synced
- `2026-07-10T18:09` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
