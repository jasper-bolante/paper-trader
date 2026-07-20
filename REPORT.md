# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-20 17:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,909.19** |
| Total return since inception | -0.45% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,004.84 (0.02%) |
| Positions value | $18,411.55 |
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
| BEN | 42 | $33.14 | $32.40 | $1,360.59 | $-31.37 | $30.26 |
| CNC | 13 | $66.94 | $66.57 | $865.41 | $-4.83 | $61.84 |
| DDOG | 3 | $260.67 | $266.12 | $798.36 | $16.36 | $236.06 |
| DVA | 6 | $227.39 | $236.83 | $1,420.98 | $56.62 | $213.37 |
| FFIV | 3 | $430.59 | $416.64 | $1,249.92 | $-41.85 | $388.22 |
| FTNT | 5 | $155.14 | $162.95 | $814.75 | $39.07 | $150.16 |
| HUM | 2 | $401.64 | $397.37 | $794.74 | $-8.54 | $366.83 |
| IBKR | 10 | $95.61 | $92.42 | $924.20 | $-31.86 | $87.64 |
| MPC | 3 | $306.56 | $317.76 | $953.29 | $33.62 | $281.36 |
| NTAP | 5 | $161.48 | $163.75 | $818.75 | $11.37 | $147.36 |
| SPY | 5 | $743.10 | $744.72 | $3,723.60 | $8.10 | — |
| STT | 8 | $185.86 | $182.49 | $1,459.92 | $-26.95 | $168.04 |
| UNH | 3 | $425.21 | $421.10 | $1,263.30 | $-12.32 | $383.45 |
| URI | 1 | $1,090.35 | $1,019.48 | $1,019.48 | $-70.87 | $980.79 |
| VLO | 3 | $304.72 | $314.75 | $944.25 | $30.09 | $278.68 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T17:02` no_trade skip_entry **MNST** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **CSX** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **DOC** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **JBHT** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **CVS** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **WST** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **MGM** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T17:02` no_trade skip_entry **TRGP** — insufficient investable cash (size $485, need >= $500)
- `2026-07-20T15:30` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T15:30` no_trade skip_entry **MNST** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **CSX** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **DOC** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **JBHT** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **CVS** — insufficient investable cash (size $484, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
