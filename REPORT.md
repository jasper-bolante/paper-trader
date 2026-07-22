# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-22 15:21 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,848.68** |
| Total return since inception | -0.76% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,130.53 (0.65%) |
| Positions value | $18,464.75 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $13.89 |
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
| CNC | 13 | $66.94 | $66.84 | $868.92 | $-1.32 | $61.84 |
| DDOG | 3 | $260.67 | $247.59 | $742.77 | $-39.23 | $236.93 |
| DVA | 6 | $227.39 | $233.57 | $1,401.45 | $37.09 | $213.53 |
| FFIV | 3 | $430.59 | $404.39 | $1,213.17 | $-78.60 | $388.22 |
| FTNT | 5 | $155.14 | $155.22 | $776.10 | $0.42 | $150.16 |
| HUM | 2 | $401.64 | $400.60 | $801.19 | $-2.09 | $366.83 |
| IBKR | 10 | $95.61 | $93.56 | $935.65 | $-20.41 | $87.64 |
| MPC | 3 | $306.56 | $320.07 | $960.21 | $40.53 | $287.83 |
| NTAP | 5 | $161.48 | $166.67 | $833.35 | $25.97 | $149.12 |
| PSX | 5 | $215.50 | $212.57 | $1,062.88 | $-14.61 | $191.32 |
| SPY | 5 | $743.10 | $749.15 | $3,745.77 | $30.27 | — |
| STT | 8 | $185.86 | $183.99 | $1,471.92 | $-14.95 | $168.04 |
| TRGP | 5 | $282.92 | $282.77 | $1,413.85 | $-0.76 | $254.49 |
| UNH | 3 | $425.21 | $433.77 | $1,301.31 | $25.69 | $393.25 |
| VLO | 3 | $304.72 | $312.07 | $936.21 | $22.05 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-22T15:21` entry buy **PSX** — momentum entry: rank 14, mom 0.336, vol 34%
- `2026-07-22T15:21` entry buy **TRGP** — momentum entry: rank 10, mom 0.382, vol 28%
- `2026-07-22T15:21` no_trade skip_entry **WST** — sector cap: Health Care would exceed 25% of equity
- `2026-07-22T15:21` no_trade skip_entry **CVS** — sector cap: Health Care would exceed 25% of equity
- `2026-07-21T20:46` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
