# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-28 15:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,388.38** |
| Total return since inception | -3.06% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,885.61 (-0.57%) |
| Positions value | $15,587.42 |
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
| DDOG | 3 | $260.67 | $251.63 | $754.89 | $-27.11 | $236.93 |
| DOC | 32 | $22.25 | $22.64 | $724.32 | $12.30 | $20.26 |
| DVA | 6 | $227.39 | $238.90 | $1,433.40 | $69.04 | $213.53 |
| HUM | 2 | $401.64 | $382.50 | $765.01 | $-38.27 | $366.83 |
| IBKR | 10 | $95.61 | $91.00 | $910.00 | $-46.06 | $87.64 |
| JBHT | 3 | $277.72 | $278.01 | $834.03 | $0.86 | $252.76 |
| MPC | 3 | $306.56 | $309.09 | $927.27 | $7.59 | $287.83 |
| NTAP | 5 | $161.48 | $173.31 | $866.53 | $59.15 | $152.80 |
| PSX | 5 | $215.50 | $206.59 | $1,032.95 | $-44.53 | $191.32 |
| SPY | 5 | $743.10 | $741.94 | $3,709.70 | $-5.80 | — |
| STT | 8 | $185.86 | $181.29 | $1,450.32 | $-36.55 | $168.04 |
| UNH | 3 | $425.21 | $426.75 | $1,280.24 | $4.62 | $393.25 |
| VLO | 3 | $304.72 | $299.59 | $898.77 | $-15.39 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-586.37 | $0.00 | $0.00 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-28T15:52` no_trade skip_entry **CSX** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **BBY** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **ADM** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **TRV** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **CVS** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **FFIV** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **CNC** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` no_trade skip_entry **FTNT** — insufficient investable cash (size $17, need >= $500)
- `2026-07-28T15:52` exit sell **TRGP** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-07-28T15:52` exit sell **CNC** — trailing stop 10%
- `2026-07-28T15:52` exit sell **FTNT** — trailing stop 10%
- `2026-07-27T20:06` system — eod_complete
- `2026-07-27T20:06` system **DOC** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-27T20:06` system — corporate_actions_synced
- `2026-07-27T18:08` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
