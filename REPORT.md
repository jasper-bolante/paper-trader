# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-24 21:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,698.16** |
| Total return since inception | -1.51% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,182.69 |
| Settled cash | $1,579.42 |
| Unsettled cash (T+1) | $944.42 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.58% | 2.58% |
| Annualized volatility | 12.09% | 12.84% |
| Sharpe (rf 4%) | -1.28 | 1.27 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 34 | 34 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.49 | $741.72 | $-21.89 | $25.00 |
| BBY | 14 | $88.05 | $87.46 | $1,224.44 | $-8.31 | $80.33 |
| CRL | 2 | $285.12 | $298.56 | $597.12 | $26.88 | $268.70 |
| CSX | 17 | $50.29 | $51.45 | $874.65 | $19.70 | $46.44 |
| EXPE | 2 | $331.47 | $339.15 | $678.30 | $15.36 | $305.24 |
| FDS | 2 | $299.76 | $305.01 | $610.02 | $10.49 | $274.51 |
| IQV | 2 | $255.46 | $260.31 | $520.61 | $9.70 | $234.27 |
| MPC | 3 | $306.56 | $362.62 | $1,087.86 | $168.18 | $330.10 |
| NTAP | 4 | $187.95 | $186.93 | $747.72 | $-4.07 | $169.07 |
| PANW | 2 | $388.17 | $350.68 | $701.36 | $-74.98 | $322.11 |
| PSX | 5 | $215.50 | $241.94 | $1,209.70 | $132.22 | $219.13 |
| SPY | 5 | $743.10 | $763.65 | $3,818.25 | $102.75 | — |
| STT | 8 | $185.86 | $190.98 | $1,527.84 | $40.97 | $173.64 |
| VEEV | 3 | $250.82 | $248.45 | $745.35 | $-7.12 | $225.63 |
| VLO | 3 | $304.72 | $345.96 | $1,037.88 | $123.72 | $315.01 |
| WST | 3 | $336.32 | $353.29 | $1,059.87 | $50.91 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-24T19:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:56` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T19:10` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:10` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T18:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T18:00` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T16:05` entry buy **NTAP** — momentum entry: rank 2, mom 0.918, vol 44%
- `2026-08-24T16:05` exit sell **NTAP** — trailing stop 10%
- `2026-08-24T15:11` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T15:11` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T14:20` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T14:20` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-21T20:52` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
