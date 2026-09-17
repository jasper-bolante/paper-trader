# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-17 17:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,046.70** |
| Total return since inception | 0.23% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,294.71 (1.47%) |
| Positions value | $15,950.82 |
| Settled cash | $1,429.21 |
| Unsettled cash (T+1) | $2,679.72 |
| Tax reserve | $13.05 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.10% | 1.29% |
| Annualized volatility | 11.16% | 11.60% |
| Sharpe (rf 4%) | -0.82 | 0.28 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 50 | 50 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $199.19 | $796.76 | $29.64 | $177.94 |
| BBY | 8 | $101.21 | $94.17 | $753.32 | $-56.36 | $83.90 |
| CRL | 3 | $296.67 | $285.21 | $855.64 | $-34.38 | $256.69 |
| IQV | 2 | $255.46 | $270.50 | $541.00 | $30.09 | $244.26 |
| MPC | 3 | $306.56 | $421.89 | $1,265.67 | $345.99 | $372.01 |
| NTAP | 5 | $206.27 | $196.80 | $984.00 | $-47.35 | $179.40 |
| PSX | 5 | $215.50 | $272.03 | $1,360.15 | $282.67 | $238.47 |
| RVTY | 9 | $122.75 | $148.69 | $1,338.16 | $233.44 | $131.31 |
| SPY | 5 | $743.10 | $762.37 | $3,811.85 | $96.35 | — |
| TECH | 12 | $72.32 | $72.42 | $868.98 | $1.14 | $65.20 |
| TGT | 7 | $162.82 | $158.69 | $1,110.83 | $-28.88 | $147.91 |
| VLO | 3 | $304.72 | $409.88 | $1,229.62 | $315.47 | $363.00 |
| ZBRA | 3 | $345.13 | $344.94 | $1,034.82 | $-0.56 | $310.45 |

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
