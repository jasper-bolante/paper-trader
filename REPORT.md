# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-13 18:18 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,112.78** |
| Total return since inception | 0.56% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,318.67 (1.59%) |
| Positions value | $12,365.56 |
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
| BEN | 42 | $33.14 | $32.85 | $1,379.91 | $-12.05 | $29.81 |
| CNC | 13 | $66.94 | $68.15 | $885.95 | $15.71 | $60.84 |
| CSCO | 8 | $120.26 | $120.03 | $960.24 | $-1.85 | $109.12 |
| DVA | 6 | $227.39 | $235.35 | $1,412.10 | $47.74 | $209.26 |
| FFIV | 3 | $430.59 | $424.36 | $1,273.08 | $-18.69 | $387.13 |
| FTNT | 5 | $155.14 | $160.94 | $804.70 | $29.02 | $147.32 |
| HUM | 2 | $401.64 | $408.13 | $816.26 | $12.98 | $361.29 |
| SPY | 5 | $743.10 | $749.44 | $3,747.20 | $31.70 | — |
| URI | 1 | $1,090.35 | $1,086.12 | $1,086.12 | $-4.23 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $14.65. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-09T18:19` no_trade skip_entry — no entry slots (positions 4/15, new today 2/2)
- `2026-07-09T16:13` entry buy **DVA** — momentum entry: rank 4, mom 0.706, vol 25%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
