# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-29 16:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,286.30** |
| Total return since inception | -3.57% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,937.96 (-0.31%) |
| Positions value | $16,000.32 |
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
| DDOG | 3 | $260.67 | $263.29 | $789.87 | $7.87 | $236.93 |
| DOC | 32 | $22.25 | $22.64 | $724.48 | $12.46 | $20.55 |
| DVA | 6 | $227.39 | $241.17 | $1,447.02 | $82.66 | $215.55 |
| FTNT | 7 | $149.43 | $145.50 | $1,018.53 | $-27.50 | $131.17 |
| HUM | 3 | $391.16 | $362.88 | $1,088.64 | $-84.83 | $329.83 |
| JBHT | 3 | $277.72 | $272.56 | $817.68 | $-15.49 | $252.76 |
| MPC | 3 | $306.56 | $309.63 | $928.89 | $9.21 | $287.83 |
| NTAP | 5 | $161.48 | $173.26 | $866.30 | $58.92 | $157.11 |
| PSX | 5 | $215.50 | $208.53 | $1,042.65 | $-34.83 | $191.32 |
| SPY | 5 | $743.10 | $733.71 | $3,668.55 | $-46.95 | — |
| STT | 8 | $185.86 | $178.19 | $1,425.56 | $-61.31 | $168.04 |
| UNH | 3 | $425.21 | $424.36 | $1,273.08 | $-2.54 | $393.25 |
| VLO | 3 | $304.72 | $303.02 | $909.06 | $-5.10 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-641.19 | $0.00 | $95.51 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-28T17:58` no_trade skip_entry **TRV** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **CVS** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **FFIV** — insufficient investable cash (size $16, need >= $500)
- `2026-07-28T17:58` no_trade skip_entry **CNC** — insufficient investable cash (size $16, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
