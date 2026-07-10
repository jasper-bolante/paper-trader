# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-10 20:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,107.42** |
| Total return since inception | 0.54% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,318.67 (1.59%) |
| Positions value | $9,877.89 |
| Settled cash | $10,217.08 |
| Unsettled cash (T+1) | $14.65 |
| Tax reserve | $2.20 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.47% | 1.41% |
| Annualized volatility | 5.22% | 5.70% |
| Sharpe (rf 4%) | 10.55 | 30.45 |
| Max drawdown | 0.00% | 0.00% |
| EOD observations | 3 | 3 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $67.35 | $875.55 | $5.31 | $60.84 |
| CSCO | 8 | $120.26 | $121.24 | $969.92 | $7.83 | $109.12 |
| DVA | 6 | $227.39 | $232.51 | $1,395.06 | $30.70 | $209.26 |
| FFIV | 3 | $430.59 | $430.15 | $1,290.45 | $-1.32 | $387.13 |
| FTNT | 5 | $155.14 | $157.50 | $787.50 | $11.82 | $147.32 |
| HUM | 2 | $401.64 | $392.36 | $784.71 | $-18.57 | $361.29 |
| SPY | 5 | $743.10 | $754.94 | $3,774.70 | $59.20 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $14.65. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-10T20:00` system **CSCO** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-10T20:00` system — corporate_actions_synced
- `2026-07-10T18:09` no_trade — no signals crossed action thresholds this hour
- `2026-07-10T18:09` no_trade skip_entry — no entry slots (positions 6/15, new today 2/2)
- `2026-07-10T15:57` entry buy **CSCO** — momentum entry: rank 6, mom 0.506, vol 40%
- `2026-07-10T15:57` entry buy **FFIV** — momentum entry: rank 5, mom 0.551, vol 30%
- `2026-07-09T20:24` system — eod_complete
- `2026-07-09T18:19` no_trade — no signals crossed action thresholds this hour
- `2026-07-09T18:19` no_trade skip_entry — no entry slots (positions 4/15, new today 2/2)
- `2026-07-09T16:13` entry buy **DVA** — momentum entry: rank 4, mom 0.706, vol 25%
- `2026-07-09T16:13` entry buy **CNC** — momentum entry: rank 3, mom 0.802, vol 42%
- `2026-07-08T20:45` system — eod_complete
- `2026-07-08T20:45` system **HUM** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-08T20:45` system **SPY** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-08T20:45` system — corporate_actions_synced

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
