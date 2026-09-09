# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-09 22:42 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,565.75** |
| Total return since inception | -2.17% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,516.22 (2.58%) |
| Positions value | $16,947.02 |
| Settled cash | $1,127.31 |
| Unsettled cash (T+1) | $1,502.04 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.24% | 2.40% |
| Annualized volatility | 11.07% | 11.84% |
| Sharpe (rf 4%) | -1.48 | 0.87 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 45 | 45 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 24 | $27.11 | $24.40 | $585.60 | $-64.93 | $22.38 |
| CRL | 2 | $285.12 | $278.51 | $557.02 | $-13.22 | $268.70 |
| EXPE | 2 | $303.37 | $272.59 | $545.18 | $-61.56 | $249.03 |
| HUM | 2 | $426.49 | $401.11 | $802.22 | $-50.75 | $371.57 |
| IQV | 2 | $255.46 | $257.00 | $514.00 | $3.09 | $244.26 |
| MPC | 3 | $306.56 | $399.51 | $1,198.53 | $278.85 | $359.56 |
| NTAP | 5 | $206.27 | $184.65 | $923.25 | $-108.10 | $170.20 |
| PAYX | 8 | $115.18 | $114.77 | $918.16 | $-3.29 | $103.61 |
| PSX | 5 | $215.50 | $260.85 | $1,304.25 | $226.77 | $234.77 |
| RVTY | 9 | $122.75 | $123.90 | $1,115.10 | $10.38 | $111.51 |
| SPY | 5 | $743.10 | $762.28 | $3,811.40 | $95.90 | — |
| STT | 8 | $185.86 | $191.92 | $1,535.36 | $48.49 | $174.87 |
| TECH | 12 | $72.32 | $72.26 | $867.12 | $-0.72 | $65.20 |
| TGT | 7 | $162.82 | $157.59 | $1,103.13 | $-36.58 | $147.91 |
| VLO | 3 | $304.72 | $388.90 | $1,166.70 | $252.54 | $350.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,071.35 | $0.00 | $921.91 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-09T19:58` no_trade — no signals crossed action thresholds this hour
- `2026-09-09T19:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-09-09T17:14` entry buy **PAYX** — momentum entry: rank 13, mom 0.297, vol 31%
- `2026-09-09T17:14` entry buy **RVTY** — momentum entry: rank 12, mom 0.313, vol 31%
- `2026-09-09T17:14` exit sell **HPE** — momentum rank decayed (None > 150 or ineligible: volatility 0.567446032372815 above cap 0.5)
- `2026-09-09T17:14` exit sell **FDS** — trailing stop 10%
- `2026-09-08T20:10` system — eod_complete
- `2026-09-08T17:23` entry buy **BAX** — momentum entry: rank 13, mom 0.337, vol 42%
- `2026-09-08T17:23` entry buy **EXPE** — momentum entry: rank 5, mom 0.493, vol 49%
- `2026-09-08T17:23` no_trade skip_entry **DASH** — insufficient investable cash (size $615, need >= $500)
- `2026-09-08T17:23` exit sell **FTNT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-08T17:23` exit sell **DASH** — trailing stop 10%
- `2026-09-08T17:23` exit sell **BAX** — trailing stop 10%
- `2026-09-04T22:29` system — eod_complete
- `2026-09-04T19:49` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
