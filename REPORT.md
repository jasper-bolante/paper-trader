# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-24 20:48 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,531.71** |
| Total return since inception | -2.34% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,870.54 (-0.65%) |
| Positions value | $16,985.61 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $1,176.06 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.41% | -0.82% |
| Annualized volatility | 9.74% | 11.33% |
| Sharpe (rf 4%) | -5.62 | -1.83 |
| Max drawdown | 3.03% | 2.21% |
| EOD observations | 13 | 13 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $63.40 | $824.13 | $-46.11 | $61.84 |
| DDOG | 3 | $260.67 | $246.71 | $740.13 | $-41.87 | $236.93 |
| DVA | 6 | $227.39 | $235.33 | $1,411.98 | $47.62 | $213.53 |
| FTNT | 5 | $155.14 | $152.38 | $761.90 | $-13.78 | $150.16 |
| HUM | 2 | $401.64 | $388.90 | $777.80 | $-25.48 | $366.83 |
| IBKR | 10 | $95.61 | $91.77 | $917.70 | $-38.36 | $87.64 |
| MPC | 3 | $306.56 | $309.18 | $927.54 | $7.86 | $287.83 |
| NTAP | 5 | $161.48 | $167.80 | $839.00 | $31.62 | $151.02 |
| PSX | 5 | $215.50 | $206.78 | $1,033.90 | $-43.58 | $191.32 |
| SPY | 5 | $743.10 | $738.29 | $3,691.45 | $-24.05 | — |
| STT | 8 | $185.86 | $185.45 | $1,483.60 | $-3.27 | $168.04 |
| TRGP | 5 | $282.92 | $281.42 | $1,407.10 | $-7.51 | $256.96 |
| UNH | 3 | $425.21 | $420.67 | $1,262.00 | $-13.62 | $393.25 |
| VLO | 3 | $304.72 | $302.46 | $907.38 | $-6.78 | $283.28 |

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
