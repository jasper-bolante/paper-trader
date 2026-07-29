# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-29 19:54 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,301.35** |
| Total return since inception | -3.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,937.96 (-0.31%) |
| Positions value | $16,015.37 |
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
| DDOG | 3 | $260.67 | $265.73 | $797.19 | $15.19 | $236.93 |
| DOC | 32 | $22.25 | $22.49 | $719.68 | $7.66 | $20.55 |
| DVA | 6 | $227.39 | $239.90 | $1,439.40 | $75.04 | $215.55 |
| FTNT | 7 | $149.43 | $154.37 | $1,080.59 | $34.55 | $131.17 |
| HUM | 3 | $391.16 | $363.86 | $1,091.58 | $-81.89 | $329.83 |
| JBHT | 3 | $277.72 | $275.65 | $826.95 | $-6.22 | $252.76 |
| MPC | 3 | $306.56 | $308.55 | $925.65 | $5.97 | $287.83 |
| NTAP | 5 | $161.48 | $173.48 | $867.40 | $60.02 | $157.11 |
| PSX | 5 | $215.50 | $206.73 | $1,033.65 | $-43.83 | $191.32 |
| SPY | 5 | $743.10 | $730.79 | $3,653.95 | $-61.55 | — |
| STT | 8 | $185.86 | $175.92 | $1,407.36 | $-79.51 | $168.04 |
| UNH | 3 | $425.21 | $421.18 | $1,263.54 | $-12.08 | $393.25 |
| VLO | 3 | $304.72 | $302.81 | $908.43 | $-5.73 | $283.28 |

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
