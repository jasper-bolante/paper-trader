# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 15:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,745.74** |
| Total return since inception | -1.27% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $16,810.64 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $1,586.68 |
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
| BAX | 28 | $27.27 | $26.46 | $740.88 | $-22.73 | $25.00 |
| BBY | 14 | $88.05 | $87.09 | $1,219.33 | $-13.42 | $80.33 |
| CRL | 2 | $285.12 | $297.28 | $594.56 | $24.32 | $260.98 |
| CSX | 17 | $50.29 | $51.42 | $874.14 | $19.19 | $46.01 |
| EXPE | 2 | $331.47 | $325.88 | $651.75 | $-11.19 | $298.17 |
| IQV | 2 | $255.46 | $257.56 | $515.12 | $4.21 | $229.79 |
| MPC | 3 | $306.56 | $363.84 | $1,091.52 | $171.84 | $330.10 |
| NTAP | 5 | $161.48 | $196.30 | $981.50 | $174.12 | $186.39 |
| PANW | 2 | $388.28 | $355.64 | $711.28 | $-65.28 | $349.27 |
| PSX | 5 | $215.50 | $245.05 | $1,225.25 | $147.77 | $219.13 |
| SPY | 5 | $743.10 | $767.20 | $3,836.00 | $120.50 | — |
| STT | 8 | $185.86 | $187.66 | $1,501.28 | $14.41 | $173.64 |
| VEEV | 3 | $250.82 | $251.28 | $753.84 | $1.37 | $225.62 |
| VLO | 3 | $304.72 | $347.68 | $1,043.04 | $128.88 | $315.01 |
| WST | 3 | $336.32 | $357.05 | $1,071.15 | $62.19 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-20T14:09` exit sell **FTNT** — trailing stop 10%
- `2026-08-19T20:56` system — eod_complete
- `2026-08-19T20:56` system — corporate_actions_synced
- `2026-08-19T19:51` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T19:51` no_trade skip_entry **WSM** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **NUE** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **APA** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TGT** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **BKNG** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TECH** — insufficient investable cash (size $374, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
