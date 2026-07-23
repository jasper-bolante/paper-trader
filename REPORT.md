# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-23 20:38 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,555.83** |
| Total return since inception | -2.22% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,889.92 (-0.55%) |
| Positions value | $18,171.90 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $13.89 |
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
| CNC | 13 | $66.94 | $63.72 | $828.36 | $-41.88 | $61.84 |
| DDOG | 3 | $260.67 | $244.43 | $733.29 | $-48.71 | $236.93 |
| DVA | 6 | $227.39 | $234.24 | $1,405.44 | $41.08 | $213.53 |
| FFIV | 3 | $430.59 | $388.03 | $1,164.09 | $-127.68 | $388.22 |
| FTNT | 5 | $155.14 | $151.48 | $757.40 | $-18.28 | $150.16 |
| HUM | 2 | $401.64 | $394.51 | $789.02 | $-14.26 | $366.83 |
| IBKR | 10 | $95.61 | $91.74 | $917.40 | $-38.66 | $87.64 |
| MPC | 3 | $306.56 | $312.24 | $936.72 | $17.04 | $287.83 |
| NTAP | 5 | $161.48 | $164.60 | $823.00 | $15.62 | $149.88 |
| PSX | 5 | $215.50 | $206.92 | $1,034.60 | $-42.88 | $191.32 |
| SPY | 5 | $743.10 | $739.01 | $3,695.05 | $-20.45 | — |
| STT | 8 | $185.86 | $184.18 | $1,473.44 | $-13.43 | $168.04 |
| TRGP | 5 | $282.92 | $285.51 | $1,427.55 | $12.94 | $256.96 |
| UNH | 3 | $425.21 | $423.52 | $1,270.57 | $-5.05 | $393.25 |
| VLO | 3 | $304.72 | $305.32 | $915.96 | $1.80 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-23T18:47` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T18:47` no_trade skip_entry **MNST** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **CSX** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **DOC** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **BNY** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **MGM** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **BBY** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **WST** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T18:47` no_trade skip_entry **CVS** — insufficient investable cash (size $391, need >= $500)
- `2026-07-23T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T17:02` no_trade skip_entry **MNST** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **CSX** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **DOC** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **BNY** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **MGM** — insufficient investable cash (size $390, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
