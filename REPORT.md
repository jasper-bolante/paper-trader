# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-02 17:16 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,720.33** |
| Total return since inception | -1.40% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,505.99 (2.53%) |
| Positions value | $16,967.28 |
| Settled cash | $1,156.42 |
| Unsettled cash (T+1) | $1,607.24 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.94% | 2.35% |
| Annualized volatility | 11.57% | 12.07% |
| Sharpe (rf 4%) | -1.38 | 0.97 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 40 | 40 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.88 | $724.50 | $-39.11 | $25.00 |
| CRL | 2 | $285.12 | $285.79 | $571.58 | $1.34 | $268.70 |
| DASH | 4 | $228.34 | $226.07 | $904.30 | $-9.04 | $205.31 |
| EXPE | 2 | $331.47 | $310.10 | $620.20 | $-42.74 | $305.24 |
| FDS | 2 | $299.76 | $304.12 | $608.24 | $8.71 | $282.41 |
| FTNT | 4 | $170.05 | $152.69 | $610.76 | $-69.43 | $137.42 |
| HPE | 15 | $50.38 | $50.38 | $755.70 | $-0.02 | $45.34 |
| IQV | 2 | $255.46 | $263.05 | $526.10 | $15.19 | $235.96 |
| MPC | 3 | $306.56 | $388.79 | $1,166.37 | $246.69 | $344.47 |
| NTAP | 4 | $187.95 | $183.85 | $735.40 | $-16.39 | $174.52 |
| PSX | 5 | $215.50 | $255.80 | $1,279.00 | $201.52 | $226.77 |
| SPY | 5 | $743.10 | $764.91 | $3,824.55 | $109.05 | — |
| STT | 8 | $185.86 | $190.03 | $1,520.28 | $33.41 | $174.19 |
| TECH | 12 | $72.32 | $72.34 | $868.08 | $0.24 | $65.09 |
| TGT | 7 | $162.82 | $165.00 | $1,155.03 | $15.32 | $147.35 |
| VLO | 3 | $304.72 | $365.73 | $1,097.19 | $183.03 | $325.96 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-977.67 | $0.00 | $623.64 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-02T17:16` entry buy **FTNT** — momentum entry: rank 7, mom 0.595, vol 48%
- `2026-09-02T17:16` entry buy **HPE** — momentum entry: rank 1, mom 1.022, vol 50%
- `2026-09-02T17:16` no_trade skip_entry **HUM** — insufficient investable cash (size $771, need >= $500)
- `2026-09-02T17:16` exit sell **CSX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-02T17:16` exit sell **FTNT** — trailing stop 10%
- `2026-09-01T20:07` system — eod_complete
- `2026-09-01T20:07` system **TGT** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T20:07` system — corporate_actions_synced
- `2026-09-01T17:25` entry buy **DASH** — momentum entry: rank 12, mom 0.410, vol 41%
- `2026-09-01T17:25` entry buy **TGT** — momentum entry: rank 10, mom 0.426, vol 31%
- `2026-09-01T17:25` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-01T00:02` system — eod_complete
- `2026-09-01T00:02` system **TECH** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T00:02` system — corporate_actions_synced
- `2026-08-31T19:35` entry buy **TECH** — momentum entry: rank 11, mom 0.392, vol 4%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
