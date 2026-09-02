# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-02 20:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,731.39** |
| Total return since inception | -1.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,594.81 (2.97%) |
| Positions value | $16,978.35 |
| Settled cash | $1,156.42 |
| Unsettled cash (T+1) | $1,607.24 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.41% | 2.79% |
| Annualized volatility | 11.52% | 11.95% |
| Sharpe (rf 4%) | -1.07 | 1.18 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 41 | 41 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.70 | $719.60 | $-44.01 | $25.00 |
| CRL | 2 | $285.12 | $291.61 | $583.22 | $12.98 | $268.70 |
| DASH | 4 | $228.34 | $226.21 | $904.84 | $-8.50 | $205.31 |
| EXPE | 2 | $331.47 | $308.06 | $616.12 | $-46.82 | $305.24 |
| FDS | 2 | $299.76 | $306.25 | $612.49 | $12.96 | $282.41 |
| FTNT | 4 | $170.05 | $154.52 | $618.08 | $-62.11 | $139.07 |
| HPE | 15 | $50.38 | $51.84 | $777.60 | $21.88 | $46.66 |
| IQV | 2 | $255.46 | $263.98 | $527.96 | $17.05 | $237.58 |
| MPC | 3 | $306.56 | $387.24 | $1,161.72 | $242.04 | $348.52 |
| NTAP | 4 | $187.95 | $180.57 | $722.28 | $-29.51 | $174.52 |
| PSX | 5 | $215.50 | $256.01 | $1,280.05 | $202.57 | $230.41 |
| SPY | 5 | $743.10 | $765.20 | $3,826.00 | $110.50 | — |
| STT | 8 | $185.86 | $189.93 | $1,519.44 | $32.57 | $174.19 |
| TECH | 12 | $72.32 | $72.31 | $867.72 | $-0.12 | $65.09 |
| TGT | 7 | $162.82 | $163.34 | $1,143.38 | $3.67 | $147.35 |
| VLO | 3 | $304.72 | $365.95 | $1,097.85 | $183.69 | $329.36 |

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
