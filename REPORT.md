# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-28 20:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,412.15** |
| Total return since inception | -2.94% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,937.96 (-0.31%) |
| Positions value | $15,611.18 |
| Settled cash | $992.69 |
| Unsettled cash (T+1) | $2,814.43 |
| Tax reserve | $6.16 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.01% | -0.49% |
| Annualized volatility | 9.09% | 10.53% |
| Sharpe (rf 4%) | -6.43 | -1.16 |
| Max drawdown | 3.62% | 2.21% |
| EOD observations | 15 | 15 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| DDOG | 3 | $260.67 | $251.04 | $753.12 | $-28.88 | $236.93 |
| DOC | 32 | $22.25 | $22.83 | $730.56 | $18.54 | $20.55 |
| DVA | 6 | $227.39 | $239.50 | $1,436.97 | $72.61 | $215.55 |
| HUM | 2 | $401.64 | $388.70 | $777.40 | $-25.88 | $366.83 |
| IBKR | 10 | $95.61 | $90.90 | $909.00 | $-47.06 | $87.64 |
| JBHT | 3 | $277.72 | $277.80 | $833.40 | $0.23 | $252.76 |
| MPC | 3 | $306.56 | $306.34 | $919.02 | $-0.66 | $287.83 |
| NTAP | 5 | $161.48 | $174.57 | $872.85 | $65.47 | $157.11 |
| PSX | 5 | $215.50 | $205.78 | $1,028.90 | $-48.58 | $191.32 |
| SPY | 5 | $743.10 | $740.79 | $3,703.97 | $-11.53 | — |
| STT | 8 | $185.86 | $182.59 | $1,460.76 | $-26.11 | $168.04 |
| UNH | 3 | $425.21 | $428.94 | $1,286.82 | $11.20 | $393.25 |
| VLO | 3 | $304.72 | $299.47 | $898.41 | $-15.75 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-586.37 | $0.00 | $0.00 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-28T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-07-28T17:58` no_trade skip_entry **CSX** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **BBY** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **ADM** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **TRV** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **CVS** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **FFIV** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **CNC** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **FTNT** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **CSX** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **BBY** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **ADM** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **TRV** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **CVS** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **FFIV** — insufficient investable cash (size $17, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
