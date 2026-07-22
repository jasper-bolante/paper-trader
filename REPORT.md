# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-22 16:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,828.57** |
| Total return since inception | -0.86% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,130.53 (0.65%) |
| Positions value | $18,444.64 |
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
| CNC | 13 | $66.94 | $66.50 | $864.44 | $-5.80 | $61.84 |
| DDOG | 3 | $260.67 | $246.55 | $739.65 | $-42.35 | $236.93 |
| DVA | 6 | $227.39 | $232.54 | $1,395.24 | $30.88 | $213.53 |
| FFIV | 3 | $430.59 | $403.18 | $1,209.54 | $-82.23 | $388.22 |
| FTNT | 5 | $155.14 | $155.30 | $776.50 | $0.82 | $150.16 |
| HUM | 2 | $401.64 | $397.85 | $795.69 | $-7.59 | $366.83 |
| IBKR | 10 | $95.61 | $93.64 | $936.40 | $-19.66 | $87.64 |
| MPC | 3 | $306.56 | $318.86 | $956.58 | $36.90 | $287.83 |
| NTAP | 5 | $161.48 | $166.91 | $834.52 | $27.14 | $149.12 |
| PSX | 5 | $215.50 | $212.27 | $1,061.35 | $-16.13 | $191.32 |
| SPY | 5 | $743.10 | $749.94 | $3,749.70 | $34.20 | — |
| STT | 8 | $185.86 | $184.73 | $1,477.84 | $-9.03 | $168.04 |
| TRGP | 5 | $282.92 | $282.99 | $1,414.95 | $0.34 | $254.49 |
| UNH | 3 | $425.21 | $432.87 | $1,298.60 | $22.98 | $393.25 |
| VLO | 3 | $304.72 | $311.21 | $933.64 | $19.49 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-22T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-22T16:57` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
