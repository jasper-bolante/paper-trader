# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 15:11 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,642.50** |
| Total return since inception | -1.79% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,306.71 |
| Settled cash | $2,331.21 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.79% | 2.84% |
| Annualized volatility | 12.26% | 13.01% |
| Sharpe (rf 4%) | -1.43 | 1.45 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 33 | 33 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.25 | $734.86 | $-28.75 | $25.00 |
| BBY | 14 | $88.05 | $87.64 | $1,226.96 | $-5.79 | $80.33 |
| CRL | 2 | $285.12 | $294.83 | $589.67 | $19.43 | $265.83 |
| CSX | 17 | $50.29 | $51.45 | $874.65 | $19.70 | $46.44 |
| EXPE | 2 | $331.47 | $333.72 | $667.44 | $4.50 | $298.17 |
| FDS | 2 | $299.76 | $307.04 | $614.08 | $14.55 | $269.64 |
| IQV | 2 | $255.46 | $259.85 | $519.69 | $8.78 | $234.04 |
| MPC | 3 | $306.56 | $358.62 | $1,075.86 | $156.18 | $330.10 |
| NTAP | 5 | $161.48 | $187.36 | $936.80 | $129.42 | $186.39 |
| PANW | 2 | $388.17 | $352.43 | $704.86 | $-71.48 | $322.11 |
| PSX | 5 | $215.50 | $240.32 | $1,201.60 | $124.12 | $219.13 |
| SPY | 5 | $743.10 | $762.87 | $3,814.32 | $98.82 | — |
| STT | 8 | $185.86 | $189.26 | $1,514.08 | $27.21 | $173.64 |
| VEEV | 3 | $250.82 | $248.75 | $746.26 | $-6.21 | $225.63 |
| VLO | 3 | $304.72 | $345.01 | $1,035.03 | $120.87 | $315.01 |
| WST | 3 | $336.32 | $350.18 | $1,050.54 | $41.58 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T15:11` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T15:11` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T14:20` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T14:20` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-21T20:52` system — eod_complete
- `2026-08-21T20:52` system — corporate_actions_synced
- `2026-08-21T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T19:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:07` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:58` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:03` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T16:00` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
