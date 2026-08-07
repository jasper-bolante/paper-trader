# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 14:34 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,214.41** |
| Total return since inception | -3.93% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,673.66 (3.37%) |
| Positions value | $16,556.38 |
| Settled cash | $1,218.43 |
| Unsettled cash (T+1) | $1,446.40 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -4.22% | 3.19% |
| Annualized volatility | 11.48% | 15.02% |
| Sharpe (rf 4%) | -4.79 | 2.31 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 22 | 22 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.27 | $763.56 | $-0.05 | $24.54 |
| BBY | 14 | $88.05 | $81.58 | $1,142.12 | $-90.63 | $79.24 |
| CSCO | 8 | $131.57 | $120.31 | $962.48 | $-90.11 | $108.28 |
| CSX | 17 | $50.29 | $50.27 | $854.67 | $-0.28 | $46.01 |
| DDOG | 3 | $268.94 | $238.31 | $714.93 | $-91.89 | $211.93 |
| FTNT | 7 | $149.43 | $160.92 | $1,126.44 | $80.40 | $151.44 |
| HPQ | 31 | $28.20 | $28.95 | $897.45 | $23.21 | $25.38 |
| MPC | 3 | $306.56 | $293.25 | $879.74 | $-39.94 | $287.83 |
| NTAP | 5 | $161.48 | $187.72 | $938.60 | $131.22 | $172.38 |
| PSX | 5 | $215.50 | $202.05 | $1,010.25 | $-67.23 | $191.32 |
| SPY | 5 | $743.10 | $772.62 | $3,863.10 | $147.60 | — |
| STT | 8 | $185.86 | $183.34 | $1,466.72 | $-20.15 | $168.31 |
| VLO | 3 | $304.72 | $293.77 | $881.31 | $-32.85 | $283.28 |
| WST | 3 | $336.32 | $351.67 | $1,055.01 | $46.05 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-819.48 | $0.00 | $324.57 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-07T14:34` entry buy **CSCO** — momentum entry: rank 8, mom 0.353, vol 36%
- `2026-08-07T14:34` entry buy **BAX** — momentum entry: rank 4, mom 0.473, vol 50%
- `2026-08-07T14:34` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T14:34` exit sell **DOC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T00:25` system — eod_complete
- `2026-08-06T16:00` entry buy **HPQ** — momentum entry: rank 5, mom 0.453, vol 44%
- `2026-08-06T16:00` entry buy **DDOG** — momentum entry: rank 1, mom 0.960, vol 46%
- `2026-08-06T15:59` exit sell **DDOG** — trailing stop 10%
- `2026-08-05T20:10` system — eod_complete
- `2026-08-05T18:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-05T18:07` no_trade skip_entry **CVS** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **TRV** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **NUE** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CSCO** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CNC** — insufficient investable cash (size $394, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
