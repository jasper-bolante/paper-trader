# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-29 21:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,286.69** |
| Total return since inception | -3.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,593.59 (-2.03%) |
| Positions value | $16,000.70 |
| Settled cash | $1,668.58 |
| Unsettled cash (T+1) | $1,623.56 |
| Tax reserve | $6.16 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.63% | -2.20% |
| Annualized volatility | 8.94% | 12.30% |
| Sharpe (rf 4%) | -7.35 | -3.31 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 16 | 16 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| DDOG | 3 | $260.67 | $264.38 | $793.14 | $11.14 | $237.94 |
| DOC | 32 | $22.25 | $22.49 | $719.68 | $7.66 | $20.55 |
| DVA | 6 | $227.39 | $240.87 | $1,445.22 | $80.86 | $216.78 |
| FTNT | 7 | $149.43 | $153.44 | $1,074.08 | $28.04 | $138.10 |
| HUM | 3 | $391.16 | $365.51 | $1,096.53 | $-76.94 | $329.83 |
| JBHT | 3 | $277.72 | $276.08 | $828.25 | $-4.92 | $252.76 |
| MPC | 3 | $306.56 | $309.10 | $927.30 | $7.62 | $287.83 |
| NTAP | 5 | $161.48 | $173.25 | $866.25 | $58.87 | $157.11 |
| PSX | 5 | $215.50 | $206.80 | $1,034.00 | $-43.48 | $191.32 |
| SPY | 5 | $743.10 | $728.00 | $3,640.00 | $-75.50 | — |
| STT | 8 | $185.86 | $175.91 | $1,407.28 | $-79.59 | $168.04 |
| UNH | 3 | $425.21 | $420.66 | $1,261.98 | $-13.64 | $393.25 |
| VLO | 3 | $304.72 | $302.33 | $906.99 | $-7.17 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-641.19 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-29T19:54` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T19:54` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T18:33` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T18:33` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T16:52` no_trade — no signals crossed action thresholds this hour
- `2026-07-29T16:52` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-29T15:32` entry buy **HUM** — momentum entry: rank 4, mom 0.701, vol 33%
- `2026-07-29T15:32` entry buy **FTNT** — momentum entry: rank 2, mom 1.006, vol 35%
- `2026-07-29T15:31` exit sell **IBKR** — trailing stop 10%
- `2026-07-29T15:31` exit sell **HUM** — trailing stop 10%
- `2026-07-28T20:03` system — eod_complete
- `2026-07-28T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-07-28T17:58` no_trade skip_entry **CSX** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **BBY** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **ADM** — insufficient investable cash (size $16, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
