# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-01 17:25 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,604.06** |
| Total return since inception | -1.98% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,639.75 (3.20%) |
| Positions value | $17,088.47 |
| Settled cash | $1,733.37 |
| Unsettled cash (T+1) | $791.63 |
| Tax reserve | $9.41 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.25% | 3.02% |
| Annualized volatility | 11.60% | 12.09% |
| Sharpe (rf 4%) | -1.01 | 1.36 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 39 | 39 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.91 | $725.62 | $-37.99 | $25.00 |
| CRL | 2 | $285.12 | $282.78 | $565.56 | $-4.68 | $268.70 |
| CSX | 17 | $50.29 | $47.91 | $814.38 | $-40.57 | $46.58 |
| DASH | 4 | $228.34 | $228.12 | $912.48 | $-0.86 | $205.31 |
| EXPE | 2 | $331.47 | $307.70 | $615.40 | $-47.54 | $305.24 |
| FDS | 2 | $299.76 | $308.90 | $617.80 | $18.27 | $282.41 |
| FTNT | 5 | $171.82 | $161.71 | $808.55 | $-50.53 | $154.62 |
| IQV | 2 | $255.46 | $258.62 | $517.25 | $6.34 | $235.96 |
| MPC | 3 | $306.56 | $379.67 | $1,139.01 | $219.33 | $336.02 |
| NTAP | 4 | $187.95 | $179.64 | $718.56 | $-33.23 | $174.52 |
| PSX | 5 | $215.50 | $250.44 | $1,252.22 | $174.74 | $222.14 |
| SPY | 5 | $743.10 | $761.62 | $3,808.10 | $92.60 | — |
| STT | 8 | $185.86 | $187.10 | $1,496.80 | $9.93 | $174.19 |
| TECH | 12 | $72.32 | $72.22 | $866.64 | $-1.20 | $65.09 |
| TGT | 7 | $162.82 | $162.73 | $1,139.11 | $-0.60 | $146.46 |
| VLO | 3 | $304.72 | $363.66 | $1,090.98 | $176.82 | $323.20 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-930.09 | $0.00 | $554.53 |

Dividends received: $62.71. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-01T17:25` entry buy **DASH** — momentum entry: rank 12, mom 0.410, vol 41%
- `2026-09-01T17:25` entry buy **TGT** — momentum entry: rank 10, mom 0.426, vol 31%
- `2026-09-01T17:25` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-01T00:02` system — eod_complete
- `2026-09-01T00:02` system **TECH** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T00:02` system — corporate_actions_synced
- `2026-08-31T19:35` entry buy **TECH** — momentum entry: rank 11, mom 0.392, vol 4%
- `2026-08-31T19:35` entry buy **FTNT** — momentum entry: rank 7, mom 0.552, vol 45%
- `2026-08-31T19:35` exit sell **VEEV** — momentum rank decayed (None > 150 or ineligible: volatility 0.5791043137848686 above cap 0.5)
- `2026-08-31T19:35` exit sell **PANW** — momentum rank decayed (None > 150 or ineligible: volatility 0.55859509743112 above cap 0.5)
- `2026-08-31T19:35` exit sell **BBY** — trailing stop 10%
- `2026-08-31T19:35` system **FDS** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-31T19:35` system **CSX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-28T23:10` system — eod_complete
- `2026-08-28T23:10` system **BAX** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
