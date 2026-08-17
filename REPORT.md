# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 16:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,946.40** |
| Total return since inception | -0.27% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,919.85 |
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
| BAX | 28 | $27.27 | $26.16 | $732.34 | $-31.27 | $25.00 |
| BBY | 14 | $88.05 | $85.81 | $1,201.27 | $-31.48 | $79.24 |
| CNC | 8 | $75.27 | $65.08 | $520.64 | $-81.49 | $58.73 |
| CRL | 2 | $285.12 | $288.57 | $577.14 | $6.90 | $256.47 |
| CSX | 17 | $50.29 | $50.98 | $866.58 | $11.62 | $46.01 |
| FTNT | 7 | $149.43 | $157.57 | $1,103.02 | $56.98 | $151.44 |
| HUM | 2 | $398.00 | $385.60 | $771.19 | $-24.80 | $350.32 |
| MPC | 3 | $306.56 | $362.42 | $1,087.26 | $167.58 | $321.00 |
| NTAP | 5 | $161.48 | $207.26 | $1,036.30 | $228.92 | $186.39 |
| NUE | 2 | $269.82 | $271.43 | $542.86 | $3.22 | $245.24 |
| PANW | 2 | $388.28 | $374.71 | $749.42 | $-27.14 | $349.27 |
| PSX | 5 | $215.50 | $240.09 | $1,200.45 | $122.97 | $210.25 |
| SPY | 5 | $743.10 | $774.80 | $3,874.02 | $158.52 | — |
| STT | 8 | $185.86 | $194.75 | $1,557.96 | $71.09 | $172.62 |
| VLO | 3 | $304.72 | $349.21 | $1,047.63 | $133.47 | $308.51 |
| WST | 3 | $336.32 | $350.59 | $1,051.77 | $42.81 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-14T19:30` no_trade skip_entry **ALL** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $318, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
