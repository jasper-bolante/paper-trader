# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 14:22 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,631.35** |
| Total return since inception | -1.84% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,115.88 |
| Settled cash | $2,510.89 |
| Unsettled cash (T+1) | $12.95 |
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
| BAX | 28 | $27.27 | $26.10 | $730.80 | $-32.81 | $25.00 |
| BBY | 14 | $88.05 | $86.44 | $1,210.16 | $-22.59 | $80.33 |
| CRL | 2 | $285.12 | $297.73 | $595.46 | $25.22 | $268.70 |
| CSX | 17 | $50.29 | $51.63 | $877.79 | $22.84 | $46.44 |
| EXPE | 2 | $331.47 | $335.96 | $671.92 | $8.98 | $305.24 |
| FDS | 2 | $299.76 | $301.34 | $602.68 | $3.15 | $274.51 |
| IQV | 2 | $255.46 | $259.51 | $519.02 | $8.11 | $234.27 |
| MPC | 3 | $306.56 | $359.74 | $1,079.20 | $159.52 | $330.10 |
| NTAP | 4 | $187.95 | $188.11 | $752.44 | $0.65 | $169.07 |
| PANW | 2 | $388.17 | $346.86 | $693.72 | $-82.62 | $322.11 |
| PSX | 5 | $215.50 | $240.86 | $1,204.30 | $126.82 | $219.13 |
| SPY | 5 | $743.10 | $765.14 | $3,825.72 | $110.22 | — |
| STT | 8 | $185.86 | $191.00 | $1,528.00 | $41.13 | $173.64 |
| VEEV | 3 | $250.82 | $244.77 | $734.31 | $-18.16 | $225.63 |
| VLO | 3 | $304.72 | $345.78 | $1,037.34 | $123.18 | $315.01 |
| WST | 3 | $336.32 | $351.00 | $1,053.00 | $44.04 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-25T14:22` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T14:22` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T21:00` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
