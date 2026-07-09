# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-09 21:34 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,107.02** |
| Total return since inception | 0.54% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,227.43 (1.14%) |
| Positions value | $7,626.48 |
| Settled cash | $12,470.94 |
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
| CNC | 13 | $66.94 | $67.60 | $878.80 | $8.56 | $60.84 |
| DVA | 6 | $227.39 | $229.25 | $1,375.47 | $11.11 | $206.32 |
| FTNT | 5 | $155.14 | $163.69 | $818.45 | $42.77 | $147.32 |
| HUM | 2 | $401.64 | $398.00 | $796.01 | $-7.27 | $361.29 |
| SPY | 5 | $743.10 | $751.55 | $3,757.75 | $42.25 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $11.29. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-08T14:56` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T14:56` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
