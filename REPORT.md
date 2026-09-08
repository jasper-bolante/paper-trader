# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-08 17:23 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,618.13** |
| Total return since inception | -1.91% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,728.84 (3.64%) |
| Positions value | $16,466.33 |
| Settled cash | $1,012.13 |
| Unsettled cash (T+1) | $2,150.29 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.00% | 3.46% |
| Annualized volatility | 11.33% | 11.95% |
| Sharpe (rf 4%) | -1.37 | 1.43 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 43 | 43 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 24 | $27.11 | $24.82 | $595.56 | $-54.97 | $22.33 |
| CRL | 2 | $285.12 | $282.95 | $565.90 | $-4.34 | $268.70 |
| EXPE | 2 | $303.37 | $276.70 | $553.40 | $-53.34 | $249.03 |
| FDS | 2 | $299.76 | $290.72 | $581.44 | $-18.09 | $282.41 |
| HPE | 16 | $53.55 | $54.99 | $879.84 | $23.00 | $48.99 |
| HUM | 2 | $426.49 | $406.12 | $812.24 | $-40.73 | $371.57 |
| IQV | 2 | $255.46 | $263.15 | $526.31 | $15.40 | $244.26 |
| MPC | 3 | $306.56 | $395.90 | $1,187.70 | $268.02 | $350.35 |
| NTAP | 5 | $206.27 | $185.97 | $929.88 | $-101.47 | $167.03 |
| PSX | 5 | $215.50 | $258.68 | $1,293.40 | $215.92 | $230.41 |
| SPY | 5 | $743.10 | $767.52 | $3,837.62 | $122.12 | — |
| STT | 8 | $185.86 | $193.70 | $1,549.60 | $62.73 | $174.87 |
| TECH | 12 | $72.32 | $72.34 | $868.08 | $0.24 | $65.20 |
| TGT | 7 | $162.82 | $163.14 | $1,141.98 | $2.27 | $147.91 |
| VLO | 3 | $304.72 | $381.12 | $1,143.38 | $229.22 | $333.54 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,108.07 | $0.00 | $921.91 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-08T17:23` entry buy **BAX** — momentum entry: rank 13, mom 0.337, vol 42%
- `2026-09-08T17:23` entry buy **EXPE** — momentum entry: rank 5, mom 0.493, vol 49%
- `2026-09-08T17:23` no_trade skip_entry **DASH** — insufficient investable cash (size $615, need >= $500)
- `2026-09-08T17:23` exit sell **FTNT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-08T17:23` exit sell **DASH** — trailing stop 10%
- `2026-09-08T17:23` exit sell **BAX** — trailing stop 10%
- `2026-09-04T22:29` system — eod_complete
- `2026-09-04T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-04T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-09-04T16:59` entry buy **NTAP** — momentum entry: rank 3, mom 0.631, vol 35%
- `2026-09-03T20:04` system — eod_complete
- `2026-09-03T20:04` system — corporate_actions_synced
- `2026-09-03T17:08` entry buy **HUM** — momentum entry: rank 3, mom 0.749, vol 35%
- `2026-09-03T17:08` entry buy **HPE** — momentum entry: rank 1, mom 1.081, vol 49%
- `2026-09-03T17:08` exit sell **HPE** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
