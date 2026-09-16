# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-16 21:37 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,792.82** |
| Total return since inception | -1.04% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,294.71 (1.47%) |
| Positions value | $16,475.24 |
| Settled cash | $1,083.84 |
| Unsettled cash (T+1) | $2,245.65 |
| Tax reserve | $11.90 |

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
| ANET | 4 | $191.78 | $197.71 | $790.84 | $23.72 | $177.94 |
| BBY | 8 | $101.21 | $92.42 | $739.32 | $-70.36 | $83.90 |
| FDS | 3 | $293.49 | $276.31 | $828.93 | $-51.53 | $253.30 |
| GPC | 8 | $132.94 | $130.56 | $1,044.48 | $-19.05 | $119.77 |
| HUM | 2 | $426.49 | $384.81 | $769.61 | $-83.36 | $371.57 |
| IQV | 2 | $255.46 | $268.84 | $537.68 | $26.77 | $244.26 |
| MPC | 3 | $306.56 | $413.34 | $1,240.02 | $320.34 | $372.01 |
| NTAP | 5 | $206.27 | $191.50 | $957.52 | $-73.82 | $179.40 |
| PSX | 5 | $215.50 | $264.62 | $1,323.10 | $245.62 | $238.47 |
| RVTY | 9 | $122.75 | $145.90 | $1,313.10 | $208.38 | $131.31 |
| SPY | 5 | $743.10 | $754.05 | $3,770.25 | $54.75 | — |
| TECH | 12 | $72.32 | $72.32 | $867.84 | $-0.00 | $65.20 |
| TGT | 7 | $162.82 | $154.65 | $1,082.55 | $-57.16 | $147.91 |
| VLO | 3 | $304.72 | $403.33 | $1,209.99 | $295.83 | $363.00 |

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
