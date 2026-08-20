# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 16:01 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,732.50** |
| Total return since inception | -1.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $16,797.40 |
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
| BAX | 28 | $27.27 | $26.45 | $740.74 | $-22.87 | $25.00 |
| BBY | 14 | $88.05 | $86.69 | $1,213.66 | $-19.09 | $80.33 |
| CRL | 2 | $285.12 | $299.23 | $598.46 | $28.22 | $260.98 |
| CSX | 17 | $50.29 | $51.27 | $871.67 | $16.72 | $46.01 |
| EXPE | 2 | $331.47 | $326.52 | $653.04 | $-9.90 | $298.17 |
| IQV | 2 | $255.46 | $259.86 | $519.72 | $8.81 | $229.79 |
| MPC | 3 | $306.56 | $365.99 | $1,097.97 | $178.29 | $330.10 |
| NTAP | 5 | $161.48 | $196.05 | $980.25 | $172.87 | $186.39 |
| PANW | 2 | $388.28 | $352.57 | $705.14 | $-71.42 | $349.27 |
| PSX | 5 | $215.50 | $245.62 | $1,228.08 | $150.60 | $219.13 |
| SPY | 5 | $743.10 | $765.67 | $3,828.35 | $112.85 | — |
| STT | 8 | $185.86 | $185.31 | $1,482.48 | $-4.39 | $173.64 |
| VEEV | 3 | $250.82 | $252.35 | $757.05 | $4.58 | $225.62 |
| VLO | 3 | $304.72 | $348.13 | $1,044.40 | $130.25 | $315.01 |
| WST | 3 | $336.32 | $358.80 | $1,076.38 | $67.42 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
