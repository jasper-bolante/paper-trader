# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-16 17:42 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,899.78** |
| Total return since inception | -0.50% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,391.87 (1.96%) |
| Positions value | $16,582.19 |
| Settled cash | $1,083.84 |
| Unsettled cash (T+1) | $2,245.65 |
| Tax reserve | $11.90 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.48% | 1.78% |
| Annualized volatility | 11.24% | 11.67% |
| Sharpe (rf 4%) | -1.00 | 0.51 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 49 | 49 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $198.42 | $793.68 | $26.56 | $173.50 |
| BBY | 8 | $101.21 | $92.69 | $741.52 | $-68.16 | $83.90 |
| FDS | 3 | $293.49 | $274.63 | $823.89 | $-56.57 | $253.30 |
| GPC | 8 | $132.94 | $132.15 | $1,057.20 | $-6.33 | $119.77 |
| HUM | 2 | $426.49 | $387.77 | $775.55 | $-77.42 | $371.57 |
| IQV | 2 | $255.46 | $272.81 | $545.62 | $34.71 | $244.26 |
| MPC | 3 | $306.56 | $418.15 | $1,254.45 | $334.77 | $369.56 |
| NTAP | 5 | $206.27 | $193.74 | $968.68 | $-62.67 | $179.40 |
| PSX | 5 | $215.50 | $266.24 | $1,331.20 | $253.72 | $238.47 |
| RVTY | 9 | $122.75 | $146.24 | $1,316.16 | $211.44 | $126.15 |
| SPY | 5 | $743.10 | $759.52 | $3,797.60 | $82.10 | — |
| TECH | 12 | $72.32 | $72.30 | $867.60 | $-0.24 | $65.20 |
| TGT | 7 | $162.82 | $155.94 | $1,091.58 | $-48.13 | $147.91 |
| VLO | 3 | $304.72 | $405.82 | $1,217.46 | $303.30 | $357.42 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,094.73 | $0.00 | $1,021.65 |

Dividends received: $79.33. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-16T17:42` no_trade skip_entry **GEN** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **MET** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **CNC** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **APA** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **MRK** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **NUE** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **GPN** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` no_trade skip_entry **CRL** — insufficient investable cash (size $77, need >= $500)
- `2026-09-16T17:42` exit sell **STT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-16T17:42` exit sell **INCY** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-15T21:41` system — eod_complete
- `2026-09-15T17:44` entry buy **BBY** — momentum entry: rank 13, mom 0.308, vol 41%
- `2026-09-15T17:44` entry buy **ANET** — momentum entry: rank 11, mom 0.357, vol 49%
- `2026-09-15T17:44` no_trade skip_entry **CRL** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T22:42` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
