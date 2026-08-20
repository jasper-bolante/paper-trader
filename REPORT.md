# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 19:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,545.23** |
| Total return since inception | -2.27% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $15,912.00 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $2,284.80 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.50% | 3.32% |
| Annualized volatility | 12.28% | 13.14% |
| Sharpe (rf 4%) | -1.30 | 1.85 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 31 | 31 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.36 | $737.94 | $-25.67 | $25.00 |
| BBY | 14 | $88.05 | $85.69 | $1,199.73 | $-33.02 | $80.33 |
| CRL | 2 | $285.12 | $292.38 | $584.76 | $14.52 | $260.98 |
| CSX | 17 | $50.29 | $50.96 | $866.32 | $11.37 | $46.01 |
| EXPE | 2 | $331.47 | $324.82 | $649.64 | $-13.30 | $298.17 |
| IQV | 2 | $255.46 | $256.77 | $513.55 | $2.64 | $229.79 |
| MPC | 3 | $306.56 | $358.95 | $1,076.85 | $157.17 | $330.10 |
| NTAP | 5 | $161.48 | $192.73 | $963.65 | $156.27 | $186.39 |
| PSX | 5 | $215.50 | $239.69 | $1,198.42 | $120.94 | $219.13 |
| SPY | 5 | $743.10 | $762.35 | $3,811.75 | $96.25 | — |
| STT | 8 | $185.86 | $183.41 | $1,467.28 | $-19.59 | $173.64 |
| VEEV | 3 | $250.82 | $250.35 | $751.05 | $-1.42 | $225.62 |
| VLO | 3 | $304.72 | $341.92 | $1,025.75 | $111.59 | $315.01 |
| WST | 3 | $336.32 | $355.11 | $1,065.32 | $56.36 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,136.32 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T19:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
