# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-21 18:12 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,572.55** |
| Total return since inception | 2.86% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,740.95 (3.70%) |
| Positions value | $18,618.98 |
| Settled cash | $1,130.16 |
| Unsettled cash (T+1) | $838.27 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.64% | 3.52% |
| Annualized volatility | 11.04% | 11.07% |
| Sharpe (rf 4%) | 0.20 | 0.77 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 74 | 74 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.85 | $947.15 | $108.26 | $44.90 |
| CRL | 3 | $296.67 | $344.88 | $1,034.65 | $144.63 | $283.90 |
| EL | 10 | $105.95 | $104.12 | $1,041.20 | $-18.28 | $95.47 |
| FFIV | 2 | $448.44 | $456.79 | $913.58 | $16.69 | $431.75 |
| IQV | 2 | $255.46 | $273.98 | $547.95 | $37.04 | $247.54 |
| MPC | 3 | $399.06 | $469.12 | $1,407.38 | $210.20 | $436.32 |
| NTAP | 4 | $214.92 | $216.67 | $866.68 | $7.01 | $193.37 |
| PLTR | 5 | $194.57 | $199.48 | $997.40 | $24.54 | $175.08 |
| PSX | 5 | $215.50 | $289.36 | $1,446.80 | $369.32 | $267.61 |
| RVTY | 9 | $122.75 | $157.14 | $1,414.26 | $309.54 | $141.67 |
| SPY | 5 | $743.10 | $773.92 | $3,869.62 | $154.12 | — |
| TECH | 12 | $72.32 | $72.60 | $871.20 | $3.36 | $65.36 |
| VLO | 3 | $392.61 | $431.28 | $1,293.84 | $116.02 | $413.91 |
| WST | 2 | $370.69 | $395.22 | $790.44 | $49.06 | $349.94 |
| ZBRA | 3 | $345.13 | $392.27 | $1,176.82 | $141.44 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,184.63 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-21T18:12` no_trade skip_entry **IT** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CRM** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CNC** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **WDAY** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **NOW** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **HUM** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **VEEV** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **FTNT** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` exit sell **DDOG** — momentum rank decayed (None > 150 or ineligible: volatility 0.5136731923759654 above cap 0.5)
- `2026-10-20T21:48` system — eod_complete
- `2026-10-20T21:48` system — corporate_actions_synced
- `2026-10-20T18:05` entry buy **EL** — momentum entry: rank 20, mom 0.290, vol 36%
- `2026-10-20T18:05` no_trade skip_entry **CRM** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
