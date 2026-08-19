# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 19:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,736.07** |
| Total return since inception | -1.32% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,111.32 |
| Settled cash | $1,366.98 |
| Unsettled cash (T+1) | $1,266.14 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.75% | 3.08% |
| Annualized volatility | 12.31% | 13.37% |
| Sharpe (rf 4%) | -0.80 | 1.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 30 | 30 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.64 | $745.78 | $-17.83 | $25.00 |
| BBY | 14 | $88.05 | $89.14 | $1,247.96 | $15.21 | $79.24 |
| CNC | 8 | $75.27 | $64.57 | $516.56 | $-85.57 | $58.73 |
| CRL | 2 | $285.12 | $290.16 | $580.32 | $10.08 | $258.00 |
| CSX | 17 | $50.29 | $50.67 | $861.39 | $6.44 | $46.01 |
| EXPE | 2 | $331.47 | $328.52 | $657.05 | $-5.89 | $298.17 |
| FTNT | 7 | $149.43 | $152.76 | $1,069.36 | $23.32 | $151.44 |
| MPC | 3 | $306.56 | $361.24 | $1,083.72 | $164.04 | $330.10 |
| NTAP | 5 | $161.48 | $196.12 | $980.62 | $173.25 | $186.39 |
| PANW | 2 | $388.28 | $358.78 | $717.56 | $-59.00 | $349.27 |
| PSX | 5 | $215.50 | $242.22 | $1,211.08 | $133.60 | $219.13 |
| SPY | 5 | $743.10 | $769.58 | $3,847.90 | $132.40 | — |
| STT | 8 | $185.86 | $186.21 | $1,489.64 | $2.77 | $173.64 |
| VLO | 3 | $304.72 | $346.34 | $1,039.02 | $124.86 | $315.01 |
| WST | 3 | $336.32 | $354.45 | $1,063.37 | $54.40 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-983.43 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-19T19:03` no_trade skip_entry **WSM** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **NUE** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **APA** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **TGT** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **BKNG** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **TECH** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **IQV** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **VEEV** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` exit sell **NUE** — trailing stop 10%
- `2026-08-19T17:52` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T17:52` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T16:57` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T15:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T15:59` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
