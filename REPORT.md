# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-23 17:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,593.17** |
| Total return since inception | -2.03% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,148.03 (0.74%) |
| Positions value | $18,209.24 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $13.89 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.14% | 0.56% |
| Annualized volatility | 9.37% | 10.55% |
| Sharpe (rf 4%) | -3.47 | 1.01 |
| Max drawdown | 1.77% | 1.73% |
| EOD observations | 11 | 11 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $63.82 | $829.66 | $-40.58 | $61.84 |
| DDOG | 3 | $260.67 | $243.77 | $731.31 | $-50.69 | $236.93 |
| DVA | 6 | $227.39 | $232.34 | $1,394.01 | $29.65 | $213.53 |
| FFIV | 3 | $430.59 | $393.85 | $1,181.55 | $-110.22 | $388.22 |
| FTNT | 5 | $155.14 | $151.59 | $757.98 | $-17.70 | $150.16 |
| HUM | 2 | $401.64 | $391.58 | $783.16 | $-20.12 | $366.83 |
| IBKR | 10 | $95.61 | $91.22 | $912.20 | $-43.86 | $87.64 |
| MPC | 3 | $306.56 | $313.77 | $941.32 | $21.64 | $287.83 |
| NTAP | 5 | $161.48 | $166.80 | $834.00 | $26.62 | $149.88 |
| PSX | 5 | $215.50 | $209.67 | $1,048.35 | $-29.13 | $191.32 |
| SPY | 5 | $743.10 | $738.59 | $3,692.95 | $-22.55 | — |
| STT | 8 | $185.86 | $185.17 | $1,481.36 | $-5.51 | $168.04 |
| TRGP | 5 | $282.92 | $285.90 | $1,429.50 | $14.89 | $255.94 |
| UNH | 3 | $425.21 | $422.15 | $1,266.45 | $-9.17 | $393.25 |
| VLO | 3 | $304.72 | $308.48 | $925.44 | $11.28 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-23T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T17:02` no_trade skip_entry **MNST** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **CSX** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **DOC** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **BNY** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **MGM** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **BBY** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **WST** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T17:02` no_trade skip_entry **CVS** — insufficient investable cash (size $390, need >= $500)
- `2026-07-23T15:34` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T15:34` no_trade skip_entry **MNST** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **CSX** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **DOC** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **BNY** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **MGM** — insufficient investable cash (size $389, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
