# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-10 20:34 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,285.22** |
| Total return since inception | -3.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,301.94 (1.51%) |
| Positions value | $9,236.94 |
| Settled cash | $7,154.38 |
| Unsettled cash (T+1) | $2,909.64 |
| Tax reserve | $15.74 |

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
| EL | 10 | $105.95 | $113.27 | $1,132.70 | $73.22 | $101.83 |
| RVTY | 9 | $122.75 | $159.35 | $1,434.15 | $329.43 | $149.17 |
| SPY | 5 | $743.10 | $749.27 | $3,746.35 | $30.85 | — |
| TECH | 12 | $72.32 | $72.81 | $873.78 | $5.94 | $65.53 |
| VEEV | 4 | $305.03 | $305.93 | $1,223.72 | $3.60 | $279.52 |
| WST | 2 | $370.69 | $413.12 | $826.24 | $84.86 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $104.95. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-10T20:34` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-10T20:34` exit sell **WDAY** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:34` exit sell **PSX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:34` exit sell **MPC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:33` system **WST** — cash settles on pay date; 15% dividend tax reserved
- `2026-11-09T23:07` system — eod_complete
- `2026-11-07T00:14` system — eod_complete
- `2026-11-06T20:03` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-06T20:03` exit sell **IT** — trailing stop 10%
- `2026-11-06T01:29` system — eod_complete
- `2026-11-06T01:29` system — corporate_actions_synced
- `2026-11-05T20:47` no_trade — no signals crossed action thresholds this hour
- `2026-11-05T20:47` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-05T20:47` system — drawdown_state
- `2026-11-05T01:00` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
