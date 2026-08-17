# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 15:51 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,911.61** |
| Total return since inception | -0.44% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,885.06 |
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
| BAX | 28 | $27.27 | $26.25 | $734.86 | $-28.75 | $25.00 |
| BBY | 14 | $88.05 | $85.67 | $1,199.38 | $-33.37 | $79.24 |
| CNC | 8 | $75.27 | $64.64 | $517.12 | $-85.01 | $58.73 |
| CRL | 2 | $285.12 | $287.31 | $574.61 | $4.37 | $256.47 |
| CSX | 17 | $50.29 | $50.78 | $863.34 | $8.39 | $46.01 |
| FTNT | 7 | $149.43 | $157.84 | $1,104.85 | $58.81 | $151.44 |
| HUM | 2 | $398.00 | $383.38 | $766.76 | $-29.23 | $350.32 |
| MPC | 3 | $306.56 | $361.26 | $1,083.78 | $164.10 | $321.00 |
| NTAP | 5 | $161.48 | $206.13 | $1,030.67 | $223.29 | $186.39 |
| NUE | 2 | $269.82 | $270.56 | $541.13 | $1.49 | $245.24 |
| PANW | 2 | $388.28 | $378.73 | $757.46 | $-19.10 | $349.27 |
| PSX | 5 | $215.50 | $238.58 | $1,192.90 | $115.42 | $210.25 |
| SPY | 5 | $743.10 | $775.24 | $3,876.18 | $160.68 | — |
| STT | 8 | $185.86 | $194.14 | $1,553.12 | $66.25 | $172.62 |
| VLO | 3 | $304.72 | $347.14 | $1,041.42 | $127.26 | $308.51 |
| WST | 3 | $336.32 | $349.16 | $1,047.48 | $38.52 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-14T19:30` no_trade skip_entry **GEN** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **FFIV** — insufficient investable cash (size $318, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
