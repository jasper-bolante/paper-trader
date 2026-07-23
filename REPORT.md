# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-23 18:47 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,576.06** |
| Total return since inception | -2.12% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,148.03 (0.74%) |
| Positions value | $18,192.13 |
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
| CNC | 13 | $66.94 | $63.95 | $831.35 | $-38.89 | $61.84 |
| DDOG | 3 | $260.67 | $244.25 | $732.75 | $-49.25 | $236.93 |
| DVA | 6 | $227.39 | $233.32 | $1,399.92 | $35.56 | $213.53 |
| FFIV | 3 | $430.59 | $390.32 | $1,170.96 | $-120.81 | $388.22 |
| FTNT | 5 | $155.14 | $151.77 | $758.85 | $-16.83 | $150.16 |
| HUM | 2 | $401.64 | $390.17 | $780.34 | $-22.94 | $366.83 |
| IBKR | 10 | $95.61 | $91.33 | $913.30 | $-42.76 | $87.64 |
| MPC | 3 | $306.56 | $314.43 | $943.29 | $23.61 | $287.83 |
| NTAP | 5 | $161.48 | $164.58 | $822.90 | $15.52 | $149.88 |
| PSX | 5 | $215.50 | $208.94 | $1,044.72 | $-32.76 | $191.32 |
| SPY | 5 | $743.10 | $737.28 | $3,686.40 | $-29.10 | — |
| STT | 8 | $185.86 | $184.73 | $1,477.84 | $-9.03 | $168.04 |
| TRGP | 5 | $282.92 | $286.21 | $1,431.07 | $16.46 | $255.94 |
| UNH | 3 | $425.21 | $424.28 | $1,272.84 | $-2.78 | $393.25 |
| VLO | 3 | $304.72 | $308.53 | $925.59 | $11.43 | $283.28 |

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
