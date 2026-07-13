# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-13 20:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,101.57** |
| Total return since inception | 0.51% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,162.29 (0.81%) |
| Positions value | $12,342.57 |
| Settled cash | $7,748.63 |
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
| BEN | 42 | $33.14 | $32.84 | $1,379.28 | $-12.68 | $29.81 |
| CNC | 13 | $66.94 | $68.29 | $887.77 | $17.53 | $61.46 |
| CSCO | 8 | $120.26 | $119.27 | $954.16 | $-7.93 | $109.12 |
| DVA | 6 | $227.39 | $235.50 | $1,412.97 | $48.61 | $211.95 |
| FFIV | 3 | $430.59 | $420.73 | $1,262.19 | $-29.58 | $387.13 |
| FTNT | 5 | $155.14 | $160.63 | $803.15 | $27.47 | $147.32 |
| HUM | 2 | $401.64 | $405.85 | $811.70 | $8.42 | $365.27 |
| SPY | 5 | $743.10 | $749.13 | $3,745.65 | $30.15 | — |
| URI | 1 | $1,090.35 | $1,085.70 | $1,085.70 | $-4.65 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-10T18:09` no_trade skip_entry — no entry slots (positions 6/15, new today 2/2)
- `2026-07-10T15:57` entry buy **CSCO** — momentum entry: rank 6, mom 0.506, vol 40%
- `2026-07-10T15:57` entry buy **FFIV** — momentum entry: rank 5, mom 0.551, vol 30%
- `2026-07-09T20:24` system — eod_complete
- `2026-07-09T18:19` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
