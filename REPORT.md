# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-18 22:46 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,976.16** |
| Total return since inception | -0.12% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,525.64 (2.63%) |
| Positions value | $18,096.34 |
| Settled cash | $1,868.39 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.19% | 2.45% |
| Annualized volatility | 11.39% | 11.63% |
| Sharpe (rf 4%) | -0.38 | 0.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 52 | 52 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $199.43 | $797.72 | $30.60 | $179.57 |
| BBY | 8 | $101.21 | $92.90 | $743.20 | $-66.48 | $85.09 |
| CNC | 16 | $71.60 | $65.11 | $1,041.68 | $-103.94 | $59.53 |
| CRL | 3 | $296.67 | $277.64 | $832.92 | $-57.10 | $256.69 |
| GEN | 40 | $29.13 | $29.01 | $1,160.40 | $-4.86 | $26.22 |
| IQV | 2 | $255.46 | $266.56 | $533.13 | $22.22 | $244.26 |
| MPC | 3 | $306.56 | $424.59 | $1,273.77 | $354.09 | $382.13 |
| NTAP | 5 | $206.27 | $197.73 | $988.65 | $-42.70 | $179.40 |
| PSX | 5 | $215.50 | $273.20 | $1,366.02 | $288.54 | $246.58 |
| RVTY | 9 | $122.75 | $143.40 | $1,290.56 | $185.84 | $132.06 |
| SPY | 5 | $743.10 | $762.63 | $3,813.15 | $97.65 | — |
| TECH | 12 | $72.32 | $72.40 | $868.80 | $0.96 | $65.20 |
| TGT | 7 | $162.82 | $158.16 | $1,107.12 | $-32.59 | $147.91 |
| VLO | 3 | $304.72 | $413.02 | $1,239.06 | $324.90 | $371.72 |
| ZBRA | 3 | $345.13 | $346.72 | $1,040.16 | $4.78 | $313.44 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,107.74 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-18T22:46` system **SPY** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-18T22:46` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
