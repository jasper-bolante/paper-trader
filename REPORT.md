# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 15:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,856.13** |
| Total return since inception | -0.72% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,824.18 |
| Settled cash | $2,029.92 |
| Unsettled cash (T+1) | $9.95 |
| Tax reserve | $7.92 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.87% | 3.81% |
| Annualized volatility | 12.53% | 13.38% |
| Sharpe (rf 4%) | -0.89 | 2.28 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 29 | 29 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.21 | $734.02 | $-29.59 | $25.00 |
| BBY | 14 | $88.05 | $87.86 | $1,230.04 | $-2.71 | $79.24 |
| CNC | 8 | $75.27 | $65.61 | $524.84 | $-77.29 | $58.73 |
| CRL | 2 | $285.12 | $285.74 | $571.47 | $1.23 | $258.00 |
| CSX | 17 | $50.29 | $50.59 | $860.03 | $5.08 | $46.01 |
| FTNT | 7 | $149.43 | $156.49 | $1,095.43 | $49.39 | $151.44 |
| HUM | 2 | $398.00 | $387.21 | $774.42 | $-21.57 | $350.32 |
| MPC | 3 | $306.56 | $362.22 | $1,086.66 | $166.98 | $322.39 |
| NTAP | 5 | $161.48 | $203.59 | $1,017.95 | $210.57 | $186.39 |
| NUE | 2 | $269.82 | $264.44 | $528.87 | $-10.77 | $245.50 |
| PANW | 2 | $388.28 | $369.60 | $739.20 | $-37.36 | $349.27 |
| PSX | 5 | $215.50 | $240.28 | $1,201.38 | $123.89 | $216.44 |
| SPY | 5 | $743.10 | $767.70 | $3,838.48 | $122.98 | — |
| STT | 8 | $185.86 | $191.75 | $1,534.00 | $47.13 | $173.64 |
| VLO | 3 | $304.72 | $346.89 | $1,040.67 | $126.51 | $312.28 |
| WST | 3 | $336.32 | $348.91 | $1,046.73 | $37.77 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T15:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:03` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T14:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:07` system **PSX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-17T20:56` system — eod_complete
- `2026-08-17T20:56` system — corporate_actions_synced
- `2026-08-17T19:53` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T19:53` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-17T19:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-17T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-17T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T16:57` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
