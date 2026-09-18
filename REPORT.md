# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-18 19:54 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,954.40** |
| Total return since inception | -0.23% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,522.41 (2.61%) |
| Positions value | $18,082.60 |
| Settled cash | $1,868.39 |
| Unsettled cash (T+1) | $16.46 |
| Tax reserve | $13.05 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.24% | 2.43% |
| Annualized volatility | 11.47% | 11.74% |
| Sharpe (rf 4%) | -0.19 | 0.75 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 51 | 51 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $198.82 | $795.30 | $28.18 | $179.57 |
| BBY | 8 | $101.21 | $93.31 | $746.48 | $-63.20 | $85.09 |
| CNC | 16 | $71.60 | $65.31 | $1,044.96 | $-100.66 | $59.53 |
| CRL | 3 | $296.67 | $277.86 | $833.57 | $-56.45 | $256.69 |
| GEN | 40 | $29.13 | $29.00 | $1,159.80 | $-5.46 | $26.22 |
| IQV | 2 | $255.46 | $266.98 | $533.96 | $23.05 | $244.26 |
| MPC | 3 | $306.56 | $423.66 | $1,270.98 | $351.30 | $380.05 |
| NTAP | 5 | $206.27 | $196.44 | $982.20 | $-49.15 | $179.40 |
| PSX | 5 | $215.50 | $273.09 | $1,365.45 | $287.97 | $246.58 |
| RVTY | 9 | $122.75 | $143.37 | $1,290.33 | $185.61 | $132.06 |
| SPY | 5 | $743.10 | $761.41 | $3,807.05 | $91.55 | — |
| TECH | 12 | $72.32 | $72.43 | $869.16 | $1.32 | $65.20 |
| TGT | 7 | $162.82 | $157.97 | $1,105.79 | $-33.92 | $147.91 |
| VLO | 3 | $304.72 | $412.59 | $1,237.77 | $323.61 | $371.22 |
| ZBRA | 3 | $345.13 | $346.60 | $1,039.80 | $4.42 | $313.44 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,107.74 | $0.00 | $1,142.35 |

Dividends received: $87.01. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-18T19:54` no_trade — no signals crossed action thresholds this hour
- `2026-09-18T19:54` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-09-18T17:09` entry buy **GEN** — momentum entry: rank 10, mom 0.314, vol 33%
- `2026-09-18T17:09` entry buy **CNC** — momentum entry: rank 8, mom 0.412, vol 36%
- `2026-09-17T21:39` system — eod_complete
- `2026-09-17T17:43` entry buy **ZBRA** — momentum entry: rank 4, mom 0.548, vol 26%
- `2026-09-17T17:43` entry buy **CRL** — momentum entry: rank 3, mom 0.565, vol 42%
- `2026-09-17T17:43` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-17T17:43` exit sell **GPC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-17T17:43` exit sell **FDS** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-17T17:43` system **BBY** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-16T21:37` system — eod_complete
- `2026-09-16T17:42` no_trade skip_entry **GEN** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **MET** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **CNC** — insufficient investable cash (size $77, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
