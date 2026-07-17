# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-17 20:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,856.79** |
| Total return since inception | -0.72% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,004.84 (0.02%) |
| Positions value | $18,359.15 |
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
| BEN | 42 | $33.14 | $32.63 | $1,370.46 | $-21.50 | $30.26 |
| CNC | 13 | $66.94 | $66.42 | $863.46 | $-6.78 | $61.84 |
| DDOG | 3 | $260.67 | $258.73 | $776.19 | $-5.81 | $236.06 |
| DVA | 6 | $227.39 | $237.07 | $1,422.45 | $58.09 | $213.37 |
| FFIV | 3 | $430.59 | $409.19 | $1,227.59 | $-64.18 | $388.22 |
| FTNT | 5 | $155.14 | $161.60 | $808.02 | $32.35 | $150.16 |
| HUM | 2 | $401.64 | $400.21 | $800.43 | $-2.85 | $366.83 |
| IBKR | 10 | $95.61 | $90.50 | $905.05 | $-51.01 | $87.64 |
| MPC | 3 | $306.56 | $312.62 | $937.86 | $18.18 | $281.36 |
| NTAP | 5 | $161.48 | $163.73 | $818.65 | $11.27 | $147.36 |
| SPY | 5 | $743.10 | $743.28 | $3,716.40 | $0.90 | — |
| STT | 8 | $185.86 | $182.53 | $1,460.24 | $-26.63 | $168.04 |
| UNH | 3 | $425.21 | $426.06 | $1,278.16 | $2.55 | $383.45 |
| URI | 1 | $1,090.35 | $1,045.26 | $1,045.26 | $-45.09 | $980.79 |
| VLO | 3 | $304.72 | $309.64 | $928.92 | $14.76 | $278.68 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-17T20:28` system — corporate_actions_synced
- `2026-07-17T18:36` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T18:36` no_trade skip_entry **DAL** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MGM** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **MNST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **CVS** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **DOC** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **WST** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **JBHT** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T18:36` no_trade skip_entry **TRGP** — insufficient investable cash (size $488, need >= $500)
- `2026-07-17T16:42` no_trade — no signals crossed action thresholds this hour
- `2026-07-17T16:42` no_trade skip_entry **DAL** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MGM** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **MNST** — insufficient investable cash (size $489, need >= $500)
- `2026-07-17T16:42` no_trade skip_entry **CVS** — insufficient investable cash (size $489, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
