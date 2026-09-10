# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-10 19:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,390.26** |
| Total return since inception | -3.05% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,516.22 (2.58%) |
| Positions value | $17,616.31 |
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
| BAX | 24 | $27.11 | $24.20 | $580.68 | $-69.85 | $22.38 |
| CRL | 2 | $285.12 | $272.75 | $545.50 | $-24.74 | $268.70 |
| EXPE | 2 | $303.37 | $276.79 | $553.57 | $-53.17 | $249.03 |
| FDS | 3 | $293.49 | $262.69 | $788.07 | $-92.39 | $253.30 |
| HUM | 2 | $426.49 | $400.33 | $800.66 | $-52.31 | $371.57 |
| IQV | 2 | $255.46 | $257.57 | $515.15 | $4.24 | $244.26 |
| MPC | 3 | $306.56 | $392.67 | $1,178.01 | $258.33 | $359.56 |
| NTAP | 5 | $206.27 | $183.56 | $917.80 | $-113.55 | $170.20 |
| PAYX | 8 | $115.18 | $115.19 | $921.52 | $0.07 | $103.61 |
| PSX | 5 | $215.50 | $258.44 | $1,292.20 | $214.72 | $234.77 |
| RVTY | 9 | $122.75 | $120.98 | $1,088.82 | $-15.90 | $111.51 |
| SPY | 5 | $743.10 | $757.78 | $3,788.90 | $73.40 | — |
| STT | 8 | $185.86 | $191.63 | $1,533.08 | $46.21 | $174.87 |
| TECH | 12 | $72.32 | $72.12 | $865.44 | $-2.40 | $65.20 |
| TGT | 7 | $162.82 | $155.78 | $1,090.42 | $-49.29 | $147.91 |
| VLO | 3 | $304.72 | $385.50 | $1,156.49 | $242.33 | $350.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,035.67 | $0.00 | $957.59 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-10T19:59` no_trade — no signals crossed action thresholds this hour
- `2026-09-10T19:59` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
