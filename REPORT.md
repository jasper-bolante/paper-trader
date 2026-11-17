# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-17 21:52 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,944.33** |
| Total return since inception | -5.28% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,777.07 (-1.11%) |
| Positions value | $8,895.24 |
| Settled cash | $10,058.75 |
| Unsettled cash (T+1) | $6.23 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -5.34% | -1.29% |
| Annualized volatility | 12.30% | 14.45% |
| Sharpe (rf 4%) | -1.47 | -0.45 |
| Max drawdown | 8.60% | 6.06% |
| EOD observations | 94 | 94 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $104.51 | $1,045.10 | $-14.38 | $102.06 |
| RVTY | 9 | $122.75 | $147.78 | $1,330.02 | $225.30 | $149.17 |
| SPY | 5 | $743.10 | $733.26 | $3,666.30 | $-49.20 | — |
| TECH | 12 | $72.32 | $72.65 | $871.80 | $3.96 | $65.55 |
| VEEV | 4 | $305.03 | $288.49 | $1,153.96 | $-66.16 | $279.52 |
| WST | 2 | $370.69 | $414.03 | $828.06 | $86.68 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-16T22:59` system — eod_complete
- `2026-11-14T01:24` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
