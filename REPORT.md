# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 19:53 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,857.68** |
| Total return since inception | -0.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,831.13 |
| Settled cash | $1,119.18 |
| Unsettled cash (T+1) | $914.34 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.50% | 4.25% |
| Annualized volatility | 12.72% | 13.52% |
| Sharpe (rf 4%) | -0.62 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 28 | 28 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.95 | $726.74 | $-36.87 | $25.00 |
| BBY | 14 | $88.05 | $85.27 | $1,193.78 | $-38.97 | $79.24 |
| CNC | 8 | $75.27 | $64.67 | $517.40 | $-84.73 | $58.73 |
| CRL | 2 | $285.12 | $285.90 | $571.80 | $1.56 | $256.47 |
| CSX | 17 | $50.29 | $50.53 | $859.01 | $4.06 | $46.01 |
| FTNT | 7 | $149.43 | $156.05 | $1,092.35 | $46.31 | $151.44 |
| HUM | 2 | $398.00 | $384.08 | $768.16 | $-27.83 | $350.32 |
| MPC | 3 | $306.56 | $361.09 | $1,083.27 | $163.59 | $321.00 |
| NTAP | 5 | $161.48 | $205.06 | $1,025.30 | $217.92 | $186.39 |
| NUE | 2 | $269.82 | $272.60 | $545.20 | $5.56 | $245.24 |
| PANW | 2 | $388.28 | $374.96 | $749.92 | $-26.64 | $349.27 |
| PSX | 5 | $215.50 | $240.44 | $1,202.17 | $124.69 | $210.25 |
| SPY | 5 | $743.10 | $772.79 | $3,863.95 | $148.45 | — |
| STT | 8 | $185.86 | $193.31 | $1,546.48 | $59.61 | $172.62 |
| VLO | 3 | $304.72 | $347.87 | $1,043.61 | $129.45 | $308.51 |
| WST | 3 | $336.32 | $347.33 | $1,041.99 | $33.03 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-17T14:55` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T14:55` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-17T14:03` entry buy **CNC** — momentum entry: rank 5, mom 0.422, vol 38%
- `2026-08-17T14:03` entry buy **CRL** — momentum entry: rank 4, mom 0.464, vol 47%
- `2026-08-17T14:03` exit sell **HPQ** — momentum rank decayed (None > 150 or ineligible: volatility 0.5054050659101534 above cap 0.5)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
