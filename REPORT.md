# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-14 01:24 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,230.40** |
| Total return since inception | -3.85% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,284.95 (1.42%) |
| Positions value | $9,181.31 |
| Settled cash | $10,058.75 |
| Unsettled cash (T+1) | $6.23 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.91% | 1.25% |
| Annualized volatility | 12.33% | 14.28% |
| Sharpe (rf 4%) | -1.16 | 0.03 |
| Max drawdown | 7.86% | 6.06% |
| EOD observations | 92 | 92 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $111.68 | $1,116.80 | $57.32 | $102.06 |
| RVTY | 9 | $122.75 | $154.54 | $1,390.86 | $286.14 | $149.17 |
| SPY | 5 | $743.10 | $752.09 | $3,760.45 | $44.95 | — |
| TECH | 12 | $72.32 | $72.79 | $873.48 | $5.64 | $65.55 |
| VEEV | 4 | $305.03 | $301.68 | $1,206.72 | $-13.40 | $279.52 |
| WST | 2 | $370.69 | $416.50 | $833.00 | $91.62 | $374.85 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-13T20:37` no_trade — no signals crossed action thresholds this hour
- `2026-11-13T20:37` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-13T20:37` system **TECH** — cash settles on pay date; 15% dividend tax reserved
- `2026-11-12T21:01` system — eod_complete
- `2026-11-12T01:58` system — eod_complete
- `2026-11-11T00:51` system — eod_complete
- `2026-11-10T20:34` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-10T20:34` exit sell **WDAY** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:34` exit sell **PSX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:34` exit sell **MPC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-10T20:33` system **WST** — cash settles on pay date; 15% dividend tax reserved
- `2026-11-09T23:07` system — eod_complete
- `2026-11-07T00:14` system — eod_complete
- `2026-11-06T20:03` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-06T20:03` exit sell **IT** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
