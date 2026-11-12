# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-12 21:01 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,258.22** |
| Total return since inception | -3.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,421.69 (2.11%) |
| Positions value | $9,209.94 |
| Settled cash | $10,058.12 |
| Unsettled cash (T+1) | $5.90 |
| Tax reserve | $15.74 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.77% | 1.93% |
| Annualized volatility | 12.39% | 14.31% |
| Sharpe (rf 4%) | -1.13 | 0.17 |
| Max drawdown | 7.86% | 6.06% |
| EOD observations | 91 | 91 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $110.49 | $1,104.90 | $45.42 | $102.06 |
| RVTY | 9 | $122.75 | $156.98 | $1,412.82 | $308.10 | $149.17 |
| SPY | 5 | $743.10 | $757.16 | $3,785.80 | $70.30 | — |
| TECH | 12 | $72.32 | $72.83 | $873.96 | $6.12 | $65.55 |
| VEEV | 4 | $305.03 | $302.43 | $1,209.72 | $-10.40 | $279.52 |
| WST | 2 | $370.69 | $411.37 | $822.74 | $81.36 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $104.95. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-11-06T01:29` system — eod_complete
- `2026-11-06T01:29` system — corporate_actions_synced
- `2026-11-05T20:47` no_trade — no signals crossed action thresholds this hour
- `2026-11-05T20:47` no_trade skip_entry — no entries: drawdown state 'no_buys'

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
