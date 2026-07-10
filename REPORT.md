# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-10 18:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,105.17** |
| Total return since inception | 0.53% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,227.43 (1.14%) |
| Positions value | $9,878.49 |
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
| CNC | 13 | $66.94 | $67.13 | $872.69 | $2.45 | $60.84 |
| CSCO | 8 | $120.26 | $120.36 | $962.92 | $0.83 | $108.21 |
| DVA | 6 | $227.39 | $234.34 | $1,406.04 | $41.68 | $206.32 |
| FFIV | 3 | $430.59 | $430.54 | $1,291.61 | $-0.16 | $387.02 |
| FTNT | 5 | $155.14 | $157.78 | $788.90 | $13.22 | $147.32 |
| HUM | 2 | $401.64 | $392.49 | $784.98 | $-18.30 | $361.29 |
| SPY | 5 | $743.10 | $754.27 | $3,771.35 | $55.85 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $11.29. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-08T18:55` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T18:55` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
