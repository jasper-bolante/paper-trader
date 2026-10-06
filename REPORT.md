# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-06 23:11 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,274.76** |
| Total return since inception | 1.37% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,973.22 (4.87%) |
| Positions value | $17,169.85 |
| Settled cash | $1,341.92 |
| Unsettled cash (T+1) | $1,777.46 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.30% | 4.68% |
| Annualized volatility | 11.13% | 11.25% |
| Sharpe (rf 4%) | 0.16 | 1.33 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 64 | 64 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $215.43 | $861.72 | $94.60 | $193.89 |
| APA | 19 | $44.15 | $44.11 | $838.09 | $-0.80 | $39.73 |
| CRL | 3 | $296.67 | $305.38 | $916.14 | $26.12 | $279.86 |
| FFIV | 2 | $448.44 | $470.10 | $940.20 | $43.31 | $423.09 |
| IQV | 2 | $255.46 | $259.90 | $519.80 | $8.89 | $247.54 |
| MPC | 3 | $399.06 | $432.44 | $1,297.31 | $100.13 | $390.17 |
| NTAP | 5 | $206.27 | $228.45 | $1,142.25 | $110.90 | $205.60 |
| PSX | 5 | $215.50 | $269.74 | $1,348.70 | $271.22 | $246.58 |
| RVTY | 9 | $122.75 | $153.37 | $1,380.33 | $275.61 | $141.67 |
| SPY | 5 | $743.10 | $779.26 | $3,896.30 | $180.80 | — |
| TECH | 12 | $72.32 | $72.44 | $869.28 | $1.44 | $65.36 |
| VLO | 3 | $392.61 | $419.26 | $1,257.78 | $79.96 | $377.45 |
| WST | 2 | $370.69 | $372.98 | $745.95 | $4.57 | $339.09 |
| ZBRA | 3 | $345.13 | $385.33 | $1,156.00 | $120.62 | $346.80 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-06T19:00` no_trade skip_entry **WAT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **TMO** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **MSFT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **A** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **PLTR** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **WDAY** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **FTNT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **MU** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` exit sell **TGT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-10-06T19:00` exit sell **BBY** — trailing stop 10%
- `2026-10-06T01:43` system — eod_complete
- `2026-10-02T23:11` system — eod_complete
- `2026-10-02T18:39` no_trade — no signals crossed action thresholds this hour
- `2026-10-02T18:39` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-01T23:22` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
