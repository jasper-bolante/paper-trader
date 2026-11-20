# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-20 21:27 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,531.56** |
| Total return since inception | -7.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $18,673.67 (-6.63%) |
| Positions value | $8,482.47 |
| Settled cash | $10,059.27 |
| Unsettled cash (T+1) | $5.71 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -7.41% | -6.80% |
| Annualized volatility | 12.29% | 15.52% |
| Sharpe (rf 4%) | -1.91 | -1.37 |
| Max drawdown | 10.59% | 10.96% |
| EOD observations | 97 | 97 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $99.46 | $994.60 | $-64.88 | $102.06 |
| RVTY | 9 | $122.75 | $145.32 | $1,307.88 | $203.16 | $149.17 |
| SPY | 5 | $743.10 | $692.35 | $3,461.75 | $-253.75 | — |
| TECH | 12 | $72.32 | $72.69 | $872.28 | $4.44 | $65.55 |
| VEEV | 4 | $305.03 | $266.21 | $1,064.84 | $-155.28 | $279.52 |
| WST | 2 | $370.69 | $390.56 | $781.12 | $39.74 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-19T21:43` system — eod_complete
- `2026-11-18T21:31` system — eod_complete
- `2026-11-17T21:52` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
