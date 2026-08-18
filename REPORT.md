# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 19:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,876.28** |
| Total return since inception | -0.62% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,844.33 |
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
| BAX | 28 | $27.27 | $26.05 | $729.26 | $-34.35 | $25.00 |
| BBY | 14 | $88.05 | $87.79 | $1,229.06 | $-3.69 | $79.24 |
| CNC | 8 | $75.27 | $65.58 | $524.60 | $-77.53 | $58.73 |
| CRL | 2 | $285.12 | $281.40 | $562.81 | $-7.43 | $258.00 |
| CSX | 17 | $50.29 | $50.30 | $855.01 | $0.06 | $46.01 |
| FTNT | 7 | $149.43 | $158.40 | $1,108.77 | $62.73 | $151.44 |
| HUM | 2 | $398.00 | $383.73 | $767.46 | $-28.53 | $350.32 |
| MPC | 3 | $306.56 | $364.71 | $1,094.13 | $174.45 | $322.39 |
| NTAP | 5 | $161.48 | $205.38 | $1,026.90 | $219.52 | $186.39 |
| NUE | 2 | $269.82 | $264.55 | $529.10 | $-10.54 | $245.50 |
| PANW | 2 | $388.28 | $373.75 | $747.50 | $-29.06 | $349.27 |
| PSX | 5 | $215.50 | $242.00 | $1,210.00 | $132.52 | $216.44 |
| SPY | 5 | $743.10 | $767.80 | $3,839.02 | $123.52 | — |
| STT | 8 | $185.86 | $191.81 | $1,534.48 | $47.61 | $173.64 |
| VLO | 3 | $304.72 | $348.97 | $1,046.91 | $132.75 | $312.28 |
| WST | 3 | $336.32 | $346.44 | $1,039.32 | $30.36 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T19:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
