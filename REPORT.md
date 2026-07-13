# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-13 16:06 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,152.41** |
| Total return since inception | 0.76% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,318.67 (1.59%) |
| Positions value | $12,405.19 |
| Settled cash | $7,734.77 |
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
| BEN | 42 | $33.14 | $33.12 | $1,391.04 | $-0.92 | $29.81 |
| CNC | 13 | $66.94 | $68.46 | $889.98 | $19.74 | $60.84 |
| CSCO | 8 | $120.26 | $120.11 | $960.88 | $-1.21 | $109.12 |
| DVA | 6 | $227.39 | $235.69 | $1,414.14 | $49.78 | $209.26 |
| FFIV | 3 | $430.59 | $426.78 | $1,280.34 | $-11.43 | $387.13 |
| FTNT | 5 | $155.14 | $161.65 | $808.23 | $32.55 | $147.32 |
| HUM | 2 | $401.64 | $407.51 | $815.02 | $11.74 | $361.29 |
| SPY | 5 | $743.10 | $751.16 | $3,755.80 | $40.30 | — |
| URI | 1 | $1,090.35 | $1,089.77 | $1,089.77 | $-0.58 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $14.65. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-09T18:19` no_trade skip_entry — no entry slots (positions 4/15, new today 2/2)
- `2026-07-09T16:13` entry buy **DVA** — momentum entry: rank 4, mom 0.706, vol 25%
- `2026-07-09T16:13` entry buy **CNC** — momentum entry: rank 3, mom 0.802, vol 42%
- `2026-07-08T20:45` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
