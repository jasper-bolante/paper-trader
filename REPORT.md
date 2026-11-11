# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-11 00:51 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,285.76** |
| Total return since inception | -3.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,226.69 (1.13%) |
| Positions value | $9,237.48 |
| Settled cash | $7,154.38 |
| Unsettled cash (T+1) | $2,909.64 |
| Tax reserve | $15.74 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.64% | 0.96% |
| Annualized volatility | 12.52% | 14.28% |
| Sharpe (rf 4%) | -1.10 | -0.02 |
| Max drawdown | 7.86% | 6.06% |
| EOD observations | 89 | 89 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $113.40 | $1,134.00 | $74.52 | $102.06 |
| RVTY | 9 | $122.75 | $159.18 | $1,432.58 | $327.86 | $149.17 |
| SPY | 5 | $743.10 | $749.93 | $3,749.65 | $34.15 | — |
| TECH | 12 | $72.32 | $72.82 | $873.84 | $6.00 | $65.54 |
| VEEV | 4 | $305.03 | $305.51 | $1,222.04 | $1.92 | $279.52 |
| WST | 2 | $370.69 | $412.69 | $825.38 | $84.00 | $374.59 |

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
