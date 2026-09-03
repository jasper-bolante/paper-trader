# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-03 17:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,702.58** |
| Total return since inception | -1.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,594.81 (2.97%) |
| Positions value | $16,614.88 |
| Settled cash | $1,130.86 |
| Unsettled cash (T+1) | $1,967.46 |
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
| BAX | 28 | $27.27 | $25.47 | $713.16 | $-50.45 | $25.00 |
| CRL | 2 | $285.12 | $289.35 | $578.69 | $8.45 | $268.70 |
| DASH | 4 | $228.34 | $223.29 | $893.16 | $-20.18 | $205.31 |
| FDS | 2 | $299.76 | $311.00 | $622.00 | $22.47 | $282.41 |
| FTNT | 4 | $170.05 | $157.67 | $630.68 | $-49.51 | $139.07 |
| HPE | 16 | $53.55 | $50.02 | $800.32 | $-56.52 | $45.02 |
| HUM | 2 | $426.49 | $412.86 | $825.71 | $-27.26 | $371.57 |
| IQV | 2 | $255.46 | $267.41 | $534.82 | $23.91 | $237.58 |
| MPC | 3 | $306.56 | $392.08 | $1,176.24 | $256.56 | $348.52 |
| PSX | 5 | $215.50 | $258.52 | $1,292.60 | $215.12 | $230.41 |
| SPY | 5 | $743.10 | $772.60 | $3,863.00 | $147.50 | — |
| STT | 8 | $185.86 | $193.47 | $1,547.76 | $60.89 | $174.19 |
| TECH | 12 | $72.32 | $72.39 | $868.68 | $0.84 | $65.09 |
| TGT | 7 | $162.82 | $164.95 | $1,154.65 | $14.94 | $147.35 |
| VLO | 3 | $304.72 | $371.13 | $1,113.40 | $199.25 | $329.36 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,103.64 | $0.00 | $710.55 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-03T17:08` entry buy **HUM** — momentum entry: rank 3, mom 0.749, vol 35%
- `2026-09-03T17:08` entry buy **HPE** — momentum entry: rank 1, mom 1.081, vol 49%
- `2026-09-03T17:08` exit sell **HPE** — trailing stop 10%
- `2026-09-03T17:08` exit sell **NTAP** — trailing stop 10%
- `2026-09-03T17:08` exit sell **EXPE** — trailing stop 10%
- `2026-09-02T20:03` system — eod_complete
- `2026-09-02T17:16` entry buy **FTNT** — momentum entry: rank 7, mom 0.595, vol 48%
- `2026-09-02T17:16` entry buy **HPE** — momentum entry: rank 1, mom 1.022, vol 50%
- `2026-09-02T17:16` no_trade skip_entry **HUM** — insufficient investable cash (size $771, need >= $500)
- `2026-09-02T17:16` exit sell **CSX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-02T17:16` exit sell **FTNT** — trailing stop 10%
- `2026-09-01T20:07` system — eod_complete
- `2026-09-01T20:07` system **TGT** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-01T20:07` system — corporate_actions_synced
- `2026-09-01T17:25` entry buy **DASH** — momentum entry: rank 12, mom 0.410, vol 41%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
