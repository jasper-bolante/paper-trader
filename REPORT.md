# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-11 19:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,602.42** |
| Total return since inception | -1.99% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,397.52 (1.99%) |
| Positions value | $17,431.35 |
| Settled cash | $1,043.36 |
| Unsettled cash (T+1) | $1,138.33 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.12% | 1.81% |
| Annualized volatility | 11.13% | 11.80% |
| Sharpe (rf 4%) | -1.90 | 0.57 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 46 | 46 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CRL | 2 | $285.12 | $277.81 | $555.62 | $-14.62 | $268.70 |
| FDS | 3 | $293.49 | $259.60 | $778.80 | $-101.66 | $253.30 |
| HUM | 2 | $426.49 | $408.59 | $817.18 | $-35.79 | $371.57 |
| INCY | 6 | $122.55 | $121.55 | $729.27 | $-6.00 | $110.18 |
| IQV | 2 | $255.46 | $262.05 | $524.10 | $13.19 | $244.26 |
| MPC | 3 | $306.56 | $396.35 | $1,189.05 | $269.37 | $359.56 |
| NTAP | 5 | $206.27 | $199.09 | $995.43 | $-35.92 | $170.20 |
| PAYX | 8 | $115.18 | $115.81 | $926.52 | $5.07 | $103.66 |
| PSX | 5 | $215.50 | $259.64 | $1,298.20 | $220.72 | $234.77 |
| RVTY | 9 | $122.75 | $124.37 | $1,119.33 | $14.61 | $111.51 |
| SPY | 5 | $743.10 | $764.54 | $3,822.70 | $107.20 | — |
| STT | 8 | $185.86 | $193.27 | $1,546.16 | $59.29 | $174.87 |
| TECH | 12 | $72.32 | $72.17 | $865.98 | $-1.86 | $65.20 |
| TGT | 7 | $162.82 | $155.75 | $1,090.25 | $-49.46 | $147.91 |
| VLO | 3 | $304.72 | $390.92 | $1,172.76 | $258.60 | $350.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,160.54 | $0.00 | $957.59 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-11T19:58` no_trade — no signals crossed action thresholds this hour
- `2026-09-11T19:58` no_trade skip_entry **NUE** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **CF** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **ADP** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **GEN** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **GPN** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **GPC** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **MRK** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **APA** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T17:08` entry buy **INCY** — momentum entry: rank 12, mom 0.309, vol 27%
- `2026-09-11T17:08` no_trade skip_entry **NUE** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **CF** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **ADP** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **GEN** — insufficient investable cash (size $51, need >= $500)
- `2026-09-11T17:08` no_trade skip_entry **GPN** — insufficient investable cash (size $51, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
