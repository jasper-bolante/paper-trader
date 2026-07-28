# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-28 17:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,412.53** |
| Total return since inception | -2.94% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,885.61 (-0.57%) |
| Positions value | $15,611.57 |
| Settled cash | $992.69 |
| Unsettled cash (T+1) | $2,814.43 |
| Tax reserve | $6.16 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.48% | -0.75% |
| Annualized volatility | 9.34% | 10.87% |
| Sharpe (rf 4%) | -5.59 | -1.65 |
| Max drawdown | 3.10% | 2.21% |
| EOD observations | 14 | 14 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| DDOG | 3 | $260.67 | $251.69 | $755.07 | $-26.93 | $236.93 |
| DOC | 32 | $22.25 | $22.84 | $731.04 | $19.02 | $20.26 |
| DVA | 6 | $227.39 | $240.74 | $1,444.44 | $80.08 | $213.53 |
| HUM | 2 | $401.64 | $387.19 | $774.39 | $-28.89 | $366.83 |
| IBKR | 10 | $95.61 | $90.43 | $904.30 | $-51.76 | $87.64 |
| JBHT | 3 | $277.72 | $278.70 | $836.10 | $2.93 | $252.76 |
| MPC | 3 | $306.56 | $308.95 | $926.85 | $7.17 | $287.83 |
| NTAP | 5 | $161.48 | $171.64 | $858.20 | $50.82 | $152.80 |
| PSX | 5 | $215.50 | $207.20 | $1,036.00 | $-41.48 | $191.32 |
| SPY | 5 | $743.10 | $740.84 | $3,704.20 | $-11.30 | — |
| STT | 8 | $185.86 | $181.18 | $1,449.40 | $-37.47 | $168.04 |
| UNH | 3 | $425.21 | $429.37 | $1,288.10 | $12.48 | $393.25 |
| VLO | 3 | $304.72 | $301.16 | $903.48 | $-10.68 | $283.28 |

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
