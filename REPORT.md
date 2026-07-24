# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-24 15:14 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,640.32** |
| Total return since inception | -1.80% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,889.92 (-0.55%) |
| Positions value | $17,094.22 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $1,176.06 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.29% | -0.73% |
| Annualized volatility | 10.21% | 11.88% |
| Sharpe (rf 4%) | -5.53 | -1.69 |
| Max drawdown | 2.91% | 2.11% |
| EOD observations | 12 | 12 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $63.62 | $827.00 | $-43.25 | $61.84 |
| DDOG | 3 | $260.67 | $244.43 | $733.29 | $-48.71 | $236.93 |
| DVA | 6 | $227.39 | $236.73 | $1,420.38 | $56.02 | $213.53 |
| FTNT | 5 | $155.14 | $153.57 | $767.85 | $-7.83 | $150.16 |
| HUM | 2 | $401.64 | $394.00 | $788.00 | $-15.28 | $366.83 |
| IBKR | 10 | $95.61 | $91.01 | $910.10 | $-45.96 | $87.64 |
| MPC | 3 | $306.56 | $314.62 | $943.88 | $24.20 | $287.83 |
| NTAP | 5 | $161.48 | $166.36 | $831.80 | $24.42 | $149.88 |
| PSX | 5 | $215.50 | $209.81 | $1,049.05 | $-28.43 | $191.32 |
| SPY | 5 | $743.10 | $741.99 | $3,709.95 | $-5.55 | — |
| STT | 8 | $185.86 | $185.43 | $1,483.40 | $-3.47 | $168.04 |
| TRGP | 5 | $282.92 | $288.53 | $1,442.65 | $28.04 | $256.96 |
| UNH | 3 | $425.21 | $422.72 | $1,268.16 | $-7.46 | $393.25 |
| VLO | 3 | $304.72 | $306.24 | $918.72 | $4.56 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-24T15:14` no_trade skip_entry **MNST** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **BBY** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **DOC** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **NUE** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **CSX** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **WST** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **CVS** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **JBHT** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` exit sell **FFIV** — trailing stop 10%
- `2026-07-23T20:38` system — eod_complete
- `2026-07-23T18:47` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T18:47` no_trade skip_entry **MNST** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **CSX** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **DOC** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **BNY** — insufficient investable cash (size $391, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
