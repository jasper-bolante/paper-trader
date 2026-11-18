# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-18 21:31 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,902.66** |
| Total return since inception | -5.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,691.85 (-1.54%) |
| Positions value | $8,853.57 |
| Settled cash | $10,059.27 |
| Unsettled cash (T+1) | $5.71 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -5.55% | -1.71% |
| Annualized volatility | 12.24% | 14.39% |
| Sharpe (rf 4%) | -1.52 | -0.53 |
| Max drawdown | 8.80% | 6.11% |
| EOD observations | 95 | 95 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $104.05 | $1,040.45 | $-19.03 | $102.06 |
| RVTY | 9 | $122.75 | $152.50 | $1,372.50 | $267.78 | $149.17 |
| SPY | 5 | $743.10 | $730.10 | $3,650.50 | $-65.00 | — |
| TECH | 12 | $72.32 | $72.74 | $872.88 | $5.04 | $65.55 |
| VEEV | 4 | $305.03 | $277.23 | $1,108.92 | $-111.20 | $279.52 |
| WST | 2 | $370.69 | $404.16 | $808.32 | $66.94 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-11-10T20:33` system **WST** — cash settles on pay date; 15% dividend tax reserved
- `2026-11-09T23:07` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
