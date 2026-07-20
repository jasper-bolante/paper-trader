# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-20 19:14 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,844.92** |
| Total return since inception | -0.78% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,004.84 (0.02%) |
| Positions value | $18,347.28 |
| Settled cash | $1,486.06 |
| Unsettled cash (T+1) | $17.25 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.78% | -0.15% |
| Annualized volatility | 8.10% | 11.75% |
| Sharpe (rf 4%) | -3.95 | -0.76 |
| Max drawdown | 1.50% | 1.54% |
| EOD observations | 8 | 8 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $32.18 | $1,351.56 | $-40.40 | $30.26 |
| CNC | 13 | $66.94 | $66.47 | $864.11 | $-6.13 | $61.84 |
| DDOG | 3 | $260.67 | $263.91 | $791.73 | $9.73 | $236.06 |
| DVA | 6 | $227.39 | $235.71 | $1,414.23 | $49.87 | $213.37 |
| FFIV | 3 | $430.59 | $412.92 | $1,238.76 | $-53.01 | $388.22 |
| FTNT | 5 | $155.14 | $162.36 | $811.80 | $36.12 | $150.16 |
| HUM | 2 | $401.64 | $400.30 | $800.60 | $-2.68 | $366.83 |
| IBKR | 10 | $95.61 | $91.64 | $916.45 | $-39.61 | $87.64 |
| MPC | 3 | $306.56 | $317.49 | $952.46 | $32.78 | $281.36 |
| NTAP | 5 | $161.48 | $162.17 | $810.85 | $3.47 | $147.36 |
| SPY | 5 | $743.10 | $741.78 | $3,708.90 | $-6.60 | — |
| STT | 8 | $185.86 | $181.87 | $1,454.92 | $-31.95 | $168.04 |
| UNH | 3 | $425.21 | $423.23 | $1,269.68 | $-5.94 | $383.45 |
| URI | 1 | $1,090.35 | $1,016.50 | $1,016.50 | $-73.84 | $980.79 |
| VLO | 3 | $304.72 | $314.91 | $944.73 | $30.57 | $278.68 |

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
