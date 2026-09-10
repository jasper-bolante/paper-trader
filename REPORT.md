# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-10 17:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,554.15** |
| Total return since inception | -2.23% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,516.22 (2.58%) |
| Positions value | $17,780.20 |
| Settled cash | $1,778.63 |
| Unsettled cash (T+1) | $5.94 |
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
| BAX | 24 | $27.11 | $24.11 | $578.64 | $-71.89 | $22.38 |
| CRL | 2 | $285.12 | $273.62 | $547.24 | $-23.00 | $268.70 |
| EXPE | 2 | $303.37 | $282.66 | $565.32 | $-41.42 | $249.03 |
| FDS | 3 | $293.49 | $281.44 | $844.32 | $-36.14 | $253.30 |
| HUM | 2 | $426.49 | $403.46 | $806.92 | $-46.05 | $371.57 |
| IQV | 2 | $255.46 | $258.26 | $516.52 | $5.61 | $244.26 |
| MPC | 3 | $306.56 | $399.36 | $1,198.08 | $278.40 | $359.56 |
| NTAP | 5 | $206.27 | $185.78 | $928.92 | $-102.42 | $170.20 |
| PAYX | 8 | $115.18 | $115.35 | $922.80 | $1.35 | $103.61 |
| PSX | 5 | $215.50 | $261.93 | $1,309.65 | $232.17 | $234.77 |
| RVTY | 9 | $122.75 | $122.00 | $1,098.00 | $-6.72 | $111.51 |
| SPY | 5 | $743.10 | $759.02 | $3,795.10 | $79.60 | — |
| STT | 8 | $185.86 | $191.69 | $1,533.52 | $46.65 | $174.87 |
| TECH | 12 | $72.32 | $72.27 | $867.18 | $-0.66 | $65.20 |
| TGT | 7 | $162.82 | $157.04 | $1,099.28 | $-40.43 | $147.91 |
| VLO | 3 | $304.72 | $389.57 | $1,168.71 | $254.55 | $350.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,035.67 | $0.00 | $957.59 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-10T17:07` entry buy **FDS** — momentum entry: rank 13, mom 0.282, vol 42%
- `2026-09-10T17:07` no_trade skip_entry **INCY** — sector cap: Health Care would exceed 25% of equity
- `2026-09-09T22:42` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
