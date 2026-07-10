# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-10 15:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,092.45** |
| Total return since inception | 0.46% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,227.43 (1.14%) |
| Positions value | $9,865.76 |
| Settled cash | $10,217.08 |
| Unsettled cash (T+1) | $11.29 |
| Tax reserve | $1.69 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.47% | 0.96% |
| Annualized volatility | — | — |
| Sharpe (rf 4%) | — | — |
| Max drawdown | 0.00% | 0.00% |
| EOD observations | 2 | 2 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $67.68 | $879.84 | $9.60 | $60.84 |
| CSCO | 8 | $120.26 | $120.23 | $961.84 | $-0.25 | $108.21 |
| DVA | 6 | $227.39 | $232.00 | $1,392.00 | $27.64 | $206.32 |
| FFIV | 3 | $430.59 | $430.02 | $1,290.06 | $-1.71 | $387.02 |
| FTNT | 5 | $155.14 | $158.43 | $792.12 | $16.45 | $147.32 |
| HUM | 2 | $401.64 | $393.20 | $786.40 | $-16.88 | $361.29 |
| SPY | 5 | $743.10 | $752.70 | $3,763.50 | $48.00 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $11.29. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-08T18:55` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T18:55` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)
- `2026-07-08T17:00` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T17:00` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
