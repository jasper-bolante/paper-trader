# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-05 20:47 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,155.69** |
| Total return since inception | -4.22% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,684.39 (3.42%) |
| Positions value | $12,755.81 |
| Settled cash | $6,410.16 |
| Unsettled cash (T+1) | $5.38 |
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
| EL | 10 | $105.95 | $108.71 | $1,087.10 | $27.62 | $100.89 |
| IT | 4 | $220.40 | $195.67 | $782.68 | $-98.91 | $186.37 |
| MPC | 2 | $428.77 | $381.89 | $763.78 | $-93.77 | $351.03 |
| PSX | 4 | $274.37 | $249.74 | $998.96 | $-98.50 | $233.77 |
| RVTY | 9 | $122.75 | $151.34 | $1,362.06 | $257.34 | $149.17 |
| SPY | 5 | $743.10 | $735.26 | $3,676.30 | $-39.20 | — |
| TECH | 12 | $72.32 | $72.73 | $872.76 | $4.92 | $65.47 |
| VEEV | 4 | $305.03 | $307.67 | $1,230.68 | $10.56 | $279.52 |
| WDAY | 6 | $194.97 | $198.72 | $1,192.35 | $22.55 | $181.66 |
| WST | 2 | $370.69 | $394.57 | $789.14 | $47.76 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-973.47 | $0.00 | $1,512.22 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-05T20:47` no_trade — no signals crossed action thresholds this hour
- `2026-11-05T20:47` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-05T20:47` system — drawdown_state
- `2026-11-05T01:00` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
