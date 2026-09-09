# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-09 17:14 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,584.22** |
| Total return since inception | -2.08% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,617.95 (3.09%) |
| Positions value | $16,965.49 |
| Settled cash | $1,127.31 |
| Unsettled cash (T+1) | $1,502.04 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.98% | 2.91% |
| Annualized volatility | 11.19% | 11.90% |
| Sharpe (rf 4%) | -1.35 | 1.13 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 44 | 44 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 24 | $27.11 | $24.68 | $592.32 | $-58.21 | $22.38 |
| CRL | 2 | $285.12 | $277.52 | $555.04 | $-15.20 | $268.70 |
| EXPE | 2 | $303.37 | $272.63 | $545.26 | $-61.48 | $249.03 |
| HUM | 2 | $426.49 | $401.04 | $802.08 | $-50.89 | $371.57 |
| IQV | 2 | $255.46 | $255.05 | $510.10 | $-0.81 | $244.26 |
| MPC | 3 | $306.56 | $400.23 | $1,200.68 | $281.00 | $358.26 |
| NTAP | 5 | $206.27 | $186.26 | $931.30 | $-100.05 | $170.20 |
| PAYX | 8 | $115.18 | $115.12 | $920.96 | $-0.49 | $103.61 |
| PSX | 5 | $215.50 | $261.04 | $1,305.20 | $227.72 | $233.25 |
| RVTY | 9 | $122.75 | $122.68 | $1,104.12 | $-0.60 | $110.41 |
| SPY | 5 | $743.10 | $763.02 | $3,815.10 | $99.60 | — |
| STT | 8 | $185.86 | $193.16 | $1,545.28 | $58.41 | $174.87 |
| TECH | 12 | $72.32 | $72.30 | $867.60 | $-0.24 | $65.20 |
| TGT | 7 | $162.82 | $159.42 | $1,115.94 | $-23.77 | $147.91 |
| VLO | 3 | $304.72 | $384.84 | $1,154.52 | $240.36 | $345.00 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,071.35 | $0.00 | $921.91 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-04T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-09-04T16:59` entry buy **NTAP** — momentum entry: rank 3, mom 0.631, vol 35%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
