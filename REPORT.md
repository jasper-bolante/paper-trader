# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-21 20:46 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,961.03** |
| Total return since inception | -0.19% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,130.53 (0.65%) |
| Positions value | $16,085.01 |
| Settled cash | $1,486.06 |
| Unsettled cash (T+1) | $2,395.63 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.26% | 0.48% |
| Annualized volatility | 8.85% | 11.19% |
| Sharpe (rf 4%) | -1.25 | 0.88 |
| Max drawdown | 1.74% | 1.73% |
| EOD observations | 10 | 10 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $67.62 | $879.06 | $8.82 | $61.84 |
| DDOG | 3 | $260.67 | $254.81 | $764.43 | $-17.57 | $236.93 |
| DVA | 6 | $227.39 | $237.25 | $1,423.53 | $59.17 | $213.53 |
| FFIV | 3 | $430.59 | $408.66 | $1,225.98 | $-65.79 | $388.22 |
| FTNT | 5 | $155.14 | $158.08 | $790.40 | $14.72 | $150.16 |
| HUM | 2 | $401.64 | $404.36 | $808.72 | $5.44 | $366.83 |
| IBKR | 10 | $95.61 | $94.35 | $943.50 | $-12.56 | $87.64 |
| MPC | 3 | $306.56 | $319.81 | $959.44 | $39.76 | $287.83 |
| NTAP | 5 | $161.48 | $165.69 | $828.45 | $21.07 | $149.12 |
| SPY | 5 | $743.10 | $747.95 | $3,739.75 | $24.25 | — |
| STT | 8 | $185.86 | $183.33 | $1,466.64 | $-20.23 | $168.04 |
| UNH | 3 | $425.21 | $436.94 | $1,310.82 | $35.20 | $393.25 |
| VLO | 3 | $304.72 | $314.76 | $944.28 | $30.12 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-21T18:51` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T18:51` no_trade skip_entry **DOC** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **CSX** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **MGM** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **PSX** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **JBHT** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **CVS** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **WST** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **TRGP** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T16:57` no_trade skip_entry **DOC** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **CSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **MGM** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **PSX** — insufficient investable cash (size $482, need >= $500)
- `2026-07-21T16:57` no_trade skip_entry **JBHT** — insufficient investable cash (size $482, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
