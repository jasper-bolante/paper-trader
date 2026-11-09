# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-09 23:06 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,345.62** |
| Total return since inception | -3.27% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,301.94 (1.51%) |
| Positions value | $12,201.52 |
| Settled cash | $7,154.38 |
| Unsettled cash (T+1) | $5.38 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.34% | 1.33% |
| Annualized volatility | 12.59% | 14.35% |
| Sharpe (rf 4%) | -1.04 | 0.06 |
| Max drawdown | 7.86% | 6.06% |
| EOD observations | 88 | 88 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $113.14 | $1,131.40 | $71.92 | $101.83 |
| MPC | 2 | $428.77 | $389.78 | $779.56 | $-77.99 | $351.03 |
| PSX | 4 | $274.37 | $253.18 | $1,012.72 | $-84.74 | $233.77 |
| RVTY | 9 | $122.75 | $160.74 | $1,446.66 | $341.94 | $149.17 |
| SPY | 5 | $743.10 | $752.72 | $3,763.60 | $48.10 | — |
| TECH | 12 | $72.32 | $72.81 | $873.78 | $5.94 | $65.53 |
| VEEV | 4 | $305.03 | $306.36 | $1,225.44 | $5.32 | $279.52 |
| WDAY | 6 | $194.97 | $190.28 | $1,141.68 | $-28.12 | $181.66 |
| WST | 2 | $370.69 | $413.34 | $826.68 | $85.30 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,110.84 | $0.00 | $1,512.22 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-07T00:14` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
