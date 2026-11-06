# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-06 20:03 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,114.74** |
| Total return since inception | -4.43% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,703.17 (-1.48%) |
| Positions value | $11,970.65 |
| Settled cash | $6,410.16 |
| Unsettled cash (T+1) | $749.60 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -4.46% | -1.66% |
| Annualized volatility | 12.52% | 13.92% |
| Sharpe (rf 4%) | -1.34 | -0.57 |
| Max drawdown | 7.74% | 6.06% |
| EOD observations | 86 | 86 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $110.08 | $1,100.80 | $41.32 | $100.89 |
| MPC | 2 | $428.77 | $373.70 | $747.41 | $-110.14 | $351.03 |
| PSX | 4 | $274.37 | $246.77 | $987.08 | $-110.38 | $233.77 |
| RVTY | 9 | $122.75 | $156.12 | $1,405.08 | $300.36 | $149.17 |
| SPY | 5 | $743.10 | $737.91 | $3,689.57 | $-25.93 | — |
| TECH | 12 | $72.32 | $72.76 | $873.12 | $5.28 | $65.47 |
| VEEV | 4 | $305.03 | $300.98 | $1,203.90 | $-16.22 | $279.52 |
| WDAY | 6 | $194.97 | $194.35 | $1,166.10 | $-3.70 | $181.66 |
| WST | 2 | $370.69 | $398.79 | $797.58 | $56.20 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,110.84 | $0.00 | $1,512.22 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-06T20:03` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-06T20:03` exit sell **IT** — trailing stop 10%
- `2026-11-06T01:29` system — eod_complete
- `2026-11-06T01:29` system — corporate_actions_synced
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
