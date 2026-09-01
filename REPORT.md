# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-01 20:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,625.32** |
| Total return since inception | -1.87% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,505.99 (2.53%) |
| Positions value | $17,102.82 |
| Settled cash | $1,741.49 |
| Unsettled cash (T+1) | $791.63 |
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
| BAX | 28 | $27.27 | $25.48 | $713.44 | $-50.17 | $25.00 |
| CRL | 2 | $285.12 | $282.31 | $564.62 | $-5.62 | $268.70 |
| CSX | 17 | $50.29 | $48.71 | $828.07 | $-26.88 | $46.58 |
| DASH | 4 | $228.34 | $225.58 | $902.32 | $-11.02 | $205.31 |
| EXPE | 2 | $331.47 | $304.21 | $608.42 | $-54.52 | $305.24 |
| FDS | 2 | $299.76 | $304.49 | $608.98 | $9.45 | $282.41 |
| FTNT | 5 | $171.82 | $161.79 | $808.97 | $-50.11 | $154.62 |
| IQV | 2 | $255.46 | $258.39 | $516.78 | $5.87 | $235.96 |
| MPC | 3 | $306.56 | $382.74 | $1,148.22 | $228.54 | $344.47 |
| NTAP | 4 | $187.95 | $183.10 | $732.42 | $-19.37 | $174.52 |
| PSX | 5 | $215.50 | $251.97 | $1,259.85 | $182.37 | $226.77 |
| SPY | 5 | $743.10 | $761.90 | $3,809.50 | $94.00 | — |
| STT | 8 | $185.86 | $187.79 | $1,502.32 | $15.45 | $174.19 |
| TECH | 12 | $72.32 | $72.19 | $866.34 | $-1.50 | $65.09 |
| TGT | 7 | $162.82 | $163.72 | $1,146.04 | $6.33 | $147.35 |
| VLO | 3 | $304.72 | $362.18 | $1,086.53 | $172.37 | $325.96 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-930.09 | $0.00 | $554.53 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-01T20:07` system **TGT** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T20:07` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
