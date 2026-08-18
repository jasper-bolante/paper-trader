# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 15:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,859.08** |
| Total return since inception | -0.70% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,827.13 |
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
| BAX | 28 | $27.27 | $25.98 | $727.30 | $-36.31 | $25.00 |
| BBY | 14 | $88.05 | $87.56 | $1,225.77 | $-6.98 | $79.24 |
| CNC | 8 | $75.27 | $65.42 | $523.32 | $-78.81 | $58.73 |
| CRL | 2 | $285.12 | $283.87 | $567.74 | $-2.50 | $258.00 |
| CSX | 17 | $50.29 | $50.31 | $855.27 | $0.32 | $46.01 |
| FTNT | 7 | $149.43 | $156.84 | $1,097.88 | $51.84 | $151.44 |
| HUM | 2 | $398.00 | $383.46 | $766.92 | $-29.07 | $350.32 |
| MPC | 3 | $306.56 | $365.04 | $1,095.12 | $175.44 | $322.39 |
| NTAP | 5 | $161.48 | $206.29 | $1,031.45 | $224.07 | $186.39 |
| NUE | 2 | $269.82 | $264.69 | $529.39 | $-10.25 | $245.50 |
| PANW | 2 | $388.28 | $371.25 | $742.50 | $-34.06 | $349.27 |
| PSX | 5 | $215.50 | $241.20 | $1,206.00 | $128.52 | $216.44 |
| SPY | 5 | $743.10 | $768.12 | $3,840.60 | $125.10 | — |
| STT | 8 | $185.86 | $191.38 | $1,531.04 | $44.17 | $173.64 |
| VLO | 3 | $304.72 | $348.28 | $1,044.84 | $130.68 | $312.28 |
| WST | 3 | $336.32 | $347.33 | $1,041.99 | $33.03 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-17T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
