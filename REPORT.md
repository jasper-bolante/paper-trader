# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 20:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,839.31** |
| Total return since inception | -0.80% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,812.76 |
| Settled cash | $1,119.18 |
| Unsettled cash (T+1) | $914.34 |
| Tax reserve | $6.97 |

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
| BAX | 28 | $27.27 | $25.91 | $725.48 | $-38.13 | $25.00 |
| BBY | 14 | $88.05 | $85.45 | $1,196.30 | $-36.45 | $79.24 |
| CNC | 8 | $75.27 | $64.43 | $515.44 | $-86.69 | $58.73 |
| CRL | 2 | $285.12 | $286.67 | $573.34 | $3.10 | $258.00 |
| CSX | 17 | $50.29 | $50.59 | $860.03 | $5.08 | $46.01 |
| FTNT | 7 | $149.43 | $155.79 | $1,090.53 | $44.49 | $151.44 |
| HUM | 2 | $398.00 | $383.92 | $767.84 | $-28.15 | $350.32 |
| MPC | 3 | $306.56 | $358.21 | $1,074.63 | $154.95 | $322.39 |
| NTAP | 5 | $161.48 | $204.23 | $1,021.15 | $213.77 | $186.39 |
| NUE | 2 | $269.82 | $272.78 | $545.56 | $5.92 | $245.50 |
| PANW | 2 | $388.28 | $375.84 | $751.68 | $-24.88 | $349.27 |
| PSX | 5 | $215.50 | $240.49 | $1,202.45 | $124.97 | $216.44 |
| SPY | 5 | $743.10 | $772.75 | $3,863.75 | $148.25 | — |
| STT | 8 | $185.86 | $192.93 | $1,543.44 | $56.57 | $173.64 |
| VLO | 3 | $304.72 | $346.98 | $1,040.94 | $126.78 | $312.28 |
| WST | 3 | $336.32 | $346.74 | $1,040.20 | $31.24 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-17T14:55` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T14:55` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-17T14:03` entry buy **CNC** — momentum entry: rank 5, mom 0.422, vol 38%
- `2026-08-17T14:03` entry buy **CRL** — momentum entry: rank 4, mom 0.464, vol 47%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
