# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 17:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,900.28** |
| Total return since inception | -0.50% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,873.73 |
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
| BAX | 28 | $27.27 | $25.91 | $725.62 | $-37.99 | $25.00 |
| BBY | 14 | $88.05 | $85.68 | $1,199.52 | $-33.23 | $79.24 |
| CNC | 8 | $75.27 | $64.77 | $518.16 | $-83.97 | $58.73 |
| CRL | 2 | $285.12 | $288.19 | $576.38 | $6.14 | $256.47 |
| CSX | 17 | $50.29 | $50.84 | $864.37 | $9.41 | $46.01 |
| FTNT | 7 | $149.43 | $156.91 | $1,098.37 | $52.33 | $151.44 |
| HUM | 2 | $398.00 | $384.43 | $768.86 | $-27.13 | $350.32 |
| MPC | 3 | $306.56 | $361.55 | $1,084.65 | $164.97 | $321.00 |
| NTAP | 5 | $161.48 | $206.28 | $1,031.42 | $224.04 | $186.39 |
| NUE | 2 | $269.82 | $271.39 | $542.78 | $3.14 | $245.24 |
| PANW | 2 | $388.28 | $374.69 | $749.37 | $-27.19 | $349.27 |
| PSX | 5 | $215.50 | $239.07 | $1,195.35 | $117.87 | $210.25 |
| SPY | 5 | $743.10 | $773.43 | $3,867.15 | $151.65 | — |
| STT | 8 | $185.86 | $194.54 | $1,556.32 | $69.45 | $172.62 |
| VLO | 3 | $304.72 | $348.76 | $1,046.28 | $132.12 | $308.51 |
| WST | 3 | $336.32 | $349.71 | $1,049.13 | $40.17 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-14T19:30` no_trade skip_entry **URI** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **TRV** — insufficient investable cash (size $318, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
