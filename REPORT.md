# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-01 00:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,762.96** |
| Total return since inception | -1.19% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,639.75 (3.20%) |
| Positions value | $15,976.05 |
| Settled cash | $1,038.54 |
| Unsettled cash (T+1) | $2,757.78 |
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
| BAX | 28 | $27.27 | $26.00 | $728.00 | $-35.61 | $25.00 |
| CRL | 2 | $285.12 | $288.94 | $577.89 | $7.65 | $268.70 |
| CSX | 17 | $50.29 | $50.49 | $858.33 | $3.38 | $46.58 |
| EXPE | 2 | $331.47 | $317.11 | $634.22 | $-28.72 | $305.24 |
| FDS | 2 | $299.76 | $313.79 | $627.57 | $28.04 | $282.41 |
| FTNT | 5 | $171.82 | $170.90 | $854.50 | $-4.58 | $154.62 |
| HUM | 2 | $406.24 | $384.24 | $768.48 | $-43.99 | $357.63 |
| IQV | 2 | $255.46 | $261.34 | $522.68 | $11.77 | $235.96 |
| MPC | 3 | $306.56 | $373.36 | $1,120.08 | $200.40 | $336.02 |
| NTAP | 4 | $187.95 | $185.25 | $741.00 | $-10.79 | $174.52 |
| PSX | 5 | $215.50 | $246.82 | $1,234.10 | $156.62 | $222.14 |
| SPY | 5 | $743.10 | $766.87 | $3,834.35 | $118.85 | — |
| STT | 8 | $185.86 | $191.21 | $1,529.68 | $42.81 | $174.19 |
| TECH | 12 | $72.32 | $72.32 | $867.84 | $-0.00 | $65.09 |
| VLO | 3 | $304.72 | $359.11 | $1,077.33 | $163.17 | $323.20 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-899.35 | $0.00 | $554.53 |

Dividends received: $62.71. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-27T23:02` system — eod_complete
- `2026-08-27T23:02` system **EXPE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — corporate_actions_synced
- `2026-08-26T21:00` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
