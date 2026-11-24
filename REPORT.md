# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-24 01:09 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,812.38** |
| Total return since inception | -5.94% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,512.22 (-2.44%) |
| Positions value | $8,763.28 |
| Settled cash | $10,064.98 |
| Unsettled cash (T+1) | $0.00 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -6.00% | -2.61% |
| Annualized volatility | 12.49% | 17.10% |
| Sharpe (rf 4%) | -1.54 | -0.55 |
| Max drawdown | 10.59% | 10.96% |
| EOD observations | 98 | 98 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $103.78 | $1,037.80 | $-21.68 | $102.06 |
| RVTY | 9 | $122.75 | $151.22 | $1,361.02 | $256.30 | $149.17 |
| SPY | 5 | $743.10 | $723.44 | $3,617.20 | $-98.30 | — |
| TECH | 12 | $72.32 | $72.84 | $874.08 | $6.24 | $65.56 |
| VEEV | 4 | $305.03 | $268.65 | $1,074.60 | $-145.52 | $279.52 |
| WST | 2 | $370.69 | $399.29 | $798.58 | $57.20 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-20T21:27` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
