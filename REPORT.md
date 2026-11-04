# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-04 20:31 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,621.93** |
| Total return since inception | -1.89% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,344.28 (1.72%) |
| Positions value | $13,222.05 |
| Settled cash | $3,838.26 |
| Unsettled cash (T+1) | $2,577.28 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.36% | 1.54% |
| Annualized volatility | 12.00% | 10.98% |
| Sharpe (rf 4%) | -0.88 | 0.11 |
| Max drawdown | 5.72% | 3.57% |
| EOD observations | 84 | 84 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $112.68 | $1,126.80 | $67.32 | $98.41 |
| IT | 4 | $220.40 | $205.87 | $823.48 | $-58.11 | $184.00 |
| MPC | 2 | $428.77 | $386.33 | $772.66 | $-84.89 | $347.70 |
| PSX | 4 | $274.37 | $257.16 | $1,028.64 | $-68.82 | $231.44 |
| RVTY | 9 | $122.75 | $162.28 | $1,460.52 | $355.80 | $149.17 |
| SPY | 5 | $743.10 | $768.22 | $3,841.10 | $125.60 | — |
| TECH | 12 | $72.32 | $72.80 | $873.54 | $5.70 | $65.44 |
| VEEV | 4 | $305.03 | $312.69 | $1,250.76 | $30.64 | $274.35 |
| WDAY | 6 | $194.97 | $204.50 | $1,227.00 | $57.20 | $178.25 |
| WST | 2 | $370.69 | $408.77 | $817.55 | $76.17 | $374.59 |

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
