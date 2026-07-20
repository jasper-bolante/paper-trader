# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-20 15:30 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,923.90** |
| Total return since inception | -0.38% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,004.84 (0.02%) |
| Positions value | $18,426.26 |
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
| BEN | 42 | $33.14 | $32.52 | $1,365.84 | $-26.12 | $30.26 |
| CNC | 13 | $66.94 | $66.55 | $865.15 | $-5.09 | $61.84 |
| DDOG | 3 | $260.67 | $264.02 | $792.06 | $10.06 | $236.06 |
| DVA | 6 | $227.39 | $237.17 | $1,423.02 | $58.66 | $213.37 |
| FFIV | 3 | $430.59 | $414.57 | $1,243.71 | $-48.06 | $388.22 |
| FTNT | 5 | $155.14 | $162.40 | $812.00 | $36.32 | $150.16 |
| HUM | 2 | $401.64 | $399.69 | $799.38 | $-3.90 | $366.83 |
| IBKR | 10 | $95.61 | $92.96 | $929.60 | $-26.46 | $87.64 |
| MPC | 3 | $306.56 | $317.10 | $951.30 | $31.62 | $281.36 |
| NTAP | 5 | $161.48 | $163.41 | $817.05 | $9.67 | $147.36 |
| SPY | 5 | $743.10 | $745.86 | $3,729.28 | $13.78 | — |
| STT | 8 | $185.86 | $182.75 | $1,462.00 | $-24.87 | $168.04 |
| UNH | 3 | $425.21 | $422.39 | $1,267.18 | $-8.43 | $383.45 |
| URI | 1 | $1,090.35 | $1,027.53 | $1,027.53 | $-62.82 | $980.79 |
| VLO | 3 | $304.72 | $313.72 | $941.16 | $27.00 | $278.68 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-20T15:30` no_trade — no signals crossed action thresholds this hour
- `2026-07-20T15:30` no_trade skip_entry **MNST** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **CSX** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **DOC** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **JBHT** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **CVS** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **WST** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **MGM** — insufficient investable cash (size $484, need >= $500)
- `2026-07-20T15:30` no_trade skip_entry **TRGP** — insufficient investable cash (size $484, need >= $500)
- `2026-07-17T20:28` system — eod_complete
- `2026-07-17T20:28` system — corporate_actions_synced
- `2026-07-17T18:36` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T18:36` no_trade skip_entry **DAL** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MGM** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MNST** — insufficient investable cash (size $488, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
