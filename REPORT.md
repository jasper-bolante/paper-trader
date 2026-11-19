# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-19 21:43 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,731.60** |
| Total return since inception | -6.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,321.80 (-3.39%) |
| Positions value | $8,682.51 |
| Settled cash | $10,059.27 |
| Unsettled cash (T+1) | $5.71 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -6.41% | -3.56% |
| Annualized volatility | 12.25% | 14.63% |
| Sharpe (rf 4%) | -1.70 | -0.86 |
| Max drawdown | 9.63% | 7.87% |
| EOD observations | 96 | 96 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $101.78 | $1,017.85 | $-41.63 | $102.06 |
| RVTY | 9 | $122.75 | $151.62 | $1,364.62 | $259.90 | $149.17 |
| SPY | 5 | $743.10 | $716.38 | $3,581.90 | $-133.60 | — |
| TECH | 12 | $72.32 | $72.70 | $872.40 | $4.56 | $65.55 |
| VEEV | 4 | $305.03 | $263.00 | $1,052.00 | $-168.12 | $279.52 |
| WST | 2 | $370.69 | $396.87 | $793.74 | $52.36 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-11-10T20:33` system **WST** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
