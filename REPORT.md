# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-05 01:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,581.68** |
| Total return since inception | -2.09% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,684.39 (3.42%) |
| Positions value | $13,181.80 |
| Settled cash | $3,838.26 |
| Unsettled cash (T+1) | $2,577.28 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.16% | 3.24% |
| Annualized volatility | 11.93% | 11.29% |
| Sharpe (rf 4%) | -0.82 | 0.55 |
| Max drawdown | 5.72% | 3.57% |
| EOD observations | 85 | 85 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $112.11 | $1,121.05 | $61.57 | $100.89 |
| IT | 4 | $220.40 | $207.08 | $828.32 | $-53.27 | $186.37 |
| MPC | 2 | $428.77 | $390.03 | $780.06 | $-77.49 | $351.03 |
| PSX | 4 | $274.37 | $259.74 | $1,038.96 | $-58.50 | $233.77 |
| RVTY | 9 | $122.75 | $159.47 | $1,435.23 | $330.51 | $149.17 |
| SPY | 5 | $743.10 | $766.90 | $3,834.50 | $119.00 | — |
| TECH | 12 | $72.32 | $72.74 | $872.88 | $5.04 | $65.47 |
| VEEV | 4 | $305.03 | $310.58 | $1,242.32 | $22.20 | $279.52 |
| WDAY | 6 | $194.97 | $201.85 | $1,211.10 | $41.30 | $181.66 |
| WST | 2 | $370.69 | $408.69 | $817.38 | $76.00 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-973.47 | $0.00 | $1,512.22 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-04T20:31` entry buy **PSX** — momentum entry: rank 5, mom 0.462, vol 35%
- `2026-11-04T20:31` entry buy **MPC** — momentum entry: rank 3, mom 0.643, vol 40%
- `2026-11-04T20:31` no_trade skip_entry **HUM** — insufficient investable cash (size $870, need >= $500)
- `2026-11-04T20:31` exit sell **NTAP** — momentum rank decayed (None > 150 or ineligible: volatility 0.5383352861062571 above cap 0.5)
- `2026-11-04T20:31` exit sell **PSX** — trailing stop 10%
- `2026-11-04T20:31` exit sell **MPC** — trailing stop 10%
- `2026-11-04T00:48` system — eod_complete
- `2026-11-04T00:48` system — corporate_actions_synced
- `2026-11-03T20:14` entry buy **IT** — momentum entry: rank 6, mom 0.518, vol 44%
- `2026-11-03T20:14` entry buy **VEEV** — momentum entry: rank 2, mom 0.782, vol 31%
- `2026-11-03T20:14` exit sell **IQV** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-03T20:14` exit sell **CRL** — momentum rank decayed (None > 150 or ineligible: volatility 0.5135575388287749 above cap 0.5)
- `2026-11-03T20:14` exit sell **IT** — trailing stop 10%
- `2026-11-03T20:14` exit sell **PLTR** — trailing stop 10%
- `2026-11-03T20:14` exit sell **APA** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
