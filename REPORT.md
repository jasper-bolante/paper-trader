# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 17:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,654.99** |
| Total return since inception | -1.73% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $16,719.88 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $1,586.68 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.50% | 3.32% |
| Annualized volatility | 12.28% | 13.14% |
| Sharpe (rf 4%) | -1.30 | 1.85 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 31 | 31 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.26 | $735.28 | $-28.33 | $25.00 |
| BBY | 14 | $88.05 | $86.22 | $1,207.15 | $-25.60 | $80.33 |
| CRL | 2 | $285.12 | $295.41 | $590.82 | $20.58 | $260.98 |
| CSX | 17 | $50.29 | $51.13 | $869.29 | $14.34 | $46.01 |
| EXPE | 2 | $331.47 | $327.31 | $654.62 | $-8.32 | $298.17 |
| IQV | 2 | $255.46 | $259.08 | $518.16 | $7.25 | $229.79 |
| MPC | 3 | $306.56 | $360.98 | $1,082.94 | $163.26 | $330.10 |
| NTAP | 5 | $161.48 | $196.16 | $980.80 | $173.42 | $186.39 |
| PANW | 2 | $388.28 | $352.55 | $705.10 | $-71.46 | $349.27 |
| PSX | 5 | $215.50 | $243.15 | $1,215.75 | $138.27 | $219.13 |
| SPY | 5 | $743.10 | $764.73 | $3,823.65 | $108.15 | — |
| STT | 8 | $185.86 | $185.37 | $1,482.96 | $-3.91 | $173.64 |
| VEEV | 3 | $250.82 | $251.50 | $754.50 | $2.03 | $225.62 |
| VLO | 3 | $304.72 | $343.54 | $1,030.61 | $116.45 | $315.01 |
| WST | 3 | $336.32 | $356.08 | $1,068.25 | $59.29 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-20T14:09` exit sell **FTNT** — trailing stop 10%
- `2026-08-19T20:56` system — eod_complete
- `2026-08-19T20:56` system — corporate_actions_synced
- `2026-08-19T19:51` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
