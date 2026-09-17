# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-17 21:39 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,060.81** |
| Total return since inception | 0.30% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,522.41 (2.61%) |
| Positions value | $15,964.93 |
| Settled cash | $1,429.21 |
| Unsettled cash (T+1) | $2,679.72 |
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
| ANET | 4 | $191.78 | $199.53 | $798.10 | $30.98 | $179.57 |
| BBY | 8 | $101.21 | $94.55 | $756.40 | $-53.28 | $85.09 |
| CRL | 3 | $296.67 | $282.03 | $846.09 | $-43.93 | $256.69 |
| IQV | 2 | $255.46 | $269.41 | $538.82 | $27.91 | $244.26 |
| MPC | 3 | $306.56 | $422.28 | $1,266.84 | $347.16 | $380.05 |
| NTAP | 5 | $206.27 | $197.11 | $985.55 | $-45.80 | $179.40 |
| PSX | 5 | $215.50 | $273.98 | $1,369.90 | $292.42 | $246.58 |
| RVTY | 9 | $122.75 | $146.74 | $1,320.62 | $215.90 | $132.06 |
| SPY | 5 | $743.10 | $762.51 | $3,812.55 | $97.05 | — |
| TECH | 12 | $72.32 | $72.42 | $869.10 | $1.26 | $65.20 |
| TGT | 7 | $162.82 | $159.82 | $1,118.74 | $-20.97 | $147.91 |
| VLO | 3 | $304.72 | $412.47 | $1,237.41 | $323.25 | $371.22 |
| ZBRA | 3 | $345.13 | $348.27 | $1,044.81 | $9.43 | $313.44 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,194.54 | $0.00 | $1,055.55 |

Dividends received: $87.01. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-16T17:42` no_trade skip_entry **APA** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **MRK** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **NUE** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **GPN** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **CRL** — insufficient investable cash (size $77, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
