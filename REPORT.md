# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-20 18:05 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,337.26** |
| Total return since inception | 1.69% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,635.98 (3.18%) |
| Positions value | $19,209.92 |
| Settled cash | $1,130.16 |
| Unsettled cash (T+1) | $12.04 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.83% | 3.00% |
| Annualized volatility | 11.02% | 11.12% |
| Sharpe (rf 4%) | -0.05 | 0.63 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 73 | 73 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.74 | $945.06 | $106.17 | $44.78 |
| CRL | 3 | $296.67 | $312.97 | $938.91 | $48.89 | $279.86 |
| DDOG | 3 | $264.28 | $257.31 | $771.93 | $-20.92 | $234.24 |
| EL | 10 | $105.95 | $105.89 | $1,058.90 | $-0.58 | $95.30 |
| FFIV | 2 | $448.44 | $453.45 | $906.90 | $10.01 | $431.75 |
| IQV | 2 | $255.46 | $266.53 | $533.06 | $22.15 | $247.54 |
| MPC | 3 | $399.06 | $475.02 | $1,425.06 | $227.89 | $436.32 |
| NTAP | 4 | $214.92 | $210.06 | $840.24 | $-19.43 | $193.37 |
| PLTR | 5 | $194.57 | $195.68 | $978.38 | $5.51 | $175.08 |
| PSX | 5 | $215.50 | $290.72 | $1,453.60 | $376.12 | $267.61 |
| RVTY | 9 | $122.75 | $156.74 | $1,410.66 | $305.94 | $141.67 |
| SPY | 5 | $743.10 | $769.40 | $3,847.00 | $131.50 | — |
| TECH | 12 | $72.32 | $72.56 | $870.72 | $2.88 | $65.36 |
| VLO | 3 | $392.61 | $434.53 | $1,303.59 | $125.77 | $413.91 |
| WST | 2 | $370.69 | $388.14 | $776.28 | $34.90 | $345.65 |
| ZBRA | 3 | $345.13 | $383.21 | $1,149.63 | $114.25 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,218.01 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-20T18:05` entry buy **EL** — momentum entry: rank 20, mom 0.290, vol 36%
- `2026-10-20T18:05` no_trade skip_entry **CRM** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **NOW** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **WDAY** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **HUM** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **FTNT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-19T23:01` system — eod_complete
- `2026-10-19T23:01` system — corporate_actions_synced
- `2026-10-19T19:26` entry buy **PLTR** — momentum entry: rank 7, mom 0.620, vol 39%
- `2026-10-19T19:26` no_trade skip_entry **TMO** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CNC** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CRM** — insufficient investable cash (size $461, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
