# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 14:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,888.21** |
| Total return since inception | -0.56% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,856.26 |
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
| BAX | 28 | $27.27 | $26.11 | $731.22 | $-32.39 | $25.00 |
| BBY | 14 | $88.05 | $87.01 | $1,218.14 | $-14.61 | $79.24 |
| CNC | 8 | $75.27 | $65.88 | $527.00 | $-75.13 | $58.73 |
| CRL | 2 | $285.12 | $289.53 | $579.06 | $8.82 | $258.00 |
| CSX | 17 | $50.29 | $50.38 | $856.46 | $1.51 | $46.01 |
| FTNT | 7 | $149.43 | $157.37 | $1,101.59 | $55.55 | $151.44 |
| HUM | 2 | $398.00 | $388.56 | $777.12 | $-18.87 | $350.32 |
| MPC | 3 | $306.56 | $361.56 | $1,084.68 | $165.00 | $322.39 |
| NTAP | 5 | $161.48 | $207.13 | $1,035.67 | $228.29 | $186.39 |
| NUE | 2 | $269.82 | $265.89 | $531.78 | $-7.86 | $245.50 |
| PANW | 2 | $388.28 | $373.92 | $747.84 | $-28.72 | $349.27 |
| PSX | 5 | $215.50 | $239.73 | $1,198.65 | $121.17 | $216.44 |
| SPY | 5 | $743.10 | $769.19 | $3,845.95 | $130.45 | — |
| STT | 8 | $185.86 | $192.72 | $1,541.76 | $54.89 | $173.64 |
| VLO | 3 | $304.72 | $346.44 | $1,039.32 | $125.16 | $312.28 |
| WST | 3 | $336.32 | $346.67 | $1,040.01 | $31.05 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-17T15:51` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T15:51` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
