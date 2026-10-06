# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-06 19:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,321.14** |
| Total return since inception | 1.61% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,851.57 (4.26%) |
| Positions value | $17,216.23 |
| Settled cash | $1,341.92 |
| Unsettled cash (T+1) | $1,777.46 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.06% | 4.07% |
| Annualized volatility | 11.21% | 11.30% |
| Sharpe (rf 4%) | 0.08 | 1.14 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 63 | 63 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $214.41 | $857.66 | $90.54 | $186.60 |
| APA | 19 | $44.15 | $44.24 | $840.56 | $1.67 | $39.73 |
| CRL | 3 | $296.67 | $306.40 | $919.20 | $29.18 | $279.86 |
| FFIV | 2 | $448.44 | $467.98 | $935.96 | $39.07 | $412.39 |
| IQV | 2 | $255.46 | $262.75 | $525.50 | $14.59 | $247.54 |
| MPC | 3 | $399.06 | $434.68 | $1,304.04 | $106.87 | $390.17 |
| NTAP | 5 | $206.27 | $229.50 | $1,147.53 | $116.18 | $203.86 |
| PSX | 5 | $215.50 | $271.42 | $1,357.08 | $279.60 | $246.58 |
| RVTY | 9 | $122.75 | $153.00 | $1,377.00 | $272.28 | $141.67 |
| SPY | 5 | $743.10 | $780.15 | $3,900.75 | $185.25 | — |
| TECH | 12 | $72.32 | $72.45 | $869.40 | $1.56 | $65.36 |
| VLO | 3 | $392.61 | $421.95 | $1,265.85 | $88.03 | $377.45 |
| WST | 2 | $370.69 | $374.34 | $748.68 | $7.30 | $339.09 |
| ZBRA | 3 | $345.13 | $389.01 | $1,167.03 | $131.65 | $338.33 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-06T19:00` no_trade skip_entry **WAT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **TMO** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **MSFT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **A** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **PLTR** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **WDAY** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **FTNT** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` no_trade skip_entry **MU** — insufficient investable cash (size $311, need >= $500)
- `2026-10-06T19:00` exit sell **TGT** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-10-06T19:00` exit sell **BBY** — trailing stop 10%
- `2026-10-06T01:43` system — eod_complete
- `2026-10-02T23:11` system — eod_complete
- `2026-10-02T18:39` no_trade — no signals crossed action thresholds this hour
- `2026-10-02T18:39` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-01T23:22` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
