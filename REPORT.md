# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 16:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,858.50** |
| Total return since inception | -0.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,826.55 |
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
| BAX | 28 | $27.27 | $25.79 | $722.12 | $-41.49 | $25.00 |
| BBY | 14 | $88.05 | $87.77 | $1,228.78 | $-3.97 | $79.24 |
| CNC | 8 | $75.27 | $65.42 | $523.40 | $-78.73 | $58.73 |
| CRL | 2 | $285.12 | $282.95 | $565.90 | $-4.34 | $258.00 |
| CSX | 17 | $50.29 | $50.30 | $855.10 | $0.15 | $46.01 |
| FTNT | 7 | $149.43 | $157.65 | $1,103.55 | $57.51 | $151.44 |
| HUM | 2 | $398.00 | $383.18 | $766.36 | $-29.63 | $350.32 |
| MPC | 3 | $306.56 | $365.01 | $1,095.03 | $175.35 | $322.39 |
| NTAP | 5 | $161.48 | $205.10 | $1,025.52 | $218.14 | $186.39 |
| NUE | 2 | $269.82 | $264.24 | $528.48 | $-11.16 | $245.50 |
| PANW | 2 | $388.28 | $374.19 | $748.38 | $-28.18 | $349.27 |
| PSX | 5 | $215.50 | $240.93 | $1,204.65 | $127.17 | $216.44 |
| SPY | 5 | $743.10 | $768.68 | $3,843.42 | $127.92 | — |
| STT | 8 | $185.86 | $191.48 | $1,531.84 | $44.97 | $173.64 |
| VLO | 3 | $304.72 | $349.01 | $1,047.03 | $132.87 | $312.28 |
| WST | 3 | $336.32 | $345.66 | $1,036.98 | $28.02 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T16:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T16:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:58` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
