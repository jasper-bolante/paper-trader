# Paper Trading Account — Performance Report

_Updated 2026-07-08 15:20 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,983.34** |
| Total return since inception | -0.08% |
| S&P 500 benchmark (same $ , dividends reinvested) | — (—) |
| Positions value | $5,277.80 |
| Settled cash | $14,705.54 |
| Unsettled cash (T+1) | $0.00 |
| Tax reserve | $0.00 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | — | — |
| Annualized volatility | — | — |
| Sharpe (rf 4%) | — | — |
| Max drawdown | — | — |
| EOD observations | 0 | 0 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| FTNT | 5 | $155.14 | $155.09 | $775.48 | $-0.20 | $139.55 |
| HUM | 2 | $401.64 | $398.45 | $796.90 | $-6.38 | $361.29 |
| SPY | 5 | $743.10 | $741.09 | $3,705.43 | $-10.07 | — |

## Realized gains & tax

_No realized gains yet._

Dividends received: $0.00. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-08T14:56` no_trade — no signals crossed action thresholds this hour
- `2026-07-08T14:56` no_trade skip_entry — no entry slots (positions 2/15, new today 2/2)
- `2026-07-08T14:33` system **SPY** — SPY buy-and-hold benchmark funded with same $
- `2026-07-08T14:33` entry buy **SPY** — ballast rebalance: 0.0% < band 15%, buying toward 20%
- `2026-07-08T14:33` entry buy **HUM** — momentum entry: rank 2, mom 0.900, vol 38%
- `2026-07-08T14:33` entry buy **FTNT** — momentum entry: rank 1, mom 0.951, vol 44%
- `2026-07-08T14:32` system — simulated cash account funded; T+1 settlement, no margin

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
