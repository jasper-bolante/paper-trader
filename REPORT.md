# Paper Trading Account — Performance Report

_Updated 2026-07-08 20:45 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,013.61** |
| Total return since inception | 0.07% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,035.26 (0.18%) |
| Positions value | $5,298.47 |
| Settled cash | $14,705.54 |
| Unsettled cash (T+1) | $11.29 |
| Tax reserve | $1.69 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.00% | 0.00% |
| Annualized volatility | — | — |
| Sharpe (rf 4%) | — | — |
| Max drawdown | — | — |
| EOD observations | 1 | 1 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| FTNT | 5 | $155.14 | $156.70 | $783.50 | $7.82 | $141.03 |
| HUM | 2 | $401.64 | $396.46 | $792.92 | $-10.36 | $361.29 |
| SPY | 5 | $743.10 | $744.41 | $3,722.05 | $6.55 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $11.29. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-08T20:45` system **HUM** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-08T20:45` system **SPY** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-08T20:45` system — corporate_actions_synced
- `2026-07-08T18:55` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T18:55` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)
- `2026-07-08T17:00` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T17:00` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)
- `2026-07-08T14:56` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T14:56` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)
- `2026-07-08T14:33` system **SPY** — SPY buy-and-hold benchmark funded with same $
- `2026-07-08T14:33` entry buy **SPY** — ballast rebalance: 0.0% < band 15%, buying toward 20%
- `2026-07-08T14:33` entry buy **HUM** — momentum entry: rank 2, mom 0.900, vol 38%
- `2026-07-08T14:33` entry buy **FTNT** — momentum entry: rank 1, mom 0.951, vol 44%
- `2026-07-08T14:32` system — simulated cash account funded; T+1 settlement, no margin

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
