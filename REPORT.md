# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-09 19:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,576.87** |
| Total return since inception | -2.12% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,617.95 (3.09%) |
| Positions value | $16,958.14 |
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
| BAX | 24 | $27.11 | $24.47 | $587.28 | $-63.25 | $22.38 |
| CRL | 2 | $285.12 | $278.48 | $556.96 | $-13.28 | $268.70 |
| EXPE | 2 | $303.37 | $272.77 | $545.54 | $-61.20 | $249.03 |
| HUM | 2 | $426.49 | $400.96 | $801.92 | $-51.05 | $371.57 |
| IQV | 2 | $255.46 | $257.43 | $514.86 | $3.95 | $244.26 |
| MPC | 3 | $306.56 | $400.37 | $1,201.11 | $281.43 | $358.26 |
| NTAP | 5 | $206.27 | $184.55 | $922.75 | $-108.60 | $170.20 |
| PAYX | 8 | $115.18 | $114.79 | $918.32 | $-3.13 | $103.61 |
| PSX | 5 | $215.50 | $261.25 | $1,306.25 | $228.77 | $233.25 |
| RVTY | 9 | $122.75 | $124.21 | $1,117.89 | $13.17 | $110.41 |
| SPY | 5 | $743.10 | $762.26 | $3,811.30 | $95.80 | — |
| STT | 8 | $185.86 | $192.15 | $1,537.20 | $50.33 | $174.87 |
| TECH | 12 | $72.32 | $72.25 | $867.00 | $-0.84 | $65.20 |
| TGT | 7 | $162.82 | $157.58 | $1,103.06 | $-36.65 | $147.91 |
| VLO | 3 | $304.72 | $388.90 | $1,166.70 | $252.54 | $345.00 |

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
