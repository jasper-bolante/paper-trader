# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-29 15:32 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,296.33** |
| Total return since inception | -3.52% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,937.96 (-0.31%) |
| Positions value | $16,010.35 |
| Settled cash | $1,668.58 |
| Unsettled cash (T+1) | $1,623.56 |
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
| DDOG | 3 | $260.67 | $256.67 | $770.01 | $-11.99 | $236.93 |
| DOC | 32 | $22.25 | $22.74 | $727.68 | $15.66 | $20.55 |
| DVA | 6 | $227.39 | $241.39 | $1,448.34 | $83.98 | $215.55 |
| FTNT | 7 | $149.43 | $145.75 | $1,020.22 | $-25.82 | $131.17 |
| HUM | 3 | $391.16 | $366.48 | $1,099.44 | $-74.03 | $329.83 |
| JBHT | 3 | $277.72 | $271.35 | $814.05 | $-19.12 | $252.76 |
| MPC | 3 | $306.56 | $308.55 | $925.63 | $5.96 | $287.83 |
| NTAP | 5 | $161.48 | $172.71 | $863.55 | $56.17 | $157.11 |
| PSX | 5 | $215.50 | $208.58 | $1,042.90 | $-34.58 | $191.32 |
| SPY | 5 | $743.10 | $734.59 | $3,672.95 | $-42.55 | — |
| STT | 8 | $185.86 | $179.61 | $1,436.88 | $-49.99 | $168.04 |
| UNH | 3 | $425.21 | $426.26 | $1,278.80 | $3.18 | $393.25 |
| VLO | 3 | $304.72 | $303.30 | $909.90 | $-4.26 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-641.19 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-29T15:32` entry buy **HUM** — momentum entry: rank 4, mom 0.701, vol 33%
- `2026-07-29T15:32` entry buy **FTNT** — momentum entry: rank 2, mom 1.006, vol 35%
- `2026-07-29T15:31` exit sell **IBKR** — trailing stop 10%
- `2026-07-29T15:31` exit sell **HUM** — trailing stop 10%
- `2026-07-28T20:03` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
