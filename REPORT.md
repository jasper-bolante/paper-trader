# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-20 20:50 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,791.57** |
| Total return since inception | -1.04% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,966.36 (-0.17%) |
| Positions value | $18,293.93 |
| Settled cash | $1,486.06 |
| Unsettled cash (T+1) | $17.25 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.11% | -0.34% |
| Annualized volatility | 7.60% | 10.92% |
| Sharpe (rf 4%) | -5.11 | -1.31 |
| Max drawdown | 1.74% | 1.73% |
| EOD observations | 9 | 9 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $32.25 | $1,354.50 | $-37.46 | $30.26 |
| CNC | 13 | $66.94 | $65.86 | $856.18 | $-14.06 | $61.84 |
| DDOG | 3 | $260.67 | $263.26 | $789.78 | $7.78 | $236.93 |
| DVA | 6 | $227.39 | $234.07 | $1,404.42 | $40.06 | $213.37 |
| FFIV | 3 | $430.59 | $411.89 | $1,235.68 | $-56.09 | $388.22 |
| FTNT | 5 | $155.14 | $160.27 | $801.35 | $25.67 | $150.16 |
| HUM | 2 | $401.64 | $397.98 | $795.96 | $-7.32 | $366.83 |
| IBKR | 10 | $95.61 | $91.64 | $916.40 | $-39.66 | $87.64 |
| MPC | 3 | $306.56 | $315.32 | $945.96 | $26.28 | $283.79 |
| NTAP | 5 | $161.48 | $161.19 | $805.92 | $-1.46 | $147.36 |
| SPY | 5 | $743.10 | $741.85 | $3,709.25 | $-6.25 | — |
| STT | 8 | $185.86 | $182.46 | $1,459.68 | $-27.19 | $168.04 |
| UNH | 3 | $425.21 | $421.85 | $1,265.55 | $-10.07 | $383.45 |
| URI | 1 | $1,090.35 | $1,013.12 | $1,013.12 | $-77.23 | $980.79 |
| VLO | 3 | $304.72 | $313.39 | $940.17 | $26.01 | $282.05 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-20T19:14` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T19:14` no_trade skip_entry **MNST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **CSX** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **DOC** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **JBHT** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **CVS** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **WST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **MGM** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T19:14` no_trade skip_entry **TRGP** — insufficient investable cash (size $488, need >= $500)
- `2026-07-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T17:02` no_trade skip_entry **MNST** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **CSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **DOC** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **JBHT** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **CVS** — insufficient investable cash (size $485, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
