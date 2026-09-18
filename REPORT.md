# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-18 17:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,937.24** |
| Total return since inception | -0.31% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,522.41 (2.61%) |
| Positions value | $18,065.44 |
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
| ANET | 4 | $191.78 | $198.53 | $794.10 | $26.98 | $179.57 |
| BBY | 8 | $101.21 | $93.65 | $749.20 | $-60.48 | $85.09 |
| CNC | 16 | $71.60 | $66.14 | $1,058.24 | $-87.38 | $59.53 |
| CRL | 3 | $296.67 | $277.45 | $832.35 | $-57.67 | $256.69 |
| GEN | 40 | $29.13 | $29.13 | $1,165.20 | $-0.06 | $26.22 |
| IQV | 2 | $255.46 | $265.96 | $531.92 | $21.01 | $244.26 |
| MPC | 3 | $306.56 | $422.50 | $1,267.49 | $347.81 | $380.05 |
| NTAP | 5 | $206.27 | $195.00 | $975.00 | $-56.35 | $179.40 |
| PSX | 5 | $215.50 | $272.20 | $1,361.00 | $283.52 | $246.58 |
| RVTY | 9 | $122.75 | $144.13 | $1,297.17 | $192.45 | $132.06 |
| SPY | 5 | $743.10 | $759.38 | $3,796.90 | $81.40 | — |
| TECH | 12 | $72.32 | $72.31 | $867.72 | $-0.12 | $65.20 |
| TGT | 7 | $162.82 | $157.85 | $1,104.95 | $-34.76 | $147.91 |
| VLO | 3 | $304.72 | $409.92 | $1,229.75 | $315.59 | $371.22 |
| ZBRA | 3 | $345.13 | $344.82 | $1,034.46 | $-0.92 | $313.44 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,107.74 | $0.00 | $1,142.35 |

Dividends received: $87.01. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-16T17:42` no_trade skip_entry **APA** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **MRK** — insufficient investable cash (size $77, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
