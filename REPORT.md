# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-31 15:38 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,472.91** |
| Total return since inception | -2.64% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,986.27 (-0.07%) |
| Positions value | $18,485.06 |
| Settled cash | $990.39 |
| Unsettled cash (T+1) | $4.26 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.79% | -0.24% |
| Annualized volatility | 9.70% | 14.62% |
| Sharpe (rf 4%) | -4.96 | -0.47 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 17 | 17 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $86.53 | $1,211.42 | $-21.33 | $79.24 |
| CSX | 17 | $50.29 | $50.28 | $854.76 | $-0.19 | $45.25 |
| DDOG | 3 | $260.67 | $269.70 | $809.12 | $27.12 | $241.84 |
| DOC | 32 | $22.25 | $21.86 | $699.68 | $-12.34 | $20.55 |
| DVA | 6 | $227.39 | $237.59 | $1,425.54 | $61.18 | $216.78 |
| FTNT | 7 | $149.43 | $159.00 | $1,112.97 | $66.93 | $138.79 |
| HUM | 3 | $391.16 | $370.38 | $1,111.14 | $-62.33 | $330.02 |
| MPC | 3 | $306.56 | $311.96 | $935.89 | $16.22 | $287.83 |
| NTAP | 5 | $161.48 | $177.27 | $886.35 | $78.97 | $157.11 |
| PSX | 5 | $215.50 | $209.67 | $1,048.35 | $-29.13 | $191.32 |
| SPY | 5 | $743.10 | $742.26 | $3,711.30 | $-4.20 | — |
| STT | 8 | $185.86 | $184.88 | $1,479.00 | $-7.87 | $168.04 |
| UNH | 3 | $425.21 | $420.81 | $1,262.43 | $-13.19 | $393.25 |
| VLO | 3 | $304.72 | $307.81 | $923.44 | $9.28 | $283.28 |
| WST | 3 | $336.32 | $337.89 | $1,013.67 | $4.71 | $305.31 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-679.45 | $0.00 | $95.51 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-31T15:38` entry buy **CSX** — momentum entry: rank 11, mom 0.334, vol 26%
- `2026-07-31T15:38` no_trade skip_entry **VTRS** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **BNY** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **ADM** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **UNP** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **WELL** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **TRV** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **URI** — insufficient investable cash (size $10, need >= $500)
- `2026-07-31T15:38` no_trade skip_entry **CVS** — sector cap: Health Care would exceed 25% of equity
- `2026-07-31T15:38` system **VLO** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-30T20:44` system — eod_complete
- `2026-07-30T20:44` system **WST** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-30T20:44` system — corporate_actions_synced
- `2026-07-30T18:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-30T18:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
