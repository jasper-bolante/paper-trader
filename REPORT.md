# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-11 22:44 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,603.71** |
| Total return since inception | -1.98% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,568.43 (2.84%) |
| Positions value | $17,432.64 |
| Settled cash | $1,043.36 |
| Unsettled cash (T+1) | $1,138.33 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.05% | 2.66% |
| Annualized volatility | 11.35% | 11.81% |
| Sharpe (rf 4%) | -1.30 | 0.94 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 47 | 47 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CRL | 2 | $285.12 | $278.08 | $556.16 | $-14.08 | $268.70 |
| FDS | 3 | $293.49 | $259.66 | $778.98 | $-101.48 | $253.30 |
| HUM | 2 | $426.49 | $409.86 | $819.72 | $-33.25 | $371.57 |
| INCY | 6 | $122.55 | $121.47 | $728.82 | $-6.45 | $110.18 |
| IQV | 2 | $255.46 | $262.02 | $524.04 | $13.13 | $244.26 |
| MPC | 3 | $306.56 | $395.96 | $1,187.88 | $268.20 | $359.56 |
| NTAP | 5 | $206.27 | $199.33 | $996.65 | $-34.70 | $179.40 |
| PAYX | 8 | $115.18 | $115.78 | $926.24 | $4.79 | $104.20 |
| PSX | 5 | $215.50 | $259.54 | $1,297.70 | $220.22 | $234.77 |
| RVTY | 9 | $122.75 | $124.41 | $1,119.69 | $14.97 | $111.97 |
| SPY | 5 | $743.10 | $764.22 | $3,821.10 | $105.60 | — |
| STT | 8 | $185.86 | $193.48 | $1,547.84 | $60.97 | $174.87 |
| TECH | 12 | $72.32 | $72.13 | $865.56 | $-2.28 | $65.20 |
| TGT | 7 | $162.82 | $155.81 | $1,090.67 | $-49.04 | $147.91 |
| VLO | 3 | $304.72 | $390.53 | $1,171.59 | $257.43 | $351.48 |

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
