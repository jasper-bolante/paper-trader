# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-24 19:01 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,557.36** |
| Total return since inception | -2.21% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,889.92 (-0.55%) |
| Positions value | $17,011.26 |
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
| CNC | 13 | $66.94 | $63.18 | $821.34 | $-48.90 | $61.84 |
| DDOG | 3 | $260.67 | $246.23 | $738.69 | $-43.31 | $236.93 |
| DVA | 6 | $227.39 | $235.76 | $1,414.56 | $50.20 | $213.53 |
| FTNT | 5 | $155.14 | $153.52 | $767.60 | $-8.08 | $150.16 |
| HUM | 2 | $401.64 | $391.27 | $782.54 | $-20.74 | $366.83 |
| IBKR | 10 | $95.61 | $91.19 | $911.90 | $-44.16 | $87.64 |
| MPC | 3 | $306.56 | $311.13 | $933.39 | $13.71 | $287.83 |
| NTAP | 5 | $161.48 | $167.45 | $837.25 | $29.87 | $149.88 |
| PSX | 5 | $215.50 | $207.86 | $1,039.30 | $-38.18 | $191.32 |
| SPY | 5 | $743.10 | $738.82 | $3,694.10 | $-21.40 | — |
| STT | 8 | $185.86 | $184.75 | $1,478.00 | $-8.87 | $168.04 |
| TRGP | 5 | $282.92 | $283.74 | $1,418.70 | $4.09 | $256.96 |
| UNH | 3 | $425.21 | $420.02 | $1,260.06 | $-15.56 | $393.25 |
| VLO | 3 | $304.72 | $304.61 | $913.83 | $-0.33 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-24T19:01` no_trade — no signals crossed action thresholds this hour
- `2026-07-24T19:01` no_trade skip_entry **MNST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **BBY** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **DOC** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **NUE** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **CSX** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **WST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **CVS** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **JBHT** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade — no signals crossed action thresholds this hour
- `2026-07-24T17:08` no_trade skip_entry **MNST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **BBY** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **DOC** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **NUE** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade skip_entry **CSX** — insufficient investable cash (size $392, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
