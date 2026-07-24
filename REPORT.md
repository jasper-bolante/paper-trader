# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-24 17:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,565.40** |
| Total return since inception | -2.17% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,889.92 (-0.55%) |
| Positions value | $17,019.30 |
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
| CNC | 13 | $66.94 | $63.23 | $821.99 | $-48.25 | $61.84 |
| DDOG | 3 | $260.67 | $245.64 | $736.92 | $-45.08 | $236.93 |
| DVA | 6 | $227.39 | $235.86 | $1,415.16 | $50.80 | $213.53 |
| FTNT | 5 | $155.14 | $153.26 | $766.32 | $-9.36 | $150.16 |
| HUM | 2 | $401.64 | $391.10 | $782.20 | $-21.08 | $366.83 |
| IBKR | 10 | $95.61 | $91.66 | $916.60 | $-39.46 | $87.64 |
| MPC | 3 | $306.56 | $310.94 | $932.82 | $13.14 | $287.83 |
| NTAP | 5 | $161.48 | $167.48 | $837.40 | $30.02 | $149.88 |
| PSX | 5 | $215.50 | $207.32 | $1,036.60 | $-40.88 | $191.32 |
| SPY | 5 | $743.10 | $740.59 | $3,702.95 | $-12.55 | — |
| STT | 8 | $185.86 | $185.40 | $1,483.16 | $-3.71 | $168.04 |
| TRGP | 5 | $282.92 | $283.33 | $1,416.67 | $2.07 | $256.96 |
| UNH | 3 | $425.21 | $420.19 | $1,260.57 | $-15.05 | $393.25 |
| VLO | 3 | $304.72 | $303.31 | $909.93 | $-4.23 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-24T17:08` no_trade — no signals crossed action thresholds this hour
- `2026-07-24T17:08` no_trade skip_entry **MNST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **BBY** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **DOC** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **NUE** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **CSX** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **WST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **CVS** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **JBHT** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **MNST** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **BBY** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **DOC** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **NUE** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **CSX** — insufficient investable cash (size $388, need >= $500)
- `2026-07-24T15:14` no_trade skip_entry **WST** — insufficient investable cash (size $388, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
