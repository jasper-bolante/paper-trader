# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 19:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,880.81** |
| Total return since inception | -0.60% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,854.26 |
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
| BAX | 28 | $27.27 | $25.98 | $727.58 | $-36.03 | $25.00 |
| BBY | 14 | $88.05 | $85.51 | $1,197.14 | $-35.61 | $79.24 |
| CNC | 8 | $75.27 | $64.46 | $515.68 | $-86.45 | $58.73 |
| CRL | 2 | $285.12 | $284.44 | $568.87 | $-1.37 | $256.47 |
| CSX | 17 | $50.29 | $50.59 | $859.95 | $5.00 | $46.01 |
| FTNT | 7 | $149.43 | $156.63 | $1,096.41 | $50.37 | $151.44 |
| HUM | 2 | $398.00 | $383.76 | $767.52 | $-28.47 | $350.32 |
| MPC | 3 | $306.56 | $362.01 | $1,086.05 | $166.37 | $321.00 |
| NTAP | 5 | $161.48 | $205.69 | $1,028.47 | $221.09 | $186.39 |
| NUE | 2 | $269.82 | $271.88 | $543.76 | $4.12 | $245.24 |
| PANW | 2 | $388.28 | $376.71 | $753.42 | $-23.14 | $349.27 |
| PSX | 5 | $215.50 | $239.57 | $1,197.85 | $120.37 | $210.25 |
| SPY | 5 | $743.10 | $773.27 | $3,866.35 | $150.85 | — |
| STT | 8 | $185.86 | $194.33 | $1,554.64 | $67.77 | $172.62 |
| VLO | 3 | $304.72 | $348.11 | $1,044.33 | $130.17 | $308.51 |
| WST | 3 | $336.32 | $348.75 | $1,046.25 | $37.29 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-14T20:05` system — eod_complete
- `2026-08-14T19:30` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
