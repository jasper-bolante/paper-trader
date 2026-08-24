# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 14:20 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,670.39** |
| Total return since inception | -1.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,334.60 |
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
| BAX | 28 | $27.27 | $26.36 | $738.08 | $-25.53 | $25.00 |
| BBY | 14 | $88.05 | $87.30 | $1,222.13 | $-10.62 | $80.33 |
| CRL | 2 | $285.12 | $295.50 | $591.00 | $20.76 | $265.83 |
| CSX | 17 | $50.29 | $51.68 | $878.56 | $23.61 | $46.44 |
| EXPE | 2 | $331.47 | $333.39 | $666.79 | $3.85 | $298.17 |
| FDS | 2 | $299.76 | $304.33 | $608.67 | $9.14 | $269.64 |
| IQV | 2 | $255.46 | $259.98 | $519.96 | $9.05 | $234.04 |
| MPC | 3 | $306.56 | $361.39 | $1,084.17 | $164.49 | $330.10 |
| NTAP | 5 | $161.48 | $187.72 | $938.60 | $131.22 | $186.39 |
| PANW | 2 | $388.17 | $347.57 | $695.15 | $-81.19 | $322.11 |
| PSX | 5 | $215.50 | $242.57 | $1,212.88 | $135.39 | $219.13 |
| SPY | 5 | $743.10 | $762.89 | $3,814.45 | $98.95 | — |
| STT | 8 | $185.86 | $189.61 | $1,516.88 | $30.01 | $173.64 |
| VEEV | 3 | $250.82 | $248.34 | $745.00 | $-7.47 | $225.63 |
| VLO | 3 | $304.72 | $347.58 | $1,042.74 | $128.58 | $315.01 |
| WST | 3 | $336.32 | $353.18 | $1,059.54 | $50.58 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-21T16:00` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T15:05` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
